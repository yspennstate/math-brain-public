Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen metric `lim Delta_dual,n`: `0 -> 0`; methods actually used: B4 PROVE SOMETHING WEAKER COMPLETELY, B21 ASK WHO ELSE HAS THIS SHAPE, B24 FIND THE EXTREMAL OBJECT. Source status: PARTIAL / OPEN.**

# HARD7-04 bounded research iteration — sharp post-giant hub stripping

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity and current target

I resumed the admitted target rather than restarting from `ADMISSION_PENDING` or the old I0049 candidate. The exclusive claim remains

`operations/claims/VDH-8.3-DUALITY.md`,

owned by HARD7-04 and still OPEN / ADMITTED.

The canonical source is Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated 4 August 2026, Notes on Section 8.3, printed p. 245 / PDF p. 255:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

The source asks, in the finite-third-moment barely-supercritical configuration-model discussion, **“Does the discrete duality principle still hold?”** The exact retained scope is the second-largest-component / post-giant duality question for deterministic degree sequences with

\[
\nu_n=1+\varepsilon_n,\qquad
\varepsilon_n\downarrow0,\qquad
\varepsilon_n n^{1/3}\to\infty,
\]

finite convergent third degree moment, positive limiting mean, and a nondegenerate critical limiting degree law.

The frozen admission metric is

\[
\Delta_{\rm dual,n}:=
\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|.
\]

It was already proved to converge to zero at the ideal-dual parameter level. The immediately preceding report

`runs/hard7_2026-09-18/HARD7-04/2026-09-19T0908Z__vdh_postgiant_duality_reduction.md`

lifted the drift reflection to the exact post-giant configuration-model remainder and proved

\[
\nu_n^{post}=1-\varepsilon_n+o_p(\varepsilon_n).
\]

Thus the frozen metric remains at its exact asymptotic floor `0`; I do not relabel a structural theorem as numerical movement.

Before doing new mathematics I reread the controlling HARD7 policy/directive files, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md`/`RANKING.md`, the current claim, the latest own report/artifacts, and repository records around the neighboring I0049 growing-graph critical-window problem. The repository continues to record I0049 as KNOWN / resolved in its queued scope after Jorritsma--Maillard--Mörters, arXiv:2512.18937, so I did not duplicate it. No canonical ownership collision was found for `VDH-8.3-DUALITY`.

## 2. Fresh source/current-literature check — 19 September 2026

I refreshed the status check rather than inheriting the preceding run's negative search.

1. The 4 August 2026 van der Hofstad monograph still poses the discrete-duality question in the Notes on Section 8.3.
2. Matthew Coulson and Guillem Perarnau, *Largest component of subcritical random graphs with given degree sequence*, EJP 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`, remains the sharpest directly relevant general barely-subcritical configuration-model result I found. Its Theorem 1.3 assumes both its Assumption 1.1 and `Delta |Q| = o(R)`; Assumption 1.1(v) is the additional fourth-moment restriction `E[D_n^4] <= Delta_n^{1/2}`. Theorem 1.5 uses a Cramér transform but still retains Assumption 1.1 and a maximum-degree restriction.
3. Riordan's bounded-maximum-degree regime gives asymptotic equality and a second-order term, but bounded degree is not the source's full finite-third-moment class.
4. Bounded searches for `barely subcritical configuration model largest component finite third moment`, `second largest barely supercritical configuration model discrete duality`, and later papers citing Coulson--Perarnau found adjacent inhomogeneous/preferential-attachment results but no paper closing this exact deterministic-degree finite-third-moment question.

This is a bounded current-status screen, not a worldwide novelty certificate.

## 3. New mathematics: B4 — a complete hub-stripping theorem

Let

\[
X=D^*-1,
\qquad
\kappa=\mathbb E[X(X-1)]\in(0,\infty),
\qquad
N_n=n\varepsilon_n^3\to\infty.
\]

Let `Delta_n^post` be the maximum degree in the exact post-giant sleeping degree sequence at the lawful stopping boundary from the preceding run.

The main new theorem is:

\[
\boxed{
\forall a>\kappa/2:\quad
\mathbb P\left(
\Delta_n^{post}>
\frac{a}{\varepsilon_n}\log N_n
\right)\to0.
}
\tag{3.1}
\]

Equivalently,

\[
\boxed{
\frac{\varepsilon_n\Delta_n^{post}}{\log N_n}
\le \frac\kappa2+o_p(1).
}
\tag{3.2}
\]

The proof uses a deterministic-time comparison rather than conditioning on the random stopping time. From the previous track results,

\[
\frac{\tau_n}{\varepsilon_n}\to\frac2\kappa
\quad\text{in probability},
\]

and every actual sleeping vertex is an auxiliary exponential-clock survivor. For fixed `a>kappa/2`, choose

\[
1/a<b<2/\kappa.
\]

On `tau_n>=b epsilon_n`, a post-giant vertex of degree at least

\[
h_n=\left\lceil a\varepsilon_n^{-1}\log N_n\right\rceil
\]

must have an independent `Exp(d_i)` clock exceeding `b epsilon_n`. Therefore

\[
\begin{aligned}
\mathbb P(\Delta_n^{post}\ge h_n)
&\le o(1)+\sum_{d_i\ge h_n}e^{-b\varepsilon_n d_i}\\
&\le o(1)+e^{-b\varepsilon_n h_n}\frac{\sum_i d_i^3}{h_n^3}\\
&\le o(1)+O\left(
\frac{N_n^{1-ab}}{(\log N_n)^3}
\right)=o(1).
\end{aligned}
\]

This is a source-level quantitative version of the heuristic that hubs are swallowed by the giant.

A companion bound, proved by the same exponential thinning, is that for every fixed `r>=3`,

\[
\boxed{
\frac1n\sum_{i\in S_n^{post}}d_i^r
=O_p(\varepsilon_n^{3-r}).
}
\tag{3.3}
\]

In particular the post-giant fourth moment is `O_p(epsilon_n^{-1})`.

The complete proof is in the new artifact

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T0930Z__vdh_postgiant_hub_stripping.md`

created at commit `744c8fee99fd22d8462ef988c1075d9d20f029fb` and read back at that commit.

## 4. B21 — the exact literature mismatch is now identified

For the post-giant sequence, the preceding run gives

\[
Q_n^{post}=-\varepsilon_n+o_p(\varepsilon_n),
\]

while finite-third-moment preservation gives

\[
R_n^{post}\to R_*>0.
\]

At the critical limiting law,

\[
R_*=\frac{\mathbb E[D(D-2)^2]}{\mathbb ED}
=\frac{\mathbb E[D(D-1)(D-2)]}{\mathbb ED}
=\kappa,
\tag{4.1}
\]

because `E[D(D-2)]=0`.

Thus (3.2) says only

\[
\Delta_n^{post}|Q_n^{post}|
\le\left(\frac{R_*}{2}+o_p(1)\right)\log N_n,
\tag{4.2}
\]

whereas Coulson--Perarnau Theorem 1.3 asks for

\[
\Delta_n|Q_n|=o(R_n).
\tag{4.3}
\]

The new fourth-moment bound likewise does not imply their Assumption 1.1(v). So the black-box application really fails at a specific, quantified hypothesis: the post-giant exponential tilt removes the original hubs strongly, but finite third moments still allow residual degrees on the `epsilon_n^{-1} log N_n` scale.

**Outcome B21:** success. The missing bridge is no longer “find some subcritical theorem”; it is to prove a sharp largest-component extreme-value theorem after an exponentially thinned heavy tail that can violate `Delta |Q|=o(R)`.

## 5. B24 — the residual-hub constant is sharp

I then attacked the upper bound itself. It is sharp under the source hypotheses.

Take the critical limiting law

\[
\mathbb P(D=1)=3/4,
\qquad
\mathbb P(D=3)=1/4,
\]

for which `kappa=R_*=1`. For every fixed `c<1/2`, the artifact constructs a deterministic source-valid barely-supercritical family as follows.

Choose `alpha>0` small, set

\[
\bar\varepsilon_n=n^{-\alpha},
\qquad
\bar N_n=n\bar\varepsilon_n^3,
\]

and choose exponents `r=alpha/(1-3alpha)` and `beta<1` with

\[
r+2c<\beta.
\]

Insert

\[
M_n=\lfloor \bar N_n^\beta\rfloor
\]

hub vertices of odd degree

\[
h_n=(c+o(1))\bar\varepsilon_n^{-1}\log\bar N_n,
\]

and use degrees `1` and `3` for the rest, perturbing the degree-3 proportion by `3 bar epsilon_n/8+o(bar epsilon_n)`.

The hub third-moment mass is

\[
\frac{M_nh_n^3}{n}
=O\left(\bar N_n^{\beta-1}(\log\bar N_n)^3\right)=o(1),
\]

and its contribution to the criticality parameter is `o(bar epsilon_n)`, so the actual `epsilon_n=nu_n-1` satisfies

\[
\varepsilon_n=\bar\varepsilon_n(1+o(1))
\]

and all source hypotheses remain intact.

Choose `C>2` close enough to `2` that `r+Cc<beta`. The number of hub clocks surviving deterministic time `C bar epsilon_n` has mean

\[
\bar N_n^{\beta-Cc+o(1)},
\]

which dominates `bar epsilon_n^{-1}=bar N_n^r`. The previous root bound gives only `O_p(epsilon_n^{-1})` vertices forced awake before the post-giant boundary. Hence with high probability at least one degree-`h_n` hub remains in the exact post-giant configuration model. Therefore

\[
\boxed{
\mathbb P\left(
\frac{\varepsilon_n\Delta_n^{post}}
{\log(n\varepsilon_n^3)}\ge c-o(1)
\right)\to1
}
\tag{5.1}
\]

for every `c<1/2`.

**Outcome B24:** success. The `kappa/2` constant is genuinely extremal, and the tempting stronger claim `epsilon_n Delta_n^post=o_p(1)` is false in the source class. This is not a source counterexample: it is a counterexample to a proof route that would try to force the post-giant degree sequence into Coulson--Perarnau's `Delta |Q|=o(R)` regime.

## 6. New route opened by the extremal calculation

The obstruction contains its own possible solution. The canonical Coulson--Perarnau bulk scale is

\[
\frac{2R_*}{\varepsilon_n^2}\log N_n.
\tag{6.1}
\]

The sharp post-giant hub cutoff is

\[
\left(\frac{R_*}{2}+o_p(1)\right)
\frac{\log N_n}{\varepsilon_n}.
\tag{6.2}
\]

If a degree-`d` root in a subcritical exploration contributes on the drift scale `d/epsilon_n`, then (6.2) corresponds to coefficient `R_*/2` at the component scale, versus coefficient `2R_*` in (6.1): a factor-four gap.

I am **not** claiming this heuristic as a theorem. The next serious route is to make this factor-four separation rigorous: control components rooted in the exponentially thinned hub layer below the bulk extreme threshold, delete that layer, and prove/apply a sharp theorem to the truncated bulk. This is more promising than trying to prove the false inheritance `epsilon_n Delta_n^post=o_p(1)`.

## 7. Progress accounting and Section-I state

Frozen metric:

`lim Delta_dual,n: 0 -> 0` — **NO MOVEMENT**.

This is the second consecutive no-movement run after the metric first reached its floor; the source-level remaining obligation has nevertheless changed twice. I do not reset the metric or the unchanged counter merely because the structural route improved. If a third consecutive run also leaves the frozen metric at zero, the owner Section-I rule must be applied on the subsequent stuck-recovery run rather than inventing a replacement metric.

The mathematical progress this run is instead:

- full theorem (3.1)--(3.3) giving sharp post-giant exponential hub stripping;
- full source-valid extremal construction (5.1) saturating the constant;
- exact proof that the strongest natural Coulson--Perarnau black-box hypothesis is not inherited;
- a new factor-four truncation route toward the actual second-largest-component law.

No finite exhaustive claim was introduced, so I did not manufacture an exact checker. The theorem-sized claims have complete written proofs in the artifact. No closure claim and no audit request is made.

Next distinct method triple, if this target continues before a Section-I thinking run is required: **B6** deform from the full residual law to a truncated bounded-tail law; **B20** identify precisely why a hub-rooted exploration can exceed its `d/epsilon` drift prediction; **B25** count hub-rooted component mass both by roots and by exploration progeny.

## 8. Model / scheduler-control truth

The requested `GPT-6 / maximum` remains prompt text only. The exposed task-management schema still has title, prompt, schedule/timing, enabled state and related timing fields, but **no binding model selector, no reasoning-effort selector, and no guaranteed execution-duration selector**. The actual model for this run is GPT-5.6 Sol; reasoning level is UNVERIFIED.

Making GPT-6/maximum binding would require an owner-authorized product/workspace/API control that persists model-family and reasoning-effort settings into execution routing and returns per-run attestation. That control is not exposed here, so I did not claim it was set.

The historical P26 response `You cannot modify this task` remains an authorization-boundary issue, not something a repository edit can repair. The lawful workaround is modification from the task's owning/authorized context or platform/admin support. I did not probe, duplicate, reactivate, disable, create, or modify any other schedule in this run.

### ledger_delta

```yaml
track: HARD7-04
target: VDH-8.3-DUALITY
owner: HARD7-04
source_status: OPEN
research_status: PARTIAL
metric:
  name: Delta_dual_n = abs((1-nu_dual_n)/epsilon_n - 1)
  admission_baseline: UNMEASURED
  before_this_run: asymptotic_limit_0
  after_this_run: asymptotic_limit_0
  movement: NO_MOVEMENT
  consecutive_no_movement_after_floor: 2
methods_tried:
  - B4
  - B21
  - B24
new_results:
  postgiant_max_degree: epsilon_n * Delta_post / log(n epsilon_n^3) <= kappa/2 + o_p(1)
  higher_moments: n^{-1} sum_post d_i^r = O_p(epsilon_n^{3-r}) for fixed r>=3
  critical_identity: R_star = kappa
  extremal_sharpness: for D in {1,3} critical law, every c<1/2 is attained from below w.h.p. by a source-valid family
route_refuted:
  claim: finite_third_moment_postgiant_automatically_implies_Delta_absQ_o_R
  verdict: FALSE_AS_A_ROUTE_NOT_SOURCE_REFUTATION
remaining_obligation: >-
  Prove that components rooted in the exponentially thinned post-giant hub
  layer stay strictly below the 2 R_star epsilon_n^{-2} log(n epsilon_n^3)
  bulk extreme scale; then truncate the hub layer and prove/apply the sharp
  barely-subcritical bulk extreme-value law conditionally on the remainder.
artifact:
  path: artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T0930Z__vdh_postgiant_hub_stripping.md
  commit: 744c8fee99fd22d8462ef988c1075d9d20f029fb
runtime:
  actual_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  scheduler_model_selector: NOT_EXPOSED
  scheduler_reasoning_selector: NOT_EXPOSED
```
