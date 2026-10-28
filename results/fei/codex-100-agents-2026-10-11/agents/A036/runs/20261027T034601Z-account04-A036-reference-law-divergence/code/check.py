from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, time, sys, importlib.util

R=Path(__file__).resolve().parents[1]
old=R.parent/'20261023T135330Z-account03-A036-reference-law-divergence/code/exact.py'
spec=importlib.util.spec_from_file_location('own_interval',old)
ex=importlib.util.module_from_spec(spec);spec.loader.exec_module(ex)
start=time.monotonic(); checks=0; limit=55 if '--pilot' in sys.argv else 240; stats={'queries':0,'inside':0,'absorption':0,'ghost_rows':0,'trees':0}
def ck(x):
 global checks
 checks+=1
 assert x, (checks,stats)
 if checks%1000==0: assert time.monotonic()-start<limit

@lru_cache(None)
def vals(x):
 out={}
 for z,sgn in [(x.numerator,1),(x.denominator,-1)]:
  d=2
  while d*d<=z:
   while z%d==0:out[d]=out.get(d,0)+sgn;z//=d
   d+=1
  if z>1:out[z]=out.get(z,0)+sgn
 return tuple((p,e) for p,e in out.items() if e)
def word(terms):
 out={}
 for c,x in terms:
  if c:
   ck(x>0)
   for p,e in vals(x):out[p]=out.get(p,F(0))+c*e
 return {p:c for p,c in out.items() if c}
def add(*ws):
 out={}
 for w in ws:
  for p,c in w.items():out[p]=out.get(p,F(0))+c
 return {p:c for p,c in out.items() if c}
def scale(c,w):return {p:c*v for p,v in w.items() if c*v}
def kl(p,q):return word((x,x/y) for x,y in zip(p,q) if x)
def ent(p):return word((-x,x) for x in p if x)
def nonneg(w):
 if not w:return True
 a=ex.total(ex.scale(c,ex.logpoint(F(p))) for p,c in w.items())
 return a[0]>=0
@lru_cache(None)
def spectrum(t):
 n=len(t)
 a=tuple(F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),n) for s in range(n))
 p=tuple(v*v for v in a);ck(sum(p)==1)
 return a,p
def ref(p,J,alpha):
 if J==0:return p
 q=tuple((p[0] if s==0 else (1-alpha)*x+alpha*(1-p[0])*(s==J)) for s,x in enumerate(p))
 ck(sum(q)==1 and q[0]==p[0]);ck(all(y>0 for x,y in zip(p,q) if x))
 return q
def delete(s,i):return (s&((1<<i)-1))|((s>>(i+1))<<i)
def child(t,i,y):return tuple(v for x,v in enumerate(t) if (x>>i)&1==y)
@lru_cache(None)
def node(t,J,i,alpha):
 n=len(t).bit_length()-1;a,p=spectrum(t);q=ref(p,J,alpha)
 ts=tuple(child(t,i,y) for y in [0,1]); ps=tuple(spectrum(t)[1] for t in ts)
 pairs=[(s,s|(1<<i)) for s in range(len(p)) if not s&(1<<i)]
 pb=tuple(p[s]+p[z] for s,z in pairs); qb=tuple(q[s]+q[z] for s,z in pairs)
 ck(pb==tuple((x+y)/2 for x,y in zip(*ps)))
 kernels=tuple(tuple(pp/(2*x) if x else F(1,2) for pp,x in zip(py,pb)) for py in ps)
 ry=tuple(sum((x*k for x,k in zip(qb,ky)),F(0)) for ky in kernels)
 ck(sum(ry)==1 and min(ry)>=(1-alpha)/2)
 inherited=tuple(tuple(x*k/r for x,k in zip(qb,ky)) for ky,r in zip(kernels,ry))
 ck(all(sum(qy)==1 for qy in inherited))
 E=add(kl(p,q),scale(-1,kl(pb,qb)));O=kl((F(1,2),)*2,ry)
 Ki=scale(F(1,2),add(*(kl(py,qy) for py,qy in zip(ps,inherited))))
 ck(add(E,O,Ki)==kl(p,q));ck(nonneg(E) and nonneg(O) and nonneg(Ki))
 Jc=delete(J,i);fresh=tuple(ref(py,Jc,alpha) for py in ps)
 Kf=scale(F(1,2),add(*(kl(py,qy) for py,qy in zip(ps,fresh))))
 sig=add(Kf,scale(-1,Ki));ar=1-p[J]
 ac=tuple(1-py[Jc] for py in ps);b2=p[J^(1<<i)]
 ck(sum(ac)/2==ar-b2)
 bank=(n-1)*ar if J else 0
 bc=tuple((n-2)*x if Jc else 0 for x in ac)
 drop=bank-sum(bc)/2
 ell=word([(1,1/(1-alpha))])
 ck(drop>=0)
 ck(nonneg(add(scale(drop,ell),scale(-1,sig))))
 if J and Jc:ck(drop>=sum(ac)/2)
 if not Jc:ck(nonneg(scale(-1,sig)))
 if not J:ck(sig=={} and E=={} and O=={})
 stats['queries']+=1;stats['inside']+=bool(J&(1<<i));stats['absorption']+=bool(J and not Jc)
 stats['ghost_rows']+=sum(not x and y>0 for x,y in zip(pb,qb))
 return ts,Jc,E,O,sig,bank,bc

@lru_cache(None)
def tree(t,J,alpha,mode,depth=0):
 n=len(t).bit_length()-1;p=spectrum(t)[1];q=ref(p,J,alpha)
 if n==0 or (mode==2 and depth==1 and t[0]==1):
  return {},{}, {},kl(p,q),F(0) if not J else (n-1)*(1-p[J]),1-p[J]
 i=0 if mode==0 else n-1 if mode==1 else (sum(x==1 for x in t)+depth)%n
 ts,Jc,E,O,sig,B,bc=node(t,J,i,alpha)
 ch=[tree(s,Jc,alpha,mode,depth+1) for s in ts]
 sums=[scale(F(1,2),add(*(x[k] for x in ch))) for k in range(4)]
 Sigma=add(sig,sums[0]);Etot=add(E,sums[1]);Otot=add(O,sums[2]);Kterm=sums[3]
 Bt=sum(x[4] for x in ch)/2;At=sum(x[5] for x in ch)/2
 ck(add(Etot,Otot,Kterm)==add(kl(p,q),Sigma))
 ell=word([(1,1/(1-alpha))]);ck(nonneg(add(scale(B-Bt,ell),scale(-1,Sigma))))
 ck(At<=1-p[J])
 # Boolean entropy is a supermartingale under physical restrictions.
 ck(nonneg(add(ent(p),scale(F(-1,2),add(*(ent(spectrum(s)[1]) for s in ts))))))
 return Sigma,Etot,Otot,Kterm,Bt,At

def main():
 pilot='--pilot' in sys.argv;maxn=2 if pilot else 3
 for n in range(1,maxn+1):
  for f in range(1<<(1<<n)):
   t=tuple(-1 if f>>x&1 else 1 for x in range(1<<n))
   for alpha in [F(1,6),F(1,2)]:
    for J in range(1<<n):
     for i in range(n):node(t,J,i,alpha)
     if alpha==F(1,6):
      for mode in [0,1,2]:tree(t,J,alpha,mode);stats['trees']+=1
 for m in range(1,20):
  c=F(1)
  for k in range(1,m+1):
   ck(F((2*k-1)**2,4*k*k)<=F(k,k+1));c*=F(2*k-1,2*k)
  ck(c*c<=F(1,m+1))
 ck(6**15<16*5**15)
 ck(F(6*10,1024)*F(4,15)==F(1,64)) # strictness comes from ell<4/15
 ck(F(61,32)-F(1,4)==F(53,32))
 # Original source is more than sufficient after the retained quarter.
 ck(F(741,256)-F(1,64)>F(61,32))
 out={'status':'PASS','domain':f'all Boolean n=1..{maxn}; all anchors incl empty; all coordinates; alpha=1/6,1/2; three stopped/complete adaptive rules','checks':checks,'stats':stats,'seconds':time.monotonic()-start,'arithmetic':'Fraction; exact prime-log words; outward rational atanh log intervals; no floating signs','external_producer_code_imported':False}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps(out))
if __name__=='__main__':main()
