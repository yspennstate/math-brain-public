Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on active R09 successor `CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM`: `p_cert = 1/2 -> 1/2`; supported unchanged count `4 -> 5`. Methods used: B14, B20, B23.**

# R09 run — OU subharmonicity closes every pure-weight face locally

## Continuity, source, literature, ownership

I did not reopen Tang Q4.11 or G0013. Tang's periodic-tree clause remains REFUTED/RETIRED in this track and its transitive-graph clause remains open. G0013 remains retired after its six-run handoff. The current exclusive R09 claim remains `operations/claims/CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM.md`.

I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current claim, and the newest complete R09 report `runs/R09/20260918T1232Z_gaussian_hr_compact_secondorder_b6e4a1.md`. Repository searches for the exact source title, arXiv `2405.01368`, `Gaussian copula`, and `WUVS` found the present R09 claim/reports but no distinct competing owner for this exact conjecture; the arXiv-ID search did not expose an intake alias that would supersede the current claim.

Fresh web checks dated 2026-09-18 again recovered the primary source, Yuyu Chen, Ruodu Wang, Yuming Wang and Wenhao Zhu, *Subuniformity of harmonic mean p-values*, Canadian Journal of Statistics 54 (2026), e70017, DOI `10.1002/cjs.70017`, first published online 26 July 2025, arXiv:2405.01368. Its Section 7 says that the positive-Gaussian case is not known in the literature and Section 8 explicitly conjectures subuniformity for Gaussian copulas with positive correlation coefficients. I found no later primary paper resolving that precise conjecture.

I also rechecked the later-author paper Yuyu Chen, Liyuan Lin and Ruodu Wang, *Universal Value-at-Risk superadditivity*, arXiv:2606.22884, submitted 22 June 2026. It develops UVS/WUVS and preservation results, but the bounded current search did not find a theorem there establishing WUVS for standard-Pareto margins coupled by an arbitrary positive Gaussian copula. This is bounded negative evidence, not a novelty certificate.

The fixed metric remains

\[
p_{\rm cert}:=\inf\Bigl\{p_0:\Pr(M_r^{\mathbf w}(U)\le p)\ge p
\text{ for every }p\in[p_0,1),\ n,\mathbf w,R,\ r\le-1\Bigr\},
\]

with `R` ranging over source-admissible positive-correlation Gaussian matrices. Before this run `p_cert=1/2`; after this run it is still `1/2`.

## B14 — find the group acting: all simplex vertices are strict local minima

The source quantifies over every weight vector. The previous Huesler--Reiss coefficient becomes small as a bivariate weight approaches `0` or `1`. Rather than estimate that degeneration, I moved to the weight simplex itself and used coordinate-permutation symmetry: it is enough to understand one pure-weight vertex and then relabel coordinates.

### Theorem (all-dimensional simplex-vertex OU repulsion)

Let `X=(X_1,...,X_n)` be a centered Gaussian vector with unit variances and positive definite correlation matrix `R`, with

\[
0<R_{ij}<1\qquad(i\ne j).
\]

Put `U_i=Phi(X_i)`. Fix a vertex `j`, a probability vector `a=(a_i)_{i\ne j}` on the other coordinates, and for `epsilon in [0,1]` define

\[
w_j(\varepsilon)=1-\varepsilon,
\qquad
w_i(\varepsilon)=\varepsilon a_i\quad(i\ne j),
\]

\[
H_\varepsilon
=\left(\frac{1-\varepsilon}{U_j}
+\varepsilon\sum_{i\ne j}\frac{a_i}{U_i}\right)^{-1},
\qquad
F_\varepsilon(p)=\Pr\{H_\varepsilon\le p\}.
\]

For every fixed `p in (0,1)`, writing `z_p=Phi^{-1}(p)`, `f(x)=1/Phi(x)`, and `P_t` for the Ornstein--Uhlenbeck semigroup

\[
P_t f(x)=\mathbb E f\left(e^{-t}x+\sqrt{1-e^{-2t}}Z\right),
\]

we have the exact one-sided derivative

\[
\boxed{
F_{0+}'(p)
=p^2\sum_{i\ne j}a_i
\left(P_{t_{ij}}f(z_p)-f(z_p)\right),
\qquad e^{-t_{ij}}=R_{ij}.
}
\]

Moreover

\[
\boxed{P_t f(x)>f(x)\qquad(t>0,\ x\in\mathbb R),}
\]

so

\[
\boxed{F_{0+}'(p)>0}
\]

whenever the inward direction gives positive weight to at least one coordinate not perfectly correlated with coordinate `j`.

Consequently, for every fixed positive-definite source-admissible `R`, every fixed `p in (0,1)`, and every fixed nontrivial inward direction from a simplex vertex, there is `epsilon_0>0` such that

\[
\Pr\{H_\varepsilon\le p\}>p
\qquad(0<\varepsilon<\varepsilon_0).
\]

By coordinate relabeling, the statement holds at every pure-weight vertex. By power-mean monotonicity, the same local subuniformity conclusion holds for every source order `r<=-1`.

This is PARTIAL. The radius `epsilon_0` is not uniform in `R,p,n`, and the theorem says nothing by itself about diffuse interior weights.

### Proof, part 1: the reciprocal normal CDF is strictly OU-subharmonic

Let

\[
\lambda(x)=\frac{\phi(x)}{\Phi(x)},
\qquad f(x)=\frac1{\Phi(x)}.
\]

Then

\[
f'(x)=-f(x)\lambda(x),
\qquad
\lambda'(x)=-\lambda(x)(x+\lambda(x)),
\]

and hence

\[
f''(x)=f(x)\lambda(x)(x+2\lambda(x)).
\]

For the OU generator `L=d^2/dx^2-x d/dx`,

\[
\boxed{
Lf(x)=f''(x)-xf'(x)
=2f(x)\lambda(x)(x+\lambda(x)).
}
\]

The factor `x+lambda(x)` is strictly positive. It is obvious for `x>=0`; for `x<0`, the strict Mills inequality

\[
\Phi(x)<\frac{\phi(x)}{-x}
\]

gives `lambda(x)>-x`. Thus `Lf>0` everywhere.

For every finite `t>0`, `P_t f(x)` is finite: the Gaussian transition variance `1-e^{-2t}` is strictly below one, while `f(y)` grows like a polynomial times `exp(y^2/2)` in the negative tail. The same integrability permits the standard semigroup differentiation, giving

\[
\frac{d}{dt}P_t f=P_tLf>0.
\]

Since `P_0f=f`, this proves `P_tf>f` for all finite `t>0`.

### Proof, part 2: differentiate the harmonic CDF at a weight vertex

Set

\[
V=U_j,
\qquad
B=\sum_{i\ne j}\frac{a_i}{U_i}.
\]

Then exactly

\[
H_\varepsilon
=\frac{V}{1+\varepsilon(VB-1)}
=V+\varepsilon V(1-VB)+o(\varepsilon)
\]

in the local first-order sense needed below. Because `V` is uniform on `(0,1)`, the standard derivative-of-a-regular-level-set identity gives

\[
F_{0+}'(p)
=-\mathbb E\left[V(1-VB)\mid V=p\right]
=p\left(p\,\mathbb E[B\mid V=p]-1\right).
\]

For completeness, this identity does not require a second moment of `B`. Truncate at `B<=M`. On the truncated event the displayed rational formula has a uniform first-order expansion in a fixed neighborhood of `V=p`, so conditioning on `V=v` and integrating over the `O(epsilon)` strip around `p` gives the derivative with `B` replaced by `B wedge M`. The conditional first moment of `B` is finite and continuous near `p` because each conditional Gaussian below has variance strictly less than one; letting `M to infinity` gives the formula by uniform integrability of the first moment.

Now condition on `V=p`, equivalently `X_j=z_p`. For each `i ne j`,

\[
X_i\mid X_j=z_p
\sim N\left(R_{ij}z_p,1-R_{ij}^2\right),
\]

so, with `e^{-t_{ij}}=R_{ij}`,

\[
\mathbb E\left[\frac1{U_i}\mid V=p\right]
=P_{t_{ij}}f(z_p)>f(z_p)=\frac1p.
\]

Therefore

\[
\mathbb E[B\mid V=p]
=\sum_{i\ne j}a_iP_{t_{ij}}f(z_p)>\frac1p,
\]

which yields the boxed derivative formula and strict positivity.

The ingredients `Mills ratio + OU semigroup` are classical; I found no source in the bounded search packaging this specific simplex-vertex harmonic-CDF derivative. Priority is therefore **unverified**, and I do not label the mechanism novel without an independent prior-art audit.

## B20 — find why the covering algorithm fails

I next tried to turn all currently proved positive regimes into an actual cover of the source parameter space. This produced two useful all-dimensional structural facts and a precise failure mode.

### Structural fact A: the Gaussian acceptance CDF is log-concave in the reciprocal threshold

Define

\[
S(x)=\sum_i\frac{w_i}{\Phi(x_i)}.
\]

The one-variable function `1/Phi` is convex, hence `S` is convex. For `t>1` set

\[
G(t)=\Pr\{S(X)\le t\}.
\]

If `A_t={x:S(x)<=t}`, convexity gives

\[
\theta A_s+(1-\theta)A_t
\subseteq A_{\theta s+(1-\theta)t}.
\]

A Gaussian measure is log-concave, so Prekopa--Leindler implies

\[
\boxed{
G(\theta s+(1-\theta)t)
\ge G(s)^\theta G(t)^{1-\theta}.
}
\]

Thus `G` is log-concave on its effective support. This does not use positive correlations.

### Structural fact B: every positive moment of the harmonic mean is universally bounded by the uniform moment

For any copula at all and every `k>0`, weighted AM--GM applied to the reciprocals gives

\[
H=\left(\sum_i\frac{w_i}{U_i}\right)^{-1}
\le\prod_iU_i^{w_i}.
\]

Then Holder gives

\[
\boxed{
\mathbb EH^k
\le \mathbb E\prod_iU_i^{kw_i}
\le\prod_i(\mathbb EU_i^k)^{w_i}
=\frac1{k+1}.
}
\]

These are strong one-dimensional shape constraints, but I did not find a valid argument converting them into the required first-order stochastic domination `H <=_st Uniform`. Moment domination and log-concavity are therefore recorded as tools, not as closure.

### The cover and the exact uncovered obligation

The existing R09 results now cover five different boundary mechanisms:

1. every dimension, every covariance, every weight, `p>=1/2`;
2. every dimension and every fixed weight, a neighborhood of the comonotone covariance, on each significance window bounded away from zero;
3. bivariate fixed `rho<1`, all weights fixed in the interior, sufficiently small `p`;
4. the bivariate Huesler--Reiss transition on compact interior `(delta,w)` boxes;
5. this run: every dimension, every `p`, a one-sided neighborhood of each pure-weight simplex vertex for each fixed covariance/direction.

The covering algorithm fails for a reason more serious than one missing bivariate boundary estimate. The metric `p_cert` quantifies over **all dimensions**, so even a complete proof of the bivariate conjecture would not move it. The still-uncovered source-valid obligation is genuinely high-dimensional:

\[
\boxed{
\Pr_R\left\{\left(\sum_{i=1}^n\frac{w_i}{U_i}\right)^{-1}\le p\right\}
\ge p
\quad
\text{for }n\ge3,\ 0<p<\tfrac12,\ R_{ij}>0,\mathbf w\in\Delta_n^+.
}
\]

Furthermore, the local radii from the covariance-face and weight-vertex theorems degenerate when the model approaches simultaneous near-comonotonicity / diffuse-or-nearly-pure weights. There is no dimension-free quantitative overlap yet. This is the precise reason that continuing to manufacture bivariate boundary lemmas cannot move the fleet metric.

This changes the next research target: the only worthwhile final pre-retirement attack is a **dimension-reduction/WUVS theorem** or a genuine high-dimensional counterexample.

## B23 — do what the proposer did not expect: search actively for a Gaussian counterexample

I attacked the negation rather than assuming the positive conjecture.

For the bivariate harmonic mean there is an exact stable one-dimensional representation. With weight `w`, correlation `rho`, and

\[
u_0=\frac{wp}{1-p(1-w)},
\qquad
v_p(u)=\frac{p(1-w)u}{u-wp},
\]

we have

\[
\Pr(H_w\le p)
=u_0+
\int_{u_0}^1
\Phi\left(
\frac{\Phi^{-1}(v_p(u))-\rho\Phi^{-1}(u)}{\sqrt{1-\rho^2}}
\right)du.
\]

Changing to Gaussian-score coordinates resolves the narrow boundary layer as `rho -> 1`. Exploratory searches using this representation, together with independent scrambled quasi-Monte-Carlo probes for small higher dimensions and nontrivial positive-correlation matrices, did not produce a negative margin that survived higher-accuracy recomputation. Apparent violations arose only in the numerically singular near-comonotone / highly imbalanced-weight regime and disappeared when the score-space boundary layer was resolved.

This is deliberately **not** a finite theorem or certificate: no exhaustive grid is claimed, no counterexample was found, and no numerical result is promoted to mathematical evidence. Therefore I did not create a checker-only artifact. The useful outcome of B23 is methodological: the numerical danger zone coincides exactly with the faces where the analytic positive margins degenerate, so any future counterexample search must use boundary-adapted coordinates or interval methods rather than ordinary quadrature.

## What moved and what did not

The mathematical state improved in two source-relevant ways:

- every pure-weight vertex is now proved to be a strict local CDF minimum in every dimension, using a clean OU-subharmonicity identity;
- the remaining obstruction has been identified as genuinely high-dimensional interior WUVS/dimension reduction, not merely unfinished bivariate gluing.

The fixed fleet metric nevertheless did **not** move:

\[
\boxed{p_{\rm cert}:\frac12\longrightarrow\frac12.}
\]

Supported unchanged count: `4 -> 5`.

Status: **PARTIAL / OPEN_CURRENT**.

Only one supported unchanged run remains before the CLOSABLE six-run retirement rule fires. The next run must either move the all-dimensional metric or write the six-run handoff and rotate.

## Next route

This run used B14, B20, B23. The next fresh triple is **B1, B3, B26**:

- **B1 (change the category):** work entirely in the Pareto/WUVS formulation and ask for a dimension-free stochastic-order criterion for Gaussian-copula Pareto vectors, rather than another harmonic-CDF local expansion.
- **B3 (prove something stronger):** seek a conditional or semigroup domination statement strong enough to imply WUVS simultaneously for every weight vector; the OU identity above is the one-coordinate boundary case of such a statement.
- **B26 (hunt the sporadic case):** if the strong route fails, search specifically in genuinely high-dimensional positive Gaussian covariance geometries, especially non-MTP2 / non-one-factor configurations, because bivariate and simple near-comonotone regimes are now heavily constrained. Any candidate must be interval- or otherwise rigorously certified before it can refute the source.

If `p_cert` remains `1/2` on that run, this target is retired from active R09 research under the six-unchanged-run CLOSABLE rule, with an immutable handoff preserving all partial theorems.

## Model / scheduler control status

The exposed task-management schema still supplies title, prompt, schedule/timing and enabled-state controls but no binding model-family selector, no reasoning-effort selector and no authenticated completed-run model telemetry. Therefore `GPT-6 / maximum` remains prompt text only; the actual metadata I can honestly report is `GPT-5.6 Sol / reasoning UNVERIFIED`.

The historical P26 message `You cannot modify this task` is an authorization-context issue. The lawful remedies remain use of the owning authorized context, an ownership/admin transfer, or platform support. Creating a duplicate or bypassing permissions is not a valid workaround. No scheduler or permission change was attempted.

## Bookkeeping

No checker artifact was created because this run's promoted results are analytic theorems with complete arguments on this page and no finite computational core. No shared-root, peer-track, email, Drive, public-posting, purchase, workflow, permission, or scheduler operation was performed.

```yaml
ledger_delta:
  track: R09
  active_claim: CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM
  source_status: OPEN_CURRENT
  result_status: PARTIAL
  metric_name: p_cert
  metric_before: 1/2
  metric_after: 1/2
  movement: no_movement
  supported_unchanged_before: 4
  supported_unchanged_after: 5
  methods_used: [B14, B20, B23]
  new_results:
    - name: all-dimensional simplex-vertex OU repulsion
      scope: positive-definite positive-correlation Gaussian copulas; every dimension and p; one-sided local weight perturbations from pure simplex vertices
      formula: "F'_0+(p)=p^2 sum_i a_i(P_{t_ij}f(z_p)-f(z_p)), f=1/Phi, exp(-t_ij)=R_ij"
      sign: strictly_positive_if_any_imperfect_pair
    - name: reciprocal-threshold acceptance CDF log-concavity
      scope: every Gaussian covariance and every positive weight vector
    - name: universal positive-moment domination
      scope: every copula; E[H^k] <= 1/(k+1) for every k>0
  prior_art_status: bounded_search_no_source_resolution_found_new_packaging_priority_unverified
  counterexample_search: no_candidate_promoted
  next_methods: [B1, B3, B26]
  retirement_trigger_if_next_unchanged: true
  tang_q411_periodic_tree: RETIRED_REFUTED
  g0013: RETIRED_HANDOFF_READY
```
