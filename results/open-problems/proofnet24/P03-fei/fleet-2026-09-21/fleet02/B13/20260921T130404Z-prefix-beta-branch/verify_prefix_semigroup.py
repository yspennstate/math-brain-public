#!/usr/bin/env python3
"""
Self-check for B13 prefix-shadow / Beta-semigroup identities.

The theorem-sized claims in REPORT.md are proved there.  This program checks the
finite algebra independently for all Boolean functions through n=4 (mod global
sign), and prints two explicit Boolean stress families.

No external packages are used.
"""
from fractions import Fraction
from math import comb, factorial, log2

def pc(x):
    return x.bit_count()

def fwht_int(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for s in range(0, len(a), 2*h):
            for j in range(s, s+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def spectral(vals, n):
    w = fwht_int(vals)
    den = (1 << n) ** 2
    return [Fraction(x*x, den) for x in w]

def prefix_shadow(p, n, A):
    a = pc(A)
    return sum(
        (p[B] / comb(pc(B), a)
         for B in range(1 << n) if (B & A) == A),
        Fraction(0)
    )

def influence(p):
    return sum((pc(A) * p[A] for A in range(len(p))), Fraction(0))

def local_mi(p, v, n, A):
    """I(next coordinate ; final set | prefix A, continue), in bits."""
    a = pc(A)
    w = v[A] - p[A]
    if not w:
        return None
    r = []
    for i in range(n):
        if not ((A >> i) & 1):
            q = v[A | (1 << i)] / Fraction(a + 1)
            if q:
                r.append(float(q / w))
    hnext = -sum(x * log2(x) for x in r)
    cond = 0.0
    for B, pb in enumerate(p):
        if B != A and pb and (B & A) == A:
            b = pc(B)
            mass = float((pb / comb(b, a)) / w)
            cond += mass * log2(b - a)
    return hnext - cond

def beta_coeff(a, d):
    # integral_0^1 (1-s)^a s^(d-1) ds = a!(d-1)!/(a+d)!
    assert d >= 1
    return Fraction(factorial(a) * factorial(d-1), factorial(a+d))

def main():
    prefix_checks = 0
    beta_checks = 0
    max_mi = {}

    for n in range(1, 5):
        N = 1 << n
        best = -1.0
        best_A = None
        # Quotient global output negation by fixing f(0)=+1.
        for mask in range(1 << (N-1)):
            vals = [1] + [
                -1 if (mask >> (x-1)) & 1 else 1
                for x in range(1, N)
            ]
            p = spectral(vals, n)
            v = [prefix_shadow(p, n, A) for A in range(N)]
            I = influence(p)

            # Global continuation mass identity: sum_A (v_A-p_A)=I.
            assert sum((v[A]-p[A] for A in range(N)), Fraction(0)) == I

            for A in range(N):
                a = pc(A)
                w = v[A] - p[A]

                # Child-flow identity:
                # sum_{i notin A} v_{A+i}=(a+1)(v_A-p_A).
                child = sum(
                    (v[A | (1 << i)]
                     for i in range(n) if not ((A >> i) & 1)),
                    Fraction(0)
                )
                assert child == Fraction(a+1) * w
                prefix_checks += 1

                mi = local_mi(p, v, n, A)
                if mi is not None and mi > best:
                    best, best_A = mi, A

                # Coefficient-level Beta identity behind the semigroup formula.
                for i in range(n):
                    if (A >> i) & 1:
                        continue
                    Ai = A | (1 << i)
                    for B in range(N):
                        if (B & Ai) != Ai:
                            continue
                        d = pc(B) - a
                        lhs = Fraction(1, (a+1) * comb(pc(B), a+1))
                        rhs = beta_coeff(a, d)
                        assert lhs == rhs
                        beta_checks += 1

        max_mi[n] = (best, best_A)

    print("ALL_EXACT_PREFIX_IDENTITIES_PASS")
    print("prefix_checks", prefix_checks)
    print("beta_coefficient_checks", beta_checks)
    for n in sorted(max_mi):
        print("max_local_MI_n%d %.15f prefix_mask=%d" %
              (n, max_mi[n][0], max_mi[n][1]))

    print("ONE_POINT_DEFECT_PREFIX_GRANULARITY_RATIO")
    for n in range(2, 11):
        # For |A|=1:
        # v_A / |fhat(A)| = (2^n-1)/(n 2^(n-1)).
        r = Fraction((1 << n)-1, n * (1 << (n-1)))
        print(n, str(r), "%.12f" % float(r))

    print("ODD_MAJORITY_ROOT_MI_JENSEN_LOWER_BOUND")
    for n in (13, 151, 251):
        c = comb(n-1, (n-1)//2)
        inf_i = Fraction(c, 1 << (n-1))
        I = Fraction(n) * inf_i
        lb = -log2(float(inf_i))  # log2(n/I)
        print(n, "I=%.12f" % float(I), "MI_root>=%.12f" % lb)

if __name__ == "__main__":
    main()
