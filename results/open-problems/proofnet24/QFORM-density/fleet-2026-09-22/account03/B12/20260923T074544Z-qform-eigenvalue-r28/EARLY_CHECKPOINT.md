# account03/B12 r28 early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260923T074544Z-qform-eigenvalue-r28
Assignment: additional eigenvalue control
Status: partial derivation, full QFORM open.

## New structural observation

For a physical core I and a rank-r update `U Theta U^T`, write the partner Schur data with `W` spanning `range(U)`, complementary basis `Z`,

`C=B11-B12 D^{-1} B12^T`, `F=(W^T U)(W^T U)^T`, `K=F^{-1/2} C F^{-1/2}`.

If `G=W^T U` and `S=F^{-1/2}G`, then `S` is orthogonal and

`C+G Theta G^T = F^{1/2}(K+S Theta S^T)F^{1/2}`.

Thus the account04/B12 shear factorization extends at the matrix level to

`sigma_min(B+U Theta U^T) >= ell(rho)^2 min{mu, f sigma_min(K+S Theta S^T)}`,

where `f=lambda_min(F)`, `mu=sigma_min(D)`, and `ell(rho)=(sqrt(rho^2+4)-rho)/2`.

## First obstruction

For r>=2, two arbitrary matrix-parameter resonance varieties cannot in general be positively separated. For any symmetric H1,H2 in Sym_r, the sets

`R_j={Theta in Sym_r: det(Theta+H_j)=0}`

intersect. Choose orthonormal eigenvectors u,v of H2-H1, so `u^T(H2-H1)v=0`; then prescribe a symmetric Theta with `Theta u=-H1 u` and `Theta v=-H2 v` (the compatibility condition for symmetric extension is exactly that displayed orthogonality). Hence both determinants vanish.

This shows why the partner's two-core theorem is genuinely scalar/common-shift and cannot simply be promoted to fully independent rank-r eigenvalue shifts with the same two-core separation hypothesis.

## Candidate replacement

If r+1 physical cores have isotropic transformed Schur anchors `K_j=c_j I_r`, with pairwise separated scalars `|c_j-c_k|>=Delta`, then for every arbitrary symmetric Theta one anchor is at distance at least Delta/2 from every eigenvalue of `-Theta`: r eigenvalues cannot cover r+1 disjoint Delta/2-neighborhoods. Therefore one physical core has gap at least

`ell_*^2 min{mu_*, f_* Delta/2}`.

This would yield a uniform density bound after arbitrary signed rank-r updates, plus any further perturbation whose compression is below that gap. The final report will prove this carefully and give an explicit r=2 target-class example.
