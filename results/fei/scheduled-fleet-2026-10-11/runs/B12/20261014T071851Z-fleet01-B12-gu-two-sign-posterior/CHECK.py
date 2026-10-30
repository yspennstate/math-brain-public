#!/usr/bin/env python3
"""Exact/deterministic checks for the two-sign posterior identity."""

from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import log2
import random

SEED = 0xB12A05805
TOL = 5e-10


@lru_cache(maxsize=None)
def fwht(values):
    a = [Fraction(x) for x in values]
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for j in range(start, start + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return tuple(x / len(a) for x in a)


@lru_cache(maxsize=None)
def spectral_law(values):
    return tuple(x * x for x in fwht(values))


def upper_masses(p):
    z = list(p)
    n = len(p).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if not (s & bit):
                z[s] += z[s | bit]
    return tuple(z)


@lru_cache(maxsize=None)
def u_value(values):
    p = spectral_law(values)
    pi = upper_masses(p)
    return sum(float(x) * log2(float(y / x))
               for x, y in zip(p, pi) if x)


@lru_cache(maxsize=None)
def influence(values):
    return sum(Fraction(s.bit_count()) * mass
               for s, mass in enumerate(spectral_law(values)))


@lru_cache(maxsize=None)
def restrict_one(values, i, bit):
    n = len(values).bit_length() - 1
    return tuple(values[(z & ((1 << i) - 1)) | (bit << i) |
                        ((z >> i) << (i + 1))]
                 for z in range(1 << (n - 1)))


@lru_cache(maxsize=None)
def g_value(values):
    n = len(values).bit_length() - 1
    return sum(u_value(values) - 0.5 * (
        u_value(restrict_one(values, i, 0)) +
        u_value(restrict_one(values, i, 1))) for i in range(n))


def multiply(g, h):
    return tuple(x * y for x, y in zip(g, h))


@lru_cache(maxsize=None)
def collision(g, h):
    return u_value(multiply(g, h)) - u_value(g) - u_value(h)


def collision_laplacian(g, h):
    n = len(g).bit_length() - 1
    c = collision(g, h)
    return sum(c - 0.5 * (
        collision(restrict_one(g, i, 0), restrict_one(h, i, 0)) +
        collision(restrict_one(g, i, 1), restrict_one(h, i, 1)))
               for i in range(n))


@lru_cache(maxsize=None)
def active_coords(g, h):
    n = len(g).bit_length() - 1
    return tuple(i for i in range(n) if any(
        g[x] != g[x ^ (1 << i)] or h[x] != h[x ^ (1 << i)]
        for x in range(1 << n)))


@lru_cache(maxsize=None)
def policy_companion(g, h):
    active = active_coords(g, h)
    if not active:
        return 0.0
    i = active[0]
    child = 0.5 * (
        policy_companion(restrict_one(g, i, 0), restrict_one(h, i, 0)) +
        policy_companion(restrict_one(g, i, 1), restrict_one(h, i, 1)))
    return collision_laplacian(g, h) - collision(g, h) + child


def expected_policy_child(g, h):
    active = active_coords(g, h)
    if not active:
        return 0.0
    i = active[0]
    return 0.5 * (
        policy_companion(restrict_one(g, i, 0), restrict_one(h, i, 0)) +
        policy_companion(restrict_one(g, i, 1), restrict_one(h, i, 1)))


def joint_pivotal(g, h):
    n = len(g).bit_length() - 1
    ans = Fraction(0)
    for i in range(n):
        ans += Fraction(sum(
            g[x] != g[x ^ (1 << i)] and h[x] != h[x ^ (1 << i)]
            for x in range(1 << n)), 1 << n)
    return ans


@lru_cache(maxsize=None)
def mixture_terms(fplus, fminus):
    pplus = spectral_law(fplus)
    pminus = spectral_law(fminus)
    uplus = upper_masses(pplus)
    uminus = upper_masses(pminus)
    q = tuple((x + y) / 2 for x, y in zip(pplus, pminus))
    m = tuple((x + y) / 2 for x, y in zip(uplus, uminus))
    mix = sum(float(x) * log2(float(y / x))
              for x, y in zip(q, m) if x)
    kl = 0.0
    for xp, xm, yp, ym, qs, ms in zip(
            pplus, pminus, uplus, uminus, q, m):
        if not qs:
            continue
        for pe, ue in ((xp, yp), (xm, ym)):
            if pe:
                r = pe / (2 * qs)
                s = ue / (2 * ms)
                kl += float(qs * r) * log2(float(r / s))
    return mix, kl


def pair_laplacians(fplus, fminus):
    mix, kl = mixture_terms(fplus, fminus)
    n = len(fplus).bit_length() - 1
    lmix = 0.0
    lkl = 0.0
    for i in range(n):
        children = [mixture_terms(restrict_one(fplus, i, bit),
                                  restrict_one(fminus, i, bit))
                    for bit in (0, 1)]
        lmix += mix - 0.5 * (children[0][0] + children[1][0])
        lkl += kl - 0.5 * (children[0][1] + children[1][1])
    return lmix, lkl


def defect(f, a, b):
    return g_value(f) - a * float(influence(f)) - b * u_value(f)


def verify_pair(fplus, fminus, frozen_pairs):
    mix, kl = mixture_terms(fplus, fminus)
    lmix, lkl = pair_laplacians(fplus, fminus)
    avg_u = 0.5 * (u_value(fplus) + u_value(fminus))
    avg_g = 0.5 * (g_value(fplus) + g_value(fminus))
    err_u = abs(avg_u - (mix - kl))
    err_g = abs(avg_g - (lmix - lkl))
    assert err_u <= TOL and err_g <= TOL
    max_defect_error = 0.0
    avg_i = 0.5 * (float(influence(fplus)) + float(influence(fminus)))
    for a, b in frozen_pairs:
        lhs = 0.5 * (defect(fplus, a, b) + defect(fminus, a, b))
        rhs = lmix - a * avg_i - b * mix + b * kl - lkl
        max_defect_error = max(max_defect_error, abs(lhs - rhs))
        assert abs(lhs - rhs) <= TOL
    return err_u, err_g, max_defect_error, kl, lkl


def verify_product_projection(g, h, frozen_pairs):
    fplus = multiply(g, h)
    fminus = g
    c = collision(g, h)
    lc = collision_laplacian(g, h)
    p = policy_companion(g, h)
    rp = expected_policy_child(g, h)
    j = float(joint_pivotal(g, h))
    assert abs(lc - (c + p - rp)) <= TOL
    max_error = 0.0
    for a, b in frozen_pairs:
        lhs = defect(fplus, a, b) - defect(fminus, a, b)
        rhs = defect(h, a, b) + (1 - b) * c + 2 * a * j + p - rp
        max_error = max(max_error, abs(lhs - rhs))
        assert abs(lhs - rhs) <= TOL
    return max_error


def tensor(f, copies):
    out = (1,)
    for _ in range(copies):
        out = tuple(x * y for x in out for y in f)
    return out


def activate_half(f):
    return tuple([1] * len(f) + list(f))


def main():
    frozen_pairs = ((0.0, 0.0), (4.0, 0.5), (6.0, 0.25))
    max_u_error = max_g_error = max_defect_error = max_projection_error = 0.0
    min_lkl = (float("inf"), None)
    max_lkl = (-float("inf"), None)
    positive_p_zero_k = 0
    exhaustive_pairs = 0

    for n in range(1, 4):
        functions = list(product((-1, 1), repeat=1 << n))
        for g in functions:
            for h in functions:
                fplus = multiply(g, h)
                fminus = g
                eu, eg, ed, kl, lkl = verify_pair(
                    fplus, fminus, frozen_pairs)
                ep = verify_product_projection(g, h, frozen_pairs)
                max_u_error = max(max_u_error, eu)
                max_g_error = max(max_g_error, eg)
                max_defect_error = max(max_defect_error, ed)
                max_projection_error = max(max_projection_error, ep)
                p = policy_companion(g, h)
                if p > TOL and kl < TOL:
                    positive_p_zero_k += 1
                if lkl < min_lkl[0]:
                    min_lkl = (lkl, (n, g, h))
                if lkl > max_lkl[0]:
                    max_lkl = (lkl, (n, g, h))
                exhaustive_pairs += 1

    rng = random.Random(SEED)
    random_pairs = 180
    maximum_dimension = 3
    for _ in range(random_pairs):
        n = rng.randint(4, 6)
        g = tuple(rng.choice((-1, 1)) for _ in range(1 << n))
        h = tuple(rng.choice((-1, 1)) for _ in range(1 << n))
        fplus = multiply(g, h)
        eu, eg, ed, _, _ = verify_pair(fplus, g, frozen_pairs)
        ep = verify_product_projection(g, h, frozen_pairs)
        max_u_error = max(max_u_error, eu)
        max_g_error = max(max_g_error, eg)
        max_defect_error = max(max_defect_error, ed)
        max_projection_error = max(max_projection_error, ep)
        maximum_dimension = max(maximum_dimension, n)

    positive_g = (-1, -1, -1, -1, -1, 1, 1, 1)
    positive_h = (-1, 1, 1, -1, -1, 1, 1, -1)
    negative_g = (-1, -1, -1, 1)
    negative_h = negative_g

    controls = (
        ("positive_three_bit", positive_g, positive_h),
        ("negative_two_bit", negative_g, negative_h),
        ("positive_tensor_two", tensor(positive_g, 2), tensor(positive_h, 2)),
        ("rare_half_activation", activate_half(positive_g),
         activate_half(positive_h)),
    )
    control_lines = []
    for name, g, h in controls:
        fplus = multiply(g, h)
        mix, kl = mixture_terms(fplus, g)
        lmix, lkl = pair_laplacians(fplus, g)
        verify_pair(fplus, g, frozen_pairs)
        verify_product_projection(g, h, frozen_pairs)
        control_lines.append(
            f"{name}=n:{len(g).bit_length()-1},C:{collision(g,h):.17g},"
            f"LC:{collision_laplacian(g,h):.17g},"
            f"P:{policy_companion(g,h):.17g},"
            f"RP:{expected_policy_child(g,h):.17g},"
            f"K:{kl:.17g},LK:{lkl:.17g},M:{mix:.17g},LM:{lmix:.17g}")

    # Exact root-posterior falsifier.
    zero_g = (-1, -1, -1, -1, -1, -1, -1, 1)
    zero_h = (-1, 1, 1, 1, 1, 1, 1, -1)
    zero_fplus = multiply(zero_g, zero_h)
    pplus = spectral_law(zero_fplus)
    pminus = spectral_law(zero_g)
    assert pplus == pminus
    assert upper_masses(pplus) == upper_masses(pminus)
    _, zero_k = mixture_terms(zero_fplus, zero_g)
    _, zero_lk = pair_laplacians(zero_fplus, zero_g)
    assert zero_k == 0.0
    assert collision(zero_g, zero_h) == -0.5
    assert abs(collision_laplacian(zero_g, zero_h) - 1.5) <= TOL
    assert abs(policy_companion(zero_g, zero_h) - 1.0) <= TOL
    assert abs(expected_policy_child(zero_g, zero_h) + 1.0) <= TOL
    assert joint_pivotal(zero_g, zero_h) == Fraction(3, 4)
    assert zero_lk < -0.5

    print("STATUS PASS")
    print(f"seed={SEED}")
    print(f"exhaustive_product_pairs={exhaustive_pairs}")
    print(f"random_product_pairs={random_pairs}")
    print(f"maximum_dimension={maximum_dimension}")
    print(f"maximum_U_identity_error={max_u_error:.17g}")
    print(f"maximum_G_identity_error={max_g_error:.17g}")
    print(f"maximum_center_defect_error={max_defect_error:.17g}")
    print(f"maximum_product_projection_error={max_projection_error:.17g}")
    print(f"positive_companion_zero_root_K_count={positive_p_zero_k}")
    print(f"minimum_LK={min_lkl[0]:.17g}")
    print(f"maximum_LK={max_lkl[0]:.17g}")
    print(f"minimum_LK_witness={min_lkl[1]}")
    print(f"maximum_LK_witness={max_lkl[1]}")
    print("zero_K_witness_squared_law=" + str(tuple(pplus)))
    print("zero_K_witness_C=-1/2")
    print("zero_K_witness_LC=3/2")
    print("zero_K_witness_P=1")
    print("zero_K_witness_expected_child_P=-1")
    print(f"zero_K_witness_LK={zero_lk:.17g}")
    for line in control_lines:
        print(line)
    print("universal_GU=OPEN")


if __name__ == "__main__":
    main()
