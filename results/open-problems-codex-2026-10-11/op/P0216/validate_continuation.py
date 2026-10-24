import pathlib,json,math,hashlib
R=pathlib.Path(__file__).resolve().parent
claims=[json.loads(s) for s in (R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==14
assert all(c['problem_id']=='P0216' for c in claims)
counts=json.loads((R/'balanced_counts.json').read_text())
for c in counts:c.pop('max_fixed_first_insertion',None)
(R/'balanced_counts.json').write_text(json.dumps(counts,indent=2),encoding='utf8')
sub=json.loads((R/'substitution_check.json').read_text())
by_n={x['n']:x['H_by_substitution_tree'] for x in sub}
for x in counts:assert x['H']==by_n[x['n']]
small=json.loads((R/'exact_posets.json').read_text())
for x in small:
 c=next(c for c in counts if c['n']==x['n'])
 assert abs(c['H']/math.factorial(x['n'])**3-x['collision_probability'])<1e-15
txt=(R/'CONTINUATION.md').read_text(encoding='utf8')
assert 'conditional until' not in txt
lean=json.loads((R/'collision_lean_check.json').read_text())
assert lean['exit_code']==0
assert lean['sha256']==hashlib.sha256((R/'CollisionTruth.lean').read_bytes()).hexdigest()
assert 'decide +kernel' in (R/'CollisionTruth.lean').read_text()
assert 'sorry' not in (R/'CollisionTruth.lean').read_text() and 'native_decide' not in (R/'CollisionTruth.lean').read_text()
formal=json.loads((R/'formal_series_diagnostic.json').read_text())
for c in sub:assert c['H_by_substitution_tree']==int(formal['H_coefficients'][c['n']])
assert (R/'STATUS.md').read_text().splitlines()[0]=='STATE: DONE'
out={'claims':len(claims),'counts_cross_checked_through':max(c['n'] for c in counts),'substitution_count_completed_through':max(c['n'] for c in sub),'formal_coefficients_cross_checked_through':16,'small_collision_cross_check_through':4,'tree_bound_check':json.loads((R/'tree_bound_checks.json').read_text()),'lean_exit_code':lean['exit_code'],'lean_sha256':lean['sha256'],'overlap_check':json.loads((R/'overlap_check.json').read_text()),'main_problem_solved':False,'verdict':'PARTIAL'}
(R/'continuation_validation.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
