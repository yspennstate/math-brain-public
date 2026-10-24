"""Independent exact weak-duality verification, without the assignment solver or NumPy."""
import pathlib,json,time
from fractions import Fraction
P=pathlib.Path(__file__).parent;start=time.monotonic();rows=[]
def value(mask,k):
 if k==1:return int(bin(mask).count('1')>=2)
 outputs=[bin((mask>>(3*i))&7).count('1')>=2 for i in range(3)]
 return int(sum(outputs)>=2)
for k in (1,2):
 c=json.loads((P/f'quadratic_transport_certificate_{k}.json').read_text());n=3**k
 lo=c['low'];hi=c['high'];N=len(lo)
 assert lo==[x for x in range(1<<n) if value(x,k)==0]
 assert hi==[x for x in range(1<<n) if value(x,k)==1]
 p=c['assignment'];u=c['row_potentials'];v=c['column_potentials']
 assert len(hi)==N and sorted(p)==list(range(N)) and len(u)==len(v)==N
 assert all(isinstance(x,int) for x in u+v)
 minimum=None
 for i,x in enumerate(lo):
  for j,y in enumerate(hi):
   d=bin(x^y).count('1');slack=d*d-u[i]-v[j]
   assert slack>=0
   minimum=slack if minimum is None else min(minimum,slack)
 primal=sum(bin(lo[i]^hi[p[i]]).count('1')**2 for i in range(N));dual=sum(u)+sum(v)
 assert primal==dual==c['total_cost']==c['dual_sum']
 cost=Fraction(primal,N);assert cost==(Fraction(5,2) if k==1 else Fraction(337,64))
 rows.append(dict(k=k,pointwise_dual_inequalities=N*N,min_slack=minimum,exact_primal_equals_dual=str(cost),seconds=time.monotonic()-start))
(P/'quadratic_transport_verification.json').write_text(json.dumps(rows,indent=2),encoding='utf8');print(json.dumps(rows,indent=2))
