import os
import sys
import json
from pathlib import Path

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.core.model_registry import ModelRegistry
from backend.core.benchmark_engine import BenchmarkEngine
from backend.core.runtime_selector import RuntimeModelSelector
from backend.utils.logger import get_logger

logger = get_logger("benchmark_runner")

def run_manual_benchmarks():
    print("🚀 Starting Manual Benchmark Run (PRD v4.1)...")
    
    # 1. Initialize Components
    registry = ModelRegistry()
    registry.scan_all_models()
    selector = RuntimeModelSelector(registry)
    engine = BenchmarkEngine(registry)
    
    # 2. Run Benchmarks (n_segments=5 as per PRD default)
    print("⚙️  Evaluating models (pothole/crack recall, mAP, FPS, robustness)...")
    results = engine.run_all(n_segments=5)
    
    # 3. Persist Results (so they show up in the API/Dashboard)
    results_path = Path("config/benchmark_results.json")
    results_path.parent.mkdir(exist_ok=True)
    results_path.write_text(json.dumps(results, indent=2))
    print(f"✅ Results persisted to {results_path}")
    
    # 4. Update winner tracking
    try:
        winner = selector.select_and_deploy_winner()
        print(f"🏆 Benchmark Winner: {winner}")
    except Exception as e:
        print(f"⚠️  Winner tracking failed (expected for virtual refs): {e}")

    print("\n📊 Benchmark Summary:")
    for r in results:
        print(f"  - {r['model_name']}: Composite Score = {r['composite_score']} | FPS = {r['fps']}")

if __name__ == "__main__":
    run_manual_benchmarks()
