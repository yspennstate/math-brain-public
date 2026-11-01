"""Independent finite certificate; no producer checker is imported."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter();COUNT=0
def ck(v):
    global COUNT
    COUNT+=1
    assert v,COUNT
    if time.perf_counter()-START>55:raise TimeoutError('55 second cap')
def dump(n,v):(RUN/'out'/n).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def ln_interval(q):
    z=(q-1)/(q+1);w=z;v=F(0)
    for k in range(32):v+=2*w/F(2*k+1);w*=z*z
    # Called only with 1<=q<=2, so z is nonnegative.
    return v,v+2*w/(65*(1-z*z))
LN2=ln_interval(F(2))
@lru_cache(None)
def lg(q):
    q=F(q);assert q>0
    k=q.numerator.bit_length()-q.denominator.bit_length();z=q/F(2)**k
    if z<1:k-=1;z*=2
    assert 1<=z<2
    l,h=ln_interval(z);D=1<<90
    return F((D*(k+l/LN2[1])).__floor__(),D),F((D*(k+h/LN2[0])).__ceil__(),D)
def add(*xs):return sum((x[0] for x in xs),F(0)),sum((x[1] for x in xs),F(0))
def mul(c,x):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def sub(x,y):return add(x,mul(-1,y))
def ce(P,Q):
    ans=(F(0),F(0))
    for p,q in zip(P,Q):
        if p:ck(q>0);ans=add(ans,mul(-p,lg(q)))
    return ans
def wht(vals):
    z=list(vals);h=1
    while h<len(z):
        for i in range(0,len(z),2*h):
            for j in range(i,i+h):x,y=z[j],z[j+h];z[j],z[j+h]=x+y,x-y
        h*=2
    return [F(x,len(z)) for x in z]
def spectrum(vals):return [x*x for x in wht(vals)]
def influences(vals):
    return [F(sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals))),len(vals)) for j in range((len(vals)-1).bit_length())]
def marginal(P):return [P[2*x]+P[2*x+1] for x in range(len(P)//2)]
def actual(a,b,r):return [1-2*int(x&((1<<a)-1)==0)+2*int(x==0) for x in range(1<<(a+b+r))]
def source(a,b):return [1-2*int(x&((1<<a)-1)==0) for x in range(1<<(a+b))]
def floor(a,b,r,R):
    vals=actual(a,b,r);P=spectrum(vals);N=len(R);L=1<<r
    s,t,e=F(1,1<<a),F(1,1<<(a+b)),F(2,len(vals));mu=1-2*s
    M=[sum(P[T+U*N] for U in range(L)) for T in range(N)]
    A=[(1-e/s)*v+(e/s)*mu*int(T==0)+2*e*t for T,v in enumerate(R)]
    ck(sum(A)==sum(M)==1);ck(A[0]==M[0]);ck(min(M)>0)
    Q=[A[x%N]*p/M[x%N] for x,p in enumerate(P)]
    ck(sum(Q)==sum(P)==1);ck(min(Q)>0)
    return vals,P,Q
def make_reference(a,b,r):
    Pg=spectrum(source(a,b));e=F(2,1<<(a+b+r));v=1-Pg[0]
    R=[Pg[0]]+[e**3*p for p in Pg[1:]]
    R[1]+=v*(1-e-e**3);R[1<<a]+=v*e
    ck(sum(R)==1);ck(all(q>=0 for q in R));ck(all(q>0 for p,q in zip(Pg,R) if p))
    return R
def check_case(r,full):
    a,b=4,1;R=make_reference(a,b,r)
    vals,P,Q=floor(a,b,r,R);V=marginal(R);old=marginal(Q)
    cv=vals[::2];constant=vals[1::2]
    ck(constant==[1]*len(cv));ck(cv==actual(a-1,b,r))
    Pgchild=spectrum(source(a-1,b));beta=(1-Pgchild[0])/(1-V[0])
    Rc=[Pgchild[0]]+[beta*x for x in V[1:]]
    ck(beta>0);ck(sum(Rc)==1)
    cv2,Pc,new=floor(a-1,b,r,Rc);ck(cv2==cv)
    # Independent direct character sums on the entire small witness.
    if full:
        z=wht(vals)
        for T,u in enumerate(z):ck(u==F(sum(v*(-1 if (x&T).bit_count()%2 else 1) for x,v in enumerate(vals)),len(vals)))
    else:
        # Large witness: all coefficients also match the literal analytic pattern.
        z=wht(vals);s=F(1,16);e=F(2,len(vals))
        for T,u in enumerate(z):
            ghat=1-2*s if T==0 else (-2*s if T<16 else F(0))
            ck(u==ghat+e)
    I=influences(vals);Ic=influences(cv)
    ck(sum(I)==sum(T.bit_count()*p for T,p in enumerate(P)))
    ck(I[0]+sum(Ic)/2==sum(I))
    ck(I[0]==F(1,8)-F(2,len(vals)))
    oldCE=ce(Pc,old);newCE=ce(Pc,new);Z=mul(F(1,2),sub(newCE,oldCE))
    ck(Z[0]>0)
    # Reconstruct the likelihood sum directly, not by subtracting CEs.
    direct=add(*(mul(p/2,lg(qo/qn)) for p,qo,qn in zip(Pc,old,new) if p))
    ck(max(Z[0],direct[0])<=min(Z[1],direct[1]))
    # Independently aggregated exact profile, compared atom for atom.
    s,t,e=F(1,16),F(1,32),F(2,len(vals));L=1<<r;k=1-e/s;mu=1-2*s
    qj=(2*s-e)**2+(L-1)*e*e;rp=k*R[1]+2*e*t
    p0=(1-4*s+2*e)**2;p1=4*e*e
    ag=[(p0,((mu+e)**2+rp*(2*s-e)**2/qj)/p0),(F(L-1)*p1,(e*e+rp*e*e/qj)/p1)]
    for T in range(1,16):
        oq=k*V[T]+4*e*t;nq=k*beta*V[T]+8*e*t
        mass=4*qj if T<8 else 8*e*t
        ag.append((mass,oq/nq))
        for U in range(L):ck(old[T+16*U]/new[T+16*U]==oq/nq)
    for U in range(L):ck(Pc[16*U]==(p0 if U==0 else p1))
    ck(sum(p for p,q in ag)==1)
    agg=add(*(mul(p/2,lg(q)) for p,q in ag));ck(max(agg[0],Z[0])<=min(agg[1],Z[1]))
    # Keep the complementary full inherited CE, conditional refund, and old debit.
    rootCE=ce(P,Q);pm=marginal(P);margCE=ce(pm,old)
    B=sub(ce(P,P),ce(pm,pm));kconst=mul(-1,lg(old[0]))
    refund=sub(rootCE,add(B,mul(F(1,2),oldCE),mul(F(1,2),kconst)))
    newbill=add(B,mul(F(1,2),newCE),mul(F(1,2),kconst))
    ck(refund[0]>=0)
    # Source-priced original root bank, with a declared conservative C0.
    Pg=spectrum(source(a,b));sourceCE=ce(Pg,R);Ig=sum(influences(source(a,b)))
    C0=14 if r==3 else 32;K=2*C0+10;quota=K*sum(I)
    ck(sourceCE[1]<=C0*Ig)
    W=add(sourceCE,(10*e*(a+b+r),)*2)
    ck(rootCE[1]<=W[0]);ck(newbill[1]<=W[0]);ck(W[1]<=quota)
    # A genuine prior AND2 tensor query books one erasure bit and leaves one
    # complete inherited tensor bit. Its original two bits are reserved once.
    A=[-1,1,1,1];PA=spectrum(A);VA=marginal(PA)
    ck(PA==[F(1,4)]*4);ck(VA==[F(1,2)]*2)
    ba=sub(ce(PA,PA),ce(VA,VA));ck(ba[0]<=1<=ba[1])
    ca0=ce(spectrum(A[::2]),VA);ca1=ce(spectrum(A[1::2]),VA)
    ck(ca0[0]<=1<=ca0[1]);ck(ca1[0]<=1<=ca1[1])
    if full:
        tensor=[v*w for w in A for v in vals];PT=spectrum(tensor)
        for T,pv in enumerate(PT):ck(pv==P[T%len(P)]*PA[T//len(P)])
    # The tensor's two-bit full cost is carried outside the core quota.
    d=F(1);U=sub((quota+2-d,)*2,add(rootCE,(F(1),)*2))
    remain=sub((quota+2-d,)*2,add(newbill,(F(1),)*2))
    identity=sub(add(U,refund),Z)
    ck(max(remain[0],identity[0])<=min(remain[1],identity[1]));ck(remain[0]>0)
    if r==3:ck(Z[0]>F(5,1000));ck(Z[1]<F(53,10000))
    if r==8:ck(Z[0]>F(14,1000));ck(Z[1]<F(15,1000))
    out={'a':a,'b':b,'r':r,'dimension':a+b+r,'R':[str(x) for x in R],'reset_interval':[str(x) for x in Z],'direct_interval':[str(x) for x in direct],'source_CE_interval':[str(x) for x in sourceCE],'source_C0':C0,'K':K,'query_influence':str(I[0]),'root_CE_interval':[str(x) for x in rootCE],'new_whole_bill_interval':[str(x) for x in newbill],'refund_interval':[str(x) for x in refund],'complementary_CE_interval':[str(x) for x in kconst],'remaining_with_actual_AND2_debit_interval':[str(x) for x in remain]}
    dump('EXACT_r'+str(r)+'.json',out);return out
def main():
    amendment={'helper':'A003-independent-reset-certificate-v1','domain':'fixed r=3 and r=8; a4,b1, query0; one supplied reference each','case_count':2,'prior_history':'independent AND2 tensor query; erasure debit1 and full inherited tensor CE1 retained from initial CE2','symmetry':'none','arithmetic':'integer Walsh/direct character sums; Fraction laws; 32-term rational log intervals','memory_estimate_mb':120,'max_runtime_seconds':55,'independence':'producer code not imported; literal truth tables and independent aggregated profile agree'}
    (RUN/'FROZEN_CERTIFICATE.json').write_text(json.dumps(amendment,indent=2)+'\n',encoding='utf-8')
    rows=[check_case(3,True),check_case(8,False)]
    # Positive asymptotic limiting expression: integer comparison is exact.
    ck(3**18<2**29)
    lim=mul(F(1,32),sub((F(29),)*2,mul(18,lg(F(3)))))
    ck(lim[0]>F(14,1000));ck(lim[1]<F(15,1000))
    result={'status':'EXACT_CERTIFICATE_PASS','cases':2,'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'rows':rows,'limit_interval':[str(x) for x in lim],'rung':'exact finite certificate; analytic limit requires the separate written argument'}
    dump('VALIDATION.json',result);print(json.dumps({k:v for k,v in result.items() if k not in ['rows','limit_interval']}))
if __name__=='__main__':main()
