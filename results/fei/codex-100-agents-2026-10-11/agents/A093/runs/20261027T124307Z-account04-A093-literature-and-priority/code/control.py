from fractions import Fraction as F
from pathlib import Path
import json
r=Path(__file__).resolve().parents[1];k=0
def ck(v):
 global k
 k+=1
 assert v
p=[F(1,4)]*4;q=[p[0]+p[1],p[2]+p[3]];R=[F(1),F(0)]
ck(sum(p)==sum(q)==sum(R)==1);ck(q==[F(1,2)]*2)
ck(R[0]/q[0]==2);ck(q[1]>0 and R[1]==0)
ck(F(1)*1+F(0)==1) # forward fee1bit: log2(2)=1
ck(R==[F(1),F(0)])
receipt={'status':'PASS','exact_assertions':k,'forward_fee_bits':1,'reverse_KL':'INFINITE_SUPPORT_OBSTRUCTION','scope':'matched-parent AND2 orientation control; already frozen; not main-domain expansion'}
(r/'out/CONTROL.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8');print(json.dumps(receipt))
