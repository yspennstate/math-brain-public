from fractions import Fraction as F
from pathlib import Path
import json,time,sys
from functools import lru_cache
R=Path(__file__).resolve().parents[1];START=time.perf_counter();CHECKS=0
def eq(a,b):
 global CHECKS
 assert a==b,(a,b);CHECKS+=1
def spectrum(vals):
 a=list(vals);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h):x,y=a[i],a[i+h];a[i],a[i+h]=x+y,x-y
  h*=2
 return [F(x*x,len(a)**2) for x in a]
def ln_small(x):
 z=(x-1)/(x+1);z2=z*z;power=z;v=F(0)
 for j in range(32):v+=2*power/F(2*j+1);power*=z2
 return v,v+2*power/F(65)/(1-z2)
L2=ln_small(F(2))
@lru_cache(maxsize=2048)
def log2(x):
 assert x>0;e=0
 while x<1:x*=2;e-=1
 while x>=2:x/=2;e+=1
 lo,hi=ln_small(x)
 return F(e)+lo/L2[1],F(e)+hi/L2[0]
def kl(p,q):
 lo=hi=F(0)
 for x,y in zip(p,q):
  if x:
   a,b=log2(x/y);lo+=x*a;hi+=x*b
 return lo,hi
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def scale(a,c):return a[0]*c,a[1]*c
def restrict(vals,i,b):
 return [vals[(x&((1<<i)-1))|(b<<i)|((x>>i)<<(i+1))] for x in range(len(vals)//2)]
def pivot(vals,i):return F(sum(v!=vals[x^(1<<i)] for x,v in enumerate(vals)),len(vals))
def fresh_core(vals,alpha):
 p=spectrum(vals);active=[t for t,v in enumerate(p) if v]
 if len(active)==1:return p
 n=(len(vals)).bit_length()-1;full=0
 for i in range(n):
  if pivot(vals,i):full|=1<<i
 q=[p[0]]+[(1-alpha)*v for v in p[1:]]
 q[full]+=alpha*(1-p[0]);eq(sum(q),1)
 return q
def lifted(vals,s,alpha):
 j=[v for g in vals for v in (s,g)];p=spectrum(j);q=fresh_core(vals,alpha)
 out=[p[0],p[1]]+[q[t]/4 for t in range(1,len(q)) for _ in range(2)]
 eq(sum(out),1);return p,out
def erase(v,i):
 out=[F(0)]*(len(v)//2)
 for t,x in enumerate(v):out[(t&((1<<i)-1))|((t>>(i+1))<<i)]+=x
 return out
def psi(t,alpha):
 if not t:return F(0),F(0)
 return scale(log2(1+alpha/((1-alpha)*t)),t)
def grouped(r,k,alpha):
 base=F(4,2**(2*r));d=F(1,2**k);t=4*d*d*base
 v=sub(scale(psi(t/2,alpha),F(1,2)),scale(psi(base,alpha),F(1,4)))
 v=sub(v,scale(psi(t,alpha),F(1,4)))
 return sub(v,scale(log2(1-alpha*alpha/4),F(1,2)))
def overlap(a,b):assert max(a[0],b[0])<=min(a[1],b[1])
def main():
 pilot='--pilot' in sys.argv;domain=[(2,1)] if pilot else [(6,1),(6,2)]
 records=[];alpha=F(1,7)
 for r,k in domain:
  n=r+k+2;i=r+1
  vals=[]
  for x in range(1<<n):
   z=-1 if x&1 else 1
   a=-1 if ((x>>1)&((1<<r)-1))==(1<<r)-1 else 1
   d=-1 if ((x>>i)&((1<<(k+1))-1))==(1<<(k+1))-1 else 1
   vals.append(z*a*d)
  eq(pivot(vals,i),F(1,2**k));eq(sum(vals),0)
  for s in (-1,1):
   P,Q=lifted(vals,s,alpha);E=erase(P,i+1);D=erase(Q,i+1)
   sig=(F(0),F(0));outcomes=[]
   for b in (0,1):
    child=restrict(vals,i,b);Pc,N=lifted(child,s,alpha)
    raw=[d*(pc/(2*e) if e else F(1,2)) for e,d,pc in zip(E,D,Pc)]
    Z=sum(raw);old=[x/Z for x in raw]
    eq(Z,F(1,2)+(-1 if b==0 else 1)*alpha/4)
    eq(sum(old),1);eq(sum(N),1)
    ko=kl(Pc,old);kn=kl(Pc,N);sig=add(sig,scale(sub(kn,ko),F(1,2)))
    outcomes.append({'b':b,'reference_outcome':str(Z),'inherited_KL':[str(x) for x in ko],'fresh_KL':[str(x) for x in kn]})
   formula=grouped(r,k,alpha);overlap(sig,formula)
   if not pilot:assert sig[0]>F(1,2048)
   records.append({'r':r,'k':k,'sign':s,'core_influence':str(pivot(vals,i)),'activation_influence':str(pivot(vals,i)/2),'sigma_interval':[str(x) for x in sig],'formula_interval':[str(x) for x in formula],'outcomes':outcomes})
   assert time.perf_counter()-START<55
 # Integer/rational certificate for the UNIFORM lower bound and original-bank allowance.
 eq(F(515,3)<256,True)
 eq(F(1,392)-F(1,512)>F(1,2048),True)
 eq(8**4<2*7**4,True);eq(7**4<2*6**4,True)
 result={'status':'PASS','pilot':pilot,'cases':len(records),'assertions':CHECKS,'seconds':time.perf_counter()-START,'records':records,'scope':'actual full normalized activation histories, grouped formula and uniform lower-bound certificates; full FEI OPEN'}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='records'}))
if __name__=='__main__':main()
