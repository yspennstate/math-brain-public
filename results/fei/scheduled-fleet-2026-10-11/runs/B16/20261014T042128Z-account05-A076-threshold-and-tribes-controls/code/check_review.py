from pathlib import Path
from fractions import Fraction as F
import time,json
ROOT=Path(__file__).resolve().parents[1]
exec(compile((ROOT/'code/arithmetic.py').read_text(encoding='utf-8'),str(ROOT/'code/arithmetic.py'),'exec'))
start=time.perf_counter()
def edges(t,i):return F(sum(t[z]!=t[z^(1<<i)] for z in range(len(t))),len(t))
def mux(g,h):return tuple(v for a,b in zip(g,h) for v in [a,b])
def bent(s,k):return (-1)**sum(((s>>j)&1)*((s>>(j+1))&1) for j in range(0,k,2))
def shift(u,d,v):return plus((Phi((u+v)**2,d*d),F(1,4)),(Phi((u-v)**2,d*d),F(1,4)),(Phi(u*u,d*d),F(-1,2)))
sharp=[]
for k in [2,4,6,8]:
    a=F(1,1<<k);g=tuple(bent(z>>1,k)*(-1 if z==0 else 1) for z in range(1<<(k+1)))
    h=tuple(bent(z>>1,k) for z in range(len(g)));f=mux(g,h)
    expectedG=[a]+[F(1,2)+a]*k;expectedH=[F(0)]+[F(1,2)]*k
    expectedF=[a/2,a/2]+[F(1,2)+a/2]*k
    for t,expected in [(g,expectedG),(h,expectedH),(f,expectedF)]:
        for i,e in enumerate(expected):eq(inf(t,i),e);eq(edges(t,i),e)
    eq(I(f),F(k,2)+F(k+2,2)*a)
    sharp.append(dict(k=k,I_G=str(I(g)),I_H=str(I(h)),I_F=str(I(f))))
activated=[]
for k in [2,4]:
    for r in [1,2]:
        if time.perf_counter()-start>55:raise RuntimeError('frozen review deadline')
        a=F(1,1<<k);b=F(1,1<<(k//2));q=F(1,1<<r);c=(1-b+a)/2
        # branch coordinates: x, k shared s bits, then r common point controls
        gs=[];hs=[]
        for z in range(1<<(k+1+r)):
            active=(z>>(k+1))==0;s=(z>>1)&((1<<k)-1);x=z&1
            gs.append(-1 if active and s==0 and x==0 else 1)
            hs.append(bent(s,k) if active else 1)
        g=tuple(gs);h=tuple(hs);f=mux(g,h)
        expected=[q*c,q*a/2]+[q*(a+F(1,2))/2]*k+[q*c]*r
        for i,e in enumerate(expected):eq(inf(f,i),e);eq(edges(f,i),e)
        eq(I(f),q*(F(k,4)+F(k+1,2)*a+(r+1)*c))
        D=plus((B(f,1),F(1)),(B(g,0),F(-1,2)))
        formula=plus((shift(-a,a,b),q*((1<<k)-1)),(shift(-a,a,b-1),q*(1-q)),(shift(1-q*a,q*a,1-q+q*b),F(1)))
        equal_expr(plus((D,F(1)),(formula,F(-1))))
        if k>=4:leq(plus((D,F(-1))),-(k-4)*q*a/2)
        A=plus((B(f,1),F(1)),(B(g,0),F(-1,4)))
        leq(A,4*q*c);leq(plus((A,F(-1))),F(0))
        activated.append(dict(k=k,r=r,selector_influence=str(q*c),I_F=str(I(f))))
result=dict(status='PASS',exact_assertions=checks,elapsed_seconds=time.perf_counter()-start,sharp_full_influences=sharp,
            A077_actual_activated_roots=activated)
(ROOT/'out/REVIEW_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
