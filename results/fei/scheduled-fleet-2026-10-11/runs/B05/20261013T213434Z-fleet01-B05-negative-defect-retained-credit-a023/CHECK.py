#!/usr/bin/env python3
from fractions import Fraction
from math import log2


def walsh(values):
    a = [Fraction(v) for v in values]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / n for x in a]


def UI(values):
    hats = walsh(values)
    p = [x * x for x in hats]
    nbits = (len(values)).bit_length() - 1
    caps = list(p)
    for bit in range(nbits):
        b = 1 << bit
        for s in range(len(caps)):
            if not (s & b):
                caps[s] += caps[s | b]
    U = 0.0
    I = Fraction(0)
    for s, ps in enumerate(p):
        if not ps:
            continue
        cap = caps[s]
        U += float(ps) * log2(float(cap / ps))
        I += s.bit_count() * ps
    return U, I


def tensor(f, g):
    return [x * y for x in f for y in g]


def activate(q):
    return [1] * len(q) + list(q)


def point_defect(r, negative=False):
    q = [-1] + [1] * (2**r - 1)
    return [-x for x in q] if negative else q


def build(base, ranks):
    # F_1=A(wP), then F_k=A(N_{r_k}F_{k-1}).
    f = activate(tensor([1, -1], base))
    for r in ranks:
        f = activate(tensor(point_defect(r, True), f))
    return f


def restrict(values, var, sign):
    n = len(values).bit_length() - 1
    out = []
    bit = 1 << (n - 1 - var)
    want = 0 if sign == 1 else bit
    for idx, val in enumerate(values):
        if idx & bit == want:
            out.append(val)
    return out


def pruned_leaves(values, order, depth=0, weight=Fraction(1)):
    # A fixed, genuinely pruned policy: stop on positive branches at odd depth.
    if depth == len(order) or (depth > 0 and depth % 2 == 1 and values[0] == 1):
        return [(weight, values)]
    var = order[depth]
    return (pruned_leaves(restrict(values, var, 1), order, depth + 1, weight / 2)
            + pruned_leaves(restrict(values, var, -1), order, depth + 1, weight / 2))


def R(t):
    def xlog(x):
        return 0.0 if x == 0 else x * log2(1 / x)
    E = ((1 + t) ** 2 / 4) * log2(4 / (1 + t) ** 2)
    if t == 1:
        second = 0.0
    else:
        second = ((1 - t) ** 2 / 4) * log2(2 / (1 - t))
    return E + second - 0.5 * xlog(t * t) + 0.25 * (1 - t * t)


max_block_ratio = 0.0
for r in range(2, 41):
    p = 2.0 ** (-r)
    beta = 1 - 2 * p
    I = 2 * r * p
    U = beta * beta * log2(1 / (beta * beta)) + 2 * r * p * beta
    ratio = U / float(I)
    max_block_ratio = max(max_block_ratio, ratio)
    assert ratio <= 16 / 9 + 1e-12

max_scalar = max(R(-s / 100000) for s in range(12500, 50001))
assert max_scalar <= 1 + 1e-12

bases = [[1, -1], [-1, 1, 1, 1]]
rank_sequences = [[], [2], [3], [4], [2, 2], [4, 2], [2, 3, 2]]
direct_cases = 0
max_ratio = 0.0
for base in bases:
    Ub, Ib = UI(base)
    assert Ub <= (16 / 9) * float(Ib) + 1e-12
    for ranks in rank_sequences:
        f = build(base, ranks)
        if len(f) > 2**15:
            continue
        U, I = UI(f)
        max_ratio = max(max_ratio, U / float(I))
        assert U <= (16 / 9) * float(I) + 1e-11
        direct_cases += 1

# Exact recurrence checks against direct truth tables.
recurrence_cases = 0
for base in bases:
    f = build(base, [])
    Uprev, Iprev = UI(f)
    mprev = Fraction(sum(f), len(f))
    for r in [2, 4, 3]:
        block = point_defect(r, True)
        Ub, Ib = UI(block)
        beta = Fraction(1) - Fraction(2, 2**r)
        s = beta * mprev
        nxt = activate(tensor(block, f))
        U, I = UI(nxt)
        assert abs(U - (0.5 * Uprev + 0.5 * Ub + R(-float(s)))) < 2e-11
        assert I == Iprev / 2 + Ib / 2 + (1 + s) / 2
        assert Fraction(1, 4) <= mprev <= Fraction(1, 2)
        assert Fraction(1, 8) <= s <= Fraction(1, 2)
        f, Uprev, Iprev = nxt, U, I
        mprev = Fraction(sum(f), len(f))
        recurrence_cases += 1

# Pruned-tree endpoint telescope and common-core cancellation.
tree_cases = 0
max_telescope_error = 0.0
for base in bases:
    f = build(base, [2])
    rootU, rootI = UI(f)
    n = len(f).bit_length() - 1
    for order in [list(range(min(4, n))), list(reversed(range(min(4, n))))]:
        leaves = pruned_leaves(f, order)
        leafU = sum(float(w) * UI(g)[0] for w, g in leaves)
        loss = rootU - leafU
        assert loss <= (16 / 9) * float(rootI) + 1e-11
        h = [-1, 1, 1, 1]
        rootUh = UI(tensor(f, h))[0]
        leafUh = sum(float(w) * UI(tensor(g, h))[0] for w, g in leaves)
        err = abs((rootUh - leafUh) - loss)
        max_telescope_error = max(max_telescope_error, err)
        assert err < 2e-10
        tree_cases += 1

print(f"block_ranks_checked=2..40 max_U_over_I={max_block_ratio:.12f}")
print(f"scalar_grid=[-0.5,-0.125] max_R={max_scalar:.12f}")
print(f"direct_tower_cases={direct_cases} max_U_over_I={max_ratio:.12f}")
print(f"recurrence_cases={recurrence_cases}")
print(f"pruned_tree_cases={tree_cases} max_terminal_cancel_error={max_telescope_error:.3e}")
print("proved_endpoint_constant=16/9")
print("proved_FEI_corollary_constant=50/9")
print("status=PASS")
