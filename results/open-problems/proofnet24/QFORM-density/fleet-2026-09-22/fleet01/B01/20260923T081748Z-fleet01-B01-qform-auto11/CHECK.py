import math
import numpy as np

rng = np.random.default_rng(230923)
max_rel = 0.0
min_N = float('inf')
used = 0

for _ in range(500):
    m = int(rng.integers(4, 15))
    V, _ = np.linalg.qr(rng.normal(size=(m, 2)))
    w = rng.normal(size=m)
    w /= np.linalg.norm(w)
    j = int(rng.integers(0, m))

    v = V[j, :]
    h = float(v @ v)
    q = V.T @ w
    t = w - V @ q
    Omega = float(np.linalg.norm(t))
    tau = float(t[j])
    if Omega < 1e-10:
        continue
    ell = h + tau * tau / (Omega * Omega)

    lam = float(rng.choice([-1.0, 1.0]) * 10 ** rng.uniform(-1, 1))
    d = float(rng.normal())
    a = d + lam * w[j] ** 2
    if abs(a) < 1e-7:
        continue

    c = lam * w[j] / a
    Z = np.array([V[l, :] - c * w[l] * v for l in range(m) if l != j])
    lhs = float(np.linalg.det(Z.T @ Z))
    N = (lam ** 2 * w[j] ** 2 * ell * Omega ** 2
         + 2 * lam * w[j] * d * tau
         + (1 - h) * d ** 2)
    rhs = N / (a * a)
    rel = abs(lhs - rhs) / max(1.0, abs(lhs), abs(rhs))
    max_rel = max(max_rel, rel)
    min_N = min(min_N, N)
    used += 1

print('identity_samples=', used)
print('max_normalized_identity_error=', format(max_rel, '.16e'))
print('minimum_N_seen=', format(min_N, '.16e'))

print('stress_family: c=a^(-1/2), h=3/4, Omega=1, tau=1/2, ell=1')
for a in [1/8, 1/32, 1/128, 1/512]:
    c = a ** (-0.5)
    N = (a + 0.75) ** 2 / 4
    bound = 8 * a ** (-0.25) * (c * c) ** (-0.25) * N ** (-0.125)
    closed = 8 * (2 / (a + 0.75)) ** 0.25
    print('a=', a, 'c=', c, 'N=', N, 'bound=', bound,
          'closed_form=', closed, 'difference=', abs(bound - closed))

universal_stress_cap = 8 * (8/3) ** 0.25
print('stress_uniform_cap_for_0<a<=1/8=', universal_stress_cap)
print('STATUS=PASS')
