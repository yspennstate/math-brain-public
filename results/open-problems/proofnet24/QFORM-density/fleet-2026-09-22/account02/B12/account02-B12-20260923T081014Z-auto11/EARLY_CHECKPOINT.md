SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T08:10:14Z.
attacking: robust approximate-isotropic anchor switching for arbitrary multirank signed spectral updates under a genuinely dense small operator-norm tail.

# Early mathematical checkpoint

Full QFORM target remains OPEN. This checkpoint records the first new implication before the final argument.

Sources actually consumed:
- required newest-Claude source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`;
- designated partner account03/B12: `yspennstate/math-open-problems@c00f2cfff4ac70e053c88b080e8dcfd63cde70aa:proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T074544Z-qform-eigenvalue-r28/REPORT.md`.

Partner equation (their (2.2)). On a physical core `j`, with the partner's Schur data `(K_j,S_j,F_j,D_j,rho_j)`, every symmetric rank-r parameter `Theta` obeys

`sigma_min(B_j+U_j Theta U_j^T) >= ell(rho_j)^2 min{mu_j, f_j sigma_min(K_j+S_j Theta S_j^T)}`,

where `mu_j=sigma_min(D_j)`, `f_j=lambda_min(F_j)`, `ell(rho)=(sqrt(rho^2+4)-rho)/2`, and `S_j` is orthogonal.

New observation. Suppose there are `r+1` physical cores and numbers `c_0,...,c_r` with pairwise gaps at least `Delta`, but exact isotropy is relaxed to

`||K_j-c_j I_r||_op <= eps`, with `eps<Delta/2`.

For every `Theta in Sym_r`, at least one anchor interval `(c_j-Delta/2,c_j+Delta/2)` contains no number `-lambda_k(Theta)`, since there are `r+1` pairwise-disjoint intervals but only `r` eigenvalues. For that `j`,

`min_k |c_j+lambda_k(Theta)| >= Delta/2`.

Because `S_j` is orthogonal,

`sigma_min(c_j I + S_j Theta S_j^T)=min_k |c_j+lambda_k(Theta)|`,

and Weyl therefore gives

`sigma_min(K_j+S_j Theta S_j^T) >= Delta/2-eps`.

Hence, with

`gamma = ell_*^2 min{mu_*, f_*(Delta/2-eps)}`,

one actual original-coordinate core has gap at least `gamma`, uniformly over the signs, magnitudes, and internal mixing of all eigenvalues of `Theta`. Adding an arbitrary symmetric dense tail `T` with `||T||op<=delta<gamma` leaves gap at least `gamma-delta`; if the core is a physical triple, the completed newest-Claude Theorem A gives the real density inequality

`||p_Q||inf <= 6 sqrt(pi)/(gamma-delta)`.

No estimate of `X^T T X` and no post-rotation independence is used. The final report will prove the statement carefully, include a literal arbitrary-eigenvalue-replacement construction with nonzero anisotropy `eps`, and state the remaining structural gap.
