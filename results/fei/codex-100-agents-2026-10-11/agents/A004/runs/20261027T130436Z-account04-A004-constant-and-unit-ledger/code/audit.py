"""Different representation audit: multinomial classes, not convolution."""
from check import *
import exact as E
from math import factorial

start=time.perf_counter();cases=0
for m in range(1,7):
    counts={}
    for a in range(m+1):
        for b in range(m-a+1):
            for c in range(m-a-b+1):
                d=m-a-b-c
                multiplicity=factorial(m)//(factorial(a)*factorial(b)*factorial(c)*factorial(d))
                uv=(-a+c+d,a+b-d)
                counts[uv]=counts.get(uv,0)+multiplicity
    ck(counts==conv(m))
    for w in (F(1,4),F(1,2),F(1)):
        # A genuinely matched component removes the positive mismatch barrier.
        divergence={}
        for (u,v),mult in counts.items():
            ratio=w+(1-w)*F(2)**(-u)
            ck(ratio>=w)
            divergence=add((1,divergence),(-F(mult,4**m),logq(ratio)))
        ck(bounds(divergence)[0]>=0)
        ck(bounds(add((-1,logq(w)),(-1,divergence)))[0]>=0)
        if w==1:ck(divergence=={})
        cases+=1
    # Literal truth-table word enumeration gives a third representation at m<=3.
    if m<=3:
        brute={}
        for word in range(4**m):
            u=v=0;z=word
            for _ in range(m):
                du,dv=[(-1,1),(0,1),(1,0),(1,-1)][z%4];z//=4;u+=du;v+=dv
            brute[u,v]=brute.get((u,v),0)+1
        ck(brute==counts)
    ck(time.perf_counter()-start<55)
# Character/constant point laws: no variance; scalar full mixture costs exact.
for m in (1,2,8):
    for w in (F(0),F(1,4),F(1)):
        qa,qb=F(1,2),F(1,4);prob=w*qa**m+(1-w)*qb**m
        ck(prob<=max(qa,qb)**m)
        price=add((-1,logq(prob)))
        ck(bounds(add((1,price),(-m,logq(F(2)))))[0]>=0)
# Certified exact threshold in the all-m bound, no log approximations.
for m in (87,88,89,176):
    ck((F(m,8)**2>=F(11*m,8))==(m>=88))
# Excluded hypothesis control: an actual q=p component has zero gap.
p=(F(1,4),)*4;ck(KL(p,p)=={});ck(sum(p)==1)
out={'status':'PASS','assertions':E.COUNT,'mixture_cases':cases,'seconds':time.perf_counter()-start,'representation':'multinomial counts and literal short words independent of DP; matched-component/constant/dictator controls; exact m87/88 boundary','scope':'finite audit only; general theorem is the written finite-sum proof'}
(RUN/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
