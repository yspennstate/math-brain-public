SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B17, 2026-09-23T11:43:30Z.
attacking: the fully diffuse but non-identically-distributed Lindeberg witness class; prove any exact-rank-three source-valid diffuse CLT sequence is capped asymptotically by 3sqrt(2), or isolate the precise non-Lindeberg escape.

# Early checkpoint: diffuse Lindeberg witnesses cannot asymptotically overshoot 3sqrt(2)

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `fleet02-B17-20260923T1142Z-r11`  
Status: supporting theorem in proof; full QFORM remains OPEN.

Let `R_m` be an `n_m x 3` matrix with `R_m^T R_m=I_3`, rows `r_{mi}`, and
`tau_m=max_i ||r_{mi}||^2 ->0`. Fix `Lambda=diag(lambda_1,lambda_2,lambda_3)` with `|lambda_j|>=1`, and set

`A_m=R_m Lambda R_m^T`.

Then every finite `A_m` has exact nonzero spectrum `{lambda_1,lambda_2,lambda_3}`. Let the physical inputs `X_{mi}` be independent with densities at most one, finite means `mu_{mi}` and finite variances `v_{mi}`. Put

`Z_{mi}=r_{mi}(X_{mi}-mu_{mi}) in R^3`,
`h_m=sum_i r_{mi} mu_{mi}`,
`Sigma_m=sum_i v_{mi} r_{mi}r_{mi}^T`.

Assume `h_m->h`, `Sigma_m->Sigma`, and the vector Lindeberg condition

`sum_i E[ ||Z_{mi}||^2 1_{||Z_{mi}||>eps} ] ->0` for every `eps>0`.

The first unpaid implication is then:

`limsup_m ||p_{X_m^T A_m X_m}||_infty <= 3sqrt(2)`.

Proof skeleton, with all interfaces already source-valid:

1. The cap-one bathtub variance bound gives `v_{mi}>=1/12`; hence
   `Sigma_m >= (1/12) sum_i r_{mi}r_{mi}^T = I_3/12`, so `Sigma>=I_3/12`.
2. Multivariate Lindeberg-Feller gives `R_m^T X_m => G~N(h,Sigma)`.
3. For all large `m`, `tau_m<=1/2`. Apply the completed Fresnel--Brascamp--Lieb Theorem F from
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and `FOURIER_ROUTE_REPORT.md`, with `I` all coordinates, `B=0`, and `G_I=R_m^T R_m=I_3`. It yields the actual finite-source inequality

   `|phi_m(t)| <= min(1,(4pi)^(3/2)|t|^(-3/2))`,

   since `prod_j |lambda_j|>=1`.
4. The quadratic continuous mapping theorem gives pointwise `phi_m(t)->phi_infty(t)` for `G^T Lambda G`. The common integrable majorant gives `||phi_m-phi_infty||_1->0`; Fourier inversion gives uniform output-density convergence.
5. Apply fleet03/B17's completed arbitrary-mean Gaussian ceiling
   `yspennstate/math-open-problems@dcf8885d5153370cacfa246ad1e29fb06d971769`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260923T070310Z-fleet03-B17-QFORM-r25/REPORT.md`:
   because `Sigma>=I_3/12`, `||p_{G^T Lambda G}||_infty<=3sqrt(2)`.

This is deliberately a witness-class theorem, not a proof of the arbitrary-law target: finite variance, tight projected mean/covariance and Lindeberg are explicit hypotheses. It shows that a diffuse exact-rank-three witness beating `3sqrt(2)` must leave the Gaussian domain of attraction in a genuinely non-Lindeberg/non-tight way.

Latest designated partner fleet03/B17 result consumed: `yspennstate/math-open-problems@48e35fac4689f50a415638faba5a6e634b3d0329`, rare-fragment first variation. Its exact `c_j/m^2` remote-fragment family satisfies the hypotheses above (row leverage `1/m`, projected mean `O(1/m)`, covariance `I/12+O(1/m)`, Lindeberg cost `O(1/m)`), so the theorem upgrades that partner's cone-tip first-order no-escape result to the global asymptotic inequality `limsup ||p_{Q_m}||_infty<=3sqrt(2)` for the same family. The partner's sharper cone-tip expansion remains complementary.
