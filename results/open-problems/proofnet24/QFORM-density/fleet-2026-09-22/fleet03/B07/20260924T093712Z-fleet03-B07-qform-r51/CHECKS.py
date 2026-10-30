import math
import numpy as np

EPS0 = 0.0016467608693485
ETA0 = 1/64 + EPS0
G0 = (7 - 4*math.sqrt(2))/16
SIGMA0 = G0*(1-ETA0) - ETA0
C3 = 3*2**(4/3)*math.e**(1/3)
PARTNER = 128*math.sqrt(6*math.pi*895)

assert 0 < SIGMA0
assert abs(ETA0 - 0.0172717608693485) < 1e-15
assert abs(G0 - 0.0839466094067262) < 1e-15
assert abs(SIGMA0 - 0.0652249427739121) < 1e-15
assert abs(C3/SIGMA0 - 161.750526447139) < 1e-9
assert abs(PARTNER - 16625.3979253295) < 1e-8


def hadamard(n):
    H = np.array([[1.0]])
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    return H

rng = np.random.default_rng(2026092407)
W = hadamard(128)/math.sqrt(128)
observed = []
for trial in range(200):
    r = int(rng.integers(3, 9))
    cols = rng.choice(128, size=r, replace=False)
    U = W[:, cols]
    mu = np.max(np.sum(U*U, axis=1))
    assert mu <= 1/16 + 1e-14

    vals = (1.1 + rng.random(r))*rng.choice([-1, 1], size=r)
    H = U @ np.diag(vals) @ U.T
    R = rng.standard_normal((128,128))
    R = (R + R.T)/2
    op = np.max(np.abs(np.linalg.eigvalsh(R)))
    E = (0.95*ETA0/op)*R
    A = H + E

    found = False
    for _ in range(300):
        mask = rng.random(128) < 0.5
        if mask.sum() == 0 or mask.sum() == 128:
            continue
        GI = U[mask].T @ U[mask]
        GJ = U[~mask].T @ U[~mask]
        lower = min(np.min(np.linalg.eigvalsh(GI)),
                    np.min(np.linalg.eigvalsh(GJ)))
        if lower >= G0:
            s = np.linalg.svd(A[np.ix_(mask, ~mask)], compute_uv=False)
            assert len(s) >= 3
            assert s[2] >= SIGMA0 - 1e-10
            observed.append(float(s[2]))
            found = True
            break
    assert found

print(f"eps0={EPS0:.16g}")
print(f"eta0={ETA0:.16g}")
print(f"g0={G0:.16g}")
print(f"sigma0={SIGMA0:.16g}")
print(f"C3={C3:.16g}")
print(f"C3/sigma0={C3/SIGMA0:.16g}")
print(f"partner_bound={PARTNER:.16g}")
print(f"random_trials={len(observed)}")
print(f"min_observed_cross_s3={min(observed):.16g}")
print("STATUS=PASS")
