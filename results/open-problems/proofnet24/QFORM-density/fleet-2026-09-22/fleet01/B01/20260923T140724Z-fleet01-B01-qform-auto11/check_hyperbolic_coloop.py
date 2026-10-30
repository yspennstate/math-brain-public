import math
import numpy as np

rng = np.random.default_rng(20260923)
max_error = 0.0
for _ in range(1000):
    m = 7
    a = float(rng.normal())
    if abs(a) < 0.1:
        a += 0.31
    b = float(rng.normal())
    if abs(b) < 0.1:
        b += 0.37
    lam = float(rng.normal())
    if abs(lam) < 0.1:
        lam += 0.41
    z = rng.normal(size=m)
    z /= np.linalg.norm(z)
    c = rng.normal(size=m)

    u = np.r_[0.0, z]
    v = np.r_[b, c]
    S = lam * np.outer(u, u) - (1.0 / a) * np.outer(v, v)
    ev = np.linalg.eigvalsh(S)
    nz = ev[np.abs(ev) > 1e-8]
    assert len(nz) == 2

    exact = -(lam / a) * (b*b + np.dot(c, c) - np.dot(c, z)**2)
    err = abs(np.prod(nz) - exact) / max(1.0, abs(exact))
    max_error = max(max_error, float(err))

c51 = 2.0 / (math.sqrt(51.0**2 + 4.0) + 51.0)
pair_constant = 8.0 * math.sqrt(5.0) * c51**(-0.25)
pivot_constant = 128.0 * 51.0**(-0.25)

print(f"max_normalized_schur_product_error={max_error:.17g}")
print(f"pair_constant={pair_constant:.15f}")
print(f"pivot_constant={pivot_constant:.15f}")
print(f"combined_constant={max(pair_constant, pivot_constant):.15f}")
print("STATUS=PASS" if max_error < 1e-10 and max(pair_constant, pivot_constant) < 48 else "STATUS=FAIL")
