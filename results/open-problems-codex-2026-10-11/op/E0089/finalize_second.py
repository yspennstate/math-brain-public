from pathlib import Path
import json
p=Path('SECOND_ATTEMPT.md');s=p.read_text(encoding='utf8');s=s.replace('The graph-specific median version of Corollary C also holds for the locally centred statistic.','The graph-specific median version of Corollary C also holds for the locally centred statistic. Define its conditional CDF to be zero on an impossible conditioning event; that exceptional event has probability tending to zero because the median density lies in a fixed compact interval with probability tending to one.');p.write_text(s,encoding='utf8')
rows=[json.loads(x) for x in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(rows)==20
assert all(x['problem_id']=='E0089' for x in rows)
assert 'Exit: 0' in Path('second_lean_check.txt').read_text(encoding='utf8')
checks=json.loads(Path('second_finite_checks.json').read_text());assert checks['all_passed'] and checks['message_peeling_checks']==12288
experiments=json.loads(Path('second_experiments.json').read_text());assert len(experiments['graphs'])==18
assert experiments['recursion'][-1]['t']==100000
rep=json.loads(Path('second_replica_example.json').read_text());assert rep['annealed_independent_replica_final_covariance']=='13286025/4294967296'
assert rep['one_round_count_initial_count_covariances']==['262144/177147','262144/177147']
for section in ['Theorem A','Theorem B','Corollary C','Precise remaining gap','Final verdict']:
 assert section in s
status='''STATE: DONE
NEXT: Prove a global quenched critical-window description for final core emptiness, or control the joint two-colour adaptive pairing covariance needed for ATTEMPT.md equation (6).
VERDICT: PARTIAL

2026-10-12: First attempt completed with source correction, threshold tightness, deterministic profile bounds, replica reduction, switching comparison, and core duality. No solution to E0089 was proved.
2026-10-12: Reopened at the user's request for one more serious attempt. Read ATTEMPT.md and asked the math store about the actual quenched replica gap and dependency-graph CLTs. Wrote down two new approaches in SECOND_ATTEMPT.md and pursued local peeling/conditional limit theorems.
2026-10-12: Proved Theorem A (fixed-round quenched Gaussian vacancy counts), Theorem B (growing rounds with (d-1)^t_n=o(log n)), and Corollary C (local-count CDF concentration under upper-initial-count conditioning, including the locally centred graph-specific-median version).
2026-10-12: Proved exact d=4,k=2 critical recursion and reciprocal bounds, t z_t->3/4, and a polynomial-depth obstruction to resolving the saddle-node drift by tree-ball approximations. Kernel-checked six algebraic/constant statements in CriticalRecursion.lean; exit 0.
2026-10-12: Completed 12288 exact message/peeling checks, 303 rational polynomial checks, 30 exact joint-star checks, exact local two-round means on 18 sampled graphs, and 100000 high-precision recursion iterations. Saved all checks and data. Hostile-referee audit written in SECOND_ATTEMPT.md Section 6.
2026-10-12: Second attempt finalized. The required final-success replica factorization remains unproved. Early completion at the allowed growing depths has L1 discrepancy tending to 1/2 from the final critical event. Twenty claim records are saved. Verdict PARTIAL; no full proof or random-regular-graph counterexample, and no exact published solution found.
'''
Path('STATUS.md').write_text(status,encoding='utf8')
print('Final validation passed: 20 claims; second Lean exit 0; all finite checks passed; 18 graph experiments; STATE DONE / PARTIAL.')
