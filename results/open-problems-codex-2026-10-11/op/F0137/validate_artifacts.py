import pathlib,json,hashlib
R=pathlib.Path(__file__).resolve().parent
required=['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','CHECKS.md','Algebra.lean','experiment_results.json']
for name in required: assert (R/name).is_file(),name
lines=(R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()
claims=[json.loads(x) for x in lines if x.strip()]
for c in claims:
 assert c['problem_id']=='F0137'
 assert c['status'] in {'proved','proved_special_case','numerical_evidence','conjecture','counterexample'}
 assert set(c)=={'problem_id','claim','status','proof_location','remaining_gap','checks'}
exp=json.loads((R/'experiment_results.json').read_text())
assert len(exp['finite_boundary_enumeration'])==7
assert all(x['minimum_cut']==x['kappa'] for x in exp['finite_boundary_enumeration'])
assert all(x['subsets_checked']==502 for x in exp['finite_boundary_enumeration'])
assert len(exp['exact_rational_loop_crosscheck'])==7
lean=(R/'Algebra.lean').read_text(encoding='utf8')
assert 'sorry' not in lean and 'native_decide' not in lean and '\nimport Mathlib\n' not in lean
summary={'claims':len(claims),'parameter_vectors':7,'nontrivial_subsets_per_vector':502,
 'connected_subsets_per_vector':209,'rational_loop_checks':7*2*8,
 'lean_sha256':hashlib.sha256((R/'Algebra.lean').read_bytes()).hexdigest(),
 'remaining_gap':'No bound for all repeated-departure wrong-exit paths or for the full regeneration range.'}
(R/'artifact_validation.json').write_text(json.dumps(summary,indent=2),encoding='utf8')
print(json.dumps(summary,indent=2))
