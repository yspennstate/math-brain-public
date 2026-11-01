import sympy as sp,json,pathlib,time
# Z^2 l1-radius-one ball: one center and four mutually nonadjacent leaves.
# Lumping by (center infected?, number of infected leaves) is exact because
# internal transitions and exits depend only on these two counts.
states=[(c,l) for c in [0,1] for l in range(5) if (c,l)!=(0,0)]
idx={s:i for i,s in enumerate(states)}
out=[]
for lam in [sp.Rational(1,8),sp.Rational(1,4),sp.Rational(2,5),sp.Rational(1,2)]:
 A=sp.zeros(len(states));b=sp.zeros(len(states),1)
 for i,(c,l) in enumerate(states):
  transitions=[]
  if c:transitions.append(((0,l),sp.Rational(1)))
  if l:transitions.append(((c,l-1),sp.Rational(l)))
  if not c and l:transitions.append(((1,l),lam*l))
  if c and l<4:transitions.append(((1,l+1),lam*(4-l)))
  exit_rate=3*lam*l
  A[i,i]=exit_rate+sum(rate for _,rate in transitions)
  b[i,0]=exit_rate
  for target,rate in transitions:
   if target in idx:A[i,idx[target]]-=rate
 q=A.inv()*b
 assert A*q==b
 assert all(0<x<1 for x in q)
 val=q[idx[(1,0)],0];lower=(lam/(1+lam))**2
 assert val>=lower
 rec={'lambda':str(lam),'q_star_exact':str(val),'q_star_decimal':float(val),'q_zero':str(4*lam/(1+4*lam)),'two_step_lower_bound':str(lower),'star_path_threshold':'1/243','certificate_passes':bool(val<sp.Rational(1,243)),'exact_linear_residual_zero':True}
 out.append(rec);print(json.dumps(rec))
pathlib.Path('exit_results.json').write_text(json.dumps({'states':states,'results':out},indent=2),encoding='utf8')
