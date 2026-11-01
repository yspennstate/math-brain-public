from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261014T054454Z-fleet05-A014-overlap-beyond-worst-case-read/code/check.py'
exec(compile(old.read_text(encoding='utf-8').split('rows=[];candidates=0;sets=0;wins=')[0],str(old),'exec'),globals())
budget=60
C=[int(z.bit_count()<=1) for z in range(8)]
def transform(vals):
 return [sum(F(val*(-1 if (A&z).bit_count()%2 else 1),len(vals)) for z,val in enumerate(vals)) for A in range(len(vals))]
fh=transform([1-2*c for c in C]);p=[a*a for a in fh]
I=sum(F(A.bit_count())*pA for A,pA in enumerate(p))
ck(I==F(3,2));ck(p==[0,F(1,4),F(1,4),0,F(1,4),0,0,F(1,4)])
c0=transform([C[z<<1] for z in range(4)]);c1=transform([C[(z<<1)+1] for z in range(4)])
s=F(sum(C),8);row=[(c0[A>>1]**2+c1[A>>1]**2)/(4*s) for A in range(8)]
ck(s==F(1,2));ck(row[0]==F(5,16))
rowstar=[row[A]/(1-row[0]) for A in range(1,8)]
ck(rowstar==[F(5,11)]+[F(1,11)]*6)
P=p[1:];epsilon=F(1,2**64);atom=2
q=[epsilon if A==atom else (1-epsilon)*rowstar[A-1]/F(10,11) for A in range(1,8)]
ck(sum(q)==1 and min(q)>0)
def kl(a,b):
 ca,ha=CE(a,b),CE(a,a);return ca[0]-ha[1],ca[1]-ha[0]
kp=kl(P,q);kr=kl(rowstar,q)
margin=(kp[0]-kr[1]-F(9,2)*I,kp[1]-kr[0]-F(9,2)*I)
ck(margin[0]>F(15,4))
out={'method':'direct finite character sums; no FWHT used for triangle probabilities','s':str(s),'I':str(I),'r':str(row[0]),'L':'11/4','epsilon':str(epsilon),'coefficient_one_plus_9I_over2_failure_margin':outward(margin),'strict_margin_lower_bound':'15/4','assertions':assertions,'elapsed_seconds':time.monotonic()-start}
(R/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
