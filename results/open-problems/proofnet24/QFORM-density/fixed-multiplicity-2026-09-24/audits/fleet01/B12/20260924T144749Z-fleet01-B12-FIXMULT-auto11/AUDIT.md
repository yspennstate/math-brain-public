# fleet01/B12 complete fixed-multiplicity audit

Run: `20260924T144749Z-fleet01-B12-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

## Verdict

**PASS — complete mathematical audit of the pinned 790-line manuscript.**

I read `manuscript.tex` from line 1 through the end and independently re-derived every definition, displayed identity, lemma, proposition, corollary, theorem invocation, constant-bearing estimate and final scaling step. I found **no mathematical FALSE statement and no mathematical GAP** in the written candidate theorem

\[
s_{17}(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
\le 10^4 K^2/s,
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary affine terms, and independent real coordinates with densities bounded by `K`. No Gaussian, support, moment, iid, sign, exact-rank, log-concavity, or post-rotation-independence hypothesis is needed. The manuscript does **not** prove the unrestricted three-eigenvalue conjecture.

The support package requested by the owner is now present on fresh `master`: `README.md`, `AUDIT.md`, `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`. This resolves the package-absence issue recorded in my previous invocation.

## Exact range-by-range audit

The line ranges below are the source ranges in the pinned manuscript. `PASS` means I checked the statement and proof against its exact hypotheses, not merely against a prior report.

| Source range | Item | Verdict | Independent audit reasoning |
|---|---|---|---|
| 1–46 | title, scope, notation, normalization conventions | PASS | Quantifiers agree with the stated arbitrary-law/symmetric-matrix/affine scope; no hidden regularity or rotated-independence assumption. |
| 47–57, proof 726–749 | main 17-direction theorem | PASS | Branch exhaustion is scalar pivot / definite pair / indefinite pair / no pivot. Constants all stay below `10000`; final `Y=KX`, `A/s` scaling contributes exactly `K^2/s`. |
| 59–61 | 33-direction corollary | PASS | Immediate monotonicity of ordered singular values. |
| 63–90 | preliminary definitions and Fourier convention | PASS | Conventions used consistently in later Plancherel and inversion constants. |
| 91–120 | Gaussian inversion / Fourier density lemma | PASS | Regularization, Fubini/Tonelli and limiting argument are valid for rough laws; `(2pi)^{-1}` normalization is consistent. |
| 122–130 | power-envelope integration | PASS | Direct split at the crossover scale gives the displayed `L^1` Fourier bound and density constant for exponent `>1`. |
| 132–160 | negative half-moment / Riesz lemma | PASS | Gaussian/Riesz representation and truncation are used in the correct direction; full versus truncated kernels are kept distinct downstream. |
| 169–181 | rank perturbation lemma | PASS | Min-max/rank-loss indexing is correct and is used consistently in interpolation and Schur counts. |
| 183–207 | principal-Schur spectral count | PASS | Congruence/graph-subspace argument loses at most the pivot-block dimension and does not assume invertibility outside the pivot. |
| 209–217 | strict diagonal dominance | PASS | Gershgorin/elementary invertibility criterion is applied only with strict row dominance. |
| 221–255 | geometric Brascamp–Lieb heat-flow proof | PASS | Weight condition, covariance inequality, monotonicity, Gaussian endpoint and rough-law limiting passage are all valid. |
| 258–282 | product-projection density | PASS | Deterministic polar/Jacobian reduction preserves the original product law; no independence of projected coordinates is asserted. |
| 284–301 | scalar Fourier-power estimate | PASS | Rearrangement/Plancherel interpolation and scaling in the frequency variable are correct for every required exponent `p>=2`. |
| 310–324 | decoupling with independent copies | PASS | The copy structure and square-root exponent are correct; the retained phases are handled before absolute values. |
| 326–373 | regularized determinant theorem | PASS | Graph determinant/Jacobian identity, leverage weights, regularizer and determinant aggregation are algebraically consistent. |
| 386–400 | crossing-volume Fourier envelope | PASS | Exterior-volume lower bound is inserted with correct homogeneity and Fourier exponent. |
| 404–414 | scalar square inverse profile | PASS | Completing the square is performed in a literal original coordinate; conditional measure domination yields the inverse-square-root kernel without an independence claim between the square and the remainder. |
| 423–434 | definite pair | PASS | Two-dimensional coarea/area estimate gives the stated determinant-scale density cap. |
| 437–482 | hyperbolic pair | PASS | The two hyperbola branches have Jacobian `1/(2 sqrt D)`; tail monotonicity and the rough-density bathtub bound are valid; `Lambda>=2/sqrt D` produces the stated logarithmic envelope. |
| 485–525 | quarter-power concentration | PASS | Layer-cake and splitting arguments correctly convert the density/potential inputs without silently upgrading endpoint regularity. |
| 528–535 | pivot and disjoint-volume definitions | PASS | Scalar/pair thresholds and disjointness conventions match all later uses. |
| 545–564 | determinant-squared sampling | PASS | Ordered/disjoint multiplicities and normalization are correct. |
| 566–580 | interpolation completion | PASS | The completion is genuinely nonsymmetric; `D` vanishes on the seed, global rank is `<=3r`, and the restricted residual rank is `<=r`. |
| 582–619 | no-pivot spectral-to-volume proposition | PASS | The sampled error estimate, rank subtraction and strict diagonal-dominance contradiction have correct dimensions; the terminal count is `4r-3`. |
| 621–630 | fair coordinate cut | PASS | Every disjoint `k x k` minor crosses with probability `4^{-k}` and Cauchy–Binet gives the stated crossing volume. |
| 632–645 | no-pivot nine-direction intermediate | PASS | `k=3` uses exactly nine singular directions and the determinant receiver gives the advertised bounded density. |
| 654–674 | logarithmic and square-root kernel estimates | PASS | Truncation ranges and integrability exponents are correct; no full half-potential is inferred from a truncated one without paying the tail. |
| 676–714 | pivot truncated half-potential proposition | PASS | Scalar, definite-pair and indefinite-pair branches retain the required Schur directions and use the correct kernel estimate. |
| 716–724 | nine-direction half-potential proposition | PASS | The no-pivot order-two branch uses only the amount of spectral information claimed; the pivot branch invokes the preceding proposition correctly. |
| 726–790 | main scalar closure, constants, rescaling and closing remarks | PASS | Scalar pivot uses the full remainder half-potential, pair pivots are smaller, no-pivot branch is already closed, and rescaling is dimensionally exact. |

## B12 starting-lens audit

The particularly sensitive chain for this slot is also PASS:

1. **Scalar completion:** the coefficient `A_ii` is an original-coordinate coefficient. Completing its square modifies only the deterministic Schur polynomial in the other original coordinates; it never declares the square and Schur remainder independent.
2. **Square inverse branch:** the conditional profile is a measure-domination inequality with the exact `|a|^{-1/2}|z-R|^{-1/2}` kernel.
3. **Hyperbolic logarithm:** the pair coarea formula is valid a.e.; the critical level is null and the nonnegative-test-function version is adequate under further conditioning.
4. **Full versus truncated half-potential:** the manuscript pays the far tail by the trivial bound `|R-a|^{-1/2}<=1` outside unit distance before using the scalar square profile. No truncated-to-full shortcut occurs.
5. **Nine-eigenvalue intermediate and main scalar closure:** the intermediate no-pivot theorem and the later half-potential theorem have distinct roles and their spectral counts are sufficient at every invocation.

## Supplementary package status

Fresh `master` now contains all six named support files. I read all of them in full.

- `SOURCE_MANIFEST.json`: PASS as a source-identification record; it pins the same manuscript hash/blob used above.
- `proof_map.csv`: PASS as a dependency/range map; its ranges agree with the source.
- `verify.py`: PASS as a readable scoped checker script; its tests target interpolation identities, volume identities, Schur-threshold numerics and graph-weight identities.
- `checks.json`: reports `PASS` for the current scoped suite (534 exact interpolation seeds, 18 exact volume comparisons, 240 numerical Schur-threshold cases and 30 graph-weight cases, with exact diagonal-dominance slack `297/2800`). These checks are supporting diagnostics, not proof.
- `AUDIT.md`: read in full. It is the authoring/self-audit record and is not counted as independent validation.
- `README.md`: read in full; its theorem/scope/review-gate description is consistent with the source.

## UNCHECKED portions

The following are the only items I leave `UNCHECKED`; none is a missing mathematical implication in the 17-direction proof.

1. **Checker execution by this B12 invocation — UNCHECKED.** I read `verify.py` and the committed `checks.json`, but did not independently execute the script in this connector-only runtime. I therefore do not relabel the committed checker output as a fresh B12 execution.
2. **Historical finite-check counts in the older self-audit — UNCHECKED as a fresh rerun.** The current scoped `checks.json` is a newer suite with different counts. I do not conflate the two runs.
3. **Compiled PDF rendering / visual typography — UNCHECKED.** The mathematical source was audited; no committed PDF binary is needed for the theorem proof and I did not independently compile/render one here.
4. **External priority/literature completeness — UNCHECKED in this run.** The manuscript is self-contained, so this is not a proof dependency. I made no novelty claim from search absence.

## Impact and next obligation

The pinned 17-direction manuscript remains mathematically PASS in this independent B12 audit. A strictly stronger complete nine-direction replacement theorem exists in the repository and is reviewed separately in the companion improvement file for this run. The unrestricted three-eigenvalue conjecture is still open.
