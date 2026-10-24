# account02/B04 independent fixed-multiplicity audit r25

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`.

- source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`
- source SHA-256 pinned by the owner/package: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- git blob read from the pinned source: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- source length: 47,883 bytes / 790 lines
- fresh package/master head after the final control refresh in this run: `f31e60e539306b42bf9dbb9085311c518bd04156`

## Verdict

**Baseline seventeen-eigenvalue manuscript: PASS in this independent B04 review.** I reread the complete 790-line source in this invocation and reconstructed the analytic and algebraic dependency chain. I found no FALSE item and no unresolved mathematical GAP in

` s_17(A) >= s > 0  =>  ||p_(X^T A X+b^T X+c)||_infinity <= 10000 K^2/s.`

All dimensions, signatures, arbitrary affine terms, arbitrary remaining spectrum and arbitrary independent rough coordinate laws with density cap `K` are retained. The unrestricted three-eigenvalue conjecture is not solved here.

The package/reproducibility GAP recorded in my earlier B04 review is now **RESOLVED**: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are present on fresh master. I read all four. I also independently re-executed the exact/numerical checker logic under the package-reported Python/numpy/sympy versions and reproduced all currently advertised counts exactly: 534 interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases, diagonal-dominance slack `297/2800`, 240 Schur-threshold diagnostics and 30 graph-weight diagnostics. This is finite reproducibility evidence, not mathematical proof.

No mathematical section of the pinned 790-line baseline is left UNCHECKED in this review. The compiled PDF itself remains a conversation-delivered binary rather than a committed file, so I did not independently re-render that binary in this run; this has no effect on the source-proof verdict.

## End-to-end source audit

| Source lines | Statement / dependency | Status | Independent reasoning / impact / next obligation |
|---|---|---|---|
| 1--46 | Preamble, definitions, conventions | PASS | The singular-value convention is compatible with symmetric `A`; density means Lebesgue density and the norm is essential supremum. No hidden regularity assumption enters the theorem. |
| 47--74 | Main theorem, corollary, normalized parameters and architecture | PASS | Quantifiers retain arbitrary dimension, sign, affine terms and rough independent laws. The normalized proof and final scaling are dimensionally correct. The architecture correctly distinguishes density from half-potential conclusions. |
| 75--120 | Fourier normalization, Gaussian regularization, Plancherel and inversion | PASS | `g_epsilon` has transform `e^{-epsilon t^2}` in the stated convention. The `L^2` approximate-identity passage is legitimate. If `phi` is integrable, Gaussian smoothing converges uniformly to the continuous inverse Fourier density. No circular density assumption is used. |
| 122--160 | Power envelope and Riesz negative-half-moment formula | PASS | The envelope integrates to `2ap/(p-1)`. The gamma/Gaussian representation is nonnegative, so both Tonelli uses are legal; the constant `1/sqrt(2 pi)` and the `12 sqrt(u)` weighted integral are correct. |
| 161--218 | Singular-value perturbation, Schur count, strict diagonal dominance | PASS | Approximation-number proofs work for nonsymmetric matrices. The inverse-compression proof of the Schur spectral count is valid, including the singular limiting argument. Strict row diagonal dominance does not require symmetry. |
| 219--255 | Geometric Brascamp--Lieb heat flow | PASS | Rebuilt below in detail. The heat-flow differential identity, frame contraction, integration by parts, `t -> infinity` dominated limit, `t downarrow 0` Fatou step and monotone truncation are all justified. No nonintegrable boundary term or hidden uniform-integrability step remains. |
| 257--301 | Product-projection density and integrated scalar Fourier powers | PASS | All orthogonal maps are deterministic integral changes of variables; rotated random coordinates are never declared independent. The geometric BL frame is exact. The cap-one density powers and the `m=floor(p/2)` argument yield the stated scalar Fourier constant. |
| 310--324 | Two/fourth-power decoupling | PASS | The copied bank consists of original independent coordinates. Fubini is harmless because pre-estimate integrands have modulus one. Difference coordinates remain independent and have cap-one densities. Jensen is applied only to a nonnegative right-hand side. |
| 326--400 | Regularized crossing determinant and volume envelopes | PASS | The graph vectors form an exact frame. The `d_i` powers cancel, `alpha=(2 pi e)^2` cancels the entropy factor, and fourth-root decoupling yields determinant exponent `-1/8`. `k=5` gives an integrable density envelope; `k=3` is used only with the Riesz weight and is not misreported as direct density inversion. |
| 404--482 | Scalar square, definite pair, hyperbolic pair | PASS | Conditional changes of variables remain in original coordinates. The square profile is measure domination, not an independence assertion. The definite pair uses only a deterministic rotation of the integral. Hyperbolic coordinates have Jacobian `1/(2 sqrt D)` and the tail estimate uses a single original-coordinate density cap; the critical level is handled in test-function/Tonelli form. |
| 485--525 | Quarter-power concentration and logarithmic potential | PASS | The random-sign physical cut produces a literal crossing with norm at least `L/4`; retaining the top singular factor in the determinant theorem gives `|t|^{-1/4}`. Gaussian smoothing proves concentration before layer cake; non-atomicity is established before the logarithmic expectation is invoked. |
| 528--580 | Pivot-volume definition, sampled interpolation, completion | PASS | Ordered disjoint-minor convention is consistent. Singular deleted seeds may have nonsingular extensions, so the sampling count is correctly an inequality. `P` may be nonsymmetric. The support of `R-P`, global `rank R<=3r`, restricted `rank R[L,L]<=r`, zero diagonal of `E`, and `D=0` on the seed are all used exactly as proved. |
| 582--645 | Spectral-to-volume proposition, random cut, no-pivot consequences | PASS | In the small-volume branch `||E||_F<=1/16`; rank perturbation forces at least `r+1` large entries of `D` in `L`. Row diagonal dominance then contradicts `rank R[L,L]<=r`. The random-cut probability is exactly `4^{-k}`. Constants for orders three/five check. |
| 654--674 | Singular kernels | PASS | The near/far split of `J(d)` is integrable and the logarithmic kernel is controlled by interval superlevel overlap plus Tonelli. A sharper exact scalar-kernel identity is recorded separately in this run's improvement note, but the manuscript's looser constants are valid. |
| 676--714 | Pivot truncated half potential | PASS | Scalar pivot uses one surviving Schur eigenvalue only after it is proved. Definite/indefinite pair branches retain the exact determinant hypothesis and average conditional measure bounds. Full and truncated half potentials are not conflated. |
| 716--724 | Nine-eigenvalue full half potential | PASS | With a pivot, the preceding truncated estimate applies; without a pivot, order-three volume gives a full half potential. The tail outside unit distance costs at most one, giving `601`. |
| 726--749 | Main theorem and scaling | PASS | No-pivot `s_17` gives density directly. A scalar pivot removes at most one spectral direction, leaving at least sixteen and hence the proved nine-direction half-potential hypothesis. A pair pivot removes at most two; the indefinite branch needs only one surviving direction. Scaling with `Y=KX`, `A/s`, and output factor `s/K^2` gives exactly `K^2/s`. |
| 751--790 | Threshold accounting, limitations, bibliography | PASS | The paper correctly states that the order-three baseline envelope itself is not density-integrable and explicitly does not claim the three-eigenvalue theorem or global continuity. The dependency table matches the proof. |

## B04 primary lens: heat-flow proof rebuilt

For bounded compactly supported `h_i` of positive mass define

`f_i(t,s)=g_t*h_i(s)`, `v_i=partial_s log f_i`, and

`F(t,x)=prod_i f_i(t,u_i.x)^{c_i}`.

The chosen heat kernel solves `partial_t f_i=partial_s^2 f_i`. Direct logarithmic differentiation gives

`(partial_t-Delta_x)F = F [sum_i c_i v_i^2 - |sum_i c_i u_i v_i|^2]`.

Let `W` have columns `sqrt(c_i)u_i`. The frame identity is `WW^T=I`, hence `||W||=1`; applying it to `(sqrt(c_i)v_i)_i` makes the bracket nonnegative.

### Positive-time differentiation and integration by parts

Fix `0<tau<=t<=T`. Heat convolution makes every factor smooth and strictly positive. If every original support is contained in `[-R,R]`, then for a suitable constant depending only on `tau,T,R` and the bounded input,

`f_i(t,s) <= C exp(-c s^2)`.

Moreover

`partial_s log f_i(t,s)`

is the heat-kernel weighted mean of `-(s-y)/(2t)`, so

`|partial_s log f_i(t,s)| <= (|s|+R)/(2 tau)`.

Higher derivatives occurring after differentiating the displayed expression are bounded by a polynomial in `|s|` times the same Gaussian scale. The frame relation gives

`sum_i c_i (u_i.x)^2 = |x|^2`.

Therefore `F`, its first spatial derivatives and the Laplacian terms admit integrable Gaussian-times-polynomial majorants on `[tau,T]`. Boundary integrals over expanding balls tend to zero. Differentiation under the integral and integration by parts are consequently legitimate, proving that `int F(t,x) dx` is nondecreasing.

### Large-time endpoint

Taking traces in the frame identity gives `sum_i c_i=d`. With `M_i=int h_i` and `x=sqrt(t) z`, for fixed `z`,

`sqrt(t) f_i(t,sqrt(t)u_i.z) -> (4pi)^(-1/2) M_i exp(-(u_i.z)^2/4)`.

For `t>=1`, compact support plus `(s-a)^2 >= s^2/2-a^2` gives a uniform factorwise Gaussian bound, and the frame identity turns their product into `C exp(-|z|^2/8)`. This is integrable in `R^d`, so dominated convergence gives

`lim_(t->infinity) int F(t,x) dx = prod_i M_i^{c_i}`.

No exchange here requires a moment assumption on the original probability laws; this theorem is first proved only for compactly supported `h_i`.

### Small-time endpoint

For each one-dimensional `h_i`, the non-Lebesgue-point set is null. Because `u_i` is a nonzero unit vector, the inverse image of such a null set under `x -> u_i.x` is null: rotate `u_i` to a coordinate vector and apply Fubini. There are finitely many factors, so almost every `x` is simultaneously a Lebesgue point for all of them. Thus

`F(t,x) -> prod_i h_i(u_i.x)^{c_i}`

for almost every `x`. Since `F>=0`, Fatou alone is sufficient:

`int prod_i h_i(u_i.x)^{c_i} dx <= liminf_(t downarrow 0) int F(t,x) dx`.

No dominated-convergence or uniform-integrability assertion is needed at this endpoint.

### Rough-law closure

Zero-mass factors vanish almost everywhere. For arbitrary nonnegative integrable `h_i`, the truncations

`h_i^(m)=min(h_i,m) 1_{[-m,m]}`

increase pointwise to `h_i`. Apply the bounded compact-support result and monotone convergence on both sides. This closes the geometric inequality for the exact rough scope used later.

**B04 verdict:** no unjustified limit exchange, boundary term, nonintegrable endpoint majorant, or post-rotation independence is present in lines 219--255.

## New package files: independent reproducibility check

Fresh master now contains all support files named by the objective. I read:

- `SOURCE_MANIFEST.json`: source commit/blob/hash/bytes/lines and hashes of the support files;
- `proof_map.csv`: label-to-statement/proof line map;
- `verify.py`: source hash check, exact interpolation/rank/bordered-minor assertions, exact aggregate sampling inequality and floating Schur/graph diagnostics;
- `checks.json`: the actually recorded result.

I separately executed the checker logic under the versions recorded by the manifest (`Python 3.13.5`, `numpy 2.3.5`, `sympy 1.14.0`). It reproduces:

- exact interpolation seeds: `534`;
- exact volume-sampling cases: `18`;
- strict sampling cases: `9`;
- exact diagonal-dominance slack: `297/2800`;
- floating Schur-threshold cases: `240`;
- floating graph-weight cases: `30`.

The historical counts retained in the author `AUDIT.md` are from a different suite; the README/manifest/checks explicitly say that the new suite does not retroactively reproduce them. I therefore record no contradiction. Finite checks remain diagnostics only.

## Lower-threshold status after securing the baseline

The repository contains the complete account03/B04 replacement argument lowering the threshold from seventeen to nine while retaining the original quantifiers. Its new ingredients are a grouped physical product-Fourier compiler, a marginal-free third-crossing-volume density receiver and a marginal-free second-crossing-volume half-potential receiver. In normalized form it proves the no-pivot `s_9` branch from order-three crossing volume and pays the scalar-pivot Schur remainder from either a pivot or order-two volume.

I had independently reconstructed this candidate in the preceding B04 audit and supplied an explicit smoothing/Fourier-Fatou closure for the one compressed rough-pushforward passage. This invocation reread the candidate against the now-complete package and found no new defect.

Fresh repository evidence now also contains at least two other reports explicitly labelled independent PASS reconstructions of the nine-eigenvalue candidate: account01/B16 (`54ec2a651d854563f8db0d92c4c3426f76551786`) and account03/B08 (`c02a08f19d010e508578695a5906744fdbcfcd70`). The latter independently reconstructs the threshold reduction through earlier full-form physical E3/E2 receivers and records a sharpened valid constant `<3110 K^2/s` under `s_9(A)>=s`. **I do not self-award release/independent-validation status here; determining that those reports meet the owner's separation/reconciliation gate belongs to the release synthesis.**

I found no valid counterexample to the nine-direction statement.

## Why this mechanism currently stops at nine

The spectral-to-volume proof for order three samples seed order `r` up to `2`. At the worst seed `r=2`, completion has

`rank R <= 6` globally and `rank R[L,L] <=2`.

If `m` large singular values are available, rank perturbation forces `m-6` large diagonal entries of `D`. To contradict the restricted rank using strict diagonal dominance requires at least `r+1=3` such entries. Thus this exact bookkeeping needs

`m-6 >=3`, i.e. `m>=9`.

At `m=8`, it forces only two large diagonal entries; a rank-two restricted matrix can support a two-by-two diagonally dominant block, so the manuscript's contradiction simply does not fire. This is an exact barrier of the present interpolation/diagonal-dominance mechanism, not a counterexample to an eight-eigenvalue theorem. A proof below nine must add genuinely new structural information or a different analytic/geometry exit; it cannot be obtained by relabelling the current rank count.

## Supporting constant refinement (does not lower the multiplicity)

For the scalar-pivot kernel one can sharpen the manuscript estimate exactly. For `d>0`,

`J(d)=int_{-1}^1 |x|^(-1/2)|x-d|^(-1/2) dx`

obeys

- for `0<d<=1`, `J(d)=2 asinh(d^(-1/2))+pi+2 acosh(d^(-1/2))`;
- for `d>=1`, `J(d)=2 asinh(d^(-1/2))+2 asin(d^(-1/2))`.

Hence

`J(d) <= (pi+4 log 2)+2 log_+(1/d)`.

The manuscript's Gaussian-smoothed quarter-power step has general optimization factor proportional to `e^v v^(-1/8)`, uniquely minimized at the already chosen `v=1/8`. Its exact coefficient is

`C_q=2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)=3.995259361581614...`,

so the corresponding logarithmic potential constant is

`L_q=4+4 log C_q=9.540433994633053...`.

At `eta=1/100`, this sharpens the *scalar subbranch* of the pivot truncated half-potential to

`10[(pi+4 log2)+2L_q] = 249.9504936509568...`.

It does **not** improve the current global nine-direction `<3110` constant, because the independently checked indefinite-pair subbranch remains about `306.7443` with the existing hyperbolic estimate. This calculation is therefore recorded only as a local constant refinement and a precise indication of the next place one would have to improve.

## Final status and next obligation

- Baseline `s_17` theorem: **PASS** in this complete B04 audit.
- Geometric Brascamp--Lieb heat flow and all endpoint/rough-law passages: **PASS**.
- Support-package reproducibility files: **PASS / PRESENT**, and the new checker counts reproduce exactly; the prior package GAP is resolved.
- Threshold-nine replacement: **no defect found in this review; multiple separate PASS reports now exist in the repository, but release status is not self-awarded here**.
- Multiplicity below nine: **UNCHECKED/OPEN as a theorem**. The current `r=2` interpolation rank count has an exact barrier at nine; a new mechanism is required.
- Unrestricted three-eigenvalue conjecture: **OPEN**.
