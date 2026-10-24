# account01/B03 r14 — full audit of the pinned seventeen-eigenvalue manuscript

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T145056Z-fixed-multiplicity-audit-r14`  
Account/slot: `account01/B03`  
Pinned baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned `manuscript.tex` git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Pinned source length: 790 lines, 47,883 bytes.

## Verdict

**PASS — mathematical theorem as stated.** I read the entire pinned 790-line source independently in this run, together with `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`. I found no fatal mathematical gap in the stated theorem

\[
s_{17}(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary real symmetric `A`, arbitrary `b,c`, and arbitrary independent real coordinate laws with Lebesgue densities bounded by `K`.

This PASS is one worker audit, not formal verification, journal peer review, or a claim that the unrestricted three-eigenvalue problem is solved. The theorem asserts an essentially bounded density; continuity is not established in every pivot branch and is not needed for the stated theorem.

## End-to-end source audit

| Source range | Item | Verdict | Independent check and downstream impact |
|---|---|---|---|
| 39–89 | Definitions, theorem/corollary, normalization and proof architecture | **PASS** | Quantifiers are preserved: arbitrary dimension/signature/remaining spectrum/affine terms/rough product densities. `s_j(A)` is singular-value ordering, hence absolute eigenvalue ordering for symmetric `A`. The normalized reduction `K=s=1` used later is compatible with the final scaling. |
| 91–120 | Fourier/Plancherel/Gaussian inversion | **PASS** | Fourier convention and constants are internally consistent. Approximate-identity passage is legitimate in `L^2`; if `phi in L^1`, Gaussian-smoothed densities converge uniformly to a continuous nonnegative density representing the law. The Gaussian identity has the stated `1/(2 sqrt(pi v))` factor. |
| 122–160 | Power envelope and Riesz negative-half-moment bound | **PASS** | The envelope integral is `2ap/(p-1)`, producing `ap/[pi(p-1)]`. The gamma representation and the substitution in the `v`-integral give the stated `1/sqrt(2pi)` Riesz constant. The `3/4` tail gives weighted integral `12 sqrt(u)`. Tonelli is used only for nonnegative majorants. |
| 169–217 | Singular-value perturbation, Schur count, strict diagonal dominance | **PASS** | The nonsymmetric singular-value rank perturbation is the correct tool later. The Schur spectral-count proof through the complementary principal block of `A^{-1}` is valid; singular `A` is handled by an `A+epsilon I` sequence while keeping the pivot invertible and passing thresholds continuously. The diagonal-dominance lemma does not assume symmetry. |
| 221–255 | Geometric rank-one Brascamp–Lieb proof | **PASS** | Heat-flow identity has the correct sign and frame contraction. Compact-support Gaussian bounds justify differentiation/integration by parts. The large-time normalization uses `sum c_i=d`; the small-time Fatou passage is valid almost everywhere. Monotone truncation extends to general nonnegative integrable factors. |
| 258–282 | Product-projection density bound | **PASS** | The orthogonal completion is used only in a deterministic integral, not to assert independence after rotation. The frame weights are `b_i=|w_i|^2`; factors with `b_i=0` are safely discarded using `f_i<=1`. The bound `prod b_i^{-b_i/2}<=e^{d/2}` follows from `-b log b<=1-b`. Scalar rescaling gives `sqrt(e)/|a|`. |
| 284–301 | Scalar Fourier powers and difference-density cap | **PASS** | Since `|fhat|<=1` and `f in L^2`, all even powers used are integrable. Fourier inversion at zero applies to the continuous convolution density and the projection bound on `2m` signed original coordinates yields exactly the advertised `2pi sqrt(2e)/sqrt(p)` bound. A copied difference has density `f*tilde f<=1`. |
| 303–324 | Independent-copy decoupling | **PASS** | This is the B03-sensitive step. Cauchy–Schwarz is applied in one original product bank, the square is expanded with one independent copy of the opposite bank, and integration over untouched original coordinates creates the product Fourier factors. The copied differences are independent across physical coordinates and have density cap one. The proof **never** assumes independence between a difference and its corresponding sum. Jensen is applied only to the nonnegative RHS, giving the fourth-power inequality. No moments are needed because all pre-estimate oscillatory integrands have modulus one. |
| 326–373 | Regularized crossing determinant | **PASS** | With `a=2t`, `alpha=(2pi e)^2`, the frame weights satisfy `sum d_i=sum(1-c_j)`. The graph-BL Jacobian factors are correct. Applying the scalar Fourier lemma with exponent `2/d_i` produces `(2pi sqrt(e d_i))^{d_i}`; the `d_i` powers cancel, and the coordinate entropy contributes `e^{theta/2}`. This cancels exactly with the chosen regularizer. Taking the fourth root of the decoupled fourth-power estimate gives determinant exponent `-1/8`, hence crossing order `k` gives Fourier exponent `k/4`. |
| 376–400 | Crossing volumes and order-three/order-five envelopes | **PASS** | Cauchy–Binet coefficient identity is correct. Retaining the order-`k` determinant term gives `u_k=pi e Z_k^{-1/(2k)}` and exponent `k/4`. `k=5` is integrable (`5/4>1`); `k=3` is not used for direct inversion but becomes integrable after the `|t|^{-1/2}` Riesz weight. Constants `5e` and the three-volume half-potential bound are correct. |
| 404–434 | Scalar square and definite two-coordinate pivots | **PASS** | The square pushforward profile and interval preimage length are correct. The conditional domination formula is a measure inequality obtained against nonnegative test functions, so no independence of the square part and residual is asserted. The definite-pair polar change of variables has Jacobian `1/(2 sqrt(det B))` and gives `pi M/sqrt(|det B|)` without claiming rotated random coordinates are independent. |
| 437–482 | Hyperbolic pair | **PASS** | Level-set parametrization and Jacobian `1/(2 sqrt(D))` are correct. The tail coordinate can be chosen in the original coordinate system; the monotonicity and reciprocal-tail estimates use only one original marginal density at a time. The middle interval contributes the logarithm. AM–GM converts `Lambda` to the displayed determinant-only envelope. The critical level is null, and the proof explicitly routes conditional use through nonnegative test functions rather than pointwise exceptional slices. |
| 485–525 | Quarter-power concentration and logarithmic potential | **PASS** | Large diagonal case follows from the scalar square preimage length. In the off-diagonal case the random sign cut gives a physical cross block with norm at least `L/4`; applying the determinant theorem at one singular direction gives the `|t|^{-1/4}` majorant. Gaussian smoothing and the explicit gamma integral give the stated quarter-power coefficient (<16). Layer cake then gives `L_0=4+4 log 16`; atoms are excluded by shrinking the small-ball radius. |
| 528–580 | Disjoint volumes, sampled interpolation, completion | **PASS** | The volume uses ordered disjoint row/column sets. The bordered-minor identity is exact for nonsingular seeds, and sorting signs disappear after squaring. Singular seeds can have nonsingular extensions, so the proof correctly claims an inequality rather than equality. The nonsymmetric interpolant `P` has rank at most `r` and exactly interpolates rows `S` and columns `T`. In the completion, `R-P` is supported in rows `T` or columns `S` outside the already-zero row/column/block pieces, yielding global `rank R<=3r`, while `R_LL=P_LL` yields the sharper restricted rank `<=r`. `D` vanishes on `S union T`. |
| 582–619 | No-pivot spectral-to-volume proposition | **PASS** | The telescoping ratio argument handles both positive volumes and first vanishing volume. For `r=0`, the no-pivot entry bound contradicts `s_{4k-3}>=1`. For `1<=r<=4`, `epsilon<=(r+1)/80<=1/16`. Rank perturbation with the **possibly nonsymmetric** `D+R` forces at least `r+1` large diagonal entries of `D`, all in `L`. The off-diagonal bound gives row sum `<23/28`, while the diagonal lower bound is `371/400`; strict diagonal dominance contradicts `rank R_LL<=r`. No eigenvalue argument is incorrectly applied to the nonsymmetric auxiliary matrix. |
| 621–645 | Random physical cut and no-pivot analytic consequences | **PASS** | Each disjoint `k+k` minor crosses a fair cut with probability `4^{-k}`. The resulting `Z_k^{-1/(2k)}<=160` is correct. Order three gives the full half-potential bound `<200`; order five gives continuous density `<=800e<2400`. Affine and within-bank terms remain inside arbitrary `F,G`. |
| 654–714 | Singular kernels and pivot truncated half potential | **PASS** | Both kernel estimates are valid and are used under Tonelli. Scalar pivot: Schur leaves one spectral direction for the logarithmic residual; `eta^{-1/2}(8+3L0)<600`. Definite pair gives a uniform conditional density. Indefinite pair uses the hyperbolic envelope and the exact `sup D^{-1/2} log_+ D=2/e`; conditioning variables only change affine/critical values, handled through measure domination. |
| 716–724 | Nine-eigenvalue full half-potential theorem | **PASS** | Pivot branch uses the truncated bound; no-pivot branch has the stronger full half-potential. Outside the truncation radius the kernel is at most one, so the full potential is `<=601`. |
| 726–749 | Main theorem proof | **PASS** | No-pivot branch uses order five. Scalar pivot loses at most one large spectral direction and hence leaves at least nine for the residual; density `<=6010`. Definite pair is immediate. Indefinite pair loses at most two directions and only needs one surviving direction for the logarithmic potential. All branches fit below `10^4`. |
| 750–790 | Scaling, equivalence, threshold accounting, limitations | **PASS** | With `Y=KX`, the new densities are cap one; `Q=(s/K^2) Qtilde` with quadratic matrix `A/s`, giving the final `K^2/s` scaling. Interval domination/density equivalence is standard. The manuscript correctly distinguishes order-three half-potential from order-five direct density and explicitly does **not** claim the full three-eigenvalue theorem or universal continuity. |

## Package/support verdicts

- `README.md`, `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`: **PASS as readable package contents**. The baseline blob/hash/line/byte metadata are mutually consistent with the file actually read in this run.
- `verify.py`: **PASS on code inspection for its stated limited purpose**. It pins the baseline hash, checks the interpolation/rank identities on exact symbolic examples, and performs explicitly non-rigorous floating diagnostics separately.
- Recorded execution in `checks.json`: **UNCHECKED in this run as an execution event**. I read the code and the recorded PASS payload but did not re-execute Python. The finite suite is not used as a premise of the theorem audit.
- Compiled PDF hash/render claim in `SOURCE_MANIFEST.json` / `DELIVERY_STATUS.md`: **UNCHECKED in this run**. I audited the complete 790-line mathematical source rather than rebuilding/rendering the binary PDF.
- Bibliographic attribution wording to BCCT and Rudelson–Vershynin: **UNCHECKED as a primary-source literature claim in this run**. The specialized inequalities actually used are reproved in the manuscript, so this does not create a dependency gap in the mathematical proof.

There are no source-line ranges of the mathematical proof left UNCHECKED in this B03 audit.

## B03-specific conclusions

The sensitive copy/exponent chain is sound. The manuscript pays two powers exactly as follows:

1. one Cauchy–Schwarz square creates one independent copy and a product of scalar Fourier factors;
2. Jensen on the resulting nonnegative expectation creates the fourth-power inequality;
3. geometric BL bounds that fourth-power RHS by a determinant to exponent `-1/2`;
4. taking the fourth root produces determinant exponent `-1/8`;
5. an order-`k` minor coefficient therefore produces decay `|t|^{-k/4}`.

Thus order four is genuinely the critical `|t|^{-1}` endpoint; order five is the first leverage-free integrable crossing order in this mechanism. Any proposed 17-to-13 reduction must obtain additional structure/cancellation rather than silently treating the copied sum as independent of its difference or changing the Fourier power bookkeeping.

## Review status

This report is my own complete review only. I do not convert other workers' artifacts into a second review and do not mark the candidate independently validated here. Any lower-multiplicity replacement theorem still requires its own complete proof and two genuinely separate end-to-end reviews before validation.
