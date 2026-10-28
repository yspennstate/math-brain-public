import json,time
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
src=(R.parent/'20261014T055119Z-account05-A019-orthogonality-extensions/code/check_exposure.py').read_text(encoding='utf-8')
ns={'Q':Q,'lru_cache':lru_cache,'checks':0}
exec(src[src.index('def ck(x):'):src.index("transport={'positive'")],ns)
ck,ce,add,psi,nn=[ns[s] for s in ('ck','ce','add','psi','nonnegative')]
start=time.monotonic();cases=0
def direct(tt):
 return tuple(Q(sum(val*(-1 if (s&x).bit_count()%2 else 1) for x,val in enumerate(tt)),len(tt))**2 for s in range(len(tt)))
def activation(h,q):
 tt=tuple(1 if x==0 else h[y]*(-1 if z==0 else 1) for z in range(4) for y in range(len(h)) for x in range(2))
 p=direct(tt);ref=[]
 for j in range(4*len(h)):
  v=(q[j%len(h)]/4+int(j==0))/2;mass=p[2*j]+p[2*j+1]
  ref.extend((v*p[2*j]/mass,v*p[2*j+1]/mass) if mass else (v,Q(0)))
 ck(sum(ref)==1);ck(sum(p)==1)
 return ce(p,ref)
for k in (2,3):
 for kind in ('opposite','one_biased'):
  e=Q(1,1<<k)
  base=tuple(1-2*u for v in range(1<<k) for u in range(2))
  plus=tuple(1 if v==0 else 1-2*u for v in range(1<<k) for u in range(2))
  minus=tuple(-1 if v==0 else 1-2*u for v in range(1<<k) for u in range(2))
  a,b=(plus,minus) if kind=='opposite' else (base,plus)
  pa,pb=direct(a),direct(b)
  qa=tuple((p+int(i==0))/2 for i,p in enumerate(pa));qb=tuple((p+int(i==0))/2 for i,p in enumerate(pb))
  h=tuple(z for pair in zip(a,b) for z in pair);ph=direct(h);qh=[]
  for i in range(len(a)):
   m=ph[2*i]+ph[2*i+1];v=(qa[i]+qb[i])/2
   qh.extend((v*ph[2*i]/m,v*ph[2*i+1]/m) if m else (v,Q(0)))
  costs=[activation(z,q) for z,q in ((a,qa),(b,qb),(h,tuple(qh)))];cases+=3
  beta=[Q(sum(z),len(z)) for z in (a,b,h)]
  # Direct complete CE compared with independently scalarized empty-row refund.
  Ds=[]
  for z,p,q,beta0,cost in zip((a,b,h),(pa,pb,ph),(qa,qb,qh),beta,costs):
   r=beta0**2/4;v=q[0]/4
   D=add((Q(1,2),ns['logform'](1+v))) if not r else add((Q(1,2),ce((r,1),(v,1))),(-Q(1,2),ce((r,1),(r,1))),((1+r)/2,ns['logform']((1+v)/(1+r))))
   ck(cost==add((Q(1,2),ce(p,q)),(1,{2:Q(1)}),(1,psi(beta0/2)),(-1,D)))
   Ds.append(D)
  kl=lambda p,q:add((1,ce(p,q)),(-1,ce(p,p)))
  dc=add((Q(1,2),kl(pa,qa)),(Q(1,2),kl(pb,qb)),(-1,kl(ph,qh)))
  lam=add((Q(1,2),Ds[0]),(Q(1,2),Ds[1]),(-1,Ds[2]),(-Q(1,2),dc))
  ck(nn(lam));assert time.monotonic()-start<60
out={'status':'PASS','full_activation_cases':cases,'checks':ns['checks'],'seconds':time.monotonic()-start,'method':'literal character summation, complete reference cost; no fast Walsh or old gate helper used','full_fei':'OPEN'}
(R/'out/DIRECT_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
