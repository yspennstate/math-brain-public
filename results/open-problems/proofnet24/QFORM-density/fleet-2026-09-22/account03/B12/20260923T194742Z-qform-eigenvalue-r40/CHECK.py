import itertools
import math
import numpy as np

rng = np.random.default_rng(20260923)
TRIALS = 10000

def ell(rho):
    return (math.sqrt(rho*rho + 4.0) - rho) / 2.0

shear_viol = pair_viol = triple_viol = 0
shear_min = float("inf")
pair_ratio_min = float("inf")
triple_ratio_min = float("inf")

for _ in range(TRIALS):
    m = int(rng.integers(4, 9))
    n = int(rng.integers(max(3, m-2), m+4))

    M = rng.normal(size=(m, m))
    C = (M + M.T) / 2.0
    i = int(rng.integers(0, m))
    if abs(C[i, i]) < 1e-8:
        C[i, i] += 1.0
    K = [j for j in range(m) if j != i]
    eta = C[K, i] / C[i, i]

    B = rng.normal(size=(m, n))
    Bp = B[K, :] - np.outer(eta, B[i, :])
    sB = np.linalg.svd(B, compute_uv=False)
    sBp = np.linalg.svd(Bp, compute_uv=False)

    if len(sB) >= 3 and len(sBp) >= 2:
        margin = sBp[1] - ell(np.linalg.norm(eta))*sB[2]
        shear_min = min(shear_min, margin)
        shear_viol += int(margin < -1e-9)

    if len(sBp) >= 2:
        target = sBp[1]**2 / math.sqrt(math.comb(m-1, 2))
        best = 0.0
        for a, b in itertools.combinations(range(m-1), 2):
            R = Bp[[a, b], :]
            best = max(best, math.sqrt(max(0.0, np.linalg.det(R @ R.T))))
        if target > 1e-12:
            pair_ratio_min = min(pair_ratio_min, best/target)
            pair_viol += int(best + 1e-9 < target)

    if len(sB) >= 3:
        target3 = sB[2]**3 / math.sqrt(math.comb(m, 3))
        best3 = 0.0
        for inds in itertools.combinations(range(m), 3):
            R = B[list(inds), :]
            best3 = max(best3, math.sqrt(max(0.0, np.linalg.det(R @ R.T))))
        if target3 > 1e-12:
            triple_ratio_min = min(triple_ratio_min, best3/target3)
            triple_viol += int(best3 + 1e-9 < target3)

# Concrete constants for Section 7.
m = 8
g = s = 7/4
N2 = math.comb(m, 2)
N3 = math.comb(m, 3)
Np = math.comb(m-1, 2)
c = 1749/1000
b = 27/125
a = 3/500
kappa = b/N2 - a
alpha = c/m - b
L = (c/math.sqrt(m) + b)/alpha
le = ell(L)
d0 = math.sqrt(g*g - c*c)
d1 = math.sqrt(g*g - b*b)
terms = {
    "finite_core": 2*math.sqrt(6*math.pi*m)/a,
    "definite_pair": math.pi/kappa,
    "indefinite_pair": 3*(400**(1/3))*kappa**(-5/6)*s**(-1/6),
    "rank3_cross": 3*math.sqrt(2)*N3**(1/6)/d0,
    "rank1_shear_square_peel": 2**(11/4)*Np**(1/8)/math.sqrt(alpha*le*d1),
}

print(f"trials={TRIALS}")
print(f"shear_violations={shear_viol}; min_margin={shear_min:.15g}")
print(f"pair_extraction_violations={pair_viol}; min_ratio={pair_ratio_min:.15g}")
print(f"triple_extraction_violations={triple_viol}; min_ratio={triple_ratio_min:.15g}")
print(f"kappa={kappa:.15g}; alpha={alpha:.15g}; L={L:.15g}; ell_L={le:.15g}")
for name, value in terms.items():
    print(f"{name}={value:.15g}")
print(f"compiler_max={max(terms.values()):.15g}")
