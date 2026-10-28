"""Direct-character independent certificate: a canonical return has positive cost."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
RUN=Path(__file__).resolve().parents[1]
def fourier(v):
    return [sum(F(y*(-1 if (x&s).bit_count()%2 else 1),len(v)) for x,y in enumerate(v)) for s in range(len(v))]
def law(v):return [a*a for a in fourier(v)]
def restriction(v,i,b):
    return [v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(v)//2)]
def canonical(g):
    eps=F(1,len(g));p=law(g);W=2*eps-sum(bool(x) for x in p)*eps*eps
    v=g+g;v[len(g)]*=-1
    q=[(1-W)*p[j] if j<len(p) and p[j] else eps*eps for j in range(len(v))]
    assert sum(q)==1
    return v,q
# Literal original h4*h2 point-selector; both narrow coordinates fixed to zero.
g=[(1-2*((x&15)==0))*(1-2*((x>>4)==0)) for x in range(64)]
root,_=canonical(g)
v,_=canonical([1 if x==0 else -1 for x in range(16)])
assert restriction(restriction(root,4,0),4,0)==v
v,Q=canonical([1 if x==0 else -1 for x in range(16)])
child=restriction(v,0,0);P=law(child)
otherP=law(restriction(v,0,1));mu=[(a+b)/2 for a,b in zip(P,otherP)]
r=[Q[2*j]+Q[2*j+1] for j in range(len(P))]
raw=[r[j]*P[j]/mu[j] if mu[j] else r[j] for j in range(len(P))]
Z=sum(raw);old=[x/Z for x in raw]
freshv,fresh=canonical([1 if x==0 else -1 for x in range(8)])
assert freshv==child and Z==F(529,452)
assert old[0]==F(18375,33856)
assert old[1:8]==[F(1695,33856)]*7 and old[8:]==[F(113,8464)]*8
assert fresh[0]==F(63,128) and fresh[1:8]==[F(7,128)]*7 and fresh[8:]==[F(1,64)]*8
ratios=Counter()
for p,a,b in zip(P,old,fresh):
    if p:ratios[a/b]+=p
assert ratios=={F(12250,11109):F(49,64),F(3390,3703):F(7,64),F(452,529):F(1,8)}
# Original reach of this third reset is 1/8. Multiply its log expression by512.
N=12250**49*3390**7*452**8
D=11109**49*3703**7*529**8
assert N>16*D and N*N<512*D*D
# Therefore 1/128 < (log2(N/D))/512 <9/1024, with exact integer comparisons.
out={'status':'EXACT_INTEGER_CERTIFICATE_PASS','family':'h4*h2 point-selector, w4 m0 d0 eta0, two narrow zero resets then wide coordinate0 zero canonical reset','original_reach':'1/8','inherited_normalizer':str(Z),'local_probability_ratio_classes':{str(k):str(v) for k,v in ratios.items()},'reached_excess_formula':'log2(N/D)/512','N':str(N),'D':str(D),'N_greater_than_16D':N>16*D,'N_squared_less_than_512D_squared':N*N<512*D*D,'strict_reached_excess_bounds':['1/128','9/1024'],'conclusion':'Canonical reset can strictly increase complete CE; this refutes the free-reset shortcut, not A095 two-reset theorem or FEI.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(RUN/'out/CANONICAL_POSITIVE_RESET_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['N','D','local_probability_ratio_classes']}))
