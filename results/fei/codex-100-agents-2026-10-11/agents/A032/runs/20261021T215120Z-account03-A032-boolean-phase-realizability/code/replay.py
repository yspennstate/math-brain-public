from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
import json,time,math
R=Path(__file__).resolve().parents[1]; t=time.perf_counter(); checks=0
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]
def fw(v):
    v=list(v);step=1
    while step<len(v):
        for start in range(0,len(v),2*step):
            for j in range(start,start+step):v[j],v[j+step]=v[j]+v[j+step],v[j]-v[j+step]
        step*=2
    return v
def ck(v):
    global checks
    checks+=1;assert v
    assert time.perf_counter()-t<60
def plus(x,y):return tuple(i+j for i,j in zip(x,y))
def half(x):return tuple(i/2 for i in x)
def neg(x):return tuple(-i for i in x)
@lru_cache(None)
def sign(x):
    # a+b log2(3) has sign of 2^(La)3^(Lb)-1, L>0.
    L=math.lcm(x[0].denominator,x[1].denominator)
    p,q=int(L*x[0]),int(L*x[1]);num=2**max(p,0)*3**max(q,0);den=2**max(-p,0)*3**max(-q,0)
    return (num>den)-(num<den)
@lru_cache(None)
def base(st):
    free=[i for i in range(4) if st[i]<0]
    inds=[sum((st[i] if st[i]>=0 else (v>>free.index(i)&1))<<i for i in range(4)) for v in range(1<<len(free))]
    av=[a[i] for i in inds]; bv=[1-x*x for x in av]
    truth=[x+z*y for z in [1,-1] for x,y in zip(av,bv)]
    W=fw(truth);N=len(truth);H=[Q(0),Q(0)];I=Q(0)
    for s,w in enumerate(W):
        p=Q(w*w,N*N)
        I+=s.bit_count()*p
        if not p:continue
        for v,k in [(p.denominator,1),(p.numerator,-1)]:
            for j,prime in enumerate([2,3]):
                e=0
                while v%prime==0:v//=prime;e+=1
                H[j]+=k*e*p
            ck(v==1)
    ck(I==Q(sum(truth[v]!=truth[v^(1<<i)] for i in range(len(free)+1) for v in range(N)),N))
    return tuple(H),I
@lru_cache(None)
def hist(st):
    H,I=base(st); ans=Counter({(Q(0),Q(0)):1})
    for i in range(4):
        if st[i]>=0:continue
        kids=[]
        for bit in [0,1]:s=list(st);s[i]=bit;kids.append(tuple(s))
        h0,i0=base(kids[0]);h1,i1=base(kids[1])
        delta=plus(H,neg(half(plus(h0,h1))));inf=I-(i0+i1)/2
        cost=plus(delta,(-4*inf,Q(0)))
        for x,nx in hist(kids[0]).items():
            for y,ny in hist(kids[1]).items():
                ans[plus(cost,half(plus(x,y)))]+=nx*ny
    ck(sum(ans.values())==[1,2,9,244,238145][st.count(-1)])
    return ans
root=(-1,)*4; hh=hist(root);limit=(Q(1),-Q(9,16))
for value in hh:ck(sign(plus(limit,neg(value)))>=0)
ck(limit in hh);ck(sign(plus(limit,(-Q(1,10),Q(0))))>0);ck(sign(plus((Q(1,8),Q(0)),neg(limit)))>0)
data={'PASS':True,'checks':checks,'seconds':time.perf_counter()-t,'trees':sum(hh.values()),'distinct_costs':len(hh),'maximum':[str(x) for x in limit],'maximizing_trees':hh[limit],'histogram':[{'cost':[str(y) for y in x],'trees':v} for x,v in sorted(hh.items())]}
(R/'out/replay.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in data.items() if k!='histogram'},indent=2))
