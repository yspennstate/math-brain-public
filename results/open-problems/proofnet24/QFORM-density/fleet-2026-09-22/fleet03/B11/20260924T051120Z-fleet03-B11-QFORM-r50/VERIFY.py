import numpy as np
from math import sqrt

rng=np.random.default_rng(20260924)
max_factor_err=0.0
max_gram_err=0.0
max_det_err=0.0
checks=0
for _ in range(20000):
    q=float(rng.uniform(0.5,0.999999))
    lam=float(10**rng.uniform(-1,1))
    vals=np.array([
        rng.choice([-1,1])*lam*(1+rng.uniform(0,4)),
        rng.choice([-1,1])*lam*(1+rng.uniform(0,4)),
        rng.choice([-1,1])*lam*(1+rng.uniform(0,4)),
    ])
    if np.all(vals>0) or np.all(vals<0):
        vals[0]*=-1
    Z=rng.normal(size=(3,3))
    O,_=np.linalg.qr(Z)
    M0=O@np.diag(vals)@O.T
    e1=np.array([1.0,0.0,0.0])
    m1=M0@e1
    trans=m1-m1[0]*e1
    if np.linalg.norm(trans)<1e-8:
        continue
    e2=trans/np.linalg.norm(trans)
    e3=np.cross(e1,e2)
    E=np.column_stack([e1,e2,e3])
    M=E.T@M0@E
    a,r,_=M[0]
    b,c=M[1,1],M[1,2]
    d=M[2,2]
    if abs(a)<1e-7 or abs(d)<1e-7:
        continue
    det=float(np.linalg.det(M))
    gamma=det/(a*d)
    st=sqrt(1-q); sq=sqrt(q)
    R=np.array([[sq,st,0,0],[0,0,1,0],[0,0,0,1]],float)
    A4=R.T@M@R
    u=np.array([sq,st,r/a,0.0])
    y=np.array([0.0,0.0,1.0,0.0])
    v=np.array([0.0,0.0,c/d,1.0])
    A4b=a*np.outer(u,u)+gamma*np.outer(y,y)+d*np.outer(v,v)
    max_factor_err=max(max_factor_err,float(np.max(np.abs(A4-A4b))))
    C=np.column_stack([u,y,v])
    gramdet=float(np.linalg.det(C.T@C))
    max_gram_err=max(max_gram_err,abs(gramdet-1.0))
    max_det_err=max(max_det_err,abs(a*gamma*d-det))
    checks+=1

q0=63/64
ratio_gamma=63.0
ratio_partner=q0*64.0

print("QFORM fleet03/B11 r50 deterministic verification")
print("checks",checks)
print("max_factorization_error",repr(max_factor_err))
print("max_unit_volume_gramdet_error",repr(max_gram_err))
print("max_coefficient_product_error",repr(max_det_err))
print("hard_collar_gamma_d_over_s2_lower_bound",ratio_gamma)
print("hard_collar_partner_Delta2_over_s2_lower_bound",ratio_partner)
assert max_factor_err < 1e-7
assert max_gram_err < 1e-6
assert max_det_err < 1e-7
assert abs(ratio_partner-63.0)<1e-12
print("QFORM_B11_R50_VOLUME_PRESERVING_LDL_CHECK_PASS")
