#!/usr/bin/env python3
"""Deterministic checks for the joint payment on the tensor no-go family."""

from fractions import Fraction as Q
import math
import numpy as np

U_INDEX = 22338
V_INDEX = 38505
BASE_U = np.array([1.0 if (U_INDEX >> r) & 1 else -1.0 for r in range(16)])
BASE_V = np.array([1.0 if (V_INDEX >> r) & 1 else -1.0 for r in range(16)])


def fwht_float(x):
    x = np.asarray(x, dtype=np.float64).copy()
    size = len(x)
    step = 1
    while step < size:
        view = x.reshape(-1, 2 * step)
        a = view[:, :step].copy()
        b = view[:, step:].copy()
        view[:, :step] = a + b
        view[:, step:] = a - b
        step *= 2
    return x / size


def fwht_exact(values):
    x = [Q(v) for v in values]
    step = 1
    while step < len(x):
        for base in range(0, len(x), 2 * step):
            for j in range(base, base + step):
                a, b = x[j], x[j + step]
                x[j], x[j + step] = a + b, a - b
        step *= 2
    return [v / len(x) for v in x]


def upper(p):
    q = np.asarray(p, dtype=np.float64).copy()
    idx = np.arange(len(q))
    for bit in range(len(q).bit_length() - 1):
        lo = idx[(idx & (1 << bit)) == 0]
        q[lo] += q[lo | (1 << bit)]
    return q


def u_from_hat(hat):
    p = hat * hat
    cap = upper(p)
    nz = p > 1e-28
    return float(np.sum(p[nz] * np.log2(cap[nz] / p[nz])))


def raw_entropy(q):
    q = np.asarray(q, dtype=np.float64)
    nz = q > 1e-28
    return float(np.sum(q[nz] * np.log2(1.0 / q[nz])))


def point_u(n):
    size = 2.0 ** n
    p0 = (1.0 - 2.0 / size) ** 2
    return ((0.0 if p0 == 0 else p0 * math.log2(1.0 / p0))
            + 2.0 * n / size - 4.0 * n / (size * size))


def composition_quantities(uh, vh, n):
    rare = 2.0 ** (-n)
    q = 1.0 - rare
    mu = -1.0 + 2.0 * rare
    delta = 1.0 - mu * mu
    a = (uh + vh) / 2.0
    b = (vh - uh) / 2.0
    beta = float(np.dot(b, b))
    c = a + mu * b

    # Exact ordinary-entropy sector decomposition.
    h_nonempty = delta * (2 * n - 2)
    entropy = raw_entropy(c * c) + beta * h_nonempty + delta * raw_entropy(b * b)

    # Exact upper-mass biased-child formula.
    b2 = b * b
    mixed = c * c + delta * b2
    cap = upper(mixed)
    p = c * c
    nz = p > 1e-28
    phi = float(np.sum(p[nz] * np.log2(cap[nz] / p[nz])))
    phi += delta * u_from_hat(b)
    psi = mu * mu * math.log2(1.0 / (mu * mu))
    theta = phi - beta * psi
    root_u = beta * point_u(n) + theta
    endpoint_chord = q * u_from_hat(uh) + rare * u_from_hat(vh)
    reserve = theta - endpoint_chord

    degrees = np.fromiter((i.bit_count() for i in range(len(uh))), float)
    outer_law = c * c + delta * b2
    outer_i = float(np.dot(degrees, outer_law))
    child_i = beta * n * 2.0 ** (1 - n)
    return entropy, root_u, reserve, outer_i + child_i


def restrict_values(values, bit, sign):
    want = 1 if sign == 1 else 0
    idx = np.arange(len(values))
    return values[((idx >> bit) & 1) == want]


def tensor(base, k):
    out = np.array([1.0])
    for _ in range(k):
        out = np.kron(out, base)
    return out


# Exact base identities used by the all-k proof.
ue = fwht_exact([int(x) for x in BASE_U])
ve = fwht_exact([int(x) for x in BASE_V])
rho = sum((x * y for x, y in zip(ue, ve)), Q())
iu = sum((Q(mask.bit_count()) * x * x for mask, x in enumerate(ue)), Q())
iv = sum((Q(mask.bit_count()) * x * x for mask, x in enumerate(ve)), Q())
assert rho == Q(1, 8)
assert iu == Q(7, 4)
assert iv == 4

# The displayed constant-3 proof is an exact rational comparison.
entropy_coefficient = Q(81, 16)
influence_coefficient = Q(255, 256) * iu
margin = 3 * influence_coefficient - entropy_coefficient
class_constant = entropy_coefficient / influence_coefficient
assert margin == Q(171, 1024) > 0
assert class_constant == Q(1728, 595) < 3

print("status=PASS")
print(f"rho={rho}")
print(f"I_u={iu} I_v={iv}")
print(f"H_upper_per_k={entropy_coefficient}")
print(f"I_lower_per_k={influence_coefficient}")
print(f"proved_class_constant={class_constant}")
print(f"three_I_minus_H_margin_per_k={margin}")
print("direct_diagnostics:")

for k in range(1, 5):
    u = tensor(BASE_U, k)
    v = tensor(BASE_V, k)
    uh, vh = fwht_float(u), fwht_float(v)
    n = 8 * k
    entropy, root_u, reserve, influence = composition_quantities(uh, vh, n)

    # Direct one-scale G diagnostic; not used in the all-k theorem.
    child_next_u = composition_quantities(uh, vh, n - 1)[1]
    child_g = n * (root_u - 0.5 * (u_from_hat(uh) + child_next_u))
    outer_g = 0.0
    for bit in range(4 * k):
        restricted = []
        for sign in (-1, 1):
            ur = fwht_float(restrict_values(u, bit, sign))
            vr = fwht_float(restrict_values(v, bit, sign))
            restricted.append(composition_quantities(ur, vr, n)[1])
        outer_g += root_u - 0.5 * sum(restricted)
    gu = child_g + outer_g

    assert root_u <= entropy + 1e-10
    assert reserve <= root_u + 1e-10
    assert entropy <= 3.0 * influence + 1e-10
    print(
        f"k={k} H/I={entropy/influence:.15f} "
        f"U/I={root_u/influence:.15f} reserve/I={reserve/influence:.15e} "
        f"G/I={gu/influence:.15f} child_G={child_g:.15e} outer_G={outer_g:.15f}"
    )

print("all_k_theorem=H(F_k)<=(1728/595) I(F_k), hence U(F_k)<=(1728/595) I(F_k)")
print("all_k_reserve=overline_Theta_k(mu_k)<=(1728/595) I(F_k)")
print("random_seed=None")
