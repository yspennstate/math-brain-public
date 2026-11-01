"""
PROB20-16 exploratory search: two active singleton sites with an arbitrary
coherent exterior and arbitrary complex two-row coupling.

This is NOT a certificate or proof.  It searches for a positive eigenvalue of
the entropy Hessian in squared row-amplitude coordinates (x,y).  Exact atom
probabilities are computed by signed determinants.  The bilinear atom model is
recovered from the four corners, so the entropy Hessian itself is then evaluated
analytically (not by finite differences).

The run retained in the accompanying report tested 64,000 interior
(point,kernel) samples for n=3,4,5,6 and found no positive eigenvalue above
floating-point tolerance.  This is evidence only.
"""
import numpy as np


def atom_probs(K):
    K = np.asarray(K, dtype=complex)
    n = K.shape[0]
    out = np.empty(1 << n, float)
    for mask in range(1 << n):
        M = K.copy()
        outside = [i for i in range(n) if not ((mask >> i) & 1)]
        for i in outside:
            M[i, i] -= 1
        out[mask] = (((-1) ** len(outside)) * np.linalg.det(M)).real
    return out


def coeffs_xy(d, C, B):
    vals = {}
    for x, y in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        sf = np.diag([np.sqrt(x), np.sqrt(y)])
        Bf = sf @ B
        K = np.block([[d, Bf], [Bf.conj().T, C]])
        vals[(x, y)] = atom_probs(K)
    p0 = vals[(0, 0)]
    a = vals[(1, 0)] - p0
    b = vals[(0, 1)] - p0
    c = vals[(1, 1)] - vals[(1, 0)] - vals[(0, 1)] + p0
    return p0, a, b, c


def entropy_hessian(p0, a, b, c, x, y):
    p = p0 + x * a + y * b + x * y * c
    if p.min() <= 0:
        return None
    px = a + y * c
    py = b + x * c
    Hxx = -np.sum(px * px / p)
    Hyy = -np.sum(py * py / p)
    Hxy = -np.sum(px * py / p + c * np.log(p))
    return np.array([[Hxx, Hxy], [Hxy, Hyy]])


rng = np.random.default_rng(4)
best_eigenvalue = -np.inf
best_record = None
count = 0

for n in [3, 4, 5, 6]:
    exterior = n - 2
    for trial in range(4000):
        d = np.diag(rng.uniform(.02, .98, 2))

        Z = rng.normal(size=(exterior, exterior)) + 1j * rng.normal(
            size=(exterior, exterior)
        )
        U, _ = np.linalg.qr(Z)
        lam = rng.uniform(.02, .98, exterior)
        C = U @ np.diag(lam) @ U.conj().T

        B = rng.normal(size=(2, exterior)) + 1j * rng.normal(
            size=(2, exterior)
        )
        B /= max(1.0, np.linalg.norm(B, 2))

        # Find a near-maximal strict feasible scale for B.
        lo, hi = 0.0, 0.5
        for _ in range(30):
            s = (lo + hi) / 2
            K = np.block([[d, s * B], [s * B.conj().T, C]])
            eig = np.linalg.eigvalsh(K)
            if eig.min() > 1e-7 and eig.max() < 1 - 1e-7:
                lo = s
            else:
                hi = s
        if lo < 1e-6:
            continue

        B2 = lo * rng.uniform(.2, .999) * B
        p0, a, b, c = coeffs_xy(d, C, B2)

        for _ in range(4):
            x, y = rng.uniform(.005, .995, 2)
            H = entropy_hessian(p0, a, b, c, x, y)
            if H is None:
                continue
            eigmax = float(np.linalg.eigvalsh(H)[-1])
            count += 1
            if eigmax > best_eigenvalue:
                best_eigenvalue = eigmax
                best_record = (n, trial, x, y, eigmax)
            if eigmax > 1e-9:
                raise AssertionError(
                    f"candidate positive curvature: {best_record}, H={H}"
                )

print("SEARCH COMPLETE; NO CERTIFIED CONCLUSION")
print("samples =", count)
print("largest observed Hessian eigenvalue =", best_eigenvalue)
print("best record =", best_record)
