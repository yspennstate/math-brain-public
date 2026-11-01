#!/usr/bin/env python3
"""Exact-support checker for the B12 Palm-insertion/co-sensitivity report.

The Boolean family is a selector between two disjoint parity blocks X,Y of
size m. Its spectral law has exactly four atoms X, X+z, Y, Y+z, each mass 1/4.
All combinatorial masses are exact Fraction objects. Information quantities
are evaluated with 70-digit Decimal logarithms.
"""
from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
import math

getcontext().prec = 70
LN2 = Decimal(2).ln()


def D(x: Fraction) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)


def log2q(x: Fraction) -> Decimal:
    assert x > 0
    return D(x).ln() / LN2


def d2_bern(a: Fraction, b: Fraction) -> Decimal:
    if a == 0:
        return -log2q(1 - b)
    if a == 1:
        return -log2q(b)
    return D(a) * log2q(a / b) + D(1 - a) * log2q((1 - a) / (1 - b))


def run(m: int):
    n = 2 * m + 1
    z = 2 * m
    X = sum(1 << i for i in range(m))
    Y = sum(1 << (m + i) for i in range(m))
    atoms = [X, X | (1 << z), Y, Y | (1 << z)]

    # Spectral mass is 1/4 on each of the four atoms.
    v = defaultdict(Fraction)
    for T in atoms:
        k = T.bit_count()
        A = T
        while True:
            a = A.bit_count()
            v[A] += Fraction(1, 4) / math.comb(k, a)
            if A == 0:
                break
            A = (A - 1) & T

    I = Fraction(2 * m + 1, 2)
    q_label = Fraction(1, n)  # every coordinate has influence 1/2
    label_mass = [Fraction(0) for _ in range(n)]
    total_edge = Fraction(0)
    Dseq = Decimal(0)
    Rseq = Decimal(0)

    # Edge law w(A,i)=v(A+i)/(a+1).
    for A, va in list(v.items()):
        a = A.bit_count()
        children = []
        c = Fraction(0)
        for i in range(n):
            if A & (1 << i):
                continue
            B = A | (1 << i)
            vb = v.get(B, Fraction(0))
            if vb:
                w = vb / (a + 1)
                children.append((i, w, vb))
                c += w
        if c:
            for i, w, vb in children:
                total_edge += w
                label_mass[i] += w
                Dseq += D(w) * log2q((w / c) / q_label)
                Rseq += D(w) * log2q(va / vb)

    assert total_edge == I
    assert all(x == Fraction(1, 2) for x in label_mass)

    # For a nonselector coordinate j,
    # beta_j=P(j lies in the predecessor prefix)=(2m-1)/(4(2m+1)).
    # For selector z, beta_z=m/(2(2m+1)).
    beta_b = Fraction(2 * m - 1, 4 * (2 * m + 1))
    beta_z = Fraction(m, 2 * (2 * m + 1))

    # Tempting but false strengthening: sum every j!=i binary divergence.
    S_naive = (
        Decimal(m)
        * (
            Decimal(m - 1) * d2_bern(Fraction(1, 2), beta_b)
            + Decimal(m) * d2_bern(Fraction(0), beta_b)
            + d2_bern(Fraction(1, 4), beta_z)
        )
        + Decimal(m) * d2_bern(Fraction(1, 4), beta_b)
    )

    # Rigorous one-bit data-processing lower bound: each label i may choose
    # one witness g(i), including self (whose true predecessor bit is 0).
    block_best = max(
        d2_bern(Fraction(0), beta_b),
        d2_bern(Fraction(1, 2), beta_b),
        d2_bern(Fraction(1, 4), beta_z),
    )
    selector_best = max(
        d2_bern(Fraction(0), beta_z),
        d2_bern(Fraction(1, 4), beta_b),
    )
    D_adapt = Decimal(m) * block_best + Decimal(1) / 2 * selector_best

    return {
        "m": m,
        "n": n,
        "I": D(I),
        "Dseq_over_I": Dseq / D(I),
        "naive_pair_sum_over_I": S_naive / D(I),
        "adaptive_one_bit_over_I": D_adapt / D(I),
        "naive_over_Dseq": S_naive / Dseq,
        "Rseq_over_I": Rseq / D(I),
        "prefix_states": len(v),
        "beta_block": beta_b,
        "beta_selector": beta_z,
    }


def main():
    print("m n I Dseq/I naive_sum/I adaptive/I naive/Dseq Rseq/I states beta_b beta_z")
    for m in range(2, 11):
        r = run(m)
        print(
            r["m"], r["n"], r["I"],
            r["Dseq_over_I"], r["naive_pair_sum_over_I"],
            r["adaptive_one_bit_over_I"], r["naive_over_Dseq"],
            r["Rseq_over_I"], r["prefix_states"],
            f'{r["beta_block"].numerator}/{r["beta_block"].denominator}',
            f'{r["beta_selector"].numerator}/{r["beta_selector"].denominator}',
        )


if __name__ == "__main__":
    main()
