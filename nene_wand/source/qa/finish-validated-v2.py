"""Create review media from the validated replacement output, with no cleanup."""
import json
import subprocess
import sys
from pathlib import Path

run = Path(__file__).resolve().parents[1]
scripts = Path.home() / ".codex/skills/hatch-pet/scripts"
assert json.loads((run / "final/validation-extended-fixed.json").read_text())["ok"]
atlas = run / "final/spritesheet-extended-fixed.webp"
preview = run.parent / "preview"
preview.mkdir(exist_ok=True)
def native(name, *args):
    subprocess.run([sys.executable, str(scripts / name), *map(str, args)], check=True)
native("make_contact_sheet.py", atlas, "--output", preview / "contact-sheet.png")
native("make_direction_qa_sheet.py", atlas, "--output", preview / "look-directions.png")
native("make_direction_blind_qa_sheet.py", atlas, "--output", run / "qa/direction-blind-pairs.png", "--answer-key", run / "qa/direction-blind-answer-key.json")
native("measure_direction_continuity.py", atlas, "--json-out", run / "qa/look-continuity.json")
for helper in ("render-final-previews.py", "check-preview-files.py", "prepare-blind-display.py"):
    subprocess.run([sys.executable, str(run / "qa" / helper)], check=True)
