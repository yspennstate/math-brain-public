"""Reproduce X006's exact identities and bounded floating-point self-checks.

The exact tests are algebraic identities, not floating-point sign proofs.
The universal inequalities are proved in agents/X006.md.
"""
import json
from pathlib import Path
from fractions import Fraction
from math import factorial
import numpy as np
import sympy as sp
from explore import data, BASIS
from conditional_geometry import matrices

def adj(A):
    return A@A-np.trace(A)*A+0.5*(np.trace(A)**2-np.trace(A@A))*np.eye(3)

def exact_checks():
    # A generic complex-Hermitian 3x3 direction, with the last coordinate
    # as pivot. This checks the entire conditional determinant expansion.
    a,c,tau,d,b1,b2,br,bi=sp.symbols('a c tau d b1 b2 br bi',real=True)
    vr1,vi1,vr2,vi2,wr1,wi1,wr2,wi2=sp.symbols('vr1 vi1 vr2 vi2 wr1 wi1 wr2 wi2',real=True)
    v=sp.Matrix([vr1+sp.I*vi1,vr2+sp.I*vi2])
    w=sp.Matrix([wr1+sp.I*wi1,wr2+sp.I*wi2])
    B=sp.Matrix([[b1,br+sp.I*bi],[br-sp.I*bi,b2]])
    A=B.row_join(w).col_join(w.conjugate().T.row_join(sp.Matrix([[d]])))
    V=v*v.conjugate().T
    cross=w*v.conjugate().T+v*w.conjugate().T
    r=sp.symbols('r',nonzero=True,real=True)
    L=sp.trace(B.adjugate()*cross)
    E=d*(v.conjugate().T*B.adjugate()*v)[0]-(v[0]*w[1]-v[1]*w[0])*sp.conjugate(v[0]*w[1]-v[1]*w[0])
    residual=sp.expand((B-cross/r+d*V/r**2).det()-B.det()+L/r-E/r**2)
    assert residual==0
    eta=(c+tau*(1-a))/(a*(1-a))
    N=(eta*V).row_join(tau*v).col_join((tau*v.conjugate().T).row_join(sp.Matrix([[c+tau*a]])))
    residual2=sp.expand(sp.trace(N*A.adjugate())-(c+tau*a)*B.det()+tau*L-eta*E)
    assert sp.cancel(residual2)==0
    assert sp.factor(eta-tau**2/(c+tau*a)-c*(c+tau)/(a*(1-a)*(c+tau*a)))==0
    # Weighted sums which turn the conditional expansion into N.
    assert sp.simplify(a*(c+tau)/a+(1-a)*c/(a-1)-tau)==0
    assert sp.simplify(a*(c+tau)/a**2+(1-a)*c/(a-1)**2-eta)==0
    e=sp.symbols('e',positive=True)
    cc=(8-5*e+sp.I*sp.sqrt(e*(16-25*e)))/8
    # The real and imaginary parts determine |c|^2 without branch issues.
    assert sp.expand(((8-5*e)**2+e*(16-25*e))/64-(1-e))==0
    determinant=1-sp.Rational(3,4)-sp.Rational(3,4)-(1-e)+sp.Rational(3,2)*(8-5*e)/8
    assert sp.expand(determinant-e/16)==0
    Z=1+3+sp.Rational(1,4)+e+sp.Rational(1,4)+e/16
    assert Z==sp.Rational(9,2)+17*e/16
    exp_lower=sum(Fraction(9,7)**j/factorial(j) for j in range(5))
    assert exp_lower>Fraction(7,2)
    return {'generic_complex_conditional_determinant':'PASS','generic_adjugate_matrix_identity':'PASS','N_schur_complement':'PASS','conditional_weighted_sums':'PASS','tauzero_family_principal_determinants':'PASS','exp_9_over_7_rational_lower_bound':str(exp_lower),'exp_bound_margin':str(exp_lower-Fraction(7,2))}

def hessian(K,A):
    FI=0.;accel=0.
    for s in range(8):
        Q=K-np.diag([1-(s>>i&1) for i in range(3)])
        p=(-1)**(3-s.bit_count())*np.linalg.det(Q).real
        R=np.linalg.solve(Q,A);score=np.trace(R).real
        second=p*(score**2-np.trace(R@R).real)
        FI+=p*score**2;accel-=second*np.log(p)
    return FI,accel,accel-FI

def diagnostic(K,A,label):
    d=data(K);Ns,R=matrices(K,d)
    FI,accel,H=hessian(K,A);Ad=adj(A)
    D=sum(A[k,k].real**2/(K[k,k].real*(1-K[k,k].real)) for k in range(3))
    conditional_res=[]
    for k,N in enumerate(Ns):
        inds=[i for i in range(3) if i!=k]
        a=K[k,k].real;v=K[inds,k];w=A[inds,k];B=A[np.ix_(inds,inds)];dd=A[k,k].real
        lhs=0.
        for s in (0,1):
            r=a-(1-s);pi=a if s else 1-a
            Bs=B-(np.outer(w,v.conj())+np.outer(v,w.conj()))/r+dd*np.outer(v,v.conj())/r**2
            lhs+=pi*(d['c'][k]+d['tau']*s)*np.linalg.det(Bs).real
        conditional_res.append(float(lhs-np.trace(N@Ad).real))
    bound1=-FI/7-2*D/7-2*np.trace(R@Ad).real
    bound2=-np.trace((d['M']+7*R)@Ad).real/3-D/3
    qN=2*np.trace(sum(Ns)@Ad).real
    return {'label':label,'tau':float(d['tau']),'A_eigenvalues':np.linalg.eigvalsh(A).tolist(),'FI':float(FI),'Hessian':float(H),'Lorentz_formula_residual':float(accel-2*np.trace(d['M']@Ad).real),'conditional_identity_residuals':conditional_res,'conditional_Fisher_margin':float((2/7)*(3*FI-D)-qN),'bound_4_1':float(bound1),'bound_4_2':float(bound2),'N_eigenvalues':[np.linalg.eigvalsh(N).tolist() for N in Ns]}

def run():
    exact=exact_checks()
    K0=np.array([[1/3,1/10,-1j/15],[1/10,1/2,1/12],[1j/15,1/12,2/3]])
    A0=np.array([[.4,.1-.2j,.15+.2j],[.1+.2j,.8,-.1+.3j],[.15-.2j,-.1-.3j,-.15]])
    e=2.**-20
    cc=(8-5*e+1j*np.sqrt(e*(16-25*e)))/8
    L=np.array([[1,np.sqrt(3)/2,np.conj(cc)],[np.sqrt(3)/2,1,np.sqrt(3)/2],[cc,np.sqrt(3)/2,1]])
    K=np.linalg.solve(np.eye(3)+L,L)
    d=data(K);Ns,R=matrices(K,d);S=d['M']+7*R
    eig,U=np.linalg.eigh(S);epsilon=eig[0]/(2*(np.trace(S).real-eig[0]))
    u=U[:,0];A=np.eye(3)-(1+epsilon)*np.outer(u,u.conj())
    diags=[diagnostic(K0,A0,'general_tau_general_direction'),diagnostic(K,np.eye(3),'tauzero_positive_definite'),diagnostic(K,A,'tauzero_full_rank_indefinite')]
    assert max(abs(x) for q in diags for x in q['conditional_identity_residuals'])<1e-10
    assert max(abs(q['Lorentz_formula_residual']) for q in diags)<1e-5
    assert all(q['conditional_Fisher_margin']>-1e-8 for q in diags)
    assert all(q['Hessian']<=q['bound_4_1']+1e-8 and q['Hessian']<=q['bound_4_2']+1e-8 for q in diags)
    assert diags[-1]['A_eigenvalues'][0]<0 and diags[-1]['Hessian']<0
    out={'exact_checks':exact,'bounded_diagnostics':diags,'difficult_family':{'epsilon':e,'occupation_only_scalar':float(d['three']),'trace_variance_ratio':float(d['ratio']),'exact_full_scalar':float(d['scalar']),'indefinite_direction_epsilon':float(epsilon)}}
    Path(__file__).with_name('reproduce.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

if __name__=='__main__':run()
