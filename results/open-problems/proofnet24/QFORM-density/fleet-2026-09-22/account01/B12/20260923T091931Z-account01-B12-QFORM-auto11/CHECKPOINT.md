SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T09:19:31Z.
attacking: frame-covariant routing of arbitrary signed eigenvalue replacements through nonaligned physical cores, plus arbitrary dense matrix tails.

# Early substantive checkpoint

Full QFORM remains OPEN. This checkpoint records the first useful derivation before the final report.

Use account03/B12's completed matrix-parameter Schur inequality (math-open-problems@333dd6db61c9d18e88f9b8be5bae55c811d49b42): on physical core j,

sigma_min(B_j+U_j Theta U_j^T) >= ell(rho_j)^2 min{mu_j, f_j sigma_min(K_j+S_j Theta S_j^T)},

where S_j is orthogonal.

The key identity is

K_j+S_j Theta S_j^T = S_j( S_j^T K_j S_j + Theta )S_j^T.

Therefore exact alignment S_j=I is unnecessary. For diagonal spectral motion Theta=diag(tau_1,...,tau_r), define the parameter-frame anchor

Khat_j := S_j^T K_j S_j.

If Khat_j=D_j+E_j with D_j=diag(c_{j1},...,c_{jr}), ||E_j||op<=eps<Delta/2, and for each coordinate k the r+1 values c_{0k},...,c_{rk} are pairwise Delta-separated, then account02/B12's completed bad-core counting argument applies literally to Khat_j+Theta: for each k at most one core satisfies |c_{jk}+tau_k|<Delta/2, hence one of r+1 cores is good for every k. On that core,

sigma_min(Khat_j+Theta)>=Delta/2-eps,

and consequently

sigma_min(B_j+U_j Theta U_j^T)
 >= ell(rho_j)^2 min{mu_j, f_j(Delta/2-eps)}.

This removes the partner theorem's S_j=I alignment hypothesis without rotating the random variables. The remaining work in this run is to state the quantitative theorem cleanly, add arbitrary local/dense matrix tails by Weyl, and build an exact target-class family with genuinely different S_j to demonstrate the extension.
