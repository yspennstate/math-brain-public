#!/usr/bin/env python3
"""Exact finite check for the d=3, |supp x|=3 kernel-vector classification.

We enumerate every simple graph induced on the three support vertices and every
multiset of possible outside neighbourhoods of size 2 or 3 consistent with
3-regularity.  Singleton outside neighbourhoods are impossible for a kernel
vector whose three support coordinates are nonzero, so they are omitted.

For each incidence pattern we build the homogeneous integer linear system for
Ax=0 restricted to the support coordinates.  A pattern is accepted exactly
when the rational nullspace contains a vector with all three coordinates
nonzero.  Over Q, a finite-dimensional vector space contains such a vector iff
it is nonzero and is not contained in any coordinate hyperplane; this is tested
by rank increments after adjoining x_i=0.

Expected unique survivor: no internal support edges and three outside vertices,
each adjacent to all three support vertices.  This is exactly a K_{3,3}
component; its kernel on one bipartition is {x_1+x_2+x_3=0}.
"""

from fractions import Fraction
from itertools import product


def rank_q(rows, ncols=3):
    A = [[Fraction(x) for x in row] for row in rows if any(row)]
    if not A:
        return 0
    m = len(A)
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, m) if A[i][c] != 0), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(ncols)]
        r += 1
        if r == m:
            break
    return r


EDGES = [(0, 1), (0, 2), (1, 2)]
BOUNDARY_TYPES = [(0, 1), (0, 2), (1, 2), (0, 1, 2)]

survivors = []
patterns_tested = 0

for mask in range(8):
    internal = [EDGES[i] for i in range(3) if (mask >> i) & 1]
    ideg = [0, 0, 0]
    for a, b in internal:
        ideg[a] += 1
        ideg[b] += 1
    remaining = [3 - z for z in ideg]
    if min(remaining) < 0:
        continue

    # No boundary type can occur more than three times because each support
    # vertex has degree exactly three.
    for mult in product(range(4), repeat=4):
        bdeg = [0, 0, 0]
        for m, S in zip(mult, BOUNDARY_TYPES):
            for v in S:
                bdeg[v] += m
        if bdeg != remaining:
            continue
        patterns_tested += 1

        rows = []
        # Equations (Ax)_v=0 for v in the support, from internal support edges.
        for v in range(3):
            row = [0, 0, 0]
            for a, b in internal:
                if a == v:
                    row[b] += 1
                elif b == v:
                    row[a] += 1
            rows.append(row)

        # Equations at outside boundary vertices.
        for m, S in zip(mult, BOUNDARY_TYPES):
            for _ in range(m):
                row = [0, 0, 0]
                for v in S:
                    row[v] = 1
                rows.append(row)

        r = rank_q(rows)
        if r >= 3:
            continue
        all_coordinates_possible = all(
            rank_q(rows + [[1 if j == i else 0 for j in range(3)]]) == r + 1
            for i in range(3)
        )
        if all_coordinates_possible:
            survivors.append((tuple(internal), mult, r))

print(f"patterns_tested={patterns_tested}")
print(f"survivor_count={len(survivors)}")
for item in survivors:
    print(item)

expected = [((), (0, 0, 0, 3), 1)]
assert survivors == expected, (survivors, expected)
print("EXACT_CHECK_PASS")
