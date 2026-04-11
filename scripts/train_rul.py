"""
ROADAI XGBoost / GradientBoosting RUL Training Script
======================================================
Run: python scripts/train_rul.py

Trains on synthetic data based on road engineering (AASHTO-inspired).
Saves: models/runtime/rul_model.pkl + rul_scaler.pkl
"""
import numpy as np, pickle, os
from pathlib import Path

os.makedirs("models/runtime", exist_ok=True)
print("Generating synthetic RUL dataset (N=6000)...")
np.random.seed(42)
N = 6000
health      = np.random.uniform(0, 100, N)
potholes    = np.random.poisson(np.clip((100-health)/20, 0, 15), N).astype(float)
cracks      = np.random.poisson(np.clip((100-health)/12, 0, 25), N).astype(float)
coverage    = np.random.uniform(0, np.clip((100-health)/8, 0, 20), N)
avg_depth   = np.clip(np.random.normal((100-health)/150, 0.1, N), 0, 1)
weather_code= np.random.randint(0, 5, N).astype(float)
total_damage= potholes + cracks
active_lane = np.clip(np.random.poisson(potholes*0.3, N), 0, 8).astype(float)
base_rul = np.where(health>=85,12.,np.where(health>=70,8.,np.where(health>=55,5.,np.where(health>=40,2.5,np.where(health>=25,1.,0.25)))))
rul = np.clip(base_rul - potholes*0.35 - cracks*0.12 - coverage*0.06 - avg_depth*1.5 - weather_code*0.15 + np.random.normal(0,0.3,N), 0.1, 20.0)
X = np.column_stack([health, potholes, cracks, coverage, avg_depth, weather_code, total_damage, active_lane])
y = rul
print(f"Dataset shape: {X.shape}, RUL range: {y.min():.2f}–{y.max():.2f} yrs")

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
X_tr,X_te,y_tr,y_te = train_test_split(X,y,test_size=0.2,random_state=42)
sc = StandardScaler()
Xs_tr = sc.fit_transform(X_tr); Xs_te = sc.transform(X_te)

try:
    import xgboost as xgb
    model = xgb.XGBRegressor(n_estimators=300,max_depth=6,learning_rate=0.05,subsample=0.8,colsample_bytree=0.8,random_state=42,n_jobs=-1,verbosity=0)
    name = "XGBoost"
except ImportError:
    from sklearn.ensemble import GradientBoostingRegressor
    model = GradientBoostingRegressor(n_estimators=250,max_depth=5,learning_rate=0.05,subsample=0.85,random_state=42)
    name = "GradientBoosting (sklearn)"

print(f"Training {name}...")
model.fit(Xs_tr, y_tr)
preds = model.predict(Xs_te)
print(f"✅ {name} — MAE: {mean_absolute_error(y_te,preds):.3f} yrs  R²: {r2_score(y_te,preds):.4f}")
with open("models/runtime/rul_model.pkl","wb") as f: pickle.dump(model,f)
with open("models/runtime/rul_scaler.pkl","wb") as f: pickle.dump(sc,f)
print("✅ Saved to models/runtime/rul_model.pkl + rul_scaler.pkl")
print("Restart ROADAI backend to activate ML RUL engine.")
