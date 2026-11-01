from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
import sys,json,time
ROOT=Path(__file__).resolve().parents[1];(ROOT/'out').mkdir(exist_ok=True)
PILOT='--pilot' in sys.argv;START=time.perf_counter();CAP=50 if PILOT else 240
def clock():
 if time.perf_counter()-START>CAP:raise RuntimeError('frozen runtime cap reached; no domain escalation')
def fwht(v):
 v=list(v);s=1
 while s<len(v):
  clock()
  for base in range(0,len(v),2*s):
   for j in range(base,base+s):a,b=v[j],v[j+s];v[j],v[j+s]=a+b,a-b
  s*=2
 return v
def unitln(q):
 z=(q-1)/(q+1);term=z;lo=Q(0)
 for j in range(28):lo+=2*term/Q(2*j+1);term*=z*z
 return lo,lo+2*term/Q(57)/(1-z*z)
LN2=unitln(Q(2))
@lru_cache(None)
def logint(k):
 if k==1:return Q(0),Q(0)
 shift=k.bit_length()-1;l,u=unitln(Q(k,1<<shift))
 return shift+l/LN2[1],shift+u/LN2[0]
def rounded(a):
 scale=1<<128
 return Q(a[0].numerator*scale//a[0].denominator,scale),Q(-((-a[1].numerator*scale)//a[1].denominator),scale)
def add(a,b):return rounded((a[0]+b[0],a[1]+b[1]))
def sub(a,b):return rounded((a[0]-b[1],a[1]-b[0]))
def mul(a,k):return rounded((a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k))
def ratlog(q):return sub(logint(q.numerator),logint(q.denominator))
def ent(q):return mul(ratlog(q),-q) if q else (Q(0),Q(0))
def h2(q):return add(ent(q),ent(1-q))
def phi(a,b):return sub(add(ent(a),ent(b)),ent(a+b))
def emit(a):
 scale=10**12
 return [str(Q(a[0].numerator*scale//a[0].denominator,scale)),str(Q(-((-a[1].numerator*scale)//a[1].denominator),scale))]
LOGE=(1/LN2[1],1/LN2[0])
def bent(x,n):return -1 if sum(((x>>(2*j))&3)==3 for j in range(n//2))%2 else 1
def table(m,L):
 n=m+5*L;vals=[]
 for a in range(1<<n):
  y=a&((1<<m)-1);p=y.bit_count()%2;s=bent(y,m)
  for j in range(L):
   x=(a>>(m+5*j))&15;z=(a>>(m+5*j+4))&1
   s*=bent(x,4)
   if p and x==0 and z:s=-s
  vals.append(s)
 return vals
def influence(t):
 N=len(t);n=N.bit_length()-1
 return Q(sum(t[x]!=t[x^(1<<j)] for j in range(n) for x in range(N)),N)
def spectrumI(t):
 N=len(t);a=fwht(t)
 return a,Q(sum(s.bit_count()*v*v for s,v in enumerate(a)),N*N)
def restrict(t,i,value):
 n=len(t).bit_length()-1;lo=(1<<i)-1
 return [t[(x&lo)|((x&~lo)<<1)|(value<<i)] for x in range(1<<(n-1))]
def entropy_table(t):
 N=len(t);hist=Counter(v*v for v in fwht(t) if v);H=(Q(0),Q(0))
 for v,c in hist.items():H=add(H,mul(ent(Q(v,N*N)),c))
 return H
checks=0
def split(t,i):
 global checks
 N=len(t)//2;g,h=restrict(t,i,0),restrict(t,i,1)
 A=[(x+y)//2 for x,y in zip(g,h)];V=[(x-y)//2 for x,y in zip(g,h)]
 assert all(a*a+v*v==1 and a*v==0 for a,v in zip(A,V));checks+=1
 u,v=fwht(A),fwht(V);d=Q(sum(x*x for x in v),N*N)
 assert d==Q(sum(x!=y for x,y in zip(g,h)),N);checks+=1
 # Full mixed signed convolutions: transform back to physical A,V,
 # multiply there, transform again. No absolute values precede cancellation.
 aa,vv=fwht(u),fwht(v);mixed=fwht([a*b for a,b in zip(aa,vv)])
 assert mixed==[0]*N;checks+=1
 signedvv=fwht([a*a for a in vv]);G=[a*b for a,b in zip(g,h)];gh=fwht(G)
 assert all((N**3 if s==0 else 0)-2*signedvv[s]==N*N*gh[s] for s in range(N));checks+=1
 W=Q(sum(s.bit_count()*a*a for s,a in enumerate(gh)),2*N*N)
 assert W==influence(G)/2;checks+=1
 B=(Q(0),Q(0));pairs=Counter(zip((a*a for a in u),(a*a for a in v)))
 for (a,b),count in pairs.items():B=add(B,mul(phi(Q(a,N*N),Q(b,N*N)),count))
 M=sub(h2(d),B);R=sub((W,W),ent(d));sigma=sub(mul(LOGE,d),ent(1-d))
 reconstruction=sub(sub(sub(add((W,W),mul(LOGE,d)),R),M),sigma)
 assert reconstruction[0]<=B[1] and reconstruction[1]>=B[0];checks+=1
 assert R[1]>=0 and M[1]>=0 and sigma[1]>=0;checks+=3
 return dict(d=d,W=W,B=B,M=M,R=R,sigma=sigma)
