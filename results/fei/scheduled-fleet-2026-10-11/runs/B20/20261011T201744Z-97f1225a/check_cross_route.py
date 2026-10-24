#!/usr/bin/env python3
"""Rational-interval check for the B05 -> B09 cross-route payment.

The proof is analytic.  This checker evaluates the exact four-class B05 packet
law and rigorously encloses logarithms by the atanh series.  No floating-point
quantity participates in an assertion.
"""

from fractions import Fraction as Q


def ln_interval(x, terms=48):
    assert x > 0
    exp, y = 0, x
    while y >= 2:
        y /= 2
        exp += 1
    while y < 1:
        y *= 2
        exp -= 1

    def core(z):
        u = (z - 1) / (z + 1)
        au = abs(u)
        acc, power = Q(0), u
        for j in range(terms):
            acc += power / (2 * j + 1)
            power *= u * u
        center = 2 * acc
        tail = 2 * au ** (2 * terms + 1) / ((2 * terms + 1) * (1 - au * au))
        return center - tail, center + tail

    l2, u2 = core(Q(2))
    ly, uy = core(y)
    if exp >= 0:
        return ly + exp * l2, uy + exp * u2
    return ly + exp * u2, uy + exp * l2


LN2 = ln_interval(Q(2))


def log2_interval(x):
    nlo, nhi = ln_interval(x)
    vals = (nlo / LN2[0], nlo / LN2[1], nhi / LN2[0], nhi / LN2[1])
    return min(vals), max(vals)


def add(X, Y): return X[0] + Y[0], X[1] + Y[1]
def smul(c, X): return (c * X[0], c * X[1]) if c >= 0 else (c * X[1], c * X[0])


LOG2E = Q(1) / LN2[1], Q(1) / LN2[0]


def entropy_term(q, e):
    if e == 0 or e == q:
        return Q(0), Q(0)
    # q h2(e/q) = e log2(q/e) + (q-e) log2(q/(q-e)).
    return add(smul(e, log2_interval(q / e)), smul(q - e, log2_interval(q / (q - e))))


def classes(k):
    delta = Q(1, 1 << k)
    p = delta * delta
    d = p * delta
    out = []

    # Nonempty data coefficient sign classes.  A quadratic bent truth table
    # has 2^(k-1)+2^(k/2-1) positive and the complementary number negative.
    nplus = (1 << (k - 1)) + (1 << (k // 2 - 1))
    # The empty coefficient is positive for the chosen standard bent phase.
    nplus_nonempty = nplus - 1
    nminus_nonempty = (1 << k) - nplus
    controls = 1 << (2 * k)
    root_delta = Q(1, 1 << (k // 2))
    for sign, mult in ((1, nplus_nonempty * controls), (-1, nminus_nonempty * controls)):
        midpoint = p * (sign * root_delta - delta)
        e = d * d
        q = midpoint * midpoint + e
        out.append((mult, q, e, "nonempty-data"))

    # Empty data, nonempty control modes.
    midpoint = p * (root_delta - 1 - delta)
    e = d * d
    q = midpoint * midpoint + e
    out.append((controls - 1, q, e, "empty-data/nonempty-control"))

    # All-empty packet.
    midpoint = 1 + p * (root_delta - 1 - delta)
    q = midpoint * midpoint + e
    out.append((1, q, e, "all-empty"))
    return delta, p, d, out


def main():
    print("B20 CROSS-ROUTE RATIONAL-INTERVAL CERTIFICATE")
    print("randomness: NONE; atanh terms: 48")
    count = 0
    for k in range(4, 42, 2):
        delta, p, d, cs = classes(k)
        mass = sum(Q(mult) * q for mult, q, _, _ in cs)
        mismatch = sum(Q(mult) * e for mult, _, e, _ in cs)
        assert mass == 1
        assert mismatch == d
        count += 2

        L = (Q(0), Q(0))
        for mult, q, e, _ in cs:
            L = add(L, smul(Q(mult), entropy_term(q, e)))
        Delta = smul(delta, log2_interval((1 - delta) / delta))
        payment = add(smul(p, Delta), (3 * d, 3 * d))
        assert L[1] < payment[0]
        count += 1

        # Check the explicit classwise upper bound used in the proof.
        upper = (1 - delta) * d * (k + 1) + delta * d * (2 * k + 1) + d * d * (6 * k + 1)
        upper_I = add((upper, upper), smul((1 - delta) * d + delta * d + d * d, LOG2E))
        assert L[1] <= upper_I[1]
        count += 1

        if k in (4, 6, 10, 20, 40):
            ratio = L[0] / d, L[1] / d
            paid = payment[0] / d, payment[1] / d
            print(f"k={k:2d}: L/d in [{float(ratio[0]):.12f}, {float(ratio[1]):.12f}], "
                  f"[p Delta(delta)+3d]/d in [{float(paid[0]):.12f}, {float(paid[1]):.12f}] PASS")

    print(f"exact/rational-interval assertions: {count}; failed: 0")


if __name__ == "__main__":
    main()
