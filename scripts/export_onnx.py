"""
ROADAI ONNX Export Script
==========================
Exports best.pt to ONNX format for TensorRT / ONNX Runtime acceleration.

Requirements: ultralytics installed, best.pt present
Usage: python scripts/export_onnx.py

TensorRT conversion (after ONNX export):
  trtexec --onnx=models/runtime/best.onnx --saveEngine=models/runtime/best.trt \
          --fp16 --workspace=4096
"""
from pathlib import Path
import sys
import shutil

# Make output dir
ONNX_DIR = Path("models/onnx")
ONNX_DIR.mkdir(parents=True, exist_ok=True)

MODELS_TO_EXPORT = [
    Path("models/custom/best.pt"),
    Path("models/candidates/yolov8n.pt"),
    Path("models/candidates/yolov8s.pt"),
    Path("models/candidates/yolov8m.pt")
]

try:
    from ultralytics import YOLO
    
    for pt_path in MODELS_TO_EXPORT:
        if not pt_path.exists():
            print(f"⚠️ {pt_path} not found, skipping...")
            continue
            
        print(f"🔄 Loading {pt_path.name}...")
        model = YOLO(str(pt_path))
        
        print(f"⚙️ Exporting {pt_path.name} to ONNX (dynamic batch)...")
        # Export model
        exported_file = model.export(format="onnx", opset=12, dynamic=True, half=False)
        
        # Move destination
        out_path = ONNX_DIR / f"{pt_path.stem}.onnx"
        if Path(exported_file).exists():
            shutil.move(exported_file, out_path)
            print(f"✅ Exported to {out_path}")
            
except ImportError:
    print("❌ ultralytics not installed. Run: pip install ultralytics")
except Exception as e:
    print(f"❌ Export failed: {e}")
