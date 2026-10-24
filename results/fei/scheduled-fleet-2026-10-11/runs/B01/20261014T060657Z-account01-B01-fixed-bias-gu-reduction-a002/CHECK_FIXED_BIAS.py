#!/usr/bin/env python3
"""Independent finite checks for the fixed-bias GU hardness embedding.

The all-dimensional reduction is analytic. Walsh masses here are reconstructed
directly from the character definition; no producer checker is imported.
"""

from fractions import Fraction
import itertools
import math
import random

SEED = 202610140606
TOL = 4e-11


def spectrum(values):
    npts = len(values)
    out = []
    for mask in range(npts):
        raw = 0
        for x, value in enumerate(values):
            raw += value * (-1 if (mask & x).bit_count() & 1 else 1)
        out.append(Fraction(raw * raw, npts * npts))
    return out


def caps(p):
    out = p[:]
    n = len(p).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(out)):
            if not s & bit:
                out[s] += out[s | bit]
    return out


def U_only(values):
    p = spectrum(values)
    pi = caps(p)
    return sum(
        float(mass) * math.log2(float(cap / mass))
        for mass, cap in zip(p, pi) if mass
    )


def restriction(values, coordinate, bit):
    n = len(values).bit_length() - 1
    result = []
    for reduced in range(1 << (n - 1)):
        low = reduced & ((1 << coordinate) - 1)
        high = reduced >> coordinate
        x = low | (bit << coordinate) | (high << (coordinate + 1))
        result.append(values[x])
    return tuple(result)


def stats(values):
    p = spectrum(values)
    n = len(values).bit_length() - 1
    U = U_only(values)
    I = sum(s.bit_count() * float(p[s]) for s in range(len(p)))
    G = sum(
        U - 0.5 * (
            U_only(restriction(values, i, 0))
            + U_only(restriction(values, i, 1))
        )
        for i in range(n)
    )
    return U, I, G


def transform(q):
    # Low bit z: q-branch at z=0, constant branch at z=1.
    # High bit y balances the q-branch.
    out = []
    n = len(q).bit_length() - 1
    for ybit in (0, 1):
        y = -1 if ybit == 0 else 1
        for x in range(1 << n):
            out.extend((y * q[x], 1))
    return tuple(out)


def tensor(f, g):
    return tuple(a * b for b in g for a in f)


def tensor_power(f, t):
    result = (1,)
    for _ in range(t):
        result = tensor(result, f)
    return result


def zlog(x):
    return 0.0 if x == 0.0 else x * math.log2(1.0 / x)


def R(t):
    x = (1.0 + t) ** 2 / 4.0
    s = (1.0 - t) / 2.0
    old = zlog(t * t)
    return zlog(x) + (0.0 if s == 0.0 else s * s * math.log2(1.0 / s)) - old / 2.0 + (1.0 - t * t) / 4.0


def kappa(t):
    return 2.0 - 0.5 * (R(t) + R(-t))


def main():
    cores = []
    for n in range(4):
        cores.extend(itertools.product((-1, 1), repeat=1 << n))
    rng = random.Random(SEED)
    for _ in range(1024):
        cores.append(tuple(1 if rng.getrandbits(1) else -1 for _ in range(16)))

    max_u_error = 0.0
    max_i_error = 0.0
    max_g_error = 0.0
    fixed_bias_checks = 0
    formula_checks = 0
    for q in cores:
        tq = transform(q)
        Uq, Iq, Gq = stats(q)
        Ut, It, Gt = stats(tq)
        m = sum(q) / len(q)
        max_u_error = max(max_u_error, abs(Ut - (1.0 + Uq / 2.0)))
        max_i_error = max(max_i_error, abs(It - (1.0 + Iq / 2.0)))
        max_g_error = max(max_g_error, abs(Gt - (Gq / 2.0 + kappa(m))))
        assert abs(sum(tq) / len(tq) - 0.5) <= TOL
        assert abs(Ut - (1.0 + Uq / 2.0)) <= TOL
        assert abs(It - (1.0 + Iq / 2.0)) <= TOL
        assert abs(Gt - (Gq / 2.0 + kappa(m))) <= TOL
        fixed_bias_checks += 1
        formula_checks += 3

    # Check the exact tensor-transfer rearrangement for several pairs.
    transfer_checks = 0
    max_transfer_error = 0.0
    A = 3.75
    B = 0.75
    seeds = []
    for n in range(3):
        seeds.extend(itertools.product((-1, 1), repeat=1 << n))
    for q in seeds:
        Uq, Iq, Gq = stats(q)
        m = sum(q) / len(q)
        for t in range(1, 4):
            qt = tensor_power(q, t)
            f = transform(qt)
            Uf, If, Gf = stats(f)
            slice_slack_twice = 2.0 * (A * If + B * Uf - Gf)
            seed_slack = t * (A * Iq + B * Uq - Gq)
            correction = 2.0 * (A + B - kappa(m ** t))
            error = abs(slice_slack_twice - seed_slack - correction)
            max_transfer_error = max(max_transfer_error, error)
            assert error <= TOL
            transfer_checks += 1

    # Explicit compactness bound used in the analytic limit.
    scalar_checks = 0
    min_kappa = 1e100
    max_kappa = -1e100
    for j in range(500_001):
        m = -1.0 + 2.0 * j / 500_000.0
        value = kappa(m)
        min_kappa = min(min_kappa, value)
        max_kappa = max(max_kappa, value)
        assert -0.5 <= R(m) <= 1.75
        assert 0.25 <= value <= 2.5
        scalar_checks += 1

    print("status=PASS")
    print(f"boolean_cores_checked={len(cores)}")
    print(f"fixed_bias_checks={fixed_bias_checks}")
    print(f"embedding_formula_checks={formula_checks}")
    print(f"tensor_transfer_checks={transfer_checks}")
    print(f"scalar_bound_checks={scalar_checks}")
    print(f"max_U_error={max_u_error:.3e}")
    print(f"max_I_error={max_i_error:.3e}")
    print(f"max_G_error={max_g_error:.3e}")
    print(f"max_transfer_error={max_transfer_error:.3e}")
    print(f"observed_kappa_range=[{min_kappa:.15f},{max_kappa:.15f}]")
    print(f"seed={SEED}")


if __name__ == "__main__":
    main()
