from fractions import Fraction as Q
from pathlib import Path
import itertools,json,time
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();cases=drifts=0
for s,L,R,T,Ig in itertools.product(range(1,9),range(1,4),range(1,4),range(1,4),(Q(1),Q(5,2),Q(10))):
    q,r=Q(1,2**R),Q(1,2**T);eta=Q(1,2**(L+R+T));e=q+r-q*r-eta
    JB=(L+R+T)*eta;JC=R*q*(1-r)+T*r*(1-q);JD=JB+JC
    m=(min(R,T)+1).bit_length()+2
    def V(j):
        M=min(j,m)
        return Q(1,2**j)*(M*JD+e*M*(M-1)/2+M*e*Ig)
    spent=Q(0)
    for j in range(1,s+1):
        c=Q(1,2**j)*(JD+(j-1)*e+e*Ig)
        drift=V(j)-V(j-1)/2
        assert drift==(c if j<=m else 0);drifts+=1
        if j<=m:spent+=Q(1,2**(s-j))*c
    a=Q(1,2**s);pi=eta+a*e;Is=s*a*e;Io=(1-a)*JB+a*JC;It=pi*Ig
    M=min(s,m)
    assert spent==V(s)
    assert V(s)<=M*Io+Q(M-1,2)*Is+M*It<=M*(Is+Io+It)
    assert e>=max(q,r)
    cases+=1
out={'status':'PASS','rational_account_cases':cases,'exact_drift_checks':drifts,'recorded_assertions':drifts+3*cases,'runtime_seconds':time.perf_counter()-start,'no_entropy_approximation':True}
(ROOT/'out'/'RESERVE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
