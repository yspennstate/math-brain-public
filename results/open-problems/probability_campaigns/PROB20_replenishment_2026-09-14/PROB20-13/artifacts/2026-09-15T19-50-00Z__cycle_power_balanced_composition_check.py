"""Exact rational checker for PROB20-13 cycle-power report.

Verifies the explicit balanced-composition distributions used for k=3 and
k=4, closes them under the induction increments, and checks the resulting
closed forms and the elementary 2D comparison on a finite range.

This is a reproducibility check only; the Markdown report contains the proof.
"""

from fractions import Fraction as F


def expected_counts(dist, k):
    out = [F(0) for _ in range(k)]
    total = F(0)
    for p, comp in dist:
        total += p
        for s in comp:
            assert 1 <= s <= k
            out[s - 1] += p
    assert total == 1
    return out


def combine(d1, d2):
    return [(p * q, c1 + c2) for p, c1 in d1 for q, c2 in d2]


MU3 = {
    3: [(F(1, 2), (3,)), (F(1, 2), (1, 2))],
    4: [(F(1, 3), (2, 2)), (F(2, 3), (1, 3))],
    5: [
        (F(1, 2), (2, 3)),
        (F(1, 6), (1, 2, 2)),
        (F(1, 3), (1, 1, 3)),
    ],
    6: [(F(1), (1, 2, 3))],
}

MU4 = {
    4: [
        (F(2, 5), (4,)),
        (F(1, 5), (2, 2)),
        (F(2, 5), (1, 3)),
    ],
    5: [(F(1, 2), (1, 4)), (F(1, 2), (2, 3))],
    6: [
        (F(1, 5), (3, 3)),
        (F(3, 5), (2, 4)),
        (F(1, 5), (1, 1, 1, 3)),
    ],
    7: [
        (F(7, 10), (3, 4)),
        (F(1, 10), (1, 2, 2, 2)),
        (F(1, 5), (1, 1, 1, 2, 2)),
    ],
}


def mu3(r):
    assert r >= 3
    if r in MU3:
        return MU3[r]
    base = 4 + ((r - 4) % 3)
    dist = MU3[base]
    for _ in range((r - base) // 3):
        dist = combine(dist, MU3[3])
    return dist


def mu4(r):
    assert r >= 4
    if r in MU4:
        return MU4[r]
    base = 4 + ((r - 4) % 4)
    dist = MU4[base]
    for _ in range((r - base) // 4):
        dist = combine(dist, MU4[4])
    return dist


def mean_cycle_distance(n):
    if n % 2 == 0:
        return F(n, 4)
    return F(n * n - 1, 4 * n)


def ceil_div(a, b):
    return (a + b - 1) // b


def verify_balanced_distributions(limit=80):
    for r in range(4, limit + 1):
        e = expected_counts(mu3(r), 3)
        target = F(r, 6)
        assert e == [target] * 3, ("k=3", r, e, target)

    for r in range(4, limit + 1):
        e = expected_counts(mu4(r), 4)
        target = F(r, 10)
        assert e == [target] * 4, ("k=4", r, e, target)


def verify_closed_forms(nmax=200):
    for k in (3, 4):
        for n in range(2 * k + 1, nmax + 1):
            bar = mean_cycle_distance(n)
            flow = F(4, k + 1) * bar

            # At n=2k+1 the power is the complete graph K_n.
            if n == 2 * k + 1:
                assert flow == F(2 * (n - 1), n)
                continue

            # For noncomplete cycle powers the archived lemma gives tau_rel >= 1.
            # So checking flow <= 2D verifies the elementary final comparison.
            R = n // 2
            diameter = ceil_div(R, k)
            assert flow <= 2 * diameter, (k, n, flow, diameter)


def main():
    verify_balanced_distributions()
    verify_closed_forms()
    print("exact balanced-composition checks passed")
    print("k=3: F(C_n^3) = mean ordinary-cycle distance")
    print("k=4: F(C_n^4) = (4/5) mean ordinary-cycle distance")


if __name__ == "__main__":
    main()
