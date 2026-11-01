import itertools, math
import numpy as np

rng = np.random.default_rng(42)
accepted = 0
violations = []
max_marginal_error = 0.0
min_cross_ratio = float('inf')
min_star_ratio = float('inf')

# Finite regression only. The proof is in REPORT.md.
for trial in range(2000):
    if accepted >= 100:
        break
    n = 10
    r = np.ones(n)
    r = r / np.linalg.norm(r) * math.sqrt(0.2 + rng.random())
    z = rng.normal(size=n)
    z = z - r * (r @ z) / (r @ r)
    if np.linalg.norm(z) < 1e-12:
        continue
    z = z / np.linalg.norm(z) * math.sqrt(0.3 + rng.random())

    R2 = r @ r
    Z2 = z @ z
    a = r*r/R2
    b = z*z/Z2
    kappa = np.outer(r,z) - np.outer(z,r)
    m = (kappa*kappa).sum(axis=1)
    mu = m/(R2*Z2)
    max_marginal_error = max(max_marginal_error, float(np.max(np.abs(mu-(a+b)))))

    # Test the no-hub branch only.
    if np.max(mu) >= 2/5:
        continue
    accepted += 1

    found = False
    for maskint in range(1, 2**n-1):
        mask = np.array([(maskint >> i) & 1 for i in range(n)], dtype=bool)
        A = float(a[mask].sum())
        B = float(b[mask].sum())
        if 1/8 < A < 7/8 and 1/8 < B < 7/8:
            cross = float((kappa[np.ix_(mask,~mask)]**2).sum())
            cross_ratio = cross/(R2*Z2)
            star_ratio = float(np.linalg.norm(r[mask])*np.linalg.norm(r[~mask])/R2)
            min_cross_ratio = min(min_cross_ratio, cross_ratio)
            min_star_ratio = min(min_star_ratio, star_ratio)
            if cross_ratio < 1/32 - 1e-12:
                violations.append(('cross', trial, cross_ratio, A, B))
            if star_ratio < math.sqrt(7)/8 - 1e-12:
                violations.append(('star', trial, star_ratio, A, B))
            found = True
            break
    if not found:
        violations.append(('no_cut', trial))

print(f'accepted_no_hub_trials={accepted}')
print(f'max_marginal_identity_error={max_marginal_error:.3e}')
print(f'min_observed_cross_ratio={min_cross_ratio:.12f}')
print(f'theoretical_cross_floor={1/32:.12f}')
print(f'min_observed_star_ratio={min_star_ratio:.12f}')
print(f'theoretical_star_floor={math.sqrt(7)/8:.12f}')
print(f'violations={len(violations)}')
print('STATUS=PASS' if not violations and accepted == 100 else 'STATUS=FAIL')
