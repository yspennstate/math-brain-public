#!/usr/bin/env python3
"""Independent reconstruction of B05's half-packet activation invariant."""
from fractions import Fraction
from itertools import product as cartesian
from math import log, log2
from random import Random


LN2 = log(2.0)
AUTHOR_CSTAR = Fraction(29, 2) + 4 / LN2
REVIEW_CSTAR = Fraction(29, 2) + 2 / LN2


def xlog_ratio(x, total):
    return 0.0 if x == 0 else float(x) * log2(float(total / x))


def pair_entropy(a, b):
    return xlog_ratio(a, a + b) + xlog_ratio(b, a + b)


def upper_masses(p):
    ans = list(p)
    n = len(ans).bit_length() - 1
    for j in range(n):
        bit = 1 << j
        for s in range(len(ans)):
            if s & bit == 0:
                ans[s] += ans[s | bit]
    return ans


def walsh(values):
    out = [Fraction(v) for v in values]
    step = 1
    while step < len(out):
        for base in range(0, len(out), 2 * step):
            for k in range(base, base + step):
                a, b = out[k], out[k + step]
                out[k], out[k + step] = a + b, a - b
        step *= 2
    return [a / len(out) for a in out]


def restriction(values, coordinate, bit):
    n = len(values).bit_length() - 1
    result = []
    for t in range(1 << (n - 1)):
        low = t & ((1 << coordinate) - 1)
        high = t >> coordinate
        result.append(values[low | (bit << coordinate) | (high << (coordinate + 1))])
    return tuple(result)


def q(t):
    if t == 0:
        return 0.0
    return t * log2(1.0 / t) + 2.0 * t / LN2


def statistics(values):
    coeff = walsh(values)
    p = [a * a for a in coeff]
    pi = upper_masses(p)
    n = len(values).bit_length() - 1
    U = sum(xlog_ratio(a, b) for a, b in zip(p, pi))
    I = sum(s.bit_count() * float(a) for s, a in enumerate(p))
    B = 0.0
    for j in range(n):
        bit = 1 << j
        B += sum(pair_entropy(p[s], p[s | bit]) for s in range(len(p)) if not s & bit)
    G = n * U
    for j in range(n):
        G -= sum(statistics_base(restriction(values, j, bit))[0] for bit in (0, 1)) / 2
    phi = sum(q(float(p[1 << j])) for j in range(n))
    return {"U": U, "I": I, "B": B, "G": G, "M": G - B,
            "phi": phi, "coeff": coeff, "p": p}


def statistics_base(values):
    coeff = walsh(values)
    p = [a * a for a in coeff]
    pi = upper_masses(p)
    U = sum(xlog_ratio(a, b) for a, b in zip(p, pi))
    I = sum(s.bit_count() * float(a) for s, a in enumerate(p))
    return U, I


def activation(values):
    # Last coordinate selects the core on bit 0 and the constant +1 on bit 1.
    return tuple(values) + (1,) * len(values)


def tensor(values, other):
    return tuple(a * b for b in other for a in values)


def R(m):
    p = [(1 + m) ** 2 / 4, (1 - m * m) / 4,
         (1 - m) ** 2 / 4, (1 - m * m) / 4]
    u = sum(xlog_ratio(a, b) for a, b in zip(p, upper_masses(p)))
    return u - xlog_ratio(m * m, 1.0) / 2


def C(m, p):
    return (-pair_entropy(m * m, p) / 2
            + pair_entropy((1 + m) ** 2, p) / 4
            + pair_entropy((1 - m) ** 2, p) / 4)


def P(m, a):
    return R(m) - (R(m - a) + R(m + a)) / 2 - C(m, a * a)


def L(stats, eta, c=REVIEW_CSTAR):
    return stats["M"] + (1 + eta) * stats["U"] - float(c) * stats["I"]


def invariant(stats, eta, c=REVIEW_CSTAR):
    return L(stats, eta, c) + 2 * stats["phi"]


def scalar_reconstruction():
    tested = 0
    max_ratio = (-1e100, None)
    N = 850
    for jm in range(N + 1):
        m = -1 + 2 * jm / N
        room = 1 - abs(m)
        for ja in range(1, N + 1):
            a = room * ja / N
            if not a:
                continue
            residual = P(m, a) - q(a * a) / 2
            assert residual <= 7e-12
            ratio = P(m, a) / q(a * a)
            max_ratio = max(max_ratio, (ratio, (m, a)))
            tested += 1
    # Explicit rare/boundary probes not represented well by an affine grid.
    rare = 0
    for exponent in range(2, 15):
        a = 10.0 ** (-exponent)
        for r in (-1e4, -100, -1, 0, 1, 100, 1e4):
            m = r * a
            if abs(m) + a <= 1:
                assert P(m, a) <= q(a * a) / 2 + 1e-14
                rare += 1
    return tested, rare, max_ratio


def analytic_shape_checks():
    # These are the explicit derivatives in the proof, not numerical differentiation.
    inside = outside = 0
    for j in range(1, 200000):
        r = j / 200000
        psi3 = (2*r/(1+r*r) + 2*r/(1-r*r)
                + 4*r/(1+r*r)**2)
        assert psi3 > 0
        inside += 1
    for j in range(1, 200000):
        r = 1 + 30 * j / 200000
        psi2 = log((1+r*r)/(r*r-1)) - 2/(1+r*r)
        assert psi2 > 0
        outside += 1
    return inside, outside


def selector_reserve_checks():
    # Exact bracket after division by J:
    # 4(1-J)+4J log_2(1/J)+4J/ln2 <= 4+2/ln2.
    tests = 0
    max_value = (-1e100, None)
    for j in range(1, 1000001):
        J = j / 1000000
        value = 4*(1-J) + 4*J*log2(1/J) + 4*J/LN2
        assert value <= 4 + 2/LN2 + 2e-14
        max_value = max(max_value, (value, J))
        tests += 1
    # The derivative is 4(log_2(1/J)-1), hence the exact maximizer is J=1/2.
    assert abs(max_value[1] - 0.5) <= 1e-6
    assert abs(max_value[0] - (4 + 2/LN2)) <= 2e-12
    return tests, max_value


def boolean_and_activation_checks():
    rng = Random(191014)
    functions = []
    for n in range(4):
        length = 1 << n
        for mask in range(1 << length):
            functions.append(tuple(1 if mask & (1 << k) else -1 for k in range(length)))
    for n in range(4, 8):
        length = 1 << n
        for _ in range(64):
            functions.append(tuple(1 if rng.randrange(2) else -1 for _ in range(length)))

    etas = (1e-6, 0.125, 0.5, 0.999999, 1.0)
    activation_tests = phi_identity_tests = 0
    max_contraction = -1e100
    for values in functions:
        s = statistics(values)
        sa = statistics(activation(values))
        m = float(s["coeff"][0])
        J = (1 - m) / 2
        w1 = sum(float(s["p"][1 << j]) for j in range(len(values).bit_length() - 1))
        phi_formula = q(J*J) + s["phi"] / 4 + w1 / 2
        assert abs(sa["phi"] - phi_formula) <= 3e-12
        phi_identity_tests += 1
        for eta in etas:
            residual = invariant(sa, eta) - invariant(s, eta) / 2
            assert residual <= 4e-10
            max_contraction = max(max_contraction, residual)
            activation_tests += 1
    return len(functions), activation_tests, phi_identity_tests, max_contraction


def product_checks():
    two_bit = []
    for mask in range(16):
        two_bit.append(tuple(1 if mask & (1 << j) else -1 for j in range(4)))
    count = 0
    max_phi = max_l = -1e100
    for f, g in cartesian(two_bit, repeat=2):
        sf, sg, sh = statistics(f), statistics(g), statistics(tensor(f, g))
        phi_res = sh["phi"] - sf["phi"] - sg["phi"]
        l_res = L(sh, 1.0) - L(sf, 1.0) - L(sg, 1.0)
        assert phi_res <= 2e-12
        assert abs(l_res) <= 2e-12
        max_phi, max_l = max(max_phi, phi_res), max(max_l, abs(l_res))
        count += 1
    return count, max_phi, max_l


def generated_restriction_checks():
    rng = Random(94023)
    pool = [(1,), (-1,), (-1, 1), (1, -1)]
    nodes = restrictions = 0
    max_inv = -1e100
    for _ in range(180):
        f = rng.choice([v for v in pool if len(v) <= 128])
        if rng.random() < 0.7:
            h = activation(f)
        else:
            g = rng.choice([v for v in pool if len(v) * len(f) <= 256])
            h = tensor(f, g)
        pool.append(h)
        sh = statistics(h)
        value = invariant(sh, 1.0)
        assert value <= 8e-9
        max_inv = max(max_inv, value)
        nodes += 1
        n = len(h).bit_length() - 1
        for j in range(n):
            for bit in (0, 1):
                sr = statistics(restriction(h, j, bit))
                value = invariant(sr, 1.0)
                assert value <= 8e-9
                max_inv = max(max_inv, value)
                restrictions += 1
    return nodes, restrictions, max_inv


scalar = scalar_reconstruction()
shape = analytic_shape_checks()
boolean = boolean_and_activation_checks()
products = product_checks()
generated = generated_restriction_checks()
selector = selector_reserve_checks()

print("status=PASS")
print("scalar_grid_tests=", scalar[0])
print("scalar_rare_boundary_tests=", scalar[1])
print("max_P_over_q=", scalar[2])
print("analytic_inside_derivative_tests=", shape[0])
print("analytic_outside_derivative_tests=", shape[1])
print("selector_reserve_tests=", selector[0])
print("max_selector_reserve_ratio=", selector[1])
print("boolean_cores=", boolean[0])
print("activation_eta_tests=", boolean[1])
print("phi_identity_tests=", boolean[2])
print("max_augmented_contraction_residual=", boolean[3])
print("product_pairs=", products[0])
print("max_product_phi_residual=", products[1])
print("max_product_L_absolute_error=", products[2])
print("generated_nodes=", generated[0])
print("generated_restrictions=", generated[1])
print("max_generated_invariant=", generated[2])
print("author_c_star=", float(AUTHOR_CSTAR))
print("review_c_star=", float(REVIEW_CSTAR))
print("review_GU_constant=", float(REVIEW_CSTAR) + 2)
print("review_FEI_constant=", 2 + 2 * (float(REVIEW_CSTAR) + 2))
