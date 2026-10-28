from fractions import Fraction as Q
from pathlib import Path
import json,time
t0=time.monotonic(); checks=0
def ck(v):
 global checks
 checks+=1
 assert v
 assert time.monotonic()-t0<55
def factors(f,A):
 B=15^A
 # rank-one sign matrix iff f(x)=f(x_A) f(x_B) / f(0)
 return all(f[x]*f[0]==f[x&A]*f[x&B] for x in range(16))
parts=[A for A in range(1,15) if A&1]
def infl(f,direction): return Q(sum(f[x]!=f[x^direction] for x in range(16)),16)
cases=0
for a in range(16):
 for b in range(16):
  base=[(-1 if a>>(x&3)&1 else 1)*(-1 if b>>(x>>2)&1 else 1) for x in range(16)]
  ck(sum(v<0 for v in base)%2==0)
  ck(factors(base,3)) # positive control MUST find a genuine product
  original=[infl(base,1<<i) for i in range(4)]
  for vertex in range(16):
   f=base[:]; f[vertex]*=-1; cases+=1
   ck(sum(v<0 for v in f)%2==1)
   for A in parts: ck(not factors(f,A))
   for i in range(4): ck(abs(infl(f,1<<i)-original[i])<=Q(1,8))
   for direction in range(1,16): ck(0<infl(f,direction)<1)
rows=[]
for m in [8,9,10,12]:
 d=Q(1,1<<(m-1)); L=(1<<(m-1))//m; N=m*L
 I=L*m*d
 ck(Q(15,16)<=I<=1); ck(N>=128)
 u=Q(1,1<<(N-1))
 ck(N*u<Q(1,16)); ck(N*u*Q(2*N+1,2)<Q(1,16))
 # eta upper bounded rationally for both even and odd N.
 eta_upper=Q(1,1<<(N//2-1))
 ck(eta_upper*Q(3*N+1,2)<Q(1,16))
 lower=Q(15,16)*(m-5-Q(2,m))-Q(1,8)
 rows.append({'m':m,'L':L,'N':N,'I_before':str(I),'TC_after_strict_lower_bound':str(lower),'H_after_upper_bound':'69/16','I_after_interval':['7/8','17/16']})
out={'status':'PASS','assertions':checks,'flipped_constructions':cases,'unflipped_positive_controls':256,'partitions_per_flip':len(parts),'rows':rows,'runtime_seconds':time.monotonic()-t0}
r=Path(__file__).resolve().parents[1]; (r/'out').mkdir(exist_ok=True)
(r/'out/checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
