import numpy as np
from math import sqrt

rng = np.random.default_rng(20260923)
gamma = 0.4
qualifying = 0
min_margin = float('inf')

for _ in range(20000):
    h, l = 2, 4
    Q, _ = np.linalg.qr(rng.normal(size=(l, l)))
    mus = rng.uniform(-1.5, 1.5, l)
    D = Q @ np.diag(mus) @ Q.T
    R = rng.normal(size=(h, h))
    R = (R + R.T) / 2
    top = np.linalg.eigvalsh(R).max()
    B = R - (top - (1-gamma) + 0.1) * np.eye(h)
    C = 0.8 * rng.normal(size=(h, l))
    A = np.block([[B, C], [C.T, D]])

    for sig in (+1, -1):
        pA = np.count_nonzero(np.linalg.eigvalsh(sig*A) >= 1-1e-10)
        pD = np.count_nonzero(np.linalg.eigvalsh(sig*D) >= 1-1e-10)
        if pA <= pD:
            continue
        if np.linalg.eigvalsh(sig*B).max() > 1-gamma+1e-10:
            continue
        vals, vecs = np.linalg.eigh(sig*D)
        use = vals < 1-1e-10
        assert np.any(use)
        resolvent = vecs[:,use] @ np.diag(1/(1-vals[use])) @ vecs[:,use].T
        weighted = C @ resolvent @ C.T
        carrier = np.linalg.eigvalsh(weighted).max()
        assert carrier >= gamma-1e-8
        qualifying += 1
        min_margin = min(min_margin, carrier-gamma)

# Exact sharp family: spectrum {1,1,-1,-delta}, carrier^2=delta,
# and the normalized threshold carrier equals one.
for delta in (0.5, 0.1, 0.01, 1e-4):
    B = np.array([[0.0]])
    D = np.diag([1.0, -1.0, 1.0-delta])
    C = np.array([[0.0, 0.0, sqrt(delta)]])
    A = np.block([[B,C],[C.T,D]])
    assert np.allclose(np.linalg.eigvalsh(A), [-1.0, -delta, 1.0, 1.0], atol=1e-10)
    vals, vecs = np.linalg.eigh(D)
    use = vals < 1-1e-12
    resolvent = vecs[:,use] @ np.diag(1/(1-vals[use])) @ vecs[:,use].T
    weighted = (C @ resolvent @ C.T)[0,0]
    assert abs(weighted-1.0) < 2e-10
    assert abs(np.linalg.norm(C,2)**2-delta) < 2e-12

print('QFORM_B19_THRESHOLD_NORMALIZED_CARRIER_CHECK_PASS')
print('qualifying_sign_cases', qualifying)
print('minimum_random_margin_above_gamma', min_margin)
print('sharp_family_normalized_carrier', 1.0)
