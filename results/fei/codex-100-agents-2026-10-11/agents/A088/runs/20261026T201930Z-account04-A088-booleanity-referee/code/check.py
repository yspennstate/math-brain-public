from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys,itertools,hashlib
R=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0

def ck(v):
 global checks
 assert v
 checks+=1
 assert time.monotonic()-start<60

Q=1<<100
@lru_cache(None)
def ln_interval(x):
 x=F(x); k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 z=(x-1)/(x+1); zn=z; low=0
 for j in range(32):
  term=2*zn/(2*j+1); low+=term.numerator*Q//term.denominator
  zn*=z*z
 rem=2*zn/(65*(1-z*z)); hi=low+32+(rem.numerator*Q+rem.denominator-1)//rem.denominator
 if k:
  a,b=ln_interval(F(2)) if x!=2 else (None,None)
  low,hi=(low+k*a,hi+k*b) if k>=0 else (low+k*b,hi+k*a)
 return low,hi
# Avoid recursive ln(2) reduction.
z=F(1,3); t=z; ls=0
for j in range(32):
 term=2*t/(2*j+1);ls+=term.numerator*Q//term.denominator;t*=z*z
rem=2*t/(65*(1-z*z)); LN2=(ls,ls+32+(rem.numerator*Q+rem.denominator-1)//rem.denominator)
ln_interval.cache_clear()
# separate normalized logarithm, integer exponent handled against known ln2
@lru_cache(None)
def log2i(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 a,b=ln_interval(x)
 return F(a,LN2[1])+k,F(b,LN2[0])+k

def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def H(p):
 a=(F(0),F(0))
 for v in p:
  if v:a=add(a,scale(log2i(v),-v))
 return a
def CE(p,q):
 a=(F(0),F(0))
 for v,u in zip(p,q):
  if v:
   ck(u>0);a=add(a,scale(log2i(u),-v))
 return a

def spec(t):
 a=list(t);N=len(a);h=1
 while h<N:
  for i in range(0,N,2*h):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return tuple(F(x*x,N*N) for x in a)
def inf(t):
 n=len(t).bit_length()-1
 return sum(F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n))
def res(t,i,v):return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(v<<i)] for x in range(len(t)//2))
def marg(q,i):return tuple(q[(x&((1<<i)-1))|((x>>i)<<(i+1))]+q[(x&((1<<i)-1))|((x>>i)<<(i+1))|(1<<i)] for x in range(len(q)//2))
def phase(n,edges):return tuple((-1)**(sum(((x>>i)&1)*((x>>j)&1) for i,j in edges)%2) for x in range(1<<n))
def rank(n,edges):
 rows=[sum(1<<j for j in range(n) if (min(i,j),max(i,j)) in edges) for i in range(n)];r=0
 for j in range(n):
  z=next((k for k in range(r,n) if rows[k]>>j&1),None)
  if z is not None:
   rows[r],rows[z]=rows[z],rows[r]
   for k in range(n):
    if k!=r and rows[k]>>j&1:rows[k]^=rows[r]
   r+=1
 return r

mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
n=8;m=4;d=F(1,256)
matching=[(i,i+1) for i in range(0,n,2)]
graphs=[matching] if mode=='pilot' else [matching,list(itertools.combinations(range(n),2)),matching+[(0,2),(0,3)]]
pairs=[(0,1)] if mode=='pilot' else [(7,31)]
orders=[list(range(9)),list(reversed(range(9))),[8,0,2,4,6,1,3,5,7],[0,8,1,2,3,4,5,6,7],[0,1,2,3,8,4,5,6,7],[7,5,3,1,0,2,4,6,8]]
rows=[];frontiers=0
for gi,edges in enumerate(graphs):
 ck(rank(n,edges)==n);b0=phase(n,edges);pb0=spec(b0);ck(set(pb0)=={d});ck(inf(b0)==m)
 b=b0+b0;pb=spec(b);Hb=H(pb);Ib=inf(b)
 for aa,bb in pairs:
  c=list(b);c[aa]*=-1;c[bb]*=-1;c=tuple(c);qc=spec(c);Hc=H(qc);Ic=inf(c)
  g=b+c;Hg=H(spec(g));Ix=(Ib+Ic)/2;r4=sub((4*Ix,4*Ix),Hg)
  ck(Ix>=m-4*m*d+d);ck(r4[0]>=2*m-16*m*d+4*d-2)
  # canceled sector is exactly a parity half-support law
  ck(set(qc[256:])=={F(0),4*d*d});ck(sum(qc[256:])==2*d)
  for order in orders:
   # entries: actual physical table, original inherited law, original reach, remaining labels
   leaves=[(c,qc,F(1,2),list(range(9)),b)]
   for depth in range(10):
    frontier=[(b,pb,F(1,2),list(range(9)),b)]+leaves
    h=(F(0),F(0));ce=(F(0),F(0));iavg=F(0)
    for t,q,w,labs,base in frontier:
     p=spec(t);ck(sum(p)==1);ck(sum(q)==1)
     h=add(h,scale(H(p),w));ce=add(ce,scale(CE(p,q),w));iavg+=w*inf(t)
    J=Ix-iavg;ck(J>=0)
    Hroot=scale(add(Hb,Hc),F(1,2))
    eh=sub(sub(Hroot,h),(4*J,4*J));eq=sub(sub(Hroot,ce),(4*J,4*J));kl=sub(ce,h)
    ck(max(abs((sub(eh,add(eq,kl)))[j]) for j in [0,1])<F(1,10**18))
    ck(kl[1]<=F(3,2)+F(1,10**18));ck(eq[1]<3+(2*m+4)*d)
    ck(eh[1]<F(9,2)+(2*m+4)*d);ck(r4[0]-eh[1]>F(39,32))
    frontiers+=1
    if depth==9:break
    lab=order[depth];new=[]
    for t,q,w,labs,base in leaves:
     # Keep ALL exits, and query only if actual table still differs from unedited phase restriction.
     # Reconstruct unedited restriction from path-independent clean detector: quadratic truth is tracked below.
     if lab not in labs:new.append((t,q,w,labs,base));continue
     idx=labs.index(lab)
     # a branch is edited iff its table differs from its quadratic counterpart; stored externally by table key
     if t==base:new.append((t,q,w,labs,base));continue
     qm=marg(q,idx);newlabs=labs[:idx]+labs[idx+1:]
     for v in [0,1]:
      tt=res(t,idx,v);bt=res(base,idx,v)
      new.append((tt,qm,w/2,newlabs,bt))
    leaves=new
  rows.append({'graph':gi,'pair':[aa,bb],'r4_lower':str(r4[0]),'source_I_X':str(Ix)})

ck(F(131,49)<4);ck(F(2*4)-F(13,2)-F(18*4,4**4)==F(39,32))
ck(399**2+40**2==401**2);ck(401>16)
result={'mode':mode,'assertions':checks,'sources':len(rows),'frontiers':frontiers,'seconds':time.monotonic()-start,'arithmetic':'exact Fraction Walsh/edges,100-bit outward ln series32 terms; no floating signs','rows':rows}
(R/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
