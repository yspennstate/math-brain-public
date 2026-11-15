#!/usr/bin/env python3
"""Independent ordered-tuple Decimal evaluation and precision audit."""
from decimal import Decimal as D, localcontext
from fractions import Fraction
from itertools import product
import os
import resource
import signal
import sys

sys.dont_write_bytecode = True
from certify import Certificate


def evaluate(precision):
    with localcontext() as ctx:
        ctx.prec = precision
        p = list(map(D, ("0.2493", "0.2778", "0.2880", "0.1849")))
        q = list(map(D, ("0.1184", "0.5947", "0.8876", "0.9827")))
        L = D("19.3")
        m = D(".557")
        v = sum(p[i] * p[j] * p[k] *
                (m * (1 + (L - 1) * (1 - q[i]) * (1 - q[j]) * (1 - q[k])).ln()).exp()
                for i, j, k in product(range(4), repeat=3))
        e = sum(p[i] * p[j] *
                (m * (1 - (1 - 1 / L) * q[i] * q[j]).ln()).exp()
                for i, j in product(range(4), repeat=2))
        b = (v.ln() - D("1.5") * e.ln()) / (m * L.ln())
        return v, e, b


def main():
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    signal.alarm(120)
    a = evaluate(70)
    b = evaluate(110)
    for name, lowprec, value in zip(("V", "E", "B"), a, b):
        print(f"{name} (110-digit ordered Decimal) = {value}")
        with localcontext() as ctx:
            ctx.prec = 120
            assert abs(lowprec - value) < D("1e-67")
    p = tuple(map(Fraction, (".2493", ".2778", ".2880", ".1849")))
    q = tuple(map(Fraction, (".1184", ".5947", ".8876", ".9827")))
    lam = Fraction("19.3")
    for digits, nterms in ((18, 48), (24, 64)):
        c = Certificate(digits, nterms)
        intervals = c.bound(p, q, lam)
        for value, (lo, hi) in zip(b, intervals):
            assert lo <= Fraction(value) <= hi
        print(f"Decimal values inside exact intervals: grid 10^-{digits}, N={nterms} PASS")
    print("70/110-digit agreement within 1e-67 PASS")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert rss < 1024**3
    print("peak RSS bytes =", rss)


if __name__ == "__main__":
    main()
