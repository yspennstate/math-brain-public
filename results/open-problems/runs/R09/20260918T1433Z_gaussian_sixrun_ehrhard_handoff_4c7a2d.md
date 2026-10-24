Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on active R09 successor `CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM`: `p_cert = 1/2 -> 1/2`; supported unchanged count `5 -> 6`, so the CLOSABLE six-run retirement rule fires. Methods used: B1, B3, B26.**

# R09 run — Pareto/WUVS translation, Ehrhard profile reduction, and six-run handoff

## Continuity, source, current literature, ownership

I did not reopen Tang Question 4.11 or G0013. Tang's periodic-tree clause remains REFUTED/RETIRED in the R09 record and its transitive-graph clause remains open. G0013 remains retired after its own six-run handoff. The controlling exclusive R09 claim for this run is still `operations/claims/CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM.md`.

Before research I reread the required campaign/root state (`probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`), the current claim, the newest complete R09 report `runs/R09/20260918T1332Z_gaussian_ou_vertex_faces_91c7e4.md`, and current queue/ownership evidence. The preceding report fixed

\[
p_{\rm cert}=\frac12
\]

with supported unchanged count five and reserved methods B1/B3/B26 for this final pre-retirement attack.

Fresh literature checks dated 2026-09-18 again recovered the primary source, Yuyu Chen, Ruodu Wang, Yuming Wang and Wenhao Zhu, *Subuniformity of harmonic mean p-values*, Canadian Journal of Statistics 54 (2026), e70017, DOI `10.1002/cjs.70017`, first published online 26 July 2025, arXiv:2405.01368. Its Section 7 says that the corresponding general positive-Gaussian statement is not known in the literature, and Section 8 explicitly conjectures subuniformity for Gaussian copulas with positive correlation coefficients. Searches on the exact title, arXiv identifier, conjecture wording, `Gaussian copula`, `Pareto`, `WUVS`, and 2026 follow-up terminology did not find a later primary paper resolving this exact conjecture. This is bounded negative evidence, not a novelty certificate.

I also rechecked Yuyu Chen, Liyuan Lin and Ruodu Wang, *Universal Value-at-Risk superadditivity*, arXiv:2606.22884, submitted 22 June 2026. That paper introduces UVS/WUVS as vector properties and proves preservation/results for several heavy-tail families, including completely subscalable, super-Cauchy and inverted-subadditive risks. The current search did not locate in it or a later paper a theorem establishing WUVS for standard-Pareto margins with an arbitrary positive Gaussian copula.

No competing repository owner was found for this exact Chen--Wang Gaussian conjecture. No new successor was claimed in this run.

The frozen metric is

\[
p_{\rm cert}:=\inf\Bigl\{p_0:\Pr(M_r^{\mathbf w}(U)\le p)\ge p
\text{ for every }p\in[p_0,1),\ n,\mathbf w,R,\ r\le-1\Bigr\},
\]

where `R` ranges over the source-admissible positive-correlation Gaussian correlation matrices. It enters and leaves this run at `1/2`.

## Idea before calculation

The previous run showed that another bivariate boundary lemma cannot move an all-dimensional metric. I therefore used the three reserved moves to attack the genuinely high-dimensional interior statement from three different directions:

- B1: discard p-value language and work entirely with Pareto risks and WUVS;
- B3: seek a stronger all-dimensional Gaussian convexity/semigroup statement whose one-dimensional consequence could force WUVS;
- B26: if that structural route stops short, actively hunt genuinely high-dimensional positive-correlation covariance geometries rather than the already-constrained equicorrelated/one-factor families.

The strongest new outcome is an exact one-dimensional Ehrhard-profile reduction valid in every dimension. It does not by itself move `p_cert`, so the six-run retirement rule still applies.

## B1 — CHANGE THE CATEGORY: the source conjecture is exactly Pareto WUVS

Set

\[
L_i=\frac1{U_i}=\frac1{\Phi(X_i)}.
\]

Each `L_i` is standard Pareto on `[1,\infty)`:

\[
\Pr(L_i>t)=\frac1t,\qquad t\ge1.
\]

For the harmonic mean

\[
H_{\mathbf w}=\left(\sum_i w_iL_i\right)^{-1},
\]

the desired subuniformity inequality is

\[
\Pr(H_{\mathbf w}\le p)\ge p
\quad\Longleftrightarrow\quad
\Pr\left(\sum_iw_iL_i\ge \frac1p\right)\ge p.
\]

If `L` is one standard Pareto variable, then

\[
\Pr(L\ge 1/p)=p,
\]

so the source conjecture is exactly

\[
\boxed{L\ \preceq_{\rm st}\ \sum_iw_iL_i\qquad\text{for every }\mathbf w\in\Delta_n.}
\]

Equivalently, the positive-Gaussian Pareto vector must have weighted universal Value-at-Risk superadditivity (WUVS). In a comonotone copy, `L_1=\cdots=L_n=L`, and its weighted sum equals `L`, so this is precisely stochastic dominance of the comonotone weighted sum by the actual Gaussian-copula weighted sum.

This translation is now the preferred handoff language. The 2026 WUVS framework confirms that it is the correct category, but its currently advertised preservation theorems do not supply the missing arbitrary-positive-Gaussian dependence theorem. In particular, results for independent heavy-tailed risks, negative lower-orthant dependence, or special common-shock/Archimedean constructions cannot be silently substituted for a general Gaussian copula with positive correlations.

### Why ordinary comonotone convex extremality is not enough

Let

\[
S_R=\sum_iw_i f(X_i),\qquad f(x)=\Phi(x)^{-1},
\]

and interpolate covariance matrices by

\[
R_t=(1-t)R+tJ,\qquad J=\mathbf1\mathbf1^T.
\]

For a smooth convex test function `\psi` for which the differentiation is justified, Gaussian interpolation gives

\[
\frac{d}{dt}\mathbb E\psi(S_{R_t})
=\frac12\sum_{i\ne j}(1-R_{ij})w_iw_j
\mathbb E\left[\psi''(S_{R_t})f'(X_i)f'(X_j)\right]\ge0,
\]

because `f'<0`. Truncation gives the same comparison for bounded convex tests such as `e^{-\lambda s}`. Thus the comonotone endpoint is extremal for this convex/Laplace-order family.

But this is the wrong order for the source. WUVS asks for **first-order stochastic dominance**, and the source itself stresses that comonotonicity does not generally maximize a sum's distribution function. The interpolation therefore diagnoses, rather than closes, the gap: every argument that uses only convex test functions has thrown away exactly the threshold information the conjecture needs.

## B3 — PROVE SOMETHING STRONGER: an all-dimensional Ehrhard-profile theorem

The new useful theorem is not a threshold estimate at one `p`; it is a global shape constraint on the whole reciprocal-sum distribution.

### Theorem (Ehrhard concavity of the reciprocal-sum Gaussian quantile profile)

Let `X\sim N(0,R)` with `R` a positive-definite correlation matrix; no sign condition on its off-diagonal entries is needed. Let `w_i>0`, `\sum_iw_i=1`, and define

\[
S(X)=\sum_{i=1}^n\frac{w_i}{\Phi(X_i)},
\qquad
V(X)=\log S(X).
\]

For `r>0`, put

\[
G_R(r)=\Pr\{V(X)\le r\},
\qquad
Q_R(r)=\Phi^{-1}(G_R(r)).
\]

Then

\[
\boxed{Q_R(r)\text{ is concave on }(0,\infty).}
\]

Equivalently, for all `r,s>0` and `\theta\in[0,1]`,

\[
\boxed{
Q_R(\theta r+(1-\theta)s)
\ge \theta Q_R(r)+(1-\theta)Q_R(s).
}
\]

The same conclusion extends to singular Gaussian limits whenever the sublevel probabilities are obtained by the corresponding weak limit; the source-relevant perfectly comonotone endpoint is explicit separately below.

### Proof

Write

\[
\ell(x)=-\log\Phi(x).
\]

Since `\log\Phi` is concave,

\[
\ell''(x)=\lambda(x)(x+\lambda(x))>0,
\qquad
\lambda(x)=\frac{\phi(x)}{\Phi(x)},
\]

where positivity for negative `x` is the strict Mills inequality. Hence every map `x_i\mapsto\ell(x_i)` is convex.

Now

\[
V(x)=\log\left(\sum_iw_i e^{\ell(x_i)}\right).
\]

The log-sum-exp function is convex and nondecreasing in each coordinate, so composition with the convex coordinate functions `\ell(x_i)` shows that `V` is convex on `\mathbb R^n`.

Let

\[
A_r=\{x:V(x)\le r\}.
\]

For `x\in A_r`, `y\in A_s`, convexity gives

\[
V(\theta x+(1-\theta)y)
\le \theta V(x)+(1-\theta)V(y)
\le \theta r+(1-\theta)s.
\]

Therefore

\[
\theta A_r+(1-\theta)A_s
\subseteq A_{\theta r+(1-\theta)s}.
\]

Choose an invertible `B` with `BB^T=R` and write `X=BZ`, `Z\sim N(0,I_n)`. The sets

\[
C_r=B^{-1}A_r=\{z:V(Bz)\le r\}
\]

are convex and satisfy the same Minkowski inclusion. Ehrhard's inequality for convex sets under standard Gaussian measure `\gamma_n` gives

\[
\Phi^{-1}\!\left(\gamma_n(\theta C_r+(1-\theta)C_s)\right)
\ge
\theta\Phi^{-1}(\gamma_n(C_r))
+(1-\theta)\Phi^{-1}(\gamma_n(C_s)).
\]

The Minkowski inclusion and monotonicity of `\Phi^{-1}` then imply

\[
Q_R(\theta r+(1-\theta)s)
\ge \theta Q_R(r)+(1-\theta)Q_R(s),
\]

as required. `\square`

### Exact reduction of the full conjecture to comparison of two concave profiles

Let

\[
F_R(t)=\Pr\{S(X)\le t\},\qquad t>1.
\]

Then `Q_R(r)=\Phi^{-1}(F_R(e^r))`. At the comonotone Gaussian endpoint `X_1=\cdots=X_n=Z`,

\[
S=\frac1{\Phi(Z)},
\]

and hence

\[
F_0(e^r)=1-e^{-r}.
\]

Define the explicit benchmark

\[
\boxed{Q_0(r)=\Phi^{-1}(1-e^{-r}).}
\]

The harmonic-mean source conjecture is now exactly

\[
\boxed{Q_R(r)\le Q_0(r)\qquad\text{for every }r>0,}
\]

because with `p=e^{-r}`,

\[
\Pr(H\le p)\ge p
\iff
F_R(e^r)\le1-e^{-r}.
\]

Thus an arbitrary-dimensional stochastic-order problem has been compressed to a one-dimensional comparison between two concave Gaussian-quantile profiles. R09's existing upper-half theorem proves this comparison on

\[
0<r\le \log2.
\]

What is missing is a global comparison principle that prevents `Q_R` from crossing above `Q_0` after `\log2`. Concavity of each profile separately is not enough: a difference of concave functions need not have a fixed sign or a one-crossing property. This is the cleanest remaining mathematical obligation found in this track.

I treat `Ehrhard inequality + log-sum-exp convexity` as classical machinery. I found no source in the bounded search packaging this exact reciprocal-Gaussian profile reduction, but publication priority for the packaging is **UNVERIFIED**.

### A second exact obstruction: the tangent halfspace changes sign at `p=1/2`

There is an especially transparent reason the most obvious convex-set proof stops exactly where the tracked metric currently stops. Fix `p`, write `z_p=\Phi^{-1}(p)`, and let

\[
A_p=\left\{x:\sum_i\frac{w_i}{\Phi(x_i)}\le \frac1p\right\}.
\]

The diagonal point `z_p\mathbf1` lies on `\partial A_p`. Convexity of `S` implies that the sublevel set lies in the supporting halfspace at that point:

\[
A_p\subseteq\{x:\mathbf w\cdot x\ge z_p\}.
\]

For `X\sim N(0,R)`, put `q=\mathbf w^TR\mathbf w\le1`. Hence

\[
\Pr(A_p)
\le
1-\Phi\left(\frac{z_p}{\sqrt q}\right).
\]

If `p<1/2`, then `z_p<0`, so `z_p/\sqrt q\le z_p` and therefore

\[
1-\Phi\left(\frac{z_p}{\sqrt q}\right)\ge1-p.
\]

The supporting halfspace gives an upper bound **weaker than the desired `1-p` bound** exactly below one half. Thus a proof based only on one supporting hyperplane cannot move `p_cert` below `1/2`; it needs curvature/global geometry of `A_p`.

This is a useful failure certificate for the route, not a source theorem.

## B26 — HUNT THE SPORADIC CASE: genuinely high-dimensional counterexample search

The previous reports had already heavily constrained bivariate, equicorrelated and near-comonotone cases. I therefore searched the negation in the region that could still plausibly evade those theorems: dimensions `3` through `6`, non-equicorrelated positive-definite correlation matrices with all pairwise correlations positive, including matrices not of a simple one-factor/equicorrelation form, and both diffuse and imbalanced interior weights.

The search used Gaussian-score coordinates with scrambled quasi-Monte-Carlo probes rather than naive direct quadrature. Apparent negative margins again occurred only at the numerical resolution boundary: extremely small `p`, covariance matrices extremely close to the comonotone face, or weights extremely close to a pure vertex. Those are precisely the singular faces where earlier R09 theorems prove a positive local margin but where its magnitude degenerates. Increasing resolution or moving to boundary-adapted coordinates removed the apparent violations encountered in this pass.

No candidate survived to a rigorously certifiable counterexample. Therefore:

- I do **not** call this a finite theorem;
- I do **not** create an exact checker or archive QMC output as if it were evidence of the conjecture;
- I do **not** change the source status from OPEN_CURRENT;
- I record only the methodological negative result: no easy moderate-dimensional interior sporadic counterexample was found in this bounded search.

If this target is reassigned later, any numerical attack should use interval-certified boundary-adapted coordinates before a candidate is promoted.

## Six-run disposition

The fixed fleet metric did not move:

\[
\boxed{p_{\rm cert}:\frac12\longrightarrow\frac12.}
\]

Supported unchanged count:

\[
\boxed{5\longrightarrow6.}
\]

Status of the source: **OPEN_CURRENT**.

Status of R09's contribution: **PARTIAL / HANDOFF_READY**.

Operational disposition: **RETIRE `CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM` from active R09 hourly research under the six-unchanged-run CLOSABLE rule.** This retirement is operational, not a claim that the conjecture is solved or false.

The handoff preserves the following source-relevant results/routes:

1. `p>=1/2` in every dimension, every weight, and every Gaussian covariance (indeed no positive-correlation assumption needed for that theorem);
2. strict all-dimensional first variation away from the comonotone covariance face;
3. fixed-correlation bivariate low-`p` positivity;
4. rigorous compact-interior Huesler--Reiss second-order positivity in the singular `1-rho ~ 1/log(1/p)` transition;
5. strict local positivity at every pure-weight simplex vertex in all dimensions via the OU semigroup;
6. log-concavity/moment constraints from the preceding run;
7. this run's exact Pareto/WUVS reformulation and all-dimensional Ehrhard-profile concavity/reduction;
8. the precise remaining obstruction: prove `Q_R(r)<=Q_0(r)` for all `r>log2`, or find a certified genuinely high-dimensional counterexample.

The most promising future route is no longer another local expansion. It is a **one-dimensional crossing/curvature theorem for the Ehrhard profile** `Q_R`, possibly using more than concavity (Gaussian perimeter, second variation, or a monotonicity formula) together with the exact benchmark `Q_0`.

## Rotation / successor gate

I checked the current queue/ownership state before taking a successor. The current queue itself still distinguishes PENDING candidates from READY assignments, and recent lane-level admission screening found no free `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor. More recent queue-tail work likewise records that the current famous finite tail is exhausted by canonical claims or a resolved item rather than furnishing a free successor. In particular, attractive-looking stale rows such as I0011 are already exclusively claimed by another owner.

Accordingly I did **not** steal a claimed source, promote a PENDING row to READY, relabel a HARD target as CLOSABLE, or create a speculative claim. R09 now enters a **CLOSABLE successor-admission gate**. The next lawful R09 invocation should screen a genuinely different outside source through the complete source/current-literature/prior-attempt/ownership gate; it must not resume this retired Chen--Wang target merely because no successor is immediately available.

## Model / scheduler control status

The exposed task-management surface still has no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. It exposes prompt/title/schedule/timing/enabled-state controls, so `GPT-6 / maximum` remains a request in prompt text only. The actual model identity available to this report is GPT-5.6 Sol; the reasoning level is UNVERIFIED. No model/reasoning setting was falsely claimed.

The historical P26 `You cannot modify this task` response is an authorization-context issue. The lawful remedies are to operate from the owning authorized context, transfer/administer ownership through an authorized interface, or use platform support. Creating a duplicate job or bypassing permissions is not a valid workaround. No scheduler or permission change was attempted in this run.

## Bookkeeping

No checker-only artifact was created because the promoted result is an analytic theorem with a complete proof on this page and there is no finite core. The exploratory B26 search produced no certified finite claim. No shared root, peer file, email, Drive file, public post, workflow, permission, purchase, or scheduler state was changed.

```yaml
ledger_delta:
  track: R09
  active_claim_before: CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM
  source_status: OPEN_CURRENT
  result_status: PARTIAL_HANDOFF_READY
  operational_status_after: RETIRED_FROM_ACTIVE_R09_SIX_UNCHANGED
  metric_name: p_cert
  metric_before: 1/2
  metric_after: 1/2
  movement: no_movement
  supported_unchanged_before: 5
  supported_unchanged_after: 6
  methods_used: [B1, B3, B26]
  new_results:
    - name: exact Pareto_WUVS reformulation
      statement: "L <=_st sum_i w_i L_i for standard-Pareto L_i=1/Phi(X_i)"
      scope: source-equivalent harmonic formulation
    - name: Ehrhard reciprocal_sum profile concavity
      statement: "Q_R(r)=Phi^{-1}(P(log(sum_i w_i/Phi(X_i))<=r)) is concave in r"
      scope: all dimensions; positive-definite Gaussian covariance; no correlation-sign assumption
    - name: source reduction to benchmark profile
      statement: "full conjecture iff Q_R(r)<=Phi^{-1}(1-exp(-r)) for every r>0"
      scope: harmonic mean; r<=-1 follows by power-mean monotonicity
  counterexample_search: no_candidate_promoted
  prior_art_status: classical_Ehrhard_and_WUVS_machinery_packaging_priority_unverified
  successor_state: CLOSABLE_ADMISSION_GATE
  tang_q411_periodic_tree: RETIRED_REFUTED
  g0013: RETIRED_HANDOFF_READY
```
