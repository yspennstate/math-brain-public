"""Independent exact full physical hull certificate, actual Boolean spectra."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json,time,sys,hashlib
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True)
G=1<<192;CHECKS=0
T=[('P',0)]+[('A',m) for m in range(6)]+[('L',m) for m in range(2,7)];ROOT=11
def ck(b):
 global CHECKS
 assert b;CHECKS+=1
def ceildiv(a,b):return -((-a)//b)
def save(n,d):(R/'out'/n).write_text(json.dumps(d,indent=2,default=str)+'\n',encoding='utf-8',newline='\n')
def plus(*xs):return sum(x[0] for x in xs),sum(x[1] for x in xs)
def scale(x,c):
 a,b=x if c>=0 else (x[1],x[0]);return (a*c).__floor__(),(b*c).__ceil__()
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mean(a,b):return (a[0]+b[0])//2,ceildiv(a[1]+b[1],2)
def ser(z):
 # 0<=z<=1/3. Positive atanh series, interval multiplication and divisions.
 ck(0<=z<=F(1,3));zl=(z*G).__floor__();zh=(z*G).__ceil__()
 z2l=zl*zl//G;z2h=ceildiv(zh*zh,G);pl,ph=zl,zh;lo=hi=0
 for j in range(48):
  lo+=2*pl//(2*j+1);hi+=ceildiv(2*ph,2*j+1)
  pl=pl*z2l//G;ph=ceildiv(ph*z2h,G)
 # True analytic tail <=3^-96, independent of fixed-point overestimates.
 return lo,hi+ceildiv(G,3**96)
LN=ser(F(1,3))
@lru_cache(None)
def log(x):
 ck(x>0);k=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**k
 if y<1:y*=2;k-=1
 ck(1<=y<2)
 if y==1:return k*G,k*G
 a,b=ser((y-1)/(y+1))
 return k*G+a*G//LN[1],k*G+ceildiv(b*G,LN[0])
@lru_cache(None)
def ell(x):
 if not x:return (0,0)
 ck(0<x<=1);a,b=log(x);return (-x*b).__floor__(),(-x*a).__ceil__()
def entropy(ps):return plus(*(ell(x) for x in ps))
def truth(t):
 k,m=t
 return (1,) if k=='P' else tuple(-1 if x in ({0} if k=='A' else {0,1,2}) else 1 for x in range(1<<m))
def child(t,j,b):return tuple(y for x,y in enumerate(t) if x>>j&1==b)
def walsh(t):
 w=list(t);s=1
 while s<len(w):
  for a in range(0,len(w),2*s):
   for j in range(a,a+s):u,v=w[j],w[j+s];w[j],w[j+s]=u+v,u-v
  s*=2
 return [F(x,len(w)) for x in w]
def canon(t):
 while len(t)>1:
  j=next((j for j in range(len(t).bit_length()-1) if child(t,j,0)==child(t,j,1)),None)
  if j is None:break
  t=child(t,j,0)
 return t
def acts(t):
 k,m=t
 if k=='P' or not m:return []
 if k=='A':return [(0,T.index(('A',m-1)),0)]
 return [(0,T.index(('A',m-2)),T.index(('A',m-1)))]+([(2,T.index(('L',m-1)),0)] if m>=3 else [])
ACT=[acts(t) for t in T]
def init():
 cores=[]
 for t in T:
  tab=truth(t);w=walsh(tab);n=len(tab);dim=n.bit_length()-1
  ck(all(w[s]==F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(tab)),n) for s in range(n)))
  ck(sum(v*v for v in w)==1)
  ds=[]
  for j in range(dim):
   d=F(sum(tab[x]!=tab[x^(1<<j)] for x in range(n)),n);ck(d==sum(v*v for s,v in enumerate(w) if s>>j&1));ds.append(d)
  cores.append({'mu':w[0],'var':1-w[0]**2,'I':sum(ds),'H':entropy([v*v for v in w]),'ds':ds,'nonempty':Counter(v*v for v in w[1:] if v)})
 tab=truth(('L',6));ct=nr=0
 for ass in product([-1,0,1],repeat=6):
  raw=tuple(tab[x] for x in range(64) if all(b<0 or x>>i&1==b for i,b in enumerate(ass)));v=canon(raw)
  ck(v in [truth(t) for t in T]);i=[truth(t) for t in T].index(v);ct+=1
  for j in range(len(raw).bit_length()-1):
   aa,bb=canon(child(raw,j,0)),canon(child(raw,j,1));nr+=1
   ck(aa==bb==v or any((aa,bb)==(truth(T[a]),truth(T[b])) or (bb,aa)==(truth(T[a]),truth(T[b])) for _,a,b in ACT[i]))
 return cores,{'labelled_restrictions':ct,'labelled_physical_rows':nr}
NEG={0,1,2,4,8,16,32,6,17,40};K=tuple(1 if z<<2 in NEG else -1 for z in range(16));W=walsh(K)
C=[]
def full(ts,atoms=False):
 cs=[C[i] for i in ts];mus=[c['mu'] for c in cs];vs=[c['var'] for c in cs];ps=[];coef=[]
 for B in range(16):
  v=F(0)
  for U in range(16):
   if U&B!=B:continue
   a=W[U]
   for j in range(4):
    if (U^B)>>j&1:a*=mus[j]
   v+=a
  p=v*v
  for j in range(4):
   if B>>j&1:p*=vs[j]
  coef.append(v);ps.append(p)
 ck(sum(ps)==1)
 qs=[]
 for j in range(4):
  q=F(0)
  for z in range(16):
   if z>>j&1 or K[z]==K[z|1<<j]:continue
   a=F(1)
   for i in range(4):
    if i!=j:a*=((1-mus[i])/2 if z>>i&1 else (1+mus[i])/2)
   q+=a
  ck(sum(p for B,p in enumerate(ps) if B>>j&1)==q*vs[j]);qs.append(q)
 I=sum(q*c['I'] for q,c in zip(qs,cs));H=entropy(ps)
 for q,c in zip(qs,cs):H=plus(H,scale(sub(c['H'],entropy([c['var'],1-c['var']])),q))
 if atoms:
  counts=Counter()
  for B,v in enumerate(coef):
   if not v:continue
   ids=[j for j in range(4) if B>>j&1]
   for row in product(*(list(cs[j]['nonempty'].items()) for j in ids)):
    mass=v*v;count=1
    for p,n in row:mass*=p;count*=n
    counts[mass]+=count
  ck(sum(p*n for p,n in counts.items())==1)
  hh=plus(*(scale(ell(p),n) for p,n in counts.items()));ck(max(H[0],hh[0])<=min(H[1],hh[1]))
 return {'state':list(ts),'H':H,'I':str(I),'S':sub(scale((G,G),4*I),H)}
def block(i,pilot=False):
 start=time.perf_counter();before=CHECKS;out=[]
 domain=[(a,b,ROOT,ROOT) for a,b in product(range(12),repeat=2)] if pilot else [(i,)+s for s in product(range(12),repeat=3)]
 for j,ts in enumerate(domain):
  out.append(full(ts,atoms=pilot or j in [0,257,1023,1727]));ck(time.perf_counter()-start<55)
 tag='PILOT' if pilot else f'BLOCK_{i:02d}'
 save(tag+'_STATES.json',out);z={'status':'EXACT_PASS','profiles':len(out),'checks':CHECKS-before,'seconds':time.perf_counter()-start,'log_cache':log.cache_info().currsize};save(tag+'_VALIDATION.json',z);print(tag,json.dumps(z),flush=True)
def setup():
 global C
 C,red=init();return red
if __name__=='__main__':
 red=setup();save('REDUCTION.json',red)
 if '--pilot' in sys.argv:block(0,True)
 elif '--block' in sys.argv:block(int(sys.argv[sys.argv.index('--block')+1]))
 elif '--full' in sys.argv:
  start=time.perf_counter()
  for i in range(12):
   block(i);log.cache_clear();ell.cache_clear();ck(time.perf_counter()-start<840)
  save('SPECTRUM_VALIDATION.json',{'status':'PASS','profiles':20736,'checks':CHECKS,'seconds':time.perf_counter()-start,'arithmetic':'exact Fraction and 192-bit outward intervals;48-term positive atanh+proved tail'})
