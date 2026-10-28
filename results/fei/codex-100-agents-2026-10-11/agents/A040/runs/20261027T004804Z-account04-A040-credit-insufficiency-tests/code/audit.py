"""Separate representation: direct character sums, rowwise transport, prime-log chain."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,time,hashlib
R=Path(__file__).resolve().parents[1]; N=0
def check(x):
    global N
    N+=1
    assert x,N
def factors(n):
    out={}; j=2
    while j*j<=n:
        while n%j==0: out[j]=out.get(j,0)+1; n//=j
        j+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def logs(p,q):
    out=defaultdict(F)
    for k,v in p.items():
        if not v: continue
        x=v/q[k]
        for j,e in factors(x.numerator).items(): out[j]+=v*e
        for j,e in factors(x.denominator).items(): out[j]-=v*e
    return dict(out)
def run():
    st=time.perf_counter(); cases=0
    for r in [3,4]:
        n=r+3; M=1<<n; vals={}
        for t in range(M):
            w=t>>3; core=(-1 if t&4 else 1)*(-1 if w==0 or(t&2 and w==3) else 1)
            vals[t]=core if t&1 else 1
        co={s:F(sum(v*(-1 if (s&t).bit_count()%2 else 1) for t,v in vals.items()),M) for s in range(M)}
        p={s:v*v for s,v in co.items() if v}
        a=F(1,r*r); q={s:(1-a)*v for s,v in p.items()}
        for s in [0,1]: q[s]=p[s]
        for s in [M-1,M-2]: q[s]+=a/4
        ep=defaultdict(F); eq=defaultdict(F)
        for s,v in p.items(): ep[s&~2]+=v
        for s,v in q.items(): eq[s&~2]+=v
        score={s:co[s]*co[s|2]/v for s,v in ep.items()}
        V=sum(ep[s]*v*v for s,v in score.items())
        X=sum((eq[s]-v)**2/v for s,v in ep.items())
        d=F(1,1<<r); A=1-3*d
        check(V==(d*d*A*A/(A*A+d*d)+F(7,10)*d-F(9,10)*d*d)/2)
        check(X==a*a*(1/(10*d*d)-1)/2)
        jointp={}; jointq={}; childlog=defaultdict(F); outcomes={}
        for y in [0,1]:
            pp={}; qq={}
            for s in ep:
                k=F(1,2)+(1 if y==0 else -1)*score[s]
                check(0<=k<=1)
                jointp[(y,s)]=ep[s]*k; jointq[(y,s)]=eq[s]*k
            ry=sum(jointq[(y,s)] for s in ep); outcomes[y]=ry
            for s in ep:
                if jointp[(y,s)]: pp[s]=2*jointp[(y,s)]
                if jointq[(y,s)]: qq[s]=jointq[(y,s)]/ry
            check(sum(pp.values())==sum(qq.values())==1)
            for j,v in logs(pp,qq).items(): childlog[j]+=v/2
        ej=logs(ep,eq); jj=logs(jointp,jointq)
        oo=logs({0:F(1,2),1:F(1,2)},outcomes)
        for j in set(ej)|set(jj)|set(oo)|set(childlog):
            check(ej.get(j,0)==jj.get(j,0))
            check(ej.get(j,0)==oo.get(j,0)+childlog.get(j,0))
        cases+=1
    # Pure rational coefficient limits: tight fixed brackets, independent of logs.
    normalized=[]
    for r in [8,16,32,64,128]:
        d=F(1,1<<r); a=F(1,r*r); A=1-3*d
        V=(d*d*A*A/(A*A+d*d)+F(7,10)*d-F(9,10)*d*d)/2
        X=a*a*(1/(10*d*d)-1)/2
        z=X*V*d/(a*a)
        check(F(17,1000)<z<F(18,1000))
        check(F(34,100)<V/d<F(36,100))
        normalized.append({'r':r,'XV_d_over_alpha2':str(z)})
    result={'status':'PASS','checks':N,'direct_Walsh_cases':cases,'runtime_seconds':time.perf_counter()-st,
            'normalized':normalized,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (R/'out/AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','checks','direct_Walsh_cases','runtime_seconds']}))
if __name__=='__main__':run()
