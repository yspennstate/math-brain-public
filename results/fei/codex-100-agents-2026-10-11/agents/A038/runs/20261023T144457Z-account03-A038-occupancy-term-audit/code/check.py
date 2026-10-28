import json,time,sys,hashlib,shutil
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
R=Path(__file__).resolve().parents[1];A=R.parents[1];start=time.monotonic();count=0
prior=A/'runs/20261023T123226Z-account03-A038-occupancy-term-audit'
shutil.copyfile(prior/'code/interval_primitives.py',R/'code/interval_primitives.py')
import interval_primitives as m
V=m.V
def ck(x,label):
 global count
 count+=1
 assert x,label
 if time.monotonic()-start>55:raise RuntimeError('frozen55-second watchdog')
def restrict(t,i,s):return tuple(t[j] for j in range(len(t)) if j>>i&1==s)
@lru_cache(None)
def direct(t):
 a=m.spectrum(t);p=[x*x for x in a];n=len(t).bit_length()-1
 d=[sum((w for j,w in enumerate(p) if j>>i&1),F(0)) for i in range(n)]
 for i in range(n):ck(d[i]==F(sum(t[j]!=t[j^(1<<i)] for j in range(len(t))),len(t)),'independent edge influence')
 return m.entropy(p),sum(d),d
@lru_cache(None)
def dp(t):
 H,I,d=direct(t);n=len(t).bit_length()-1
 if not n:return V(0)
 opts=[]
 for i in range(n):
  a=restrict(t,i,0);b=restrict(t,i,1)
  delta=H-(direct(a)[0]+direct(b)[0])/2-4*d[i]
  opts.append(m.positive(delta)+(dp(a)+dp(b))/2)
 return V(max(x.a for x in opts),max(x.b for x in opts))
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):return a[0]*c,a[1]*c
def sub(a,b):return plus(a,scale(b,-1))
def ln(q):
 t=(q-1)/(q+1);lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
 return lo,lo+2*t**65/(65*(1-t*t))
la,lb=ln(F(3,2));lc,ld=ln(F(2));LOG3=(1+la/ld,1+lb/lc)
def bounds(a):
 u,v=a;return (u+v*LOG3[0],u+v*LOG3[1]) if v>=0 else (u+v*LOG3[1],u+v*LOG3[0])
def sign(a):
 if a==(0,0):return 0
 lo,hi=bounds(a);ck(lo>0 or hi<0,'rigorously resolved exact prime-log comparison')
 return 1 if lo>0 else -1
@lru_cache(None)
def symbolic(t):
 w=list(t);size=1
 while size<len(w):
  for j in range(0,len(w),2*size):
   for k in range(size):x,y=w[j+k],w[j+k+size];w[j+k]=x+y;w[j+k+size]=x-y
  size*=2
 n=len(t).bit_length()-1;p=[F(a*a,len(t)**2) for a in w];H=(F(0),F(0));d=[F(0)]*n
 for mask,q in enumerate(p):
  for i in range(n):
   if mask>>i&1:d[i]+=q
  if not q:continue
  num,den=q.numerator,q.denominator;e2=e3=0
  while num%2==0:num//=2;e2+=1
  while den%2==0:den//=2;e2-=1
  while num%3==0:num//=3;e3+=1
  ck(num==den==1,'symbolic spectrum uses only primes2/3 on frozen domain')
  H=plus(H,(-q*e2,-q*e3))
 return H,sum(d),d
def children(t,i):
 # Independent bit-insertion restriction, not the direct lane's filtered path.
 out=[]
 for s in [0,1]:out.append(tuple(t[(j&((1<<i)-1))|(s<<i)|((j>>i)<<(i+1))] for j in range(len(t)//2)))
 return out
@lru_cache(None)
def exactdp(t):
 H,I,d=symbolic(t);best=(F(0),F(0))
 for i in range(len(d)):
  a,b=children(t,i);delta=sub(H,scale(plus(symbolic(a)[0],symbolic(b)[0]),F(1,2)));delta=plus(delta,(-4*d[i],F(0)))
  pos=delta if sign(delta)>0 else (F(0),F(0))
  option=plus(pos,scale(plus(exactdp(a),exactdp(b)),F(1,2)))
  if sign(sub(option,best))>0:best=option
 return best
if __name__=='__main__':
 pilot='--pilot' in sys.argv;top=2 if pilot else 3;best=(F(0),F(0));witness=None;tables=0
 for n in range(top+1):
  for bits in range(1<<(1<<n)):
   t=tuple(1 if bits>>j&1 else -1 for j in range(1<<n));tables+=1
   val=dp(t);ex=exactdp(t);H,I,d=direct(t);hs,ii,dd=symbolic(t)
   ck(I==ii and d==dd,'direct versus WHT influences')
   lo,hi=bounds(hs);ck(H.a<=hi and lo<=H.b,'independent entropy representations')
   lo,hi=bounds(ex);ck(val.a<=hi and lo<=val.b,'independent Bellman representations')
   ck(sign(plus(ex,(-I,F(0))))<=0,'EXACT finite certificate V4<=I')
   ck(val.b<=I,'independent interval upper certificate V4<=I')
   if I:
    ratio=scale(ex,1/I)
    if sign(sub(ratio,best))>0:best=ratio;witness={'n':n,'truth_bits':bits,'I':str(I),'V4_pair':[str(x) for x in ex]}
 tensors=0
 if not pilot:
  for s in [-1,1]:
   f=tuple(s*(-1 if j==0 else 1) for j in range(8))
   for bits in range(4):
    g=tuple(1 if bits>>j&1 else -1 for j in range(2));product=tuple(f[j&7]*g[j>>3] for j in range(16))
    ck(exactdp(product)==plus(exactdp(f),exactdp(g)),'EXACT positive-potential tensor identity')
    ck(sign(exactdp(f))>0,'tensor check has positive potential, not zero-only')
    tensors+=1
 out={'status':'PASS','assertions':count,'runtime_seconds':time.monotonic()-start,'truth_tables':tables,'tensor_transactions':tensors,'maximum_ratio_pair':[str(x) for x in best],'maximum_ratio_interval':[str(x) for x in bounds(best)],'witness':witness,'external_review':'PENDING','arithmetic':'two independent mathematical lanes; exact symbolic max comparisons, interval upper checks'}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
 print(json.dumps(out))
