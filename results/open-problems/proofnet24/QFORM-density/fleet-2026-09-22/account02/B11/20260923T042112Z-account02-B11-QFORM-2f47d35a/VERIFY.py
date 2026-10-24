import math
import numpy as np


def build(m, eps):
    off = math.sqrt(1.0 + eps * eps)
    B = np.array([[eps, off], [off, -eps]], dtype=float)
    b = np.ones(m, dtype=float) / math.sqrt(m)
    A = np.zeros((m + 2, m + 2), dtype=float)
    A[:2, :2] = B
    A[2:, 2:] = np.outer(b, b)
    return A, B


def check(m, eps):
    A, B = build(m, eps)
    s = math.sqrt(1.0 + 2.0 * eps * eps)
    eig = np.linalg.eigvalsh(A)
    expected = np.array([-s] + [0.0] * (m - 1) + [1.0, s])
    assert np.max(np.abs(eig - expected)) < 1e-10

    detBabs = 1.0 + 2.0 * eps * eps
    assert abs(np.linalg.det(B) + detBabs) < 1e-12

    # Every invertible physical 3x3 principal block must use both pair
    # coordinates and one bank coordinate.  Its determinant is det(B)/m.
    max_other = 0.0
    det_pair_bank = []
    n = m + 2
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                I = [i, j, k]
                d = float(np.linalg.det(A[np.ix_(I, I)]))
                if i == 0 and j == 1 and k >= 2:
                    det_pair_bank.append(d)
                else:
                    max_other = max(max_other, abs(d))
    assert max_other < 1e-10
    assert max(abs(d + detBabs / m) for d in det_pair_bank) < 1e-10

    aggregate = 16.0 * math.sqrt(60.0) * detBabs ** (-0.25)
    one_sheet = math.pi * math.sqrt(2.0)
    bank_pivot = 16.0 * math.sqrt(30.0) * (detBabs / (m * m)) ** (-0.25)
    if eps > 0:
        minority = 2.0 * math.sqrt(math.pi) * (eps * detBabs / m) ** (-0.25)
        zero = None
    else:
        minority = None
        zero = 3.0 * 2.0 ** (2.0 / 3.0) * (m / detBabs) ** (1.0 / 3.0)
    return eig, aggregate, one_sheet, bank_pivot, minority, zero


for eps in (0.0, 0.01, 0.1, 0.5):
    eig, aggregate, one_sheet, bank_pivot, minority, zero = check(64, eps)
    nz = eig[np.abs(eig) > 1e-9]
    print(f"eps={eps:g} nonzero_eigs={nz.tolist()}")
    print(f"  aggregate={aggregate:.12f} one_sheet={one_sheet:.12f} bank_pivot={bank_pivot:.12f}")
    if minority is not None:
        print(f"  minority_local={minority:.12f}")
    if zero is not None:
        print(f"  zero_local={zero:.12f}")

print("QFORM_BANKED_PAIR_SQUARE_INTERPOLATION_CHECK_PASS")
