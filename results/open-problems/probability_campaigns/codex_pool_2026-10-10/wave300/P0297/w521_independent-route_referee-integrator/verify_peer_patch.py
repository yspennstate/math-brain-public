import json
from pathlib import Path

src = Path('~/<private-repo>/06_math_research/probability_1000_intake_D_20260908/attempts.jsonl')
diff = Path('~/brain_workers/w519/patches/01_intake_D_lqg_dimension_identity.diff')
source_line = src.read_text(encoding='utf-8').splitlines()[42]
patch_lines = diff.read_text(encoding='utf-8').splitlines()
assert patch_lines[2] == '@@ -43 +43 @@'
old_line = next(x[1:] for x in patch_lines if x.startswith('-{'))
new_line = next(x[1:] for x in patch_lines if x.startswith('+{'))
assert source_line == old_line
old = json.loads(old_line)
new = json.loads(new_line)
assert old['attempt_id'] == new['attempt_id'] == 'D0049-A001'
changed = {key for key in old if old[key] != new[key]}
assert changed == {'key_identity', 'method'}, changed
assert old['key_identity'].startswith('d_gamma = 2Q/xi')
assert new['key_identity'].startswith('d_gamma = gamma/xi')
assert 'd_gamma = 2 Q / xi' in old['method']
assert 'd_gamma = gamma / xi' in new['method']
print('PATCH_CHECK_OK source_line=43 changed_fields=2 untouched_fields=' + str(len(old) - 2))
