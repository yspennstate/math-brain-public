from pathlib import Path
import json
p=Path('.')
assert (p/'STATUS.md').read_bytes().splitlines()[0]==b'STATE: DONE'
claims=[json.loads(x) for x in (p/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==7 and all(x['problem_id']=='D0047' for x in claims)
assert all((p/f).is_file() for f in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl'])
assert 'Exit code: 0' in (p/'lean_check.txt').read_text(encoding='utf8')
print('Final artifact audit PASS: exact first line STATE: DONE; verdict PARTIAL; 7 valid claims; Lean exit 0.')
print((p/'STATUS.md').read_text(encoding='utf8').splitlines()[:3])
