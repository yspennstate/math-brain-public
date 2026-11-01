import math
import numpy as np

rng = np.random.default_rng(20260923)

def weighted_constant(theta, q):
    m = 2.0 + theta
    return (math.e * m / ((m - 2.0*q)*math.sqrt(q))
            * (theta**theta * (1.0-theta)**(1.0-theta))**(1.0/(2.0*m)))

# Exact reduction to r23 at theta=1/2, q=1.
c_new = weighted_constant(0.5, 1.0)
c_old = 5.0*math.e/(2.0**(1.0/5.0))
assert abs(c_new-c_old) < 1e-12

# Relaxed 3/5-gate constant.
c_relaxed = weighted_constant(0.5, 6.0/5.0)

# Algebraic anchored-E2 and double-anchored-E3 identities.
max_e2_rel = 0.0
max_e3_rel = 0.0
for _ in range(1000):
    nr, nc = 5, 6
    N = rng.normal(size=(nr, nc))
    i = int(rng.integers(nr)); j = int(rng.integers(nc))
    rr = [i] + [k for k in range(nr) if k != i]
    cc = [j] + [k for k in range(nc) if k != j]
    Q = N[np.ix_(rr, cc)]
    a = Q[0, 0]; r = Q[0, 1:]; c = Q[1:, 0]; M = Q[1:, 1:]
    h2 = 0.0
    for u in range(1, nr):
        for v in range(1, nc):
            h2 += np.linalg.det(Q[np.ix_([0,u],[0,v])])**2
    rhs2 = np.linalg.norm(a*M - np.outer(c,r), 'fro')**2
    max_e2_rel = max(max_e2_rel, abs(h2-rhs2)/(1+abs(h2)+abs(rhs2)))

    nr2, nc2 = 6, 7
    B = rng.normal(size=(nr2, nc2))
    rows = list(rng.choice(nr2, 2, replace=False))
    cols = list(rng.choice(nc2, 2, replace=False))
    rrest = [k for k in range(nr2) if k not in rows]
    crest = [k for k in range(nc2) if k not in cols]
    W = B[np.ix_(rows+rrest, cols+crest)]
    P = W[:2,:2]; R = W[:2,2:]; C = W[2:,:2]; D = W[2:,2:]
    g3 = 0.0
    for u in range(2, nr2):
        for v in range(2, nc2):
            g3 += np.linalg.det(W[np.ix_([0,1,u],[0,1,v])])**2
    adjP = np.array([[P[1,1], -P[0,1]], [-P[1,0], P[0,0]]])
    rhs3 = np.linalg.norm(np.linalg.det(P)*D - C@adjP@R, 'fro')**2
    max_e3_rel = max(max_e3_rel, abs(g3-rhs3)/(1+abs(g3)+abs(rhs3)))

# Partner L2 + relaxed tail hybrid constant.
theta = 0.5
q = 6.0/5.0
m = 2.0 + theta
Ctheta = theta**(-theta)*(1.0-theta)**(-(1.0-theta))
coef = Ctheta**(-0.5)*math.e**m*q**(-m/2.0)*math.pi**m
Kc = coef**(1.0/(2.0*q))
b = m/(2.0*q)
rhyb = 1.0/(2.0*b-1.0)
Lconst = (6.0*math.pi*2.0**(2.0/3.0))**0.5
Icoef = (math.sqrt(2.0)*(2.0*b-1.0)/(2.0*(b-1.0))
         *(2.0*math.sqrt(2.0))**rhyb)
hybrid = Icoef*(Lconst**(1.0-rhyb))*(Kc**rhyb)/(2.0*math.pi)

print(f"weighted_theta_half_q1={c_new:.12f}")
print(f"weighted_theta_half_q6over5={c_relaxed:.12f}")
print(f"max_anchored_E2_relative_error={max_e2_rel:.3e}")
print(f"max_double_anchor_E3_relative_error={max_e3_rel:.3e}")
print(f"partner_hybrid_constant={hybrid:.12f}")
assert max_e2_rel < 1e-12
assert max_e3_rel < 1e-12
assert abs(c_relaxed-54.00548472344774) < 1e-12
assert abs(hybrid-54.8932933449953) < 1e-12
print("STATUS=PASS")
