from fractions import Fraction as Q
from pathlib import Path
import itertools,json,time
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();cases=drifts=0
for s,L,R,T,Ig in itertools.product(range(1,9),range(1,4),range(1,9),range(1,9),(Q(1),Q(5,2))):
    q,r=Q(1,2**R),Q(1,2**T);eta=Q(1,2**(L+R+T));e=q+r-q*r-eta
    JB=(L+R+T)*eta;JC=R*q*(1-r)+T*r*(1-q);JD=JB+JC
    m=0 if min(R,T)>=4 else (min(R,T)+1).bit_length()+2
    assert m<=5
    def V(j):
        M=min(j,m);return Q(1,2**j)*(M*JD+e*M*(M-1)/2+M*e*Ig)
    for j in range(1,s+1):
        c=Q(1,2**j)*(JD+(j-1)*e+e*Ig)
        assert V(j)-V(j-1)/2==(c if j<=m else 0);drifts+=1
    a=Q(1,2**s);pi=eta+a*e;Is=s*a*e;Io=(1-a)*JB+a*JC;It=pi*Ig
    M=min(s,m)
    assert V(s)<=M*Io+Q(max(M-1,0),2)*Is+M*It<=5*(Is+Io+It)
    if m==0:assert e<=Q(1,8) and V(s)==0
    cases+=1
out={'status':'PASS','rational_account_cases':cases,'exact_layer_drifts':drifts,'recorded_assertions':drifts+cases,'runtime_seconds':time.perf_counter()-start,'reserve_max_layers':5,'rare_regime_reserve_layers':0}
(ROOT/'out'/'ACCOUNT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
