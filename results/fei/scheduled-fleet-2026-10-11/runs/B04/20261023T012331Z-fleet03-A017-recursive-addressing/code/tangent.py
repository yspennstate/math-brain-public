from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,time,sys
R=Path(__file__).resolve().parents[1]
def phase(n,edges):return [(-1)**(sum((x>>i&1)*(x>>j&1) for i,j in edges)%2) for x in range(1<<n)]
def influence(f,j):return F(sum(v!=f[x^(1<<j)] for x,v in enumerate(f)),len(f))
start=time.perf_counter();pilot='--pilot' in sys.argv;cases=checks=0;boundary=None
for n in [4,5,6]:
 N=1<<n;q=phase(n,[(0,1),(2,3)]);inside=[x for x in range(N) if x&2];outside=[x for x in range(N) if not x&2]
 if n==4:
  sets=[{x for j,x in enumerate(inside) if code>>j&1} for code in range(16 if pilot else 256)]
 else:
  sets=[set(),set(inside),{x for x in inside if q[x]<0},{x for x in inside if q[x]>0},set(inside[:len(inside)//2]),set(inside[len(inside)//2:]),set(inside[::2]),set(inside[1::2])]
 outs=[s for k in range(N//32+1) for s in combinations(outside,k)]
 if pilot:outs=outs[:4]
 for Ei in sets:
  for Eo in outs:
   E=Ei|set(Eo);f=[v*(-1 if x in E else 1) for x,v in enumerate(q)];I=influence(f,2);lower=F(1,4)-F(2*len(Eo),N)
   assert I>=lower>=F(3,16);checks+=2;cases+=1
   if n==6 and len(Eo)==2 and I==F(3,16):boundary={'inside_edits':sorted(Ei),'outside_edits':list(Eo),'influence':str(I)}
# Break each structural hypothesis using actual Boolean functions.
n=6;N=64;q=phase(n,[(0,1),(1,2)]);E={x for x,v in enumerate(q) if v<0};assert all(x&2 for x in E)
f=[1]*N;assert influence(f,1)==influence(f,2)==0;checks+=2
q=phase(n,[(0,1),(2,3)]);Ei={x for x in range(N) if x&2 and q[x]<0};Eo={8,9,24};E=Ei|Eo;f=[v*(-1 if x in E else 1) for x,v in enumerate(q)]
assert influence(f,2)==F(5,32)<F(3,16);checks+=1
assert 3**3*13**13>2**52;checks+=1
res={'status':'PASS','pilot':pilot,'actual_parent_cases':cases,'assertions':checks,'sharp_boundary':boundary,'counterexamples':{'non_tangent_row':'q=x1*(x0+x2), i0,j1,E=negative(q) contained in P; edited phase constant','dependent_tangent_row':'same q,i0,j2,rows Qj=Qi; edited phase constant','outside_density_above_threshold':{'outside_edits':[8,9,24],'influence':'5/32','allowed_threshold':'3/16'}},'elapsed_seconds':time.perf_counter()-start}
(R/'out'/('tangent_pilot.json' if pilot else 'tangent_certificate.json')).write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in res.items() if k not in ['sharp_boundary','counterexamples']}))
