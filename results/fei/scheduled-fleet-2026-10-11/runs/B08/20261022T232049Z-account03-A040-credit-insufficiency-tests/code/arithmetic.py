from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys,itertools,hashlib
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
Z=(F(0),F(0))
GRID=2**120
def rounded(a):return F(a[0].numerator*GRID//a[0].denominator,GRID),F(-((-a[1].numerator*GRID)//a[1].denominator),GRID)
def ck(b):
 global checks
 assert b
 checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('frozen runtime exceeded')
def add(a,b):return rounded((a[0]+b[0],a[1]+b[1]))
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
@lru_cache(None)
def lnunit(x):
 z=(x-1)/(x+1);s=F(0);t=z
 for k in range(36):s+=t/F(2*k+1);t*=z*z
 rem=2*t/F(73)/(1-z*z)
 return 2*s,2*s+rem
L2=lnunit(F(2))
@lru_cache(None)
def log(x):
 assert x>0
 k=x.numerator.bit_length()-x.denominator.bit_length();v=x/F(2)**k
 if v<1:v*=2;k-=1
 l,u=lnunit(v)
 return rounded((l/L2[1]+k,u/L2[0]+k))
@lru_cache(None)
def entterm(x):return scale(log(x),-x) if x else Z
def entropy(p):
 o=Z
 for x in p:o=add(o,entterm(x))
 return o
def kl(p,q):
 o=Z
 for x,y in zip(p,q):
  if x:assert y>0;o=add(o,scale(sub(log(x),log(y)),x))
 return o
@lru_cache(None)
def spectrum(g):
 v=list(g);h=1
 while h<len(v):
  for b in range(0,len(v),2*h):
   for i in range(b,b+h):a,c=v[i],v[i+h];v[i],v[i+h]=a+c,a-c
  h*=2
 return tuple(F(a,len(g)) for a in v)
def law(g):return tuple(a*a for a in spectrum(g))
def infl(g,i):return F(sum(g[x]!=g[x^(1<<i)] for x in range(len(g))),len(g))
def influence(g):return sum((infl(g,i) for i in range(len(g).bit_length()-1)),F(0))
def restrict(g,i,b):return tuple(y for x,y in enumerate(g) if (x>>i)&1==b)
def family(g):
 return tuple(1+(bool((x>>1&1)*(x>>2&1)*(x>>3&1) or (x&1)*((x>>2&1) or (x>>3&1))))*(g[x>>4]-1) for x in range(16*len(g)))
def product(p):
 n=len(p).bit_length()-1;ds=[sum((p[x] for x in range(len(p)) if x>>i&1),F(0)) for i in range(n)]
 return tuple(__import__('math').prod(ds[i] if x>>i&1 else 1-ds[i] for i in range(n)) for x in range(len(p)))
def fmt(x):return [str(x[0]),str(x[1])]
def mid(x):return float((x[0]+x[1])/2)
def mean(x,y):return scale(add(x,y),F(1,2))
def bank(g,j=1,L=1,R=1,T=1):
 a=1-spectrum(g)[0];q=F(1,2**R);r=F(1,2**T);eta=F(1,2**(L+R+T));e=q+r-q*r-eta;M=min(j,0 if min(R,T)>=4 else 3)
 JB=(L+R+T)*eta;JC=R*q*(1-r)+T*r*(1-q)
 return F(1,2**j)*(a*M*(JB+JC)+a*e*M*(M-1)/2+M*e*influence(g))
def nonlinear(a,p):
 # H(F)-pH(g) minus the linear term 2a H_un(Ahat^2).
 ans=sub(entterm((1-a*p)**2),scale(entterm((1-a)**2),p))
 ans=sub(ans,scale(entterm(p*p),a*a))
 if a:ans=sub(ans,scale(log(a*a),a*a*(p-p*p)))
 return ans

def query(g,i,detail=False):
 f=family(g);g0,g1=[restrict(g,i,b) for b in (0,1)];f0,f1=[restrict(f,4+i,b) for b in (0,1)]
 ck(f0==family(g0) and f1==family(g1))
 P=law(f);P0=law(f0);P1=law(f1);H=entropy(P);H0=entropy(P0);H1=entropy(P1)
 dg=sub(entropy(law(g)),mean(entropy(law(g0)),entropy(law(g1))))
 df=sub(H,mean(H0,H1));pi=F(7,16);t=infl(g,i)
 release=bank(g)-(bank(g0)+bank(g1))/2
 ck(release==F(5,16)*t);ck(infl(f,4+i)==pi*t)
 correction=sub(df,scale(dg,pi));a=1-spectrum(g)[0];a0=1-spectrum(g0)[0];a1=1-spectrum(g1)[0]
 scalar=sub(nonlinear(a,pi),mean(nonlinear(a0,pi),nonlinear(a1,pi)))
 ck(max(correction[0],scalar[0])<=min(correction[1],scalar[1]))
 residual=sub(correction,(release,release))
 if not detail:return {'core':list(g),'i':i,'means':[str(a),str(a0),str(a1)],'residual':fmt(residual),'scalar_correction':fmt(scalar)}
 # A single original product reference; transport SAME signed physical kernel.
 Q=product(P);n=len(P0);q=[];qt=[]
 for x in range(n):
  lo=(x&((1<<(4+i))-1))|((x>>(4+i))<<(5+i));hi=lo|(1<<(4+i))
  q.append(P[lo]+P[hi]);qt.append(Q[lo]+Q[hi])
 k0=[P0[x]/(2*q[x]) if q[x] else F(1,2) for x in range(n)]
 un0=[qt[x]*k0[x] for x in range(n)];un1=[qt[x]*(1-k0[x]) for x in range(n)];z0=sum(un0);z1=sum(un1)
 ck(z0>0 and z1>0 and z0+z1==1)
 Q0=[x/z0 for x in un0];Q1=[x/z1 for x in un1]
 A=kl(P,Q);K=mean(kl(P0,Q0),kl(P1,Q1));O=scale(add(scale(log(2*z0),-1),scale(log(2*z1),-1)),F(1,2))
 # Conditional erasure KL, directly by every source pair.
 E=Z
 for x in range(n):
  lo=(x&((1<<(4+i))-1))|((x>>(4+i))<<(5+i));hi=lo|(1<<(4+i))
  if q[x]:E=add(E,scale(kl([P[lo]/q[x],P[hi]/q[x]],[Q[lo]/qt[x],Q[hi]/qt[x]]),q[x]))
 chain=sub(A,add(E,add(O,K)));ck(chain[0]<=0<=chain[1])
 TC=mean(kl(P0,product(P0)),kl(P1,product(P1)));conversion=sub(add(O,TC),A)
 surplus=mean(sub((4*influence(f0),)*2,H0),sub((4*influence(f1),)*2,H1))
 # Deduct every still-live inherited separator reserve before bank eligibility.
 remaining=(bank(g0)+bank(g1))/2;available=sub(surplus,(remaining,remaining))
 debit=max(F(0),residual[1])+max(F(0),conversion[1]); inherited_available=sub(available,K); product_available=sub(available,TC); reset=sub(TC,K)
 return {'inherited_full_bank':fmt(inherited_available),'product_full_bank':fmt(product_available),'signed_reset':fmt(reset),'H':fmt(H),'child_H':[fmt(H0),fmt(H1)],'child_I':[str(influence(f0)),str(influence(f1))],'Dg':fmt(dg),'Df':fmt(df),'release':str(release),'residual':fmt(residual),'reference_outcome_normalizers':[str(z0),str(z1)],'A':fmt(A),'E':fmt(E),'O':fmt(O),'K':fmt(K),'TCmean':fmt(TC),'conversion_debit':fmt(conversion),'full_child_surplus':fmt(surplus),'inherited_child_reserve':str(remaining),'available_bank':fmt(available),'total_positive_debit_upper':str(debit),'fraction_of_available_upper':str(debit/available[0]) if available[0]>0 else None,'reference_only_rows':sum(q[x]==0 and qt[x]>0 for x in range(n)),'decimal_diagnostics':{'residual':mid(residual),'conversion':mid(conversion),'available':mid(available)}}
