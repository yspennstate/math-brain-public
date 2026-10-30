from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import time,json
ROOT=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0; inputs=0
def ck(test):
    global checks
    checks+=1
    assert test,checks
    assert time.perf_counter()-start<55
@lru_cache(None)
def ln(x):
    z=(x-1)/(x+1); v=z; s=F(0)
    for j in range(24): s+=2*v/(2*j+1); v*=z*z
    return s,s+2*v/(49*(1-z*z))
@lru_cache(None)
def log2(x):
    k=x.numerator.bit_length()-x.denominator.bit_length(); y=x/(F(2)**k)
    if y<1:k-=1; y*=2
    l,h=ln(y); a,b=ln(F(2))
    return F(k)+l/b,F(k)+h/a
def dist(vals):
    N=len(vals)
    return [F(sum(v*(-1 if (x&A).bit_count()%2 else 1) for x,v in enumerate(vals))**2,N*N) for A in range(N)]
def influence(vals,n):return F(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals)) for i in range(n)),len(vals))
def cost(P,Q):
    lo=hi=F(0)
    for A,p in enumerate(P):
        if A and p:
            l,h=log2(1/Q[A]); lo+=p*l;hi+=p*h
    return lo,hi
rows=[]
for truth in range(1,15):
    hv=[1 if truth>>a&1 else -1 for a in range(4)]
    b=F(sum(x==1 for x in hv),4); Ph=dist(hv); Ih=influence(hv,2); vh=sum(Ph[1:])
    ck(vh==4*b*(1-b))
    for q in [{1:F(1,3),2:F(1,3),3:F(1,3)},{1:F(1,2),2:F(1,3),3:F(1,6)}]:
        cl,ch=cost(Ph,q); ck(ch<4*Ih)
        for k in [1,2,3]:
            n=k+2; mask=(1<<k)-1; t=F(1,1<<k)
            vals=[1 if x&mask or hv[x>>k]==1 else -1 for x in range(1<<n)]
            inputs+=len(vals); PG=dist(vals); IG=influence(vals,n)
            R={D:F(1,2*((1<<k)-1)) for D in range(1,1<<k)}
            for A,p in q.items():
                for D in range(1<<k): R[(A<<k)|D]=p*t/2
            ck(sum(R.values())==1)
            ck(IG==2*t*k*(1-b)+t*Ih)
            for D in range(1,1<<k):ck(PG[D]==4*t*t*(1-b)**2)
            for A in [1,2,3]:
                for D in range(1<<k):ck(PG[(A<<k)|D]==t*t*Ph[A])
            lo,hi=cost(PG,R)
            coremass=4*t*(1-t)*(1-b)**2
            ll,lh=log2(F((1<<k)-1)); fl=coremass*(1+ll)+t*(k+1)*vh+t*cl;fh=coremass*(1+lh)+t*(k+1)*vh+t*ch
            ck(lo<=fh and fl<=hi)
            ck(hi<=4*IG)
            rows.append({'inner_truth':truth,'core_size':k,'reference':[str(q[a]) for a in [1,2,3]],'I':str(IG),'C_interval':[str(lo),str(hi)]})
out={'status':'PASS','helper_version':'A006-paid-core-lift-v1','reference_cases':len(rows),'distinct_physical_truth_tables':42,'assertions':checks,'truth_inputs_with_reference_repetition':inputs,'seconds':time.perf_counter()-start,'rows':rows,'log_certificate':'24-term rational atanh with geometric tail; no floating arithmetic in certificates'}
(ROOT/'out/TRANSFER.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','reference_cases','assertions','truth_inputs_with_reference_repetition','seconds']}))
