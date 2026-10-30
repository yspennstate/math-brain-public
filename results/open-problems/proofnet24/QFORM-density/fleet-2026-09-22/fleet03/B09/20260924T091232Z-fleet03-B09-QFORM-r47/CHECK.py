import math
import numpy as np

RNG = np.random.default_rng(4709)
C_DEF = (2.0 ** (5.0/4.0)) * math.pi * math.sqrt(3.0)

# 1. Exact square-completion algebra and polynomial-star identity.
max_completion_error = 0.0
max_star_error = 0.0
for _ in range(1000):
    L = RNG.normal(size=(2,2))
    B = L @ L.T + 0.1*np.eye(2)
    a, c, b = B[0,0], B[0,1], B[1,1]
    m = 6
    u = RNG.normal(size=m)
    v = RNG.normal(size=m)
    C = RNG.normal(size=(m,m)); C = 0.5*(C+C.T)
    alpha, beta = RNG.normal(size=2)
    gamma = RNG.normal(size=m)
    q0 = float(RNG.normal())
    x, y = RNG.normal(size=2); z = RNG.normal(size=m)
    q = (a*x*x + 2*c*x*y + b*y*y + 2*x*np.dot(u,z) +
         2*y*np.dot(v,z) + z @ C @ z + alpha*x + beta*y +
         np.dot(gamma,z) + q0)
    h = (c*y + np.dot(u,z) + alpha/2.0)/a
    delta = b - c*c/a
    g = v - (c/a)*u
    eta = (beta - c*alpha/a)/2.0
    W = z @ C @ z + np.dot(gamma,z) + q0 - (np.dot(u,z)+alpha/2.0)**2/a
    s = delta*y*y + 2*y*(np.dot(g,z)+eta) + W
    q2 = a*(x+h)**2 + s
    max_completion_error = max(max_completion_error, abs(q-q2))
    H = a*v - c*u
    max_star_error = max(max_star_error, np.linalg.norm(H-a*g))
assert max_completion_error < 1e-10
assert max_star_error < 1e-12

# 2. Numerical regression of the analytic arcsine-bathtub inequality.
def indicator_union(x, intervals):
    out = np.zeros_like(x, dtype=float)
    for aa, bb in intervals:
        out = np.maximum(out, ((x >= aa) & (x <= bb)).astype(float))
    return out

max_arcsine_ratio = 0.0
for _ in range(80):
    starts = np.sort(RNG.uniform(-5.0, 5.0, size=6))
    lengths = RNG.uniform(0.02, 0.3, size=6)
    lengths /= lengths.sum()
    intervals = [(float(s), float(s+l)) for s,l in zip(starts,lengths)]
    for _ in range(25):
        center = float(RNG.uniform(-6.0, 6.0))
        R = float(10.0 ** RNG.uniform(-2.0, 1.0))
        theta = np.linspace(-math.pi/2, math.pi/2, 5001)
        vals = indicator_union(center + R*np.sin(theta), intervals)
        A = float(np.trapezoid(vals, theta))
        yy = np.linspace(center-R, center+R, 5001)
        mass = float(np.trapezoid(indicator_union(yy, intervals), yy))
        avg = max(0.0, mass/(2.0*R))
        bound = math.pi*math.sqrt(avg)
        if bound > 2e-3:
            max_arcsine_ratio = max(max_arcsine_ratio, A/bound)
assert max_arcsine_ratio < 1.01

# 3. Target-valid punctured-definite stress family.
def stress_matrix(delta):
    return np.array([
        [2.0, 2.0, 0.0, 0.0],
        [2.0, 2.0 + delta/2.0, 1.0, 0.0],
        [0.0, 1.0, -5.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ])

stress_rows = []
for delta in [1.0, 1e-2, 1e-4, 1e-8, 1e-12]:
    A = stress_matrix(delta)
    ev = np.linalg.eigvalsh(A)
    B = A[:2,:2]
    detB = float(np.linalg.det(B))
    a, c = B[0,0], B[0,1]
    u = A[0,2:]
    v = A[1,2:]
    H = a*v-c*u
    assert detB > 0.0
    assert abs(detB-delta) <= max(1e-11, 1e-9*delta)
    assert np.linalg.norm(H-np.array([2.0,0.0])) < 1e-12
    assert np.count_nonzero(np.abs(ev) >= 1.0-1e-12) >= 3
    stress_rows.append((delta, ev.tolist(), detB, float(np.linalg.norm(H))))

stress_bound = C_DEF/math.sqrt(2.0)
assert abs(stress_bound - 9.15130430024412) < 1e-12

# 4. Live fleet02/B08 gate application.
live_currency = (4031.0/8192.0)*(1.0/8.0)
live_bound = C_DEF/math.sqrt(live_currency)
assert live_bound < 52.184

# 5. Required fleet04/B09 application: K=diag(4,2,1), det K=8.
partner_bound = 3.0*(8.0**(-1.0/3.0))
assert abs(partner_bound - 1.5) < 1e-12

print("C_DEF =", repr(C_DEF))
print("max_completion_error =", repr(max_completion_error))
print("max_star_error =", repr(max_star_error))
print("max_arcsine_ratio =", repr(max_arcsine_ratio))
print("stress_bound =", repr(stress_bound))
print("live_bound =", repr(live_bound))
print("partner_bound =", repr(partner_bound))
for delta, ev, detB, Hnorm in stress_rows:
    print("stress", delta, "eig", ["%.12g" % x for x in ev], "detB", "%.12g" % detB, "Hnorm", Hnorm)
print("ALL_ASSERTIONS_PASSED")
