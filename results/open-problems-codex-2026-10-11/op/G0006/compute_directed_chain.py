import sympy as s,json
from pathlib import Path
lam=s.symbols('lambda',positive=True)
# Three-site directed chain: immigration at site0, births0->1 and1->2.
Q=s.zeros(8)
for x in range(8):
 for i in range(3):
  rate=s.Integer(1) if x>>i&1 else (lam if i==0 or (x>>(i-1)&1) else s.Integer(0))
  if rate:Q[x,x^(1<<i)]+=rate;Q[x,x]-=rate
A=Q.T.copy();A[7,:]=s.ones(1,8);rhs=s.zeros(8,1);rhs[7]=1
pi=(A.inv()*rhs).applyfunc(s.factor)
assert all(s.factor(v)==0 for v in Q.T*pi)
b=s.factor(sum(pi[x] for x in range(8) if (x&6)==6))
b0=s.factor(b.subs(lam,s.Rational(1,4)))
assert b0>s.Rational(1,3**25)
# Two-site version has joint occupancy lambda^2/(lambda^2+2lambda+2).
result={'three_site_joint_formula':str(b),'three_site_joint_at_1_over_4':str(b0),'decimal':float(b0),'buffered_threshold':'1/'+str(3**25),'residual_symbolically_zero':True}
result['stationary_at_1_over_4']=[str(s.factor(v.subs(lam,s.Rational(1,4)))) for v in pi]
Path('directed_chain_result.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result))
