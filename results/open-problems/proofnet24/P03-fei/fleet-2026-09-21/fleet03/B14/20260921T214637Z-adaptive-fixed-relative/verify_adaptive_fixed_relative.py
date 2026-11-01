#!/usr/bin/env python3
"""Self-check for the B14 adaptive-short-circuit test of the fixed-relative FEI obstruction.

This is diagnostic code for a structured Boolean family, not a proof of full FEI.
It uses only Python's standard library.  The formulas are the Fourier category
formulas written in REPORT.md; no truth table of the majority-substituted family
is materialized.
"""
from decimal import Decimal, getcontext
from math import comb

getcontext().prec = 120
D = Decimal
TWO = D(2)
ONE = D(1)
LN2 = TWO.ln()


def p2neg(k: int) -> Decimal:
    return TWO ** D(-k)


def log2(x: Decimal) -> Decimal:
    return x.ln() / LN2


def entropy_from_coeff_categories(categories):
    H = D(0)
    mass = D(0)
    for a, count in categories:
        a = D(a)
        m = a * a
        c = D(count)
        mass += c * m
        if m:
            H += c * m * (-log2(m))
    return H, mass


def H_match(s: int, M: int):
    """Entropy after a matched prefix, with s defining controls left."""
    q = p2neg(s)
    d = p2neg(M)
    cats = []
    # W=0, x-frequency present / absent.
    cats.append((q + d * (ONE - q), 1))
    if 2**s - 1:
        cats.append((q * (ONE - d), 2**s - 1))
    cats.append((ONE - q - d * (ONE - q) - d * s, 1))
    if s:
        cats.append((-q * (ONE - d) + d, s))
    other_T = max(0, 2**s - 1 - s)
    if other_T:
        cats.append((-q * (ONE - d), other_T))

    # W != 0, grouped by the Hamming weight h on the active selector bits.
    extra = M - s
    for h in range(s + 1):
        mult = 2**extra - (1 if h == 0 else 0)
        if mult <= 0:
            continue
        count = comb(s, h) * mult
        cats.append((d * (ONE - q), count))
        if 2**s - 1:
            cats.append((-d * q, count * (2**s - 1)))
        cats.append((-d * ((ONE - q) + (s - 2*h)), count))
        if s - h:
            cats.append((d * (q + ONE), count * (s - h)))
        if h:
            cats.append((d * (q - ONE), count * h))
        if other_T:
            cats.append((d * q, count * other_T))
    return entropy_from_coeff_categories(cats)


def H_mismatch(s: int, M: int):
    """Entropy after the first mismatch, with s untouched controls left."""
    d = p2neg(M)
    cats = [(d, 1), (ONE - d * (s + 3), 1)]
    if s:
        cats.append((d, s))
    inactive_other = M - s - 1
    for h in range(s + 1):
        for eps in (0, 1):
            sign_special = 1 - 2*eps
            mult = 2**inactive_other - (1 if h == 0 and eps == 0 else 0)
            if mult <= 0:
                continue
            count = comb(s, h) * mult
            cats.append((d, count))
            cats.append((-d * (1 + 2*sign_special + s - 2*h), count))
            if s - h:
                cats.append((d, count * (s - h)))
            if h:
                cats.append((-d, count * h))
    return entropy_from_coeff_categories(cats)


def h2(x: Decimal) -> Decimal:
    if x == 0 or x == 1:
        return D(0)
    return -(x * log2(x) + (ONE - x) * log2(ONE - x))


def jfun(p: Decimal) -> Decimal:
    x = D('0.5') + (p * (ONE - p)).sqrt()
    return ONE - h2(x)


def infl_match(s: int, M: int):
    q = p2neg(s)
    d = p2neg(M)
    # x; each remaining z; active w directions; other w directions.
    return (
        q + (ONE - q) * d,
        q + d - 3*q*d,
        d * (s - q),
        d * (s + 1 - q),
    )


def infl_mismatch(s: int, M: int):
    d = p2neg(M)
    # x; each remaining z; active w; special w; other w.
    return d, d, d*(s+2), d*(s+1), d*(s+3)


def Phi_match(s: int, M: int):
    px, pz, pwa, pwi = infl_match(s, M)
    return jfun(px) + s*jfun(pz) + s*jfun(pwa) + (M-s)*jfun(pwi)


def Phi_mismatch(s: int, M: int):
    px, pz, pwa, pws, pwi = infl_mismatch(s, M)
    return (jfun(px) + s*jfun(pz) + s*jfun(pwa) + jfun(pws)
            + (M-s-1)*jfun(pwi))


def folded(p: Decimal) -> Decimal:
    return min(p, ONE-p)


def J_match(s: int, M: int):
    px, pz, pwa, pwi = infl_match(s, M)
    return folded(px) + s*folded(pz) + s*folded(pwa) + (M-s)*folded(pwi)


def J_mismatch(s: int, M: int):
    px, pz, pwa, pws, pwi = infl_mismatch(s, M)
    return (folded(px) + s*folded(pz) + s*folded(pwa) + folded(pws)
            + (M-s-1)*folded(pwi))


def stopped_stats(r: int):
    M = r + 4
    H0, mass0 = H_match(r, M)
    P0 = Phi_match(r, M)
    J0 = J_match(r, M)
    EH = EP = EJ = D(0)
    max_mass_error = abs(mass0 - ONE)
    for t in range(1, r+1):
        # first mismatch at query t; this leaf has probability 2^{-t}
        s = r - t
        w = p2neg(t)
        Hm, massm = H_mismatch(s, M)
        max_mass_error = max(max_mass_error, abs(massm - ONE))
        EH += w * Hm
        EP += w * Phi_mismatch(s, M)
        EJ += w * J_mismatch(s, M)
    # all-match leaf has probability 2^{-r} and is exactly chi_x, so H=Phi=J=0.
    dH = H0 - EH
    dP = P0 - EP
    dF = dH - dP
    dJ = J0 - EJ

    q = p2neg(r)
    delta = p2neg(r+4)
    exact_drift = (r+1)*q - 3*r*q*delta + 2*delta*(ONE-q)
    return {
        'r': r,
        'delta_H_over_delta_J': dH/dJ,
        'delta_F_over_delta_J': dF/dJ,
        'delta_J': dJ,
        'exact_drift': exact_drift,
        'drift_error': dJ-exact_drift,
        'max_parseval_error': max_mass_error,
    }


def main():
    rows = [2, 3, 4, 5, 6, 7, 8, 12, 16, 24, 32, 48, 64, 80, 100]
    print('r  DeltaH/DeltaJ  DeltaF/DeltaJ  drift_error  max_parseval_error')
    for r in rows:
        s = stopped_stats(r)
        print(
            f"{r:3d} "
            f"{s['delta_H_over_delta_J']:.18f} "
            f"{s['delta_F_over_delta_J']:.18f} "
            f"{s['drift_error']:.2E} "
            f"{s['max_parseval_error']:.2E}"
        )


if __name__ == '__main__':
    main()
