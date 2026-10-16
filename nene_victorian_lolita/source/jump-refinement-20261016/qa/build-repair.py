"""Replace only the regenerated jump row; preserve every other cleaned pixel."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
from PIL import Image, ImageDraw

run = Path(__file__).resolve().parents[1]
pet = run.parent.parent
scripts = Path.home() / '.codex/skills/hatch-pet/scripts'
previous = pet / 'source/previous-distribution/nene_balloon-v1.7.0'

def native(name, *args):
    subprocess.run([sys.executable, '-B', str(scripts / name), *map(str, args)], check=True)

assert not (run / 'qa/chroma-despill-jump.json').exists(), 'One cleanup only for the new row'
subprocess.run([sys.executable, '-B', str(pet / 'source/qa/despill-validator-compatible.py'),
    str(run / 'final/jump-row-preclean.png'), '--output', str(run / 'final/jump-row.png'),
    '--webp-output', str(run / 'final/jump-row.webp'), '--chroma-key', '#FF00FF',
    '--json-out', str(run / 'qa/chroma-despill-jump.json')], check=True)
row = Image.open(run / 'final/jump-row.png').convert('RGBA')
assert row.getchannel('A').tobytes() == Image.open(run / 'final/jump-row-preclean.png').getchannel('A').tobytes()
old = Image.open(previous / 'spritesheet.webp').convert('RGBA')
atlas = old.copy()
atlas.paste(row, (0, 832))
for index in range(11):
    if index != 4:
        box = (0, index * 208, 1536, (index + 1) * 208)
        assert atlas.crop(box).tobytes() == old.crop(box).tobytes()
atlas.save(run / 'final/spritesheet-extended.png')
atlas.save(run / 'final/spritesheet-extended.webp', format='WEBP', lossless=True, exact=True, quality=100, method=6)
native('validate_atlas.py', run / 'final/spritesheet-extended.webp', '--json-out', run / 'final/validation-extended.json', '--chroma-key', '#FF00FF', '--require-v2')
(run / 'preview').mkdir()
native('make_contact_sheet.py', run / 'final/spritesheet-extended.webp', '--output', run / 'preview/contact-sheet.png')
native('make_direction_qa_sheet.py', run / 'final/spritesheet-extended.webp', '--output', run / 'preview/look-directions.png')
for script in ['render-final-previews.py', 'check-preview-files.py']:
    subprocess.run([sys.executable, '-B', str(run / 'qa' / script)], check=True)
boxes = [row.crop((192*i, 0, 192*(i+1), 208)).getbbox() for i in range(5)]
assert max(b[1] for b in boxes) - min(b[1] for b in boxes) <= 18
assert max(b[3] for b in boxes) - min(b[3] for b in boxes) <= 10
comparison = Image.new('RGBA', (960, 460), '#f6f5f8')
draw = ImageDraw.Draw(comparison)
draw.text((4, 4), 'Previous jump', fill='#35313d')
draw.text((4, 234), 'Gentle hop', fill='#35313d')
for index in range(5):
    comparison.alpha_composite(old.crop((192*index,832,192*(index+1),1040)), (192*index,22))
    comparison.alpha_composite(row.crop((192*index,0,192*(index+1),208)), (192*index,252))
comparison.save(run / 'qa/jump-comparison.png')
report = {'ok': True, 'pet_id': pet.name, 'new_jump_bboxes': boxes,
    'canopy_top_range_before_px': 71, 'canopy_top_range_after_px': max(b[1] for b in boxes)-min(b[1] for b in boxes),
    'boot_lift_before_px': 39, 'boot_lift_after_px': max(b[3] for b in boxes)-min(b[3] for b in boxes),
    'other_eight_states_pixel_identical': True, 'all_sixteen_gazes_pixel_identical': True,
    'neutral_pixel_identical': True, 'jump_cleanup_alpha_preserved': True,
    'cleanup_scope': 'Only newly generated jump row; previously cleaned rows copied exactly.',
    'prior_atlas_sha256': hashlib.sha256((previous/'spritesheet.webp').read_bytes()).hexdigest(),
    'new_atlas_sha256': hashlib.sha256((run/'final/spritesheet-extended.webp').read_bytes()).hexdigest(),
    'blind_qa_provenance': 'Existing 3-reviewer gaze results remain applicable: all16 gaze cells and neutral pixels unchanged.'}
(run / 'qa/change-verification.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps(report, indent=2))
