from pathlib import Path
from fractions import Fraction as Q
from collections import Counter,defaultdict
import json,time,math
import kernel as k
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();k.CAP=50
def walsh(t):
 return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t))]
def factor(n):
 d=2;out={}
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def coefficients(pairs,den):
 out=defaultdict(Q)
 for (a,b),c in pairs.items():
  for value,sgn in ((a+b,1),(a,-1),(b,-1)):
   for prime,e in factor(value).items():out[prime]+=Q(c*sgn*value*e,den)
 return {p:v for p,v in out.items() if v}
def diff(a,b,weight=Q(1)):
 out={p:a.get(p,Q(0))-weight*b.get(p,Q(0)) for p in a.keys()|b.keys()}
 return {p:v for p,v in out.items() if v}
def certify(c):
 scale=math.lcm(*(v.denominator for v in c.values()));exponents={p:int(v*scale) for p,v in c.items()}
 num=math.prod(p**e for p,e in exponents.items() if e>0)
 den=math.prod(p**(-e) for p,e in exponents.items() if e<0)
 assert num!=den
 return dict(sign=1 if num>den else -1,scale=scale,prime_exponents=exponents,numerator_bits=num.bit_length(),denominator_bits=den.bit_length(),method='exact integer product comparison; prime_exponents regenerate both integers')
module=[k.bent(a&15,4)*(-1 if (a&15)==0 and (a>>4)&1 else 1) for a in range(32)]
gm=walsh(module[:16]);hm=walsh(module[16:]);up=[(a+b)//2 for a,b in zip(gm,hm)];vp=[(a-b)//2 for a,b in zip(gm,hm)]
beta=coefficients(Counter(zip((u*u for u in up),(v*v for v in vp))),256)
records=[]
for point in (0,1):
 t=[];cp=[];cm=[]
 for y in range(4):
  phase=(-1 if y.bit_count()%2 else 1)*(-1 if y==point else 1);b=k.bent(y,2)
  cp.append(b if phase==1 else 0);cm.append(b if phase==-1 else 0)
 for z in (0,1):
  for x in range(16):
   for y in range(4):t.append(k.bent(x,4)*(cp[y]+cm[y]*(-1 if x==0 and z else 1)))
 g,h=t[:64],t[64:];ga,ha=walsh(g),walsh(h)
 u=[(a+b)//2 for a,b in zip(ga,ha)];v=[(a-b)//2 for a,b in zip(ga,ha)]
 pairs=Counter(zip((a*a for a in u),(b*b for b in v)))
 B=coefficients(pairs,4096);p=Q(sum(c!=0 for c in cm),4)
 ca,cb=walsh(cp),walsh(cm);bx=walsh([k.bent(x,4) for x in range(16)])
 flipped=walsh([k.bent(x,4)*(-1 if x==0 else 1) for x in range(16)])
 t0=[(a+b)//2 for a,b in zip(bx,flipped)];t1=[(a-b)//2 for a,b in zip(bx,flipped)]
 barpairs=Counter((ca[s]**2*bx[q]**2+cb[s]**2*t0[q]**2,cb[s]**2*t1[q]**2) for s in range(4) for q in range(16))
 bar=coefficients(barpairs,4096)
 rho=Q(sum(a*a+b*b for a,b in zip(u,v) if b),4096)
 rg=Q(sum(a*a for a,b in zip(ga,v) if b),4096);rh=Q(sum(a*a for a,b in zip(ha,v) if b),4096)
 assert rg==rh==rho==1 and sum(a*b for a,b in zip(u,v))==0
 d=Q(sum(b*b for b in v),4096)
 within=k.sub(k.h2(d),k.split(t,6)['B'])
 exactB=(Q(0),Q(0))
 for prime,c in B.items():exactB=k.add(exactB,k.mul(k.logint(prime),c))
 delta=certify(diff(B,beta,p));signed=certify(diff(B,bar));ambiguity=certify(diff(bar,beta,p))
 assert delta['sign']==signed['sign']==(-1 if point==0 else 1) and ambiguity['sign']==1
 I=Q(sum(t[x]!=t[x^(1<<j)] for x in range(128) for j in range(7)),128)
 assert I==Q(205 if point==0 else 197,64)
 records.append(dict(point=point,p=str(p),I=str(I),d=str(d),rho=str(rho),within_carrier_credit=k.emit(within),B=k.emit(exactB),B_prime_log_coefficients={str(p):str(v) for p,v in B.items()},coherent_pairs={str(p):c for p,c in pairs.items()},incoherent_pairs_child_scaled={str(p):c for p,c in barpairs.items()},denominator=4096,total_correction_certificate=delta,signed_correction_certificate=signed,ambiguity_certificate=ambiguity))
out=dict(helper_version='A035-direct-collision-reproducer-v1',runtime_seconds=time.perf_counter()-start,case_count=2,records=records,status='PASS; independent transform and exact integer sign certificates')
(ROOT/'out'/'reproduction.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
