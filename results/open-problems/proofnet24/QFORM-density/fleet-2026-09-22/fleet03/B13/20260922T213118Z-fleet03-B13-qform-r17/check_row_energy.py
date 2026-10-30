import math
import numpy as np

KAPPA = 7/800
DELTA = 1/100
C0 = 3/10

r_spec = math.sqrt(KAPPA)*math.sqrt(1-DELTA**2)-DELTA
r_phys = math.sqrt(C0)*r_spec
Astar = math.sqrt(math.pi*math.sqrt(2)/r_phys)
Cstar = math.exp(0.5)*math.gamma(0.25)/math.sqrt(2*r_phys)

assert r_spec > 0
assert r_phys > 0

rng = np.random.default_rng(20260922)
max_identity_error = 0.0
min_lower_margin = float('inf')
accepted = 0
for _ in range(100):
    n = 7
    P = rng.normal(size=(n,2))
    G = P.T @ P
    P = P / math.sqrt(2*np.linalg.eigvalsh(G).max())
    G = P.T @ P
    if np.linalg.eigvalsh(G).min() < KAPPA:
        continue

    w = rng.normal(size=2)
    val = float(w @ G @ w)
    if val > 0:
        w = w * math.sqrt(0.8/val)

    e = rng.normal(size=n)
    e = e - P @ np.linalg.solve(G, P.T @ e)
    en = np.linalg.norm(e)
    if en > 0:
        e = e * (0.08/en)

    t = P @ w + e
    a = rng.uniform(-DELTA, DELTA)
    bv = rng.normal(size=2)
    bv /= np.linalg.norm(bv)
    b = bv * (math.sqrt(1-a*a) + rng.uniform(0,1))

    s = a*t + P@b
    lhs = float(s@s)
    rhs_identity = float((b+a*w)@G@(b+a*w) + a*a*(e@e))
    lower = KAPPA*(math.sqrt(1-a*a)-abs(a)/math.sqrt(KAPPA))**2

    max_identity_error = max(max_identity_error, abs(lhs-rhs_identity))
    min_lower_margin = min(min_lower_margin, lhs-lower)
    accepted += 1

assert accepted > 0
assert max_identity_error < 1e-12
assert min_lower_margin >= -1e-12
assert abs(r_spec - 0.08353675748068244) < 1e-14
assert abs(r_phys - 0.0457549664530082) < 1e-14
assert abs(Astar - 9.854017169074433) < 1e-12
assert abs(Cstar - 19.76033020223181) < 1e-12

print('QFORM_B13_R17_CHECK_PASS')
print(f'r_spec={r_spec:.17g}')
print(f'r_phys={r_phys:.17g}')
print(f'Astar={Astar:.17g}')
print(f'Cstar={Cstar:.17g}')
print(f'accepted_random_identity_checks={accepted}')
print(f'max_identity_error={max_identity_error:.3e}')
print(f'min_random_lower_margin={min_lower_margin:.17g}')
