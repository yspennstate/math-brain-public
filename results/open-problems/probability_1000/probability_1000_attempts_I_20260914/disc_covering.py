"""The maximum discrepancy of an n x n sign matrix is a covering-code quantity.

disc(A) >= v  iff  every sign vector x has some row r with |r.x| >= v.  Since |r.x| = |n - 2 d(r,x)|,
that says every x is within Hamming distance (n-v)/2 of some row OR of its complement.  So

    max over A of disc(A) = n - 2 * min { r : there is a binary covering code of length n, radius r,
                                              consisting of n codewords together with their complements }.

Standard covering-code tables list K(n,r), the least size of ANY binary covering code of length n and
radius r.  A code and its complements have size at most twice the original, so

    K(n,r) <= n   ==>  feasible,        K(n,r) > 2n  ==>  infeasible,

which brackets the answer from published tables.  This checks the identification against the exact
discrepancies computed directly.
"""
K = {  # published least sizes of binary covering codes, K(n,r)
 (3,1):2,(4,1):4,(5,1):7,(6,1):12,(7,1):16,(8,1):32,(9,1):62,(10,1):107,(11,1):180,(12,1):342,
 (5,2):2,(6,2):4,(7,2):7,(8,2):12,(9,2):16,(10,2):30,(11,2):44,(12,2):78,
 (7,3):2,(8,3):4,(9,3):7,(10,3):12,(11,3):16,(12,3):28,(13,3):42,(14,3):64,
 (9,4):2,(10,4):4,(11,4):7,(12,4):12,(13,4):16,(14,4):28,
 (11,5):2,(12,5):4,(13,5):7,(14,5):12,
 (13,6):2,(14,6):4,
}
DISC = {2:2,3:1,4:2,5:3,6:4,7:3,8:4,9:5,10:4,11:5}   # computed exactly here

print(f"{'n':>3} {'disc':>5} {'implied r':>10} {'K(n,r)':>7} {'2n':>4} {'K(n,r-1)':>9} {'consistent':>11}")
for n, d in sorted(DISC.items()):
    r = (n - d) // 2
    k_r = K.get((n, r)); k_prev = K.get((n, r - 1))
    ok = (k_r is not None and k_r <= 2 * n) and (k_prev is None or k_prev > 2 * n)
    print(f"{n:>3} {d:>5} {r:>10} {str(k_r):>7} {2*n:>4} {str(k_prev):>9} {'yes' if ok else '?':>11}")
print("\nreading: radius r must be achievable by 2n codewords (K(n,r) <= 2n) and radius r-1 must not be")
