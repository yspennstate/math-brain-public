from pathlib import Path
import json
import hashlib

root=Path(__file__).resolve().parent
claims=root/'CLAIMS.jsonl'
raw=claims.read_text(encoding='utf-8')
if raw.endswith('\\n'):
    raw=raw[:-2]+'\n'
    claims.write_text(raw,encoding='utf-8')
rows=[json.loads(line) for line in raw.splitlines() if line.strip()]
assert all(row['problem_id']=='P0306' for row in rows)
assert all(row['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture'] for row in rows)
checks=json.loads((root/'second_check_results.json').read_text(encoding='utf-8'))
for row in checks:
    if 'integral' in row:
        assert abs(row['integral']-row['exact_integral'])<1e-12
        assert row['speed_identity_max_abs_error']<1e-12
for name in ['SECOND_ATTEMPT.md','RECORD_REDUCTION.md','BARRIER_REDUCTION.md','SECOND_REFEREE.md','SECOND_SOURCE_EXCERPTS.md','LITERATURE.md','ATTEMPT.md']:
    assert (root/name).stat().st_size>100
lean=root/'SecondCheck.lean'
lean_text=lean.read_text(encoding='utf-8')
assert 'sorry' not in lean_text and 'native_decide' not in lean_text and 'import Mathlib\n' not in lean_text
report={'claim_rows':len(rows),'numerical_checks':'passed','required_documents':'present','lean_file_sha256':hashlib.sha256(lean.read_bytes()).hexdigest(),'lean_completion':'record separately; this script does not execute Lean'}
(root/'second_validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
with (root/'ATTEMPT.md').open('a',encoding='utf-8') as f:
    f.write('\nThe second approach was also made quantitative in BARRIER_REDUCTION.md. Its conditional-expectation proof gives an exact sufficient exponent, including a diameter-size-biased law formulation; the required LQG barrier and moment estimates are not proved. The full audit is in SECOND_REFEREE.md, with exact source excerpts in SECOND_SOURCE_EXCERPTS.md.\n')
print(json.dumps(report,indent=2))
