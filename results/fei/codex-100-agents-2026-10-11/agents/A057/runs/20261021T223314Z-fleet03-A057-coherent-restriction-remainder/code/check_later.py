"""Frozen v1 exact physical Walsh check; no external writes or third party modules."""
from pathlib import Path
import itertools, json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
(ROOT/'out').mkdir(exist_ok=True)
START=time.monotonic()
def walsh(v):
    w=list(v);h=1
    while h<len(w):
        for j in range(0,len(w),2*h):
            for k in range(j,j+h):
                x,y=w[k],w[k+h];w[k],w[k+h]=x+y,x-y
        h*=2
    return w

def table(n,t):return [1 if (t>>x)&1 else -1 for x in range(1<<n)]

def check(ns,ts,r,s):
    cores=[table(n,t) for n,t in zip(ns,ts)]
    n=r+s+1+sum(ns);N=1<<n
    vals=[]
    for x in range(N):
        A=int(x&((1<<r)-1)==0);B=int((x>>r)&((1<<s)-1)==0);Y=(x>>(r+s))&1
        off=r+s+1;vs=[]
        for dim,c in zip(ns,cores):
            vs.append(c[(x>>off)&((1<<dim)-1)]);off+=dim
        u,v,g=vs
        vals.append(g if not Y else u if A else v if B else g)
    w=walsh(vals);bit=1<<r
    cross=sum(abs(w[j]*w[j|bit]) for j in range(N) if not j&bit)
    den=sum(w[j|bit]**2 for j in range(N) if not j&bit)
    physical=sum(vals[x]!=vals[x^bit] for x in range(N))
    assert den==physical*N
    assert 2*cross<=12*den,(ns,ts,r,s,cross,den)
    # Compare the analytically derived S bound using K and D on no-B cube.
    # Actual pair total is already a rigorous upper certificate for erasure,
    # given the separately proved scalar Phi(a^2,b^2)<=2|ab|.
    return cross,den,N

cases=0;zero=0;maxratio=(0,1);maxw=None
families=[(1,1,1),(2,1,1),(1,2,1),(1,1,2)]
for ns in families:
    for ts in itertools.product(*(range(1<<(1<<n)) for n in ns)):
        for r,s in itertools.product((1,2),repeat=2):
            if time.monotonic()-START>55:raise RuntimeError('Frozen 55-second cap exceeded; no complete-domain claim')
            cross,den,N=check(ns,ts,r,s);cases+=1;zero+=den==0
            if den and cross*maxratio[1]>maxratio[0]*den:
                maxratio=(cross,den);maxw=[ns,ts,r,s]

result={'helper':'check_later.py v1','cases':cases,'exact_assertions':2*cases,'zero_influence_cases':zero,
        'max_2cross_over_d_rational':[2*maxratio[0],maxratio[1]],'max_fixture':maxw,
        'elapsed_seconds':time.monotonic()-START,'arithmetic':'integer Walsh, no floating point used for signs',
        'status':'PASS','full_fei':'OPEN'}
(ROOT/'out'/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
