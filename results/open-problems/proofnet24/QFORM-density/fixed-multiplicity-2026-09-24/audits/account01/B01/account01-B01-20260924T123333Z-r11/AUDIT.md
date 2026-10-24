# account01/B01 full fixed-multiplicity audit — run account01-B01-20260924T123333Z-r11

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `account01/B01`  
Initial source commit specified by owner: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Canonical manuscript blob audited: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Canonical source SHA-256 specified by owner: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh `master` immediately before publication was re-resolved separately; the manuscript blob remained exactly the canonical blob above.

## Verdict

**PASS on the complete 790-line mathematical argument for the 17-eigenvalue candidate.** I re-read the full source in this invocation and found no fatal mathematical defect. The exact theorem checked is:

> Independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A` with `s_17(A)>=s>0`, and arbitrary affine `b,c` imply that `X^T A X+b^T X+c` has an essentially bounded density with `||p||_infinity <=10000 K^2/s`.

This is a review of the written candidate, not a self-awarded independent-validation certificate and not a proof of the unrestricted three-eigenvalue conjecture. The theorem proves essential boundedness globally; only the integrable-Fourier no-pivot branch proves continuity directly.

## Complete source audit

Every source line is covered below. `PASS` means I independently checked the displayed statement and the hypotheses of each downstream invocation, rather than accepting the manuscript self-audit as evidence.

| Source range / item | Status | Check and reasoning | Downstream impact |
|---|---|---|---|
| 1–83: definitions, theorem, corollary, architecture, parameters | **PASS** | Singular values are zero-padded, so the hypothesis is meaningful in every dimension. Quantifiers retain arbitrary independent rough cap-`K` laws, arbitrary signature/remaining spectrum and affine terms. No moment, support, smoothness or rotated-independence hypothesis is inserted. | Main statement has the advertised scope. |
| 84–151: Fourier convention, Gaussian regularization, Plancherel/inversion, power envelope, Riesz half-potential | **PASS** | With `hat f(t)=int e^{itx}f(x)dx`, Plancherel has factor `2pi` and inversion `1/(2pi)`. The Gaussian/Tonelli derivation of the half-potential constant `(2pi)^(-1/2)` is consistent; the `3/4` envelope gives weighted integral `12 sqrt(u)`. | Fourier and negative-moment constants are normalized correctly. |
| 152–220: singular-value perturbation/rank, Schur spectral count, diagonal dominance | **PASS** | Approximation numbers justify the nonsymmetric singular-value inequalities. For invertible `A`, the complementary compression of `A^{-1}` is `S^{-1}`; positive/negative compression interlacing yields the absolute-eigenvalue count. For singular `A`, `A+epsilon I` along invertible values and continuity of ordered eigenvalue moduli gives the claimed limit. Strict row diagonal dominance needs no symmetry. | All Schur counts and nonsymmetric rank arguments are available at exactly the stated thresholds. |
| 221–282: geometric Brascamp–Lieb heat flow and product projections | **PASS** | The frame identity makes the map with columns `sqrt(c_i)u_i` a contraction, hence `partial_t F-Delta F>=0`. Trace gives `sum c_i=d`; the large-time normalization and `t downarrow0` Fatou step are valid. The projection proof uses only a deterministic change of variables; it does not assert probabilistic independence after rotation. | Projection density `<=e^{d/2}` is proved internally. |
| 283–300: integrated scalar Fourier powers | **PASS** | `|hat f|<=1` reduces to an even exponent. `|hat f|^{2m}` is integrable because it is bounded by `|hat f|^2`, so Fourier inversion at zero is not circular. The sum of `m` independent differences is a genuine original-coordinate projection and the projection lemma gives the stated constant. | No external Hausdorff–Young or extremizer input is needed. |
| 301–400: decoupling, graph-BL determinant, crossing volumes | **PASS** | Independent-copy decoupling preserves product provenance. In the regularized frame, the `c_j,d_i` weights and one-dimensional Jacobians are correct; `alpha=(2pi e)^2` cancels the entropy multiplier and the fourth root gives determinant exponent `-1/8`. Cauchy–Binet gives `Z_k`; `k=5` yields direct `L^1` Fourier inversion, while `k=3` is used only with the Riesz weight. | Both no-pivot analytic receivers close with their advertised scopes. |
| 401–500: scalar square, definite pair, hyperbolic pair | **PASS** | Scalar inverse branches give the square-root profile. Definite-pair polar coordinates give `pi M/sqrt(|det B|)`. In the indefinite pair, the `(delta,t)` Jacobian is `1/(2sqrt D)`; on each hyperbolic tail one original coordinate is monotone with derivative comparable to its magnitude, so the cap-one/mass-one bathtub estimate controls the tail. No independence after diagonalizing `B` is used. | Coordinate pivots are valid for rough product laws. |
| 501–526: quarter-power concentration and logarithmic potential | **PASS** | A large diagonal gives the square-root small-ball estimate. Otherwise the random-sign split creates an original-coordinate cross block of norm at least `||S||/4`; one singular factor of the determinant estimate gives `|t|^{-1/4}`. Gaussian smoothing and layer cake give the displayed quarter-power and logarithmic bounds. | One surviving spectral direction controls the logarithmic singularity in pivot branches. |
| 527–600: disjoint volumes, sampled interpolation, completion | **PASS** | The bordered determinant identity is exact. Singular deleted seeds only remove representations, so the `(r+1)^2` counting is correctly an inequality. For `P=A[:,T]A[S,T]^{-1}A[S,:]`, `P[S,:]=A[S,:]` and `P[:,T]=A[:,T]`. The constructed `D,E,R` satisfy `D=0` on the seed, `diag E=0`, `R[L,L]=P[L,L]`, global `rank R<=3r`, and restricted `rank R[L,L]<=r`; nonsymmetry causes no invalid eigenvalue use. | The sensitive interpolation dependency is closed. |
| 601–630: spectral-to-volume proposition | **PASS** | A bad ratio gives `||E||<=1/16`. With `m=4k-3` and `r<=k-1`, global rank loss `3r` leaves at least `r+1` large diagonal entries of `D`, all in `L`. On the resulting block, diagonal magnitude is at least `371/400` and the off-diagonal row sum is `<23/28`, so strict diagonal dominance contradicts restricted rank `<=r`. The `r=0` branch also contradicts `||A||>=1`. | This proves the full `4k-3 -> V_k` conversion for `k<=5`. |
| 631–651: random cut and no-pivot analytic consequences | **PASS** | Each ordered disjoint minor survives the fair cut with probability `4^{-k}`. The resulting constants are `12 sqrt(80e)<200` for the order-three full half-potential and `800e<2400` for the order-five density. | No-pivot `s_9` and `s_17` branches close. |
| 652–730: truncated half-potential, singular kernels, pivot estimate | **PASS** | The two kernel bounds are valid nonnegative Tonelli/layer-cake estimates. Scalar pivot uses the Schur remainder's surviving spectral direction; definite and indefinite pairs are conditioned only on original coordinates. The distinction between truncated and full half potentials is maintained. | Pivot branch gives `H<=600`. |
| 731–790: nine-direction proposition, main proof, scaling, limitations | **PASS** | Pivot/no-pivot is exhaustive. A scalar pivot from `s_17>=1` leaves at least 16 Schur directions, enough for the `s_9` half-potential theorem; definite pair is directly bounded; an indefinite pair leaves at least one direction for the logarithmic potential. Scaling `Y=KX` gives `Q=(s/K^2) Qtilde`, hence exactly `10000 K^2/s`. The paper correctly does not claim global continuity or the three-eigenvalue conjecture. | Main candidate closes with all stated quantifiers. |

No mathematical source line in `manuscript.tex` is left **UNCHECKED** in this review.

## B01 lens: quantifiers, scaling, dependency closure

The normalization is exact. If `Y=KX`, then every coordinate density of `Y` is bounded by one and

`Qtilde = Y^T(A/s)Y + (K/s)b^T Y + (K^2/s)c`,  `Q=(s/K^2)Qtilde`.

Thus `s_17(A/s)>=1` and the normalized bound rescales by exactly `K^2/s`. No dimension, signature, affine-vector, remaining-spectrum or distributional regularity parameter enters.

The specialized proof dependency chain is self-contained in the manuscript:

`Gaussian/Fourier/Riesz -> geometric BL -> product projection -> scalar Fourier powers -> decoupling/regularized determinant -> crossing-volume envelopes -> sampled interpolation/rank contradiction -> no-pivot receivers`,

and

`square/definite/hyperbolic coordinate changes -> quarter concentration/log potential -> pivot half-potential -> nine-direction full half-potential -> scalar-pivot branch of the main theorem`.

The bibliography is attribution/background only; no theorem from either cited paper is required as an unproved premise at a used constant.

## Gaps and repairs

### GAP-PACKAGE-1 — advertised supplementary files absent

At the fresh repository root I found `manuscript.tex`, `README.md`, `AUDIT.md`, `audits/`, and `improvements/`. Direct reads of all four files advertised by README/current objective returned `Not Found`:

- `proof_map.csv`
- `SOURCE_MANIFEST.json`
- `verify.py`
- `checks.json`

**Impact:** reproducibility/release-package gap only. The mathematical theorem does not depend on them because every specialized proof used above is in `manuscript.tex`. The numerical-check claims in the self-audit cannot be independently rerun from the currently published package.

**Repair:** restore the four source-pinned artifacts, or edit README/AUDIT/current release metadata so they no longer claim repository presence.

### GAP-PRESENTATION-1 — global bounded representative convention should be stated once

The theorem assumes `f_i<=K` almost everywhere, while some inverse-branch/coarea formulas later write pointwise density representatives. The projection lemma explicitly chooses everywhere-bounded versions, but the convention is not stated globally before the first pointwise formulas.

**Impact:** no theorem failure. Replacing each density by a Borel representative equal almost everywhere to it and clipped into `[0,K]` preserves the law and supplies the pointwise cap used in all deterministic formulas. Conditional conclusions are then integrated as measure-domination inequalities through Tonelli, so exceptional output levels remain harmless.

**Repair:** add one sentence near the opening conventions: “Throughout, replace every marginal density by a Borel version equal a.e. to the given density and bounded pointwise by its stated cap.”

## Threshold lowering: what is and is not proved

No complete theorem below 17 is proved in this run. Within the manuscript's current no-pivot mechanism, direct Fourier inversion requires order `k=5`, because the regularized determinant receiver gives decay exponent `k/4` and `k=4` is the nonintegrable endpoint `|t|^{-1}`. The interpolation contradiction needs, in the worst ratio chamber `r=k-1`,

`m >= 3r+(r+1)=4r+1=4k-3`,

so order five closes first at `m=17`.

At an attempted `s_16` theorem the only unclosed chamber is the terminal `r=4` saturation: global rank `<=12` forces only four large diagonal entries, and an invertible diagonally-dominant `4x4` block is compatible with restricted rank `<=4`. Smaller numerical choices of `eta` or `kappa` do not alter that exact rank saturation. A genuine `17 ->16` theorem therefore needs new structure at that terminal chamber or an endpoint analytic receiver stronger than absolute `|t|^{-1}` inversion.

This run proves a new exact-rank cross-bank Plancherel receiver in the companion improvement artifact. It strengthens the analytic toolbox but does **not** by itself lower the multiplicity threshold, because the baseline spectral argument produces aggregate crossing volume rather than a dimension-free lower bound on one exact-rank physical cross bank.

## Final status

- 17-eigenvalue candidate: **PASS** in this complete B01 review.
- Fatal mathematical defect found: **none**.
- Supplementary package: **GAP** as above.
- Rough-density representative wording: **GAP-PRESENTATION**, repair supplied above.
- Proven multiplicity reduction below 17 in this run: **none**.
- Full three-eigenvalue conjecture: **OPEN**.
- Independent-validation status: **not self-awarded**; separate complete reviews/release synthesis remain distinct from this report.
- Repository transport is not native learned-memory ingestion: `WITHOUT_VERIFIED_BRAIN`.
