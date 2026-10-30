"""Independent exact prime-log audit. Imports no producer or interval helper."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,hashlib
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks;assert time.perf_counter()-start<55
def spectrum(t):
 n=len(t)
 return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)),n)**2 for s in range(n)]
def reference(p,j):
 q=[F(5,6)*v for v in p];q[0]=p[0];q[j]+=F(1,6)*(1-p[0]);return q
@lru_cache(None)
def factor(n):
 out={};d=2
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def logadd(w,x,c):
 for p,e in factor(x.numerator).items():w[p]=w.get(p,F(0))+c*e
 for p,e in factor(x.denominator).items():w[p]=w.get(p,F(0))-c*e
def kl(p,q):
 w={}
 for a,b in zip(p,q):
  if a:ck(b>0);logadd(w,a/b,a)
 return {p:c for p,c in w.items() if c}
def linear(*terms):
 w={}
 for c,v in terms:
  for p,e in v.items():w[p]=w.get(p,F(0))+c*e
 return {p:c for p,c in w.items() if c}
def erase_mask(s,i):return (s&((1<<i)-1))|((s>>(i+1))<<i)
def restriction(t,i,y):
 return [t[x] for x in range(len(t)) if ((x>>i)&1)==y]
def transact(t,p,q,i):
 ts=[restriction(t,i,y) for y in [0,1]];ps=[spectrum(v) for v in ts];N=len(p)//2
 pb=[F(0)]*N;qb=[F(0)]*N
 for s in range(len(p)):pb[erase_mask(s,i)]+=p[s];qb[erase_mask(s,i)]+=q[s]
 ck(pb==[(a+b)/2 for a,b in zip(*ps)])
 ks=[[a/(2*b) if b else F(1,2) for a,b in zip(v,pb)] for v in ps]
 norms=[sum((a*b for a,b in zip(qb,k)),F(0)) for k in ks];ck(sum(norms)==1 and min(norms)>0)
 qs=[[a*b/r for a,b in zip(qb,k)] for k,r in zip(ks,norms)]
 for v in qs:ck(sum(v)==1)
 E=linear((1,kl(p,q)),(-1,kl(pb,qb)));O=kl([F(1,2)]*2,norms)
 kin=[kl(a,b) for a,b in zip(ps,qs)]
 ck(not linear((1,kl(p,q)),(-1,E),(-1,O),(-F(1,2),kin[0]),(-F(1,2),kin[1])))
 return ts,ps,qs,E,O
def main():
 queries=0;ghosts=0;words=0
 for truth in range(256):
  t=[1-2*((truth>>x)&1) for x in range(8)];p=spectrum(t)
  for J in range(1,8):
   q=reference(p,J);ck(sum(q)==1 and q[0]==p[0]);ghosts+=sum(bool(b) and not a for a,b in zip(p,q))
   decomposition={};logadd(decomposition,F(6,5),1-p[0]-p[J])
   if p[J]:logadd(decomposition,p[J]/q[J],p[J])
   ck(not linear((1,kl(p,q)),(-1,decomposition)))
   for i in range(3):
    if J>>i&1:continue
    ts,ps,qs,E,O=transact(t,p,q,i);Jc=erase_mask(J,i);a=1-p[J];ac=[1*v[0]+sum(v[1:])-v[Jc] for v in ps]
    ck(sum(ac)/2==a-p[J|(1<<i)])
    r=3-J.bit_count();drop=r*a-(r-1)*sum(ac)/2
    ck(drop>=sum(ac)/2)
    fresh=[kl(v,reference(v,Jc)) for v in ps];old=[kl(v,qq) for v,qq in zip(ps,qs)]
    sigma=linear((F(1,2),fresh[0]),(F(1,2),fresh[1]),(-F(1,2),old[0]),(-F(1,2),old[1]))
    ck(not linear((1,sigma),(-F(1,2),fresh[0]),(-F(1,2),fresh[1]),(1,kl(p,q)),(-1,E),(-1,O)))
    queries+=1;words+=1
 ck(6**15<2**4*5**15)
 ck(6*10*F(1,1024)*F(4,15)==F(1,64))
 ck(F(741,256)-F(1,64)-F(1,4)==F(673,256))
 out={'status':'PASS','all_three_bit_queries':queries,'prime_log_chain_and_reset_identities':words,'reference_only_atoms':ghosts,'assertions':checks,'seconds':time.perf_counter()-start,'imports_producer':False,'arithmetic':'Literal Walsh; exact Fraction kernels; prime valuation log words; zero interval or floating arithmetic'}
 (R/'out/INDEPENDENT_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
