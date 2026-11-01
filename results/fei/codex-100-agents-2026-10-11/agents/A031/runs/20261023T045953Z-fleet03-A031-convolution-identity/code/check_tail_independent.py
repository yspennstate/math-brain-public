from pathlib import Path
from fractions import Fraction as F
import json
R=Path(__file__).resolve().parents[1];checks=0
def ck(b):
 global checks
 assert b
 checks+=1
def log(x):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def ln(z):
  t=(z-1)/(z+1);v=t;s=F(0)
  for j in range(20):s+=v/(2*j+1);v*=t*t
  return 2*s,2*s+2*v/(41*(1-t*t))
 a,b=ln(x);c,d=ln(F(2));return k+a/d,k+b/c
def L(w,x):return tuple(w*v for v in log(x))
def add(*xs):return tuple(sum(x[j] for x in xs) for j in [0,1])
amps={s:F(3,4) if s==0 else F(-1,4) for s in range(8)};p={s:v*v for s,v in amps.items()};ck(sum(p.values())==1)
M=[];Bx=[]
for i in range(3):
 bit=1<<i
 for S in p:
  if S&bit:continue
  a,b=p[S],p[S|bit];M.append(L(b,(a+b)/b))
  if i==0:Bx.extend([L(a,(a+b)/a),L(b,(a+b)/b)])
childCE=[]
for u in [0,1]:
 pp={S:(amps[S]+(-1)**u*amps[S|1])**2 for S in [0,2,4,6]};ck(sum(pp.values())==1)
 # Retained marker here is bit1; query variable was bit0.
 Q={S:(pp[S&~2]+pp[S|2])/2 for S in pp};ck(sum(Q.values())==1)
 childCE.append(add(*(L(v,1/Q[S]) for S,v in pp.items() if v)))
cinf=add(add(*M),add(*Bx),tuple(sum(x[j] for x in childCE)/2 for j in [0,1]));source=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))['tail'];a,b=[F(x) for x in source['C_infinity']];ck(max(a,cinf[0])<=min(b,cinf[1]))
Mcoeff=[350,4,2];Ecoeff=[584,24,0];P=[Mcoeff[j]+5*Ecoeff[j] for j in range(3)];ck(P==[3270,124,2]);val=sum(v*20**j for j,v in enumerate(P));ck(val==6550)
lower=F(17,4)-cinf[1]-F(4*val+17,4*(1<<20));ck(lower>F(7,8))
out={'checks':checks,'method':'direct limiting root rows and actual child amplitudes; distinct20-term rational log enclosures','tail_endpoint_L':20,'P_coefficients_low_first':P,'original_spare_lower':str(lower),'strictly_greater_than':'7/8'}
(R/'out/TAIL_REPRODUCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'checks':checks,'result':'tail endpoint independently PASS'}))
