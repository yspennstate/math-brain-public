from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def scale(c,a):return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def total(z):
 a=(F(0),F(0))
 for x in z:a=add(a,x)
 return a
def mean(z):return scale(F(1,2),total(z))
def meet(a,b):ck(a[0]<=b[1] and b[0]<=a[1])
def ln_series(x):
 z=(x-1)/(x+1);a=sum((z**(2*k+1)/F(2*k+1) for k in range(40)),F(0))*2
 err=2*abs(z)**81/(81*(1-z*z))
 return a-err,a+err
LN2=ln_series(F(2))
@lru_cache(None)
def log(x):
 ck(x>0);k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 a=ln_series(x)
 return F(k)+a[0]/LN2[1],F(k)+a[1]/LN2[0]
def H(p):return total(scale(-x,log(x)) for x in p if x)
def KL(p,q):return total(scale(x,log(x/y)) for x,y in zip(p,q) if x)
def law(t):
 a=t[:];k=1
 while k<len(a):
  for lo in range(0,len(a),2*k):
   for j in range(lo,lo+k):a[j],a[j+k]=a[j]+a[j+k],a[j]-a[j+k]
  k*=2
 p=[F(x*x,len(a)**2) for x in a];ck(sum(p)==1);return p
def marg(p):return [sum((v for s,v in enumerate(p) if s>>j&1),F(0)) for j in range(len(p).bit_length()-1)]
def prod(d):
 q=[]
 for s in range(1<<len(d)):
  a=F(1)
  for j,x in enumerate(d):a*=x if s>>j&1 else 1-x
  q.append(a)
 return q
def hb(x):return H([x,1-x])
def restrict(t,j,y):return [t[s|(y<<j)] for s in range(len(t)) if not(s>>j&1)]
w=2;core=[(1-2*int((z&3)==0))*(1-2*int((z>>2)==0)) for z in range(16)]
root=[-1 if not(t&1) and t&2 else core[t>>3] if t&1 and t&4 else 1 for t in range(128)]
front=[(restrict(root,1,y),F(1,2)) for y in range(2)];cases=0;distinct=0;unequal_nonconstant=0
for depth in range(4):
 nxt=[]
 for tab,reach in front:
  p=law(tab);d=marg(p);q=prod(d);i=2
  ts=[restrict(tab,i,y) for y in range(2)];ps=[law(t) for t in ts]
  er=[p[s]+p[s|(1<<i)] for s in range(len(p)) if not(s>>i&1)]
  qr=[q[s]+q[s|(1<<i)] for s in range(len(q)) if not(s>>i&1)]
  ck(er==[(x+y)/2 for x,y in zip(*ps)])
  kernel=[[py[j]/(2*er[j]) if er[j] else F(1,2) for j in range(len(er))] for py in ps]
  pi=[sum((x*y for x,y in zip(qr,k)),F(0)) for k in kernel]
  ck(sum(pi)==1 and all(x>0 for x in pi))
  pred=[[x*y/z for x,y in zip(qr,k)] for k,z in zip(kernel,pi)]
  ds=[marg(p1) for p1 in ps]
  tc= sub(total(hb(x) for x in d),H(p));tc1=[sub(total(hb(x) for x in a),H(p1)) for a,p1 in zip(ds,ps)]
  E=sub(KL(p,q),KL(er,qr));O=KL([F(1,2)]*2,pi);K=mean([KL(p1,r) for p1,r in zip(ps,pred)])
  B=sub(H(p),H(er));J=sub(H(er),mean([H(p1) for p1 in ps]));Gamma=total(sub(hb(d[j]),mean([hb(a[j if j<i else j-1]) for a in ds])) for j in range(len(d)) if j!=i)
  meet(KL(p,q),add(E,add(O,K)));meet(E,sub(hb(d[i]),B));meet(sub(mean(tc1),K),sub(add(O,J),Gamma))
  if sub(B,J)[0]>0 or sub(B,J)[1]<0:distinct+=1
  if ts[0]!=ts[1] and all(len(set(t))==2 for t in ts):unequal_nonconstant+=1
  nxt.extend((t,reach/2) for t in ts);cases+=1
 front=nxt
ck(distinct>0);ck(unequal_nonconstant>0)
out={'status':'PASS','checks':checks,'actual_query_transactions':cases,'strict_B_J_separations':distinct,'unequal_nonconstant_child_pairs':unequal_nonconstant,'arithmetic':'independent integer FWHT, Fraction coherent kernels, 40-term atanh rational logarithm with explicit geometric remainder','seconds':time.perf_counter()-start,'scope':'w2 all outcomes fixed data order; algebra verification, not the allw proof'}
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='\n');print(json.dumps(out))
