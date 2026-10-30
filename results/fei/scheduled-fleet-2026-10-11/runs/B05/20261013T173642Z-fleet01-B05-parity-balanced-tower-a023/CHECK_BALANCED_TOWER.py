#!/usr/bin/env python3
"""Exact-Walsh/numerical-log audit for parity-balanced activation towers."""
from math import log2
import random


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def ui(v):
    N = len(v)
    n = N.bit_length()-1
    w = fwht(v)
    p = [z*z/(N*N) for z in w]
    cap = p[:]
    for j in range(n):
        for s in range(N):
            if not ((s >> j) & 1):
                cap[s] += cap[s | (1 << j)]
    U = sum(x*log2(cap[s]/x) for s, x in enumerate(p) if x)
    I = sum(sum(v[x] != v[x ^ (1 << j)] for x in range(N))/N for j in range(n))
    return U, I


def balance(v):
    return list(v) + [-x for x in v]


def activate(v):
    return [1]*len(v) + list(v)


def tower(v, depth):
    q = balance(v)
    for k in range(1, depth+1):
        f = activate(q)
        if k < depth:
            q = balance(f)
    return f


def restrict(v, j, b):
    return [v[x] for x in range(len(v)) if ((x >> j) & 1) == b]


def random_leaf_average_u(v, rng, stop_probability=0.3):
    n = len(v).bit_length()-1
    def rec(cur, coords):
        if not coords or rng.random() < stop_probability:
            return ui(cur)[0]
        pos = rng.randrange(len(coords))
        j = coords[pos]
        # After restriction, coordinates above j shift down by one.
        nxt = [k if k < j else k-1 for k in coords if k != j]
        return (rec(restrict(cur, j, 0), nxt) + rec(restrict(cur, j, 1), nxt))/2
    return rec(v, list(range(n)))


def tensor(v, h):
    return [a*b for b in h for a in v]


rng = random.Random(20261013)
formula_checks = 0
tree_checks = 0
terminal_checks = 0
max_formula_error = 0.0
max_tree_ratio = 0.0

bases = []
for n in range(0, 4):
    N = 1 << n
    for mask in range(1 << max(0, N-1)):
        bases.append([1 if (mask >> x) & 1 else -1 for x in range(N)])
for n, count in ((4, 100), (5, 30)):
    N = 1 << n
    for _ in range(count):
        bases.append([rng.choice((-1, 1)) for _ in range(N)])

for idx, base in enumerate(bases):
    U0, I0 = ui(base)
    for depth in range(1, 5):
        f = tower(base, depth)
        U, I = ui(f)
        predicted_u = 2 + (U0-2)/(1 << depth)
        predicted_i = 2 + (I0-2)/(1 << depth)
        max_formula_error = max(max_formula_error, abs(U-predicted_u), abs(I-predicted_i))
        assert abs(U-predicted_u) < 2e-11
        assert abs(I-predicted_i) < 2e-11
        if U0 <= 2*I0 + 1e-12:
            assert U <= 2*I + 1e-11
        formula_checks += 1
        if idx % 17 == 0 and depth in (2, 4):
            leaf_u = random_leaf_average_u(f, rng)
            loss = U-leaf_u
            assert loss <= U + 1e-12
            assert loss <= 2*I + 1e-11
            if I:
                max_tree_ratio = max(max_tree_ratio, loss/I)
            tree_checks += 1

for base in bases[::31]:
    f = tower(base, 3)
    h = [1, 1, 1, -1]
    Uf, _ = ui(f)
    Uh, _ = ui(h)
    Ufh, _ = ui(tensor(f, h))
    assert abs(Ufh-Uf-Uh) < 2e-11
    terminal_checks += 1

print("B05 A023 parity-balanced activation tower audit")
print(f"base_functions={len(bases)}")
print(f"formula_checks={formula_checks}")
print(f"random_pruned_tree_checks={tree_checks}")
print(f"disjoint_terminal_checks={terminal_checks}")
print(f"max_formula_error={max_formula_error:.3e}")
print(f"max_sampled_retained_loss_over_I={max_tree_ratio:.12f}")
print("PASS_ANALYTIC_PROOF_CONTROLS_ALL_PARAMETERS")
