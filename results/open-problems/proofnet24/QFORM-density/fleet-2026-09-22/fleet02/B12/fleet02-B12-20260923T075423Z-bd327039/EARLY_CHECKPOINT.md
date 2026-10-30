SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-23T07:54:23Z.
attacking: three-core routing for arbitrary rank-two eigenvalue replacements plus an arbitrary full-rank dense tail, with a dependence-safe cross-footprint fallback.

# Early substantive checkpoint

Status: partial derivation; full QFORM open.

## First unpaid implication

The bare hypothesis s_3(A)>=1 still does not force one fixed well-conditioned physical triple or one diffuse cross-volume certificate. A useful replacement would be a finite switchable family whose certificates cannot all resonate under the same arbitrary added spectral packet.

## New rank-two routing calculation

Let U have two orthonormal columns and let H_j be three physical triples. Assume U_j=U[H_j,:] has rank two. Choose an orthonormal basis [W_j,z_j] of R^{H_j} with range(W_j)=range(U_j), and write the baseline compression in that basis as

B_j = [[B11_j,b_j],[b_j^T,d_j]],  d_j != 0.

Put G_j=W_j^T U_j, F_j=G_j G_j^T, C_j=B11_j-b_j b_j^T/d_j, K_j=F_j^{-1/2} C_j F_j^{-1/2}, and S_j=F_j^{-1/2}G_j (orthogonal). For an arbitrary symmetric 2x2 parameter Theta,

C_j+G_j Theta G_j^T = F_j^{1/2}(K_j+S_j Theta S_j^T)F_j^{1/2}.

If ||K_j-c_j I_2||op<=eps and the three scalar anchors c_j are pairwise Delta-separated, then the two eigenvalues of -Theta cannot lie within distance <Delta/2 of all three anchors. Hence one j satisfies

sigma_min(K_j+S_j Theta S_j^T) >= Delta/2-eps.

The block shear factorization then gives a uniform physical-triple gap

g0 = ell(rho)^2 min{mu, f(Delta/2-eps)},

where mu=min_j |d_j|, f=min_j lambda_min(F_j), rho=max_j ||b_j||/|d_j| and ell(r)=(sqrt(r^2+4)-r)/2. Any additional symmetric dense T with ||T||op<=delta<g0 reduces that selected triple gap by at most delta. Therefore the completed e5f Theorem A on the actual final original-coordinate triple gives

||p_{X^T(A0+U Theta U^T+T)X}||inf <= 6 sqrt(pi)/(g0-delta).

No post-rotation independence and no claim that X^T T X is small are used.

Next: prove the shear singular-value bound carefully, give a literal two-eigenvalue-replacement target family, and apply the completed fleet03/B12 cross-footprint theorem on a separate zero-footprint branch.
