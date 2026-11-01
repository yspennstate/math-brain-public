"""Independent exact controls for the P0193 two-atom kernel lemma."""

from fractions import Fraction as F


def kernel(C, y, c):
    return (C * y - c) / (2 * (y * y - 2 * c * C * y + c * c + C * C - 1))


for C in [F(2), F(201, 100), F(21, 10), F(5, 2), F(3), F(101, 20)]:
    m = 1 / (2 * (C + 1))
    M = C * C / (8 * (C * C - 1))
    assert M - m == (C - 2) ** 2 / (8 * (C * C - 1))
    if C == 2:
        assert m == M
        print("C=2: boundary has coincident maximum and center levels")
        continue
    h = (m + M) / 2
    q = C - 1 / (2 * h)
    c0 = min(F(0), (q - 1) / 2)
    ystar = C - 2 / C
    assert -1 < c0 <= 0 and c0 < q and ystar > 1
    assert kernel(C, 1, c0) < h < M <= kernel(C, ystar, c0)
    assert kernel(C, 1000, c0) < h
    print(f"C={C}: center<h<peaks; c0={c0}; two positive-y roots and four u roots")
