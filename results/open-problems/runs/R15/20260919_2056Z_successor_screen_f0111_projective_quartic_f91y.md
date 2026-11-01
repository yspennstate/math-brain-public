Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: no surviving frozen counterexample candidate, so `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`; status `OPEN / PARTIAL / RETIRED-HANDOFF`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, a new projective fourth-order necessary condition is proved for every Hessian-null exact contact and it exactly eliminates the earlier `n=4` locally feasible null candidate without using a special coordinate-face test. Methods #5, #11, #24.**

# R15 retained screen — projective fourth-order tangent obstruction

Date checked: 2026-09-19 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`. Everything newly proved below on F0111 is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen I0076, make F0111 READY, establish novelty, solve Talagrand Problem 10.9, or satisfy closure/audit requirements.

## 1. Source fidelity, lifecycle and ownership

I continued from `runs/R15/20260919_2018Z_successor_screen_f0111_allray_radial_e90x.md`, rather than restarting. I reread the current INDEX/RANKING, root POSTED/RESULTS/QUEUE, the latest R15 report, the controlling I0076 six-run handoff, current admissions/claims, and neighboring R14/R17 state.

Burdzy--Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Definition 2.1 and Problem 7.2 were rechecked. FBM uses random origins `S_n -> -infinity` whose centered futures are standard Brownian motions; BBM is the time-reversed notion; 2BM requires one random origin at which the complete centered past and future are independent standard Brownian motions. Problem 7.2 assumes only FBM + BBM and independence of the two complete centered half-processes at an arbitrary random `T`; it does not assume `T` is a stopping time and does not separately assume either half at `T` is Brownian. Problem 7.5 remains excluded.

The six-run handoff remains controlling. The source-Theorem-6.1 candidate has FBM, BBM and non-2BM but no source-valid independent real seam; the later Brownian-prefix/BES independent-seam candidate was proved to be 2BM. Hence no frozen counterexample candidate survives, so the requested four-obligation candidate metric is not honestly scoreable. Historical `2/4` is only the retired positive-route handoff metric.

Current successor state was rechecked. P0459 is now an admitted READY/CLOSABLE OUTSIDE target, but it is already exclusively claimed by native CLOSABLE slot `6aa7b517489c8191a5250c9384e9b33c`. It is not free for R15. I did not steal it or promote a PENDING row. Thus there is still no lawful newly free CLOSABLE successor visible to this worker in the bounded dispatch check.

Fresh dated 2026-09-19 searches for exact Problem 7.2/title/authors again found the source and related splitting/pasting work but no accessible later primary source explicitly claiming the exact Problem 7.2 resolution. This is bounded negative evidence only.

## 2. Section-B moves and idea-first order

The preceding run used #18/#20/#27. All 30 moves have already appeared somewhere in the long F0111 retained-screen history, so I do not falsely claim globally unused move numbers. This run uses a different triple in new roles:

- **#5 ADD A PARAMETER AND DIFFERENTIATE** — bend a Hessian-null line by an `epsilon^2 v` correction;
- **#11 DUALIZE** — minimize the fourth-order coefficient over the bend vector via the PSD Hessian / Moore--Penrose inverse;
- **#24 FIND THE EXTREMAL OBJECT** — choose the bend that makes the fourth-order constraint sharp, and in particular the radial bend `v=cq`.

The research idea was written before the checker at `artifacts/R15/f0111_projective_quartic_idea_f91y.md`, commit `f01e49e5792c36e8ca4cfb8a5eec30ed050a13da`.

## 3. New theorem: projective fourth-order necessary condition

Let `G=P-F` be the gap of a quadratic global certificate at an interior exact contact `q`, so

`G(q)=0`, `grad G(q)=0`, `H:=D^2G(q)>=0`.

Suppose `h != 0` is a Hessian-null direction, `Hh=0`. Local nonnegativity on the straight line already forces

`D^3G(q)[h,h,h]=0`.

Now bend the path at second order:

`x(epsilon)=q+epsilon h+epsilon^2 v`.

Taylor expansion gives

`G(x(epsilon)) = epsilon^4 [ (1/2)<v,Hv> + (1/2)D^3G(q)[v,h,h] + (1/24)D^4G(q)[h,h,h,h] ] + O(epsilon^5)`.

Put `b(v)=D^3G(q)[v,h,h]`. Since the quartic coefficient must be nonnegative for every `v`, first `b` must annihilate `ker H`; otherwise taking `v=c k` with `k in ker H` and a suitable large signed `c` makes the coefficient negative. Thus `b` lies in `range H`. Minimizing the quadratic expression over `v` gives

`min_v { (1/2)<v,Hv> + (1/2)b(v) } = -(1/8) b^T H^+ b`,

so every Hessian-null exact global certificate necessarily satisfies

`boxed: D^4G(q)[h,h,h,h] >= 3 b^T H^+ b.`

This is stronger than the previous straight-line condition `D^4G[h^4]>=0`: a positive quartic term can still fail because a curved second-order escape direction lowers the gap.

Generic higher-order tangent/degenerate optimality conditions are established in the optimization literature, so I do **not** claim the abstract mechanism itself is new. The value here is its explicit certificate-free specialization to this F0111 hazard and its interaction with the previous all-ray theorem.

## 4. Certificate-free radial specialization

For the `k=2` hazard

`F(t)=sum_i t_i-log S(t)`, `S(t)=sum_i exp(t_i)-(n-1)`,

all derivatives of order at least three of `G=P-F` equal those of `log S`, because `P` is quadratic. Let

`L(t)=log S(t)`.

Choose only bends `v=cq`. The preceding all-ray theorem gives

`q^T H q = -g_q''(1) = K(q) > 0`,

where `g_q(s)=F(sq)/s` and, with `r_i=exp(q_i)/S(q)`,

`K(q)=2 log S(q)-2 sum_i r_i q_i + sum_i r_i q_i^2 - (sum_i r_i q_i)^2`.

Minimizing the quartic coefficient over the scalar `c` yields the completely certificate-free necessary condition

`boxed: D_h^4 L(q) K(q) >= 3 (D^3 L(q)[q,h,h])^2.`

Equivalently the projective margin

`Delta(q,h):=D_h^4 log S(q) K(q)-3(D^3 log S(q)[q,h,h])^2`

must be nonnegative at every Hessian-null exact contact of a global quadratic certificate.

For completeness, the identity `q^T Hq=K(q)` is immediate from radial exact contact. Write `P(sq)=As+Bs^2`, `f(s)=F(sq)=s g_q(s)`. Value/gradient contact at `s=1` gives `B=g_q'(1)`, hence the radial gap second derivative is

`2B-f''(1)=-g_q''(1)=K(q)`.

## 5. Exact elimination of the earlier locally feasible n=4 candidate

The earlier graph-flow report produced an exact local candidate

`q=(u,u,v,v)`,
`u=log(6909/6820)`, `v=log(12267/10540)`,
`S(q)=7848/5797`,
`h=(9/5,9/5,-1/5,-1/5)`.

It had positive coefficients, exact value/gradient contact, a full PSD contact Hessian with null vector `h`, exact cubic nullity and strict positive straight-line quartic. Its exact fourth log-partition derivative is

`D_h^4 log S(q)=3950752179/950480000 > 4`.

The new condition kills it much more strongly. Exact rational interval arithmetic, with logarithms bounded by the convergent atanh series and a rigorous rational tail remainder, certifies

`0.006 < K(q) < 0.007`,
`1.871 < D^3 log S(q)[q,h,h] < 1.873`,

and therefore

`boxed: Delta(q,h) < -10.`

So this locally feasible Hessian-null point cannot be a global quadratic certificate even before invoking the earlier special coordinate-face violation. The failure is a projective/curved-path fourth-order obstruction.

The checker is `artifacts/R15/f0111_projective_quartic_checker_f91y.py`, commit `9d2c2f536a9938a377d90e9c7fab39470c056196`. Its archived output is `artifacts/R15/f0111_projective_quartic_checker_f91y.out`, commit `e831bb59dbc0985f31efaa3a47f3432112c2a7e0`, ending:

`PROJECTIVE_FOURTH_ORDER_NECESSARY_CONDITION_VIOLATED`
`ALL_EXACT_CHECKS_PASS`.

This is a self-check, not an independent audit.

## 6. What moved and what remains

This does not solve the full retained F0111 `k=2` screen, much less Talagrand Problem 10.9. The new theorem removes a whole class of false local candidates that survive the straight-line quartic test. An exploratory parameter scan suggests the **radial** specialization alone may not eliminate every two-block null regime; I do not count that scan as proof. The stronger next route is to use the full pseudoinverse condition `D^4G[h^4] >= 3 b^T H^+ b`, together with the nonnegative coefficient/contact equations, or optimize the projective bend over asymmetric positive directions supplied by the exact all-ray cone.

Current literature checked 2026-09-19: Ascoli--He--Park--Talagrand, arXiv:2608.11183, reformulate the discrete Convexity Conjecture via `k`-thresholds and prove broad classes; Park, arXiv:2609.14681 (2026-09-13), gives a dimension-independent bound explicitly toward the conjecture. I found no accessible source stating this F0111 projective inequality/application, but novelty remains **UNVERIFIED**. Generic higher-order tangent optimality is prior art (e.g. Penot and later degenerate-optimization work), so the mechanism should not be advertised as intrinsically new without a deeper search.

## 7. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  native_source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2 / I0076"
  native_metric_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_metric_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "retired after six-run handoff; do not increment"
  retained_screen: "Talagrand F0111 Problem 10.9, k=2; SELF_CHECK_ONLY / NOT CLAIMED / PENDING"
  retained_movement: "proved full projective fourth-order necessary condition; radial certificate-free corollary; exactly eliminated prior n=4 local null candidate"
  tried_moves: [5, 11, 24]
  remaining_obligation: "native I0076 has no surviving frozen candidate and no free lawful successor; retained screen still needs elimination or realization of all mixed-sign first-bifurcation regimes"
  evidence:
    idea_commit: "f01e49e5792c36e8ca4cfb8a5eec30ed050a13da"
    checker_commit: "9d2c2f536a9938a377d90e9c7fab39470c056196"
    checker_output_commit: "e831bb59dbc0985f31efaa3a47f3432112c2a7e0"
  audit_ids: []
  audit_status: "SELF_CHECK_ONLY; no independent audit requested or counted"
```

## 8. Model / scheduler boundary

The platform limitation remains unchanged in the exposed task surface: prompt/title, schedule/timing, enabled-state and ordinary task-update controls are exposed, but there is no binding model-family selector, no reasoning-effort selector, no authenticated per-run model/effort receipt, and no guaranteed hour-long execution field. GPT-6 / maximum therefore remains prompt-only here.

Root RESULTS also records that the historical P26 `You cannot modify this task` failure was authorization-context-specific: a later full P26 update succeeded from an authorized P/C context, while another context denied edits. The compliant workaround for an edit-denied task is the owning/authorized workspace/account/API/admin context or platform support, not a permission bypass or duplicate. Actually guaranteeing GPT-6 / maximum would require a supported scheduling/product/backend/API surface that persists those routing fields and returns authenticated runtime attestation.
