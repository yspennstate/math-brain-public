import math
import numpy as np

M0 = 3037500/(1536*math.e**2)
T0 = 16*M0
B0 = math.sqrt(2*T0)
A0 = 3.5*T0
assert abs(M0-267.630809134903) < 1e-12
assert abs(T0-4282.092946158448) < 1e-12
assert abs(B0-92.54288677319774) < 1e-12
assert abs(A0-14987.325311554569) < 1e-11

rng = np.random.default_rng(20260924)
err = 0.0
for _ in range(1000):
    c = float(rng.uniform(0.05, 1.0))
    dk = float(rng.choice([-1.0, 1.0]) * rng.uniform(1.0, 3.0))
    x = rng.normal(size=4)
    y = rng.normal(size=4)
    y[np.abs(y) < 0.1] += 0.3
    d = rng.normal(size=4)
    r = x/y
    s = y*y
    e = np.zeros((4,4))
    for i in range(4):
        for j in range(i+1,4):
            qij = (x[i]*y[j]-y[i]*x[j])**2
            tau = dk*qij + d[i]*c*s[j] + d[j]*c*s[i]
            e[i,j] = tau/(s[i]*s[j])
    lhs = e[0,2]-e[0,3]-e[1,2]+e[1,3]
    rhs = -2*dk*(r[0]-r[1])*(r[2]-r[3])
    err = max(err, abs(lhs-rhs))
    ai = c*d[0]/s[0]
    rhs2 = -dk*(r[0]-r[1])*(r[0]-r[2]) + (e[0,1]+e[0,2]-e[1,2])/2
    err = max(err, abs(ai-rhs2))

assert err < 1e-10, err
print('QFORM_B13_PROJECTIVE_PACKET_CHECK_PASS', err)
