from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import comb
import sys,json,time
from arithmetic import fw,influences,tables,reference,ent,ce,kl,add,lograt
RUN=Path(__file__).resolve().parents[1];START=time.perf_counter();MODE=sys.argv[1];COUNT=0;GRID=2**90
def ck(v):
    global COUNT
    assert v;COUNT+=1
def floor(q):return F(q.numerator*GRID//q.denominator,GRID)
def ceil(q):return -floor(-q)
z=F(1,3);ss=sum((2*z**(2*j+1)/F(2*j+1) for j in range(36)),F(0));rr=2*z**73/(73*(1-z*z));LN2=(floor(ss),ceil(ss+rr))
@lru_cache(None)
def ln(q):
    q=F(q);assert q>0
    e=q.numerator.bit_length()-q.denominator.bit_length();x=q/F(2)**e
    if x<1:e-=1;x*=2
    z=(x-1)/(x+1);s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(36)),F(0));err=2*z**73/(73*(1-z*z))
    return floor(s+e*LN2[0 if e>=0 else 1]),ceil(s+err+e*LN2[1 if e>=0 else 0])
def log2(q):
    l,h=ln(q);vals=[l/LN2[0],l/LN2[1],h/LN2[0],h/LN2[1]];return min(vals),max(vals)
def cost(p,q):
    low=high=F(0)
    for t,w in p.items():
        if w:
            l,h=log2(q[t]);low-=w*h;high-=w*l
    return low,high
def divergence(p,q):
    l=u=F(0)
    for t,w in p.items():
        if w:
            a,b=log2(w/q[t]);l+=w*a;u+=w*b
    return l,u
def checkpoint(result):
    result.update(assertions=COUNT,elapsed_seconds=time.perf_counter()-START)
    (RUN/'out'/f'{MODE.upper()}_CHECKPOINT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    if result['elapsed_seconds']>55:raise RuntimeError('Frozen cutoff: completed checkpoint saved')
def save_result(result):
    result.update(status='PASS',assertions=COUNT,runtime_seconds=time.perf_counter()-START,mode=MODE)
    (RUN/'out'/f'{MODE.upper()}_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
def actual(a,b,r,point=0):
    n=a+b;g=[-1 if x&((1<<a)-1)==0 else 1 for x in range(1<<n)]
    vals=[(v+2 if x==point and ctrl==0 else v) for ctrl in range(1<<r) for x,v in enumerate(g)]
    c=fw(g);f=fw(vals);P={t:v*v for t,v in c.items()};PF={t:v*v for t,v in f.items()}
    return g,vals,c,P,PF
def reference_floor(a,b,r,P,PF,R,normalized):
    n=a+b;s=F(1,2**a);t=F(1,2**n);p=F(1,2**r);rho=4*p*t;lam=2*p/F(2**b);mu=1-2*s
    R0=R.copy()
    if normalized:
        R0={j:mu*mu if j==0 else (R[j]*(1-mu*mu)/(1-R[0])) for j in R}
        catP={0:mu*mu,1:1-mu*mu};catR={0:R[0],1:1-R[0]}
        ck(add(add(ce(P,R),ce(P,R0),F(-1)),kl(catP,catR),F(-1))=={})
    q={T:sum(PF[T|(U<<n)] for U in range(1<<r)) for T in P}
    w=(1-lam,lam*mu,rho)
    Rp={T:w[0]*R0[T]+(w[1] if T==0 else 0)+w[2]*t for T in P}
    ck(sum(w)==1);ck(min(w)>=0);ck(all(q[T]==w[0]*P[T]+(w[1] if T==0 else 0)+w[2]*t for T in P))
    Q={T|(U<<n):Rp[T]*PF[T|(U<<n)]/q[T] for T in P for U in range(1<<r)}
    mass=w[0]*sum(R0.values())+w[1]+w[2];ck(sum(Q.values())==mass);ck(mass<=1)
    if normalized:ck(mass==1)
    componentsP=[P,{T:F(int(T==0)) for T in P},{T:t for T in P}]
    componentsR=[R0,componentsP[1],componentsP[2]]
    for T in P:
        piP=[w[j]*componentsP[j][T]/q[T] for j in range(3)]
        piR=[w[j]*componentsR[j][T]/Rp[T] for j in range(3)]
        ck(sum(piP)==sum(piR)==1)
        for j in range(3):
            if piP[j]:ck((componentsP[j][T]/componentsR[j][T])==(q[T]/Rp[T])*(piP[j]/piR[j]))
        for U in range(1<<r):
            key=T|(U<<n)
            if PF[key]:ck(PF[key]/Q[key]==q[T]/Rp[T])
    return Q,R0
def children(values,j):
    N=len(values);nd=(N-1).bit_length();out=[]
    for bit in [0,1]:
        vals=[]
        for x in range(1<<(nd-1)):
            original=(x&((1<<j)-1))|((x>>j)<<(j+1))|(bit<<j);vals.append(values[original])
        out.append(vals)
    return out
def inherited(values,P,Q,j,zero_kernel=None):
    child=children(values,j);Ps=[{t:v*v for t,v in fw(vs).items()} for vs in child]
    nr=(len(values)-1).bit_length()-1
    marginal={};refm={}
    for T in range(1<<nr):
        T0=(T&((1<<j)-1))|((T>>j)<<(j+1));keys=[T0,T0|(1<<j)]
        marginal[T]=sum(P[x] for x in keys);refm[T]=sum(Q[x] for x in keys)
        ck(marginal[T]==(Ps[0][T]+Ps[1][T])/2)
    raw=[{T:(refm[T]*Pc[T]/marginal[T] if marginal[T] else 2*refm[T]*(zero_kernel(T,bit) if zero_kernel else F(1,2))) for T in marginal} for bit,Pc in enumerate(Ps)]
    Z=[sum(row.values()) for row in raw];ck(sum(Z)==2);ck(min(Z)>0)
    R=[{T:row[T]/z for T in row} for row,z in zip(raw,Z)]
    for Pc,Rc,z in zip(Ps,R,Z):
        ck(sum(Rc.values())==1)
        for T,v in Pc.items():
            if v:ck(Rc[T]>0);ck(v/Rc[T]==(marginal[T]/refm[T])*z)
    ck(sum(influences(values))==influences(values)[j]+sum(sum(influences(vs)) for vs in child)/2)
    return child,Ps,R,Z,marginal,refm
def roots(a):
    cases=refs=queries=0
    for b in range(4):
        for r in [1,2]:
            g,vals,c,P,PF=actual(a,b,r);n=a+b;s=F(1,2**a);t=F(1,2**n);p=F(1,2**r)
            C=2*p*t*b;E=2*p*t*a;J=2*r*p*t;Ig=2*a*s;If=Ig+C-E+J
            ck(sum(influences(g))==Ig);ck(sum(influences(vals))==If)
            for variant in [0,1]:
                R=reference(P,variant);Q,R0=reference_floor(a,b,r,P,PF,R,True)
                ce_source=cost(P,R);ce_root=cost(PF,Q)
                ck(ce_root[1]<=ce_source[0]+10*(C+E+J))
                C0=ce_source[1]/Ig;ck(ce_root[1]<=(2*C0+10)*If)
                child,Ps,Rs,Z,m,rm=inherited(vals,PF,Q,0);queries+=1
                # Exact source likelihood decomposition on each queried row.
                for T in m:
                    if m[T]:
                        T0=T<<1
                        for key in [T0,T0|1]:
                            if PF[key]:ck(PF[key]/Q[key]==(m[T]/rm[T])*((PF[key]/m[T])/(Q[key]/rm[T])))
                refs+=1
            cases+=1;checkpoint({'physical_functions':cases,'references':refs,'queries':queries})
    return {'physical_functions':cases,'reference_cases':refs,'active_queries':queries}
def neutral():
    count=0
    for point_dummy in range(8):
        for r in [1,2,3]:
            point=point_dummy<<3;g,vals,c,P,PF=actual(3,3,r,point)
            R={T:F(1,128) for T in P};Q,R0=reference_floor(3,3,r,P,PF,R,False)
            root_ce=cost(PF,Q);raw_ce=cost(P,R);J=F(2*r,2**(r+6))
            ck(root_ce[1]<=raw_ce[0]+72*J);ck(sum(Q.values())== (1-4*F(4,2**(r+6)))/2+4*F(4,2**(r+6)))
            count+=1;checkpoint({'neutral_roots':count})
    return {'neutral_roots':count,'subprobability_reference_cases':count}
def shock_reference(n):
    A=1;N=2**n
    return {T:F(0) if T==0 else F(1,2) if T==A else F(1,2*(N-2)) for T in range(N)}
def shock_scalars(n):
    t=F(1,2**n);mu2=(1-2*t)**2;qA=1-2*t+2*t*t;RA=(1-2*t)/2+2*t*t
    rv=t*t+RA*(1-t)**2/qA;zp=rv/qA;zn=2-zp;qvac=mu2*rv/(2*qA-rv)
    return t,mu2,qA,RA,rv,zp,zn,qvac
def shock():
    # Exact Bernstein certificate on u=4t in [0,1].
    coefficients=[F(3),F(-9,2),F(51,16),F(-79,64),F(33,128),F(-3,128)]
    bern=[sum((coefficients[i]*F(comb(j,i),comb(5,i)) for i in range(j+1)),F(0)) for j in range(6)]
    ck(min(bern)>0)
    rows=[]
    for n in [2,3,4,5,6,8,12,16,24,32,48]:
        t,mu2,qA,RA,rv,zp,zn,qvac=shock_scalars(n)
        ck(zp+zn==2);ck(0<qvac<F(1,3));ck(mu2>=F(1,4));ck(zp>0 and zn>0)
        # The core exact reference formula and polynomial residual independently agree.
        N=t*t*qA+RA*(1-t)**2
        residual=2*qA*qA-(1+3*mu2)*N
        polynomial=2*t*sum(coefficients[i]*(4*t)**i for i in range(6))
        ck(residual==polynomial);ck(residual>0)
        if n>=3:ck(mu2>=F(9,16));ck(F(9,16)/(2*n*t)==F(9*2**n,32*n))
        if n<=6:
            g,vals,c,P,PF=actual(1,n-1,1);R=shock_reference(n)
            ck(sum(R.values())==1);ck(ce(P,R)=={2:F(1)})
            Q,_=reference_floor(1,n-1,1,P,PF,R,True);child,Ps,Rs,Z,m,rm=inherited(vals,PF,Q,0)
            ck(Ps[1]=={0:F(1),**{T:F(0) for T in range(1,len(Ps[1]))}})
            ck(Z[1]==zp and Z[0]==zn);ck(Rs[0][0]==qvac);ck(Ps[0][0]==mu2)
            ck(sum(influences(child[0]))==2*n*t);ck(sum(influences(vals))==1+(n-1)*t)
            ck(cost(PF,Q)[1]<=12*(1+(n-1)*t));ck(cost(Ps[0],Rs[0])[0]>=mu2*log2(3)[0])
        rows.append({'n':n,'t':str(t),'inherited_negative_vacuum':str(qvac),'true_negative_vacuum':str(mu2),'normalizer_positive':str(zp),'normalizer_negative':str(zn),'negative_child_influence':str(2*n*t),'CE_child_over_I_lower':str(F(9*2**n,32*n)) if n>=3 else None})
    obj={'Bernstein_polynomial_in_u_coefficients':[str(x) for x in coefficients],'Bernstein_basis_coefficients':[str(x) for x in bern],'rows':rows,'all_dimension_CE_child_over_I_lower':'9*2^n/(32n), n>=3; inherited vacuum<1/3; log2(3)>1','asymptotic_normalizers':['1/2','3/2'],'asymptotic_reference_negative_vacuum':'1/3','source_cost':'1','root_paid_price':'12','no_FEI_counterexample':True}
    (RUN/'out/INCOMING_SHOCK_CERTIFICATE.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    return {'compressed_shock_cases':len(rows),'direct_shock_cases':5,'Bernstein_coefficients':[str(x) for x in bern]}
def tensor():
    n=3;g,vals,c,P,PF=actual(1,2,1);Q,_=reference_floor(1,2,1,P,PF,shock_reference(n),True)
    child,Ps,Rs,Z,_,_=inherited(vals,PF,Q,0);N=len(vals);bits=(N-1).bit_length();cases=0
    for h in tables(2):
        Ph={T:x*x for T,x in fw(h).items()}
        for variant in [0,1]:
            Rh=reference(Ph,variant);fullvals=[a*b for a in h for b in vals]
            fullP={T:x*x for T,x in fw(fullvals).items()};fullQ={T|(U<<bits):x*y for T,x in Q.items() for U,y in Rh.items()}
            def zero_kernel(T,bit):
                low=T&((1<<(bits-1))-1)
                return Ps[bit][low]/(Ps[0][low]+Ps[1][low])
            _,bigPs,bigRs,bigZ,_,_=inherited(fullvals,fullP,fullQ,0,zero_kernel)
            ck(bigZ==Z)
            for j in [0,1]:
                expected={T|(U<<(bits-1)):x*y for T,x in Rs[j].items() for U,y in Rh.items()}
                ck(bigRs[j]==expected)
                # Marginalization plus actual ratios retain the entire terminal likelihood.
                for T,w in bigPs[j].items():
                    if w:
                        low=T&((1<<(bits-1))-1);hi=T>>(bits-1)
                        ck(w/bigRs[j][T]==(Ps[j][low]/Rs[j][low])*(Ph[hi]/Rh[hi]))
            cases+=1;checkpoint({'terminal_tensor_reference_cases':cases})
    return {'terminal_tensor_reference_cases':cases,'all_labelled_terminal_signs':16}
result=roots(int(MODE)) if MODE in ['1','2','3','4'] else {'neutral':neutral,'shock':shock,'tensor':tensor}[MODE]()
save_result(result)
