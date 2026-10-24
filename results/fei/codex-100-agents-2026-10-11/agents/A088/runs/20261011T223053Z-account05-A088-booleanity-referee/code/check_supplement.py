from pathlib import Path
from fractions import Fraction as F
from math import factorial
from collections import defaultdict
import json,time
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();count=0
def ck(x):
 global count
 assert x
 count+=1
def placements(values):
 def rec(i,left,energy,den):
  if i==len(values):return factorial(16)//den if left==energy==0 else 0
  v=values[i];total=0
  for c in range(left+1):
   if c*v*v>energy:break
   total+=rec(i+1,left-c,energy-c*v*v,den*factorial(c))
  return total
 return rec(0,16,256,1)
census=placements([0,4,8,12,16])+placements([2,6,10,14]);ck(census==975621)
for mask in range(256):
 P=[(mask>>x)&1 for x in range(8)];coeff=P[:]
 for i in range(3):
  for s in range(8):
   if s&(1<<i):coeff[s]^=coeff[s^(1<<i)]
 for i in range(3):
  d=max([s.bit_count()-1 for s in range(8) if coeff[s] and s&(1<<i)]+[0])
  weights=sum(P[x]^P[x^(1<<i)] for x in range(8))
  if 0<weights<8:
   ck(d>=1);ck(F(weights,8)>=F(1,1<<d));ck(F(weights,8)<=1-F(1,1<<d))
  else:ck(d==0)
# Formal rational-log implementation: expand log rational into prime logs.
def prime(n):
 r={};d=2
 while d*d<=n:
  while n%d==0:r[d]=r.get(d,0)+1;n//=d
  d+=1
 if n>1:r[n]=r.get(n,0)+1
 return r
def logadd(out,c,x):
 x=F(x)
 for p,k in prime(x.numerator).items():out[p]+=c*k
 for p,k in prime(x.denominator).items():out[p]-=c*k
def KL(p,q):
 out=defaultdict(F)
 for s,v in p.items():
  if v:logadd(out,v,v/q[s])
 return out
v=F(1,2);Qr={s:F(1,7) for s in range(1,8)};Pplus=Qr.copy()
for s,k in [(1,1),(6,1),(2,-1),(5,-1)]:Pplus[s]+=F(k,28)
ck(sum(Pplus.values())==1)
r=[sum(p for s,p in Pplus.items() if s&(1<<i)) for i in range(3)];ck(r==[F(4,7)]*3)
P={0:1-v,**{s:v*p for s,p in Pplus.items()}};M={0:1-v,**{s:v*p for s,p in Qr.items()}}
d=F(2,7);Q={s:d**s.bit_count()*(1-d)**(3-s.bit_count()) for s in range(8)}
full,occ,delta=KL(P,Q),KL(Pplus,Qr),KL(M,Q)
identity={str(p):str(full[p]-v*occ[p]-delta[p]) for p in set(full)|set(occ)|set(delta)}
for p in set(full)|set(occ)|set(delta):ck(full[p]==v*occ[p]+delta[p])
factor=[]
for m in range(2,13):
 d=F(1,1<<(m-1));v=2*d-d*d;r=1/(2-d);c=1-d/2
 ck(c*r==F(1,2));ck(1-c==(1-c*r)**m)
 ck(v==((1<<m)-1)*d*d)
 factor.append({'m':m,'occupancy_KL':'0','normalization_correction':'K_full'})
# phase-blind countercontrol, direct character transforms of named children.
f=[1,1,1,-1];g=[1,1,-1,1]
def walsh(a):return [sum(a[x]*(1-2*((s&x).bit_count()%2)) for x in range(len(a))) for s in range(len(a))]
ck([x*x for x in walsh(f)]==[x*x for x in walsh(g)])
ck(walsh(f[0::2])==[2,0]);ck(walsh(g[0::2])==[0,2])
out={'status':'PASS','assertions':count,'seconds':time.perf_counter()-start,'n4_arithmetic_candidate_laws':census,'n3_phase_tables':256,'occupancy_formal_log_identity':identity,'point_defect_conditioning':factor}
(ROOT/'out/SUPPLEMENT_VALIDATION.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
