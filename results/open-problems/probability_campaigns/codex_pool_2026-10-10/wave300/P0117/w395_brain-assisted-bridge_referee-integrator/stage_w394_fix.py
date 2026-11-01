"""Stage two referee fixes to w394's submitted draft without touching its inbox file."""
from __future__ import annotations

import difflib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
live = Path('~/math-brain-inbox/w394/bundle_002.json')
old = live.read_text(encoding='utf-8')
replacements = [
    ('A finite geodesic attains this infimum.', 'Call a finite path a geodesic if it attains this infimum; arbitrary positive deterministic weights need not give a minimizer for every pair.'),
    ('"kind": "refutes",\n      "rationale": "The M_R partition events satisfy uniform vanishing but have union probability one, contradicting precisely the documented fixed-endpoint promotion."',
     '"kind": "semantic_association",\n      "rationale": "The M_R partition events give a concrete probability counterexample to the inference whose failure this target node records; they support that warning rather than refuting the warning node."'),
]
new = old
for before, after in replacements:
    assert new.count(before) == 1, before
    new = new.replace(before, after, 1)
assert new != old
bundle = json.loads(new)
assert len(bundle['entries']) == 6 and len(bundle['relations']) == 5
assert bundle['relations'][0]['kind'] == 'semantic_association'
copy = root / 'reviewed_copies' / 'w394_bundle_002_referee_fix.json'
copy.parent.mkdir(exist_ok=True)
copy.write_text(new, encoding='utf-8')
target = live.as_posix()
diff = ''.join(difflib.unified_diff(old.splitlines(keepends=True), new.splitlines(keepends=True), fromfile='a/' + target, tofile='b/' + target))
patch = root / 'patches' / '03_w394_bundle_002_referee_fix.diff'
patch.parent.mkdir(exist_ok=True)
patch.write_text(diff, encoding='utf-8')
print(json.dumps({'status': 'pass', 'entry_count': len(bundle['entries']), 'relation_count': len(bundle['relations']), 'corrections': len(replacements), 'reviewed_copy': str(copy), 'patch': str(patch)}))
