Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E >= b7 -> gamma_E >= b8>b7`**; methods actually tried: **B20 / B25 / B3**.

# HARD7-04 bounded research iteration — serial historical fallback for fixed-outdegree PA criticality

Status: **PARTIAL / SOURCE OPEN**. This run proves a strict new lower-bound advance for the exact admitted sequential fixed-outdegree preferential-attachment model. It does **not** identify the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or produce a scaling-limit law.

The complete analytic proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_serial_historical_fallback_20260920T0632Z.md`

created at commit

`32f22f6f40f49084f57a4484a9f5f76938853fd2`

and read back at that exact SHA before this report was written.

---

## 1. Continuity, ownership, and evidence consumed

I resumed the exclusive canonical claim

`operations/claims/P0151.md`

owned by `HARD7-04`. I did not restart I0049, P0157, the configuration-model/MST line, any solved degree-count target, or the conditionally-independent-edge growing-graph theorem.

Before the new mathematics I reread/reconciled the required repository surfaces:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/P0151.md`;
- the current I0049 queue/task-health traces, which continue to mark its uniformly-grown critical-window scope as later-literature-known rather than available for duplicate work;
- the neighboring preferential-attachment track `runs/R08/20260917T2326Z_i0048_threshold_comparison_73b9e1.md`, which classifies the old I0048 threshold scope as known and does not own P0151;
- the complete current HARD7-04 chain through the immediately preceding report `runs/hard7_2026-09-18/HARD7-04/2026-09-20T0530Z__p0151_retrospective_parent_ticket.md` and its matching proof artifact.

A repository-wide search still showed `P0151` exclusively owned by HARD7-04. No peer claim was overwritten. `POSTED.md` contains no source-equivalent P0151 paper.

---

## 2. Frozen source statement and current-literature refresh — 20 September 2026

The model remains Ray/Hazra--van der Hofstad--Ray model (d): fixed integer `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges from each arriving vertex, target probabilities proportional to current degree plus `delta` with within-birth updates, no self-loops for the new vertex, followed by independent bond retention with probability `pi`.

The exact threshold is

`pi_c = delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

The admitted source target is the finite-size **critical regime** at/near this threshold: determine the critical window and scale/law of the largest critical components for the exact fixed-outdegree sequential model.

Fresh bounded web/source searches on **20 September 2026** rechecked:

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085, `https://arxiv.org/abs/2312.14085`. It identifies the exact threshold and giant/no-giant dichotomy through the Pólya-point-tree mean operator; the searched record does not state a finite-size critical-window theorem for this exact fixed-`m` model.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025, `https://arxiv.org/abs/2512.18937`. It proves a `(log n)^(-2)` window and `sqrt(n)/log n` critical largest-component scale when a new vertex connects **independently** to earlier vertices. That assumption does not include the exact fixed-outdegree sequential birth law here.
3. Mörters--Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844, submitted 26 June 2026, `https://arxiv.org/abs/2606.27844`. It treats a different inhomogeneous PA-kernel ensemble with `tau in (2,3)` and a moving threshold.
4. Ray's 2024 thesis/current P0151 source trace remains the primary fixed-outdegree critical-regime program used for admission.

No source-matching fixed-outdegree critical-window resolution surfaced in this bounded refresh. This is bounded negative evidence, not a worldwide novelty certificate.

---

## 3. Frozen metric: exact before/after

Put

`a:=m+delta`, `A:=2m+delta`, `pi:=pi_c`.

The frozen admitted quantity is

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The preceding run proved

`gamma_E>=b7`,

where

`b2:=m(1+a pi)/A`,
`b6:=b2+m(m-1)pi^2`,
`b_U:=b2+2m(m-1)pi^2(A+m)/A`,
`d_*:=1/2-b_U`,
`vartheta:=min(1,d_* A/[4(a+m)pi^3])`,
`eta_R:=vartheta a^2 pi^3/A^2`,
`b7:=b6+eta_R`,
`kappa_1:=2 vartheta(a+m)pi^3/A`,
`b_U':=b_U+kappa_1<1/2`.

Define the remaining square-moment safety margin

`d_7:=1/2-b_U'>0`,

and the new fallback ticket strength

`lambda:=min(1,d_7 A/[4(m-1)(a+m)pi^3])`.

Set

`eta_F:= [a^2 pi^2/A^2](1-pi vartheta)
         [1-(1-pi lambda)^(m-1)]`,

`b8:=b7+eta_F`.

This run proves

`gamma_E>=b8>b7`,

with `b8<1/2`.

Thus the source-relevant metric moves strictly:

**Before:** `gamma_E>=b7`.

**After:**

`gamma_E>=b8
 =b7+[a^2 pi_c^2/A^2](1-pi_c vartheta)
       [1-(1-pi_c lambda)^(m-1)]
 >b7`.

The unchanged-run counter resets.

---

## 4. Idea written before validation

The preceding run extracted one previously unused historical out-edge of a captured old vertex `u`. A natural stronger attempt is to use **all `m` historical out-edges of `u`**.

The first version is false as an additive counting rule: several birth edges of `u` may share the same old endpoint, so summing successful parent rewards can count one actual vertex several times. A parent can also be captured by a later bridge of the current birth. The exact obstruction is therefore duplicate/deduplicated parent mass, not lack of historical randomness.

The new idea is to turn the historical family into a **serial first-success algorithm**. Retain the old label-1 historical certificate. Only if its raw certificate fails, try labels `2,...,m` in order and stop at the first raw success. There is then at most one new fallback parent. Repeated endpoints cannot create reward overcounting, yet the unused labels generate a positive geometric fallback reward.

I wrote and checked this analytic route before considering any code.

---

## 5. B20 — find why the obvious all-parent algorithm fails

The naive simultaneous algorithm would expose all historical edge bits after a current gate-and-bridge event and add every successful parent reward. It fails as a proof device for two independent reasons.

1. `p_i(u)=p_j(u)` is allowed, so raw successful certificates are not disjoint new vertices.
2. Even a distinct historical parent can be captured by another current bridge before the historical layer is finalized.

Thus the raw sum of historical weights is not a lower bound for the actual shadow increment. Merely inserting a union bound would erase precisely the extra positive coefficient one is trying to harvest.

**Outcome B20:** the simultaneous all-parent route is rejected. The obstruction suggests using an exclusive stopping rule rather than trying to estimate complicated duplicate multiplicities.

---

## 6. B25 — count bad roots by edge incidence, not by labels

For every ordinary old root `u`, write `p_j(u)` for the endpoint of historical birth-edge label `j`. Define

`G_t^(m):={u>=3: u notin Q_t,
                   p_j(u)>=3 and p_j(u) notin Q_t for all j=1,...,m}`.

At first sight requiring **all** `m` parents to avoid the shadow appears to lose `m W_t` roots. It does not.

A bad outside root with some historical edge ending in `Q_t` can be charged to one actual bad edge incidence. The total number of such incidences is at most the total degree of `Q_t`, hence at most its attractiveness `W_t`. Likewise roots with some historical edge ending at seed `1` or `2` are bounded by the seed degree, hence by `Z_t`. Roots already in the shadow are at most `W_t/a`.

Therefore, deterministically,

`|G_t^(m)|>=t-W_t/a-W_t-Z_t-C`.

Since `c(w)=min(w,2A)>=a` for every ordinary vertex,

`sum_{u in G_t^(m)}c(w_u(t))
 >= a t-(1+a)W_t-aZ_t-C`.                                       (6.1)

This is exactly the same first-order usable-root supply as in the one-historical-edge argument. The edge-incidence double count is the structural fact that makes an all-label fallback feasible.

**Outcome B25:** succeeded and removed the apparent factor-`m` supply loss.

---

## 7. B3 — prove the stronger serial-fallback theorem

### 7.1 Freshness

If `u in G_t^(m)`, then each historical endpoint was outside the shadow at the birth of `u`, since the shadow only grows. Because `u` itself is still outside at time `t`, no historical edge from its birth produced a retained gate then. The outside historical retention bits were unnecessary for the shadow update and can be deferred. Thus all `m` historical edge bits remain mutually independent Bernoulli(`pi`) bits until the current capture of `u`.

### 7.2 Current certificate

Use current edge label `1` as a retained gate into frozen `Q_t` and current label `2` as a retained capped bridge to `u in G_t^(m)`. As in the preceding theorem,

`P(gate 1 and accepted bridge 2 to u | F_t)
 >= pi^2 W_t c(w_u(t))/(At+K)^2`.                                (7.1)

### 7.3 Serial historical fallback reward

Historical label `1` retains the preceding ticket strength

`vartheta a/w_{p_1(u)}(t)`.

Its raw success probability is at most `pi vartheta`, so fallback label `2` is reached with probability at least `1-pi vartheta`.

For each historical label `j=2,...,m`, if it is reached, use a fresh ticket of probability

`lambda a/w_{p_j(u)}(t)`.

Conditional expected raw reward at that stage is at least

`pi lambda a`,

while the probability of reaching stage `j` is at least

`(1-pi vartheta)(1-pi lambda)^(j-2)`.

Stopping at the first raw success therefore gives conditional expected raw fallback reward

`R_F
 =pi lambda a(1-pi vartheta)
   sum_{k=0}^{m-2}(1-pi lambda)^k`

`=a(1-pi vartheta)[1-(1-pi lambda)^(m-1)]>0`.                    (7.2)

Repeated historical endpoints do not affect (7.2), because distinct edge-retention bits and auxiliary tickets are independent and the rule proposes only the first successful parent.

### 7.4 Lower drift

Multiply (7.1) by (7.2), sum over the good roots, and use (6.1). The raw fallback contribution satisfies

`E[F_t^raw|F_t]
 >= eta_F W_t/t
    -C W_t^2/t^2
    -C W_tZ_t/t^2
    -C W_t/t^2`.                                                  (7.3)

A chosen fallback parent cannot equal the current gate target or the current bridge root. It can only be duplicated by one of current labels `3,...,m`. The accepted capped-bridge probability to a prescribed old parent is uniformly `O(1/t)`, because the cap is at most `2A`. Thus deleting current-birth collisions costs only

`E[F_t^raw-F_t|F_t]<=C W_t/t^2+C/t^2`.                          (7.4)

Adding the old `b7` drift gives

`E[Delta_8 W_t|F_t]
 >= b8 W_t/t
    -C W_t^2/t^2
    -C W_tZ_t/t^2
    -C W_t/t^2
    -C/t`.                                                        (7.5)

### 7.5 Upper drift and square budget

Ignoring the serial stopping conditions only enlarges the fallback. The current gate contributes `pi W_t/(At)` to first order; the accepted bridge probability is at most `2pi+o(1)`; and one fallback historical label has expected final reward at most `pi lambda(a+m)`. Hence

`E[F_t|F_t]
 <= [kappa_F/t+O(t^-2)]W_t+C/t`,

where

`kappa_F:=2(m-1)lambda(a+m)pi^3/A<=d_7/2`.

Consequently

`b_U'':=b_U'+kappa_F<1/2`.                                       (7.6)

For the square, after dropping gate/reach restrictions, a fixed fallback label/root contributes at most `C(w_{p_j(u)}+1)` after retention and inverse-weight ticketing, and current edge `2` chooses the capped root with probability `O(1/t)`. Summing over labels `2,...,m`,

`sum_{j=2}^m sum_u w_{p_j(u)}(t)
 <= sum_v d_v(t)w_v(t)
 <= V_t`.

Therefore

`E[F_t^2|F_t]<=C(1+V_t/t)`.                                      (7.7)

The preceding square-jump estimate has the same form, so

`E[(Delta_8 W_t)^2|F_t]<=C(1+V_t/t)`.

With `E V_t=O(t)` and `2b_U''<1`, the square recurrence closes:

`E W_t^2=O(t)`.                                                   (7.8)

### 7.6 Bootstrap to `b8`

Taking expectations in (7.5), using (7.8), `W_t<=At+O(1)`, and `E Z_t=O(t^h)` with `h=m/A<1/2`, gives

`mu_{t+1}
 >=[1+b8/t-C/t^2]mu_t-C/t-Ct^{h-1}`.

Since `b8>b7>h`, the normalized error series after division by the product `prod(1+b8/s-C/s^2)` are summable. The inherited positive polynomial seed from the previous shadow construction therefore yields

`E W_n>=c n^b8`.

A retained first-edge gate from each later birth occurs with conditional probability at least `pi W_t/(At+K)`. Summing these activations gives

`E|Q_n|>=c'n^b8`.

The shadow is connected in the actual percolated graph, so

`E|C_max(n,pi_c)|>=E|Q_n|>=c'n^b8`,

hence

`gamma_E>=b8>b7`.

Finally,

`1-(1-x)^(m-1)<=(m-1)x`

implies `eta_F<kappa_F`; together with the preceding `b7<b_U'` this gives

`b8<b_U''<1/2`.

**Outcome B3:** succeeded. The full proof, including every conditional-freshness, collision, first-moment and square-moment step, is in the matching analytic artifact.

---

## 8. Counterexample/stress checks and validation actually performed

The proof was stress-tested against the three places where the stronger all-label statement could fail.

1. **Duplicate historical parents:** this kills the simultaneous raw-sum argument. The serial first-success rule makes outcomes exclusive, so a repeated endpoint is never rewarded twice.
2. **Adaptive exposure:** requiring every historical parent to remain outside the current shadow guarantees that each historical retention bit was irrelevant to all earlier shadow decisions. Deferred decisions therefore supplies genuinely fresh Bernoulli bits at the current capture.
3. **High-degree fallback parents:** inverse-weight tickets cancel one parent-weight factor. For the square budget, the remaining parent weights over **all** historical labels are bounded by actual edge incidence: `sum d_v w_v<=V_t`.
4. **Second-moment margin:** `lambda` is defined from the already proved positive margin `d_7`, forcing the enlarged upper drift coefficient to remain strictly below `1/2` for every fixed `m>=2`, `delta>0`.

No finite SAT/enumeration claim is made, so no exact-arithmetic checker was manufactured. I did run a small floating-point sign sanity scan over representative `(m,delta)` pairs while deriving the formulas; it was used only to catch algebraic mistakes, not as evidence, and no theorem or bound depends on those samples. The certifying object for this run is the written analytic proof itself.

The proof artifact was fetched back from commit `32f22f6f40f49084f57a4484a9f5f76938853fd2` after creation.

---

## 9. Source-level delta versus auxiliary progress

### Source-relevant metric

`gamma_E>=b7  ->  gamma_E>=b8>b7`.

This is genuine movement on the frozen largest-critical-component quantity, but it is still only an expected-size lower exponent. Status remains **PARTIAL / SOURCE OPEN**.

### Auxiliary progress

The run also proves a reusable structural lemma: demanding that **all `m` historical parents** of an outside root avoid the connected shadow still leaves a linear root supply with first-order loss only `W_t/a+W_t+Z_t`, not `m` times that loss. This comes from charging bad roots to actual graph-edge incidences.

The serial fallback shows that every unused historical birth-edge can contribute without any distinct-parent assumption, provided the process stops at the first raw success.

Neither fact is relabeled as a full critical-window theorem.

---

## 10. Remaining full-scope obstruction and next mathematical route

The source problem remains far larger than `gamma_E`. The most important unpaid step is still the **finite-to-local transfer at logarithmic age scale**.

The earlier killed-Pólya-point-tree calculation gives an operator-level deficit

`1-r(pi_c T_L)=C_spec/L^2+O(L^-3)`.

At `L~log n`, this is the expected `(log n)^(-2)` scale. But in the exact fixed-outdegree model, repeated labels/birth-dependence at a component exploration size near `sqrt(n)/log n` can also accumulate at order `(log n)^(-2)`. Thus an `o(1)` local-weak coupling is not enough; the leading dependence correction must be computed or cancelled.

I therefore do **not** recommend spending the next run merely adding a third historical generation or optimizing `lambda`. The next run should switch mechanism to a finite-to-local dependence calculation. A nonrepeating suggested triple is **B1 / B12 / B29**:

- **B1:** change category from graph exploration to a marked branching walk with a collision/dependence operator;
- **B12:** identify the conserved collision mass or compensator created by fixed-outdegree sampling;
- **B29:** add the log-age boundary explicitly and derive the boundary correction at `L~log n` rather than hiding it in `o(1)`.

The exact target is to compare the finite exploration transfer operator to the killed PPT operator at **order `L^-2`**, not merely in weak convergence.

---

## 11. Capability / scheduler-control honesty

The model request remains prompt text only. The task-management interface available to this workflow exposes task content/title/schedule/timing/enabled controls but **no model-family selector, no reasoning-effort selector, and no authenticated guarantee of run duration**. This run identifies as GPT-5.6 Sol; the reasoning level is not authenticated, so it is reported as **UNVERIFIED**. Changing this would require the platform to expose a model/effort control for scheduled runs or to provide an authorized execution surface with such a selector; editing repository text cannot enforce it.

Repository records also explain the historical P26 `You cannot modify this task` response as an authorization-context boundary; P26 was later editable from an authorized context. For any task that still returns that denial, the compliant workaround is the owning/authorized account or context, an explicit ownership/admin transfer, or platform support — **not** schedule duplication or permission bypass.

No schedule, enabled state, email, Drive, public posting, permissions, or workflow was changed in this run.

---

## 12. Own-track ledger delta

```yaml
ledger_delta:
  track: HARD7-04
  target: P0151 fixed-outdegree PA critical window
  status: PARTIAL_SOURCE_OPEN
  metric: gamma_E lower bound
  before: b7
  after: >-
    b8 = b7 + (a^2*pi_c^2/A^2)*(1-pi_c*vartheta)*
         (1-(1-pi_c*lambda)^(m-1))
  strict_movement: true
  methods_this_run: [20, 25, 3]
  artifact: artifacts/hard7_2026-09-18/HARD7-04/p0151_serial_historical_fallback_20260920T0632Z.md
  artifact_commit: 32f22f6f40f49084f57a4484a9f5f76938853fd2
  closure: false
  audits_requested: false
  next_methods: [1, 12, 29]
```

No shared root ledger or peer file was edited.
