from fractions import Fraction as Q
from pathlib import Path
import json
def ln(y):
    z=(y-1)/(y+1)
    v=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
    return v,v+2*z**49/(49*(1-z*z))
L2=ln(Q(2))
def log(x):
    k=0
    while x<1: x*=2;k-=1
    while x>=2: x/=2;k+=1
    l,u=ln(x)
    corners=[a/b for a in [l,u] for b in L2]
    return min(corners)+k,max(corners)+k
def ent(p):
    l=u=Q(0)
    for x in p:
        if x:
            a,b=log(x);l-=x*b;u-=x*a
    return l,u
def sub(a,b): return a[0]-b[1],a[1]-b[0]
def scale(a,b):
    v=[b*x for x in a];return min(v),max(v)
P=[Q(x,256) for x in [196,12,12,36]]
assert sum(P)==1
E=sub(sub(scale(ent([Q(3,16),Q(13,16)]),2),ent(P)),scale(ent([Q(3,4),Q(1,4)]),Q(1,4)))
assert E[0]>Q(1,16)
out={'status':'PASS','p':'1/4','q':'1/4','parent_masses':[str(p) for p in P],'debt_interval':[str(x) for x in E],'certified_debt_gt':'1/16','arithmetic':'Fraction; 24-term range-reduced atanh, positive tail bound'}
(Path(__file__).resolve().parents[1]/'out'/'ORIGINAL_COUNTEREXAMPLE.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('PASS: original common-bias AND debt >1/16, exact rational interval')
