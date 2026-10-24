import pathlib,json,re,ast
root=pathlib.Path(__file__).resolve().parent
required=['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl']
assert all((root/p).is_file() and (root/p).stat().st_size for p in required)
status=(root/'STATUS.md').read_text(encoding='utf-8')
assert status.splitlines()[0] in ['STATE: WORKING','STATE: DONE']
verdict_match=re.search(r'^VERDICT: (SOLVED|PARTIAL|SOLVED_IN_LITERATURE|NO_PROGRESS)$',status,re.M)
assert verdict_match and 'NEXT: ' in status
claims=[json.loads(l) for l in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
assert all(c['problem_id']=='P0391' for c in claims)
assert all(c['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture'] for c in claims)
assert all(set(['problem_id','claim','status','proof_location','remaining_gap','checks'])<=c.keys() for c in claims)
for file in root.glob('*.py'):ast.parse(file.read_text(encoding='utf-8'))
lean=(root/'GridBridge.lean').read_text(encoding='utf-8')
assert not re.search(r'\b(sorry|native_decide)\b',lean)
assert not re.search(r'^import Mathlib\s*$',lean,re.M)
numerics=json.loads((root/'numerical_checks.json').read_text(encoding='utf-8'))
assert sum(x['reps'] for x in numerics['results'])==288
assert min(x['minimum_bridge_slack'] for x in numerics['results'])>=-1e-12
assert (root/'source_pdf.pdf').read_bytes().startswith(b'%PDF')
log=(root/'lean_check.txt').read_text(encoding='utf-8') if (root/'lean_check.txt').exists() else ''
record={'required_records':'present','claim_count':len(claims),'claims_json':'valid','python_syntax':'valid',
 'lean_source':'selective imports; no sorry or native_decide','lean_latest_log_passed':log.startswith('Exit code: 0'),
 'simulation_paths':288,'simulation_events':sum(x['events'] for x in numerics['results']),
 'minimum_numerical_bridge_slack':min(x['minimum_bridge_slack'] for x in numerics['results']),
 'mathematical_verdict':verdict_match.group(1)}
(root/'records_audit.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record,indent=2))
