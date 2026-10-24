# account01/B11 auto11 — full fixed-multiplicity manuscript audit

Run: `20260924T144041Z-account01-B11-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256 from `SOURCE_MANIFEST.json`: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Current manuscript read from `master`: same blob, hence byte-identical to the pinned baseline.

## Verdict

**PASS** for the mathematical statement actually written in the 790-line baseline manuscript:

> If the independent real coordinate densities are bounded by `K`, `A=A^T` is arbitrary, `b,c` are arbitrary, and `s_17(A)>=s>0`, then `X^TAX+b^TX+c` has an essentially bounded density with `||p||_infinity <=10000 K^2/s`.

I found no fatal mathematical defect and no theorem-changing gap. I did not audit bibliographic priority beyond the two cited classical antecedents; that is **UNCHECKED** and is not a proof dependency. I also did not execute the repository's Python checker in this connector-only run; I read its complete source and the committed PASS output. The finite suite is therefore **PASS by code inspection / recorded output, independent rerun UNCHECKED**. It is not a proof certificate.

The current package is complete: `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` are all present and were read in this run. `checks.json` records PASS on 534 exact interpolation seeds, 18 exact volume-sampling cases, 9 strict-sampling cases, 240 numerical Schur threshold cases and 30 numerical graph-weight cases.

## Fatal defects first

None found.

## Full source ledger

Every source line 1--790 was read. The following labels apply to the mathematical source, not to publication priority.

| Source range | Verdict | Reason |
|---|---|---|
| 1--46 | PASS | Preamble/abstract accurately state the 17-direction theorem and its scope; no hidden smoothness, support, moment, sign or rotated-independence assumption. |
| 47--90 | PASS | Main theorem, normalization and architecture have correct quantifiers and scaling target. The distinction between essential boundedness and continuity is explicit. |
| 91--160 | PASS | Fourier convention, Gaussian regularization, Plancherel, inversion and the half-Riesz representation have the correct constants. The order-three envelope is used with the `|t|^{-1/2}` Riesz weight, not falsely as an `L^1` Fourier envelope. |
| 161--217 | PASS | Singular-value perturbation/rank inequalities, Schur spectral count and strict diagonal dominance are correct, including singular ambient matrices and the strict/non-strict threshold conversion detailed below. |
| 218--282 | PASS | Heat-flow proof of geometric rank-one Brascamp--Lieb and product-projection density bound are valid. Orthogonal transformations occur only in deterministic integration; random coordinates are never rotated and declared independent. |
| 283--301 | PASS | Integrated scalar Fourier powers follow from Plancherel plus the one-dimensional product-projection bound. Difference densities are indeed capped by one. |
| 302--373 | PASS | Original-coordinate decoupling, two-copy difference law, regularized geometric frame and determinant exponent `-1/8` are consistent. The `c_j,d_i` trace identity and all scaling factors match. |
| 374--400 | PASS | Cauchy--Binet crossing-volume expansion and order-five/order-three envelopes have the stated powers and constants. |
| 401--434 | PASS | Scalar-square inverse branches and definite two-coordinate coarea bound are measure-domination statements valid for rough laws; no conditional independence is invented. |
| 435--482 | PASS | Hyperbolic-pair parametrization, Jacobian `1/(2 sqrt D)`, tail monotonicity and logarithmic envelope are correct. Exceptional critical levels are harmless under the nonnegative-test-function/Tonelli formulation. |
| 483--525 | PASS | Quarter-power concentration correctly splits diagonal/off-diagonal cases and invokes the determinant theorem only on literal coordinate banks. The logarithmic-potential layer-cake computation is valid. |
| 526--564 | PASS | No-pivot entry bound, ordered disjoint-minor convention and volume-sampled interpolation are correct. Singular seeds yield an inequality rather than a false equality. |
| 565--619 | PASS | Completion `A=D+R+E`, `rank R<=3r`, sharper `rank R[L,L]<=r`, zero diagonal of `E`, and diagonal dominance close exactly. The rational slack is `371/400-23/28=297/2800>0`. |
| 620--645 | PASS | Fair original-coordinate cut and no-pivot analytic consequences are correct at orders 3 and 5. |
| 646--674 | PASS | The two singular-kernel estimates used by the baseline are valid; they are deliberately coarse but sufficient. |
| 675--724 | PASS | Pivot truncated-half-potential and nine-direction half-potential propositions are valid. The scalar, definite and indefinite pair alternatives exhaust pivots. |
| 725--749 | PASS | Final theorem cases are exhaustive: no pivot `<2400`, scalar pivot `6010`, definite pair `<40`, indefinite pair `<251`; general `K,s` scaling is correct. |
| 750--790 | PASS / UNCHECKED bibliographic priority | Threshold-accounting/limitations accurately state what the proof does not prove. Bibliographic priority beyond the cited attribution was not exhaustively audited. |

No mathematical source range remains UNCHECKED.

## Schur-complement audit: the delicate singular case

The literal moving-threshold paragraph in `lem:schur` is mathematically sufficient. This resolves a current peer-label disagreement without modifying the pinned source.

Write

`A=[[B,C],[C^T,D]]`, `det B!=0`, `S=D-C^T B^{-1} C`.

For invertible `A`, `S^{-1}` is the complementary principal compression of `A^{-1}`. Cauchy interlacing separately for positive and negative thresholds gives

`#{|lambda(S^{-1})|>1/t} <= #{|lambda(A^{-1})|>1/t}`.

Because inversion changes the strict condition `>1/t` exactly into the original condition `|lambda|<t`, the two counts are

`(n-k)-N_S(t)` and `n-N_A(t)` respectively. Hence `N_S(t)>=N_A(t)-k`.

For singular `A`, take a sequence `epsilon->0` for which `A_epsilon=A+epsilon I` is invertible and `B+epsilon I` remains invertible. Put `tau_epsilon=t-|epsilon|>0`. Weyl's bound gives

`N_{A_epsilon}(tau_epsilon)>=N_A(t)`.

Applying the invertible result at the moving threshold `tau_epsilon` gives

`N_{S_epsilon}(tau_epsilon)>=N_A(t)-k`,

where

`S_epsilon=D+epsilon I-C^T(B+epsilon I)^{-1}C -> S`.

If `m=N_A(t)-k>0`, the preceding count is exactly

`s_m(S_epsilon)>=t-|epsilon|`.

Continuity of ordered singular/eigenvalue moduli therefore gives `s_m(S)>=t`, i.e.

`N_S(t)>=N_A(t)-k`.

If `m<=0` the claim is trivial. Thus the non-strict endpoint `>=t` survives the limit. A fixed-`delta` proof is an equally valid rewrite, but is not required to repair the mathematics.

## Product-projection wording check

After factors with `b_i=0` are dropped, the proof bounds

`sum_{b_i>0}[-b_i log b_i] <= sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`.

Thus the displayed `d/2` conclusion is correct. One can include the omitted zero-`b_i` terms using the convention `-b log b=0` at zero, or use the inequality above; no constant changes.

## Support package audit

- `README.md`: **PASS** as a current scope/delivery description.
- `DELIVERY_STATUS.md`: **PASS** as a delivery/status record; worker-count statements are operational evidence, not proof evidence.
- historical `AUDIT.md`: **PASS as historical self-report**, not independent validation.
- `proof_map.csv`: **PASS**; theorem/proof line ranges agree with the source structure read here.
- `SOURCE_MANIFEST.json`: **PASS**; it pins the source blob/hash/size and correctly separates the compiled conversation PDF from committed source.
- `verify.py`: **PASS by code inspection**. It checks the pinned SHA before diagnostics, exact interpolation/rank/volume identities and finite floating Schur/frame cases. It does not claim universality.
- `checks.json`: **PASS as recorded output**, matching the new suite described by `verify.py`. **Independent execution in this run: UNCHECKED**.

## Downstream consequence

The 17-direction baseline theorem is mathematically usable as written. A separate improvement artifact in this run gives a complete threshold-nine replacement and sharpens the current nine-direction constant to `<2547 K^2/s`; multiplicity eight remains open. The new constant is a B11 candidate until a genuinely separate end-to-end review checks it.

Model: GPT-5.6 Sol. Configured reasoning effort/provider reasoning counters: `UNKNOWN / NOT_EXPOSED`.