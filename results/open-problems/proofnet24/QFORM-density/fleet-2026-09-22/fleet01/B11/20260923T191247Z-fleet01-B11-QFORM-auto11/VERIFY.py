import math
import numpy as np

cmin = 63.0/64.0
mu0 = 1.0/32.0
rho0 = mu0/(1.0 + 1.0/math.sqrt(63.0))**2
r0 = 1.0/(64.0*rho0)
G0 = ((2.0*math.pi)**1.5 * math.exp(0.5)
      * math.gamma(0.25)/(4.0*math.sqrt(math.pi)*math.gamma(0.75)))
R0 = math.sqrt(5.0 + (1.0+2.0*r0)**2/(1.0-r0*r0))
B0 = 1.0 + 2.0*(2.0/math.sqrt(1.0-r0*r0) + 2.0 + G0*R0)
Cfinal = B0/rho0

print(f"rho0={rho0:.15f}")
print(f"r0={r0:.15f}")
print(f"G0={G0:.15f}")
print(f"R0={R0:.15f}")
print(f"B0={B0:.15f}")
print(f"final_constant={Cfinal:.15f}")

assert r0 < 1.0
assert Cfinal < 3656.0

# Deterministic stress test of the singular-value lower bound in (3.7).
rng = np.random.default_rng(20260923)
worst_ratio = float("inf")
violations = 0
for _ in range(20000):
    c = cmin + (1.0-cmin)*rng.random()
    eta = 1.0-c
    lam1 = mu0 + (1.0-mu0)*rng.random()
    lam2 = mu0 + (1.0-mu0)*rng.random()
    theta = 2.0*math.pi*rng.random()
    O = np.array([[math.cos(theta), -math.sin(theta)],
                  [math.sin(theta),  math.cos(theta)]])
    W = O @ np.diag([lam1, lam2]) @ O.T
    Wh = O @ np.diag([math.sqrt(lam1), math.sqrt(lam2)]) @ O.T

    q = rng.normal(size=2)
    qWq = float(q @ W @ q)
    if qWq == 0.0:
        continue
    # force q^T W q <= eta
    q *= math.sqrt(eta*rng.random()/qWq)
    rr = Wh @ q
    C = np.block([[np.array([[math.sqrt(c)]]), rr.reshape(1,2)],
                  [np.zeros((2,1)), Wh]])
    smin2 = float(np.linalg.svd(C, compute_uv=False)[-1]**2)
    bound = mu0/(1.0 + math.sqrt(eta/c))**2
    worst_ratio = min(worst_ratio, smin2/bound)
    if smin2 + 1e-12 < bound:
        violations += 1

print(f"samples=20000")
print(f"singular_bound_violations={violations}")
print(f"min_observed_ratio_actual_over_bound={worst_ratio:.12f}")
assert violations == 0
print("QFORM_B11_SUBCRITICAL_GRAPH_CHECK_PASS")
