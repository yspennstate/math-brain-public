from pathlib import Path
from fractions import Fraction as Q
import json
ROOT=Path(__file__).resolve().parents[1]
s=json.loads((ROOT/'out/SEED_CERTIFICATE.json').read_text(encoding='utf-8'))['first_certified_seed']
assert s['depth']==5 and s['n']==32 and s['sign']==1
I=Q(s['I']); l,u=map(Q,s['H']); delta=l-Q(9,2)*I
assert delta>Q(1,10)
N=2048; c=Q(1,16); A=Q(9,2); exterior=Q(7)
# The same exact E0 is added to BOTH entropy and the generously enlarged capacity.
root_H_minus_E0=(c*N*l,c*N*u)
budget_minus_E0=exterior+A*c*(N*I+1)
gap=root_H_minus_E0[0]-budget_minus_E0
assert gap>Q(883,160)>0
result=dict(status='PASS',seed_depth=5,seed_variables=32,copies=N,full_physical_dimension=4+1+32*N,core_influence=str(N*I+1),seed_influence=str(I),seed_margin_lower=str(delta),seed_margin_simplified='>1/10',budget_minus_E0=str(budget_minus_E0),entropy_minus_E0_interval=[str(a) for a in root_H_minus_E0],excess_lower=str(gap),excess_simplified='>883/160',old_costs='retaining any nonnegative old debit only decreases the unused capacity',target='original fixed9/2 complete-core payment, not FEI')
(ROOT/'out/TENSOR_CERTIFICATE.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({a:result[a] for a in ['status','full_physical_dimension','seed_margin_simplified','excess_simplified','target']}))
