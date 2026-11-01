"""80-digit checks strictly inside the explicitly proved radius, all upper sets on C4."""
import json,pathlib
from fractions import Fraction as R
import mpmath as mp
P=pathlib.Path(__file__).resolve().parent
mp.mp.dps=80;n=4
events=[]
for table in range(1<<16):
 f=[(table>>mask)&1 for mask in range(16)]
 if all(f[mask]<=f[mask|(1<<i)] for mask in range(16) for i in range(n)):events.append(f)
assert len(events)==168
def num(x):return mp.mpf(x.numerator)/x.denominator
q=[0,mp.mpc(1,1),2,mp.mpc(1,-1)]
H=mp.matrix([[q[(j-i)%n] for j in range(n)] for i in range(n)])
records=[]
for t in [R(1,5),R(1,2),R(4,5)]:
 a=min(t,1-t);c=a/2;T=max(t,1-t)
 L=3**n*(n**3+R(n**3+6*n*n+6*n)/c**3)
 delta=min(a/2,a**(n-2)/(4*T*L))/2 # sqrt(4)=2
 for sign in [-1,1]:
  epsilon=sign*delta/32
  Q=num(t)*mp.eye(n)+num(epsilon)*H+num(epsilon/R(7))*mp.eye(n)
  # ||H||<=n max_ij |H_ij|<=8. Thus this bound is strictly inside delta.
  norm_bound=abs(epsilon)*(8+R(1,7));assert norm_bound<delta
  inc=[]
  for mask in range(16):
   ix=[i for i in range(n) if mask>>i&1]
   d=mp.det(mp.matrix([[Q[i,j] for j in ix] for i in ix])) if ix else mp.mpf(1)
   assert abs(mp.im(d))<mp.mpf('1e-70');inc.append(mp.re(d))
  p=mp.root(inc[-1],n);mu=list(inc)
  for i in range(n):
   for mask in range(16):
    if not(mask>>i&1):mu[mask]-=mu[mask|(1<<i)]
  nu=[p**mask.bit_count()*(1-p)**(n-mask.bit_count()) for mask in range(16)]
  gaps=[sum(mu[mask]-nu[mask] for mask in range(16) if f[mask]) for f in events]
  assert min(gaps)>-mp.mpf('1e-70')
  strict=[v for f,v in zip(events,gaps) if any(f) and not all(f) and sum(f)!=1]
  assert min(strict)>0
  records.append({'t':str(t),'sign':sign,'certified_radius_exact':str(delta),'certified_radius_decimal':mp.nstr(num(delta),40),'perturbation_norm_upper_bound_exact':str(norm_bound),'comparisons':len(gaps),'min_gap':mp.nstr(min(gaps),50),'min_nontrivial_non_top_gap':mp.nstr(min(strict),50)})
P.joinpath('certified_radius_results.json').write_text(json.dumps(records,indent=2))
print('CERTIFIED_RADIUS_EVENT_CHECKS_PASS',len(records)*len(events),'all-event comparisons at 80 digits')
print(json.dumps(records,indent=2))
