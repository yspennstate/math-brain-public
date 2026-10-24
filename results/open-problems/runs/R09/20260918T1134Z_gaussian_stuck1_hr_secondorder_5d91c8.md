Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on active R09 successor `CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM`: `p_cert = 1/2 -> 1/2`; supported unchanged count `2 -> 3`, so this is the required STUCK1 thinking-only run. Methods used: B12, B19, B27.**

# R09 STUCK1 — Gaussian positive-correlation subuniformity

Date: 2026-09-18 UTC.

Status: **OPEN_CURRENT / PARTIAL / STUCK1**. This report makes no new theorem-sized R09 claim. It records the exact obstruction, the routes already tried, and a non-promoted asymptotic calculation identifying the next proof target.

Tang Question 4.11 is not reopened. Its periodic-tree assertion remains retired/refuted in the R09 history, and G0013 remains retired after its six-run handoff. The controlling R09 claim is `operations/claims/CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM.md`.

## Source/current-status/ownership check

The primary source is Yuyu Chen, Ruodu Wang, Yuming Wang, Wenhao Zhu, *Subuniformity of harmonic mean p-values*, Canadian Journal of Statistics, DOI `10.1002/cjs.70017`, arXiv:2405.01368. The publisher full text still says that for Gaussian copulas with positive correlations the corresponding general subuniformity statement is not known and the conclusion explicitly conjectures it. Fresh 2026-09-18 searches on the exact title/arXiv identifier, `harmonic mean p-values Gaussian copula`, and the exact Gaussian-positive-correlation wording recovered the source but no later primary resolution of that exact conjecture. This is bounded negative evidence, not a worldwide novelty certificate.

The R09 exclusive claim remains in force; repository claim/search state showed no competing owner for this exact successor. No shared root or peer file was edited.

## Frozen metric

`p_cert` is the smallest lower endpoint rigorously certified by R09 such that the source inequality holds for **every** `p in [p_cert,1)`, every dimension, every positive-correlation Gaussian copula, every source-valid weight vector, and every `r <= -1`.

Before this run: `p_cert = 1/2`.

After this run: `p_cert = 1/2`.

No movement. Supported unchanged count after the admission-run movement: `2 -> 3`.

## (a) Exact statement that blocks

It is enough to work at the harmonic mean because power means are increasing in their order. If `X ~ N(0,R)`, `U_i = Phi(X_i)`, `R` is a correlation matrix with positive off-diagonal entries, and `w_i > 0`, `sum_i w_i = 1`, define

\[
H_{R,w}=\left(\sum_{i=1}^n \frac{w_i}{U_i}\right)^{-1}.
\]

The full remaining source obligation is

\[
\boxed{\Pr_R\{H_{R,w}\le p\}\ge p
\quad\text{for every }n,\ R,\ w,\ 0<p<1/2.}
\]

To move the frozen metric below `1/2`, one needs a **uniform** theorem over the displayed class on some full interval `[p_0,1/2)`. Pointwise-in-`R`, pointwise-in-`w`, fixed-dimension, or merely asymptotic small-`p` statements do not move `p_cert`.

## (b) Routes tried and the precise reason each stops

1. **Upper-half `log Phi` route.** Concavity of `log Phi` gives
   \[
   H_{R,w}\le \prod_i U_i^{w_i}\le \Phi\!\left(\sum_i w_iX_i\right).
   \]
   Since `Var(sum w_i X_i) <= 1`, this proves the source inequality uniformly for `p >= 1/2`. For `p<1/2`, `z_p=Phi^{-1}(p)<0`, and variance contraction sends `Phi(z_p/sigma)` in the wrong direction. This route has a genuine sign wall at `1/2`, not a missing estimate.

2. **Differentiate in Gaussian correlation.** In the bivariate weighted harmonic case, exact differentiation of the moving boundary gives an integral whose sign is not pointwise fixed. At the boundary fixed point the local contribution has the wrong sign when `p<1/2`. Thus a naive monotonicity theorem in the correlation parameter cannot be proved by pointwise sign of the derivative; any successful derivative proof must exploit cancellation across the whole boundary.

3. **Comonotone first variation.** Along `R_t=(1-t)J+tR`, R09 proved
   \[
   \Pr(H_t\le p)
   =p+t(1-w^TRw)\phi(z_p)\bigl(z_p+\phi(z_p)/\Phi(z_p)\bigr)+o(t),
   \]
   with positive first-order coefficient in every nontrivial direction. This proves a neighborhood of the comonotone endpoint on every threshold window bounded away from zero, but its available remainder control is not uniform as `p downarrow 0`.

4. **Fixed-correlation hidden-tail route.** For fixed bivariate `0<rho<1` and fixed `0<w<1`, R09 proved strict subuniformity for all sufficiently small `p`, using the regularly varying lower-tail Gaussian copula and exact strip-plus-harmonic-wedge accounting. The positive margin is nonuniform as `rho -> 1`, exactly where the hidden-tail exponent degenerates toward the comonotone regime.

5. **Pareto/WUVS dual language.** Writing `L_i=1/U_i`, the desired inequality is the stochastic-order statement
   \[
   L_1\preceq_{st}\sum_iw_iL_i
   \]
   for Pareto(1) margins coupled by a positive Gaussian copula. This places the problem in weighted universal VaR superadditivity language, but the bounded literature search located no Gaussian-copula/Pareto preservation theorem strong enough to settle this case.

6. **Numerical counterexample search near `rho=1`.** Ordinary quadrature generated tiny apparent violations, but score-coordinate re-integration showed these were boundary-layer integration failures. No certified counterexample survives. The numerical route therefore does not justify REFUTED.

The common failure is now clear: the known positive margins live on opposite nonuniform scales. Fixed `rho<1` is controlled as `p -> 0`; fixed `p>0` is controlled for `rho` sufficiently close to one. Neither theorem is uniform in the coupled transition

\[
(1-\rho)\log(1/p)=\Theta(1).
\]

## (c) What a proof must contain that no completed route contains

The missing ingredient is a **second-order, sign-controlled Huesler-Reiss boundary-layer estimate for the nonlinear harmonic wedge, with a remainder uniform enough to glue to both endpoint regimes**.

### B12 — find what is conserved

Set

\[
s=-\Phi^{-1}(p),\qquad \rho_p=1-\frac{\delta}{s^2},\qquad \delta>0\ \text{fixed}.
\]

At Huesler-Reiss scale, the standard Gaussian tail calculation gives the following leading representation for the `p`-normalized lower-tail measure of

\[
A=U/p,\qquad B=V/p:
\]

\[
\mu_\delta(F)
=\int_0^\infty \mathbb E\,F\bigl(a,a e^D\bigr)\,da,
\qquad D\sim N(\delta,2\delta).
\]

This is recorded here only as the standard/formal Huesler-Reiss limit used to diagnose the obstruction; it is not promoted in this STUCK report as a new R09 theorem.

For the weighted harmonic event

\[
\mathcal A_w=\left\{(a,b):\frac wa+\frac{1-w}{b}\ge1\right\},
\]

fixing `D` and substituting `b=a e^D` turns the event into

\[
a\le w+(1-w)e^{-D}.
\]

Therefore the leading limiting mass is exactly

\[
\mu_\delta(\mathcal A_w)
=\mathbb E\bigl[w+(1-w)e^{-D}\bigr]
=1,
\]

because `E exp(-D)=1` for `D ~ N(delta,2delta)`.

**Outcome of B12:** the Huesler-Reiss leading term is exactly neutral. There is no first-order tail margin to harvest. This explains why the fixed-`rho` and near-comonotone arguments fail to overlap automatically. Any proof in the transition regime must go to the next asymptotic order.

### B19 — make the missing step an algorithm

The next-order calculation can be organized explicitly. For fixed `a>0`, if `h=log a`, then inversion of the Mills expansion gives

\[
\Phi^{-1}(pa)
=-s+\frac{h}{s}
+\frac{h^2/2-h}{s^3}
+O(s^{-5})
\]

on compact `a`-ranges. For `a>w`, the harmonic boundary is

\[
g_w(a)=\frac{a(1-w)}{a-w}.
\]

Substituting the quantile expansion into the exact conditional-normal integral and then setting

\[
q=\log\frac{a-w}{1-w}
\]

turns the Gaussian kernel into the density of

\[
Q\sim N(\delta,2\delta).
\]

After algebra and one Gaussian integration-by-parts identity, the **formal** second-order coefficient collapses to

\[
\boxed{
C(\delta,w)
=2\delta w(1-w)
\,\mathbb E\!\left[\frac{1}{w+(1-w)e^Q}\right]
>0,
\qquad Q\sim N(\delta,2\delta).
}
\]

Thus the formal expansion is

\[
\frac{\Pr_{\rho_p}(H_w\le p)}{p}
=1+\frac{C(\delta,w)}{s^2}+o(s^{-2}).
\]

This is **not certified as a theorem in this run**. The missing work is precisely the uniform error estimate: the conditional integral ranges over `a` up to `1/p`, the displayed quantile expansion is only immediately uniform on compact `a`-sets, and a source-useful statement must also control `delta -> 0`, `delta -> infinity`, and `w -> 0,1`. The sign calculation is valuable because it tells the next run exactly what to prove rather than what to guess.

The prospective proof algorithm is therefore:

1. truncate the harmonic boundary integral at `|q| <= L` and obtain a uniform second-order Gaussian-quantile expansion there;
2. bound the `|q|>L` pieces directly by Gaussian/Mills estimates uniformly on `delta` in a compact interval and `w` bounded away from `0,1`;
3. let `L` grow only after the `s -> infinity` estimate is closed;
4. use the already-proved comonotone first variation for small `delta` and the fixed-correlation hidden-tail theorem for large `delta`;
5. separately control `w` near `0` or `1`, where the harmonic mean degenerates to a single uniform and the positive coefficient above vanishes.

### B27 — swap the quantifiers

The formal calculation is positive for each fixed pair `(delta,w)`, but the source quantifiers are much stronger. The actual family has

\[
\delta=s^2(1-\rho)
\]

and `delta` may itself depend on `p`; likewise the source permits weights depending on the instance. Hence

\[
\forall\delta,w\ \exists p_0(\delta,w)
\]

is not enough. What is needed for a gluing theorem is a controlled statement of the form

\[
\exists p_0\ \forall p<p_0\ \forall\rho\in(0,1)\ \forall w\in(0,1),
\]

or a finite partition of the `(delta,w)` parameter space whose estimates are uniform on every piece. The second-order coefficient itself degenerates at all four boundary faces (`delta=0`, `delta=infinity` in the relevant normalized sense, `w=0`, `w=1`), so a direct compactness argument is unavailable until those faces are supplied with separate endpoint estimates.

**Outcome of B27:** the obstruction is not the sign of the interior Huesler-Reiss coefficient; it is the uniform gluing of the four degenerating parameter faces plus, beyond the bivariate case, the passage to arbitrary dimension/covariance.

## (d) Simplest special case still unproved

The cleanest unresolved source-valid special case is already

\[
\boxed{
\Pr_\rho\!\left\{
\frac{2UV}{U+V}\le p
\right\}\ge p
\quad\text{for every }0<p<1/2,\ 0<\rho<1,
}
\]

where `(U,V)=(Phi(X),Phi(Y))` and `(X,Y)` is standard bivariate Gaussian with correlation `rho`.

Even this equal-weight two-dimensional statement is not yet proved globally by R09. The upper half, fixed-`rho` sufficiently-small-`p` regime, and a neighborhood of `rho=1` at fixed threshold are covered separately. The transition layer above is the missing bridge.

## (e) Nearest solved problem in the literature and what it has that this problem lacks

The nearest solved asymptotic problem is the Huesler-Reiss transition for maxima of Gaussian triangular arrays. Huesler and Reiss (1989), *Maxima of normal random vectors: Between independence and complete dependence*, identify the nontrivial Gaussian extreme-value limit when correlations approach one on the logarithmic extreme scale. Engelke, Kabluchko and Schlather (Bernoulli 2015) give a broader Gaussian triangular-array formulation, and Hashorva-Peng-Weng (2014) develop higher-order expansions in the Huesler-Reiss model.

What those results supply is exactly the machinery absent from the completed R09 argument: controlled Gaussian extreme-value expansions in the coupled `rho -> 1`, tail-level `-> 0` regime. What they do **not** immediately supply is the sign-uniform second-order integral over the nonlinear harmonic wedge, nor uniformity as the harmonic weight tends to `0` or `1`. The R09 calculation above suggests that a first-order Huesler-Reiss theorem is provably insufficient because its harmonic-wedge mass is exactly `1`; one must import a **higher-order** expansion and keep the nonlinear wedge geometry.

## Required recovery choice

**Choice: PORT THE TECHNIQUE FROM (e).**

The next research run should not add another unrelated correlation lemma. It should take the existing higher-order Huesler-Reiss/penultimate Gaussian expansion machinery and make the displayed formal coefficient rigorous on a compact interior parameter box

\[
\delta\in[\delta_0,\delta_1],\qquad w\in[\varepsilon,1-\varepsilon],
\]

with an explicit uniform remainder. Only after that should it try to glue the four boundary faces using the already-existing R09 endpoint theorems.

Fresh Section-B moves reserved for that recovery: **B17, B21, B29** — identify the second-order coefficient inside the penultimate/Huesler-Reiss literature, search adjacent extreme-value/risk-aggregation formulations with the same nonlinear wedge, and compactify the degenerating parameter faces before attempting a global bivariate proof.

## Literature search log, 2026-09-18

Queries included:

- exact title `Subuniformity of harmonic mean p-values` plus `Gaussian copula` and `2026`;
- arXiv identifier `2405.01368` plus Gaussian/subuniformity terms;
- `harmonic mean p-values Gaussian positive correlations subuniformity`;
- `Huesler-Reiss Gaussian copula lower tail triangular array 1-rho log(1/p)`;
- `Gaussian copula Pareto weighted sum stochastic order harmonic mean p values`.

Recovered: the Chen-Wang-Wang-Zhu source; Huesler-Reiss (1989); later Gaussian triangular-array/Huesler-Reiss work including Engelke-Kabluchko-Schlather and higher-order expansion literature. No later primary paper resolving the exact Chen-Wang-Wang-Zhu positive-Gaussian subuniformity conjecture was found in this bounded search.

## Model / scheduler control reality

The limitation is unchanged. The exposed task-management schema permits title, prompt, schedule, timing mode and enable/disable state. It exposes **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore `GPT-6 / maximum` remains prompt text only in this environment, and this report does not claim it ran. Changing that requires a product/API scheduler surface that exposes model and reasoning fields and returns authenticated run metadata.

The recorded `You cannot modify this task` failures for P26/P01/P03 are permission/ownership failures. The legitimate remedies are the task's owning authorized context, an ownership/admin transfer through the product, or platform support. Repository edits, duplicate schedules, or permission bypass are not scheduler repairs.

## ledger_delta

```yaml
ledger_delta:
  worker: R09
  target: CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM
  source_status: OPEN_CURRENT
  status: PARTIAL_STUCK1
  metric_name: p_cert
  before: 1/2
  after: 1/2
  movement: false
  supported_unchanged_count_before: 2
  supported_unchanged_count_after: 3
  methods_this_run: [12, 19, 27]
  recovery_choice: port_nearest_solved_technique
  next_methods: [17, 21, 29]
  new_theorem_claim_this_run: false
  tang_reopened: false
  g0013_reopened: false
  shared_roots_edited: false
  peer_files_edited: false
  checker_created: false
```

No exact checker was created because this is the policy-mandated thinking-only STUCK1 run and no new finite claim is promoted. No email, Drive, public posting, purchase, permission change, workflow execution, or scheduler change was performed.