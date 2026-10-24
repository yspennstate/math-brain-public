from pathlib import Path
import json
# Final record validation; all mathematical claims remain scoped to their actual proofs.
lean=Path('lean_hellinger_check.txt').read_text(encoding='utf8')
assert 'exit=0;' in lean and 'sorryAx' not in lean
src=Path('HellingerObstruction.lean').read_text(encoding='utf8')
assert 'import Mathlib\n' not in src and 'sorry' not in src and 'native_decide' not in src
claims=[json.loads(v) for v in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==18 and all(v['problem_id']=='E0024' for v in claims)
report=Path('SECOND_ATTEMPT.md').read_text(encoding='utf8')
for key in ['Two approaches','B1.','B4.','A1.','A2.','A3.','Final hostile-referee','A3 addendum']:
 assert key in report,key
nums=json.loads(Path('second_numerical_checks.json').read_text())
assert nums['hellinger_identity_random_tests']==20000
assert len(nums['smoothing_residual'])==6
p=Path('STATUS.md');s=p.read_text(encoding='utf8')
s=s.replace('STATE: WORKING','STATE: DONE',1)
lines=s.splitlines()
lines[1]='NEXT: Prove the per-measure uniform Gaussian-smoothing approximation in SECOND_ATTEMPT.md A2 from bare factor (H), or construct an admissible thin nonpolar set.'
lines[2]='VERDICT: PARTIAL'
s='\n'.join(lines)+'\n'
s+='''
2026-10-12 (renewed attempt completed): Recorded two new approaches and queried the brain for the correlated-energy gap, Hellinger/Kakutani, and Hu-Sun-Wang. Pursued path-law transfer; proved exact optimal symmetric-reference criterion for arbitrary Levy measures and its drift condition. Skew stable (H) factors violate that criterion, preventing a general solution by this route.
2026-10-12 (renewed attempt completed): Also proved fixed-scale smoothing and its exact per-measure uniformity criterion. Explicit positive Gaussian-modulated inputs, with compact truncations, disprove the natural uniform energy-norm transfer bound; this is not a counterexample to (H).
2026-10-12 (renewed checks): Fetched Kanda's original paper and checked the exact positive-measure monotonicity assumptions. Hellinger finite algebra passed Lean with exit 0 and no sorryAx; 20000 random checks and small Gauss-Hermite experiments passed. Full proofs and hostile-referee caveats are in SECOND_ATTEMPT.md and summarized in ATTEMPT.md; 8 new claims appended. The renewed bounded attempt is finished; unrestricted E0024 remains unresolved.
'''
p.write_text(s,encoding='utf8')
assert p.read_text().splitlines()[0]=='STATE: DONE'
print('STATE: DONE; VERDICT: PARTIAL. Validated four main records, renewed report, 18 claims and Lean certificate.')
