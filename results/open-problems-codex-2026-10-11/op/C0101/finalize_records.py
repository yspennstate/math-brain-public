import json
from pathlib import Path
R=Path(__file__).parent
p=R/'CLAIMS.jsonl'
rows=[json.loads(s) for s in p.read_text(encoding='utf-8').splitlines()]
for r in rows:
 r['checks']={'written_proof':'complete, self-refereed; ATTEMPT.md','exact_arithmetic':'math_checks.json and periodic_checks.json, all passed','lean':'WitnessAlgebra.lean algebra only; exit 0; lean_result.json','full_problem_solved':False}
extras=[
 {'problem_id':'C0101','claim':'For every d>=3 there exists a maximal member of the source Gamma(Z^d) which is not an integer matrix.','status':'proved_special_case','proof_location':'ATTEMPT.md, Theorems 7 and 10','remaining_gap':'The explicit half-integral A_d is admitted but not proved maximal. Its maximal extension is existential and is not proved irrational or isolated.','checks':{'parity_table':'complete exact four-case proof','explicit_lattice_tests':'486 checks in dimensions 3-8; periodic_checks.json','domination_obstruction':'A positive-semidefinite increment has nonnegative integer diagonal of trace at most 1, so a zero row conflicts with the half-integer off-diagonal.'}},
 {'problem_id':'C0101','claim':'The corrected period-two affine-cocycle search produced 23 exact-verified witness certificates among 112 cases for 14 half-integral matrices in d=3, threshold 5.','status':'numerical_evidence','proof_location':'periodic_phase_results.json; ATTEMPT.md, Computation','remaining_gap':'No numerical infeasibility is used as global exclusion; no maximality is inferred from these finite cases.','checks':'7889 exact extended-grid checks; periodic_checks.json'}]
for r in extras:
 if not any(x['claim']==r['claim'] for x in rows):rows.append(r)
p.write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')
p=R/'LITERATURE.md'
p.write_text(p.read_text(encoding='utf-8').replace('Advances in Mathematics (January 2024), article 109400','Advances in Mathematics 436 (January 2024), article 109400'),encoding='utf-8')
p=R/'ATTEMPT.md'
p.write_text(p.read_text(encoding='utf-8').replace('no `sorry`, axioms, or `native_decide`','no `sorry`, added axioms, or `native_decide`'),encoding='utf-8')
for f in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','lean_result.json','math_checks.json','periodic_checks.json']:
 assert (R/f).exists() and (R/f).stat().st_size>0
assert json.loads((R/'lean_result.json').read_text())['exit_code']==0
assert all('remaining_gap' in r and 'proof_location' in r for r in rows)
assert len(rows)==8
(R/'STATUS.md').write_text('''STATE: DONE
NEXT: Test positive-semidefinite perturbations of the explicit A_3 using period-three/six affine-cocycle witnesses, seeking a certificate for its maximal extension.
VERDICT: PARTIAL
2026-10-12: Verified arXiv:1611.00411, p.21 definition and p.27 open problem 9(4); searched arXiv, OpenAlex, Crossref, Semantic Scholar and GitHub. No matching solution found; OpenAlex blocked by exhausted shared API budget. Searches and exact references saved in LITERATURE.md.
2026-10-12: Proved the trace bound, maximality of every integer symmetric trace-(2d-1) matrix, exact separable-witness classification, maximal-extension existence, integer harmonic-shift symmetry and rationality under a full-rank affine cocycle.
2026-10-12: Constructed A_d with diagonal (1,1,2,...,2) and A_12=A_21=1/2, proved A_d stabilizes and has no integer dominator in Gamma. Hence noninteger maximal elements exist for every d>=3; this does not imply irrationality and A_d itself is not proved maximal.
2026-10-12: Exact checks passed: 480 polynomial cases, 56303 floor-increment cases, 7889 extended-periodic cases and 486 explicit-witness cases. Lean algebra file checked with exit 0, no sorry or native_decide. Full written proofs and hostile self-referee in ATTEMPT.md; eight claims in CLAIMS.jsonl.
2026-10-12: This attempt is complete with partial results. The classification and the isolation/rationality questions for all maximal elements remain unresolved. No SOLVED or SOLVED_IN_LITERATURE verdict is asserted.
''',encoding='utf-8')
print('Saved DONE / PARTIAL; eight claims validated; all required files present.')
