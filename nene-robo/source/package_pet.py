"""Verify and package the local Nene Robo 1.0.0 deliverable."""
from pathlib import Path
from PIL import Image
import io
import json
import zipfile
import hashlib
import datetime

pet = Path(__file__).resolve().parent.parent
source = pet / "source"
output = pet.parent / "release-assets/nene-robo-v1.0.0"
for name, key, value in [("qa/final-visual-qa.json", "visual_qa", "pass"),
                         ("qa/direction-blind-validation.json", "ok", True),
                         ("qa/chroma-despill-extended.json", "ok", True)]:
    assert json.loads((source / name).read_text(encoding="utf-8"))[key] == value
assert json.loads((pet / "preview/app-loader-validation.json").read_text(encoding="utf-8"))["ok"]
validation = json.loads((pet / "validation.json").read_text(encoding="utf-8"))
assert validation["ok"] and not validation["errors"] and not validation["warnings"]
assert (pet / "spritesheet.webp").read_bytes() == (source / "final/spritesheet-extended.webp").read_bytes()
with Image.open(source / "final/spritesheet-extended-before-despill.png") as before, Image.open(source / "final/spritesheet-extended.png") as after:
    assert before.getchannel("A").tobytes() == after.getchannel("A").tobytes()

counts = dict(zip(["idle", "running-right", "running-left", "waving", "jumping", "failed", "waiting", "running", "review", "look-directions"], [6, 8, 8, 4, 5, 8, 6, 6, 6, 16]))
previews = {}
for name in [*counts, "animation-overview"]:
    with Image.open(pet / "preview" / f"{name}.gif") as image:
        assert image.size == ((576, 678) if name == "animation-overview" else (192, 208))
        if name in counts:
            assert image.n_frames == counts[name], name
        duration = 0
        for frame in range(image.n_frames):
            image.seek(frame)
            image.load()
            duration += image.info["duration"]
        if name == "animation-overview":
            assert image.n_frames > 1 and duration == 1680
        previews[name] = {"size": image.size, "frames": image.n_frames, "duration_ms": duration}
(pet / "preview/preview-files-check.json").write_text(json.dumps(previews, indent=2) + "\n", encoding="utf-8")

readme = (source / "qa/final-readme.md").read_text(encoding="utf-8")
names = ["pet.json", "spritesheet.webp", "README.md", "NOTICE.md", "validation.json"]
names += [file.relative_to(pet).as_posix() for file in sorted((pet / "preview").iterdir()) if file.is_file()]
contents = {name: readme.encode("utf-8") if name == "README.md" else (pet / name).read_bytes() for name in names}
stream = io.BytesIO()
with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as package:
    for name, data in contents.items():
        package.writestr(f"nene-robo/{name}", data)
payload = stream.getvalue()
with zipfile.ZipFile(io.BytesIO(payload)) as package:
    assert package.testzip() is None
    assert set(package.namelist()) == {f"nene-robo/{name}" for name in contents}
    for name, data in contents.items():
        assert package.read(f"nene-robo/{name}") == data

output.mkdir(parents=True, exist_ok=True)
archive = output / "nene-robo-v1.0.0.zip"
assert not archive.exists(), "Preserve the existing package before making a new candidate."
(pet / "README.md").write_text(readme, encoding="utf-8", newline="\n")
archive.write_bytes(payload)
with zipfile.ZipFile(archive) as package:
    assert package.testzip() is None
    for name in names:
        assert package.read(f"nene-robo/{name}") == (pet / name).read_bytes()
checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
sprite_hash = hashlib.sha256((pet / "spritesheet.webp").read_bytes()).hexdigest()
assert sprite_hash == "257ffd5cce157acf911c87d93385ce6325505be5a8c3c68f1b48b1a00ece54bb"
(output / "SHA256SUMS.txt").write_text(f"{checksum}  {archive.name}\n", encoding="utf-8")
report = {"ok": True, "archive": str(archive), "size": len(payload), "sha256": checksum,
          "sprite_sha256": sprite_hash, "entry_count": len(names), "entries": names,
          "source_and_package_identical": True, "application_ui_detection_verified": False,
          "floating_display_verified": False}
(output / "package-check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(source / "qa/run-summary.json").write_text(json.dumps({"ok": True, "pet_id": "nene-robo", "spriteVersionNumber": 2,
    "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "package": report,
    "gates": ["standard visual QA", "fixed-scale direction registration/edges", "16direction independent semantics",
              "single despill alpha unchanged", "v2 atlas validation", "3isolated blind workers/cardinal majority",
              "independent final visual QA", "standalone app validator replay", "all GIF frames and ZIP content"],
    "accepted_warnings": "see final-visual-qa.json and blind-review-resolution.json"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
