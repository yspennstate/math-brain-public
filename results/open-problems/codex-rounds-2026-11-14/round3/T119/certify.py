#!/usr/bin/env python3
"""Exact rational certificate of Harangi's four-atom cubic 2-RSB witness.

No third-party modules, binary floating-point, log, or exp enter the
certificate. See PROOF.md for the bounds implemented here.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, product
from math import factorial
import os
import resource
import signal
import time


def floor_root(n, degree):
    """Return floor(n**(1/degree)) by integer bisection."""
    assert n >= 0 and degree > 0
    lo, hi = 0, 1 << ((n.bit_length() + degree - 1) // degree)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**degree <= n:
            lo = mid
        else:
            hi = mid
    assert lo**degree <= n < (lo + 1)**degree
    return lo


def multiplicity(indices):
    answer = factorial(len(indices))
    for i in set(indices):
        answer //= factorial(indices.count(i))
    return answer


def terms(p, q, lam, arity):
    """Yield exact weights and bases; count permutations explicitly."""
    for ix in combinations_with_replacement(range(len(p)), arity):
        weight = F(multiplicity(ix))
        for i in ix:
            weight *= p[i]
        if arity == 3:
            base = F(1)
            for i in ix:
                base *= 1 - q[i]
            base = 1 + (lam - 1) * base
        elif arity == 2:
            i, j = ix
            base = 1 - (1 - 1 / lam) * q[i] * q[j]
        else:
            raise ValueError("only cubic stars and edges")
        yield weight, base


class Certificate:
    def __init__(self, digits=18, series_terms=48):
        assert 10 <= digits <= 30
        assert 24 <= series_terms <= 96
        self.scale = 10**digits
        self.series_terms = series_terms
        self.root_checks = 0
        self.log2 = self.log_reduced(F(2))

    @lru_cache(maxsize=128)
    def power(self, x):
        """Enclose x**(557/1000) by exact integer comparisons."""
        assert x > 0
        a, b = x.numerator, x.denominator
        right = self.scale**1000 * a**557
        denominator = b**557
        target = right // denominator
        root = floor_root(target, 1000)
        # Verify against the original rational base, independently of floor
        # division in target and of the bisection's internal checks.
        assert root**1000 * denominator <= right
        assert right < (root + 1)**1000 * denominator
        self.root_checks += 1
        return F(root, self.scale), F(root + 1, self.scale)

    def log_reduced(self, x):
        """Enclose log(x) for 1 <= x <= 2 by the atanh series."""
        assert 1 <= x <= 2
        z = (x - 1) / (x + 1)
        zz = z * z
        term, total = z, F(0)
        for j in range(self.series_terms):
            total += term / (2 * j + 1)
            term *= zz
        lower = 2 * total
        tail = 2 * term / ((2 * self.series_terms + 1) * (1 - zz))
        return lower, lower + tail

    def log(self, x):
        assert x > 0
        k, y = 0, x
        while y < 1:
            y *= 2
            k -= 1
        while y >= 2:
            y /= 2
            k += 1
        lo, hi = self.log_reduced(y)
        a, b = self.log2
        return (lo + k * a, hi + k * b) if k >= 0 else (lo + k * b, hi + k * a)

    def sums(self, p, q, lam, arity):
        ts = list(terms(p, q, lam, arity))
        assert sum(w for w, _ in ts) == 1
        lo, hi = F(0), F(0)
        for weight, base in ts:
            a, b = self.power(base)
            lo += weight * a
            hi += weight * b
        return lo, hi

    def bound(self, p, q, lam):
        assert sum(p) == 1 and all(v >= 0 for v in p)
        assert all(0 <= v <= 1 for v in q) and lam > 1
        v = self.sums(p, q, lam, 3)
        e = self.sums(p, q, lam, 2)
        lvlo, _ = self.log(v[0])
        _, lvhi = self.log(v[1])
        lelo, _ = self.log(e[0])
        _, lehi = self.log(e[1])
        nlo, nhi = lvlo - F(3, 2) * lehi, lvhi - F(3, 2) * lelo
        llo, lhi = self.log(lam)
        dlo, dhi = F(557, 1000) * llo, F(557, 1000) * lhi
        assert 0 < nlo <= nhi and 0 < dlo <= dhi
        return v, e, (nlo / dhi, nhi / dlo)


def outward(x, digits, upper=False):
    """Print a rational endpoint with outward decimal rounding."""
    scale = 10**digits
    a = x.numerator * scale
    b = x.denominator
    n = -((-a) // b) if upper else a // b
    sign = "-" if n < 0 else ""
    n = abs(n)
    whole, rest = divmod(n, scale)
    return f"{sign}{whole}.{rest:0{digits}d}"


def show(name, interval, digits=20):
    print(f"{name} in [{outward(interval[0], digits)}, "
          f"{outward(interval[1], digits, upper=True)}]")


def audit(c, p, q, lam):
    # Compare the grouped dictionary of (base -> exact weight) with an
    # independently enumerated ordered tuple dictionary. No roots involved.
    for arity in (2, 3):
        grouped = {}
        for w, x in terms(p, q, lam, arity):
            grouped[x] = grouped.get(x, F(0)) + w
        ordered = {}
        for ix in product(range(4), repeat=arity):
            w = F(1)
            for i in ix:
                w *= p[i]
            if arity == 2:
                x = 1 - (lam - 1) * q[ix[0]] * q[ix[1]] / lam
            else:
                i, j, k = ix
                x = 1 + (lam - 1) * (1 - q[i]) * (1 - q[j]) * (1 - q[k])
            ordered[x] = ordered.get(x, F(0)) + w
        assert ordered == grouped
        assert sum(multiplicity(ix) for ix in
                   combinations_with_replacement(range(4), arity)) == 4**arity
    assert floor_root(0, 1000) == 0
    assert floor_root(1, 1000) == 1
    assert floor_root(2**1000 - 1, 1000) == 1
    assert floor_root(2**1000, 1000) == 2
    assert floor_root(2**1000 + 1, 1000) == 2
    # Power transform must preserve the exact endpoints 1 and lam**557.
    assert c.power(F(1))[0] == 1
    for x in (F(1, 100), F(1, 2), F(1), F(2), lam):
        lo, hi = c.power(x)
        assert lo**1000 <= x**557 < hi**1000
    assert c.log(F(1)) == (0, 0)
    a, b = c.log(F(2))
    lo, hi = c.log(F(1, 2))
    assert lo == -b and hi == -a
    lo, hi = c.log(F(4))
    assert lo == 2 * a and hi == 2 * b
    # Degenerate choices: all q=0 gives V=lam**m, E=1, bound=1;
    # all q=1 gives V=1, E=lam**(-m), bound=3/2.
    for val, exact in ((F(0), F(1)), (F(1), F(3, 2))):
        _, _, interval = c.bound((F(1),), (val,), lam)
        assert interval[0] <= exact <= interval[1]
    # For one atom the fractional powers cancel after taking logarithms.
    # Compare with the independent, purely rational-base 1-RSB expression.
    _, _, single = c.bound((F(1),), (F(3, 5),), lam)
    q0 = F(3, 5)
    v0 = 1 + (lam - 1) * (1 - q0)**3
    e0 = 1 - (1 - 1 / lam) * q0**2
    va, vb = c.log(v0)
    ea, eb = c.log(e0)
    la, lb = c.log(lam)
    direct = ((va - F(3, 2) * eb) / lb,
              (vb - F(3, 2) * ea) / la)
    assert single[0] <= direct[0] <= direct[1] <= single[1]
    print("audit: grouped/ordered weights, 2/3-fold counts, integer root boundaries,")
    print("       power inequalities, log identities, degenerate measures, 1-RSB PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits", type=int, default=18)
    parser.add_argument("--series-terms", type=int, default=48)
    parser.add_argument("--audit", action="store_true")
    args = parser.parse_args()
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    signal.alarm(120)
    started = time.monotonic()
    p = tuple(map(F, (".2493", ".2778", ".2880", ".1849")))
    q = tuple(map(F, (".1184", ".5947", ".8876", ".9827")))
    lam = F("19.3")
    c = Certificate(args.digits, args.series_terms)
    v, e, b = c.bound(p, q, lam)
    print("arithmetic: Python integers and fractions.Fraction only")
    print("nice =", os.getpriority(os.PRIO_PROCESS, 0))
    print(f"grid = 10^-{args.digits}; log series terms = {args.series_terms}")
    print("grouped star terms = 20; grouped edge terms = 10")
    show("V", v)
    show("E", e)
    show("B", b)
    threshold = F("0.450789952")
    assert b[1] < threshold
    show("0.450789952 - B", (threshold - b[1], threshold - b[0]), digits=22)
    print("CERTIFIED: alpha_3 <= B < 0.450789952")
    print("exact power brackets checked =", c.root_checks)
    if args.audit:
        audit(c, p, q, lam)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert rss < 1024**3  # macOS bytes, rather than Linux KiB.
    print("peak RSS bytes =", rss)
    print(f"elapsed seconds = {time.monotonic() - started:.3f}")


if __name__ == "__main__":
    main()
