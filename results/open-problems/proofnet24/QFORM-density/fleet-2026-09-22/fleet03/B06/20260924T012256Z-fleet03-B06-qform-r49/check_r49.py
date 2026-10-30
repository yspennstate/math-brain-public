import numpy as np

rng=np.random.default_rng(20260924)
max_r1=0.0
max_r2=0.0
checked=0
for _ in range(10000):
    H=rng.normal(size=(2,2))
    H=(H+H.T)/2
    delta=np.linalg.det(H)
    if abs(delta)<5e-2:
        continue
    v=rng.normal(size=2)
    v=v/np.linalg.norm(v)
    lam=rng.uniform(-3,3)
    if abs(lam)<0.1:
        lam=0.5
    U=np.linalg.inv(H)+lam*np.outer(v,v)
    Hv=H@v
    for s in (0,1):
        h=H[s,s]
        if abs(h)<1e-8:
            continue
        q=np.zeros(2); q[s]=1.0
        R=U-np.outer(q,q)/h
        lhs=np.linalg.det(R)
        rhs=lam*Hv[s]**2/(h*delta)
        err=abs(lhs-rhs)/(1+abs(rhs))
        if s==0:
            max_r1=max(max_r1,err)
        else:
            max_r2=max(max_r2,err)
    checked+=1

prefactor=8*128**0.25
print("QFORM_B06_R49_CHECK_PASS")
print("checked",checked)
print("max_normalized_R1_error",max_r1)
print("max_normalized_R2_error",max_r2)
print("prefactor",prefactor)

assert max_r1 < 1e-10
assert max_r2 < 1e-10
assert abs(prefactor-26.908685288118864) < 1e-12
