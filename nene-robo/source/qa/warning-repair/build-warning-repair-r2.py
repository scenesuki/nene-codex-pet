"""Assemble and verify the two coherent warning-repair rows, without promoting them."""
from pathlib import Path
from PIL import Image
import subprocess
import sys
import json
import hashlib

pet = Path(__file__).resolve().parents[2]
qa = pet / "source/qa/warning-repair-r2"
final = pet / "source/final"
skill = Path("C:/Users/tieha/.codex/skills/hatch-pet/scripts")
before = final / "spritesheet-warning-repair-r2-before-despill.png"
clean = final / "spritesheet-warning-repair-r2.png"
webp = final / "spritesheet-warning-repair-r2.webp"
assert not clean.exists(), "Retain an existing candidate; do not repeat cleanup."

def run(script, *arguments):
    subprocess.run([sys.executable, str(skill / script), *map(str, arguments)], check=True)

run("assemble_extended_atlas.py", "--base-atlas", final / "spritesheet.webp",
    "--registered-row-9", qa / "look-row-9-registered.png",
    "--row-9-registration", qa / "look-row-9-registration.json",
    "--look-row-10", pet / "source/decoded/look-row-10-warning-repair-r5.png",
    "--neutral-cell", pet / "source/frames/idle/00.png",
    "--chroma-key", "#FF00FF", "--chroma-threshold", "96", "--output", before,
    "--manifest-output", qa / "assembly.json")
run("despill_chroma_edges.py", before, "--output", clean, "--webp-output", webp,
    "--chroma-key", "#FF00FF", "--json-out", qa / "chroma-despill.json")
run("validate_atlas.py", webp, "--require-v2", "--chroma-key", "#FF00FF",
    "--json-out", qa / "validation.json")
run("make_contact_sheet.py", webp, "--output", qa / "contact-sheet.png", "--scale", "1")
run("make_direction_qa_sheet.py", webp, "--output", qa / "look-directions.png")
run("measure_direction_continuity.py", webp, "--json-out", qa / "look-continuity.json")
run("make_direction_blind_qa_sheet.py", webp, "--output", qa / "direction-blind-pairs.png",
    "--answer-key", qa / "direction-blind-answer-key.json")

with Image.open(before) as a, Image.open(clean) as b, Image.open(pet / "spritesheet.webp") as old:
    assert a.getchannel("A").tobytes() == b.getchannel("A").tobytes()
    assert old.convert("RGBA").crop((0, 0, 1536, 1872)).tobytes() == b.crop((0, 0, 1536, 1872)).tobytes()

renderer = pet.parent / "scripts/render_previews.py"
code = renderer.read_text(encoding="utf-8")
code = code.replace('/ "nene-initial-uniform"', '/ "nene-robo"')
code = code.replace('root / "spritesheet.webp"', 'root / "source/final/spritesheet-warning-repair-r2.webp"')
code = code.replace('output = root / "preview"', 'output = root / "source/qa/warning-repair-r2/previews"')
exec(compile(code, str(renderer), "exec"), {"__file__": str(renderer)})

gif_checks = {}
for path in sorted((qa / "previews").glob("*.gif")):
    with Image.open(path) as image:
        duration = 0
        for index in range(image.n_frames):
            image.seek(index)
            image.load()
            duration += image.info["duration"]
        gif_checks[path.name] = {"size": image.size, "frames": image.n_frames, "duration_ms": duration}
    if path.name != "look-directions.gif":
        assert path.read_bytes() == (pet / "preview" / path.name).read_bytes(), path.name
assert gif_checks["look-directions.gif"] == {"size": (192, 208), "frames": 16, "duration_ms": 3200}
with Image.open(qa / "previews/look-directions.gif") as image:
    decoded = Image.new("RGBA", (1536, 416), "#f2f2f2")
    for index in range(16):
        image.seek(index)
        decoded.alpha_composite(image.convert("RGBA"), ((index % 8) * 192, (index // 8) * 208))
    decoded.convert("RGB").save(qa / "look-gif-decoded.png")
(qa / "preview-files-check.json").write_text(json.dumps(gif_checks, indent=2) + "\n", encoding="utf-8")

old_metrics = json.loads((pet / "source/qa/look-continuity.json").read_text(encoding="utf-8"))
new_metrics = json.loads((qa / "look-continuity.json").read_text(encoding="utf-8"))
report = {"ok": True, "nine_standard_rows_pixel_identical": True, "cleanup_alpha_identical": True,
          "old_sprite_sha256": hashlib.sha256((pet / "spritesheet.webp").read_bytes()).hexdigest(),
          "candidate_sprite_sha256": hashlib.sha256(webp.read_bytes()).hexdigest(),
          "baseline_closing_pair": old_metrics["pairs"][-1],
          "candidate_closing_pair": new_metrics["pairs"][-1],
          "baseline_continuity_warnings": old_metrics["warnings"],
          "candidate_continuity_warnings": new_metrics["warnings"], "promoted": False}
(qa / "comparison.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
