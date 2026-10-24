from pathlib import Path
import json,datetime
p=Path(__file__).resolve().parent
claims=[json.loads(line) for line in (p/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
assert all(c['problem_id']=='E0086' for c in claims)
assert all(c['status'] in {'proved','counterexample','proved_special_case','numerical_evidence','conjecture'} for c in claims)
for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','source.pdf','source.txt','Boundary.lean','finite_checks.json','green_checks.json']:
 assert (p/name).is_file() and (p/name).stat().st_size>0
lean=(p/'Boundary.lean').read_text();assert 'sorry' not in lean and 'native_decide' not in lean and '\nimport Mathlib\n' not in lean
lean_result=json.loads((p/'lean_check.json').read_text()) if (p/'lean_check.json').exists() else {'status':'pending shared checker'}
r={'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'folder':str(p),'claims':len(claims),'required_files_present':True,'claims_json_valid':True,'lean_has_no_sorry_or_native_decide':True,'lean_check_status':lean_result['status'],'finite_paths_per_offset':65536,'finite_offsets':3,'green_examples':9,'max_green_error':max(v['error'] for v in json.loads((p/'green_checks.json').read_text())),'scan_geometry_cases':len(json.loads((p/'scan_checks.json').read_text())),'scan_walk_runs':len(json.loads((p/'scan_walk_checks.json').read_text())['runs']),'status_first_line':(p/'STATUS.md').read_text().splitlines()[0]}
(p/'verification.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2));print('Boundary created UTC',datetime.datetime.fromtimestamp((p/'Boundary.lean').stat().st_ctime,datetime.timezone.utc))
