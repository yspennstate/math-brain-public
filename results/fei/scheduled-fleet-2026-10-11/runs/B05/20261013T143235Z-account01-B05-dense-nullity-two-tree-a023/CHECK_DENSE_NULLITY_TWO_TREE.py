#!/usr/bin/env python3
"""Direct checks for the dense-nullity-two retained-U tree theorem."""

from fractions import Fraction
from itertools import product
from math import log2
import random

SEED = 0xB05A0232
rng = random.Random(SEED)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b)) & 1


def rank(rows):
    if not rows:
        return 0
    a = [sum(bit << j for j, bit in enumerate(row)) for row in rows]
    out = 0
    for j in range(len(rows[0])):
        p = next((i for i in range(out, len(a)) if (a[i] >> j) & 1), None)
        if p is None:
            continue
        a[out], a[p] = a[p], a[out]
        for i in range(len(a)):
            if i != out and ((a[i] >> j) & 1):
                a[i] ^= a[out]
        out += 1
    return out


def fwht(vals):
    a = list(map(int, vals))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                a[j], a[j + h] = a[j] + a[j + h], a[j] - a[j + h]
        h *= 2
    return a


def spectrum(vals):
    den = len(vals) ** 2
    return [Fraction(z * z, den) for z in fwht(vals)]


def entropy(vals):
    return sum(-float(q) * log2(float(q)) for q in spectrum(vals) if q)


def upper_u(vals):
    p = spectrum(vals)
    n = len(vals).bit_length() - 1
    pi = p[:]
    for j in range(n):
        for s in range(1 << n):
            if not ((s >> j) & 1):
                pi[s] += pi[s | (1 << j)]
    return sum(float(q) * log2(float(pi[s] / q)) for s, q in enumerate(p) if q)


def influence(vals, j=None):
    n = len(vals).bit_length() - 1
    js = range(n) if j is None else [j]
    return sum(Fraction(sum(vals[x] != vals[x ^ (1 << k)] for x in range(1 << n)), 1 << n) for k in js)


def restrict(vals, j, bit):
    n = len(vals).bit_length() - 1
    out = []
    for z in range(1 << (n - 1)):
        low = z & ((1 << j) - 1)
        high = z >> j
        x = low | (bit << j) | (high << (j + 1))
        out.append(vals[x])
    return out


def build_phase(rows, dvals):
    s, m = len(rows), len(rows[0]) if rows else 2
    vals = []
    for w in range(1 << (s + m)):
        x = tuple((w >> j) & 1 for j in range(s))
        y = tuple((w >> (s + j)) & 1 for j in range(m))
        phase = 0
        for i in range(s):
            if x[i]:
                phase ^= dot(rows[i], y)
        vals.append((1 if phase == 0 else -1) * dvals[sum(y[j] << j for j in range(m))])
    return vals


def all_rank_rows(s, m, target):
    for flat in product((0, 1), repeat=s * m):
        rows = [flat[i * m:(i + 1) * m] for i in range(s)]
        if rank(rows) == target:
            yield rows


def random_tree_leaves(vals, available, stop_probability=0.28):
    if not available or rng.random() < stop_probability:
        return [(Fraction(1), vals)]
    j = rng.choice(available)
    rest = [k for k in available if k != j]
    # Indices above j shift down in the child truth table.
    rest_child = [k if k < j else k - 1 for k in rest]
    out = []
    for bit in (0, 1):
        for w, leaf in random_tree_leaves(restrict(vals, j, bit), rest_child, stop_probability):
            out.append((w / 2, leaf))
    return out


def order_ledger(vals, order):
    frontier = [(Fraction(1), vals, list(range(len(vals).bit_length() - 1)))]
    charges = []
    consumed = []
    for original_j in order:
        charge = 0.0
        inf = Fraction(0)
        new = []
        for w, f, labels in frontier:
            j = labels.index(original_j)
            kids = [restrict(f, j, bit) for bit in (0, 1)]
            charge += float(w) * (upper_u(f) - (upper_u(kids[0]) + upper_u(kids[1])) / 2)
            inf += w * influence(f, j)
            child_labels = labels[:j] + labels[j + 1:]
            new.extend([(w / 2, kids[0], child_labels), (w / 2, kids[1], child_labels)])
        charges.append(charge)
        consumed.append(inf)
        frontier = new
    return charges, consumed


def tensor(f, g):
    return [f[x] * g[y] for y in range(len(g)) for x in range(len(f))]


root_cases = 0
tree_cases = 0
tensor_checks = 0
max_u_over_i = 0.0
max_tree_loss_over_i = 0.0

# Exhaust every rank-one orientation on three y bits and every Boolean core
# modulo output complement.
for rows in all_rank_rows(1, 3, 1):
    for mask in range(1 << 7):
        d = [1 if (mask >> y) & 1 else -1 for y in range(8)]
        f = build_phase(rows, d)
        I = influence(f)
        U = upper_u(f)
        assert U <= entropy(f) + 1e-12 <= 2 * float(I) + 2e-11
        root_cases += 1
        if I:
            max_u_over_i = max(max_u_over_i, U / float(I))
        for _ in range(3):
            leaves = random_tree_leaves(f, list(range(4)))
            leaf_u = sum(float(w) * upper_u(g) for w, g in leaves)
            loss = U - leaf_u
            assert loss <= 2 * float(I) + 2e-11
            tree_cases += 1
            if I:
                max_tree_loss_over_i = max(max_tree_loss_over_i, loss / float(I))

# All rank-two 2x4 orientations with deterministic random cores.
for rows in all_rank_rows(2, 4, 2):
    for _ in range(8):
        d = [rng.choice((-1, 1)) for _ in range(16)]
        f = build_phase(rows, d)
        I, U = influence(f), upper_u(f)
        assert U <= entropy(f) + 1e-12 <= 2 * float(I) + 2e-11
        leaves = random_tree_leaves(f, list(range(6)))
        loss = U - sum(float(w) * upper_u(g) for w, g in leaves)
        assert loss <= 2 * float(I) + 2e-11
        root_cases += 1
        tree_cases += 1
        if I:
            max_u_over_i = max(max_u_over_i, U / float(I))
            max_tree_loss_over_i = max(max_tree_loss_over_i, loss / float(I))

# Common disjoint terminal cores cancel exactly from the retained loss.
for _ in range(120):
    rows = rng.choice(list(all_rank_rows(1, 3, 1)))
    d = [rng.choice((-1, 1)) for _ in range(8)]
    f = build_phase(rows, d)
    h = [rng.choice((-1, 1)) for _ in range(8)]
    j = rng.randrange(4)
    tf = tensor(f, h)
    kids = [restrict(f, j, bit) for bit in (0, 1)]
    # f variables occupy the low bits in tensor().
    tkids = [restrict(tf, j, bit) for bit in (0, 1)]
    lhs = upper_u(tf) - sum(upper_u(q) for q in tkids) / 2
    rhs = upper_u(f) - sum(upper_u(q) for q in kids) / 2
    assert abs(lhs - rhs) < 2e-11
    tensor_checks += 1

# Ordering comparison on the one-row-release suspension of the nullity-three
# point-defect boundary.  Both complete ledgers telescope to the same root U,
# although their signed level charges differ.
rows = [(1, 1, 0, 0), (0, 0, 1, 0)]
d = []
for y in range(16):
    y1, y2, y3, y4 = ((y >> j) & 1 for j in range(4))
    d.append(-1 if (y1 == 0 and y3 == 0 and y4 == 0) else 1)
suspension = build_phase(rows, d)
control_first = [0, 1, 2, 3, 4, 5]
data_first = [2, 3, 4, 5, 0, 1]
ctl_charge, ctl_inf = order_ledger(suspension, control_first)
dat_charge, dat_inf = order_ledger(suspension, data_first)
root_u = upper_u(suspension)
assert abs(sum(ctl_charge) - root_u) < 2e-11
assert abs(sum(dat_charge) - root_u) < 2e-11
assert sum(ctl_inf) == influence(suspension)
assert sum(dat_inf) == influence(suspension)

print(f"seed={SEED}")
print(f"root_cases={root_cases}")
print(f"adaptive_pruned_tree_cases={tree_cases}")
print(f"disjoint_terminal_cancellation_checks={tensor_checks}")
print(f"maximum_sampled_U_over_I={max_u_over_i:.15f}")
print(f"maximum_sampled_tree_loss_over_I={max_tree_loss_over_i:.15f}")
print(f"ordering_suspension_root_U={root_u:.15f}")
print("control_first_signed_level_charges=" + ",".join(f"{x:.15f}" for x in ctl_charge))
print("data_first_signed_level_charges=" + ",".join(f"{x:.15f}" for x in dat_charge))
print("control_first_consumed_influences=" + ",".join(str(x) for x in ctl_inf))
print("data_first_consumed_influences=" + ",".join(str(x) for x in dat_inf))
print("PASS")
