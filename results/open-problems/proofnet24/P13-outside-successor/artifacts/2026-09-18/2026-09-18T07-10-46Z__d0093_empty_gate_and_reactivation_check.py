#!/usr/bin/env python3
"""Exact finite self-check for P13 D0093, run 6.

Checks two finite claims used only as self-checks in the accompanying report:
1. For the empty-background nearest-neighbor jump chain on [-L,1] started at 0,
   exact right-hit probability is L/(L+1) and exact expected jump count is L,
   for L=1,...,8.  The values are obtained by exact Fraction Gaussian
   elimination, independently of the closed-form gambler's-ruin derivation.
2. A three-jump ARW transcript with a pre-existing sleeper shows that an
   occupied background does not support a scalar one-particle transfer state:
   0->-1 wakes the sleeper, -1->0 leaves one active at -1, and 0->+1 reaches
   the intended boundary while an active particle remains behind.

This is a bounded self-check, not a proof of any universal ARW statement.
"""

from fractions import Fraction


def gauss(A, b):
    aug = [row[:] + [rhs] for row, rhs in zip(A, b)]
    n = len(aug)
    for col in range(n):
        pivot = next(r for r in range(col, n) if aug[r][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [v / p for v in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] != 0:
                f = aug[r][col]
                aug[r] = [aug[r][c] - f * aug[col][c] for c in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


def solve_gambler_ruin(L):
    # Absorbing boundaries -L and +1; interior states -L+1,...,0.
    interior = list(range(-L + 1, 1))
    idx = {x: i for i, x in enumerate(interior)}

    # h(x) = (h(x-1)+h(x+1))/2, h(-L)=0, h(1)=1.
    A, b = [], []
    for x in interior:
        row = [Fraction(0) for _ in interior]
        row[idx[x]] = Fraction(1)
        rhs = Fraction(0)
        for y in (x - 1, x + 1):
            if y == 1:
                rhs += Fraction(1, 2)
            elif y != -L:
                row[idx[y]] -= Fraction(1, 2)
        A.append(row)
        b.append(rhs)
    h = gauss(A, b)

    # e(x) = 1 + (e(x-1)+e(x+1))/2, e(-L)=e(1)=0.
    A, b = [], []
    for x in interior:
        row = [Fraction(0) for _ in interior]
        row[idx[x]] = Fraction(1)
        for y in (x - 1, x + 1):
            if y not in (-L, 1):
                row[idx[y]] -= Fraction(1, 2)
        A.append(row)
        b.append(Fraction(1))
    e = gauss(A, b)
    return h[idx[0]], e[idx[0]]


for L in range(1, 9):
    h, e = solve_gambler_ruin(L)
    assert h == Fraction(L, L + 1), (L, h)
    assert e == L, (L, e)
print("EMPTY_GATE_FORMULAS_PASS L=1..8")


# Site state convention: absent/0 = empty; -1 = one sleeper; positive = active count.
def jump(cfg, x, y):
    cfg = dict(cfg)
    state = cfg.get(x, 0)
    if state == -1:  # acceptable toppling: force the sleeper active first
        state = 1
    assert state >= 1
    state -= 1
    if state:
        cfg[x] = state
    else:
        cfg.pop(x, None)

    dest = cfg.get(y, 0)
    if dest == -1:  # A + S -> 2A
        cfg[y] = 2
    else:
        assert dest >= 0
        cfg[y] = dest + 1
    return cfg


# Exact shortest witness used in the report.
cfg = {0: 1, -1: -1}
cfg = jump(cfg, 0, -1)
assert cfg == {-1: 2}
cfg = jump(cfg, -1, 0)
assert cfg == {-1: 1, 0: 1}
cfg = jump(cfg, 0, 1)
assert cfg == {-1: 1, 1: 1}
print("SLEEPER_REACTIVATION_WITNESS_PASS final=", dict(sorted(cfg.items())))
print("ALL_EXACT_CHECKS_PASS")
