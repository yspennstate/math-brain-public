"""Create a review-only copy and diff; never edit the live brain."""
from pathlib import Path
import difflib
import hashlib
import json

ROOT = Path(__file__).resolve().parent
LIVE = Path('~/.claude/dreaming/brain.py')
original_bytes = LIVE.read_bytes()
original = original_bytes.decode('utf-8')
old_status = '''        # an index line without a tag says nothing about status; the memory's own frontmatter does, and a
        # retraction is the one status a reader must not miss (F50) - bounded to the displayed rows
        if status == "legacy" and _frontmatter_retracted(slug):
'''
new_status = '''        # A tagged index line can also be stale. Author retractions override every index status;
        # check only displayed rows, using the existing bounded frontmatter reader.
        if _frontmatter_retracted(slug):
'''
old_description = '        d = _full_description(slug) or sr._desc(slug, idx) or "(no description)"\n'
new_description = '''        if status == "retracted":
            d = "Withdrawn by the author; open this memory for the correction before using it."
        else:
            d = _full_description(slug) or sr._desc(slug, idx) or "(no description)"
'''
for anchor in (old_status, old_description):
    if original.count(anchor) != 1:
        raise SystemExit('Source changed or anchor ambiguous; stop and rebase the local patch.')
patched = original.replace(old_status, new_status).replace(old_description, new_description)
(ROOT / 'copies').mkdir(exist_ok=True)
(ROOT / 'patches').mkdir(exist_ok=True)
(ROOT / 'copies' / 'brain.before.py').write_bytes(original_bytes)
(ROOT / 'copies' / 'brain.after.py').write_bytes(patched.encode('utf-8'))
patch = ''.join(difflib.unified_diff(original.splitlines(True), patched.splitlines(True),
    fromfile='a/.claude/dreaming/brain.py', tofile='b/.claude/dreaming/brain.py'))
(ROOT / 'patches' / '01_recall_retracted_tag_override.diff').write_bytes(patch.encode('utf-8'))
receipt = {'live_path': str(LIVE), 'patch_root': '~',
    'baseline_sha256': hashlib.sha256(original_bytes).hexdigest(),
    'candidate_sha256': hashlib.sha256(patched.encode('utf-8')).hexdigest(),
    'deployed': False, 'scope': 'display status and description only; no scoring or routing change'}
(ROOT / 'PATCH_RECEIPT.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipt))
