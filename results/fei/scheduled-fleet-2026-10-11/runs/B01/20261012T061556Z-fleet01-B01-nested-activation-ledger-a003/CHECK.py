#!/usr/bin/env python3
"""Finite Walsh checks for the A003 nested-activation ledger.

Command:
  python CHECK.py

Scope: exhaustive Boolean cores through three variables, plus structured and
seeded larger controls.  Every displayed U and G value is recomputed from the
truth table.  The analytic scalar modulus and the all-parameter theorem remain
proof obligations in NESTED_ACTIVATION_LEDGER.tex; this script is only an
independent finite falsifier search and identity check.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import itertools
import math
import random
from functools import lru_cache

getcontext().prec = 70
D = Decimal
LN2 = D(2).ln()
E = D(1).exp()
SEED = 2026101203
TOL = D("1e-54")


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


@lru_cache(maxsize=None)
def spectrum(truth):
    n = int(math.log2(len(truth)))
    w = fwht(truth)
    den = 1 << (2 * n)
    return [Fraction(x * x, den) for x in w]


def dec(q):
    return D(q.numerator) / q.denominator


def log2(x):
    return x.ln() / LN2


def upper_masses(probs):
    out = list(probs)
    n = int(math.log2(len(out)))
    for bit in range(n):
        b = 1 << bit
        for mask in range(1 << n):
            if not mask & b:
                out[mask] += out[mask | b]
    return out


@lru_cache(maxsize=None)
def U(truth):
    probs = spectrum(truth)
    upper = upper_masses(probs)
    ans = D(0)
    for p, pi in zip(probs, upper):
        if p:
            ans += dec(p) * log2(dec(pi / p))
    return ans


def restrict(truth, coord, value):
    n = int(math.log2(len(truth)))
    low = (1 << coord) - 1
    return tuple(truth[(y & low) | (value << coord) |
                       ((y >> coord) << (coord + 1))]
                 for y in range(1 << (n - 1)))


@lru_cache(maxsize=None)
def G(truth):
    n = int(math.log2(len(truth)))
    u = U(truth)
    return sum(u - (U(restrict(truth, j, 0)) +
                    U(restrict(truth, j, 1))) / 2 for j in range(n))


@lru_cache(maxsize=None)
def influence(truth):
    return sum(dec(p) * mask.bit_count()
               for mask, p in enumerate(spectrum(truth)))


@lru_cache(maxsize=None)
def singleton_stats(truth):
    probs = spectrum(truth)
    n = int(math.log2(len(truth)))
    w1 = D(0)
    l1 = D(0)
    for j in range(n):
        p = dec(probs[1 << j])
        w1 += p
        if p:
            l1 += p * log2(1 / p)
    return w1, l1


def defect_rate(truth):
    return D(sum(v == -1 for v in truth)) / len(truth)


def activate(core, d):
    active = (1 << d) - 1
    return tuple(core[x >> d] if (x & active) == 0 else 1
                 for x in range(len(core) << d))


def named_cores():
    cores = []
    for n in range(4):
        N = 1 << n
        for code in range(1 << N):
            cores.append((f"all_n{n}_{code}",
                          tuple(1 if code >> x & 1 else -1
                                for x in range(N))))
    cores.extend([
        ("majority5", tuple(1 if x.bit_count() >= 3 else -1
                            for x in range(32))),
        ("point_defect6", tuple(-1 if x == 63 else 1
                                for x in range(64))),
        ("address_2_4", tuple(1 if (x >> (2 + (x & 3))) & 1 else -1
                              for x in range(64))),
        ("near_tensor5", tuple((1 if (x & 3) == 3 else -1) *
                               (1 if ((x >> 2) & 3) == 3 else -1)
                               if x != 31 else 1 for x in range(32))),
        ("overlap_product3", tuple((1 if (x & 3) == 3 else -1) *
                                   (1 if ((x >> 1) & 3) == 3 else -1)
                                   for x in range(8))),
        ("exactly_one3_prime_control", tuple(1 if x.bit_count() == 1 else -1
                                             for x in range(8))),
        ("parity6", tuple(-1 if x.bit_count() & 1 else 1
                          for x in range(64))),
    ])
    rng = random.Random(SEED)
    for k in range(12):
        cores.append((f"random_n5_{k}",
                      tuple(rng.choice((-1, 1)) for _ in range(32))))
    return cores


CSTAR = 1 + 2 * (1 + 1 / E) / LN2
CCHAIN = CSTAR + D(8960) + D(2560) / (E * LN2)


def main():
    max_w_error = D(0)
    max_l_error = D(0)
    min_local_margin = D("Infinity")
    min_chain_margin = D("Infinity")
    min_ledger_margin = D("Infinity")
    local_cases = 0
    chain_cases = 0

    sequences = [(1,), (2,), (1, 1), (1, 2), (2, 1),
                 (1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 1, 1, 1)]

    for name, core in named_cores():
        n = int(math.log2(len(core)))
        ug, gg, ig = U(core), G(core), influence(core)
        w1, l1 = singleton_stats(core)
        r = defect_rate(core)

        for d in range(1, 6 if n <= 3 else 3):
            p = D(2) ** (-d)
            f = activate(core, d)
            ictl = 2 * p * d * r
            rhs = p * gg + 320 * p * (w1 + l1) + CSTAR * ictl
            min_local_margin = min(min_local_margin, rhs - G(f))
            local_cases += 1

        for ds in sequences:
            total_d = sum(ds)
            if n + total_d > 9:
                continue
            q = D(2) ** (-total_d)
            f = activate(core, total_d)
            wf, lf = singleton_stats(f)
            w_formula = q * q * w1 + 4 * total_d * q * q * r * r
            l_formula = (q * q * l1 + 2 * total_d * q * q * w1 +
                         (D(0) if r == 0 else
                          4 * total_d * q * q * r * r *
                          log2(1 / (4 * q * q * r * r))))
            max_w_error = max(max_w_error, abs(wf - w_formula))
            max_l_error = max(max_l_error, abs(lf - l_formula))

            ictl = 2 * q * total_d * r
            chain_rhs = (q * gg + 640 * q * l1 + 1920 * q * w1 +
                         CCHAIN * ictl)
            min_chain_margin = min(min_chain_margin, chain_rhs - G(f))

            # Directly form the accumulated singleton ledger.
            Dprev = 0
            ledger = D(0)
            for d in ds:
                qprev = D(2) ** (-Dprev)
                prev = activate(core, Dprev) if Dprev else core
                wp, lp = singleton_stats(prev)
                ledger += q / qprev * (wp + lp)
                Dprev += d
            tail = (2 * q * l1 + 6 * q * w1 +
                    (28 + 8 / (E * LN2)) * ictl)
            min_ledger_margin = min(min_ledger_margin, tail - ledger)
            chain_cases += 1

    if max_w_error > TOL or max_l_error > TOL:
        raise AssertionError((max_w_error, max_l_error))
    if min_local_margin < -TOL or min_chain_margin < -TOL:
        raise AssertionError((min_local_margin, min_chain_margin))
    if min_ledger_margin < -TOL:
        raise AssertionError(min_ledger_margin)

    print(f"seed={SEED}")
    print(f"local_cases={local_cases}")
    print(f"chain_cases={chain_cases}")
    print(f"C_star={CSTAR:.20g}")
    print(f"C_chain={CCHAIN:.20g}")
    print(f"max_W1_formula_error={max_w_error:.8g}")
    print(f"max_L1_formula_error={max_l_error:.8g}")
    print(f"min_local_bound_margin={min_local_margin:.12g}")
    print(f"min_chain_bound_margin={min_chain_margin:.12g}")
    print(f"min_ledger_margin={min_ledger_margin:.12g}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
