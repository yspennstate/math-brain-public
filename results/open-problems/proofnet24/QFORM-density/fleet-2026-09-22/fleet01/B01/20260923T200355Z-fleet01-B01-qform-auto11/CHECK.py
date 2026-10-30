import math
import numpy as np

# Strict-N3 spectral packet from REPORT.md
K=np.array([
 [0.,0.,0.,2.,0.],
 [0.,4.,0.,2.,0.],
 [0.,0.,0.,0.,2.],
 [2.,2.,0.,0.,0.],
 [0.,0.,2.,0.,0.],
])
vals=np.linalg.eigvalsh(K)
print('eigenvalues=',repr(vals.tolist()))
print('count_abs_ge_1=',int(np.sum(np.abs(vals)>=1-1e-12)))

B=2*np.eye(2)
q=np.array([2.,0.])
p=np.zeros(2)
A=np.diag([4.,0.])
a=0.
d=a-2*p@np.linalg.inv(B).T@q+q@np.linalg.inv(B)@A@np.linalg.inv(B).T@q
print('detB=',np.linalg.det(B))
print('dB=',d)

C0=5*(3*math.sqrt(6)/8)**(4/5)
bound=C0*(2*2)**(2/5)*(abs(np.linalg.det(B)))**(-2/5)*abs(d)**(-1/5)
print('C0=',repr(C0))
print('stress_bound=',repr(bound))

# exact kernel-curvature identity on random nonsymmetric invertible B
rng=np.random.default_rng(20260923)
maxerr=0.0
for _ in range(200):
    B=rng.normal(size=(2,2))
    if abs(np.linalg.det(B))<0.2:
        continue
    A0=rng.normal(size=(2,2)); A0=(A0+A0.T)/2
    p0=rng.normal(size=2); q0=rng.normal(size=2); a0=float(rng.normal())
    Binv=np.linalg.inv(B)
    d1=a0-2*p0@Binv.T@q0+q0@Binv@A0@Binv.T@q0
    v=np.r_[1.,-Binv.T@q0]
    Kxu=np.block([[np.array([[a0]]),p0.reshape(1,2)],[p0.reshape(2,1),A0]])
    d2=v@Kxu@v
    maxerr=max(maxerr,abs(d1-d2))
print('max_kernel_identity_error=',repr(maxerr))
assert np.sum(np.abs(vals)>=1-1e-12)>=3
assert abs(d-4)<1e-12
assert maxerr<1e-10
print('STATUS=PASS')
