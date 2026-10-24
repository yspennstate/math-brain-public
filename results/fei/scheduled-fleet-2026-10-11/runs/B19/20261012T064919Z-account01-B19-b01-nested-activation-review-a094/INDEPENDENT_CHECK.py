#!/usr/bin/env python3
"""Independent checks for B01's nested-activation ledger.

No code is imported from the target bundle.  Fourier probabilities and every
restriction value entering G are reconstructed from truth tables.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache
import math
import random

getcontext().prec = 80
D = Decimal
LN2 = D(2).ln()
E = D(1).exp()
TOL = D("1e-62")
SEED = 2026101205


def hadamard(v):
    v = list(v)
    step = 1
    while step < len(v):
        for left in range(0, len(v), 2 * step):
            for j in range(left, left + step):
                a, b = v[j], v[j + step]
                v[j], v[j + step] = a + b, a - b
        step *= 2
    return v


@lru_cache(None)
def spectral_law(truth):
    n = (len(truth)).bit_length() - 1
    scale = 1 << (2 * n)
    return tuple(Fraction(z * z, scale) for z in hadamard(truth))


def qdec(q):
    return D(q.numerator) / D(q.denominator)


def lg(x):
    return x.ln() / LN2


@lru_cache(None)
def upper_potential(truth):
    law = list(spectral_law(truth))
    cap = list(law)
    n = len(truth).bit_length() - 1
    for j in range(n):
        bit = 1 << j
        for s in range(1 << n):
            if not s & bit:
                cap[s] += cap[s | bit]
    total = D(0)
    for a, b in zip(law, cap):
        if a:
            total += qdec(a) * lg(qdec(b / a))
    return total


def section(truth, j, eps):
    n = len(truth).bit_length() - 1
    low = (1 << j) - 1
    return tuple(truth[(y & low) | (eps << j) | ((y >> j) << (j + 1))]
                 for y in range(1 << (n - 1)))


@lru_cache(None)
def G(truth):
    n = len(truth).bit_length() - 1
    u = upper_potential(truth)
    return sum(u - (upper_potential(section(truth, j, 0)) +
                    upper_potential(section(truth, j, 1))) / 2
               for j in range(n))


@lru_cache(None)
def influence(truth):
    return sum(qdec(p) * s.bit_count()
               for s, p in enumerate(spectral_law(truth)))


@lru_cache(None)
def singleton_pair(truth):
    n = len(truth).bit_length() - 1
    w = l = D(0)
    law = spectral_law(truth)
    for j in range(n):
        a = qdec(law[1 << j])
        w += a
        if a:
            l += a * lg(1 / a)
    return w, l


def defects(truth):
    return D(sum(x == -1 for x in truth)) / D(len(truth))


def activate(truth, d):
    mask = (1 << d) - 1
    return tuple(truth[z >> d] if (z & mask) == mask else 1
                 for z in range(len(truth) << d))


def corpus():
    out = []
    for n in range(4):
        N = 1 << n
        for code in range(1 << N):
            out.append((f"exhaustive_{n}_{code}",
                        tuple(1 if (code >> x) & 1 else -1 for x in range(N))))
    out += [
        ("majority5", tuple(1 if x.bit_count() >= 3 else -1 for x in range(32))),
        ("point_defect6", tuple(-1 if x == 0 else 1 for x in range(64))),
        ("addressing2", tuple(1 if (x >> (2 + (x & 3))) & 1 else -1
                              for x in range(64))),
        ("parity6", tuple(-1 if x.bit_count() & 1 else 1 for x in range(64))),
        ("exactly_one3", tuple(1 if x.bit_count() == 1 else -1 for x in range(8))),
        ("overlap3", tuple((1 if (x & 3) == 3 else -1) *
                           (1 if ((x >> 1) & 3) == 3 else -1)
                           for x in range(8))),
    ]
    rng = random.Random(SEED)
    for j in range(16):
        out.append((f"random5_{j}", tuple(rng.choice((-1, 1)) for _ in range(32))))
    return out


CSTAR = 1 + 2 * (1 + 1 / E) / LN2
CCHAIN = CSTAR + D(8960) + D(2560) / (E * LN2)
CSEP = 3 + 4 * (1 + 2 / E) / LN2 + 2 / LN2 + 2 / (E * LN2)


def phi(x):
    if x == 0:
        return D(0)
    return x * x * lg(1 / (x * x))


def main():
    # Independent grid challenge for the analytic central-difference lemma.
    worst_modulus_margin = D("Infinity")
    modulus_cases = 0
    N = 256
    for hi in range(1, N + 1):
        h = D(hi) / N
        rhs = 64 * h * h * (1 + lg(1 / h))
        for xi in range(-N + hi, N - hi + 1):
            x = D(xi) / N
            lhs = abs(phi(x) - (phi(x - h) + phi(x + h)) / 2)
            worst_modulus_margin = min(worst_modulus_margin, rhs - lhs)
            modulus_cases += 1

    min_local = D("Infinity")
    min_chain = D("Infinity")
    min_b05_overlap = D("Infinity")
    max_w_error = max_l_error = D(0)
    direct_cases = hierarchy_cases = 0
    sequences = [(1,), (2,), (1, 1), (1, 2), (2, 1),
                 (1, 1, 1), (2, 1, 1), (1, 2, 2)]

    for name, core in corpus():
        n = len(core).bit_length() - 1
        r = defects(core)
        w1, l1 = singleton_pair(core)
        gg = G(core)
        for d in range(1, 7 if n <= 3 else 3):
            p = D(2) ** (-d)
            f = activate(core, d)
            ictl = 2 * p * d * r
            rhs = p * gg + 320 * p * (w1 + l1) + CSTAR * ictl
            min_local = min(min_local, rhs - G(f))
            # Current reviewed B05 hierarchy theorem already gives this
            # stronger U-level payment for the same one-active-leaf class.
            min_b05_overlap = min(min_b05_overlap,
                                  p * upper_potential(core) + CSEP * ictl -
                                  upper_potential(f))
            direct_cases += 1

        for ds in sequences:
            Dtot = sum(ds)
            if n + Dtot > 9:
                continue
            q = D(2) ** (-Dtot)
            f = activate(core, Dtot)
            wf, lf = singleton_pair(f)
            predicted_w = q * q * w1 + 4 * Dtot * q * q * r * r
            predicted_l = q * q * l1 + 2 * Dtot * q * q * w1
            if r:
                predicted_l += (4 * Dtot * q * q * r * r *
                                lg(1 / (4 * q * q * r * r)))
            max_w_error = max(max_w_error, abs(wf - predicted_w))
            max_l_error = max(max_l_error, abs(lf - predicted_l))
            ictl = 2 * q * Dtot * r
            rhs = q * gg + 640 * q * l1 + 1920 * q * w1 + CCHAIN * ictl
            min_chain = min(min_chain, rhs - G(f))
            hierarchy_cases += 1

    if min(worst_modulus_margin, min_local, min_chain, min_b05_overlap) < -TOL:
        raise AssertionError((worst_modulus_margin, min_local,
                              min_chain, min_b05_overlap))
    if max(max_w_error, max_l_error) > TOL:
        raise AssertionError((max_w_error, max_l_error))

    print(f"seed={SEED}")
    print(f"modulus_grid_cases={modulus_cases}")
    print(f"direct_activation_cases={direct_cases}")
    print(f"hierarchy_cases={hierarchy_cases}")
    print(f"C_star={CSTAR:.20g}")
    print(f"C_chain={CCHAIN:.20g}")
    print(f"C_sep={CSEP:.20g}")
    print(f"min_modulus_margin={worst_modulus_margin:.12g}")
    print(f"min_local_margin={min_local:.12g}")
    print(f"min_chain_margin={min_chain:.12g}")
    print(f"min_reviewed_B05_U_margin={min_b05_overlap:.12g}")
    print(f"max_W1_identity_error={max_w_error:.8g}")
    print(f"max_L1_identity_error={max_l_error:.8g}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
