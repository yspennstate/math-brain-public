SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T09:15:49Z.
attacking: exact-rank-three indefinite pair completion — cancel the local pair determinant against the rank-one Schur curvature and reduce the local obstruction to spectral two-row area.

# Early substantive checkpoint

Let `A=R M R^T`, `R^T R=I_3`, with `M` invertible of signature `(2,1)` or `(1,2)`. Fix two original-coordinate rows `r_i,r_j`, put `P=[r_i^T;r_j^T]`, `G=P P^T`, and

`g_ij=det G=||r_i wedge r_j||^2`.

Assume `g_ij>0`. The exact identities to be used are

`det(A[{i,j},{i,j}]) = det(M) n^T M^{-1} n`, `n=r_i x r_j`,

and, whenever the physical pair `B=PMP^T` is invertible and its rank-one Schur remainder is written as `lambda h h^T` with `||h||=1`,

`det(B) lambda = det(M) g_ij`.

Equivalently,

`|det(B)| |lambda| = |det M| g_ij = sum_k |det A[{i,j,k},{i,j,k}]|`.

The last equality follows from `det A_{ijk}=det(M) det(R_{ijk})^2` and Parseval:

`sum_k det(R_{ijk})^2 = sum_k ((r_i x r_j) dot r_k)^2 = ||r_i x r_j||^2`.

Thus in the completed physical-pair logarithmic theorem the dangerous local determinant cancels exactly:

`||p_Q||_inf <= 8 sqrt(5) [kappa |det M| g_ij]^(-1/4)`,

where `kappa=sigma_min(B)`.

A second deterministic step removes small `kappa`. Let `L=||B||op`. Polar decomposition of `P` gives `B=G^(1/2) C G^(1/2)` with `C` a two-dimensional compression of `M`. Cauchy interlacing for signatures `(2,1)` and `(1,2)` implies `||C||op>=s` when `min |eig M|>=s`. Since the eigenvalues of `G` are at most one, `lambda_min(G)>=det G=g_ij`; hence

`L>=s g_ij`.

If `kappa<L/2`, then `|tr B|>L/2`, so one physical diagonal has magnitude `>L/4>=s g_ij/4`. If `kappa>=L/2` and `B` is definite, one diagonal has magnitude `>=L/2`. Only the remaining case is an invertible indefinite pair with `kappa>=s g_ij/2`.

Combining the completed scalar-pivot theorem with the determinant-cancelled pair-log theorem should therefore give the area-only local compiler

`||p_Q||_inf <= 128 sqrt(2)/(s sqrt(g_ij))`

for every exact-rank-three indefinite form and every original row pair with `g_ij>0`. This is not dimension-free by itself: a Parseval frame can have every individual `g_ij` small. The intended structural consequence is that the remaining exact-rank-three obstruction is purely an exterior-frame aggregation problem, not a small physical-pair determinant problem.

Status: checkpoint only; full proof, partner application, correction refresh and final source pins still to be completed in this run.
