#!/usr/bin/env python3
"""Exact finite self-checks for complete non-normal orbit quotients.

Run with Python 3.10+: python3 finite_core.py
No network, external packages, floating point, or randomness is used.
This checks the S3, A4, A5 templates, NOT the infinite GRR theorem,
NOT simplicity of every A_m, and NOT independent mathematical audits.
"""
from __future__ import annotations

from itertools import permutations
from math import factorial
from typing import Iterable

Perm = tuple[int, ...]


def mul(p: Perm, q: Perm) -> Perm:
    """Composition p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


def inv(p: Perm) -> Perm:
    ans = [0] * len(p)
    for i, x in enumerate(p):
        ans[x] = i
    return tuple(ans)


def even(p: Perm) -> bool:
    return sum(p[i] > p[j] for i in range(len(p))
               for j in range(i + 1, len(p))) % 2 == 0


def generated(gens: Iterable[Perm], degree: int) -> frozenset[Perm]:
    gs = tuple(set(gens))
    identity = tuple(range(degree))
    seen = {identity}
    todo = [identity]
    while todo:
        x = todo.pop()
        for s in gs:
            y = mul(x, s)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return frozenset(seen)


def all_normal_subgroups(group: tuple[Perm, ...]) -> set[frozenset[Perm]]:
    """Exhaustively generate the lattice of normal subgroups.

    Any normal subgroup is a union of conjugacy classes. Starting at {1},
    adjoining each class and taking generated subgroups reaches every
    normal subgroup. No enumeration of all 2^|G| subsets is needed.
    """
    degree = len(group[0])
    identity = tuple(range(degree))
    conjugacy_classes = {
        frozenset(mul(mul(g, x), inv(g)) for g in group)
        for x in group
    }
    todo = [frozenset({identity})]
    found = set(todo)
    while todo:
        normal = todo.pop()
        for cls in conjugacy_classes:
            if cls <= normal:
                continue
            extension = generated(normal | cls, degree)
            if extension not in found:
                found.add(extension)
                todo.append(extension)
    return found


def verify(m: int) -> None:
    assert m in (3, 4, 5), 'This finite checker is intentionally bounded.'
    identity = tuple(range(m))
    group = tuple(p for p in permutations(range(m)) if m == 3 or even(p))
    full = frozenset(group)
    expected_order = factorial(m) if m == 3 else factorial(m) // 2
    assert len(full) == expected_order
    assert generated(group, m) == full
    assert all(inv(g) in full for g in group)
    assert all(mul(g, h) in full for g in group for h in group)

    stab = frozenset(g for g in group if g[0] == 0)
    assert 1 < len(stab) < len(full)
    assert len(full) == m * len(stab)
    conjugates = {frozenset(mul(mul(g, h), inv(g)) for h in stab)
                  for g in group}
    assert len(conjugates) == m  # In particular the stabilizer is not normal.

    # Left multiplication by H has orbits Hg: RIGHT cosets, not left cosets.
    cosets = sorted({frozenset(mul(h, g) for h in stab) for g in group},
                    key=lambda c: sorted(c))
    assert len(cosets) == m
    assert frozenset().union(*cosets) == full
    assert sum(map(len, cosets)) == len(full)
    orbit = {g: i for i, coset in enumerate(cosets) for g in coset}
    adjacency = [[0 for _ in range(m)] for _ in range(m)]
    for g in group:
        for s in group:
            if s != identity:
                i, j = orbit[g], orbit[mul(g, s)]
                if i != j:  # The source suppresses loops and parallel edges.
                    adjacency[i][j] = 1
    assert adjacency == [[int(i != j) for j in range(m)] for i in range(m)]

    normals = all_normal_subgroups(group)
    image_orders = sorted({len(full) // len(n) for n in normals})
    possible_images_in_order_m_group = [d for d in image_orders if m % d == 0]
    assert possible_images_in_order_m_group == [1]
    if m == 3:
        transpositions = [g for g in group
                          if sum(g[i] != i for i in range(m)) == 2]
        assert generated(transpositions, m) == full
    else:
        three_cycles = [g for g in group
                        if sum(g[i] != i for i in range(m)) == 3]
        assert generated(three_cycles, m) == full
    if m == 5:
        assert {len(n) for n in normals} == {1, 60}

    # Exact word count and the published, deliberately loose GRR degree bound.
    a = len(full) - 1
    t = 2 * (a + a * a + a * a * a)
    degree_bound = 2 * t * (t + 14)
    name = 'S3' if m == 3 else f'A{m}'
    print(f'm={m} group={name} order={len(full)} stabilizer={len(stab)} '
          f'conjugates={len(conjugates)} quotient=K{m}')
    print(f'  normal_subgroup_orders={sorted(len(n) for n in normals)} '
          f'homomorphic_image_orders={image_orders} '
          f'possible_image_orders_in_order_{m}_group={possible_images_in_order_m_group}')
    print(f'  S1_word_count={t} GRR_degree_upper_bound={degree_bound}')
    print(f'  adjacency={adjacency}')


def main() -> None:
    print('Exact finite template self-check; NOT an independent audit.')
    for m in (3, 4, 5):
        verify(m)
    print('ALL_EXACT_CHECKS_PASS')
    print('Uncomputed dependencies: infinite free products; relative GRR; '
          'simplicity of A_m for arbitrary m>=5. See solution.tex.')


if __name__ == '__main__':
    main()
