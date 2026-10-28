from fractions import Fraction as F
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
def fw(v):
 if len(v)==1:return v
 a=fw(v[::2]);b=fw(v[1::2]);return [x+y for x,y in zip(a,b)]+[x-y for x,y in zip(a,b)]
def probs(v):return [F(x*x,len(v)**2) for x in fw(v)]
def entropy(p):
 out=F(0)
 for x in p:
  if x:
   assert x.numerator==1 and x.denominator&(x.denominator-1)==0
   out+=x*(x.denominator.bit_length()-1)
 return out
G=[1,-1,1,-1];H=[1,1,-1,-1];P=probs(G+H)
# Recursive Walsh's ordering is bit-reversed: selector is frequency bit0 here.
erased=[P[2*j]+P[2*j+1] for j in range(4)]
B=entropy(P)-entropy(erased);delta=entropy(P)-F(1,2)*(entropy(probs(G))+entropy(probs(H)))
assert B==1 and delta==2
rounded=[]
for a,b in [(1,1),(1,-1),(-1,1),(-1,-1)]:
 Q=probs([a,b]);rounded.append(entropy(Q));assert entropy(Q)==0
assert B>sum(rounded)/4
parity=[1,-1,-1,1];assert sum(x!=parity[s^1] for s,x in enumerate(parity))/4==1
assert sum(x!=parity[s^2] for s,x in enumerate(parity))/4==1
out={'status':'PASS','checks':9,'actual_both_private_negative_control':{'G':'U','H':'V','B':1,'Delta':2,'d':'1/2','rho_sum':2,'average_rounded_B':0},'false_statement':'B<=E B(rounded pure phases) without a variance correction','scope':'refutes that proof step only, not B<=4d or FEI','multiple_private_guard':{'G':'U1*U2','rho':1,'Iprivate':2}}
(R/'out/CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
