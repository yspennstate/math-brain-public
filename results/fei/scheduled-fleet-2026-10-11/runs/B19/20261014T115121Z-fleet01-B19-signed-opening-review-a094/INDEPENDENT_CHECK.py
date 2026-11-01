#!/usr/bin/env python3
"""Independent finite audit of B05 signed-opening history transfer.

This implementation was written from the definitions.  It uses exact
rational Walsh coefficients and floating logarithms only after the masses
have been formed exactly.  Finite tests are regression evidence, not the
proof of the universal statement.
"""
from fractions import Fraction
from itertools import product
from math import log, log2
from random import Random


def entropy_pair(a, b):
    total = a + b
    ans = 0.0
    for x in (a, b):
        if x:
            ans += float(x) * log2(float(total / x))
    return ans


def upper_term(mass, cap):
    return 0.0 if mass == 0 else float(mass) * log2(float(cap / mass))


def packet(t):
    if t == 0:
        return 0.0
    x = float(t)
    return x * log2(1.0 / x) + 2.0 * x / log(2.0)


def walsh(values):
    coeff = [Fraction(x) for x in values]
    step = 1
    while step < len(coeff):
        for start in range(0, len(coeff), 2 * step):
            for j in range(start, start + step):
                u, v = coeff[j], coeff[j + step]
                coeff[j], coeff[j + step] = u + v, u - v
        step *= 2
    scale = len(coeff)
    return [x / scale for x in coeff]


def zeta_upper(masses):
    out = list(masses)
    n = len(out).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(out)):
            if not (s & bit):
                out[s] += out[s | bit]
    return out


def restriction(values, coordinate, value_bit):
    n = len(values).bit_length() - 1
    ans = []
    for s in range(1 << (n - 1)):
        low = s & ((1 << coordinate) - 1)
        high = s >> coordinate
        index = low | (value_bit << coordinate) | (high << (coordinate + 1))
        ans.append(values[index])
    return tuple(ans)


def raw(values):
    hat = walsh(values)
    p = [x * x for x in hat]
    cap = zeta_upper(p)
    n = len(values).bit_length() - 1
    U = sum(upper_term(x, y) for x, y in zip(p, cap))
    I = sum(s.bit_count() * float(x) for s, x in enumerate(p))
    B = 0.0
    influence = []
    for i in range(n):
        bit = 1 << i
        influence.append(sum((p[s] for s in range(len(p)) if s & bit), Fraction(0)))
        B += sum(entropy_pair(p[s], p[s | bit]) for s in range(len(p)) if not (s & bit))
    return {"hat": hat, "p": p, "U": U, "I": I, "B": B, "inf": influence}


def functionals(values):
    d = raw(values)
    n = len(values).bit_length() - 1
    G = n * d["U"]
    for i in range(n):
        G -= 0.5 * raw(restriction(values, i, 0))["U"]
        G -= 0.5 * raw(restriction(values, i, 1))["U"]
    d["G"] = G
    d["M"] = G - d["B"]
    return d


def Phi(data):
    n = len(data["p"]).bit_length() - 1
    return sum(packet(data["p"][1 << i]) for i in range(n))


def orbit_energy(data, X, i):
    total = Fraction(0)
    sub = X
    while True:
        total += data["p"][(1 << i) | sub]
        if sub == 0:
            return total
        sub = (sub - 1) & X


def Theta(data, X):
    n = len(data["p"]).bit_length() - 1
    inside = sum(packet(data["inf"][i]) for i in range(n) if X & (1 << i))
    outside = sum(packet(orbit_energy(data, X, i)) for i in range(n) if not (X & (1 << i)))
    return inside + outside


def activate(values):
    # Fresh last coordinate z: z=0 is the core and z=1 is constant +1.
    return tuple(values) + (1,) * len(values)


def L(data, c, eta):
    return data["M"] + (1.0 + eta) * data["U"] - c * data["I"]


def all_boolean(n):
    for bits in product((-1, 1), repeat=1 << n):
        yield bits


rng = Random(19094291)
cores = []
for n in range(4):
    cores.extend(all_boolean(n))
for n in range(4, 7):
    for _ in range(24):
        cores.append(tuple(rng.choice((-1, 1)) for _ in range(1 << n)))

c_star = 29.0 / 2.0 + 4.0 / log(2.0)
node_checks = 0
identity_checks = 0
max_signed_drift = -1e300
max_ro_error = 0.0
min_domination_gap = 1e300

for core in cores:
    n = len(core).bit_length() - 1
    activated = activate(core)
    dc = functionals(core)
    da = functionals(activated)
    phic, phia = Phi(dc), Phi(da)
    z = 1 << n
    blocks = list(range(1 << n)) if n <= 3 else [0, (1 << n) - 1] + [rng.randrange(1 << n) for _ in range(18)]
    for X in blocks:
        theta_core = Theta(dc, X)
        theta_open = Theta(da, X | z)
        # Direct definitions with inherited block empty.
        opening = theta_open - phia
        reveal = theta_open - 0.5 * theta_core  # constant child contributes zero
        signed_direct = reveal - opening
        signed_simplified = phia - 0.5 * theta_core
        max_ro_error = max(max_ro_error, abs(signed_direct - signed_simplified))
        min_domination_gap = min(min_domination_gap, theta_core - phic)
        assert abs(signed_direct - signed_simplified) < 5e-13
        assert theta_core + 5e-13 >= phic
        identity_checks += 1
        for eta in (0.125, 0.25, 0.5, 1.0):
            delta_L = L(da, c_star, eta) - 0.5 * L(dc, c_star, eta)
            drift = delta_L + 2.0 * signed_direct
            max_signed_drift = max(max_signed_drift, drift)
            assert drift <= 3e-10, (n, X, eta, drift)
            node_checks += 1

print("status=PASS")
print(f"c_star={c_star:.15f}")
print(f"cores={len(cores)}")
print(f"identity_checks={identity_checks}")
print(f"signed_node_checks={node_checks}")
print(f"max_abs_R_minus_O_identity_error={max_ro_error:.3e}")
print(f"min_Theta_minus_Phi={min_domination_gap:.15g}")
print(f"max_signed_node_drift={max_signed_drift:.15g}")
print("seed=19094291")
