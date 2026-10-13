"""Build and verify the v1.0.0 desktop pet release without altering artwork."""
import hashlib
import json
from pathlib import Path
import zipfile

from PIL import Image

root = Path(__file__).resolve().parent.parent
pet = root / "nene-initial-uniform"
output = root / "release-assets/v1.0.0"
output.mkdir(parents=True, exist_ok=True)
manifest = json.loads((pet / "pet.json").read_text(encoding="utf-8"))
assert manifest["id"] == pet.name
assert manifest["spriteVersionNumber"] == 2
assert manifest["spritesheetPath"] == "spritesheet.webp"
sprite = pet / manifest["spritesheetPath"]
with Image.open(sprite) as image:
    assert image.format == "WEBP" and image.mode == "RGBA"
    assert image.size == (1536, 2288)
    image.load()
digest = lambda data: hashlib.sha256(data).hexdigest()
assert digest(sprite.read_bytes()) == "ec9c83870d127f707a5223d12067c0ae062fc7ece63b782ac9e0c7e4883d2b46"
validation = json.loads((pet / "validation.json").read_text(encoding="utf-8"))
assert validation["ok"] and not validation["errors"]
assert validation["transparent_rgb_residue_pixels"] == 0

frames = dict(zip(["idle", "running-right", "running-left", "waving", "jumping",
                   "failed", "waiting", "running", "review", "look-directions"],
                  [6, 8, 8, 4, 5, 8, 6, 6, 6, 16]))
for name, count in frames.items():
    with Image.open(pet / "preview" / f"{name}.gif") as image:
        assert image.size == (192, 208) and image.n_frames == count, name
        for frame in range(count):
            image.seek(frame)
            image.load()

with Image.open(pet / "preview/animation-overview.gif") as image:
    assert image.size == (576, 678) and image.n_frames == 17
    total_duration = 0
    for frame in range(image.n_frames):
        image.seek(frame)
        image.load()
        total_duration += image.info["duration"]
    assert total_duration == 1680  # Identical input frames are merged by the GIF encoder.
names = ["pet.json", "spritesheet.webp", "README.md", "NOTICE.md", "validation.json"]
names += [file.relative_to(pet).as_posix() for file in sorted((pet / "preview").iterdir())
          if file.suffix in {".gif", ".png", ".md"}]
archive = output / "nene-codex-pet-v1.0.0.zip"
with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
    for name in names:
        package.write(pet / name, f"{pet.name}/{name}")
with zipfile.ZipFile(archive) as package:
    assert package.testzip() is None
    assert package.namelist() == [f"{pet.name}/{name}" for name in names]
    for name in names:
        assert package.read(f"{pet.name}/{name}") == (pet / name).read_bytes(), name

checksum = digest(archive.read_bytes())
(output / "SHA256SUMS.txt").write_text(f"{checksum}  {archive.name}\n", encoding="utf-8")
report = {"ok": True, "version": "v1.0.0", "archive": archive.name,
          "size": archive.stat().st_size, "sha256": checksum,
          "sprite_sha256": digest(sprite.read_bytes()), "entries": names,
          "state_frames": frames, "application_ui_detection_verified": False,
          "floating_display_verified": False}
(output / "package-check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
