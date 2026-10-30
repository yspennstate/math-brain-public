from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,time
root=Path(__file__).resolve().parents[1]
spec={'version':'independent-prime-log-v1','family':'all Boolean signs n=1,2','domain':'every queried coordinate, every original single witness, b=1/3, deterministic ghost split','arithmetic':'exact rational prime-exponent logarithm expressions','memory_MB':50,'runtime_seconds':55,'case_count':136,'symmetry':'none'}
(root/'out/AUDIT_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
start=time.monotonic(); rows=0
def factors(x):
 d={}
 for a,sgn in [(x.numerator,1),(x.denominator,-1)]:
  j=2
  while j*j<=a:
   while a%j==0: d[j]=d.get(j,0)+sgn; a//=j
   j+=1
  if a>1:d[a]=d.get(a,0)+sgn
 return d
def logadd(d,x,c):
 if c:
  for p,e in factors(x).items(): d[p]=d.get(p,0)+c*e
def ce(p,q):
 d={}
 for a,b in zip(p,q):
  if a: logadd(d,b,-a)
 return d
def kl(p,q):
 d={}
 for a,b in zip(p,q):
  if a:logadd(d,a/b,a)
 return d
def plus(*terms):
 d={}
 for scale,t in terms:
  for p,e in t.items():d[p]=d.get(p,0)+scale*e
 return {p:e for p,e in d.items() if e}
def law(f):
 return tuple(F(sum(a*(-1 if (s&x).bit_count()%2 else 1) for x,a in enumerate(f)),len(f))**2 for s in range(len(f)))
def cal(p,q):
 if p[0]==1:return p
 return tuple(p[0] if s==0 else v*(1-p[0])/(1-q[0]) for s,v in enumerate(q))
for n in (1,2):
 N=1<<n
 for f in product((-1,1),repeat=N):
  p=law(f)
  for w in range(N):
   q=cal(p,tuple(v/3+(F(2,3) if s==w else 0) for s,v in enumerate(p)))
   for i in range(n):
    rem=[j for j in range(n) if j!=i]
    def emb(x,t):return sum(((x>>j)&1)<<k for j,k in enumerate(rem))|(t<<i)
    pc=[law(tuple(f[emb(x,t)] for x in range(N//2))) for t in (0,1)]
    m=tuple(sum(p[emb(u,t)] for t in (0,1)) for u in range(N//2))
    z=tuple(sum(q[emb(u,t)] for t in (0,1)) for u in range(N//2))
    k=[tuple(pc[t][u]/(2*m[u]) if m[u] else F(t==0) for u in range(N//2)) for t in (0,1)]
    rt=[sum(z[u]*k[t][u] for u in range(N//2)) for t in (0,1)]
    qc=[tuple(z[u]*k[t][u]/rt[t] for u in range(N//2)) for t in (0,1)]
    qs=[cal(pc[t],qc[t]) for t in (0,1)]
    H=ce(p,p); Hm=ce(m,m)
    B=plus((1,H),(-1,Hm)); J=plus((1,Hm),(-F(1,2),ce(pc[0],pc[0])),(-F(1,2),ce(pc[1],pc[1])))
    E=plus((1,kl(p,q)),(-1,kl(m,z))); O=kl((F(1,2),F(1,2)),rt)
    d=[kl((pc[t][0],1-pc[t][0]),(qc[t][0],1-qc[t][0])) for t in (0,1)]
    assert not plus((1,B),(F(1,2),ce(pc[0],qs[0])),(F(1,2),ce(pc[1],qs[1])),(-1,ce(p,q)),(1,J),(1,E),(1,O),(F(1,2),d[0]),(F(1,2),d[1]))
    assert not plus((1,kl(p,q)),(-1,E),(-1,O),(-F(1,2),d[0]),(-F(1,2),d[1]),(-F(1,2),kl(pc[0],qs[0])),(-F(1,2),kl(pc[1],qs[1])))
    rows+=1
    assert time.monotonic()-start<55
f=tuple(-1 if x==0 else 1 for x in range(8)); p=law(f)
assert p[0]==F(9,16) and all(x==F(1,16) for x in p[1:])
flat=(F(1,4),)*4
assert cal(flat,flat)==flat and flat[3]<F(1,3)
receipt={'status':'PASS','rows':rows,'complete_CE_identities':rows,'complete_KL_identities':rows,'floor_counterexample':'AND3 child AND2, matched law, empty1/4 and full1/4<1/3','seconds':time.monotonic()-start,'arithmetic':'rational prime-exponent forms; two full identities per row'}
(root/'out/AUDIT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
