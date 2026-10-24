# FOREST handoff — account02/B02 — augmented homogenized log-concavity budget

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent team state remains an internal `FULL_PROOF_CANDIDATE`; no public theorem/novelty/priority promotion. Context: `WITHOUT_VERIFIED_BRAIN`.

Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B02/20260922T041021Z-account02-B02-forest-r13/report.md`, Git blob `d0ed896c51a038ac352aa45c3e9c40513e237dfb`.

Consumed lead account01/B01 `FOREST-KN-COCKS-RECONCILED-v3`, commit `0509904b9b699563a2b6fe60b6226948886a6b86`, and assigned named OTHER-account partner account03/B03 `FOREST-KN-HERMITE-JENSEN-v1`, report blob `64b8971de058ea3f9dba14e92ee5899252c1b1c3`.

For a graph with `m` edges, the ALOV homogenized graphic-matroid independent-set polynomial is exactly

`g(y,z)=sum_{F acyclic} y^(m-|F|) z^F`.

At all ones this is the **uniform law on all unrooted forests**, including disconnected forests and every size. Let `X_e=1[e in F]`, `K=|F|`, `p_e=E X_e`, `mu=E K`, `v=Var K`, `c_e=Cov(X_e,K)`, and `C_ef=Cov(X_e,X_f)`. For exponent vector `U=(m-K,X_1,...,X_m)`, complete log-concavity gives

`diag(EU)-Cov(U) = - Hess log g(1) >= 0`.

Normalizing by `diag(EU)` and using `N^2<=N` yields the new exact augmented row budget

**`c_e^2/((m-mu)p_e(1-p_e)) + sum_{f!=e}(1-p_f)rho_ef^2 <= p_e`.**

It strictly strengthens the previous edge-only budget by the size-susceptibility term. The homogenizing coordinate also gives

**`v^2/(m-mu) + sum_e c_e^2/p_e <= v`,**

which by Cauchy recovers `v<=mu(m-mu)/m`.

For one pair define `r=m-mu-v` and `d_ef=p_ep_f-P(e,f)=-C_ef`. The `(slack,e,f)` principal minor gives

**`r p_e^2 p_f^2 + 2 c_e c_f d_ef - r d_ef^2 - p_f^2 c_e^2 - p_e^2 c_f^2 >= 0`.**

For `r>0`, equivalently

`|d_ef-c_ec_f/r| <= sqrt((p_e^2-c_e^2/r)(p_f^2-c_f^2/r))`.

This is source-valid but does **not** force the Rayleigh sign: complete log-concavity remains spectral. If `c_e,c_f>=0`, the sufficient condition `(c_e/p_e)^2+(c_f/p_f)^2>=r` does force `d_ef>=0`; it is not claimed universal.

Minimal-counterexample application: if a bad pair has `rho_ef=c>0` and every third-edge conditioned pair covariance is nonpositive, total covariance gives `rho_eg rho_fg>=c`. With `T_i=c_i^2/((m-mu)p_i(1-p_i))`, the augmented budgets imply

`(2-p_e-p_f)c^2 + 2c sum_{g notin {e,f}}(1-p_g) + T_e+T_f <= p_e+p_f`.

At source unit weights, downward closure gives `p_i<=1/2`, hence

**`c^2+(m-2)c+T_e+T_f<=1`.**

This strictly sharpens B02's earlier `c^2+(m-2)c<=1` obstruction.

Exact regression swept all 1,098 labelled simple graphs on 2--5 vertices: 5,325 edge rows and 11,766 edge pairs; zero failures of the augmented row budget, global slack budget, 3x3 determinant inequality, or ULC variance check. Checker blob `e7bce77621c3667b3437219a6009ad2818542976`, SHA-256 `1e390e30f194b8eabead337007526b26c0e845839bc83386c63801fe5ba36dd9`; output blob `0ae3b91b5ca40efb077064942185ae49eaddc24d`, SHA-256 `5641d12bc8cccf4cdf87d361ce9f9378d8ce56e3488f02056ef1f19b6bac558e`. Finite computation is regression only.

First remaining implication for a log-concavity-only proof: use graphic structure to force the Schur interval above into `d_ef>=0`; ALOV alone cannot supply an entrywise sign. The existing all-graphs candidate instead uses the partner-supported `K_n` sign plus the final Semple--Welsh attribution of Cocks's fixed-graph weighted upgrade and minor closure.
