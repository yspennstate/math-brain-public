from pathlib import Path
from fractions import Fraction as F
import json,time
import verify as C
RUN=Path(__file__).resolve().parents[1]
rows=[];START=time.perf_counter()
for m in [4,5,6,8,16,32]:
    s=F(1,1<<m);e=s*s;t=s/2;L=1<<m;k=1-s;mu=1-2*s;v=4*s*(1-s)
    Rj=v*(1-e-e**3)+4*s*s*e**3
    V0=mu*mu+Rj;beta=(8*s-16*s*s)/(1-V0)
    C.ck(beta==2*(1-2*s)/(s*s*(1-s+s**4*(1-2*s))))
    C.ck(Rj>=s);C.ck(1-e-e**3>F(3,4));C.ck(v>=F(15,4)*s)
    qj=s*s*(4-3*s);u=k*Rj+s**3
    p0=(1-4*s+2*e)**2;o0=(mu+e)**2+u*(2*s-e)**2/qj
    active_count=(1<<(m-1))-1;dummy_count=1<<(m-1)
    aa=(k*8*s**8+2*s**3)/(k*beta*8*s**8+4*s**3)
    dd=(k*v*e+2*s**3)/(k*beta*v*e+4*s**3)
    groups=[(p0,o0/p0),((L-1)*4*e*e,(1+u/qj)/4),(active_count*4*qj,aa),(4*s**3,dd),((dummy_count-1)*4*s**3,F(1,2))]
    C.ck(sum(p for p,q in groups)==1);C.ck(all(q>0 for p,q in groups))
    Z=C.add(*(C.mul(p/2,C.lg(q)) for p,q in groups));C.ck(Z[0]>0)
    # Exact source CE; the source-zero dummy mass contributes no entropy term.
    sourceCE=C.add(C.mul(-mu*mu,C.lg(mu*mu)),C.mul(-4*s*s,C.lg(Rj)),C.mul(-((1<<m)-2)*4*s*s,C.lg(4*s**8)))
    Ig=2*m*s
    C.ck(sourceCE[1]<=17*Ig)
    # Written proof upper bound, valid uniformly in m>=4.
    bound=6*s+4*s*s*m+4*s*(8*m-2)
    C.ck(sourceCE[1]<=bound);C.ck(bound<=34*m*s)
    if m in [4,6]:
        R=C.make_reference(m,1,m);vals,P,Q=C.floor(m,1,m,R)
        V=C.marginal(R);old=C.marginal(Q);Pg=C.spectrum(C.source(m-1,1))
        Rc=[Pg[0]]+[(1-Pg[0])*x/(1-V[0]) for x in V[1:]]
        cv,Pc,new=C.floor(m-1,1,m,Rc)
        C.ck(cv==vals[::2]);C.ck(vals[1::2]==[1]*len(cv))
        direct=C.add(*(C.mul(p/2,C.lg(qo/qn)) for p,qo,qn in zip(Pc,old,new) if p))
        C.ck(max(Z[0],direct[0])<=min(Z[1],direct[1]))
        for T,a in enumerate(C.wht(vals)):
            gh=mu if T==0 else (-2*s if T<(1<<m) else F(0))
            C.ck(a==gh+e)
        C.ck(C.influences(vals)[0]==2*s-e)
        # Complete floor and both terminals remain in the SAME source envelope.
        B=C.sub(C.ce(P,P),C.ce(C.marginal(P),C.marginal(P)))
        newbill=C.add(B,C.mul(F(1,2),C.ce(Pc,new)),C.mul(F(-1,2),C.lg(old[0])))
        W=C.add(sourceCE,(10*e*(2*m+1),)*2)
        C.ck(newbill[1]<=W[0]);C.ck(C.ce(P,Q)[1]<=W[0]);C.ck(W[1]<=44*sum(C.influences(vals)))
    row={'m':m,'dimension':2*m+1,'source_CE_interval':[str(x) for x in sourceCE],'source_C0':17,'reset_interval':[str(x) for x in Z],'reset_over_edit_interval':[str(x/e) for x in Z],'reset_over_query_influence_interval':[str(x/(2*s-e)) for x in Z],'literal_reconstruction':m in [4,6]}
    rows.append(row);C.dump('UNIFORM_SOURCE_CHECKPOINT.json',rows)
    if time.perf_counter()-START>55:raise TimeoutError('55 second cap')
result={'status':'EXACT_PASS','cases':6,'literal_dimensions':[9,13],'assertions':C.COUNT,'runtime_seconds':time.perf_counter()-START,'rows':rows}
C.dump('UNIFORM_SOURCE_VALIDATION.json',result)
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
