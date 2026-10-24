# FOREST handoff — account04/B03 — 20260922T070756Z

Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent FOREST: `OPEN`  
Context: `WITHOUT_VERIFIED_BRAIN`

## Lead and named OTHER-account input

Read latest complete lead account01/B01 `20260922T050946Z-b01-forest-auto11`, shared blob `4cee205cb7d254caf785692838111988a0b8a155`. Its first unpaid step is triangle-contraction STAR-2. Applied account03/B02 `20260922T051758Z`, shared blob `c165e7c6b6ca991a97c5ed3d646611f91cf96adc`, specifically its move to a loopless-multigraph minimal frame; the needed part is re-proved directly here and does not import its Cocks-dependent 3-connectivity sentence. Also retain account01/B02 `20260922T054825Z` correction: rank-degree CLC is false; only ground-set-degree CLC is used.

## First missing coverage step paid exactly

If the simple target fails, choose a counterexample with minimum physical edge count among **all loopless multigraphs**; this class is nonempty because it contains the failing simple graph. For a violating pair `e,f` and every third edge `g`, conditioning on `g=0` is the smaller deletion, and conditioning on `g=1` is the smaller contraction after discarding any loops created from edges parallel to `g`. If a mark becomes a loop its conditional covariance is zero. Hence both conditional `e,f` covariances are nonpositive for every `g`.

Writing `C_ij=Cov(X_i,X_j)` and `v_i=Var(X_i)`, exact total covariance gives

`C_eg C_fg >= C_ef v_g > 0`.

Thus the lead's triangle STAR-2 debt disappears in this minimal class: the `{1,2}` star is simply the simplified image of a smaller labelled multigraph contraction, so no weighted closure theorem is needed.

Standardizing gives `rho_eg rho_fg >= rho_ef=:a>0`. A positive correlation triangle would imply cyclically `a<=bc`, `b<=ac`, `c<=ab`, hence `1<=abc`, impossible. Therefore every third edge is negatively correlated with both members of a violating pair, and the positive-covariance graph on all physical edges is a matching.

## Corrected all-edge quantitative obstruction

Use the source-valid ground-set-degree homogenization `g(y,z)=sum_I y^(m-|I|) z^I` from ALOV III, not the refuted rank-degree substitute. If `K=|F|`, `mu=EK`, `L=m-mu`, `c_i=Cov(X_i,K)`, and

`T_i=c_i^2/[L p_i(1-p_i)]`,

then the edge-row spectral inequality is

`T_i + sum_{h!=i}(1-p_h) rho_ih^2 <= p_i`.

Applying the all-conditioner Simpson inequality to every one of the `m-2` third edges gives

`T_e+T_f+a^2+(m-2)a <= 1`.

There is also a new local occupancy floor. The `(e,f,g)` edge-only PSD block, together with the negative signs and Simpson, yields

`p_g >= 2 C_ef/(p_e p_f+C_ef)`

for every third edge. Consequently `C_ef<=p_e p_f/3`, `rho_ef<=1/3`, and after summing and using `|F|<=r(M)`,

`2(m-2)C_ef <= (r(M)-p_e-p_f)(p_e p_f+C_ef)`.

These are source-safe necessary conditions, not closure.

## Remaining debt

The parent conjecture remains open. The next target is global graphic compatibility: rule out a loopless graphic independent-set law with one positive matched pair, all third edges negatively correlated to both, and simultaneous satisfaction of the all-conditioner Simpson lower bounds plus the spectral/occupancy constraints above. Do not return to universal STAR-2 monotonicity or rank-degree CLC.

Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B03/20260922T070756Z-B03-forest-r12-34330b0f/report.md` in `yspennstate/math-open-problems`, creation commit `038ffa98b8b5ece198d38c481af10c99318f343f`. Exact checker creation commit `e172df83cbb3d517465a4a6c30014f36e145ea22`; output creation commit `04ed29589befe48e35ecc24b673cf0aec5b2870b`, ending `STATUS=PASS`.
