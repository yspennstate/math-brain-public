from pathlib import Path
from fractions import Fraction as Q
import json,time
start=time.monotonic(); assertions=0
out=Path(__file__).resolve().parents[1]/'out'
def ck(b):
    global assertions
    assertions+=1
    assert b
    if time.monotonic()-start>55:raise RuntimeError('55s cap')
def parity(x):return x.bit_count()%2
def direct(f):
    return [Q(sum(a*(-1)**parity(x&s) for x,a in enumerate(f)),len(f)) for s in range(len(f))]
def physical(f,u):return Q(sum(f[x]!=f[x^u] for x in range(len(f))),len(f))
fixtures=0; failures=[]
for n in range(4):
    for mask in range(1<<(1<<n)):
        f=[1-2*((mask>>x)&1) for x in range(1<<n)]
        F=[f[x&((1<<n)-1)] if x>>n==0 else 1 for x in range(1<<(n+2))]
        cf=direct(f); cF=direct(F); mu=cf[0]; p=Q(1,4)
        for u in range(1<<(n+2)):
            W=physical(F,u)
            ck(W==(p*(1-mu) if u>>n else p*physical(f,u)))
            ck(W==sum(a*a for s,a in enumerate(cF) if parity(s&u)))
        # All directional raw-basis comparisons in input space.
        condition=all(physical(f,u)>=physical(f,1<<i) for u in range(1,1<<n) for i in range(n) if u>>i&1)
        actual=all(min(physical(F,u),1-physical(F,u))>=physical(F,1<<i) for u in range(1,1<<(n+2)) for i in range(n+2) if u>>i&1)
        ck(condition==actual)
        for i in range(n):ck(physical(f,1<<i)<=1-mu)
        fixtures+=1
# k1 boundary: h=-1, activated function is a control character.
F=[-1,1];ck(physical(F,1)==1);ck(min(physical(F,1),1-physical(F,1))==0)
result={'status':'PASS','fixtures':fixtures,'assertions':assertions,'seconds':time.monotonic()-start,'arithmetic':'Fraction, direct characters and all physical translation edges; no imported FWHT/helper','boundary':'k1 negative constant fails affine minimality'}
(out/'INDEPENDENT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
