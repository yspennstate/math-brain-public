from pathlib import Path
from fractions import Fraction as Q
import json,math
from itertools import product
E={(i,j) for i in range(4) for j in range(4,8)};H=(E-{(0,4),(1,5)})|{(0,1),(4,5)}
checks=0
for edges in [E,H]:
 adj=[sorted(w for a,b in edges for u,w in [(a,b),(b,a)] if u==v) for v in range(8)]
 directed=[(u,v) for u in range(8) for v in adj[u]]
 for r in [2,3,4]:
  for mask in range(256):
   Z=[(mask>>v)&1 for v in range(8)];current=Z.copy();msgs={(u,v):Z[u] for u,v in directed}
   for t in range(1,9):
    predicted=[Z[v] and sum(msgs[(u,v)] for u in adj[v])>=r for v in range(8)]
    nxt=[current[v] and sum(current[u] for u in adj[v])>=r for v in range(8)]
    assert predicted==nxt
    msgs={(u,v):Z[u] and sum(msgs[(w,u)] for w in adj[u] if w!=v)>=r-1 for u,v in directed}
    current=nxt;checks+=1
for i in range(101):
 z=Q(i,1010);eta=Q(i-50,997);x=Q(3,4)+z;q=Q(8,9)
 assert q*(3*x*x-2*x**3)-x==-Q(4,3)*z*z-Q(16,9)*z**3
 assert q*(4*x**3-3*x**4)-Q(21,32)==Q(3,2)*z-z*z-Q(40,9)*z**3-Q(8,3)*z**4
 assert (q+eta)*(3*x*x-2*x**3)-x==-Q(4,3)*z*z-Q(16,9)*z**3+eta*(Q(27,32)+Q(9,8)*z-Q(3,2)*z*z-2*z**3)
# Explicit joint root survival by enumeration of adjacent stars and distance-two stars.
covchecks=0
for d in [3,4]:
 for r in range(2,d+1):
  for q in [Q(1,5),Q(1,2),Q(8,9)]:
   probbin=lambda j:sum(Q(math.comb(d-1,l))*q**l*(1-q)**(d-1-l) for l in range(j,d))
   Ar=probbin(r);Am=probbin(r-1)
   for dist in [1,2]:
    if dist==1:
     L=2*d;N0=[1]+list(range(2,d+1));N1=[0]+list(range(d+1,2*d));jointformula=q*q*Am*Am
    else:
     L=2*d+1;N0=[2]+list(range(3,d+2));N1=[2]+list(range(d+2,2*d+1));jointformula=q*q*((1-q)*Ar*Ar+q*Am*Am)
    exact=Q(0)
    for bits in product([0,1],repeat=L):
     if bits[0] and bits[1] and sum(bits[v] for v in N0)>=r and sum(bits[v] for v in N1)>=r:
      vac=sum(bits);exact+=q**vac*(1-q)**(L-vac)
    assert exact==jointformula;covchecks+=1
out=dict(message_peeling_checks=checks,polynomial_sample_checks=303,explicit_joint_star_checks=covchecks,arithmetic='exact integers and Fraction',all_passed=True)
Path('second_finite_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(out)
