SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-24T13:44:20Z.
attacking: fixed-multiplicity manuscript audit with the B12 scalar-pivot/square/logarithmic-kernel lens, then the first lower-multiplicity scalar-pivot closure.

# fleet03/B12 r57 — complete fixed-multiplicity audit

Run: `20260924T134420Z-fleet03-B12-fixedmult-audit-r57`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## Source pin

Baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`  
Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Length: 790 lines / 47,883 bytes.

I reread all 790 source lines in contiguous ranges. I also read the current `README.md`, `DELIVERY_STATUS.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. The reproducibility-package absence reported in my preceding B12 run is now repaired: all four formerly absent files are present on current `master`, and the new checker reports PASS on its stated finite scope. This finite suite is diagnostic only and is not used as a proof premise.

## Verdict

**PASS on the pinned seventeen-eigenvalue theorem in this independent B12 reread.** I found no fatal mathematical gap and no hidden support, moment, Gaussian, log-concavity, connected-support, exact-rank, or post-rotation-independence assumption. The conclusion of the baseline source is essential boundedness, not global continuity. Bibliographic priority/attribution was not independently re-researched in this run and remains UNCHECKED as a non-proof dependency.

This is one mathematical review, not formal verification or journal peer review. The unrestricted three-eigenvalue conjecture remains OPEN.

## End-to-end line ledger

| Source lines | Content | Verdict | B12 reasoning / downstream impact |
|---|---|---|---|
| 1–90 | theorem, scaling architecture, fixed parameters | PASS | Quantifiers match arbitrary independent cap-`K` laws, symmetric `A`, arbitrary `b,c`; the normalized/scaled statement has the correct `K^2/s` homogeneity. The paper explicitly separates essential boundedness from continuity. |
| 91–160 | Fourier identities, power envelope, Riesz half-potential | PASS | The `2π` normalization, Gaussian inversion, `1/sqrt(2π)` Riesz coefficient and weighted `|t|^{-1/2}` integral were rechecked. The order-three Fourier envelope is used only for a half-potential, not direct density inversion. |
| 161–217 | singular-value perturbation, Schur spectral count, diagonal dominance | PASS | Rank perturbation is correctly formulated for nonsymmetric auxiliary matrices. The Schur count is on the final symmetric quadratic matrix and loses at most the physical pivot dimension. The singular-pivot approximation preserves the non-strict threshold in the limit. |
| 218–301 | geometric BL, product projections, scalar Fourier powers | PASS | The heat-flow sign follows from the Parseval-frame contraction. Rough nonnegative inputs are reached by monotone truncation. In the projection proof, dropping `b_i=0` factors and then enlarging the entropy sum by their nonnegative `1-b_i` contributions is legitimate. Difference densities are capped by one. |
| 302–400 | physical-bank decoupling, regularized crossing determinant, crossing-volume envelopes | PASS | Independent copies are introduced only in original coordinate banks. Rotations occur only in deterministic Jacobians/frames. The determinant exponent `-1/8` and the distinction between order three (half-potential) and order five (density) are consistent. |
| 401–525 | scalar square profile, definite pair, hyperbolic pair, quarter-power concentration | PASS | The scalar profile is a conditional measure-domination statement and does not assert independence between the square and its Schur remainder. The hyperbolic change of variables keeps the original product density in the integrand. The logarithmic singularity is genuine and is integrated only after obtaining anti-concentration of the critical-value remainder. |
| 526–645 | pivots/volumes, sampled interpolation, completion, spectral-to-volume, random cut | PASS | The interpolation can be nonsymmetric without entering the random quadratic form. The global `rank R<=3r` and restricted `rank R[L,L]<=r` are used at distinct steps; `D=0` on the seed is essential. The diagonal-dominance contradiction uses the explicit positive slack. |
| 646–724 | singular kernels, pivot half-potential, nine-direction half-potential | PASS | The square-root convolution has unavoidable logarithmic growth near coincident critical values; the quarter-power logarithmic moment pays it. The pivot proposition needs only two surviving unit spectral directions. Full half-potential is obtained from the truncated bound by adding at most one outside `|Z-a|<=1`. |
| 725–780 | main theorem, scaling, threshold accounting | PASS | The scalar pivot loses one spectral direction and invokes the nine-direction half-potential theorem; pair pivots are dependence-safe after conditioning on original coordinates. Scaling back gives `K^2/s`. The source does not claim optimal multiplicity. |
| 781–790 | acknowledgments / classical attribution | UNCHECKED | No mathematical dependency: the specialized inequalities used by the proof are reproved in the manuscript. Priority was not re-searched here. |

## B12 scalar-kernel checks

At a scalar pivot `a=A_ii`, conditioning on the complement gives

\[
Q=a(X_i-m)^2+R,
\qquad
p_Q(z)\le |a|^{-1/2}\,\mathbb E|z-R|^{-1/2}.
\]

This is valid even though the shift and `R` depend on the conditioned variables. The proof is by nonnegative output test functions and Tonelli, not by declaring the two terms independent.

The two endpoint singularities in the source are genuinely necessary:

1. `X~Unif[-1/2,1/2]` gives density `p_{X^2}(u)=u^{-1/2}` on `(0,1/4)`, so a scalar square by itself has no bounded density.
2. `X,Y~Unif[-1/2,1/2]` gives `2XY` a logarithmic density singularity at zero, so an indefinite pair cannot be replaced by a uniform conditional `L∞` bound.

The manuscript's logarithmic kernels and quarter-power anti-concentration therefore address real endpoint obstructions rather than proof slack.

## Reproducibility package status

Current `master` contains `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`. The manifest pins the unchanged 790-line source. The current checker reports 534 exact interpolation seeds, 18 exact volume-sampling cases, 9 strict sampling cases, 240 floating Schur-threshold diagnostics, and 30 graph-weight diagnostics, with exact diagonal-dominance slack `297/2800`. These checks are useful algebraic diagnostics but do not replace the analytic proof or this review.

## Lower-threshold status after this audit

The repository now contains a separate nine-eigenvalue replacement argument based on a grouped product-Fourier compiler and marginal-free order-three/order-two receivers. I read that source and an independent reconstruction. It is not silently merged into the pinned seventeen-eigenvalue manuscript by this audit. A separate improvement in this run uses only the independently reconstructed order-two half-potential receiver, the pinned baseline lemmas, and the designated fleet04/B12 scalar-kernel result to prove a six-eigenvalue **scalar-pivot branch**. It does not close multiplicity eight or the full three-eigenvalue target.

## Status

- Pinned seventeen-eigenvalue theorem: **PASS in this B12 review**.
- Reproducibility support package: **present; finite checker PASS on its stated scope**.
- Global continuity of the pinned theorem: **not proved by the pivot branches**.
- Full three-eigenvalue QFORM conjecture: **OPEN**.
- New scalar-pivot `s_6` branch: see the sibling improvement for this run.
