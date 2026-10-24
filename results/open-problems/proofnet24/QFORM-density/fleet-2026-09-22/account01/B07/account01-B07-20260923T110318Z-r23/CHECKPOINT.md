SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T11:03:18Z.
attacking: the fixed double-pair third-volume survivor; compress its entire determinant bank to a physical edge and a quantitative principal-pair/tail alternative without choosing one tiny minor.

# Early substantive checkpoint

Let an ORIGINAL-coordinate cross block, after physical row/column permutations only, be

M = [[B,U],[V,D]],

where B is the fixed 2x2 row/column anchor. Define the complete anchored third-volume extension bank

H = sum_{k,l} det(M[P union {k},Q union {l}])^2.

For every residual row k and column l,

det [[B,u_l],[v_k^T,d_kl]] = det(B)d_kl - v_k^T adj(B)u_l.

Therefore, without assuming B invertible,

H = || det(B)D - V adj(B)U ||_F^2.                                      (1)

Put x=||B||_F, u=||U||_F, v=||V||_F, d=||D||_F, F=||M||_F. For 2x2 B,
|det B|<=x^2/2 and ||adj(B)||_op=||B||_op<=x. Hence

sqrt(H) <= (x^2/2)d + xuv
        = x(xd/2+uv)
        <= x F^2/2.                                                     (2)

Consequently

||B||_F >= 2 sqrt(H)/F^2,

and one of the four physical entries b of B obeys

|b| >= sqrt(H)/F^2.                                                     (3)

This is aggregate-before-inversion: no individual 3x3 determinant is selected or divided by.

If H>=cF^6, then |b|>=sqrt(c)F. For the current inherited double-pair bank c=1/64123518131896320, this gives

|b| > F/253226219.2820805.

Next step: form the symmetric ORIGINAL-coordinate principal pair on the row/column indices of b. Either both physical diagonals are <|b|/2, in which case the pair is indefinite with |det|>=3b^2/4 and sigma_min>=|b|/2, or at least one diagonal is >=|b|/2. In the first branch, apply account02/B07's completed pair-tail curvature receiver to the exact pair Schur remainder.

Status: supporting structural lemma; full QFORM remains open; continuity not claimed by this checkpoint.
