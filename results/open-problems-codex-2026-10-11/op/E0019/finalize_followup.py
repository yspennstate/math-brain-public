from pathlib import Path
import json
p=Path('CLAIMS.jsonl');claims=[json.loads(s) for s in p.read_text(encoding='utf8').splitlines()]
for c in claims:
 if c['proof_location'].startswith('FOLLOWUP.md, Theorem A'):
  c['checks']+=['FollowupAlgebra.lean: threshold equivalence kernel checked, exit code 0','240 Jacobian checks and four remainder-bound examples passed in followup_numerics.json']
 if c['claim'].startswith('At lambda_0=2'):
  c['checks']+=['Positive pulse numerical diagnostic: residual 4.46e-17; mathematical proof uses exact rotation relation and implicit-function theorem']
claims.append({'problem_id':'E0019','claim':'Second-attempt diagnostics passed on 240 fixed-time Jacobians across scalar, spiral, nonnormal and 3D models, four remainder bounds, a positive three-pulse cancellation, and exact scalar boundary identities.','status':'numerical_evidence','proof_location':'followup_numerics.json; followup_checks.py; CHECKS.md follow-up section','remaining_gap':'Numerics do not prove the analytical theorems; their complete proofs are in FOLLOWUP.md.','checks':['Seed 1900192','Maximum Jacobian absolute error <2.47e-10','Positive pulse residual <4.46e-17','Four contraction estimates <1','Exact SymPy scalar flux and threshold identities']})
p.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf8')
# All completed proof records remain explicitly special to their stated models.
req=['ATTEMPT.md','LITERATURE.md','CLAIMS.jsonl','FOLLOWUP.md','CHECKS.md','FollowupAlgebra.lean','followup_lean_result.json','followup_numerics.json']
for name in req:assert Path(name).exists(),name
lean=json.loads(Path('followup_lean_result.json').read_text(encoding='utf8'));assert lean['exit_code']==0
s=Path('FollowupAlgebra.lean').read_text(encoding='utf8');assert 'sorry' not in s and 'native_decide' not in s and 'import Mathlib\n' not in s
assert not Path('FollowupAlgebra.lean').read_bytes().startswith(b'\xef\xbb\xbf')
for c in claims:
 assert c['problem_id']=='E0019' and c['proof_location'] and c['remaining_gap'] and c['checks']
 assert c['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture']
follow=Path('FOLLOWUP.md').read_text(encoding='utf8');assert '## Two approaches not previously tried' in follow and 'Theorem A is proved' in follow and 'Theorem B is proved' in follow and '## Remaining gap' in follow
status=Path('STATUS.md');log=status.read_text(encoding='utf8');log=log.replace('STATE: WORKING','STATE: DONE',1);log=log.replace(log.splitlines()[1],'NEXT: Classify higher Ck regularity at the source spiral intermediate rates and the complete propagated singularity set; extend beyond the common-matrix constant-rate family.',1)
log+='''\n2026-10-12 follow-up complete: Wrote two untried approaches, consulted the brain about the gap and the Neumann-series reduction, and pursued the fixed-time transfer decomposition. Proved exact finite-Lp membership iff min(lambda_0,lambda_1)>-tr(A)*(1-1/p) for every stable controllable common-matrix two-mode affine system, including strict threshold necessity.\n2026-10-12 follow-up complete: Returned to the critical-rate resolvent approach. Proved interior support via three positive pulses, uniform density positivity via a smooth two-switch kernel, and logarithmic divergence at lambda_i=2 for the source spiral. Its density is bounded/continuous on R2 iff both rates exceed 2; at min(rate)=2 it is in every finite Lp but unbounded. Also gave a complete fixed-time proof of the known Ck sufficient rate condition.\n2026-10-12 follow-up checks: 240 Jacobian tests, four probability/volume contraction examples, positive pulse diagnostics and exact scalar beta-boundary tests passed. FollowupAlgebra.lean passed with exit code 0 (only redundant-tactic warnings); failed preliminary invocations were corrected and are not called checked. Full proof and referee details are in FOLLOWUP.md and CHECKS.md.\n2026-10-12 final scope: STATE DONE / VERDICT PARTIAL. The two missing special-case integrability/critical boundedness gaps are now closed. Higher differentiability at all rates, all propagated singularity sets and arbitrary nonlinear/state-dependent switched-flow regularity remain unproved. No publication-novelty or complete-literature-solution claim is made.\n'''
status.write_text(log,encoding='utf8');assert status.read_bytes().splitlines()[0]==b'STATE: DONE'
assert status.read_text(encoding='utf8').splitlines()[2]=='VERDICT: PARTIAL'
print('Final validation passed: DONE / PARTIAL; '+str(len(claims))+' claim records. Follow-up Lean exit code 0.')
