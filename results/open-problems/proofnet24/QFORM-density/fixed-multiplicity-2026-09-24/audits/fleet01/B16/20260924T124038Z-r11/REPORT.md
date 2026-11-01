# fleet01/B16 independent end-to-end audit — fixed multiplicity

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T124038Z-r11`  
Lens: independent reconstruction before reading peer verdicts.

## Source pin and package state

Mathematical source audited: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`. At run start I observed master at `8ff490c177d0cd7d6f33130f1431785e312a9d10`; later I re-read the manuscript at master snapshot `3af907947fc7e22fdac6294c53e2806edb6de71d`, and GitHub returned the same manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`. Thus concurrent audit/improvement commits did not alter the mathematical source audited here.

`README.md` and `AUDIT.md` were present and read. Direct fetches of `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` at the pinned master snapshot returned 404. Status for those four advertised supplementary artifacts: **GAP / UNCHECKED because absent from the repository root**. This is a reproducibility/package gap, not a dependency gap in the written theorem, because the proof used below is contained in `manuscript.tex` itself. I did not recompute the advertised raw-file SHA-256; the Git blob was independently observed.

## Overall mathematical verdict

**PASS for the complete written 17-eigenvalue theorem.** I read all 790 source lines in order and reconstructed the argument without using the author self-audit as a premise. I found no fatal mathematical gap in the statement

`independent real coordinate densities <= K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, `s_17(A)>=s>0`

imply

`||p_(X^T A X+b^T X+c)||_infinity <= 10000 K^2/s`.

This is one independent worker review only. It does not confer release/validation status and does not address the unrestricted three-eigenvalue conjecture.

## Exhaustive line audit

| Source range | Status | Independent reconstruction / check | Downstream impact |
|---|---|---|---|
| 1–45 | PASS | Preamble and abstract match the theorem actually proved. No hidden support, smoothness, moment, sign, log-concavity, or diagonal assumptions are introduced. | Scope preserved. |
| 46–83 | PASS | The singular-value convention is correct for symmetric `A`; theorem quantifiers include arbitrary dimension, remaining spectrum, affine terms and rough product densities. The normalization plan with `eta=1/100`, `kappa=1/80^2` is consistent. | Main theorem correctly formulated. |
| 84–160 | PASS | Plancherel uses the stated Fourier convention. Gaussian regularization gives the inversion identities with constants `1/(2 sqrt(pi v))`. The Riesz representation has coefficient `1/sqrt(2 pi)`; the `3/4` envelope integrates to `12 sqrt(u)` after the weight `|t|^{-1/2}`. Tonelli is applied only to nonnegative quantities after absolute values. | Fourier inversion and half-potential receiver valid for rough laws. |
| 161–220 | PASS | Approximation-number formulas give the nonsymmetric singular-value perturbation/rank inequalities. For an invertible principal pivot, the complementary block of `A^{-1}` equals the inverse Schur complement; positive and negative principal-compression interlacing separately imply `N_S(t)>=N_A(t)-k`. The `A+epsilon I` limiting argument handles singular `A`. Strict row diagonal dominance needs no symmetry. | All later Schur and rank uses justified. |
| 221–300 | PASS | Heat-flow proof of geometric rank-one BL: `partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` follows from the Parseval frame; large-time mass normalization and small-time Fatou are valid. Product-projection density is obtained by deterministic fiber integration; no rotated-coordinate independence is asserted. Scalar Fourier-power estimate is noncircular because `|hat f|^{2m}` is integrable by Plancherel before inversion at zero. | Projection and scalar Fourier inputs valid. |
| 301–400 | PASS | Cauchy–Schwarz gives the power-2 decoupling and Jensen gives power 4. Difference coordinates remain independent with density cap one. In the graph BL step, the regularized frame is exact, row weights satisfy `0<=d_i<=1`, `sum d_i=sum(1-c_j)`, scalar Fourier powers cancel the `d_i` Jacobians, and `alpha=(2 pi e)^2` cancels the remaining entropy factor. Fourth roots give exponent `-1/8`. Cauchy–Binet then yields the stated order-5 and order-3 envelopes. | No-pivot Fourier engine valid. |
| 401–428 | PASS | Scalar quadratic inverse branches give the square-root profile and interval-preimage estimate. Conditional use is measure domination, not independence. Definite two-coordinate polar coordinates have Jacobian `1/(2 sqrt(det B))`, yielding `pi M/sqrt(|det B|)`. | Scalar/definite pivots valid. |
| 429–484 | PASS | Hyperbolic parametrization has Jacobian `1/(2 sqrt D)`. On each branch `u e^t+w e^{-t}`, an original coordinate controls each tail; after the cutoff, `|y'|>=|y|/3`, density cap plus mass bounds the tail by `3 log 2`. The middle length gives `(15/2)log2`, and `Lambda>=2/sqrt D` converts the scale to `16 sqrt D/|z-v|`. Exceptional critical levels are harmless in the test-function/Tonelli formulation. | Indefinite pair receiver valid without post-rotation independence. |
| 485–530 | PASS | If no diagonal entry is at least `||S||/2`, the random-sign cut isolates a physical cross block of norm at least `||S||/4`. Retaining its largest singular factor gives `|phi(t)| <= (4 pi e/(L|t|))^(1/4)`. Gaussian smoothing at `v=1/8` gives the quarter-power small-ball estimate; layer cake gives `L0=4+4 log16`. | One surviving spectral direction controls the logarithmic singularity. |
| 531–584 | PASS | `V_r` uses ordered disjoint minors. The bordered determinant identity is correct; singular deleted seeds can have nonsingular extensions, so the sampling step is correctly an inequality. `P=A[:,T] B^{-1} A[S,:]` exactly interpolates rows `S` and columns `T` despite being nonsymmetric. Completion gives `D=0` on the seed, `E_ii=0`, global `rank R<=3r`, and restricted `R[L,L]=P[L,L]` with rank `<=r`. | Sensitive interpolation support/rank claims pass. |
| 585–652 | PASS | A bad volume ratio gives `||E||<=1/16`. With `m=4k-3`, global rank `3r` forces at least `r+1` diagonal entries of `D` of modulus `>=1-epsilon`, all in `L`. On those coordinates `|R_ii|>=371/400`, while each off-diagonal is `<1/7+1/16`; for `r<=4` the row sum is `<23/28`, so strict diagonal dominance contradicts `rank R[L,L]<=r`. Fair cutting preserves each ordered disjoint minor with probability `4^{-k}`. Constants give `12 sqrt(80e)=176.959...<200` and `800e=2174.625...<2400`. | Spectral-to-volume proposition and both no-pivot analytic consequences pass. |
| 653–726 | PASS | The two singular-kernel integrals are bounded correctly. Scalar pivot plus one surviving Schur direction gives truncated half potential `<600`; definite and indefinite pair alternatives are uniform. The distinction between truncated and full half potential is explicit: the tail outside radius one costs at most one, yielding `<=601`. | Exactly the receiver needed by the main scalar pivot. |
| 727–774 | PASS | The case split is exhaustive. Under `s_17>=1`, a scalar pivot leaves at least 16 Schur directions and hence the nine-direction half-potential theorem; a two-coordinate pivot leaves at least 15, while the indefinite branch needs only one surviving direction. Largest normalized branch is `6010`; other branches are `<2400`, `<40`, and `<251`. Scaling `Y=KX` and `Q=(s/K^2) Qtilde` gives `10000 K^2/s`. | Main theorem closes with all original hypotheses. |
| 775–790 | PASS for theorem scope; UNCHECKED for external attribution/priority | Limitations correctly do not claim the three-eigenvalue theorem or global continuity. BCCT/RV are attribution only; I did not perform a primary-source novelty/priority audit in this B16 run. | No theorem dependency is left unchecked. |

Every mathematical source line 1–790 is included in a contiguous PASS range above. The only UNCHECKED items are external attribution/priority and the four advertised-but-absent supplementary artifacts.

## Labeled statement / equation audit

PASS: `thm:main`, `cor:33`, `lem:fourier`, `lem:envelope`, `lem:riesz`, `lem:rank`, `lem:schur`, `lem:dd`, `thm:bl`, `lem:projection`, `lem:scalar-fourier`, `lem:decoupling`, `thm:determinant`, `cor:vol-fourier`, `lem:square`, `lem:definite`, `lem:hyperbola`, `lem:quarter`, `def:pivot-volume`, `lem:sampling`, `lem:completion`, `prop:volume`, `lem:cut`, `cor:no-pivot`, `lem:kernels`, `prop:pivot-H`, `prop:nine`, and the final theorem proof.

The corresponding labeled formulas were checked at the constants used: `eq:main`, `eq:parameters`, `eq:plancherel`, `eq:inversion`, `eq:gaussian-inversion`, `eq:envelope`, `eq:riesz`, `eq:riesz-power`, `eq:rank-perturb`, `eq:frame`, `eq:bl`, `eq:projection`, `eq:scalar-fourier`, `eq:cross-form`, `eq:decouple2`, `eq:decouple4`, `eq:determinant`, `eq:graph-bl`, `eq:Zk`, `eq:det-expand`, `eq:vol-envelope`, `eq:five-volume`, `eq:three-volume`, `eq:profile`, `eq:hyperbola`, `eq:hyper-coarea`, `eq:quarter`, `eq:log-bound`, `eq:Vr`, `eq:small-entry`, `eq:P`, `eq:sampling`, `eq:completion`, `eq:completion-bounds`, `eq:volume-lower`, `eq:cut`, `eq:no-pivot-nine`, `eq:no-pivot-seventeen`, `eq:H`, `eq:J`, `eq:log-kernel`, `eq:pivot-H`, `eq:scalar-max`, `eq:nine-H`, and `eq:final-scalar`.

## Degenerate-case ledger

- `A` singular: handled in `lem:schur` by an invertible `A+epsilon I` sequence with pivot preserved off a discrete set and Schur complements converging.
- `d_i=0` in the determinant frame: the corresponding row of `M` is zero and its Fourier factor is one, so omission is legitimate.
- zero-volume stages: the telescoping argument takes the first vanishing volume and uses the previous positive volume; no division by zero occurs.
- singular sampled seeds: they have zero sampling weight; nonsingular extensions of singular seeds are why the volume count is an inequality rather than equality.
- rough densities / exceptional level sets: every conditional singular profile is used through nonnegative test functions and Tonelli; no pointwise conditional-density version is assumed on null slices.
- affine terms: remain arbitrary throughout; they are absorbed into conditional translations/phases and never enter a spectral hypothesis.
- nonsymmetric auxiliaries `P,R,E`: only singular-value/rank estimates are applied to them; the original quadratic matrix remains symmetric.

## Package gap

The repository documentation currently claims `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` as package members, but they were absent (404) at the pinned master snapshot. Status: **GAP** in reproducibility/documentation. The theorem proof itself does not depend on these files, so this is **not fatal to the mathematical PASS**.

## Review-state conclusion

Baseline 17-eigenvalue manuscript: **PASS in this independent review**. This report is one independent full review and must not be converted into a self-awarded final validation certificate without satisfying the owner's separate-review rule.
