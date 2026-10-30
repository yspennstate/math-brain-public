#!/usr/bin/env python3
import math
import random

TOL = 3e-10
C0 = 2.0 / math.log(2.0)


def walsh(table):
    a = list(map(float, table))
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / n for x in a]


def ui(table):
    coeff = walsh(table)
    n = len(table).bit_length() - 1
    p = [x * x for x in coeff]
    upper = p[:]
    for bit in range(n):
        for s in range(1 << n):
            if not ((s >> bit) & 1):
                upper[s] += upper[s | (1 << bit)]
    U = sum(p[s] * math.log2(upper[s] / p[s]) for s in range(1 << n) if p[s] > 1e-300)
    I = sum(s.bit_count() * p[s] for s in range(1 << n))
    return U, I


def restrict(table, n, i, bit):
    return [v for x, v in enumerate(table) if ((x >> i) & 1) == bit]


def influence(table, n, i):
    return sum(
        table[x] != table[x | (1 << i)]
        for x in range(1 << n)
        if not ((x >> i) & 1)
    ) / (1 << (n - 1))


def root_kl(table, n, i):
    a = sum(table) / len(table)
    d = sum(v * (1 if (x >> i) & 1 else -1) for x, v in enumerate(table)) / len(table)
    m = a * a + d * d
    if m < 1e-300:
        return 0.0
    t = (1.0 + 2.0 * a * d / m) / 2.0
    h = 0.0 if t <= 0.0 or t >= 1.0 else -t * math.log2(t) - (1.0 - t) * math.log2(1.0 - t)
    return m * (1.0 - h)


def G(table):
    n = len(table).bit_length() - 1
    u, _ = ui(table)
    total = 0.0
    for i in range(n):
        u0, _ = ui(restrict(table, n, i, 0))
        u1, _ = ui(restrict(table, n, i, 1))
        total += u - (u0 + u1) / 2.0
    return total


def product(q, h):
    # Gate bits are the two low bits; core bits occupy the remaining positions.
    return [q[x & 3] * h[x >> 2] for x in range(4 * len(h))]


def reused_tree_ledger(F):
    n = len(F).bit_length() - 1
    U0, I0 = ui(F)
    q0 = influence(F, n, 0)
    k0 = root_kl(F, n, 0)
    sum_du = 0.0
    sum_inf = q0
    sum_k0 = k0
    leaves = []
    u_children = []
    for b0 in (0, 1):
        child = restrict(F, n, 0, b0)
        uc, _ = ui(child)
        u_children.append(uc)
        u_grand = []
        for b1 in (0, 1):
            leaf = restrict(child, n - 1, 0, b1)
            leaves.append(leaf)
            ul, _ = ui(leaf)
            u_grand.append(ul)
        sum_du += 0.5 * (uc - sum(u_grand) / 2.0)
        sum_inf += 0.5 * influence(child, n - 1, 0)
        sum_k0 += 0.5 * root_kl(child, n - 1, 0)
    sum_du += U0 - sum(u_children) / 2.0
    leaf_u = sum(ui(x)[0] for x in leaves) / 4.0
    leaf_i = sum(ui(x)[1] for x in leaves) / 4.0
    residual = sum_du - sum_k0
    return U0, I0, sum_du, sum_inf, sum_k0, leaf_u, leaf_i, residual


def tables(n):
    size = 1 << n
    for mask in range(1 << size):
        yield [1 if (mask >> x) & 1 else -1 for x in range(size)]


rng = random.Random(20261014)
gate_cases = product_cases = assertions = 0
max_add_u = max_add_i = max_add_g = 0.0
max_u_gate_surplus = max_gu_gate_surplus = 0.0
max_tree_residual_surplus = max_tree_telescope_error = 0.0

gates = list(tables(2))
cores = [[1], [-1]]
for m in range(1, 4):
    cores.extend(tables(m))
for m in range(4, 7):
    for _ in range(120):
        cores.append([rng.choice((-1, 1)) for _ in range(1 << m)])

for q in gates:
    Uq, Iq = ui(q)
    Gq = G(q)
    gate_cases += 1
    max_u_gate_surplus = max(max_u_gate_surplus, Uq - Iq)
    assert Uq <= Iq + TOL
    for b in (0.0, 0.25, 0.5, 0.75, 0.99):
        surplus = Gq - ((2.0 - b) * Iq + b * Uq)
        max_gu_gate_surplus = max(max_gu_gate_surplus, surplus)
        assertions += 1
        assert surplus <= TOL
    for h in cores:
        F = product(q, h)
        Uh, Ih, Gh = *ui(h), G(h)
        Uf, If = ui(F)
        Gf = G(F)
        max_add_u = max(max_add_u, abs(Uf - Uq - Uh))
        max_add_i = max(max_add_i, abs(If - Iq - Ih))
        max_add_g = max(max_add_g, abs(Gf - Gq - Gh))
        assertions += 3
        assert abs(Uf - Uq - Uh) <= TOL
        assert abs(If - Iq - Ih) <= TOL
        assert abs(Gf - Gq - Gh) <= TOL

        U0, I0, sum_du, pi_i, sum_k, leaf_u, leaf_i, residual = reused_tree_ledger(F)
        telescope_error = max(abs(sum_du - (U0 - leaf_u)), abs(pi_i - (I0 - leaf_i)))
        residual_surplus = residual - pi_i
        max_tree_telescope_error = max(max_tree_telescope_error, telescope_error)
        max_tree_residual_surplus = max(max_tree_residual_surplus, residual_surplus)
        assertions += 4
        assert telescope_error <= TOL
        assert residual_surplus <= TOL
        assert abs(leaf_u - Uh) <= TOL
        assert abs(leaf_i - Ih) <= TOL

        for b in (0.0, 0.5, 0.75):
            ah = 0.0 if Ih <= TOL else max(0.0, (Gh - b * Uh) / Ih)
            a = max(ah, 2.0 - b)
            assertions += 1
            assert Gf <= a * If + b * Uf + TOL
        product_cases += 1

print("claim=B06-A028-TWO-GATE-REUSE-v1")
print("verdict=PASS_AT_STATED_ALL_DIMENSIONAL_PRODUCT_SCOPE")
print("two_bit_gate_cases", gate_cases)
print("gate_core_product_cases", product_cases)
print("assertions", assertions)
print("max_U_gate_minus_I_gate", f"{max_u_gate_surplus:.3e}")
print("max_GU_gate_surplus", f"{max_gu_gate_surplus:.3e}")
print("max_U_additivity_error", f"{max_add_u:.3e}")
print("max_I_additivity_error", f"{max_add_i:.3e}")
print("max_G_additivity_error", f"{max_add_g:.3e}")
print("max_tree_telescope_error", f"{max_tree_telescope_error:.3e}")
print("max_residual_minus_queried_influence", f"{max_tree_residual_surplus:.3e}")
print("universal_shared_data_extension=OPEN")
print("universal_GU=OPEN")
