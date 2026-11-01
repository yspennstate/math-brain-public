"""Exact self-checks for X015's analytic three-site theorem.

The universal matrix inequality is proved in agents/X015.md; finite checks here
corroborate the identities and explicit example, and are not its proof.
"""
from pathlib import Path
import json
import sympy as sp
import numpy as np

OUT=Path(__file__).with_name('reproduce.json')
R=sp.Rational
I=sp.I

def adj(A):
    return A.adjugate()

def atoms(K,A=None):
    n=K.rows
    t=sp.symbols('t',real=True)
    ps=[];ds=[];dds=[]
    for mask in range(1<<n):
        Q=K-sp.diag(*[1-(mask>>i&1) for i in range(n)])
        sign=(-1)**(n-mask.bit_count())
        if A is None:
            ps.append(sp.factor(sign*Q.det()))
        else:
            pol=sp.Poly(sp.expand(sign*(Q+t*A).det()),t)
            ps.append(sp.factor(pol.nth(0)))
            ds.append(sp.factor(pol.nth(1)))
            dds.append(sp.factor(2*pol.nth(2)))
    if A is None:return ps
    return ps,ds,dds

def logvec(q):
    q=sp.Rational(q)
    d={}
    for p,e in sp.factorint(q.p).items():d[int(p)]=int(e)
    for p,e in sp.factorint(q.q).items():d[int(p)]=d.get(int(p),0)-int(e)
    return {p:e for p,e in d.items() if e}

def sumlogs(weights,qs):
    d={}
    for a,q in zip(weights,qs):
        for p,e in logvec(q).items():d[p]=d.get(p,0)+a*e
    return {p:sp.factor(v) for p,v in d.items() if sp.factor(v)!=0}

def as_float(M):
    return np.array(M.evalf(30),dtype=complex)

def report_case(K,A):
    p,dp,ddp=atoms(K,A)
    assert min(p)>0 and sum(p)==1 and sum(dp)==sum(ddp)==0
    fisher=sp.factor(sum(x*x/y for x,y in zip(dp,p)))
    D=sp.factor(sum(A[k,k]**2/(K[k,k]*(1-K[k,k])) for k in range(3)))
    cr=[sp.factor(p[2]*p[4]/(p[0]*p[6])),sp.factor(p[1]*p[4]/(p[0]*p[5])),sp.factor(p[1]*p[2]/(p[0]*p[3]))]
    tr=sp.factor(p[6]*p[5]*p[3]*p[0]/(p[7]*p[4]*p[2]*p[1]))
    c=sp.diag(*[sp.log(x) for x in cr]);tau=sp.log(tr);M=c+tau*K
    adjA=adj(A)
    exact_log_left=sumlogs([-x for x in ddp],p)
    weights=[2*adjA[k,k] for k in range(3)]+[2*sp.trace(K*adjA)]
    exact_log_right=sumlogs(weights,cr+[tr])
    assert exact_log_left==exact_log_right
    N=sp.zeros(3);branch=[];total_conditional_fisher=0;quad_alg=0
    for k in range(3):
        a=K[k,k];b=1-a;d=A[k,k]
        rr=[j for j in range(3) if j!=k]
        v=K.extract(rr,[k]);w=A.extract(rr,[k]);B=A.extract(rr,rr)
        subFI=0
        for s in [0,1]:
            mass=a if s else b
            r=a if s else -b
            J=K.extract(rr,rr)-v*v.conjugate().T/r
            E=B-(w*v.conjugate().T+v*w.conjugate().T)/r+d*v*v.conjugate().T/r**2
            cp,cdp,_=atoms(J,E)
            cf=sp.factor(sum(x*x/y for x,y in zip(cdp,cp)))
            omega=sp.factor(2+(cp[1]+cp[2])/sp.sqrt(cp[0]*cp[3]))
            col=K[:,k] if s else (sp.eye(3)-K)[:,k]
            nb=omega/mass*(col*col.conjugate().T)
            ident=sp.factor((col.conjugate().T*adjA*col)[0]-mass**2*E.det())
            assert ident==0
            # Match conditional law and first derivative directly to joint atoms.
            mdot=d if s else -d
            for loc in range(4):
                mask=(s<<k)+sum(((loc>>j)&1)<<rr[j] for j in range(2))
                assert cp[loc]==p[mask]/mass
                assert cdp[loc]==sp.factor((dp[mask]*mass-p[mask]*mdot)/mass**2)
            N+=nb;subFI+=mass*cf;quad_alg+=mass*omega*E.det()
            residual=sp.factor(cf-2*omega*E.det())
            assert float(sp.N(residual,30))>=-1e-20
            branch.append({'pivot':k,'branch':s,'omega':str(omega),'fisher':str(cf),'det_velocity':str(sp.factor(E.det())),'fisher_margin_display':float(sp.N(residual,20))})
        assert sp.factor(fisher-d*d/(a*b)-subFI)==0
        total_conditional_fisher+=subFI
    assert sp.factor(total_conditional_fisher-(3*fisher-D))==0
    assert sp.simplify(sp.trace(N*adjA)-quad_alg)==0
    sigma=9-7*sp.log(R(7,2))
    nf=as_float(N);mf=as_float(M)
    eigen_comparison=np.linalg.eigvalsh(nf-3.5*mf-float(sigma)*np.eye(3)).tolist()
    H2=-fisher-sum(ddp[j]*sp.log(p[j]) for j in range(8))
    bound=-fisher/7-2*D/7-4*sigma*sp.trace(adjA)/7
    log_ratio=sp.factor(tr)
    return {
      'K':str(K),'A':str(A),'atoms_mask_order':[str(x) for x in p],
      'pair_log_ratios':[str(x) for x in cr],'triple_log_ratio':str(log_ratio),'tau_display':float(sp.N(tau,20)),
      'K_leading_minors':[str(sp.factor(K[:j,:j].det())) for j in range(1,4)],
      'IminusK_leading_minors':[str(sp.factor((sp.eye(3)-K)[:j,:j].det())) for j in range(1,4)],
      'A_leading_minors':[str(sp.factor(A[:j,:j].det())) for j in range(1,4)],
      'commutator':str(K*A-A*K),'fisher':str(fisher),'D':str(D),'fisher_at_least_D':bool(fisher>=D),
      'ambient_log_coefficient_identity_exact':True,'conditional_probability_and_score_identities_exact':True,
      'conditional_adjugate_identities_exact':True,'score_chain_exact':True,
      'branches':branch,'matrix_comparison_eigenvalues_display':eigen_comparison,
      'H_second_display':float(sp.N(H2,20)),'strong_upper_bound_display':float(sp.N(bound,20)),
      'upper_bound_slack_display':float(sp.N(bound-H2,20))}

# Generic complex determinant identity, independent of any chosen kernel.
d,b,c,ur,ui,vr,vi,wr,wi,zr,zi,er,ei,r=sp.symbols('d b c ur ui vr vi wr wi zr zi er ei r',real=True,nonzero=True)
u=ur+I*ui;v=vr+I*vi;w=wr+I*wi;z=zr+I*zi;e=er+I*ei
AA=sp.Matrix([[d,sp.conjugate(w),sp.conjugate(z)],[w,b,e],[z,sp.conjugate(e),c]])
vcol=sp.Matrix([u,v]);wcol=sp.Matrix([w,z]);BB=AA[1:,1:]
EE=BB-(wcol*vcol.conjugate().T+vcol*wcol.conjugate().T)/r+d*vcol*vcol.conjugate().T/r**2
col=sp.Matrix([r,u,v])
assert sp.expand(r**2*EE.det()-(col.conjugate().T*adj(AA)*col)[0])==0
U,V=sp.symbols('U V',positive=True)
assert sp.expand((2+2*U**2)*(2+2*V**2)-(2+2*U*V)**2-4*(U-V)**2)==0
exp_lower=sum(R(9,7)**k/sp.factorial(k) for k in range(5))
assert exp_lower==R(68771,19208) and exp_lower>R(7,2)
K=sp.Matrix([[R(1,5),R(1,10),R(1,20)],[R(1,10),R(3,5),R(1,10)],[R(1,20),R(1,10),R(4,5)]])
A=sp.Matrix([[1,R(1,5),-R(1,10)],[R(1,5),2,R(1,20)],[-R(1,10),R(1,20),1]])
real=report_case(K,A)
Kc=sp.Matrix([[R(1,4),(1+I)/20,(1-2*I)/30],[(1-I)/20,R(1,2),(2+I)/25],[(1+2*I)/30,(2-I)/25,R(3,4)]])
Ac=sp.Matrix([[1,(1+2*I)/10,(1-I)/10],[(1-2*I)/10,2,(2-3*I)/20],[(1+I)/10,(2+3*I)/20,3]])
complex_case=report_case(Kc,Ac)
out={'generic_complex_conditional_determinant_exact':True,'scalar_logconvex_identity_exact':True,
     'exponential_lower_bound':str(exp_lower),'sigma_display':float(9-7*sp.log(R(7,2))),
     'rational_example':real,'rational_complex_example':complex_case,
     'scope':'Universal theorem proved analytically in X015.md; numerical eigenvalues are displays only.'}
OUT.write_text(json.dumps(out,indent=2))
print(json.dumps({'status':'PASS','generic_complex_identity':True,'exact_cases':2,
                  'real_tau_ratio':real['triple_log_ratio'],
                  'real_hessian':real['H_second_display'],'real_bound':real['strong_upper_bound_display'],
                  'real_comparison_min_eigenvalue_display':real['matrix_comparison_eigenvalues_display'][0],
                  'output':str(OUT)},indent=2))
