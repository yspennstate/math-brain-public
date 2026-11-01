"""Exact finite chains, and a boundary-coupling obstruction. No Monte Carlo."""
from fractions import Fraction
import collections, json, math, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
def neighbors(mask,n):
 for x in range(n):
  legal=(x>0 and mask>>(x-1)&1) or (x+1<n and mask>>(x+1)&1)
  if legal: yield mask^(1<<x),x
checks=[]
for n in range(2,10):
 seen={1}; queue=collections.deque([1])
 while queue:
  a=queue.popleft()
  for b,x in neighbors(a,n):
   if b not in seen: seen.add(b);queue.append(b)
 assert seen==set(range(1,1<<n))
 assert all(b for a in seen for b,x in neighbors(a,n))
 checks.append({'n':n,'nonempty_states_reached':len(seen),'expected':(1<<n)-1})
db=[]
for n in range(2,8):
 for q in [Fraction(1,10),Fraction(1,3),Fraction(1,2),Fraction(9,10)]:
  p=1-q; z=1-p**n
  weight=lambda a:q**a.bit_count()*p**(n-a.bit_count())/z
  for a in range(1,1<<n):
   for b,x in neighbors(a,n):
    rab=p if a>>x&1 else q
    rba=p if b>>x&1 else q
    assert weight(a)*rab==weight(b)*rba
  db.append({'n':n,'q':str(q),'detailed_balance':'exact rational passed'})
# A frozen infected boundary is already wrong for a single mutable site.
# Under healthy exterior and one infection the spin is frozen infected.
# With an infected exterior boundary it heals at rate p instead.
result={'connectivity':checks,'detailed_balance':db,
 'boundary_counterexample':{'q':0.3,'t':1,'true_healthy_probability':0,
   'frozen_infected_boundary_healthy_probability':0.7*(1-math.exp(-1))},
 'scope':'Finite interval with healthy exterior, restricted to nonempty class. Does not imply infinite-volume convergence.'}
(ROOT/'finite_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
