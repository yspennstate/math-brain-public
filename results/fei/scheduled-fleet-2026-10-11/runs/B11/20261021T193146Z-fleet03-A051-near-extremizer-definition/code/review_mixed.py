"""Independent character-sum reconstruction of A055's named critical guard."""
from pathlib import Path
from fractions import Fraction as F
import json,time
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0
def ck(b):
    global checks
    checks+=1; assert b,checks
def spectrum(f):
    return [sum(z*((-1)**((x&s).bit_count()%2)) for x,z in enumerate(f)) for s in range(len(f))]
def H(f):
    # all n<=3 tables have only these three complete spectral profiles.
    a=spectrum(f); N=len(f); ms=tuple(sorted(F(x*x,N*N) for x in a if x))
    if ms==(F(1),): return (F(0),F(0))
    if ms==(F(1,4),)*4: return (F(2),F(0))
    ck(ms==(F(1,16),)*7+(F(9,16),))
    return (F(4),-F(9,8)) # c0+c3*log2(3)
def I(f):
    n=(len(f)).bit_length()-1
    return F(sum(f[x]!=f[x^(1<<i)] for x in range(len(f)) for i in range(n)),len(f))
def plus(*vs): return tuple(sum(v[i] for v in vs) for i in range(2))
def neg(v): return tuple(-x for x in v)
profiles={}
for n in range(4):
    for t in range(1<<(1<<n)):
        f=[1-2*((t>>x)&1) for x in range(1<<n)]
        h=H(f); j=I(f); key=str(h)
        profiles[key]=min(profiles.get(key,j),j)
        if h==(0,0): ck(j>=0)
        elif h==(2,0): ck(j>=1)
        else: ck(j>=F(3,4))
# Entropy zero and entropy2 profiles have D2<=0; point profile maximizes
# at minimum I=3/4. Its deficit>1/4 since log2(3)<2 (3<4).
ck(3<4)
f=[-1]+[1]*7
edit=lambda E:[-z if x in E else z for x,z in enumerate(f)]
a=edit({0}); b=edit({7}); both=edit({0,7})
ck(H(a)==(0,0) and H(b)==(2,0) and H(both)==H(f))
ck(I(a)==0 and I(b)==F(3,2) and I(both)==I(f)==F(3,4))
T=plus(H(both),neg(H(a)),neg(H(b)),H(f))
ck(T==(F(6),-F(9,4)))
ck(3**5<2**8) # log2(3)<8/5, hence T>12/5.
ck((0^7).bit_count()==3)
for E in range(256):
    ep={x for x in range(8) if (E>>x)&1 and f[x]==1}
    em={x for x in range(8) if (E>>x)&1 and f[x]==-1}
    eu=ep|em
    e=sum((x^y).bit_count()==1 for x in ep for y in em)
    ck(I(edit(eu))-I(edit(ep))-I(edit(em))+I(f)==F(4*e,8))
res={'status':'PASS','assertions':checks,'tables':278,'ordered_mixed_edits':256,'profiles_minimum_I':{k:str(v) for k,v in profiles.items()},'mixed_T':[str(x) for x in T],'strict_certificate':'243<256','rung':'exact finite certificate plus analytic identities; independent reconstruction of A055 named guard only','runtime_seconds':time.monotonic()-start}
(ROOT/'out/REVIEW_A055_CHECK.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
print(json.dumps(res,indent=2))
