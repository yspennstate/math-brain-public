#!/usr/bin/env python3
"""Exact truth-table structural checker for the FEI gate-composition reduction.

No floating point and no FEI claim.  It:
  * enumerates ternary NPN classes exactly,
  * tests functional decomposability by the two-cofactor criterion,
  * confirms that tt=6 factors as (x0 XOR x1) AND (NOT x2).
"""
import itertools

def val(tt, x):
    return (tt >> x) & 1

def depends(tt, k, i):
    return any(val(tt, x) != val(tt, x ^ (1 << i)) for x in range(1 << k))

def cofactor_rows(tt, k, A):
    A = tuple(A)
    B = tuple(i for i in range(k) if i not in A)
    rows = []
    for aa in range(1 << len(A)):
        row = 0
        for bb in range(1 << len(B)):
            x = 0
            for j, i in enumerate(A):
                x |= ((aa >> j) & 1) << i
            for j, i in enumerate(B):
                x |= ((bb >> j) & 1) << i
            row |= val(tt, x) << bb
        rows.append(row)
    return rows

def block_decomposition(tt, k):
    for r in range(2, k):
        for A in itertools.combinations(range(k), r):
            rows = cofactor_rows(tt, k, A)
            if len(set(rows)) <= 2:
                return A, rows
    return None

def transform(tt, k, perm, negmask, outneg):
    out = 0
    for y in range(1 << k):
        x = 0
        for i in range(k):
            xi = ((y >> perm[i]) & 1) ^ ((negmask >> i) & 1)
            x |= xi << i
        out |= (val(tt, x) ^ outneg) << y
    return out

def canonical_npn(tt, k):
    return min(
        transform(tt, k, perm, negmask, outneg)
        for perm in itertools.permutations(range(k))
        for negmask in range(1 << k)
        for outneg in (0, 1)
    )

def main():
    k = 3
    reps = {}
    for tt in range(1 << (1 << k)):
        reps.setdefault(canonical_npn(tt, k), tt)
    rows = []
    for rep in sorted(reps):
        degenerate = not all(depends(rep, k, i) for i in range(k))
        dec = None if degenerate else block_decomposition(rep, k)
        status = "DEGENERATE" if degenerate else ("DECOMPOSABLE" if dec else "PRIME")
        rows.append((rep, status))
    assert len(rows) == 14
    assert sum(s == "DEGENERATE" for _, s in rows) == 4
    assert sum(s == "DECOMPOSABLE" for _, s in rows) == 5
    assert sum(s == "PRIME" for _, s in rows) == 5
    assert [r for r, s in rows if s == "PRIME"] == [22, 23, 24, 25, 27]

    A, tt6_rows = block_decomposition(6, 3)
    assert A == (0, 1)
    assert tt6_rows == [0, 1, 1, 0]
    # With residual variable x2, row 0 is constant 0 and row 1 is NOT x2.
    # The row label over (x0,x1) is XOR.
    for x in range(8):
        x0, x1, x2 = (x >> 0) & 1, (x >> 1) & 1, (x >> 2) & 1
        rhs = (x0 ^ x1) & (1 ^ x2)
        assert val(6, x) == rhs

    print("TERNARY_NPN_CLASSES=14")
    print("DEGENERATE=4")
    print("FUNCTIONALLY_DECOMPOSABLE=5")
    print("COMPOSITION_PRIME=5")
    print("PRIME_REPRESENTATIVES=22,23,24,25,27")
    print("TT6_FACTORIZATION=(x0 XOR x1) AND (NOT x2)")
    print("PASS")

if __name__ == "__main__":
    main()
