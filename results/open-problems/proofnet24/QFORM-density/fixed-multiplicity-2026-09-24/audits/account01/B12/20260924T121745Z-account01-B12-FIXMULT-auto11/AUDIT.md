# account01/B12 independent end-to-end audit

Run: `20260924T121745Z-account01-B12-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Source git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Fresh-master manuscript blob at review: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Verdict

**Mathematical verdict: PASS for the complete written 17-eigenvalue candidate.** I independently read and re-derived the complete 790-line `manuscript.tex`. I found no FALSE statement and no mathematical GAP in the proof of

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}\le 10^4K^2/s
\]

under the manuscript's full arbitrary-product-law, arbitrary-sign, arbitrary-dimension and arbitrary-affine hypotheses.

This is one independent review, not a self-awarded independent-validation certificate. The owner requires two genuinely separate complete reviews before that status is assigned. The unrestricted three-eigenvalue conjecture is not proved here.

**Repository-package verdict: GAP / UNCHECKED.** On fresh `master`, the manuscript root contains `manuscript.tex`, `README.md`, `AUDIT.md`, `audits/`, and `improvements/`, but the four supplementary files named by the README/current objective — `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` — are absent. Therefore the advertised finite-check bundle is **UNCHECKED in this review**. I do not infer its contents from the self-audit. This package defect does not create a mathematical gap in the self-contained manuscript.

## Complete line audit

### Lines 1--74 — PASS
Statement, quantifiers, definitions, normalization and proof architecture are consistent. For symmetric `A`, singular values are absolute eigenvalues. The claimed scale `K^2/s` is correct. The normalized pivot threshold is `eta=1/100`, the volume scale is `kappa=1/80^2`, and the proof separates scalar pivots, definite/indefinite two-coordinate pivots, and no-pivot crossing-volume branches without rotating the product law.

### Lines 75--129 — PASS
The Fourier convention, Gaussian normalization, Plancherel regularization and inversion constants are correct. The power-envelope integral is exactly `2ap/(p-1)`, hence the density bound `ap/[pi(p-1)]`.

### Lines 130--169 — PASS
The gamma representation of `|z|^{-1/2}`, Gaussian inversion, two Tonelli steps and the integral

`int_0^infty v^(-5/4) exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4)|t|^(-1/2)`

produce the stated Riesz constant. The `3/4` Fourier envelope gives weighted integral `12 sqrt(u)` and therefore the displayed full negative-half-moment estimate.

### Lines 170--218 — PASS
The singular-value approximation formula supports both perturbation and nonsymmetric rank-shift inequalities. The Schur-complement count is valid: for invertible `A`, the complementary principal block of `A^{-1}` is `S^{-1}`, and positive and negative principal-compression threshold counts give `N_S(t)>=N_A(t)-k`; the singular case is correctly obtained through `A+epsilon I`. Strict diagonal dominance is correctly used for nonsymmetric matrices.

### Lines 219--255 — PASS
I re-derived the heat-flow geometric Brascamp--Lieb proof. With `v_i=partial_s log f_i`,

`partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`

because the frame map with columns `sqrt(c_i)u_i` is a contraction. Gaussian tails justify the integration by parts on compact positive-time intervals; `sum c_i=d` gives the exact large-time normalization; inverse images of one-dimensional non-Lebesgue-point sets are null; truncation plus monotone convergence closes the rough-data case.

### Lines 257--309 — PASS
The product-projection density estimate uses an orthogonal change of variables only inside a deterministic integral and never asserts rotated independence. The frame weights and entropy estimate give `e^{d/2}`. The scalar Fourier-power lemma correctly uses the `m`-fold difference law, Fourier inversion at zero and the scalar projection bound, including the exponent and constant.

### Lines 311--421 — PASS
Both decoupling powers are valid under the original coordinate product law. In the regularized determinant proof, `alpha=(2*pi*e)^2`, the coordinate and row weights form an exact geometric frame, the one-dimensional Jacobians are correct, the `d_i` powers cancel, the `c_j` entropy tax contributes at most `e^{theta/2}`, and the scalar Fourier constant cancels because `sqrt(alpha)=2*pi*e`. Taking the fourth root gives the determinant exponent `-1/8`. Cauchy--Binet and the `k=5` / `k=3` envelopes have the stated constants and exponents.

### Lines 422--519 — PASS, primary B12 lens
The scalar square inverse branches and interval-preimage bound are correct. Conditional use in the scalar-pivot profile is measure domination via nonnegative test functions and Tonelli, not an independence claim.

The definite-pair polar Jacobian gives `pi M/sqrt(|det B|)`.

For the indefinite pair, the hyperbolic parameterization has absolute `(delta,t)` Jacobian `1/(2 sqrt(D))` on each branch. Writing a branch as `u e^t+w e^{-t}`, one original coordinate has `|u_i|>=rho_0/sqrt(2)`. The cutoff makes that coordinate monotone with derivative at least one third of its magnitude. Filling the nearest unit interval is the correct extremizer for the one-sided decreasing weight `1/|y|`; the two tails are finite uniformly for arbitrary rough densities. The middle interval produces the logarithm, and `Lambda>=2/sqrt(D)` has the correct direction. Exceptional critical levels are handled through the test-function formulation.

The quarter-power lemma is also valid. If no large diagonal exists, random signs create a literal original-coordinate cross block with norm at least `L/4`. Keeping one singular factor in the determinant theorem gives the `|t|^{-1/4}` envelope. Gaussian smoothing gives the displayed small-ball exponent and layer cake gives `L_0=4+4 log 16`. The no-atom conclusion is established before it is used downstream.

### Lines 520--679 — PASS
The ordered disjoint-minor convention is consistent. The volume-sampled interpolation correctly excludes singular seeds from the sampling law, uses the bordered determinant identity, and only claims an inequality when singular seeds can have nonsingular extensions. The auxiliary `P=A_{.,T}B^{-1}A_{S,.}` is allowed to be nonsymmetric.

The completion has `rank R<=3r`, `R[L,L]=P[L,L]`, `rank R[L,L]<=r`, zero diagonal `E`, and `D=0` on the seed. In the spectral-to-volume contradiction, `||E||<=1/16`, nonsymmetric singular-value rank shifting supplies at least `r+1` large entries of the diagonal `D`, those entries lie in `L`, and the induced `R[H,H]` is strictly diagonally dominant. The contradiction is with the *restricted* rank `<=r`, not the global rank. The random-cut factor is exactly `4^{-k}`.

### Lines 680--720 — PASS, primary B12 lens
For the two singular kernels, the near part of `J(d)` is uniformly finite and the far part is logarithmic; the log-kernel overlap is maximized when the interval centers coincide, giving the constant 8. No pointwise regularity of the input densities is required.

The pivot-to-truncated-half-potential proposition is correct in all three cases. A scalar pivot leaves at least one large Schur direction under the stated `s_2` hypothesis, so the logarithmic potential of the critical quadratic remainder is available. The definite-pair branch is uniformly bounded. The indefinite-pair branch integrates the hyperbolic log envelope against the truncated half kernel and the scalar maximization `sup D^{-1/2} log_+ D=2/e` is correct.

### Lines 721--790 — PASS, primary B12 lens
The distinction between truncated and full half potentials is handled correctly. Under `s_9(A)>=1`, a pivot gives `H(Q)<=600`; no pivot gives the stronger full half-potential `<200`. Outside `|Q-a|<=1`, the kernel is at most one, so the full half-potential is at most 601.

In the main scalar-pivot branch, `s_17>=1` and a one-coordinate Schur complement leave at least sixteen large eigenvalues and hence the nine needed by the preceding proposition. The profile therefore gives `10*601=6010`.

A definite pair gives the direct uniform conditional density bound. An indefinite two-coordinate pivot leaves at least fifteen large directions; the proof actually needs only one surviving large direction to control the logarithmic critical-value average. Dependence of the critical value on conditioned coordinates is handled by Tonelli/test-function domination.

Finally `Y=KX` has coordinate density caps one and `Q=(s/K^2)\widetilde Q`; the affine coefficients in `\widetilde Q` are transformed correctly. Density scaling yields exactly `10^4K^2/s`.

## Explicit UNCHECKED material

Only the absent supplementary package is UNCHECKED: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`, and therefore the numerical/checker claims attributed to those files. The mathematical content of `manuscript.tex` has no intentionally UNCHECKED range in this review.

## Threshold reduction found in this run

The baseline 17 theorem is sound, but the multiplicity is used only in the no-pivot order-five branch. The pivot branches admit much lower local thresholds, and the attempt to replace 17 by 16 reduces to one exact algebraic chamber. A full proof is saved separately in this run's improvement artifact `TERMINAL_R4_AND_PIVOT_REDUCTION.md`.

The key conclusion is: under no pivot and `s_16(A)>=1`, the existing proof already rules out every bad interpolation ratio of orders `r=0,1,2,3`; the only possible failure of the order-five crossing-volume conclusion is the terminal `r=4` chamber, where the restricted rank bound is saturated exactly. Thus `17 -> 16` requires one new argument only for that chamber (or a different analytic receiver). The scalar-pivot branch itself closes already from ten large eigenvalues; an indefinite pair closes from three.

## Final review status

- 17-eigenvalue candidate theorem: **PASS in this independent account01/B12 review**.
- FALSE statements found: **none**.
- Mathematical GAPs found: **none**.
- Repository reproducibility package: **GAP / UNCHECKED because four named files are absent**.
- Unrestricted three-eigenvalue conjecture: **OPEN**.
- Unconditional threshold reduction below 17: **not completed in this run**; `s_16` is reduced to one explicit terminal saturation chamber.
