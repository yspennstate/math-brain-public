import pathlib,json,hashlib
R=pathlib.Path(__file__).resolve().parent
cs=[json.loads(s) for s in (R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(cs)>=6
assert all(x['problem_id']=='P0216' and x['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture'] for x in cs)
assert all(all(k in x for k in ['claim','status','proof_location','remaining_gap','checks']) for x in cs)
assert 'sorry' not in (R/'GridAgreement.lean').read_text().replace('No probability','No probability')
assert 'native_decide' not in (R/'GridAgreement.lean').read_text()
result={'claims':len(cs),'lean_sha256':hashlib.sha256((R/'GridAgreement.lean').read_bytes()).hexdigest(),'record_files':{name:(R/name).stat().st_size for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl']},'openalex_limitation':'all source-search requests rate limited; citing-works traversal unavailable','remaining_problem':'prove convergence and determine the optimal constant'}
(R/'record_validation.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
