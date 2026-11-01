#!/usr/bin/env python3
"""Exact finite-width FEI certificate for the B05 aligned-kernel theorem.

The Walsh transforms and influences are integer/rational exact.  Logarithms
are enclosed by a positive atanh series after binary range reduction.
"""

from collections import Counter, defaultdict
from fractions import Fraction


TERMS = 48


def ln_interval(q: Fraction, terms: int = TERMS):
    """Rigorous interval for ln(q), for 1 <= q < 2."""
    assert Fraction(1) <= q <= Fraction(2)
    z = (q - 1) / (q + 1)
    partial = Fraction(0)
    power = z
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= z * z
    lo = 2 * partial
    # Positive tail: sum_{j>=N} z^(2j+1)/(2j+1)
    # <= z^(2N+1)/((2N+1)(1-z^2)).
    rem = 2 * power / ((2 * terms + 1) * (1 - z * z))
    return lo, lo + rem


LN2 = ln_interval(Fraction(2))


def log2_interval(q: Fraction):
    """Rigorous interval for log_2(q), q >= 1."""
    assert q >= 1
    if q == 1:
        return Fraction(0), Fraction(0)
    k = 0
    y = q
    while y >= 2:
        y /= 2
        k += 1
    yl, yu = ln_interval(y)
    dl, du = LN2
    return Fraction(k) + yl / du, Fraction(k) + yu / dl


def fwht(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def profile(values, n):
    w = fwht(values)
    den = 1 << (2 * n)
    squares = tuple(sorted(x * x for x in w if x))
    influence_num = sum(s.bit_count() * w[s] * w[s] for s in range(1 << n))
    return squares, influence_num, den


def ratio_interval(sig):
    squares, influence_num, den = sig
    assert influence_num > 0
    hlo = Fraction(0)
    hhi = Fraction(0)
    for a in squares:
        p = Fraction(a, den)
        lo, hi = log2_interval(Fraction(den, a))
        hlo += p * lo
        hhi += p * hi
    infl = Fraction(influence_num, den)
    return hlo / infl, hhi / infl


def enumerate_dimension(n):
    N = 1 << n
    profiles = Counter()
    representatives = 0
    for mask in range(1 << (N - 1)):
        # Fix value at input 0 to +1; the omitted global complements have the
        # same squared spectrum and influence.
        vals = [1]
        vals.extend(-1 if (mask >> (j - 1)) & 1 else 1 for j in range(1, N))
        sig = profile(vals, n)
        if sig[1] != 0:
            profiles[sig] += 1
        representatives += 1

    # One-point defect target, with the defect away from the fixed input 0.
    target_vals = [1] * N
    target_vals[-1] = -1
    target = profile(target_vals, n)
    target_iv = ratio_interval(target)
    assert target in profiles

    equal_target = 0
    runner_upper = Fraction(-1)
    runner_sig = None
    for sig, count in profiles.items():
        iv = ratio_interval(sig)
        if sig == target:
            equal_target += count
        else:
            if iv[1] > runner_upper:
                runner_upper = iv[1]
                runner_sig = sig
            assert iv[1] < target_iv[0], (n, iv, target_iv)

    return {
        "n": n,
        "representatives": representatives,
        "nonconstant_representatives": sum(profiles.values()),
        "profiles": len(profiles),
        "target_count": equal_target,
        "target_interval": target_iv,
        "runner_upper": runner_upper,
        "runner_signature": runner_sig,
    }


def direct_formula_checks():
    # Closed forms for the point-defect maximizers in dimensions 2,3,4.
    expected = {
        2: (Fraction(1, 4), 4, Fraction(1)),
        3: (Fraction(9, 16), 8, Fraction(3, 4)),
        4: (Fraction(49, 64), 16, Fraction(1, 2)),
    }
    for n, (big_mass, atoms, influence) in expected.items():
        vals = [1] * (1 << n)
        vals[-1] = -1
        squares, inf_num, den = profile(vals, n)
        assert len(squares) == atoms
        assert Fraction(max(squares), den) == big_mass
        assert Fraction(inf_num, den) == influence


def aligned_shield_checks():
    """Direct integer-Walsh checks of H-law inputs and influence lower bound.

    We check every D for r+t <= 4, with M0 the r x r identity.  Entropy is
    represented only through the exact squared-mass profile: the asserted
    product law says that every fiber coefficient is repeated 2^r times and
    scaled by 2^{-2r}.
    """
    checked = 0
    for r in range(1, 3):
        for t in range(0, 5 - r):
            yz = r + t
            for mask in range(1 << ((1 << yz) - 1)):
                d = [1]
                d.extend(-1 if (mask >> (j - 1)) & 1 else 1
                         for j in range(1, 1 << yz))

                # P(x,u,z)=(-1)^{x.u}D(u,z), with x,u both r bits.
                vals = []
                for xu_z in range(1 << (2 * r + t)):
                    z = xu_z & ((1 << t) - 1)
                    u = (xu_z >> t) & ((1 << r) - 1)
                    x = xu_z >> (t + r)
                    phase = (x & u).bit_count() & 1
                    Dval = d[(u << t) | z]
                    vals.append((-1 if phase else 1) * Dval)
                full_w = fwht(vals)
                full_sq = sorted(v * v for v in full_w if v)

                predicted = []
                for u in range(1 << r):
                    fiber = d[u << t:(u + 1) << t]
                    fw = fwht(fiber)
                    for q in fw:
                        if q:
                            # Full unnormalized coefficient is 2^r q and is
                            # repeated over all 2^r u-frequency choices.
                            predicted.extend([(1 << (2 * r)) * q * q] * (1 << r))
                assert full_sq == sorted(predicted)

                # Direct physical edge influence is at least r plus the
                # average z-influence of the Boolean fibers.
                nfull = 2 * r + t
                edge_infl = Fraction(0)
                for j in range(nfull):
                    changes = sum(vals[a] != vals[a ^ (1 << j)]
                                  for a in range(1 << nfull))
                    edge_infl += Fraction(changes, 1 << nfull)
                fiber_infl = Fraction(0)
                if t:
                    for u in range(1 << r):
                        fiber = d[u << t:(u + 1) << t]
                        for j in range(t):
                            changes = sum(fiber[z] != fiber[z ^ (1 << j)]
                                          for z in range(1 << t))
                            fiber_infl += Fraction(changes, 1 << (r + t))
                assert edge_infl >= r + fiber_infl
                checked += 1
    return checked


def main():
    direct_formula_checks()
    results = [enumerate_dimension(n) for n in range(1, 5)]
    shield_cases = aligned_shield_checks()
    print("B05 A023 aligned-width certificate")
    print(f"atanh terms: {TERMS}")
    for row in results:
        lo, hi = row["target_interval"]
        margin = lo - row["runner_upper"] if row["runner_upper"] >= 0 else None
        print(
            "n={n}: reps={representatives}, nonconstant={nonconstant_representatives}, "
            "profiles={profiles}, maximizer_reps={target_count}, "
            "C_interval=[{lo:.18f},{hi:.18f}], width={width:.3e}, "
            "runner_upper={ru:.18f}, margin={margin}".format(
                **row, lo=float(lo), hi=float(hi), width=float(hi - lo),
                ru=float(row["runner_upper"]),
                margin="n/a" if margin is None else f"{float(margin):.18f}"
            )
        )
    print(f"direct aligned-shield cases: {shield_cases}")
    print("all exact transforms, rational intervals, maxima, and shield identities passed")


if __name__ == "__main__":
    main()
