# fleet01/B12 complete fixed-multiplicity audit

Run: `20260924T152031Z-fleet01-B12-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

## Verdict

**PASS — complete mathematical audit of the pinned 790-line manuscript.**

I reread `manuscript.tex` line 1 through line 790 in this invocation, together with `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`. I independently rechecked every displayed identity, definition, lemma/proposition/theorem proof, constant-bearing inequality, branch transition, and scaling step. I found **no mathematical FALSE statement and no mathematical GAP** in the written candidate theorem

\[
s_{17}(A)\ge s>0
\Longrightarrow
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}\le 10^4 K^2/s,
\]

for arbitrary real symmetric `A`, arbitrary dimension, arbitrary affine terms, and independent real coordinates with densities bounded by `K`. No Gaussianity, iid law, support, moment, sign, log-concavity, exact-rank, diagonal-basis, or post-rotation-independence hypothesis is used. The unrestricted three-eigenvalue conjecture is not proved by this manuscript.

## Exact range-by-range audit

| Source range | Item | Verdict | Reasoning checked |
|---|---|---|---|
| 1–46 | scope, notation, normalization, Fourier convention setup | PASS | Quantifiers and normalizations match the theorem; no hidden regularity assumption. |
| 47–57; proof 726–749 | main 17-direction theorem | PASS | Four pivot/no-pivot branches exhaust cases; constants and final `K^2/s` scaling are correct. |
| 59–61 | 33-direction corollary | PASS | Immediate from ordered singular-value monotonicity. |
| 63–90 | preliminary conventions | PASS | Used consistently downstream. |
| 91–120 | Fourier/Gaussian inversion identities | PASS | Regularization, Fubini/Tonelli, Plancherel normalization and limiting passage are correct for rough laws. |
| 122–130 | power envelope | PASS | Crossover split and `L^1` Fourier integration are correct. |
| 132–160 | Riesz / negative half moments | PASS | Gaussian representation, truncation and constants are valid; full and truncated potentials are distinguished. |
| 169–181 | rank perturbation | PASS | Min-max indexing and rank loss are correct. |
| 183–207 | Schur spectral count | PASS | Congruence/graph-subspace argument loses only the pivot dimension. |
| 209–217 | strict diagonal dominance | PASS | Used only under strict row dominance. |
| 221–255 | geometric Brascamp–Lieb heat flow | PASS | Weight condition, covariance inequality, monotonicity, Gaussian endpoint and rough-law limit all check. |
| 258–282 | product-projection density | PASS | Jacobian/polar reduction preserves original product law; projected coordinates are never declared independent. |
| 284–301 | scalar Fourier powers | PASS | Rearrangement, Plancherel interpolation and frequency scaling are correct for all required exponents. |
| 310–324 | decoupling | PASS | Independent-copy structure and square-root exponent are correct. |
| 326–373 | regularized crossing determinant | PASS | Determinant/Jacobian identity, leverage weights, regularizer and determinant aggregation are algebraically consistent. |
| 386–400 | crossing-volume Fourier envelope | PASS | Exterior-volume homogeneity and Fourier exponent are correct. |
| 404–414 | scalar square inverse profile | PASS | Completion occurs in a literal original coordinate; conditional measure domination gives the inverse-square-root kernel without a false independence claim. |
| 423–434 | definite pair | PASS | Two-dimensional area/coarea estimate and determinant scaling are correct. |
| 437–482 | hyperbolic pair | PASS | Both branches, Jacobian, tail monotonicity and logarithmic envelope are valid for rough densities. |
| 485–525 | quarter-power concentration | PASS | Layer-cake/splitting correctly converts the potential inputs. |
| 528–535 | pivot and disjoint-volume definitions | PASS | Thresholds and disjointness conventions match all later uses. |
| 545–564 | determinant-squared sampling | PASS | Ordered/disjoint multiplicities and normalization are correct. |
| 566–580 | nonsymmetric interpolation completion | PASS | Seed zeros, global rank `<=3r`, restricted rank `<=r`, and interpolation identity are correct. |
| 582–619 | no-pivot spectral-to-volume proposition | PASS | Sampling estimate, rank subtraction and strict diagonal-dominance contradiction have the correct dimensions and terminal `4r-3` count. |
| 621–630 | fair coordinate cut | PASS | Each disjoint `k x k` minor crosses with probability `4^{-k}` and Cauchy–Binet gives the stated crossing volume. |
| 632–645 | no-pivot nine-direction intermediate | PASS | `k=3` uses exactly nine directions and the determinant receiver is applied at the correct scale. |
| 654–674 | two singular-kernel integrals | PASS | Logarithmic and square-root kernels, truncation ranges and constants are correct. |
| 676–714 | pivot truncated half-potential | PASS | Scalar/definite/indefinite branches retain enough Schur spectrum; no truncated-to-full shortcut occurs. |
| 716–724 | nine-direction half-potential proposition | PASS | No-pivot order-two and pivot branches use only the claimed spectral input. |
| 726–790 | main scalar closure, constants, rescaling, remarks | PASS | The scalar square profile receives a full half-potential; pair constants are smaller; final dimensional scaling is exact. |

## Starting-lens conclusions

The B12-sensitive chain is PASS. In particular: (i) scalar completion modifies only a deterministic Schur polynomial after conditioning on the literal pivot coordinate; (ii) the square inverse branch is a conditional measure-domination statement, not a convolution-independence statement; (iii) the hyperbolic logarithm is obtained by a valid two-branch Jacobian/coarea calculation; (iv) the far tail is explicitly paid before a truncated half-potential is upgraded to a full one; and (v) the nine-direction intermediate theorem and the final scalar closure have distinct roles and sufficient spectral counts.

## Supplementary package

All requested support files are present on fresh `master` and were read in full.

- `SOURCE_MANIFEST.json`: PASS as a source-identification record; it pins exactly the blob/hash audited here.
- `proof_map.csv`: PASS; statement/proof ranges agree with the manuscript.
- `verify.py`: PASS as a scoped checker source; it verifies interpolation/rank identities, volume sampling identities, exact diagonal-dominance arithmetic, and numerical Schur/graph diagnostics.
- `checks.json`: reports PASS for the committed scoped suite: 534 exact interpolation seeds, 18 exact volume comparisons, 9 strict sampling cases, exact slack `297/2800`, 240 numerical Schur-threshold cases, and 30 graph-weight cases. These computations are supporting diagnostics, not a proof certificate.
- `AUDIT.md`: read in full; it remains the authoring/self-audit record and is not counted as an independent review.
- `README.md`: read in full; theorem/scope/review-gate statements are consistent with the source.

## UNCHECKED portions

No manuscript proof line is left unchecked. The following non-proof items are **UNCHECKED** in this invocation:

1. **Fresh execution of `verify.py`: UNCHECKED.** I read the full script and committed `checks.json`, but this connector-only invocation did not execute the Python checker against the repository checkout.
2. **Historical finite-test counts from the older self-audit: UNCHECKED as a rerun.** The current reproducibility suite is explicitly a newer suite and does not reproduce every historical count.
3. **Compiled PDF rendering/typography: UNCHECKED.** I audited the source, not a freshly compiled/rendered PDF binary.
4. **External priority/literature completeness: UNCHECKED.** This is not a dependency of the self-contained proof and no novelty claim is made from search absence.

## Improvement status from this run

After this full audit I obtained a new candidate **multiplicity-eight** closure, saved separately in this run's improvement directory. It uses the already-proved `s_8` robust-two-anchor extraction, a new no-pivot leverage localization observation, and a one-exception interpolation completion. It preserves all arbitrary-law/matrix/affine hypotheses. It is **CANDIDATE / NOT VALIDATED** until two genuinely separate end-to-end reviews of the complete eight-direction replacement are completed. The unrestricted three-eigenvalue conjecture remains open.
