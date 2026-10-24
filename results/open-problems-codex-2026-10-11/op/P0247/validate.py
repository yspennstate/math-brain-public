from pathlib import Path
import json
p=Path(__file__).parent
files=['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','lean_check.txt']
assert all((p/f).exists() for f in files)
claims=[json.loads(s) for s in (p/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s]
assert all(c['problem_id']=='P0247' and c['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture'] for c in claims)
lean=(p/'lean_check.txt').read_text(encoding='utf-8');assert lean.startswith('exit_code=0')
source=(p/'FiniteChecks.lean').read_text(encoding='utf-8')
assert 'sorry' not in source and 'native_decide' not in source and 'import Mathlib\n' not in source
results={f:len(json.loads((p/f).read_text(encoding='utf-8'))) for f in ['computations.json','bound_checks.json','product_search.json']}
report=dict(required_files_present=True,claim_count=len(claims),lean_exit_code=0,result_counts=results,status_first_line=(p/'STATUS.md').read_text(encoding='utf-8').splitlines()[0])
(p/'validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))
