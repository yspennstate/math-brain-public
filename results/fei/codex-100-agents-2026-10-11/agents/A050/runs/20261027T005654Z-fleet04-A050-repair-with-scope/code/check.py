from fractions import Fraction as F
from itertools import product, permutations
from functools import lru_cache
from pathlib import Path
import json, sys, time
R=Path(__file__).resolve().parents[1]
pilot='--pilot' in sys.argv
start=time.monotonic(); checks=nodes=trees=projections=ghosts=endpoints=0
def ck(v):
 global checks
 checks+=1
 assert v
 if checks%1024==0: assert time.monotonic()-start < (55 if pilot else 110)
@lru_cache(None)
def spectrum(tab):
 N=len(tab); a=list(tab); h=1
 while h<N:
  for k in range(0,N,2*h):
   for j in range(k,k+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 p=tuple(F(z*z,N*N) for z in a)
 direct=tuple(F(sum(tab[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N)),N)**2 for s in range(N))
 ck(p==direct); ck(sum(p)==1)
 return p
def erase(a,i):
 out=[F(0)]*(len(a)//2)
 for s,v in enumerate(a): out[(s&((1<<i)-1))|((s>>(i+1))<<i)]+=v
 return tuple(out)
def children(tab,i):
 return [tuple(tab[(x&((1<<i)-1))|((x>>i)<<(i+1))|(t<<i)] for x in range(len(tab)//2)) for t in (0,1)]
def calibrate(p,q,b,w):
 global projections,endpoints
 r=p[0]; z=q[0]; n=len(p)
 if r==1:
  endpoints+=1; return p,F(1),{0:F(0)}
 ck(z<1)
 k=(1-r)/(1-z); bp=b*k
 ck(0<bp<=1)
 wp={j:k*c for j,c in w.items() if j!=0}
 wp[0]=r*(1-bp)
 qp=tuple((r if s==0 else k*q[s]) for s in range(n))
 ck(sum(qp)==1); ck(qp[0]==r)
 ck(all(qp[s]==bp*p[s]+wp.get(s,0) for s in range(n)))
 # Each occupied log-ratio equals the corresponding binary-cell ratio.
 for s in range(n):
  if p[s]: ck(qp[s]/q[s]==(r/z if s==0 else (1-r)/(1-z)))
 ck(all(c>=0 for c in wp.values())); ck(bp+sum(wp.values())==1)
 if z!=r: projections+=1
 if r==0: endpoints+=1
 return qp,bp,wp
def walk(tab,q,b,w,labels,order,split,depth=0):
 global nodes,ghosts
 p=spectrum(tab); nodes+=1
 ck(sum(q)==1); ck(b>0); ck(all(q[s]>=b*p[s] for s in range(len(p))))
 ck(all(q[s]==b*p[s]+w.get(s,0) for s in range(len(p))))
 ck(p[0]==q[0])
 if len(tab)==1: return
 chosen=(min(labels) if depth%2==0 else max(labels)) if order is None else next(j for j in order if j in labels)
 i=labels.index(chosen); rem=tuple(j for j in labels if j!=chosen)
 cs=children(tab,i); ps=[spectrum(t) for t in cs]
 m=erase(p,i); z=erase(q,i)
 ck(all((ps[0][u]+ps[1][u])/2==m[u] for u in range(len(m))))
 ks=[]
 for t in (0,1): ks.append(tuple(ps[t][u]/(2*m[u]) if m[u] else (F(1,2) if split==0 else F(t==0)) for u in range(len(m))))
 ck(all(ks[0][u]+ks[1][u]==1 for u in range(len(m))))
 rs=[sum(z[u]*ks[t][u] for u in range(len(m))) for t in (0,1)]
 ck(sum(rs)==1)
 for t in (0,1):
  rt=rs[t]; ck(rt>=b/2>0)
  wt={}
  for j,c in w.items():
   u=(j&((1<<i)-1))|((j>>(i+1))<<i)
   wt[u]=wt.get(u,F(0))+c*ks[t][u]/rt
  bt=b/(2*rt); qt=tuple(z[u]*ks[t][u]/rt for u in range(len(m)))
  ck(all(qt[u]==bt*ps[t][u]+wt.get(u,0) for u in range(len(m))))
  ghosts+=sum(1 for u,c in wt.items() if c and not ps[t][u])
  # Exact atomwise KL chain: erased likelihood = outcome ratio * child likelihood.
  for u in range(len(m)):
   if ps[t][u]: ck(m[u]/z[u]==F(1,2)/rt*ps[t][u]/qt[u])
  qp,bp,wp=calibrate(ps[t],qt,bt,wt)
  ck(len([j for j,c in wp.items() if c and j!=0])<=len([j for j,c in w.items() if c and j!=0]))
  walk(cs[t],qp,bp,wp,rem,order,split,depth+1)
for n in range(0,3 if pilot else 4):
 N=1<<n
 for tab in product((-1,1),repeat=N):
  p=spectrum(tab)
  for witness in set((0,N-1,1 if n else 0)):
   b=F(1,2); w={witness:F(1,2)}
   q=tuple(b*v+w.get(s,0) for s,v in enumerate(p))
   q,b,w=calibrate(p,q,b,w)
   for order in list(permutations(range(n)))+[None]:
    for split in (0,1):
     trees+=1; walk(tab,q,b,w,tuple(range(n)),order,split)
receipt={'status':'PASS','pilot':pilot,'trees':trees,'nodes':nodes,'assertions':checks,'nontrivial_calibrations':projections,'ghost_occurrences':ghosts,'endpoint_calibrations':endpoints,'seconds':time.monotonic()-start,'arithmetic':'Fraction; direct Walsh and FWHT; atomwise log-ratio identities; signs analytic Gibbs inequality'}
(R/'out'/('PILOT.json' if pilot else 'MAIN.json')).write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
