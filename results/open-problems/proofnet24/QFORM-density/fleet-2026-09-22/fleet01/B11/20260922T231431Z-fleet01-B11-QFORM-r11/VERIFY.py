import math
import numpy as np

# Constants used in REPORT.md.
delta0=(9/1024)**(1/5)
pair=3*(400**(1/3))*delta0**(-5/6)
diffuse=3*math.e**(2/3)
minority_const=4*math.sqrt(math.pi)

assert abs(delta0-0.3879613934788399) < 1e-14
assert pair < 48.658
assert diffuse < 5.844
assert minority_const < 7.090

# Random numerical audit of pdet(S)=c*det(M)/a in the minority-pivot case.
rng=np.random.default_rng(12345)
max_relerr=0.0
for _ in range(100):
    H=rng.normal(size=(3,3))
    Q,_=np.linalg.qr(H)
    vals=np.array([1.3,2.1,-1.7])
    M=Q@np.diag(vals)@Q.T

    for _ in range(1000):
        v=rng.normal(size=3)
        v/=np.linalg.norm(v)
        c=rng.uniform(0.05,0.95)
        r=np.sqrt(c)*v
        a=float(r@M@r)
        if a < -1e-4:
            break
    else:
        raise RuntimeError("failed to sample minority pivot")

    G=np.eye(3)-np.outer(r,r)
    ew,U=np.linalg.eigh(G)
    Ghalf=U@np.diag(np.sqrt(np.maximum(ew,0)))@U.T
    Rm=Ghalf
    b=Rm@M@r
    C=Rm@M@Rm.T
    S=C-np.outer(b,b)/a
    es=np.linalg.eigvalsh(S)
    nz=es[np.abs(es)>1e-8]
    pd=float(np.prod(nz))
    rhs=float(c*np.linalg.det(M)/a)
    rel=abs(pd-rhs)/max(1.0,abs(rhs))
    max_relerr=max(max_relerr,rel)

assert max_relerr < 1e-10
print(f"delta0={delta0:.16f}")
print(f"pair_bound={pair:.12f}")
print(f"diffuse_bound={diffuse:.12f}")
print(f"minority_constant={minority_const:.12f}")
print(f"max_schur_pdet_relative_error={max_relerr:.3e}")
print("QFORM_B11_HUBCURV_CHECK_PASS")
