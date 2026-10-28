from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
R=Path(__file__).resolve().parents[1];spec=json.loads((R/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'));assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest()==spec['audit_sha256'];t0=time.perf_counter();checks=0
def ck(v):
 global checks
 checks+=1;assert v,checks;assert time.perf_counter()-t0<55
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]
def coeff(v,s):return F(sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(v)),len(v))
b=[1-x*x for x in a];A=[coeff(a,j) for j in range(16)];B=[coeff(b,j) for j in range(16)]
coefficients=0;roots=0
for L in [1,2,3]:
 h=[]
 for y in range(1<<(3*L)):
  u=[((y>>(L*j))%2**L).bit_count()%2 for j in range(3)];h.append(-1 if len(set(u))==1 else 1)
 for sg in [-1,1]:
  roots+=1;v=[a[x]+sg*b[x]*h[y] for y in range(len(h)) for x in range(16)]
  piv=[F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v)) for j in range(4+3*L)]
  ck(piv[:4]==([F(5,16),F(5,16),F(1,2),F(1,2)] if sg==1 else [F(7,16),F(7,16),F(1,2),F(1,2)]));ck(all(z==F(3,16) for z in piv[4:]))
  if L==1:
   H=[coeff(h,j) for j in range(8)]
   for s in range(len(v)):
    coefficients+=1;u,w=s%16,s//16;expected=A[u]+sg*B[u]*H[0] if w==0 else sg*B[u]*H[w]
    ck(coeff(v,s)==expected)
# Independent rational multiplicative certificate for the sharp price.
p=[F(1,4)]*4;q=[F(1,4),F(5,24),F(5,24),F(1,3)];ratio=F(1)
for u,v in zip(p,q):ratio*=u/v
ck(ratio==F(27,25));ck(1<ratio<2)
ck(F(35,4)-F(1,4)-6-F(3,32)==F(77,32))
out={'status':'PASS','checks':checks,'roots_direct_pivots':roots,'direct_character_coefficients':coefficients,'exact_price_power_ratio':str(ratio),'runtime_seconds':round(time.perf_counter()-t0,6),'independence':'No import of main checker, exact helper, or author helpers'}
(R/'out/INDEPENDENT_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
