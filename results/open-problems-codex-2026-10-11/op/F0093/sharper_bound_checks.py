import json,math
from fractions import Fraction as F
from pathlib import Path
rows=[json.loads(s) for s in Path('second_experiments.jsonl').read_text().splitlines()];checks=[]
for r in rows:
 k=r['k'];e=.25;d=2 if r['model']=='Z' else 4
 A=1+(d-1)*(1-e)**2/(e*(d-(d-1)*e))
 delta=(r['KL_bound'] if r['model']=='Z' else 2*r['TV_bound']**2)*e**k
 bound=math.sqrt(max(0,(A**k-1)*delta/2))
 assert r['tv_block_change']<=bound+1e-8
 checks.append({'model':r['model'],'n':r['n'],'k':k,'block_start':r.get('block_start',0),'A':A,'sharper_TV_bound':bound,'actual_TV_change':r['tv_block_change']})
# Exact finite-alphabet counting and positivity checks for the sharper path constant.
exact=[]
for d in [2,3,4,5]:
 for e in [F(1,10),F(1,4),F(1,2),F(9,10),F(1)]:
  A=sum(F(1,d*d)**2/(e/F(d*d)+(1-e)/d*(i==j)) for i in range(d) for j in range(d))
  formula=1+(d-1)*(1-e)**2/(e*(d-(d-1)*e))
  assert A==formula and 1<=A<=1/e
  exact.append({'d':d,'epsilon':str(e),'A_exact':str(A)})
low,high=.8,.82
for _ in range(60):
 m=(low+high)/2
 if m**3+m**2+m-2>0:high=m
 else:low=m
eta=(low+high)/2;alpha=math.log(2)/math.log(2/eta)
Path('sharper_bound_checks.json').write_text(json.dumps({'numerical_bound_checks':checks,'exact_alphabet_checks':exact,'eta':eta,'alpha':alpha,'c_upper_epsilon_quarter_d4':(1-alpha)/math.log(40/13),'old_c_upper':(1-alpha)/math.log(4),'Z_barrier_epsilon_quarter_theta_zero':math.exp(-1)*(1-math.exp(-.75))/2},indent=2),encoding='utf8')
print('Verified sharper TV bounds on',len(checks),'models/blocks and',len(exact),'exact alphabet constants. Grigorchuk c upper =',(1-alpha)/math.log(40/13))
