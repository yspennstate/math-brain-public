Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on `BLANC-RENAUDIE-2026-MEANFIELD-7-10`: `M_A = 0 -> 0`; the owner’s six-unchanged CLOSABLE retirement rule is now enforced. R09 returns to the successor-admission gate with `E_ready = 0 -> 0`. Methods used: #5 ADD A PARAMETER AND DIFFERENTIATE, #22 READ THE FAILURES, NOT THE SUCCESSES, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R09 — Blanc–Renaudie terminal handoff: cut-cover sensitivity and an intrinsic Bernoulli part

Date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Lane: **CLOSABLE OUTSIDE**.

## 1. Continuity and mandatory retirement

I continued from

`runs/R09/20260919T0033Z_blanc_parity_fourier_compactification_7e4c2a.md`.

I did **not** reopen Tang Question 4.11, G0013, or the Chen–Wang successor. Tang remains **REFUTED / RETIRED** in the R09 lifecycle; its broader transitive-graph clause is not reassigned here. The active source entering this invocation was Arthur Blanc-Renaudie, *Markovian renormalisation for percolation in high-dimension: Semi-decidability of mean field behavior*, arXiv:2609.20764, for the unresolved nearest-neighbour dimensions `d=7,8,9,10`.

The fixed source metric was

\[
M_A:=\#\{d\in\{7,8,9,10\}:\text{a complete rigorous Theorem 1.1(a) initialization certificate has been obtained}\}.
\]

It remains

\[
\boxed{M_A=0.}
\]

This target has crossed the owner-defined six-unchanged-run CLOSABLE retirement threshold. Six consecutive immutable reports already state `M_A=0 -> 0`:

1. `20260918T1738Z_blanc_finite_perron_lambda_9c41e7.md`;
2. `20260918T1833Z_blanc_shift_tv_fourier_certificate_f3c91a.md`;
3. `20260918T1932Z_blanc_direct_bridge_mixing_6d13a8.md`;
4. `20260918T2038Z_blanc_F2_orbit_gateway_81d5e3.md`;
5. `20260918T2130Z_blanc_palm_sizebias_adaptive_core_4f72c9.md`;
6. `20260918T2234Z_blanc_polynomial_localmod_budget_c2a941.md`.

Two later reports, `20260918T2331Z_blanc_unified_matching_smoothness_a91f6c.md` and the controlling `20260919T0033Z...` report, also left the fixed metric unchanged. I preserve the stored `stagnation_count` as **UNKNOWN**, as instructed; retirement here is justified directly by the six named immutable no-movement reports rather than by inventing a numeric counter field.

Therefore this is a **terminal mathematical handoff**, not another attempt to keep the same source alive indefinitely. The results below are the final new-method diagnostics requested by the preceding report and are preserved because they materially sharpen the handoff. They do not reset the metric or the retirement clock.

Fresh primary-source checking on 2026-09-19 still finds arXiv:2609.20764 as the current Blanc-Renaudie source, with nearest-neighbour `d>=11` known and `7<=d<=10` explicitly left open. No later source-matching resolution surfaced in the bounded dated search. This is bounded negative evidence, not a novelty or worldwide-priority certificate.

## 2. Required repository state recovered

Before the new mathematics I recovered the current versions of the campaign/index/ranking surfaces, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the active R09 claim and newest R09 report, the newest visible neighboring CLOSABLE reports, and current admission/coordinator evidence. I also carried forward the append-only intake cursor rather than pretending to freshly render every unchanged JSONL row through the connector.

The newest admission-delta evidence visible before this write still has **no free READY CLOSABLE successor**. Newly surfaced CLOSABLE claims are owned; the freshest unclaimed replenishment lead is still PENDING rather than READY. Therefore no ownership is overridden and no source is silently promoted from PENDING to READY.

## 3. Source notation used below

For nearest-neighbour percolation (`L=1`), the source defines a pointed cluster

\[
\vec A=(A,\vec a),\qquad \vec a=(a^-,a^+),\quad a^-\in A,
\]

with

\[
\Delta(\vec A)=a^+,
\qquad
\mu_p(\vec A)=\mathbb P_p(C(0)=A),
\]

and iid pointed law

\[
\pi_p(\vec A)=\frac{\mu_p(\vec A)}{\Omega\chi(p)},
\qquad \Omega=2d.
\]

The cut relation is

\[
(\vec A,\vec B)\in\mathcal C_{\rm cut}
\iff
b^-\notin B\operatorname{off}_0(A-a^+).
\]

For fixed endpoints `A_0,A_3`, let `A_1,A_2` remain iid with law `pi_p` before killing and put

\[
X:=\Delta(\vec A_1)+\Delta(\vec A_2).
\]

Let

\[
R(x):=\mathbb P(X=x)= (q_p*q_p)(x),
\qquad q_p(x):=\mathbb P(\Delta(\vec A)=x),
\]

and let

\[
\zeta_{A_0,A_3}(x)
:=\mathbb P(X=x,\ T_{\rm cut}>3\mid \vec A_0,\vec A_3).
\]

Thus `zeta <= R` pointwise. Write

\[
D_{A_0,A_3}:=R-\zeta_{A_0,A_3}.
\]

The preceding R09 report bounded the directional fractional matching mass of `zeta` by using only the total deleted mass. The first result below identifies the exact spatial statistic that matters.

---

## 4. Method #5 — soft cut interpolation gives an exact vertex-cover influence formula

Fix a coordinate `i`. Let `G_i` be the graph on `Z^d` with edges

\[
\{x,x+e_i\},\qquad x\in\mathbb Z^d.
\]

For every summable nonnegative measure `mu` on `Z^d`, define the directional fractional matching mass

\[
\mathfrak m_i(\mu)
:=
\sup_{\eta_x\ge0}
\left\{
\sum_x\eta_x:
\eta_x+\eta_{x-e_i}\le \mu(x)\ \forall x
\right\}.
\tag{4.1}
\]

### Lemma 4.1 — exact weighted König representation

Let `VC_i` be the family of vertex covers of `G_i`, equivalently sets `V` such that every pair `{x,x+e_i}` meets `V`. Then

\[
\boxed{
\mathfrak m_i(\mu)
=
\inf_{V\in\mathrm{VC}_i}\mu(V)
=
\mu(\mathbb Z^d)-
\sup_{I:\ I\cap(I+e_i)=\varnothing}\mu(I).
}
\tag{4.2}
\]

#### Proof

On a finite union of finite coordinate-line intervals, (4.1) is the maximum-weight fractional matching LP with vertex capacities `mu(x)`. Its dual is

\[
\inf\left\{
\sum_x\mu(x)y_x:
 y_x\ge0,\ y_x+y_{x+e_i}\ge1
\right\}.
\]

`G_i` is bipartite, so the weighted vertex-cover polytope is integral; an optimal dual may be taken with `y_x in {0,1}` and is exactly a minimum `mu`-weight vertex cover. Exhaust `Z^d` by finite boxes. Since `mu` is summable, both primal and dual values converge monotonically with a vanishing boundary/tail error, giving the first identity. Complements of vertex covers are precisely independent sets for `G_i`, giving the second identity. `square`

Now interpolate linearly between the unconditioned and killed bridge measures:

\[
\mu_t:=R-tD=(1-t)R+t\zeta,
\qquad 0\le t\le1.
\tag{4.3}
\]

By (4.2),

\[
\boxed{
\mathfrak m_i(\mu_t)
=
\inf_{V\in\mathrm{VC}_i}\big(R(V)-tD(V)\big).
}
\tag{4.4}
\]

Thus the matching mass is a decreasing concave function of the cut-strength parameter `t`. On every finite truncation it is piecewise linear, and if `V_t` denotes the set of optimal covers at `t`, then

\[
\partial_+\mathfrak m_i(\mu_t)
=-\max_{V\in V_t}D(V),
\qquad
\partial_-\mathfrak m_i(\mu_t)
=-\min_{V\in V_t}D(V).
\tag{4.5}
\]

The infinite-volume statement needed here is the variational formula (4.4); (4.5) can always be used on an exact finite truncation before the tail limit.

This is the useful sensitivity calculation: **matching is destroyed only to the extent that the cut filter concentrates its deletions on the currently cheapest directional vertex covers.** Total deletion mass is not the correct statistic.

Define the directional cut-cover bias

\[
\beta_i(\vec A_0,\vec A_3)
:=
\sup_{\substack{V\in\mathrm{VC}_i\\R(V)>0}}
\frac{D_{\vec A_0,\vec A_3}(V)}{R(V)}
\in[0,1].
\tag{4.6}
\]

Because the middle states are iid before killing,

\[
\frac{D(V)}{R(V)}
=
\mathbb P(T_{\rm cut}\le3\mid X\in V,\vec A_0,\vec A_3).
\tag{4.7}
\]

Hence `beta_i` has a direct probabilistic meaning: it is the worst cut probability after conditioning the middle displacement to lie in a coordinate-direction vertex cover.

### Corollary 4.2 — conditioning-stable matching criterion

For every endpoint pair,

\[
\boxed{
\mathfrak m_i(\zeta_{\vec A_0,\vec A_3})
\ge
(1-\beta_i(\vec A_0,\vec A_3))\,
\mathfrak m_i(R).
}
\tag{4.8}
\]

#### Proof

For every vertex cover `V`, definition (4.6) gives

\[
\zeta(V)=R(V)-D(V)\ge(1-\beta_i)R(V).
\]

Take the infimum over `V` and use (4.2). `square`

This strictly sharpens the previous total-mass transfer inequality. A proof that, for typical source endpoints,

\[
\beta_i\le1-\varepsilon
\tag{4.9}
\]

would preserve a fixed fraction of the unconditional Bernoulli/matching part even if the total survival probability itself is not near one.

---

## 5. Method #22 — the relevant failed literature says “aperiodic regeneration / Bernoulli part,” not “more Fourier algebra”

I checked adjacent local-limit/total-variation methods specifically for the failure mode isolated last run.

- Barbour–Lindvall, *Translated Poisson approximation for Markov chains* (J. Theoret. Probab. 19 (2006), arXiv:0810.0599), obtain total-variation local approximation for Markov-additive sums when the **regeneration-block sum is aperiodic**, and explicitly note that without aperiodicity total-variation approximation cannot be expected.
- Dabrowski–McDonald, *An application of the Bernoulli part to local limit theorems for moving averages on stationary sequences* (1996), formulate the same issue through the amount of an extractable **Bernoulli part**.
- Giuliano–Weber, *Approximate local limit theorems with effective rate and application to random walks in random scenery* (Bernoulli 23 (2017), arXiv:1412.3980), make Bernoulli-part extraction quantitative with effective errors.

These papers do **not** solve the killed pointed-cluster problem and are not cited as prior art for a source-specific theorem here. They do confirm that the parity obstruction from the preceding R09 run is structural: a local/TV limit theorem needs a unit-lattice aperiodicity mechanism that survives the relevant conditioning or regeneration.

Blanc-Renaudie’s Proposition 3.25 obtains exactly such a mechanism by paying a multiplicative local-modification cost to change

\[
\Delta(\vec A_1)+\Delta(\vec A_2)
\]

by a coordinate unit vector. In Bernoulli-part language, the local surgery is manufacturing a unit-shift Bernoulli component after killing.

Therefore the right alternative is not another unconditional Fourier estimate—the preceding run already supplied one—but an **intrinsic Bernoulli component of the iid pointed-cluster law plus a theorem that the cut filter cannot annihilate all of it**. The next subsection supplies the first half with an explicit source-native lower bound.

---

## 6. Method #23 — opposite of source surgery: every connected cluster already carries an order-one intrinsic Bernoulli part

The source modifies clusters locally to create a unit displacement. Instead, use the open edges already present in each connected cluster.

For a finite cluster `A`, let `E_i(A)` be the number of undirected open edges of `A` parallel to the `i`th coordinate axis. Along any fixed coordinate line these edges form a path. Let `M_i(A)` be the size of a maximum matching among those `i`-direction edges.

### Theorem 6.1 — intrinsic pointed-cluster Bernoulli part

For nearest-neighbour percolation and every `p<pc`, every coordinate `i`,

\[
\boxed{
\mathfrak m_i(q_p)
\ge
\frac{\chi(p)-1}{2d\,\chi(p)}.
}
\tag{6.1}
\]

Consequently convolution preserves the same amount:

\[
\boxed{
\mathfrak m_i(q_p*q_p)
\ge
\frac{\chi(p)-1}{2d\,\chi(p)}.
}
\tag{6.2}
\]

In particular, whenever `chi(p)>=2`,

\[
\boxed{
\mathfrak m_i(q_p*q_p)\ge\frac1{4d}.
}
\tag{6.3}
\]

#### Proof of (6.1)

Fix a cluster `A` and choose a maximum matching of its internal `i`-direction edges. For every matched edge `{u,u+e_i}` and every nearest-neighbour oriented step `delta` among the `Omega=2d` choices, pair the two pointed states

\[
(A,(u,u+\delta))
\quad\text{and}\quad
(A,(u+e_i,u+e_i+\delta)).
\]

Both are legal pointed clusters because the two tails lie in `A`. They have exactly the same pointed-law mass

\[
\frac{\mu_p(A)}{\Omega\chi(p)},
\]

and their displacements differ by exactly `e_i`. The tail matching makes these pairs disjoint for fixed `delta`; different `delta` values give different pointed states. Hence they define a feasible directional matching for `q_p` of total mass

\[
\frac1{\chi(p)}
\sum_A\mu_p(A)M_i(A)
=
\frac{\mathbb E_p[M_i(C(0))]}{\chi(p)}.
\tag{6.4}
\]

The `i`-direction subgraph is a disjoint union of paths, so a maximum matching contains at least half its edges:

\[
M_i(A)\ge \frac12 E_i(A).
\]

By coordinate symmetry,

\[
\mathbb E E_i(C(0))
=
\frac1d\mathbb E |E(C(0))|.
\]

Every finite connected cluster has at least `|C|-1` edges. Therefore

\[
\mathbb E M_i(C(0))
\ge
\frac1{2d}\mathbb E(|C(0)|-1)
=
\frac{\chi(p)-1}{2d}.
\]

Substitute into (6.4). `square`

#### Proof of (6.2)

Let `eta_x` be any feasible matching for `q_p` in direction `i`, and define

\[
\bar\eta_x:=\sum_y\eta_{x-y}q_p(y).
\]

Then

\[
\bar\eta_x+\bar\eta_{x-e_i}
\le
(q_p*q_p)(x),
\]

and

\[
\sum_x\bar\eta_x=\sum_x\eta_x.
\]

Thus convolution with a probability law cannot decrease this directional matching mass. Taking the supremum and using (6.1) proves (6.2). `square`

This is stronger and cleaner than the preceding FKG-only lower bound in the large-susceptibility regime. It is also source-native: it uses only the exact pointed law (3.4), connectivity of the actual percolation cluster, and lattice symmetry.

### Corollary 6.2 — one exact remaining quantity

Combining (4.8) and (6.2), for every fixed endpoint pair,

\[
\boxed{
\mathfrak m_i(\zeta_{\vec A_0,\vec A_3})
\ge
(1-\beta_i(\vec A_0,\vec A_3))
\frac{\chi(p)-1}{2d\chi(p)}.
}
\tag{6.5}
\]

Hence if `chi(p)>=2` and a typical-endpoint theorem gives

\[
\beta_i(\vec A_0,\vec A_3)\le1-\varepsilon
\quad\text{for every }i,
\tag{6.6}
\]

then

\[
\mathfrak m_i(\zeta)\ge\frac{\varepsilon}{4d}.
\tag{6.7}
\]

The previous R09 matching lemma then immediately gives both:

1. a source-form quadratic Fourier contraction for the endpoint-conditioned bridge, with a constant at least of order `epsilon/(d*pi^2)`; and
2. a nontrivial endpoint bridge survival mass, because `P_3^otimes >= 2 m_i`.

Thus the remaining high-frequency/mixing obstruction can be packaged into **one conditioning-stability inequality for `beta_i`**.

---

## 7. Why the raw Bernoulli part does not yet close the source

I tried to prove (6.6) directly from the raw cut relation, i.e. to do the opposite of the proposer’s local-surgery proof. Two exact obstructions emerged.

### 7.1 Orientation randomness alone can never repair parity

Fix the two underlying middle clusters and their two tails `u_1,u_2`. Write the outgoing nearest-neighbour directions as `delta_1,delta_2`. Then

\[
X=u_1+u_2+\delta_1+\delta_2.
\]

On the bipartite lattice, every nearest-neighbour direction has odd checkerboard parity. Hence

\[
\operatorname{parity}(X)=\operatorname{parity}(u_1+u_2)
\]

independently of `delta_1,delta_2`. Therefore varying only the oriented edge directions can never produce a pair of displacements differing by one coordinate unit. Any conditioning-stable Bernoulli part must move a **tail / root / cluster geometry**, not merely an orientation label.

This explains the exact `p=0` parity failure found in the preceding report and rules out a tempting cheap route.

### 7.2 The cut relation consumes both sides of a pointed state

For a middle pointed cluster `B`, the incoming cut uses its tail `b^-` through

\[
b^-\in B\operatorname{off}_0(A-a^+),
\]

while its outgoing cut uses the translated obstacle `B-b^+`. Shifting the tail by an internal unit edge while keeping the outgoing direction fixed creates exactly the desired unit change in `Delta`, but it can change the incoming target and the outgoing obstacle simultaneously.

Thus the intrinsic matching in Theorem 6.1 is **not automatically conditioning-stable**. The quantity `beta_i` records precisely how badly the cut filter can align itself with this matching.

There is a useful exact re-rooting symmetry for a future worker. If `z in A`, let

\[
T_z(A,\vec a):=(A-z,\vec a-z).
\]

Translation invariance plus the fact that `0,z` are in the same cluster gives

\[
\mu_p(T_z\vec A)=\mu_p(\vec A),
\qquad
\Delta(T_z\vec A)=\Delta(\vec A)-z,
\tag{7.1}
\]

and

\[
(A-z)-(a^+-z)=A-a^+.
\tag{7.2}
\]

Therefore **the outgoing obstacle is exactly invariant under re-rooting**. What changes is the incoming cut, because the next rooted cluster is now placed differently relative to the previous obstacle. This reduces any re-rooting-based unit-shift coupling to a one-sided incoming-cut stability problem, but I do not have a uniform quantitative bound for that problem. It is a concrete handoff route, not a claimed closure.

---

## 8. Exact blocker at retirement

The cleanest remaining statement is now:

\[
\boxed{
\text{Find }\varepsilon>0\text{ and a source-acceptable exceptional mass }\delta
\text{ such that, for typical }(\vec A_0,\vec A_3),
\quad
\max_{1\le i\le d}\beta_i(\vec A_0,\vec A_3)\le1-\varepsilon.
}
\tag{8.1}
\]

Equivalently, no directional vertex cover of the middle-displacement lattice may have its raw mass **entirely or almost entirely removed by the three-cut survival filter**.

Everything before the conditioning step is now quantitatively favorable:

- the raw pointed increment law has an explicit intrinsic Bernoulli part at least `(chi-1)/(2d chi)`;
- convolution preserves it;
- the sensitivity to killing is exactly the vertex-cover cut bias `beta_i`;
- a uniform gap in `beta_i` would feed both high-frequency Fourier contraction and bridge survival/mixing.

What is missing is a source-faithful proof of (8.1) with constants that do not collapse as `chi -> infinity`. The source’s local modifications prove the needed effect by force, but with expensive finite-energy constants. The direct route must show that naturally occurring internal-tail adjacency survives conditioning with positive density.

This is the simplest special case worth attempting if the target is ever reassigned: prove (8.1) for one coordinate and endpoints in a single order-one-mass good class without using radius-`r` forced local modifications.

No finite numerical dimension certificate follows from the present theorem; `M_A` therefore remains `0` and the honest mathematical status remains **PARTIAL / OPEN / HANDOFF_READY / RETIRED_FROM_ACTIVE_R09**.

## 9. Current successor gate

Because the Blanc–Renaudie target is retired by policy, R09 returns to the established successor-admission metric

\[
E_{\rm ready}:=\#\{\text{new full-source CLOSABLE successors that pass all admission gates in the current bounded delta}\}.
\]

The latest current admission/coordinator evidence visible before this write still reports no free READY CLOSABLE source. In particular, newly created CLOSABLE claims are already owned, and the newest unclaimed replenishment lead remains PENDING rather than READY. No owner-authorized release of a suitable CLOSABLE source appears in the bounded delta.

Therefore

\[
\boxed{E_{\rm ready}:0\to0.}
\]

This is an admission result, not a theorem that no suitable problem exists anywhere. R09 should remain at the successor gate until a genuinely new/corrected source row or explicit lawful release crosses the source/current-literature/prior-attempt/ownership/closability gate. Do not reopen Blanc–Renaudie, Tang, G0013, or Chen–Wang from this slot without an explicit owner-authorized reassignment.

No checker-only artifact is added: this run produced analytic reductions and a terminal handoff, not a moved finite source metric.

## 10. Model and scheduler-control truth

The installed prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, hence reasoning is **UNVERIFIED** and GPT-6 maximum is not claimed.

The exposed scheduled-task control surface still has no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed-duration control. Making GPT-6/maximum enforceable requires an owner-authorized product/workspace/API/admin surface exposing persistent model and effort controls plus authenticated per-run attestation.

The historical P26 `You cannot modify this task` event was later superseded by a successful P26 update from another authorized context. A live modification denial must be handled from the task’s owning/authorized context or through authorized platform/admin support; duplication, identity substitution, or permission bypass is not a lawful workaround. No scheduler or permission action was attempted here.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R09
  deployment: NEW-METHODS-2026-09-16
  lane: CLOSABLE_OUTSIDE
  predecessor:
    source_id: BLANC-RENAUDIE-2026-MEANFIELD-7-10
    status_before: OPEN
    status_after: PARTIAL_OPEN_HANDOFF_READY_RETIRED_FROM_ACTIVE_R09
    metric_name: M_A
    metric_before: 0
    metric_after: 0
    movement: NO_MOVEMENT
    stagnation_count: UNKNOWN
    retirement_basis:
      rule: CLOSABLE_RETIRE_AFTER_SIX_UNCHANGED_RUNS
      evidence: six_named_immutable_reports_with_M_A_0_to_0
  methods_actual: [5, 22, 23]
  new_results:
    - exact directional weighted-Koenig / vertex-cover representation for matching mass
    - linear cut-strength interpolation and finite-truncation derivative formula
    - exact cut-cover bias beta_i controlling conditioning loss
    - intrinsic pointed-cluster Bernoulli part m_i(q_p) >= (chi-1)/(2d chi)
    - convolution preserves that Bernoulli part
    - combined killed-bridge bound m_i(zeta) >= (1-beta_i)(chi-1)/(2d chi)
    - orientation-only parity no-go and outgoing-obstacle re-rooting invariance
  remaining_obligation:
    - prove a chi-uniform typical-endpoint gap beta_i <= 1-epsilon without expensive forced local surgery
    - then instantiate the source computable initialization constants and certify at least one of d=7,8,9,10
  successor_gate:
    source_id: NONE
    claim_path: NONE
    metric_name: E_ready
    before: 0
    after: 0
    movement: NO_MOVEMENT
    status: ADMISSION_PENDING
  checker_added: false
  scheduler_changed: false
  email_or_drive: false
  public_posting_action: false
  permission_or_workflow_action: false
```

No email/Gmail, Drive, public posting, paid compute, purchase, credential access, permission change, workflow execution, shared-root edit, peer-track edit, scheduler modification, or force-push was performed.
