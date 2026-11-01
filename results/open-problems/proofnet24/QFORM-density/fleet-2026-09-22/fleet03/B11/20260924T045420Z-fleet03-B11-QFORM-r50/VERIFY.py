import numpy as np
import math

# Deterministic corroboration only; analytic proofs are in REPORT.md.

rng=np.random.default_rng(20260924)
max_rank_schur=0.0
max_shear_err=0.0
checks1=0
for _ in range(5000):
    U=rng.normal(size=(3,2)); V=rng.normal(size=(3,2)); N=U@V.T
    B=N[1:,1:]
    if abs(np.linalg.det(B))<1e-4:
        continue
    n00=N[0,0]; p=N[0,1:]; q=N[1:,0]
    aa=np.linalg.solve(B.T,p); bb=np.linalg.solve(B,q)
    max_rank_schur=max(max_rank_schur,abs(n00-p@np.linalg.solve(B,q)))
    u=float(rng.normal()); x=rng.normal(size=2)
    v=float(rng.normal()); y=rng.normal(size=2)
    lhs=np.r_[u,x]@N@np.r_[v,y]
    rhs=(x+aa*u)@B@(y+bb*v)
    max_shear_err=max(max_shear_err,abs(lhs-rhs))
    checks1+=1

rng=np.random.default_rng(1234)
max_trans_rel=0.0
checks2=0
for _ in range(5000):
    m=10
    R0,_=np.linalg.qr(rng.normal(size=(m,3)))
    p0=R0[:,0]; VV=R0[:,1:]
    lam=np.diag([rng.choice([-1,1])*rng.uniform(.5,3),
                 rng.choice([-1,1])*rng.uniform(.5,3)])
    tau=10**rng.uniform(-2,0)
    b=rng.normal(size=2)
    a0=rng.choice([-1,1])*10**rng.uniform(-2,0)
    t=tau*p0+VV@b
    ell=a0*t
    perm=rng.permutation(m); I=perm[:m//2]; J=perm[m//2:]
    c=ell[I]; r=ell[J]
    if np.linalg.norm(c)<1e-10 or np.linalg.norm(r)<1e-10:
        continue
    VI=VV[I,:]; VJ=VV[J,:]
    Pc=np.eye(len(I))-np.outer(c,c)/(c@c)
    Pr=np.eye(len(J))-np.outer(r,r)/(r@r)
    cross=Pc@VI@lam@VJ.T@Pr
    sv=np.linalg.svd(cross,compute_uv=False)
    D=sv[0]*sv[1]
    GI=R0[I,:].T@R0[I,:]; GJ=R0[J,:].T@R0[J,:]
    rhs=(abs(np.linalg.det(lam))*(a0*a0)*(tau*tau)
         *math.sqrt(max(np.linalg.det(GI),0)*max(np.linalg.det(GJ),0))
         /(np.linalg.norm(c)*np.linalg.norm(r)))
    if rhs>1e-12:
        max_trans_rel=max(max_trans_rel,abs(D-rhs)/rhs)
        checks2+=1

rng=np.random.default_rng(911)
max_partner_rel=0.0
checks3=0
for _ in range(2000):
    n=8
    Z=rng.normal(size=(n,3)); U,_=np.linalg.qr(Z)
    vals=np.array([rng.uniform(1,3),rng.uniform(1,3),-rng.uniform(1,3)])
    M=np.diag(vals); A=U@M@U.T
    h=int(rng.integers(n)); qh=float(U[h]@U[h]); a=float(A[h,h])
    if abs(a)<1e-5:
        continue
    idx=[i for i in range(n) if i!=h]
    C=A[np.ix_(idx,idx)]; ell=A[idx,h]
    S=C-np.outer(ell,ell)/a
    sv=np.linalg.svd(S,compute_uv=False)
    d2=sv[0]*sv[1]; d3=abs(np.prod(vals))
    target=qh*d3/abs(a)
    max_partner_rel=max(max_partner_rel,abs(d2-target)/target)
    checks3+=1

delta=1/36
g=.5-delta-math.sqrt(2*delta)
C0=3*math.e/g
C64=C0*4
print('QFORM_B11_R50_CHIRPED_SCHUR_CHECK')
print('shear_checks',checks1)
print('max_rank2_schur_scalar_error',f'{max_rank_schur:.16e}')
print('max_shear_identity_error',f'{max_shear_err:.16e}')
print('transverse_volume_checks',checks2)
print('max_transverse_volume_relative_error',f'{max_trans_rel:.16e}')
print('partner_schur_checks',checks3)
print('max_partner_schur_relative_error',f'{max_partner_rel:.16e}')
print('g_1_over_36',f'{g:.17f}')
print('three_e_over_g',f'{C0:.17f}')
print('control_one_minus_q_1_over_64',f'{C64:.17f}')
print('QFORM_B11_R50_CHIRPED_SCHUR_CHECK_PASS')
