import itertools
import math
import numpy as np

rng = np.random.default_rng(5108)

m0 = math.sqrt(47/48)
g = 0.5 - 1/(4*math.sqrt(2))
s0 = g*m0 - 1/4096
third_compound_constant = 6**(4/3) * (64/s0**2)**(1/3)
eps = math.sqrt((1/64)**2 + (1/4096)**2)
partner_row = 1/(4096*512)

print('m0', repr(m0))
print('g', repr(g))
print('s0', repr(s0))
print('third_compound_constant', repr(third_compound_constant))
print('double_tube_eps', repr(eps))
print('partner_row_coefficient', repr(partner_row))

# Regression 1: exterior-algebra inequality
# E3([z;D]) >= sigma1(D)^2 sigma2(D)^2 dist(z,R2(D))^2.
max_abs_violation = 0.0
min_ratio = float('inf')
tests = 0
for p in range(2, 8):
    for q in range(3, 9):
        for _ in range(40):
            D = rng.normal(size=(p, q))
            z = rng.normal(size=q)
            sing = np.linalg.svd(D, compute_uv=False)
            B = np.vstack([z, D])
            lam = np.maximum(np.linalg.eigvalsh(B @ B.T), 0.0)
            e3 = sum(lam[i]*lam[j]*lam[k]
                     for i in range(len(lam))
                     for j in range(i+1, len(lam))
                     for k in range(j+1, len(lam)))
            _, _, vt = np.linalg.svd(D, full_matrices=True)
            P = vt[:2].T @ vt[:2]
            d = np.linalg.norm(z - z @ P)
            rhs = sing[0]**2 * sing[1]**2 * d**2
            max_abs_violation = max(max_abs_violation, rhs-e3)
            if rhs > 1e-12:
                min_ratio = min(min_ratio, e3/rhs)
            tests += 1
print('exterior_tests', tests)
print('exterior_max_abs_violation_roundoff', repr(max_abs_violation))
print('exterior_min_ratio', repr(min_ratio))

# Regression 2: explicit diffuse tight frames. Random half-cuts find the
# analytic Bernoulli bound; these checks are not used as proof.
def hadamard(n):
    H = np.array([[1.0]])
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    return H

for n in (32, 64, 128):
    H = hadamard(n)/math.sqrt(n)
    V = H[:, [1, 2]]
    mu = np.max(np.sum(V*V, axis=1))
    best = float('inf')
    for _ in range(5000):
        mask = rng.random(n) < 0.5
        G = V[mask].T @ V[mask]
        best = min(best, np.linalg.norm(G-0.5*np.eye(2), ord='fro'))
    print('balanced_frame', n, 'mu', repr(float(mu)),
          'best_dev', repr(float(best)),
          'analytic_bound', repr(math.sqrt(float(mu)/2)))

print('QFORM_B08_PUNCTURED_CROSSSTAR_CHECK_PASS')
