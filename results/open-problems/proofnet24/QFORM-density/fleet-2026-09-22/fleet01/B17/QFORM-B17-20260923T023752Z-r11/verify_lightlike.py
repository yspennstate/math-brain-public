import math
import mpmath as mp
import numpy as np

mp.mp.dps = 50
C_light = 3 * mp.gamma(mp.mpf(1)/4) / (mp.sqrt(mp.pi) * mp.gamma(mp.mpf(3)/4))
barrier = 3 * mp.sqrt(2)
ratio = C_light / barrier
print("C_light", mp.nstr(C_light, 30))
print("3sqrt2", mp.nstr(barrier, 30))
print("ratio", mp.nstr(ratio, 30))
assert abs(C_light - mp.mpf("5.007761050044439")) < mp.mpf("1e-14")
assert C_light > barrier
assert ratio < mp.mpf("1.181")

# The auxiliary sinc constant used in the uniform finite-m envelope:
# 2 sqrt(m) exp(-m/12) is maximized over positive real m at m=6.
sinc_aux = 2 * mp.sqrt(6) * mp.e**(-mp.mpf(1)/2)
print("sinc_aux_max", mp.nstr(sinc_aux, 30))
assert sinc_aux < 3

# Exact frame identity checked numerically for representative theta,m.
def frame(theta, m):
    wp = np.array([1.0,0.0,1.0])/math.sqrt(2)
    wm = np.array([1.0,0.0,-1.0])/math.sqrt(2)
    e2 = np.array([0.0,1.0,0.0])
    rows = [math.sqrt(theta)*wp]
    rows += [math.sqrt((1-theta)/m)*wp for _ in range(m)]
    rows += [e2/math.sqrt(m) for _ in range(m)]
    rows += [wm/math.sqrt(m) for _ in range(m)]
    return np.vstack(rows)

J = np.diag([1.0,1.0,-1.0])
for theta in [0.0,0.17,0.5,0.93,1.0]:
    for m in [1,2,7,19]:
        R = frame(theta,m)
        assert np.linalg.norm(R.T@R-np.eye(3),ord=2) < 2e-14
        A=R@J@R.T
        ev=np.linalg.eigvalsh(A)
        nz=ev[np.abs(ev)>1e-9]
        assert len(nz)==3
        assert np.max(np.abs(np.sort(nz)-np.array([-1.0,1.0,1.0]))) < 2e-12
print("PASS QFORM-LIGHTLIKE-ONE-HEAVY-GLOBAL-v1")
