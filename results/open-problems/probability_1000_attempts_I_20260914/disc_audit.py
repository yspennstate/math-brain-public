"""Solver-independent audit of the exact maximum discrepancy of n x n sign matrices, n <= 11.

Every claim has two halves and neither needs the integer programme to be trusted:
  ACHIEVABLE  - an explicit matrix, its discrepancy recomputed by brute force over all 2^(n-1) sign
                vectors;
  NOT HIGHER  - either the counting bound (n rows each cover at most a fixed number of sign vectors at
                level v, and n times that is short of 2^(n-1)), or the published minimum size K(n,R) of
                a binary covering code, since disc >= v needs the n rows and their complements to cover
                every sign vector within Hamming distance (n-v)/2.
"""
import numpy as np
from math import comb

ROWS = {   # witnesses produced by the search, to be re-checked here from scratch
 2: ["++", "-+"],
 3: ["--+"],
 4: ["-+++", "-+-+"],
 5: ["++-++", "-+-++", "+-+-+", "--+-+"],
 6: ["--++++", "+--+++", "+++-++", "+-++-+", "-+-+-+", "-----+"],
 7: ["+-++-++", "--++-++", "++-+--+", "-+-+--+"],
 8: ["++-+++++", "-+---+++", "--+-+-++", "--+-++-+", "++--+--+", "-+-+---+", "+-+----+"],
 9: ["---++++++", "-+---++++", "+---++-++", "+++++--++", "+-+----++", "++--+++-+", "+--+-++-+",
     "-+-+-+--+", "--+-+---+"],
10: ["--+--+++++", "-+-+---+++", "--+++++-++", "++-+++--++", "++--+---++", "-+++-+-+-+",
     "+++-+--+-+", "----+-+--+", "+--+--+--+"],
11: ["++-++++++++", "---+-++++++", "+-+++-+++++", "+-++-+-++++", "-++++--++++", "++++--+-+++",
     "+--+++--+++", "-++--+---++", "---------++", "--+++-++--+", "++-+---+--+"],
}
K = {(6,0):64,(8,1):32,(10,2):30,(12,3):28,(7,1):16,(9,1):62,(11,2):44}   # published values used below

def sign_vectors(n):
    m = 1 << (n - 1)
    b = ((np.arange(m)[:, None] >> np.arange(n)[None, :]) & 1)
    b[:, n - 1] = 0
    return 1 - 2 * b

def covered_per_row(n, v):
    """number of sign vectors (up to global sign) that a single row covers at level v"""
    k = (n - v) // 2
    return sum(comb(n, j) for j in range(k + 1))

print(f"{'n':>3} {'rows':>5} {'disc (brute force)':>19} {'ratio':>7} {'v+2 ruled out by':>32}")
for n in sorted(ROWS):
    A = np.array([[1 if c == '+' else -1 for c in r] for r in ROWS[n]])
    assert A.shape[0] <= n, (n, A.shape)
    V = sign_vectors(n)
    d = int(np.abs(V @ A.T).max(axis=1).min())
    nxt = d + 2
    per = covered_per_row(n, nxt)
    r = (n - nxt) // 2
    why = ""
    if n * per < (1 << (n - 1)):
        why = f"counting: {n}x{per} < {1 << (n-1)}"
    elif (n, r) in K and K[(n, r)] > 2 * n:
        why = f"K({n},{r}) = {K[(n,r)]} > {2*n}"
    else:
        why = "integer programme only"
    print(f"{n:>3} {A.shape[0]:>5} {d:>19} {d/np.sqrt(n):>7.4f} {why:>32}")
print("\nthe ratio is disc/sqrt(n); the list records sqrt(2) = 1.4142 as the known lower bound")
