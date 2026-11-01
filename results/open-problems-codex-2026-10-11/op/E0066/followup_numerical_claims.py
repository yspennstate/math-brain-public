from pathlib import Path
import json
p=Path('.')
new=[('The uniform two-point four-type support cycles of lengths five and six were all reported infeasible in a rooted LP enumeration of 240 orders.','boundary_followup.py and boundary_followup.json','Floating-point infeasibility only; no exact dual certificates.'),('All 240 sampled moving-support repeated-value cycles with sorted vector (0.4,0.4,0.2,0) and periods five, six, seven failed necessary QBO coefficient LP constraints.','radial_followup_checks.py and radial_followup_checks.json','Sampled orders and floating-point solver; not a theorem.')]
with p.joinpath('CLAIMS.jsonl').open('a',encoding='utf8') as f:
 for c,l,g in new:f.write(json.dumps({'problem_id':'E0066','claim':c,'status':'numerical_evidence','proof_location':l,'remaining_gap':g,'checks':'HiGHS status 2 in every case; three-second per-LP limit; small matrices.'})+'\n')
print('Boundary exploration recorded as numerical evidence only')
