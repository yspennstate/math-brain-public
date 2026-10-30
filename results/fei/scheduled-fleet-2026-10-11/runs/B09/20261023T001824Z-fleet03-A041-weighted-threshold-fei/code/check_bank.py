from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json,time
root=Path(__file__).resolve().parents[1]
spec={'helper':'A041-pivotal-cap-v1','family':'all Boolean signs on three labelled variables','domain':'partition {0}|{1,2}; fair, all 1/4, and (1/4,1/2,3/4)','case_count':768,'symmetry':'none','arithmetic':'exact Fraction; direct physical and Fourier sums','memory_estimate_MB':50,'max_runtime_seconds':60}
(root/'out/FROZEN_BANK_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
t=time.monotonic(); count=0; checks=0
xs=list(product((0,1),repeat=3)); groups=({0},{1,2})
for ps in [(Q(1,2),)*3,(Q(1,4),)*3,(Q(1,4),Q(1,2),Q(3,4))]:
 v=[4*p*(1-p) for p in ps]
 mu={x:__import__('functools').reduce(lambda a,i:a*(ps[i] if x[i] else 1-ps[i]),range(3),Q(1)) for x in xs}
 for table in range(256):
  f={x:Q(1 if table>>j&1 else -1) for j,x in enumerate(xs)}
  masses={}
  for mask in range(8):
   S=[i for i in range(3) if mask>>i&1]
   a=sum((mu[x]*f[x]*__import__('functools').reduce(lambda z,i:z*((2*x[i]-1)-(2*ps[i]-1)),S,Q(1)) for x in xs),Q(0))
   masses[mask]=a*a/__import__('functools').reduce(lambda z,i:z*v[i],S,Q(1))
  Is=[sum((p for s,p in masses.items() if s>>i&1),Q(0)) for i in range(3)]
  caps=[]
  for i in range(3):
   own=next(g for g in groups if i in g); same=sorted(own-{i}); opp=sorted(set(range(3))-own)
   vals=[]
   for a in product((0,1),repeat=len(same)):
    qi=Q(0)
    for b in product((0,1),repeat=len(opp)):
     x=[0]*3
     for j,z in zip(same,a):x[j]=z
     prob=Q(1)
     for j,z in zip(opp,b):x[j]=z;prob*=ps[j] if z else 1-ps[j]
     x[i]=0;y=x.copy();y[i]=1
     qi+=prob*(f[tuple(x)]!=f[tuple(y)])
    vals.append(qi)
   caps.append(max(vals))
  pure=mixed=M=D=Q(0)
  for s,p in masses.items():
   S={i for i in range(3) if s>>i&1}; degree=len(S)
   if S&groups[0] and S&groups[1]:mixed+=degree*p;M+=p;D+=(degree-1)*p
   else:pure+=degree*p
  bank=sum(((1-caps[i])*Is[i] for i in range(3)),Q(0))
  assert pure<=sum((caps[i]*Is[i] for i in range(3)),Q(0))
  assert mixed>=bank and 2*D>=bank
  assert pure+mixed==sum(Is) and mixed==D+M
  count+=1;checks+=5
  if time.monotonic()-t>60:raise RuntimeError('frozen runtime exceeded')
out={'status':'PASS','cases':count,'assertions':checks,'runtime_seconds':time.monotonic()-t,'spec':spec}
(root/'out/BANK_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
