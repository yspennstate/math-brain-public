# fleet01/B17 full end-to-end audit — fixed multiplicity baseline

Run: `20260924T143530Z-fleet01-B17-fixedmult-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob actually read from current `master`: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Owner/source-manifest SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Current manuscript length: 790 lines, 47,883 bytes. The blob on current `master` is the same pinned source blob; concurrent audit/improvement commits do not alter the baseline manuscript.

## Verdict

**PASS** for the mathematical argument in the pinned 17-eigenvalue manuscript. I found no fatal mathematical defect in the definitions, quantifiers, equations, or proofs after an end-to-end reconstruction. This is one worker audit, not a formal certificate and not a release decision. The bibliography/prior-art attribution is **UNCHECKED** in this B17 pass because it is not a proof dependency; B18 owns primary-source priority verification. The historical counts in `AUDIT.md` differ from the later `verify.py/checks.json` suite, but README/DELIVERY_STATUS/SOURCE_MANIFEST explicitly disclose that they are different suites, so this is not a mathematical inconsistency.

The full three-eigenvalue conjecture is not proved by the baseline. The baseline conclusion is an essentially bounded density; continuity is asserted only in the no-pivot Fourier branch and is correctly kept separate elsewhere.

## Exact manuscript coverage

The table records every mathematical source range. `PASS` means I reconstructed the stated implication and checked every invocation against its hypotheses. `UNCHECKED` is retained only for literature attribution, which is not used logically.

| Lines | Item | Verdict | Audit reason |
|---|---|---|---|
| 1–46 | preamble, metadata, abstract | PASS | Metadata is consistent with the source; abstract accurately states the 17-direction theorem and the nonsymmetric interpolation mechanism. |
| 47–57 | `thm:main` | PASS | Quantifiers preserve arbitrary independent cap-`K` laws, arbitrary symmetric `A`, affine `b,c`, and remaining spectrum. Scaling is checked in lines 726–749. |
| 59–61 | `cor:33` | PASS | Follows from monotonicity `s_17(A)>=s_33(A)`. |
| 62–90 | architecture, parameters, conventions | PASS | `eta=1/100`, `kappa=1/80^2`; threshold accounting `9=4*3-3`, `17=4*5-3` matches the later proposition. No post-rotation independence is invoked. |
| 91–106 | Fourier identities statements | PASS | Fourier normalization is consistent throughout. Gaussian inversion coefficient is correct. |
| 107–120 | Fourier identities proof | PASS | Gaussian regularization, approximate identity, monotone/dominated convergence, and weak identification of the law are valid. |
| 122–130 | power envelope | PASS | Integral of `min(1,(a/|t|)^p)` is `2ap/(p-1)`; Fourier inversion gives the displayed coefficient. |
| 132–143 | negative-half-moment statements | PASS | Riesz/Gaussian representation has the correct gamma power and Fourier normalization. |
| 144–160 | negative-half-moment proof | PASS | Two Tonelli steps are on nonnegative majorants; substitution gives `sqrt(2) Gamma(1/4)|t|^-1/2`; the power-envelope integral is `12 sqrt(u)`. |
| 161–168 | norm/spectral-count conventions | PASS | Definitions match subsequent singular-value uses. |
| 169–181 | perturbation and rank | PASS | SVD approximation formula proves both nonsymmetric singular-value perturbation and rank shift exactly as used later. |
| 183–207 | Schur spectral count | PASS | For invertible `A`, `S^-1` is the complementary principal block of `A^-1`; positive/negative interlacing separately controls the absolute-value count. The `A+epsilon I` singular approximation preserves the pivot and passes to the threshold by eigenvalue continuity. |
| 209–217 | strict diagonal dominance | PASS | Standard max-coordinate proof works without symmetry. |
| 221–255 | geometric rank-one BL | PASS | Heat-flow sign follows from the Parseval frame; Gaussian tails justify differentiation/integration by parts; large-time limit and small-time Fatou/monotone approximation are valid. |
| 258–282 | product projections | PASS | Orthogonal completion, weights `b_i`, geometric BL scaling, and `-b log b<=1-b` give `exp(d/2)`. No rotated independence is asserted. |
| 284–301 | scalar Fourier powers | PASS | Plancherel plus the projection density of the `m` signed differences yields the stated `2 pi sqrt(2e)/sqrt(p)` bound for every `p>=2`; the difference density cap `<=1` is correct. |
| 302–309 | physical cross-form setup | PASS | Same-bank and affine terms are retained in `F,G`; only original independent coordinate banks are separated. |
| 310–324 | decoupling | PASS | Cauchy–Schwarz duplicates only the `J` bank; integration of original `I` coordinates gives the product of their Fourier transforms. Jensen gives the fourth-power form. |
| 326–373 | regularized crossing determinant | PASS | Frame weights `c_j,d_i`, trace identity, BL Jacobian, scalar Fourier powers and `alpha=(2pi e)^2` cancellation were rederived; fourth root gives exponent `-1/8`. No symmetry of the cross block is needed. |
| 374–385 | crossing volumes / Cauchy–Binet | PASS | `Z_k` is the elementary symmetric polynomial in squared singular values; ordered physical minors agree with Cauchy–Binet. |
| 386–400 | volume Fourier envelopes | PASS | Retaining the order-`k` determinant term gives exponent `k/4`; `k=5` is `L1`, while `k=3` is only sufficient after the Riesz weight. Constants agree. |
| 404–414 | scalar square profile | PASS | Two inverse branches and the interval-preimage bound are correct for rough cap-one densities. |
| 415–422 | conditional scalar profile | PASS | Completion of the square produces the scalar Schur complement; the inequality is measure domination via conditional test functions/Tonelli, not an independence statement. |
| 423–434 | definite pair | PASS | Deterministic completion/orthogonal diagonalization and polar Jacobian give `pi M/sqrt(|det B|)`. |
| 437–482 | hyperbolic pair | PASS | Hyperbolic parametrization has Jacobian `1/(2sqrt D)`. The two tails are controlled by one original coordinate each; the middle length and AM–GM step `Lambda>=2/sqrt D` give the stated logarithmic envelope. Exceptional critical level is handled in measure form. |
| 485–525 | quarter-power concentration | PASS | Random-sign split creates a literal physical cross block with norm at least `L/4`; determinant Fourier estimate plus Gaussian smoothing gives the `1/4` small-ball exponent. Layer cake yields `L0=4+4 log16`. |
| 528–535 | pivot / `V_r` definition | PASS | Ordered disjoint row/column pairs and empty-sum convention are consistent with sampling/cut identities. |
| 536–544 | no-pivot entry bound | PASS | Absence of scalar and principal-pair pivots gives `|a_ii|<eta` and `|a_ij|^2<eta^2+eta<1/49`, hence `|a_ij|<1/7`. |
| 545–564 | volume-sampled interpolation | PASS | Bordered determinant identity is exact after squaring sorted-index signs. Singular seeds correctly yield an inequality. Expected off-diagonal residual is bounded by `(r+1)^2 V_{r+1}/V_r`. `P` may be nonsymmetric and interpolates rows `S` / columns `T`. |
| 566–580 | diagonal plus interpolation | PASS | `E` has zero diagonal, `D` vanishes on `S union T`, `R_LL=P_LL`. Support of `R-P` lies in rows `T` or columns `S`, giving global rank `<=3r`; restricted rank is `<=r`. No symmetry is falsely imposed. |
| 582–619 | no-pivot spectral-to-volume proposition | PASS | Telescoping selects a small ratio. `r=0` contradicts `||A||>=1`. For `1<=r<=4`, `||E||<=1/16`; global rank forces at least `r+1` large diagonal entries in `L`, while zero diagonal of `E` plus the no-pivot entry bound makes the `(r+1)` restricted block of `R` strictly diagonally dominant. Exact slack is `371/400-23/28=297/2800>0`. This contradicts `rank R_LL<=r`. Threshold accounting `4k-3` is correct. |
| 621–630 | random coordinate cut | PASS | Each ordered disjoint `k,k` minor crosses a fair cut with probability `4^-k`; expectation and existence follow. |
| 632–645 | no-pivot analytic consequences | PASS | `k=3` gives full half-potential `<200`; `k=5` gives density `<=800e<2400`. Constants follow from `Z_k^-1/(2k)<=160`. |
| 646–653 | truncated half-potential definition | PASS | Atom convention and unit truncation are used consistently. |
| 654–674 | two singular kernels | PASS | Near/far split for `J(d)` and layer-cake/rearrangement for the log kernel give the stated safe constants. |
| 676–714 | pivot controls truncated half potentials | PASS | Scalar pivot uses one Schur spectral direction plus the quarter-power logarithmic bound; definite pair uses area; indefinite pair uses the hyperbolic envelope and `sup D^-1/2 log_+ D=2/e`. Conditional critical values are averaged legally by Tonelli. |
| 716–724 | nine-eigenvalue half-potential | PASS | Pivot branch invokes the preceding proposition; no-pivot invokes the full order-three Riesz bound; the exterior `|x|>1` tail contributes at most one. |
| 726–749 | main theorem / scaling | PASS | No-pivot uses order five. Scalar pivot leaves at least 16 directions and hence the nine-direction half-potential. Pair counts are sufficient. For general `K,s`, `Y=KX` has cap one and `Q=(s/K^2) Qtilde`, giving `K^2/s`. |
| 750–780 | threshold accounting / limitations | PASS | Correctly identifies order five as the baseline density bottleneck, distinguishes order-three half-potential use, and does not claim continuity in pivot branches or closure at multiplicity three. |
| 781–790 | acknowledgments / bibliography | UNCHECKED | Bibliographic attribution was read but not independently priority-verified in this B17 mathematical pass. Neither citation is a logical dependency because the needed analytic statements are reproved in the manuscript. |

**Unchecked mathematical proof lines: none.**  
**Fatal defects found: none.**

## Support-package audit

- `README.md`: **PASS**. It accurately labels 17 as a candidate with self-audit and explains that independent review/release is separate.
- `DELIVERY_STATUS.md`: **PASS for provenance/status claims actually inspectable here**. It explicitly distinguishes source delivery, task activity and proof validation.
- `AUDIT.md`: **PASS as historical self-report, not as independent evidence**. Its older finite-check counts are not the same suite as the current checker; that distinction is explicitly disclosed.
- `proof_map.csv`: **PASS**. Statement/proof ranges match the 790-line source for all labeled lemmas/theorems.
- `SOURCE_MANIFEST.json`: **PASS**. It pins baseline commit, blob, SHA-256, size/line count and separately labels the review limitation.
- `verify.py`: **PASS as a finite diagnostic only**. It pins the manuscript SHA-256, exactly checks interpolation support/ranks/bordered determinants and diagonal-dominance slack, and numerically probes Schur/graph-weight identities. It does not purport to prove the theorem.
- `checks.json`: **PASS as the recorded execution result**: 534 exact interpolation seeds, 18 exact volume-sampling cases, 240 numerical Schur threshold cases, 30 graph-weight cases, with exact slack `297/2800`. It correctly states its limitations.

## Threshold accounting result of this audit

The baseline spends 17 **only** in the no-pivot density branch: order-five crossing volume is needed because the manuscript determinant envelope has exponent `5/4>1`. Pivot branches are cheaper. In particular, the scalar-pivot branch needs a negative-half-potential theorem for its Schur complement, not order-five `L1` inversion.

The global interpolation rank `3r` cannot simply be replaced by `2r`: even for `r=1`, the completion permits a generic rank-three correction. The restricted `L x L` rank `r` is the genuinely useful sharper fact. Thus a correct threshold improvement must either improve the analytic receiver at order three/two or add new terminal structure; it cannot be obtained by silently treating the nonsymmetric interpolation as rank `2r`.

A complete multiplicity-nine replacement proof was developed in this run and is saved separately under the matching `improvements/fleet01/B17/...` directory. It uses a rough-law-safe grouped physical-product Fourier compiler, an order-three density receiver, and an order-two half-potential receiver. I do **not** mark that new theorem independently validated here; two genuinely separate full reviews of the replacement proof are still required by the owner gate.
