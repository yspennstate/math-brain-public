#!/usr/bin/env python3
"""Reproducible checks for the PROB20-16 real three-site path secant lemma.

Proof-critical sign arguments are analytic in the accompanying report.  This
script (i) verifies the algebraic posterior identities symbolically, (ii)
checks one exact rational strict path, and (iii) runs deterministic numerical
diagnostics comparing the closed-form gradient secant with direct two-site
entropy gradients and the complete atom Hessian on the A_22=0 hyperplane.
"""

from fractions import Fraction as F
import math
import numpy as np
import sympy as sp

SEED = 20260916


def symbolic_checks():
    r, u, v = sp.symbols('r u v', positive=True)
    r00 = r
    r10 = r-u
    r01 = r-v
    r11 = r-u-v
    assert sp.expand(r10*r01-r00*r11) == u*v
    t00 = 1-r00
    t10 = 1-r10
    t01 = 1-r01
    t11 = 1-r11
    assert sp.expand(t10*t01-t00*t11) == u*v

    S1, S3, lam, b, x2, y2, xy = sp.symbols(
        'S1 S3 lam b x2 y2 xy', positive=True)
    G = sp.Matrix([[S1-lam*y2/b, lam*xy/b],
                   [lam*xy/b, S3-lam*x2/b]])
    det_expected = S1*S3-(lam/b)*(S1*x2+S3*y2)
    # The cancellation uses xy^2 = x2*y2.
    det_sub = sp.expand(G.det().subs(xy**2, x2*y2))
    assert sp.simplify(det_sub-det_expected) == 0
    return True


def rational_witness():
    a,b,c,x,y = F(2,5),F(3,5),F(1,2),F(1,10),F(1,8)
    u = x*x/(a*(1-a))
    v = y*y/(c*(1-c))
    r00 = b+a*u+c*v
    r10 = r00-u
    r01 = r00-v
    r11 = r00-u-v
    success_margin = b-((1-a)*u+(1-c)*v)
    failure_margin = (1-b)-(a*u+c*v)
    assert min(r00,r10,r01,r11) > 0
    assert max(r00,r10,r01,r11) < 1
    assert success_margin > 0 and failure_margin > 0
    return dict(a=a,b=b,c=c,x=x,y=y,u=u,v=v,
                r00=r00,r10=r10,r01=r01,r11=r11,
                success_margin=success_margin,
                failure_margin=failure_margin)


def atom_probs(K):
    n = K.shape[0]
    out=[]
    for mask in range(1<<n):
        Q=K.astype(complex).copy()
        for i in range(n):
            if not ((mask>>i)&1):
                Q[i,i]-=1
        out.append((((-1)**(n-mask.bit_count()))*np.linalg.det(Q)).real)
    return np.array(out)


def grad2(Fm):
    U=float(Fm[0,0]); V=float(Fm[1,1]); Z=float(Fm[0,1])
    p00=(1-U)*(1-V)-Z*Z
    p10=U*(1-V)+Z*Z
    p01=V*(1-U)+Z*Z
    p11=U*V-Z*Z
    lam=math.log(p10*p01/(p00*p11))
    c1=math.log(p00/p10)
    c3=math.log(p00/p01)
    return np.array([[c1+lam*V,-lam*Z],[-lam*Z,c3+lam*U]])


def split_G(a,b,c,x,y):
    u=x*x/(a*(1-a)); v=y*y/(c*(1-c))
    r00=b+a*u+c*v
    r10=r00-u; r01=r00-v; r11=r00-u-v
    lp=math.log(r10*r01/(r00*r11))
    lm=math.log((1-r10)*(1-r01)/((1-r00)*(1-r11)))

    s0=math.log(r00/r10); s1=math.log(r01/r11)
    t0=math.log(r00/r01); t1=math.log(r10/r11)
    f0=math.log((1-r10)/(1-r00)); f1=math.log((1-r11)/(1-r01))
    g0=math.log((1-r01)/(1-r00)); g1=math.log((1-r11)/(1-r10))
    S1=(1-c)*s0+c*s1; S3=(1-a)*t0+a*t1
    B1=(1-c)*f0+c*f1; B3=(1-a)*g0+a*g1

    Gp=np.array([[S1-lp*y*y/b, lp*x*y/b],
                 [lp*x*y/b, S3-lp*x*x/b]])
    Gm=np.array([[B1-lm*y*y/(1-b), lm*x*y/(1-b)],
                 [lm*x*y/(1-b), B3-lm*x*x/(1-b)]])
    return Gp+Gm, Gp, Gm


def p_derivs(K,A):
    # For 3x3 determinants p(t) is cubic.  These five exact-in-degree samples
    # recover p'(0) and p''(0) without a finite-difference truncation error.
    p0=atom_probs(K)
    p1=atom_probs(K+A); pm1=atom_probs(K-A)
    p2=atom_probs(K+2*A); pm2=atom_probs(K-2*A)
    aa=(p1-pm1)/2
    bb=(p2-pm2)/4
    dp=(4*aa-bb)/3
    ddp=p1+pm1-2*p0
    return p0,dp,ddp


def H2dir(K,A):
    p,dp,ddp=p_derivs(K,A)
    return -np.sum(dp*dp/p + ddp*np.log(p))


def hermitian_basis():
    B=[]
    for i in range(3):
        M=np.zeros((3,3),complex); M[i,i]=1; B.append(M)
    for i,j in [(0,1),(0,2),(1,2)]:
        M=np.zeros((3,3),complex); M[i,j]=M[j,i]=1/math.sqrt(2); B.append(M)
    for i,j in [(0,1),(0,2),(1,2)]:
        M=np.zeros((3,3),complex); M[i,j]=1j/math.sqrt(2); M[j,i]=-1j/math.sqrt(2); B.append(M)
    return B


def hessian_on_basis(K,basis):
    q=np.array([H2dir(K,B) for B in basis])
    H=np.diag(q.copy())
    for i in range(len(basis)):
        for j in range(i+1,len(basis)):
            qij=H2dir(K,basis[i]+basis[j])
            H[i,j]=H[j,i]=(qij-q[i]-q[j])/2
    return H


def diagnostics(samples=1500):
    rng=np.random.default_rng(SEED)
    basis=hermitian_basis()
    # Exclude the middle-site diagonal basis vector: A_22=0.
    hyper=[basis[i] for i in [0,2,3,4,5,6,7,8]]
    count=0; min_G=float('inf'); max_hyp=-float('inf'); max_err=0.0
    for _ in range(30000):
        a,b,c=rng.uniform(.08,.92,3)
        x,y=rng.uniform(-.32,.32,2)
        if abs(x*y)<1e-4: continue
        K=np.array([[a,x,0],[x,b,y],[0,y,c]],float)
        if np.linalg.eigvalsh(K).min()<.025: continue
        if np.linalg.eigvalsh(np.eye(3)-K).min()<.025: continue
        z=np.array([x,y])
        F1=np.diag([a,c])-np.outer(z,z)/b
        F0=np.diag([a,c])+np.outer(z,z)/(1-b)
        Gdirect=grad2(F1)-grad2(F0)
        G,_,_=split_G(a,b,c,x,y)
        max_err=max(max_err,float(np.max(np.abs(G-Gdirect))))
        min_G=min(min_G,float(np.linalg.eigvalsh(G).min()))
        H=hessian_on_basis(K.astype(complex),hyper)
        max_hyp=max(max_hyp,float(np.linalg.eigvalsh(H).max()))
        count+=1
        if count>=samples: break
    assert count==samples
    assert min_G>0 and max_hyp<0 and max_err<1e-11
    return count,min_G,max_hyp,max_err


def main():
    symbolic_checks()
    w=rational_witness()
    print('symbolic_checks: PASS')
    print('rational_witness:')
    for k in ['a','b','c','x','y','u','v','r00','r10','r01','r11','success_margin','failure_margin']:
        print(f'  {k}={w[k]}')
    a,b,c,x,y=[float(w[k]) for k in ['a','b','c','x','y']]
    G,Gp,Gm=split_G(a,b,c,x,y)
    print('rational_G_eigenvalues:', *[f'{z:.16g}' for z in np.linalg.eigvalsh(G)])
    print('rational_Gplus_det:', f'{np.linalg.det(Gp):.16g}')
    print('rational_Gminus_det:', f'{np.linalg.det(Gm):.16g}')
    count,min_G,max_hyp,max_err=diagnostics()
    print('diagnostic_seed:',SEED)
    print('diagnostic_samples:',count)
    print('min_sampled_lambda_G:',f'{min_G:.16g}')
    print('max_sampled_hyperplane_Hessian_eigenvalue:',f'{max_hyp:.16g}')
    print('max_direct_vs_split_G_error:',f'{max_err:.16g}')
    print('NOTE: numerical diagnostics corroborate only; universal signs are proved analytically in the report.')

if __name__=='__main__':
    main()
