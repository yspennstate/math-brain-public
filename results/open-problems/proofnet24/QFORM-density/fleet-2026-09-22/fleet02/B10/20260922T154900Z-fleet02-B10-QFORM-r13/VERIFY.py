from fractions import Fraction
import math
import numpy as np


def weights(K):
    return [Fraction(2, 3**k) for k in range(1, K)] + [Fraction(1, 3**(K-1))]


def build(K):
    w = weights(K)
    rows = []
    for x in w:
        rows.append([math.sqrt(float(x)), 0.0, 0.0])
    rows += [
        [0.0, 1 / math.sqrt(2), 0.0],
        [0.0, 1 / math.sqrt(2), 0.0],
        [0.0, 0.0, 1 / math.sqrt(2)],
        [0.0, 0.0, 1 / math.sqrt(2)],
    ]
    U = np.array(rows, dtype=float)
    Lam = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    A = U @ Lam @ U.T
    return w, U, Lam, A


for K in range(2, 13):
    w, U, Lam, A = build(K)
    assert sum(w, Fraction(0)) == 1
    rem = Fraction(1)
    lev = []
    for x in w:
        lev.append(x / rem)
        rem -= x
        if rem == 0:
            break
    assert all(q == Fraction(2, 3) for q in lev[:-1])
    assert lev[-1] == 1
    assert np.linalg.norm(U.T @ U - np.eye(3), ord=np.inf) < 1e-12
    ev = np.linalg.eigvalsh(A)
    nz = ev[np.abs(ev) > 1e-9]
    assert np.allclose(nz, np.array([-1.0, 1.0, 1.0]), atol=1e-10)
    piv = np.diag(A)[:K]
    assert np.max(np.abs(piv)) < 1e-12
    assert np.max(np.abs(A[:K, :K])) < 1e-12
    print(
        f"K={K:2d} sum_w={float(sum(w)):.1f} first={float(lev[0]):.12f} "
        f"last={float(lev[-1]):.1f} spectrum={nz.tolist()}"
    )

print(f"partner_top_constant={97 * 128**0.25:.12f}")
print(f"conditional_diffuse_constant={12 * math.e:.12f}")
print(f"three_bank_constant={8 * math.sqrt(2):.12f}")
print("STATUS=PASS")
