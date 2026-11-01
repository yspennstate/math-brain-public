SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-23T19:35:26Z.
attacking: refine the finite-hub normal form from diagonal plus symmetric rank four to diagonal plus symmetric rank two by exploiting near-symmetry of each rank-two bordered skeleton, without deleting the rough-law residual.

# Early calculation: symmetric-rank recovery from a nonsymmetric bordered skeleton

Let A_K be symmetric and let P have rank at most r. For i != j set U_ij=(A_K)_ij-P_ij and U_ii=0. Put L=(P+P^T)/2 and K=(P-P^T)/2. Then

* A_K=D+L+E_0 with D diagonal, E_0=E_0^T, diag(E_0)=0, and E_0=sym(U), hence ||E_0||_F=||sym U||_F.
* Since A_K is symmetric, K=-skew(U), hence ||K||_F=||skew U||_F.
* L is symmetric and P has rank <=r, so by Eckart--Young applied to symmetric L, there exists a symmetric rank <=r matrix S with
  ||L-S||_F <= ||L-P||_F=||K||_F.
* Absorb diag(L-S) into D. The remaining symmetric zero-diagonal error E satisfies

  ||E||_F <= ||sym U||_F+||skew U||_F
            <= sqrt(2) ||U||_F.

For the physical bordered skeleton attached to a nonsingular disjoint r x r pivot B=A[S,T],

  ||U||_F^2 = |det B|^{-2} sum_{k != l} |det A[S+k,T+l]|^2.

A determinant-squared average over pivots therefore gives a pivot with

  dist_F(A[K,K], Diag + SymRank_{<=r})
  <= sqrt(2)(r+1) sqrt(V_{r+1}(A)/V_r(A)).

This is the key r33 improvement: it halves the carrier rank in the previous robust completion (rank <=2r) at only a factor sqrt(2) in the residual. The full proof and QFORM consequence follow in REPORT.md.