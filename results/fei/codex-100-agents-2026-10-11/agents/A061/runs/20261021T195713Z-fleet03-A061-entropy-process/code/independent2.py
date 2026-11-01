from pathlib import Path
from fractions import Fraction as Q
import time,json
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(b):
 global checks
 checks+=1
 assert b
def sign(x):return 1-2*(x&1)
def gf4(a,b):
 a0=a&1;a1=a>>1;b0=b&1;b1=b>>1
 return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1)<<1)
def values():
 g=[];h=[]
 for t in range(256):
  bits=[(t>>j)&1 for j in range(8)]
  u=sum(bits)%2;v=bits[1];a=bits[2]+2*bits[3];b=bits[4]+2*bits[5];x=bits[6]+2*bits[7]
  G=sign(u*v);H=G*sign(a)*(-1 if x==gf4(a,b) else 1)
  g.append(G);h.append(H)
 return g,h
def direct(a):return [sum(v*sign((s&t).bit_count()) for t,v in enumerate(a)) for s in range(len(a))]
g,h=values();f=[g[t//2] if t%2==0 else h[t//2] for t in range(512)]
wg,wh,wf=map(direct,[g,h,f]);pg=[Q(x*x,256**2) for x in wg];ph=[Q(x*x,256**2) for x in wh];pf=[Q(x*x,512**2) for x in wf]
ck(sum(pg)==sum(ph)==sum(pf)==1);ck(all(not(a and b) for a,b in zip(pg,ph)))
ck(sorted([x for x in pg if x])==[Q(1,4)]*4);ck(sorted([x for x in ph if x])==[Q(1,256)]*192+[Q(1,16)]*4)
for p,n in [(pg,8),(ph,8),(pf,9)]:
 for j in range(n):ck(sum(p[s] for s in range(1<<n) if s>>j&1)==Q(1,2))
q=[pf[2*s]+pf[2*s+1] for s in range(256)]
refonly=[s for s,x in enumerate(q) if not x];ck(len(refonly)==56)
r=sum(Q(1,256)*(pg[s]/(2*q[s]) if q[s] else Q(1,2)) for s in range(256));ck(r==Q(1,8));ck(4*r*(1-r)==Q(7,16));ck(4*r*(1-r)<Q(1,2))
def entropy_dyadic(p):
 ans=Q(0)
 for x in p:
  if not x:continue
  ck(x.numerator==1 and x.denominator&(x.denominator-1)==0)
  ans+=x*(x.denominator.bit_length()-1)
 return ans
Hg,Hh,Hf=map(entropy_dyadic,[pg,ph,pf]);ck((Hg,Hh,Hf)==(2,7,Q(13,2)))
Kp=9-Hf;Kc=8-(Hg+Hh)/2;Sbar=16-(Hg+Hh)/2
ck(Kc-Kp==1);ck(Sbar==Q(23,2));ck(Hf-(Hg+Hh)/2==2)
out=dict(status='PASS',checks=checks,seconds=time.perf_counter()-start,dimension=9,r_G=str(r),reference_only_atoms=len(refonly),entropy_bits=list(map(str,[Hg,Hh,Hf])),TC_parent=str(Kp),TC_mean_children=str(Kc),original_Sbar=str(Sbar),O='(1/2)log2(16/7)',D='1+(1/2)log2(16/7)',D_over_query_influence='6-log2(7) > 3',arithmetic='direct character sums, explicit GF4 and exact rational dyadic entropy')
assert out['seconds']<55
(R/'out'/'INDEPENDENT_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
