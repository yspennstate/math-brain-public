"""Adversarial delayed-reset and beta-martingale certificates."""
import check as c
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import time,json,hashlib
start=time.monotonic();paths=0
a,b=c.rows((-1,)*4)
h=tuple(-1 if t in (0,1,2,4) else 1 for t in range(16))
r=(F(1,4),)+tuple(F(3,4)*x for x in c.mix(c.profile(15,0),c.profile(15,1),F(1,8)))
for s in (1,-1):
 for order in [('controller','seed'),('seed','controller')]:
  for outcomes in product((0,1),repeat=2):
   aa,bb,hh,rr=a,b,h,r;q=c.coherent(aa,bb,hh,rr,s)
   for kind,bit in zip(order,outcomes):
    if kind=='seed':
     j=len(aa).bit_length()-1;hh=c.restrict(hh,0,bit);rr=c.marginal(rr,0)
    else:j=3;aa=c.restrict(aa,3,bit);bb=c.restrict(bb,3,bit)
    q=c.marginal(q,j)
   pp=c.prob(c.truth(aa,bb,hh,s));qn,rc=c.fresh(aa,bb,hh,rr,s)
   credit=c.kl(c.coarse(pp,len(aa),'controller'),c.coarse(q,len(aa),'controller'))
   c.ok(c.add((1,c.ce(pp,q)),(-1,c.ce(pp,qn)))==credit);c.ok(c.sign(credit)>=0)
   paths+=1
   if time.monotonic()-start>45:raise TimeoutError('frozen audit45s')
transitions=0
for state in product((-1,0,1),repeat=4):
 a,b=c.rows(state);beta=F(sum(b),len(b))
 for i,v in enumerate(state):
  if v!=-1:continue
  kids=[tuple(bit if k==i else z for k,z in enumerate(state)) for bit in (0,1)]
  c.ok(sum(F(sum(c.rows(k)[1]),len(c.rows(k)[1])) for k in kids)/2==beta);transitions+=1
c.ok(paths==16 and transitions==108)
out=dict(status='PASS',delayed_two_query_paths=paths,beta_states=81,beta_transitions=transitions,assertions=c.checks,seconds=time.monotonic()-start,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),core_sha256=hashlib.sha256(Path(c.__file__).read_bytes()).hexdigest(),issue='coherent reset after optional unreset seed/controller steps; actual martingale without independence shortcut')
c.save('adversarial_audit.json',out);print(json.dumps(out))
