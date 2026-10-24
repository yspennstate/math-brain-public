Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry proving GPT-6/maximum, so I do not claim otherwise. **I0082 remains RETIRED/FROZEN at `2/3` with retirement count `6`; successor movement this run: `D0016 d=2 residual` moved from unowned historical-partial to `ADMITTED_ACTIVE`, with its new frozen closure metric moving `0/2 -> 1/2`. Methods actually used: #1 CHANGE THE CATEGORY, #3 PROVE SOMETHING STRONGER, #7 TAKE THE LIMIT.**

# R08 CLOSABLE OUTSIDE — D0016 admitted: Brownian-sheet exceptional slice with infinitely many zeros

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity: I0082 stays retired

I continued from `runs/R08/20260917T0528Z_rotation_screen_d0011_6b8c3a.md`. I did **not** reopen Hasebe--Ueda Problem 3.11 after the mandatory six-unchanged-run retirement. Its frozen explicit-candidate metric remains `2/3`; C005/C006 remain the strongest preserved package and still need the two independent end-to-end audits required by the owner policy.

The active obligation was successor admission. The newest coordinator screen still had no pre-certified READY successor, so I continued beyond already-consumed queue rows rather than resetting I0082 or fabricating a finite surrogate for a HARD target.

## 2. Required repository recovery

Before the new research I recovered/read or exact-searched:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- stale canonical `operations/claims/I0082.md` together with the later controlling R08 six-run handoff lineage;
- newest own R08 report `runs/R08/20260917T0528Z_rotation_screen_d0011_6b8c3a.md`;
- newest neighboring R09 report `runs/R09/20260917T0535Z_rotation_i0033_resolution_i0036_hard_91c7e2.md` (admission-only; no new theorem package to audit);
- newest visible task-health successor screen `operations/task_health/runs/2026-09-17T054658Z/queue_screening.md`;
- exact D0016 intake row and the campaign correction for D0016.

The historical correction is important: the old first-moment count is calibrated, but in `d=2` it is only heuristic. It gives

`E(k)=k(d-2)-2=-2`

for every finite `k`, suggesting that arbitrarily high finite common-zero multiplicity has no first-moment codimension cost. The correction explicitly says that the `d=2` half still needs a second-moment/capacity argument **uniform in k** plus a limsup passage. I preserve that status rather than promoting the heuristic.

## 3. Exact source and current-literature check

Source: Davar Khoshnevisan, *Slices of Brownian Sheet: New Results, and Open Problems*, Open Problem 1, Section 8.1.

The exact source asks, for a two-parameter Brownian sheet `B` in `R^d`, `d in {2,3}`, whether outside one null set

`B^{-1}{0} intersect ({s} x (0,infinity))`

is finite for **every** `s>0`. Khoshnevisan conjectures the answer is no and even suggests that an exceptional slice may carry positive Hausdorff measure for a gauge tending to infinity.

The campaign already has a corrected `d=3` argument: three or more common slice zeros are strictly subcritical in the calibrated box count, so the `d=3` fiber is finite. I do not reopen it. The exact residual claimed here is **d=2 only**.

Fresh bounded 2026-09-17 searches used the exact source title/problem wording, `exceptional slices`, `finite slice zero set`, and later Brownian-sheet zero-set papers. I found no paper stating a resolution of Open Problem 1. The most relevant recent primary paper is:

- Keming Chen and Guillaume Woessner, *Zeros of the Brownian Sheet*, J. Theor. Probab. 38 (2025), Article 33, DOI `10.1007/s10959-024-01399-1`, arXiv:2405.20019.

That paper explicitly says it answers **Khoshnevisan Open Problem 4** (the simultaneous projection-dimension problem), not Open Problem 1. Its literature discussion still treats low-dimensional exceptional zero-hitting slices via Wiener-space capacity. So it does not close D0016.

I also checked the canonical ownership path immediately before admission: `operations/claims/D0016.md` returned 404. Repository search recovered only the historical intake/correction/campaign attempt, not a current exclusive owner.

Hence the exact residual is source-recovered, current-open in this bounded dated search, and unowned.

## 4. Admission and frozen successor metric

I admitted the `d=2` residual as R08's new CLOSABLE target and created `operations/claims/D0016.md` at commit `f0b86e4422a59b415ea42226dbc492f64f4d82c1`.

The frozen metric is the number of these two obligations proved:

1. **Uniform finite-intersection estimate.** With `S=[1,2]` and the fixed disjoint compact intervals

   `J_j=[2-2^{-j}, 2-3*2^{-j-2}]`, `j>=1`,

   define

   `K_k={s in S : there exist t_j in J_j with B(s,t_j)=0 for every j<=k}`.

   Prove there is one `c>0`, independent of `k`, such that

   `P(K_k != empty) >= c` for every `k>=1`.

2. **Compactness bridge.** Prove that obligation 1 implies positive probability of a single vertical slice containing infinitely many distinct zeros, and hence refutes the source's almost-sure finiteness assertion.

Obligation 2 is proved below. Therefore the new source metric moves

`0/2 -> 1/2`.

Finite-k simulations, separate `c_k>0` with `c_k -> 0`, or arbitrarily large finite multiplicities at different slice parameters do **not** discharge obligation 1.

## 5. Method #7 — exact compactness bridge (proved)

This is the clean limit step the old campaign did not isolate.

For a fixed sample of the continuous Brownian sheet and each `k`, consider

`Z_k = {(s,t_1,...,t_k) in S x J_1 x ... x J_k : B(s,t_j)=0 for every j<=k}`.

`Z_k` is closed in a compact product, hence compact. Its projection to the `s` coordinate is exactly `K_k`, so `K_k` is compact. Also

`K_{k+1} subset K_k`.

Let `A_k={K_k != empty}`. Then `A_{k+1} subset A_k`. If obligation 1 holds, continuity of probability from above gives

`P(intersection_{k>=1} A_k) = lim_{k->infty} P(A_k) >= c > 0`.

On the event `intersection_k A_k`, the sets `(K_k)` are nested nonempty compact subsets of `S=[1,2]`. Cantor's intersection theorem gives an `s_* in intersection_k K_k`.

For each fixed `j`, because `s_* in K_j`, there is a `t_j in J_j` with `B(s_*,t_j)=0`. The intervals `J_j` are pairwise disjoint, so the `t_j` are distinct. They accumulate only at `2`. Consequently

`#{t>0 : B(s_*,t)=0} = infinity`.

Thus obligation 1 gives

`P(exists s in [1,2] with infinitely many positive-time zeros) >= c`.

That is already enough to answer the source question **NO**: the asserted event “outside one null set every slice is finite” cannot have probability one.

This proves obligation 2 completely. No zero-one upgrade is required for source refutation.

### A reusable deterministic formulation

The same argument is deterministic apart from the uniform probability bound: for any continuous `f:S x T -> R^m`, if one has nested nonempty projection sets obtained by forcing one zero in each of countably many pairwise-disjoint compact `t`-intervals, then compactness of `S` produces a single fiber with infinitely many zeros. This is the correct way to pass from finite multiplicity to infinite multiplicity; merely proving “for every k there exists some s_k with k zeros” is insufficient because the `s_k` can drift.

## 6. Method #3 — prove the stronger estimate that actually closes

The old first-moment exponent `E(k)=-2` for every finite `k` is encouraging but logically too weak. The source does not close from `P(A_k)>0` separately for every `k`; the probabilities can tend to zero.

The right stronger target is exactly

`inf_{k>=1} P(A_k) > 0`.

This is stronger than finite-k existence but is the strength that feeds the nested compactness argument. It also explains why the owner's “prove something stronger” move is productive here rather than decorative.

A natural analytic object is the zero local time of the `2k`-dimensional Gaussian field

`Phi_k(s,t_1,...,t_k)=(B(s,t_1),...,B(s,t_k))`

on `S x J_1 x ... x J_k`.

For ordered times, the one-coordinate covariance determinant is explicit:

`det Cov(B(s,t_1),...,B(s,t_k)) = s^k t_1 product_{j=2}^k (t_j-t_{j-1})`.

Because the two spatial coordinates are independent, the zero density is

`p_{Phi_k(s,t)}(0) = (2*pi)^{-k} / [s^k t_1 product_{j=2}^k (t_j-t_{j-1})]`.

So the first moment is completely explicit. The actual remaining issue is a **uniform Paley--Zygmund/capacity ratio in k**, not whether the finite-dimensional density exists. This is the precise analytic obstruction for the next run.

I do not claim the needed uniform second-moment bound here.

## 7. Method #1 — change category to Wiener-space capacity

Write, for `u in R`,

`U(u,t)=e^{-u/2} B(e^u,t)`.

Then `u -> U(u,.)` is the stationary Ornstein--Uhlenbeck process on planar Wiener space; each fixed `u` has the law of standard planar Brownian motion in `t`. Positive scalar multiplication does not change zeros. Therefore the `d=2` residual can be restated exactly as a Wiener-space hitting question:

> Does the OU trajectory hit the null set of planar Brownian paths whose zero level set contains infinitely many positive times?

The source's one-zero exceptional-slice theory is already capacity-theoretic. The useful change is that the desired source counterexample is **not** “a typical planar Brownian path returns to zero” (it does not); it is “the Wiener-space OU path hits a measure-zero but potentially positive-capacity set of atypical paths.”

This formulation also warns against a false proof: fixed-slice Brownian recurrence to neighborhoods does not imply point returns.

## 8. A solved limit model: additive planar Brownian motion really has the infinite-fiber mechanism

There is a strong piece of evidence that did not appear in the old D0016 attempt.

Let `W_1,W_2` be independent planar Brownian motions and consider the additive field

`A(u,v)=W_1(u)-W_2(v)`.

Then with positive probability there exists `u` for which

`{v : A(u,v)=0}`

is infinite.

Reason: planar Brownian motion has points of **infinite multiplicity**. More strongly, Aidekon--Hu--Shi construct random measures supported on infinite-multiplicity points having Hausdorff dimension `2-alpha` for every `0<alpha<2`:

- E. Aidekon, Y. Hu, Z. Shi, *Points of infinite multiplicity of planar Brownian motion: measures and local times*, Ann. Probab. 48 (2020), 1785--1825, arXiv:1809.07094.

Fix an `alpha<2`. Conditional on `W_2`, its infinite-multiplicity set therefore contains a nonpolar compact subset (positive Hausdorff dimension implies positive logarithmic capacity in the plane). An independent planar Brownian motion `W_1` hits a nonpolar compact set with positive probability. At a hit `W_1(u)=x` where `x` is an infinite-multiplicity point of `W_2`, there are infinitely many `v` with `W_2(v)=x`, hence infinitely many zeros of `A(u,.)`.

I label this as a **solved comparison model / likely folklore consequence**, not as source closure and not as a novelty claim.

Why it is relevant is the exact local rectangular decomposition of the Brownian sheet. Around deterministic `(s_0,t_0)` and for `u,v>=0`,

`eps^{-1/2}[B(s_0+eps u,t_0+eps v)-B(s_0,t_0)]`

has the same law as

`sqrt(t_0) W_1(u) + sqrt(s_0) W_2(v) + sqrt(eps) W_3(u,v)`,

where `W_1,W_2` are independent planar Brownian motions and `W_3` is an independent planar Brownian sheet. Thus the small-scale tangent field is exactly additive Brownian motion, and the corner-sheet perturbation is lower order.

The missing transfer is subtle: “a vertical fiber has infinitely many exact point hits” is not an open event under uniform perturbation, so convergence to the additive tangent field does **not** by itself prove D0016. But it identifies a concrete mechanism and suggests importing the infinite-multiplicity random measures/capacity estimates rather than continuing the old first-moment box count.

## 9. What moved and what did not

Moved:

- successor admission: D0016 `d=2` is now the active exact-source R08 target;
- ownership: canonical R08 claim created;
- frozen successor metric: `0/2 -> 1/2`;
- the finite-to-infinite passage is now a complete compactness lemma;
- a solved additive tangent model exhibiting the desired infinite-fiber phenomenon is identified.

Did not move:

- the hard source obligation remains the universal uniform lower bound `inf_k P(A_k)>0` (or an equivalent positive-capacity theorem);
- no current-literature novelty certificate is claimed beyond the bounded dated search;
- I0082 remains retired and unchanged.

The next research run should **not** re-prove the compactness lemma or rerun finite-k box counts. It should attack the uniform estimate by one of: (i) a k-uniform second-moment estimate for the local time of `Phi_k`; (ii) a Wiener-space capacity lower bound for the infinite-zero path set using infinite-multiplicity measures; or (iii) a perturbative transfer from the additive tangent field that is formulated in a capacity topology strong enough to survive the `sqrt(eps) W_3` term.

Suggested next Section-B moves: #11 DUALIZE (capacity/energy), #13 FIND WHAT ONLY INCREASES (nested capacities), #29 ADD THE POINTS AT INFINITY (compactify the zero-time accumulation).

## 10. Neighboring-track check

The newest R09 report is a successor-admission screen (I0033 resolved; I0036 hard SAW/SLE) and introduces no finite or theorem-sized mathematical package requiring an R08 independent audit. I therefore did not manufacture a checker-only audit.

## 11. Model/reasoning and task-permission status

The model-control limitation is unchanged. The exposed scheduler/task schema provides title/prompt/schedule/timing/enabled controls but no model-family field, no reasoning-effort field, and no authenticated completed-run telemetry. Actually forcing and verifying GPT-6/maximum requires product/API support or an authorized owning workspace that exposes those controls plus runtime metadata.

The earlier `You cannot modify this task` result for P26 is an ownership/context boundary, not evidence that repository text can change runtime settings. The root ledger records that P26 was later updateable from a different authorized context. The legitimate workaround is the owning context, ownership transfer/admin intervention, or platform support—not a duplicate task. No scheduler mutation was attempted here.

## 12. Prohibited-action audit

No email/Gmail, Drive write, public posting, purchase, permission change, workflow execution, scheduler mutation, force-push, peer-track edit, or shared-root ledger edit was performed. No finite-arithmetic checker was created because the new claim is theorem-sized and proved on the page; the additive comparison result is literature-backed and explicitly not claimed as novel.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  run_id: 20260917T0625Z_rotation_admit_d0016_compactness_additive_4e7a2c
  retired_predecessor:
    problem: I0082
    source: Hasebe-Ueda arXiv:1710.08240v2 Problem 3.11
    metric_before: 2/3
    metric_after: 2/3
    retirement_count: 6
    state: RETIRED_FROZEN_AUDIT_PENDING
  methods_this_run: [1, 3, 7]
  successor:
    problem: D0016
    source: Khoshnevisan Open Problem 1 Section 8.1
    scope: d=2 residual only
    ownership: R08
    claim_commit: f0b86e4422a59b415ea42226dbc492f64f4d82c1
    current_status: OPEN_CURRENT_BOUNDED_2026_09_17_SEARCH
    metric_name: number_of_two_frozen_D0016_closure_obligations
    before: 0/2
    after: 1/2
    proved_this_run:
      - nested_compactness_bridge_from_uniform_finite_intersection_bound_to_one_infinite_zero_slice
    remaining_obligation: >-
      prove c>0 independent of k such that P(K_k nonempty)>=c for all k,
      or an equivalent positive-capacity theorem that yields the same source-level counterexample
    comparison_model: >-
      additive planar Brownian field has a vertical infinite-zero fiber with positive probability,
      via planar Brownian infinite-multiplicity points and logarithmic capacity
    state: ADMITTED_ACTIVE_PARTIAL
  overall: ACTIVE_D0016_1_OF_2
  new_exact_artifact: NONE_THEOREM_SIZED_PROOF_ON_PAGE
```
