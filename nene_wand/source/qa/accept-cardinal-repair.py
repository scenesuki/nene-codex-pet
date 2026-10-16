"""Normalize a generated single cardinal using the native anchor extractor."""
import hashlib
import importlib.util
import json
import shutil
import sys
from pathlib import Path
from PIL import Image

run = Path(__file__).resolve().parents[1]
source = Path(sys.argv[1])
native = Path.home() / ".codex/skills/hatch-pet/scripts/extract_cardinal_anchors.py"
spec = importlib.util.spec_from_file_location("anchor_native", native)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
target = run / "decoded/look-anchors/270.png"
preserved = run / "decoded/look-anchors/270-r1-wrong-hand.png"
assert not preserved.exists(), "Repair already recorded"
raw = run / "decoded/look-anchor-270-repair.png"
shutil.copy2(source, raw)
image = mod.remove_chroma_background(Image.open(raw), (255, 0, 255), 96)
edge = mod.edge_alpha_count(image, 2)
assert edge <= 24 and mod.alpha_count(image) >= 400
shutil.copy2(target, preserved)
mod.fit_to_cell(image).save(target)
report = {"ok": True, "direction": "270", "source_path": str(source),
          "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
          "preserved_output": str(preserved), "raw_copy": str(raw),
          "edge_pixels": edge, "normalization": "native remove_chroma_background + fit_to_cell",
          "reason": "Original left-gaze anchor exchanged cane hand; regenerate anchor only before coherent row synthesis."}
(run / "qa/cardinal-270-repair.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
