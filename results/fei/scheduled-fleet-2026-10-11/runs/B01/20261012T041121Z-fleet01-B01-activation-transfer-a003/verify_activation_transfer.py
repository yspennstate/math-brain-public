#!/usr/bin/env python3
"""Independent finite checks for the A003 fresh-activation transfer lemma.

Command:
  python verify_activation_transfer.py

The checker exhausts every Boolean core through three variables and adds
structured/random larger cores.  It directly recomputes Walsh spectra, U,
all coordinate restrictions, and G; it does not use the transfer formulas
to compute the left sides being checked.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import itertools
import math
import random

getcontext().prec = 70
D = Decimal
LN2 = D(2).ln()
E = D(1).exp()

SEED = 2026101201
TOL = D("1e-55")


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


def spectral_probabilities(truth):
    n = int(math.log2(len(truth)))
    w = fwht(truth)
    den = 1 << (2 * n)
    return [Fraction(x * x, den) for x in w]


def upper_masses(probs):
    pi = list(probs)
    n = int(math.log2(len(pi)))
    for bit in range(n):
        step = 1 << bit
        for mask in range(1 << n):
            if not mask & step:
                pi[mask] += pi[mask | step]
    return pi


def mpq(q):
    return D(q.numerator) / q.denominator


def log2(x):
    return x.ln() / LN2


def U(truth):
    probs = spectral_probabilities(truth)
    pi = upper_masses(probs)
    ans = D(0)
    for p, upper in zip(probs, pi):
        if p:
            ans += mpq(p) * log2(mpq(upper / p))
    return ans


def influence(truth):
    probs = spectral_probabilities(truth)
    return sum(mpq(p) * mask.bit_count() for mask, p in enumerate(probs))


def restrict(truth, coord, value):
    n = int(math.log2(len(truth)))
    out = []
    lowmask = (1 << coord) - 1
    for y in range(1 << (n - 1)):
        x = (y & lowmask) | (value << coord) | ((y >> coord) << (coord + 1))
        out.append(truth[x])
    return tuple(out)


def G(truth):
    n = int(math.log2(len(truth)))
    u = U(truth)
    return sum(u - (U(restrict(truth, i, 0)) + U(restrict(truth, i, 1))) / 2
               for i in range(n))


def activate(core, d):
    cmask = (1 << d) - 1
    return tuple(core[x >> d] if (x & cmask) == 0 else 1
                 for x in range(len(core) << d))


def defect_rate(core):
    return D(sum(v == -1 for v in core)) / len(core)


def M(x):
    y = (1 - 2 * x) ** 2
    return D(0) if y == 0 else y * log2(1 / y)


def Q_formula(p, r, d, ug):
    def zlog(x):
        return D(0) if x == 0 else x * log2(1 / x)
    return (M(p * r) + 2 * r * p * d - p * M(r)
            + 4 * p * r * zlog(r) - 4 * p * r * zlog(p * r))


def delta_formula(p, r):
    x = p * r
    if x == 0:
        return D(0)
    return (M(x) - M(2 * x) / 2 + 2 * x
            + 4 * x * x * (log2(1 / x) - 2))


LM = 4 * (1 + 2 / E) / LN2
LB = 4 + 2 * (1 + 2 / E) / LN2
LR = 3 * LM + LB
CSTAR = 1 + 2 * (1 + 1 / E) / LN2


def named_cores():
    cores = []
    # all Boolean cores through n=3
    for n in range(4):
        N = 1 << n
        for code in range(1 << N):
            cores.append((f"all_n{n}_{code}", tuple(1 if code >> x & 1 else -1 for x in range(N))))

    # Structured mandatory controls.
    cores.append(("and4_point_defect", tuple(-1 if x == 15 else 1 for x in range(16))))
    cores.append(("tensor_and2_and2", tuple((-1 if (x & 3) == 3 else 1) *
                                             (-1 if ((x >> 2) & 3) == 3 else 1)
                                             for x in range(16))))
    # Two address bits select one of four data bits (bits 2..5).
    cores.append(("address_2_4", tuple(1 if (x >> (2 + (x & 3))) & 1 else -1
                                      for x in range(64))))
    # A shared-variable product/near-tensor control.
    cores.append(("overlap_product", tuple((1 if ((x & 3) == 3) else -1) *
                                           (1 if (((x >> 1) & 3) == 3) else -1)
                                           for x in range(8))))
    rng = random.Random(SEED)
    for k in range(24):
        cores.append((f"random_n5_{k}", tuple(rng.choice((-1, 1)) for _ in range(32))))
    return cores


def main():
    max_q_error = D(0)
    max_decomp_error = D(0)
    min_transfer_margin = D("Infinity")
    min_nonconstant_transfer_margin = D("Infinity")
    cases = 0
    parity_cases = 0

    for name, core in named_cores():
        n = int(math.log2(len(core)))
        ug, gg, ig = U(core), G(core), influence(core)
        r = defect_rate(core)
        for d in range(1, 6 if n <= 3 else 4):
            p = D(2) ** (-d)
            f = activate(core, d)
            uf, gf, inf_f = U(f), G(f), influence(f)
            q = Q_formula(p, r, d, ug)
            max_q_error = max(max_q_error, abs((uf - p * ug) - q))

            R = q - 2 * r * p * d
            data_jensen = D(0)
            for j in range(n):
                rp = defect_rate(restrict(core, j, 0))
                rm = defect_rate(restrict(core, j, 1))
                qp = Q_formula(p, rp, d, U(restrict(core, j, 0))) - 2 * rp * p * d
                qm = Q_formula(p, rm, d, U(restrict(core, j, 1))) - 2 * rm * p * d
                data_jensen += R - (qp + qm) / 2
            decomp = p * gg + d * delta_formula(p, r) + data_jensen
            max_decomp_error = max(max_decomp_error, abs(gf - decomp))

            ictl = 2 * r * p * d
            rhs = p * gg + (LR / 2) * p * ig + CSTAR * ictl
            min_transfer_margin = min(min_transfer_margin, rhs - gf)
            if inf_f > 0:
                min_nonconstant_transfer_margin = min(min_nonconstant_transfer_margin, rhs - gf)
            if abs(inf_f - (p * ig + ictl)) > TOL:
                raise AssertionError((name, d, "influence identity", inf_f, p * ig + ictl))
            cases += 1

    # Directly test every signed parity support size through n=5 and d=1..4.
    K = LR / 2
    min_parity_margin = D("Infinity")
    min_nonconstant_parity_margin = D("Infinity")
    for n in range(6):
        for support in range(n + 1):
            mask = (1 << support) - 1
            core = tuple(-1 if (x & mask).bit_count() % 2 else 1 for x in range(1 << n))
            for sign in (-1, 1):
                signed = tuple(sign * v for v in core)
                for d in range(1, 5):
                    f = activate(signed, d)
                    margin = K * influence(f) - G(f)
                    min_parity_margin = min(min_parity_margin, margin)
                    if influence(f) > 0:
                        min_nonconstant_parity_margin = min(min_nonconstant_parity_margin, margin)
                    parity_cases += 1

    if max_q_error > TOL or max_decomp_error > TOL:
        raise AssertionError((max_q_error, max_decomp_error))
    if min_transfer_margin < -TOL or min_parity_margin < -TOL:
        raise AssertionError((min_transfer_margin, min_parity_margin))

    print(f"seed={SEED}")
    print(f"arbitrary_core_cases={cases}")
    print(f"parity_class_cases={parity_cases}")
    print(f"L_M={LM:.20g}")
    print(f"L_R={LR:.20g}")
    print(f"K_activation=L_R/2={K:.20g}")
    print(f"C_star={CSTAR:.20g}")
    print(f"max_Q_identity_error={max_q_error:.8g}")
    print(f"max_G_decomposition_error={max_decomp_error:.8g}")
    print(f"min_transfer_margin={min_transfer_margin:.12g}")
    print(f"min_nonconstant_transfer_margin={min_nonconstant_transfer_margin:.12g}")
    print(f"min_parity_GU_margin={min_parity_margin:.12g}")
    print(f"min_nonconstant_parity_GU_margin={min_nonconstant_parity_margin:.12g}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
