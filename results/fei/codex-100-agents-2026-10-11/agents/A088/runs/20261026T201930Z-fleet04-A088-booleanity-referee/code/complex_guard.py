from fractions import Fraction as F
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
ct=0
def ck(x):
 global ct
 assert x;ct+=1
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sq(a):return a[0]*a[0]+a[1]*a[1]
def spec(t):
 n=len(t);return [sq(tuple(sum(((-1)**((i&j).bit_count()%2))*t[j][k] for j in range(n))/n for k in [0,1])) for i in range(n)]
u=(F(399,401),F(40,401));one=(F(1),F(0));t=[one,one,u,neg(u)]
for z in t:ck(sq(z)==1)
ck(spec(t)==[F(1,4)]*4)
for i in [0,1]:ck(sum(sq(add(t[j],neg(t[j^(1<<i)]))) for j in range(4))/16==F(1,2))
ck(spec([one,u])==[F(400,401),F(1,401)])
ck(401>16)
(R/'out/COMPLEX.json').write_text(json.dumps({'exact_assertions':ct,'root_flat':True,'all_conditional_norms':1,'child_energy':'1/401','positive_rate4_debit':'h2(1/401)-4/401 > (log2(401)-4)/401 >0','scope':'relaxed nonpositive clean-node claim fails; no Boolean FEI counterexample'},indent=2),encoding='utf-8')
print('complex diagnostic PASS',ct)
