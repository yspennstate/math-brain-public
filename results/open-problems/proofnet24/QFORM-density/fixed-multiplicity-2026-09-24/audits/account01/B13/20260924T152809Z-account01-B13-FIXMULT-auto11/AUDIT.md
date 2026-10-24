# account01/B13 — complete audit of the nine-eigenvalue / constant-400 source

Run: `20260924T152809Z-account01-B13-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## Source pin

Audited standalone source:

- repository: `yspennstate/math-open-problems`;
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`;
- source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`;
- git blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`;
- SHA-256 from `MANIFEST.json`: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`;
- length: 955 lines, 60,749 bytes.

I read the entire 955-line `paper.tex`, and also read the current package `README.md`, `NINE_400_AND_OVERLAP.md`, `AUDIT_NEW.md`, `MANIFEST.json`, `proof_map.csv`, `verify_new.py`, and `checks_new.json`. I separately read the preserved 790-line baseline `manuscript.tex` at `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, together with the current root `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`.

## Verdict

**PASS (complete mathematical reconstruction of the exact nine/400 source).** I found no fatal mathematical gap in the theorem

\[
s_9(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 400K^2/s,
\]

for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, and arbitrary affine terms.

This is a mathematical audit, not formal verification or journal peer review. I do not claim global continuity for the assembled theorem. I did not perform an exhaustive novelty search; novelty/priority is therefore **UNCHECKED** in this run.

The exact source revision already has a separate complete B20 audit at `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account01/B20/20260924T152240Z-account01-B20-fixedmult-r11/AUDIT.md`. This B13 audit is a separate source reread and independent reconstruction, so it supplies the second complete mathematical review of this exact blob under the objective's review-count criterion. I do **not** mutate any owner release flag or call this formal verification.

## Source-range ledger

Every source line and every labeled item in `proof_map.csv` was read. The table records the status of the full intervening proof text, not just the labels.

| Source lines | Material | Status | Reconstruction |
|---|---|---|---|
| 1–80 | title, definitions, theorem, quantifiers, parameters, architecture | PASS | Exact scope is preserved: product laws only in original coordinates, no moments/support/sign restrictions; normalization/scaling target is `K^2/s`; nine and 400 are the actual stated threshold/constant. |
| 81–158 | Gaussian regularization, Plancherel, inversion, power envelope, Riesz half potential | PASS | Fourier convention and `2π` factors are consistent. The Riesz derivation gives the factor `(2π)^(-1/2)` and the `3/4` envelope contributes weighted integral `12 sqrt(u)`. |
| 159–213 | singular-value perturbation, Schur spectral count, diagonal dominance | PASS | Rank perturbation is a singular-value statement valid for nonsymmetric auxiliaries. The singular Schur case is correctly obtained by `A+epsilon I` at a fixed slightly lower threshold and limit. |
| 214–297 | geometric Brascamp–Lieb heat flow, product projections, scalar Fourier powers | PASS | Heat-flow sign follows from the frame contraction. Large-time and small-time limits are justified. Projection density uses deterministic orthogonal geometry only; no rotated independence is asserted. Scalar Fourier power proof correctly uses sums of original independent differences. |
| 298–396 | cross-block decoupling, regularized determinant estimate, Cauchy–Binet volumes | PASS | Copies are introduced on an original-coordinate bank. Difference coordinates are independent and cap-one. In the graph BL proof `alpha=(2πe)^2` cancels exactly; fourth-root decoupling yields exponent `-1/8`. |
| 397–527 | grouped mollified-`L^2` compiler, entropy step, hub promotion, terminal block, order-3/order-2 receivers | PASS | Jensen is applied to mollified `L^2` norms before taking the approximate-identity limit. The pure `J` phase is discarded only after integration of the original `I` variables. Weighted Hölder is valid for the finite non-normalized kernel measure. Hubs are literal original coordinates and all hub-to-left couplings remain in the phase. Constants reduce to `C3=3 sqrt(2)e(9/2)^(1/6)<15` and `C2=8 sqrt(e) 2^(-1/8)<14`. |
| 528–548 | scalar square and conditional profile | PASS | Completing the square is performed in one original coordinate. The density inequality is a domination formula against test functions; it does not assert independence between the square and the Schur remainder. |
| 549–562 | definite two-coordinate pair | PASS | See detailed B13 lens below. The `(delta,theta)` Jacobian is exactly `1/(2 sqrt(|det B|))`; integrating the bounded joint density over `theta` yields `πM/sqrt(|det B|)`. |
| 563–610 | indefinite pair / full hyperbolic envelope | PASS | See detailed B13 lens below. Both signs of the level set and both tails are included; translations preserve original-coordinate independence/caps; the tail estimate uses unit mass and cap one exactly once. |
| 611–662 | quarter-power small ball and logarithmic potential | PASS | The physical sign cut yields a literal crossing block with norm at least `L/4`. Gaussian smoothing and the gamma integral give a coefficient below five. Layer cake gives `4+4 log 5`; no atom follows by shrinking the interval. |
| 663–699 | pivot/volume definitions and volume-sampled interpolation | PASS | Ordered disjoint minors and squared sign conventions are correct. Singular seeds are excluded, hence the border count is an inequality, not a false equality. `P=A_{.,T}B^{-1}A_{S,.}` may be nonsymmetric. |
| 700–742 | completion and spectral-to-volume proposition | PASS | `D` is diagonal and zero on the seed; `E` has zero diagonal. Global `rank R<=3r` and restricted `rank R[L,L]<=r` are used at their correct separate steps. For `r=1,2`, exact dominance margins are `1131/2200` and `51/2200`. |
| 743–766 | random cut and no-pivot analytic consequences | PASS | Every ordered disjoint minor crosses a fair cut with probability `4^-k`. With `k=2,3` the free-volume theorem gives the stated `<70` half-potential and `<375` density bounds. |
| 767–789 | sharper convolution kernel | PASS | The exact inverse-hyperbolic formulas are consistent on `0<u<=1`; the logarithmic product bound yields `π+4 log2+2 log_+(1/u)`. For `u>=1` the displayed formula decreases and is below the same constant. |
| 790–811 | full half potential of a definite/indefinite pair | PASS | Definite density cap gives a stronger `D^-1/4` bound. In the indefinite case, scaling by `sqrt D` is correct; symmetric-decreasing overlap rearrangement is used on majorants, not on the input laws; `delta=1/64` gives `12+5 log2<16`. |
| 812–831 | five-eigenvalue full half-potential proposition | PASS | No-pivot branch uses order two. Scalar pivot combines the square profile, `J`, and one remaining spectral direction for the logarithmic expectation, adding the far kernel contribution `<=1`. Pair pivot uses the full pair potential. |
| 832–860 | main theorem proof and scaling | PASS | Scalar Schur remainder retains at least eight target-scale directions and hence five. Definite pair is direct. Indefinite pair retains at least seven; critical-value averaging is through domination/Tonelli. The branch constants are `<375,<280,<320,<383,<80,<392.5`, all below 400. `Y=KX` and division by `s` give exactly `K^2/s`. |
| 861–925 | overlap-one spectral-tail theorem and eight-direction corollary | PASS | `D` diagonal and `E` zero-diagonal are Frobenius-orthogonal. The rank-`3r` approximation tail is valid for nonsymmetric auxiliaries. Same-index bordered determinants identify the diagonal completion error exactly. `s_8>=1` therefore yields `W^x_{2,1}>=2V_2-9V_3`. |
| 926–955 | threshold accounting, limitations, acknowledgments, references | PASS for mathematical scope; UNCHECKED for exhaustive novelty | The source explicitly does not claim eight or three and does not claim global continuity. References are not mathematical dependencies because specialized statements are reproved. |

No source range remains mathematically **UNCHECKED**. The only explicit UNCHECKED item is exhaustive novelty/priority.

## B13 mandatory lens: definite pair

Let the conditional two-variable quadratic part be real symmetric definite `B`, with joint density `g<=M`. After translation and deterministic orthogonal diagonalization write eigenvalues `mu_1,mu_2>0` and level parameter `delta>0`:

\[
w=w_0+\sqrt{\delta/\mu_1}\cos\theta\,e_1
 +\sqrt{\delta/\mu_2}\sin\theta\,e_2.
\]

The determinant of the derivative matrix with columns `partial_delta w`, `partial_theta w` is

\[
\frac{1}{2\sqrt{\mu_1\mu_2}},
\]

independent of `delta,theta`. The map covers every noncritical point of the positive-definite level set once for `0<=theta<2π`. Hence the pushforward density is bounded by

\[
\frac1{2\sqrt{\det B}}\int_0^{2\pi}M\,d\theta
=\frac{\pi M}{\sqrt{\det B}}.
\]

Negative definite is reduced by negating the scalar output. The orthogonal diagonalization is only a deterministic integration coordinate change; no independence of rotated random variables is used. **PASS.**

## B13 mandatory lens: hyperbolic pair, both level-set signs and both tails

Let `mu_+>0>mu_-`, `D=mu_+|mu_-|`, and

\[
\Lambda=\mu_+^{-1}+|\mu_-|^{-1}.
\]

For `delta=z-v>0`, the two hyperbola branches are

\[
w_\epsilon(t)=\epsilon\sqrt{\delta/\mu_+}\cosh t\,e_+
 +\sqrt{\delta/|\mu_-|}\sinh t\,e_-,
\qquad \epsilon=\pm1.
\]

A direct determinant calculation gives the exact absolute Jacobian

\[
|\det(\partial_\delta w_\epsilon,\partial_t w_\epsilon)|
=\frac1{2\sqrt D}.
\]

The two values of `epsilon` cover the two connected components once. Thus coarea against nonnegative test functions gives

\[
p(v+\delta)=\frac1{2\sqrt D}\sum_{\epsilon=\pm1}
\int_\mathbb R f_1(w_{\epsilon,1}(t))f_2(w_{\epsilon,2}(t))dt.
\]

Writing one branch as `u e^t+w e^-t`, orthogonality gives `|u|=|w|=sqrt(delta Lambda)/2`. On the positive tail choose an **original** coordinate with `|u_i|>=|u|/sqrt2`; on the negative tail one may choose a different original coordinate with the analogous lower bound for `w`. The proof does not require these coordinates to coincide.

With `T_1=(3/4)log2`, the unwanted exponential is at most half of the dominant one. The chosen physical coordinate is monotone and satisfies `|x'(t)|>=|x(t)|/3`. After also requiring `|x(t)|>=1`,

\[
\int_T^\infty f_1(w_1(t))f_2(w_2(t))dt
\le 3\int_{|y|\ge m,\text{ one sign}}\frac{f_i(y)}{|y|}dy
\le3\log(1+1/m)\le3\log2.
\]

This is exactly where **both** assumptions `f_i<=1` and `\int f_i=1` are used: among cap-one mass-at-most-one functions on a half-line, the decreasing weight `1/|y|` is maximized by filling the nearest interval of length one. The middle interval is paid only by the pointwise cap `f_1f_2<=1`. The two tails and middle length give, branchwise,

\[
<6+\log_+\frac{32}{\delta\Lambda}.
\]

Since `Lambda>=2/sqrt D`, coarea yields

\[
p(v+\delta)\le D^{-1/2}
\left(6+\log_+\frac{16\sqrt D}{\delta}\right).
\]

For `delta<0`, negate the quadratic form and interchange the positive/negative eigendirections; the identical argument applies. The single critical output level is Lebesgue-null. Conditional averaging later is formulated through nonnegative test-function domination, so no pointwise version is selected on exceptional random slices. **PASS.**

## Critical-value averaging and logarithmic envelope

The quarter-power small-ball bound for a Schur critical-value polynomial `R` gives, as soon as its quadratic matrix has one target-scale spectral direction,

\[
\sup_a E\log_+(1/|R-a|)\le4+4\log5.
\]

For an indefinite physical pair of determinant modulus `D>=p`, average the hyperbolic majorant:

\[
p_Q(z)\le D^{-1/2}
\left(6+\log16+\tfrac12\log_+D+L_0\right).
\]

The only unbounded-in-`D` term is

\[
\tfrac12 D^{-1/2}\log_+D\le1/e.
\]

For `p=1/400`, this gives the source's `<392.5` branch. This is an averaging of positive majorants; it is not an assertion that the critical value is independent of the conditioned pair. **PASS.**

## Support-file audit

- `README.md`: PASS as source/scope description; correctly says the exact new revision requires independent review and does not claim eight.
- `AUDIT_NEW.md`: historical author self-audit only; its logical limitations are correctly stated.
- `proof_map.csv`: PASS; labels and source positions agree with the source read.
- `MANIFEST.json`: PASS as provenance metadata for the paper pin, size/blob/SHA and finite-check scope.
- `verify_new.py`: PASS as finite-check code. Exact fraction checks and exact finite interpolation/overlap instances are correctly distinguished from floating diagnostics.
- `checks_new.json`: PASS as the recorded output of that checker; it explicitly does not claim universal proof.
- Preserved baseline package: source pin/hash/length in `SOURCE_MANIFEST.json` agrees with the 790-line source actually read. The baseline proof is mathematically subsumed by the stronger reviewed replacement, but I also found no fatal defect in the preserved source while comparing the common analytic/algebraic spine.

## First end-to-end reconstruction

Forward dependency reconstruction:

`rough product laws -> BL projection/Fourier powers -> physical decoupling -> grouped original-coordinate receiver -> no-pivot volume -> order-3 density / order-2 half potential -> scalar/pair pivots -> Schur counts -> main theorem`.

Every arrow was rederived from its hypotheses without importing a prior PASS label. Result: **PASS**.

## Second end-to-end reconstruction

Adversarial reverse reconstruction from each final branch:

1. no pivot: `s9 -> V3 -> literal cut Z3 -> marginal-free order-3 receiver`;
2. scalar pivot: `s9 -> Schur s8 -> five-direction full half potential -> square profile`;
3. definite pair: direct two-dimensional Jacobian, no spectral remainder required;
4. indefinite pair: `s9 -> Schur at least seven -> one-direction quarter/log potential -> full two-sign hyperbolic envelope -> Tonelli average`;
5. general scale: original product cap restored through `Y=KX`, then output scaling by `s/K^2`.

I separately checked the failure modes forbidden by the live corrections: no random rotation of independence, no projected-density shortcut for an indefinite pushforward, no law-uniform pointwise quadratic-phase decay, and no diagonal-only reduction. Result: **PASS**.

## Downstream status

- Exact nine/400 theorem: **PASS in this B13 review**.
- Mathematical review-count criterion for this exact blob: this B13 reconstruction is separate from the already committed B20 complete audit. I do not self-award or mutate any release/peer-review flag.
- Global continuity of the full theorem: **NOT CLAIMED**.
- Eight-direction theorem: handled separately in this run's improvement report; it is a newer candidate, not part of this source's proved claims.
- Unrestricted three-direction conjecture: **OPEN**.
