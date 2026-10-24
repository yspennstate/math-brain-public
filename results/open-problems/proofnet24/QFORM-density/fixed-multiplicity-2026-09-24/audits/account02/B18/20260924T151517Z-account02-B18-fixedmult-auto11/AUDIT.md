# account02/B18 — complete fixed-multiplicity audit, auto11

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Run: `20260924T151517Z-account02-B18-fixedmult-auto11`.

## Source pin and verdict

Audited source is the owner-pinned manuscript at commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 790 lines. I reread the complete package `README.md`, `SOURCE_MANIFEST.json`, all 790 lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json` from fresh `master` before writing this review.

**Baseline mathematical verdict: PASS for the literal fixed-multiplicity theorem in the pinned manuscript.** Namely, for independent one-dimensional densities bounded by `K`, arbitrary real symmetric `A`, and arbitrary affine terms, `s_17(A)>=s>0` implies an essential density bound `||p_Q||_infinity <= 10000 K^2/s`. This is not a claim about the unrestricted three-large-eigenvalue conjecture.

No proof line below was accepted from the package self-audit without rechecking the argument. `verify.py/checks.json` were treated only as diagnostics.

## Exhaustive source-line ledger

Every source line 1--790 was read. The following intervals are exhaustive and disjoint; intervening prose, definitions, displayed equations and proof transitions are included in the stated interval rather than silently omitted.

| Lines | Content | Status | Independent check / impact |
|---|---|---|---|
| 1--46 | front matter, notation, theorem architecture, normalization | PASS | Quantifiers preserve arbitrary independent cap-`K` laws, arbitrary signature/dimension/remaining spectrum and affine terms. No hidden moments/support/iid/log-concavity. |
| 47--61 | main theorem and 33-eigenvalue corollary | PASS | Essential-density statement and scaling target are consistent. |
| 62--90 | Fourier conventions, Gaussian regularization setup | PASS | Sign/`2pi` convention is consistent with every later inversion. |
| 91--120 | Fourier identities / Plancherel / Gaussian inversion | PASS | Heat/Gaussian approximate-identity argument handles rough `L1 cap L2`; constants checked. |
| 121--130 | Fourier envelope-to-density lemma | PASS | `int min(1,L|t|^-a)` and inversion factors checked. |
| 131--160 | Riesz half-potential identity and Gaussian representation | PASS | Gamma factor and `|x|^-1/2` Fourier/Gaussian constants checked; Tonelli use is nonnegative. |
| 161--168 | singular-value counting notation and setup | PASS | `N_A(t)` counts equality (`>=t`), important at the Schur-limit endpoint. |
| 169--181 | rank perturbation / singular-value count | PASS | Valid for nonsymmetric auxiliaries; no eigenvalue interlacing shortcut is used. |
| 182--207 | Schur-complement spectral count, including singular ambient block | PASS | In the regularization proof, if `q=N_A(t)-k>0`, then `s_q(S_eps)>=t-|eps|`; `S_eps->S` in operator norm, hence `s_q(S)>=t`. Equality is counted. No fixed-`delta` patch is required. |
| 208--217 | strict diagonal dominance lemma | PASS | Standard Gershgorin/maximum-coordinate argument; strictness is used correctly. |
| 218--255 | geometric rank-one Brascamp--Lieb heat flow | PASS | Identity decomposition, derivative sign, large-time limit and rough-input truncation checked. Constant is exactly one. |
| 256--282 | product-projection density | PASS | Completes an orthogonal frame and applies BL; `f_i^(1/b_i)<=f_i` for `0<=f_i<=1`; no projected independence is asserted. Gives the claimed `e^(d/2)` cap. |
| 283--301 | scalar Fourier powers | PASS | Plancherel plus convolution-of-differences argument and `m=floor(p/2)>=p/4` give the displayed constant. |
| 302--324 | cross-form decoupling | PASS | Copies only an original product bank; pure same-bank phases are discarded only by modulus one. Exponents in second/fourth power bounds checked. |
| 325--373 | graph determinant theorem | PASS | BL frame, coordinate scalings, `c_j,d_i`, entropy bound and regularizer `alpha=(2pi e)^2` checked. Determinant exponent and constants agree. |
| 374--400 | Cauchy--Binet crossing volumes and Fourier/Riesz consequences | PASS | Coefficient identities and `k=5` density / `k=3` half-potential exponents checked. |
| 401--414 | scalar-square profile | PASS | Preimage-length estimate and measure domination hold for arbitrary scalar cap. |
| 415--434 | definite physical pair | PASS | Conditional change of variables gives `pi M/sqrt(|det B|)` with stated hypotheses. |
| 435--482 | indefinite/hyperbolic physical pair | PASS | Hyperbolic parametrization, Jacobian, central/tail split and logarithmic envelope checked; diagonalization is deterministic only. |
| 483--525 | quarter-power concentration / logarithmic potential | PASS | Diagonal and off-diagonal cases, layer-cake split and constants checked. |
| 526--544 | pivot/no-pivot definitions and ordered-minor volume | PASS | Physical pivots are literal original coordinates; no spectral-coordinate independence is introduced. |
| 545--564 | determinant-squared seed sampling | PASS | Bordering identity, weighted extension bound and multiplicities checked. |
| 565--580 | nonsymmetric sampled interpolant/completion | PASS | `P=A_{.,T} A_{S,T}^{-1} A_{S,.}` is intentionally nonsymmetric. Seed interpolation/support identities hold. Symmetrizing it would generally destroy them. |
| 581--619 | spectral-to-disjoint-volume proposition | PASS | Distinct budgets `rank R<=3r` globally and `rank R[L,L]<=r` are both used at the correct place. `D` vanishes on the seed and diagonal-dominance contradiction closes. |
| 620--630 | random coordinate cut | PASS | A disjoint `k x k` minor is crossing with probability `4^-k`; expectation identity is exact. |
| 631--645 | no-pivot bounded-density branch | PASS | Structural volume and Fourier receiver constants give the stated bound. |
| 646--674 | full versus truncated half-potential kernels | PASS | Tail outside unit distance is explicitly retained; no truncation is silently identified with the full potential. |
| 675--714 | pivot half-potential proposition | PASS | Scalar, definite and indefinite physical-pair branches exhaust the pivot alternative with stated spectral losses. |
| 715--724 | nine-direction half-potential proposition | PASS | This is a half-potential proposition inside the 17 proof, not a nine-direction density theorem by itself. |
| 725--749 | main 17-direction proof | PASS | No-pivot, scalar, definite-pair and indefinite-pair branches close; largest advertised bound is below `10000`. Scaling `Y=KX`, `A->A/s` gives `K^2/s`. |
| 750--790 | end matter, source notes, bibliography | PASS / UNCHECKED novelty | Bibliographic attributions checked below. Exhaustive priority/novelty is not certified and a search miss is not evidence of novelty. |

### Explicit adversarial checks

1. **Schur boundary:** the singular-ambient limit is valid at equality because singular values are continuous and `N_S(t)` uses `>=t`. This was the only baseline point on which fleet notes had visibly disagreed; I find no gap.
2. **Nonsymmetric interpolation cannot be symmetrized for free:** for rank-one row/column seeds, `P=uv^T` may exactly interpolate both required slices while `(P+P^T)/2` has rank two and loses the two interpolation identities. The manuscript correctly retains nonsymmetry only in the auxiliary rank argument.
3. **Absolute-spectrum principal interlacing is false in general:** `[[0,L],[L,0]]` has two singular/eigenvalue moduli `|L|`, while either scalar principal compression is zero. The proof does not use this invalid shortcut.
4. **Small matrix coefficient is not uniformly a small random error under arbitrary translations:** this blocks perturbative deletion arguments and is respected throughout the pinned proof.

## Package audit beyond the manuscript

- `README.md`: PASS as package description; it does not replace proof review.
- `SOURCE_MANIFEST.json`: PASS; commit/blob/SHA-256 match the owner objective.
- `proof_map.csv`: PASS as a navigation map; every listed theorem/proof range was cross-checked against the manuscript.
- `verify.py` and current `checks.json`: PASS as finite diagnostics only. Current recorded checks include interpolation seeds, volume sampling, Schur numerics and graph weights; none is treated as proof.
- Historical finite-test counts in `AUDIT.md` versus the current `verify.py/checks.json`: **GAP (reproducibility metadata only)**. The current suite is explicitly different and does not reproduce every historical count. Impact on theorem proof: none. Next obligation if archival reproducibility is desired: preserve the historical script/version that generated those counts.
- Compiled PDF binary/render and its recorded hash: **UNCHECKED** in this run because the binary is not part of the fetched package. This does not affect the TeX-source proof audit.
- Exhaustive novelty/priority: **UNCHECKED**. The audit verifies cited antecedents and hypotheses but does not infer novelty from search failure.

## Primary-source prior-art verification

### Bennett--Carbery--Christ--Tao

Primary source: arXiv `math/0505065` / the published BCCT paper. The source explicitly defines geometric Brascamp--Lieb data and states Proposition 2.8 that the geometric Brascamp--Lieb constant and Gaussian constant are both `1`; its proof section is built on heat/transport monotonicity. This matches the manuscript's attribution. The manuscript does not import a hidden BCCT numerical constant: it proves the rank-one geometric case it needs, including the rough-input limiting step.

### Rudelson--Vershynin

Primary source: arXiv `1402.4492`. Theorem 1.2 states: independent real variables, each density bounded by `K` a.e., normalized coefficients `sum a_j^2=1`, and density of the linear combination bounded by the optimal `sqrt(2) K`. No moment, support, iid, centering, symmetry or log-concavity hypothesis is present. Their higher-dimensional projection theorem has an absolute-constant `(CK)^d` form. The pinned manuscript's sharper explicit `e^(d/2)` projection bound is proved internally and is not falsely attributed to RV.

No external theorem with stronger hidden hypotheses was found to be used as a black box in the pinned proof.

## Threshold reduction status after this audit

The pinned source itself remains a 17-eigenvalue manuscript. A separate account02/B18 replacement proof from the preceding B18 run gives a nine-eigenvalue theorem with explicit constant `6010 K^2/s`. In this run I specifically re-audited the point challenged by a later B06 note: whether the grouped product-Fourier receiver illegally converts an `L1` Fourier factor into an `L2` one. The accompanying improvement artifact gives a complete regularized proof that it does not. The hub is paid by output-space Cauchy--Schwarz/Plancherel **before** the light-bank copy, and the remaining complex pushforward is controlled in `L2`; no `L1` Fourier norm of a cap-one density appears.

Thus my B18 status is:

- pinned `s_17` theorem: **PASS**;
- B18 replacement `s_9` theorem with constant `6010 K^2/s`: **PASS after the mixed-norm objection is explicitly resolved**;
- multiplicity eight: **OPEN / not certified in this run**. Recent supporting notes explicitly describe the remaining `s_8` endpoint as open, even though several leverage subchambers are now paid.
- unrestricted three-large-eigenvalue QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.

I do not adopt the newer `400` or other smaller nine-eigenvalue constants here: they are separate candidate manuscripts/retunings and were not independently audited line-by-line in this B18 invocation. This is a constant-level `UNCHECKED`, not a challenge to their claims.
