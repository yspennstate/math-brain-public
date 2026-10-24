#!/usr/bin/env python3
"""Exact self-check for HARD7-02 protected scalar three-interval packet.

For W=1,...,5 enumerate every equal-cardinality pair I,J of deleted outer
rows/columns and verify the explicit matching construction from the report.
All checks use integer arithmetic / Boolean comparisons only.
"""
from itertools import combinations
from math import comb


def construct(W, I, J):
    L = list(range(-W, 0))
    C = list(range(0, W))
    R = list(range(W, 2 * W))
    I, J = set(I), set(J)

    Lr = [x for x in L if x not in I]
    Rr = [x for x in R if x not in I]
    Lc = [x for x in L if x not in J]
    Rc = [x for x in R if x not in J]
    a, b, c, e = map(len, (Lr, Rr, Lc, Rc))
    assert a + b == c + e

    delta = a - c
    pairs = []
    used_C_rows, used_C_cols = set(), set()

    if delta >= 0:
        d = delta
        L_cross, L_dense = Lr[:d], Lr[d:]
        assert len(L_dense) == c
        pairs += list(zip(L_dense, Lc))

        R_dense_cols, R_cross_cols = Rc[:b], Rc[b:]
        assert len(R_cross_cols) == d
        pairs += list(zip(Rr, R_dense_cols))

        for p in L_cross:
            q = W + p
            assert q in C and q not in used_C_cols
            used_C_cols.add(q)
            pairs.append((p, q))

        for r in R_cross_cols:
            q = r - W
            assert q in C and q not in used_C_rows
            used_C_rows.add(q)
            pairs.append((q, r))
    else:
        d = -delta
        L_dense_cols, L_cross_cols = Lc[:a], Lc[a:]
        assert len(L_cross_cols) == d
        pairs += list(zip(Lr, L_dense_cols))

        R_cross_rows, R_dense = Rr[:d], Rr[d:]
        assert len(R_dense) == e
        pairs += list(zip(R_dense, Rc))

        for p in L_cross_cols:
            q = W + p
            assert q in C and q not in used_C_rows
            used_C_rows.add(q)
            pairs.append((q, p))

        for r in R_cross_rows:
            q = r - W
            assert q in C and q not in used_C_cols
            used_C_cols.add(q)
            pairs.append((r, q))

    remaining_C_rows = [q for q in C if q not in used_C_rows]
    remaining_C_cols = [q for q in C if q not in used_C_cols]
    assert len(remaining_C_rows) == len(remaining_C_cols)
    pairs += list(zip(remaining_C_rows, remaining_C_cols))

    rows = set(L + C + R) - I
    cols = set(L + C + R) - J
    assert len(pairs) == len(rows)
    assert {r for r, _ in pairs} == rows
    assert {c for _, c in pairs} == cols
    assert all(abs(r - c) <= W for r, c in pairs)
    return pairs


print("HARD7-02 protected scalar packet exact matching checker")
for W in range(1, 6):
    O = list(range(-W, 0)) + list(range(W, 2 * W))
    count = 0
    for k in range(2 * W + 1):
        for I in combinations(O, k):
            for J in combinations(O, k):
                construct(W, I, J)
                count += 1
    assert count == comb(4 * W, 2 * W)
    print(f"W={W}: checked {count} equal-size outer deletion pairs; explicit matching valid")
print("ALL_EXACT_CHECKS_PASS = True")
