from fractions import Fraction
import math
import numpy as np

# Exact rational constants used in REPORT.md.
lb_DH = Fraction(16320, 16321)**2 * Fraction(16, 17)
assert lb_DH == Fraction(250675200, 266375041)
assert lb_DH > Fraction(94106, 100000)

L = Fraction(9999, 10000) * Fraction(100, 1273) - Fraction(1, 127)
assert L * L > Fraction(1, 202)

# Deterministic numerical regression on canonical matrices satisfying
# sigma_min(M)>=1.  This is a regression check only; REPORT.md contains
# the exact proofs.
rng = np.random.default_rng(290324)
checked = 0
max_id = 0.0
min_d = float("inf")
min_DH = float("inf")

for _ in range(200000):
    alpha = rng.uniform(-1/16, 1/16)
    s = rng.choice([-1.0, 1.0]) * rng.uniform(math.sqrt(255/256), 5.0)
    b = rng.uniform(-40, 40)
    k = rng.uniform(-20, 20)
    d = rng.choice([-1.0, 1.0]) * rng.uniform(1.0, 20.0)
    M = np.array([[alpha, s, 0.0], [s, b, k], [0.0, k, d]])
    sv = np.linalg.svd(M, compute_uv=False)
    if sv[-1] < 1 - 1e-11:
        continue

    rho = rng.uniform(1e-8, 1/64)
    gamma2 = s*s + alpha*alpha*rho
    D = abs(np.linalg.det(M))

    lhs = (d*d - 1)*s*s
    rhs = (1 - alpha*alpha)*k*k
    assert lhs + 2e-8 >= rhs
    min_d = min(min_d, abs(d))

    sigc = (alpha**3*rho**2 + 2*alpha*rho*s*s
            + s*s*(b - k*k/d))/gamma2
    DH_direct = 1 - (alpha/gamma2)*sigc
    DH_det = -s*s*np.linalg.det(M)/(d*gamma2*gamma2)
    max_id = max(max_id, abs(DH_direct - DH_det))
    assert abs(DH_direct - DH_det) < 2e-9 * max(1, abs(DH_det))
    min_DH = min(min_DH, abs(DH_direct))

    S2 = np.array([[alpha, s], [s, b - k*k/d]])
    assert abs(np.linalg.det(M) - d*np.linalg.det(S2)) < 2e-9 * max(1, D)
    delta = abs(np.linalg.det(S2))
    assert delta + 1e-10 >= s*s/(1 + abs(alpha))
    assert abs(DH_direct) + 1e-10 >= float(lb_DH)

    checked += 1
    if checked >= 5000:
        break

assert checked >= 1000, checked
print("checked", checked)
print("max_DH_identity_error", max_id)
print("min_abs_d", min_d)
print("min_abs_DH", min_DH)
print("report_DH_lower_bound", float(lb_DH))
print("partner_r_lower_square", float(L*L), ">", float(Fraction(1, 202)))
