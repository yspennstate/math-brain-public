from fractions import Fraction as F
import time,json
from pathlib import Path
start=time.perf_counter(); checks=0; cases=0; t=F(3,4)
def ck(v):
 global checks
 assert v
 checks+=1
for ia in range(1,12):
 a=F(ia,16)
 for ib in range(1,11):
  b=F(ib,16)
  for il in range(ib+1,12):
   ell=F(il,16); z=max(a,ell); cases+=1
   p=[F(1,4),a,(t-a)/3,2*(t-a)/3]
   q0=[F(1,4),b,(t-b)/5,4*(t-b)/5]
   q=[F(1,4),z,q0[2]*(t-z)/(t-b),q0[3]*(t-z)/(t-b)]
   ck(sum(p)==sum(q0)==sum(q)==1); ck(q[1]>=ell)
   ck(q[2]/q[3]==q0[2]/q0[3]); ck(q[0]==q0[0])
   raw=F(1)
   for pi,qi,qi0 in zip(p,q,q0): raw*=(qi0/qi)**int(48*pi)
   compressed=(b/z)**int(48*a)*((t-b)/(t-z))**int(48*(t-a))
   ck(raw==compressed)
   best=z**ia*(t-z)**(12-ia)
   for iz in range(il,12):
    v=F(iz,16); ck(best>=v**ia*(t-v)**(12-ia))
   ck(time.perf_counter()-start<20)
# Independent direct Walsh endpoint; no FFT helper imported.
g=[-1 if x in (0,7) else 1 for x in range(8)]
def law(vals):
 N=len(vals); out=[]
 for s in range(N):
  w=sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(vals)); out.append(F(w*w,N*N))
 return out
ck(law(g)==[F(1,4),0,0,F(1,4),0,F(1,4),F(1,4),0])
for bit in (0,1):
 child=[g[(x<<1)|bit] for x in range(4)]; ck(law(child)==[F(1,4)]*4)
 p=[F(1,4)]*4; target=[F(1,4),F(5,24),F(5,24),F(1,3)]
 for q0,ratio in [([F(1,4)]*4,F(27,25)),([F(1,4),F(5,16),F(5,16),F(1,8)],F(27,32))]:
  product=F(1)
  for old,new in zip(q0,target):product*=old/new
  ck(product==ratio)
ck(F(27,32)<1<F(27,25))
print(json.dumps({'status':'PASS','cases':cases,'exact_assertions':checks,'seconds':time.perf_counter()-start,'arithmetic':'Fraction/integer products, direct characters; no floating signs'},indent=2))
