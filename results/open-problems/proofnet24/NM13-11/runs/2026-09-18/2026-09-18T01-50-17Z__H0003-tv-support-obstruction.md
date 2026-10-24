Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `A_echo = 0 -> 0`. SOURCE-LEVEL VERDICT MOVED: H0003 / Conjecture 11.8 is REFUTED AS WRITTEN by a support obstruction at every supercritical parameter point. Methods actually tried this run: #1 CHANGE THE CATEGORY, #19 MAKE IT AN ALGORITHM, #25 COUNT THE SAME THING TWICE.**

# NM13-11 sixth run — H0003 full-tree TV support obstruction and projective repair

Date: 2026-09-18 UTC  
Track: `NM13-11` / HARD OUTSIDE  
Repository: private `yspennstate/math-open-problems`, branch `master`  
Canonical source / claim: `H0003` / `operations/claims/H0003.md`  
Canonical dedup identity: `arxiv_2608_15987::conjecture_11.8`, SHA-256 residue `10 mod 13`  
Source-level status after this run: **REFUTED AS WRITTEN / closure AUDIT-PENDING**  
Frozen metric status: **unchanged at its proved floor `A_echo=0` on the bounded-degree source-valid slice**

## 1. Runtime honesty and task-control status

The requested task line asks for GPT-6 with maximum reasoning. That is not what I can verify ran. The actual model exposed to this invocation is **GPT-5.6 Sol**. The reasoning-effort level is not authenticated by a binding selector or runtime telemetry and is therefore **UNVERIFIED**.

The exposed task-control surface still supplies task prompt/title, timing/schedule, timing mode and enabled state, but **no binding model-family selector and no reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text, not an installed scheduler setting. Enforcing it would require an owner-authorized product/workspace/API/admin surface whose schema actually exposes those fields together with runtime attestation.

Repository policy also preserves the corrected P26 history: one older scheduler context returned `You cannot modify this task`, while a later authorized context successfully updated P26. A future denial is therefore an authorization/context boundary, not permission to clone a schedule or bypass access control. This run creates, edits, disables and duplicates **no schedule**.

## 2. Continuity recovered before new mathematics

This invocation continues the already-admitted H0003 assignment; it does **not** reopen intake and does not create or alter the claim file. `operations/claims/H0003.md` still names NM13-11 as exclusive owner. No release, handoff, retirement, POSTED entry, source correction, competing owner, or completed P26/NM13-12 audit for H0003 was recovered.

Before new work I reread or targeted-search-recovered the owner-required current surfaces:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- H-intake verification for `H0003`;
- `operations/claims/H0003.md`;
- all five preceding NM13-11 reports, newest first;
- newest visible neighboring NM13-10 and NM13-12 reports;
- repository searches for H0003 aliases, ownership, attempts, handoffs, audit state, and metric continuity.

Large root and historical surfaces are connector-bounded when rendered wholesale. I used exact-path reads and source/claim/method searches rather than pretending that every historical byte was visible in one response. The H0003 continuity needed for this run was accessible.

The five prior NM13-11 method triples and metric history are preserved exactly:

1. `#2/#4/#8`: source row-sum coefficient `Delta_max` improved on a restricted spectral subclass to `Lambda_*`;
2. `#12/#13/#21`: no metric movement; Perron-coboundary critical perturbation lemma;
3. `#5/#18/#30`: local-tree coefficient `2 sqrt(Delta_max-1)`;
4. `#11/#15/#22`: coefficient moved to `0`, i.e. no linear echo-contraction inequality is needed for the bounded-degree strictly subcritical iterated-limit theorem;
5. `#3/#7/#27`: metric stayed `0`; the no-contraction finite-transcript theorem was extended through exact criticality `rho(M)<=1`.

The newest report explicitly nominated the untried triple `#1/#19/#25`; those are the three methods genuinely attempted here.

## 3. Exact current source and bounded literature check — 2026-09-18 UTC

Exact source: Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1, 17 August 2026.

Current HTML checked directly:

`https://arxiv.org/html/2608.15987`

The current source is still v1. Its Conjecture 11.8 says, literally, that in the full saturated regime and without the dissipative restriction, the **cluster law in the finite graph `G_n`** is within total variation

`C ( epsilon(delta) + eta_n )`

of the genealogy of the multitype Galton--Watson process, with `eta_n -> 0` under Benjamini--Schramm convergence and `epsilon(delta) -> 0` as the saturation margin grows. The sentence following the display calls this equivalent to an asymptotic front-Markov property.

The same source says in Theorem 3.1 that the multitype GW process has positive survival probability iff `rho(M)>1`, explicitly develops a supercritical domain, and in its Bethe-lattice example takes `d=3`, `p=3/4`, giving `rho(M)=3/2>1`. Thus the supercritical case is not an interpretation imported from outside the source.

Fresh dated searches used the exact arXiv id/title, `Conjecture 11.8`, `Front-Markov`, `strong coupling`, `total variation`, the author name, and later author work. They recovered the same v1 source and the companion Kumar--Duddala paper arXiv:2608.21125 (21 August 2026), which concerns front propagation/Bramson correction and the continuous-type limit and does not repair or resolve Conjecture 11.8. No later source-matching correction or resolution was recovered. This is bounded negative evidence, not a worldwide bibliographic claim.

For the corrected topology below I also checked older sparse-interacting-process literature: Oliveira--Reis--Stolerman, arXiv:1812.11924, and Lacker--Ramanan--Wu, arXiv:1904.02585. They provide fixed-time/local-weak locality and continuity results for interacting processes on sparse graphs. They do **not** by themselves prove the absorbing-threshold statement below. The support obstruction used to refute the printed full-tree total-variation statement is elementary probability/topology folklore, and I make **no publication-novelty claim** for that mechanism.

## 4. Frozen metric and counters

The frozen admission metric remains

`A_echo` = the graph-amplification coefficient in a rigorously proved sufficient linear echo-stability condition

`gamma_max * L_sigma * A_echo < alpha_min`

that is actually carried through to a source-relevant front-decoupling theorem.

The fourth run already drove this coefficient to its natural floor on the bounded-degree locally-tree-like strict-subcritical slice:

`A_echo = 0`.

The fifth run kept it there while extending the finite-transcript argument through criticality. This run cannot honestly decrease a nonnegative coefficient below zero and does not rename the metric.

- **before:** `A_echo = 0`;
- **after:** `A_echo = 0`;
- **frozen-metric movement:** none;
- **consecutive metric-unchanged runs since the last movement:** `2`;
- **stuck recoveries used:** `0`.

The source-level verdict nevertheless changes decisively because the printed conjecture has a topology/support obstruction independent of `A_echo`. This is not recorded as metric movement.

---

# 5. Method #1 — CHANGE THE CATEGORY: total variation on whole trees versus projective/local laws

The preceding run proved the finite-transcript comparison for every fixed cutoff and identified survival as the obstruction to extending the cutoff to the entire cluster when `rho(M)>1`. The new question was whether that was merely a limitation of the proof route or whether the **source's target topology itself is impossible**.

It is the latter.

Let `C_(n,delta)` be the failed cluster of the root in the finite graph `G_n`, viewed in the same rooted-graph state space as the target GW genealogy `T_M`. Since `G_n` is finite,

`P( |C_(n,delta)| < infinity ) = 1`                                      (5.1)

for every `n` and every saturation margin `delta`, regardless of coupling strength or the SDE dynamics.

Let

`s(M) := P( |T_M| = infinity )`

be the survival probability of the target multitype GW law. In every supercritical parameter point `rho(M)>1`, the source's own Theorem 3.1 gives

`s(M) > 0`.                                                            (5.2)

Use the measurable event

`I := { rooted genealogy is infinite }`.

Then

`P(C_(n,delta) in I) = 0`,
`P(T_M in I) = s(M)`.

By the variational definition of total variation,

`d_TV( Law(C_(n,delta)), Law(T_M) ) >= s(M)`                            (5.3)

for **every** `n,delta`.

But Conjecture 11.8 demands

`d_TV <= C ( epsilon(delta) + eta_n )`,                                (5.4)

with `epsilon(delta) -> 0` and `eta_n -> 0`. For any fixed supercritical source parameter point and fixed finite constant `C`, the right side of (5.4) tends to zero along the conjecture's stated limits, contradicting (5.3).

This does not depend on echoes, dissipativity, local cycles, or a delicate SDE estimate. It is a support mismatch between a random object that is **always finite** and a target law with **positive mass at infinity**.

## Proposition `NM13-11-H0003-SUPPORT-OBSTRUCTION-06`

Let `(mu_n)` be arbitrary probability laws supported on finite rooted graphs, and let `nu` be any law on locally finite rooted graphs with

`nu(|T|=infinity)=s>0`.

Then for every `n`,

`d_TV(mu_n,nu) >= s`.

Consequently the literal full-tree total-variation statement of H0003 / Conjecture 11.8 is false at every source-valid parameter point with `rho(M)>1`.

### Proof

Take the measurable set `I={|T|=infinity}`. Then `mu_n(I)=0` and `nu(I)=s`. Hence

`d_TV(mu_n,nu) = sup_A |mu_n(A)-nu(A)| >= |mu_n(I)-nu(I)| = s`.

For the source application, `mu_n=Law(C_(n,delta))`, `nu=Law(T_M)`, and `s=s(M)>0` by the source's standard supercritical GW criterion. `QED`

### Scope discipline

This refutes the **printed source statement as stated**. It does not assert that the author's intended mathematical idea is false. Several nearby corrected formulations are viable:

1. local/projective convergence of every fixed number of generations;
2. total variation after truncating the genealogy at a fixed depth or fixed size;
3. total variation conditional on extinction in the supercritical regime, if the intended target is adjusted accordingly;
4. a finite-size branching approximation rather than an infinite supercritical GW law.

The source's sentence calling full-tree TV "equivalent" to finite-generation front-Markovity is therefore too strong in the supercritical regime: full-tree TV implies all finite-generation marginals, but the converse fails when probability mass can escape to infinity.

**Outcome of method #1:** **decisive success.** Changing the topology exposes a literal support contradiction in the full-tree TV claim and identifies the natural repair.

---

# 6. Method #25 — COUNT THE SAME THING TWICE: finite-genealogy mass

The same obstruction has an exact counting interpretation that makes clear why no analytic echo estimate can repair the printed statement.

Let `F` be the countable/standard-Borel collection of **finite** rooted typed genealogies. Under the finite-graph cascade,

`sum_(tau in F) P(C_(n,delta)=tau) = 1`.                              (6.1)

Under a supercritical multitype GW law,

`sum_(tau in F) P(T_M=tau) = q(M) = 1-s(M) < 1`,                      (6.2)

where `q(M)` is the extinction probability.

Thus exactly `s(M)` units of target probability mass sit on infinite genealogies, while the finite-graph law puts zero mass there. No rearrangement among finite trees can erase this deficit. Equation (5.3) is the measure-theoretic form of this double count.

This also clarifies an internal scope tension in the source. Proposition 9.1 is an exact statement on the **infinite Bethe lattice** and therefore can genuinely produce an infinite supercritical GW cluster. Conjecture 11.8, however, prints its TV comparison for the cluster law in the **finite graphs `G_n`**. Exactness on the infinite limiting tree does not imply full-tree TV convergence from finite approximants in the supercritical phase.

I do not call the Bethe calculation false. The issue is the transfer topology from finite graphs to an infinite surviving genealogy.

**Outcome of method #25:** **decisive success.** Counting total finite-tree mass on both sides gives the same nonvanishing lower bound and shows the obstruction cannot be removed by improving the echo estimate.

---

# 7. Method #19 — MAKE IT AN ALGORITHM: a corrected all-regime finite-generation theorem

The refutation suggests the right replacement: reveal only a fixed number of generations. The previous finite-horizon comparison can then be made into a deterministic reveal algorithm that works even when the target GW process is supercritical.

I state and prove this on the same bounded-degree source-valid subclass used by the preceding NM13-11 runs. This is a **repair theorem**, not a claim that the full source is true after silently changing its topology.

For a rooted genealogy `T`, let `Tr_L(T)` denote truncation after generation `L`.

## Theorem `NM13-11-H0003-PROJECTIVE-REPAIR-07`

Assume the source saturated regime on finite rooted graphs `(G_n,o_n)` with

`deg(G_n) <= Delta < infinity`

and marked local weak convergence to the source UGW tree. Keep the finite source type set and all fixed admissible SDE parameters. Impose **no condition** on

`kappa = gamma_max L_sigma Delta / alpha_min`

and **no condition** on `rho(M)`.

Then for every fixed integer `L>=0`,

`lim_(delta->infinity) limsup_(n->infinity)
 d_TV( Law(Tr_L C_(n,delta)), Law(Tr_L T_M) ) = 0`.                  (7.1)

In particular, the true cascade converges to the multitype GW genealogy in the projective/local sense of every fixed finite set of generations, including throughout the supercritical regime. This does **not** imply full-tree total-variation convergence and does not identify the finite-graph survival/giant-cluster probability.

### Proof

Put

`c := gamma_max L_sigma`,
`lambda := c Delta - alpha_min`.

#### Step 1: deterministic transcript size

A rooted graph of maximum degree `Delta` contains at most

`V_L := 1 + Delta sum_(j=0)^(L-1) (Delta-1)^j`                       (7.2)

vertices through depth `L` (with the empty sum interpreted as `0`). A breadth-first algorithm that determines all failures through generation `L` therefore needs at most the deliberately loose deterministic number

`N_L := Delta V_L`                                                    (7.3)

of one-edge transmission decisions. This bound is independent of whether the ideal branching process is subcritical, critical or supercritical.

#### Step 2: cut off long one-cell decisions

Because the source has finitely many types, uniformly nondegenerate diffusion coefficients and bounded drift while an active cell remains between the safe and failure barriers, the one-cell decision time is tight uniformly over the finitely many source types and over the bounded forcing range used in the saturated comparison. Let

`q(T) -> 0`

be a uniform upper bound on the probability that one such decision lasts longer than `T`.

By the union bound, the probability that any of the first `N_L` decisions exceeds `T` is at most

`N_L q(T)`.                                                           (7.4)

Fix `T` for now. On the complementary event, a sequential comparison of the entire depth-`L` reveal transcript needs time at most

`H_L := N_L T`.                                                       (7.5)

#### Step 3: finite-horizon echo bound, with no sign condition

Reuse the source-derived synchronous comparison inequality established in the preceding NM13-11 reports. If

`x_v(t)=|s_v(t)-s_tilde_v(t)|`,

then up to the stopped transcript

`D^+ x(t) <= (-alpha_min I + c A_n) x(t) + g(t)`                     (7.6)

coordinatewise, with same initial state and

`||g(t)||_infinity <= gamma_max epsilon(delta)`.                     (7.7)

Since every row sum of `A_n` is at most `Delta`, positivity of the Metzler semigroup yields for `t<=H_L`

`||x(t)||_infinity
 <= gamma_max epsilon(delta) J_(H_L)(lambda)`,                        (7.8)

where

`J_H(lambda) = integral_0^H exp(lambda u) du`

is finite for every fixed `H`, regardless of the sign of `lambda`.

Thus the drift seen by the currently tested child differs from the directed idealisation by at most

`r_(L,T)(delta)
 := gamma_max epsilon(delta)
    [1 + c Delta J_(H_L)(lambda)]`.                                  (7.9)

For fixed `L,T`, `r_(L,T)(delta) -> 0` as `delta->infinity` even in arbitrarily strong fixed coupling.

#### Step 4: couple each reveal decision

The source's finite-horizon first-passage stability lemma gives, for each fixed `T`, a finite common constant `C_FP(T)` over the finite type set such that a bounded drift perturbation of size `r` changes the one-cell transmission probability by at most `C_FP(T) r`.

Hence, conditional on a locally tree-like marked neighbourhood and on all relevant decisions finishing by time `T`, maximal coupling at each reveal step gives total mismatch probability at most

`N_L C_FP(T) r_(L,T)(delta)`.                                        (7.10)

Let `eta_(n,L)^loc` be the optimal coupling error for the finite marked neighbourhood large enough to contain every vertex touched by the depth-`L` transcript. Marked local weak convergence gives

`eta_(n,L)^loc -> 0`                                                   (7.11)

for each fixed `L`.

Combining (7.4), (7.10), and (7.11),

`d_TV( Law(Tr_L C_(n,delta)), Law(Tr_L T_M) )
 <= eta_(n,L)^loc
    + N_L q(T)
    + N_L C_FP(T) r_(L,T)(delta).`                                   (7.12)

First let `n->infinity`, then `delta->infinity`, with fixed `L,T`. The first and third terms vanish. Then let `T->infinity`; the second term vanishes by `q(T)->0`. This proves (7.1). `QED`

### Consequence: the correct finite-generation Front-Markov statement

For any fixed `L`, every finite collection of generation-to-generation transition decisions converges jointly to the corresponding GW decisions. In particular, conditional independence across parents and siblings holds asymptotically for every fixed set of generations, with no dissipative restriction and no subcritical/critical restriction on `rho(M)` on this bounded-degree slice.

What fails in the supercritical phase is only the upgrade from this projective statement to total variation of the **entire** genealogy. The event of infinite survival is invisible to every fixed truncation and is exactly where the support deficit lives.

**Outcome of method #19:** **success.** Writing the front as a finite-depth reveal algorithm proves the natural corrected projective statement in all branching regimes on the bounded-degree source-valid class.

---

# 8. What this decides, and what it does not

## 8.1 Literal source verdict

On the source's printed quantifiers, H0003 / Conjecture 11.8 is **REFUTED AS WRITTEN**: at every fixed supercritical parameter point,

`d_TV( finite-graph failed cluster, supercritical infinite-GW genealogy ) >= survival_probability > 0`,

while the conjectured right side tends to zero.

This is a refutation of the source statement itself, not of a stronger invented constant and not of one proof route.

## 8.2 Intended mathematical problem after correction

A corrected supercritical statement could ask for projective/local convergence, finite-depth TV, extinction-conditioned TV, or a finite-size branching approximation. The theorem above establishes the fixed-depth/projective version on the bounded-degree source-valid class without any echo-contraction condition.

The stronger source-interest questions remain genuinely nontrivial after this correction:

- a **uniform** critical-window rate of order `epsilon(delta)+eta_n`, rather than the iterated fixed-cutoff convergence already proved by NM13-11;
- an appropriate supercritical finite-size statement controlling giant-cascade/survival probabilities;
- unbounded-degree UGW limits.

Those are not silently declared solved by the literal refutation.

## 8.3 Why the previous route stopped exactly here

The fifth report observed that for `rho(M)>1`, any size cutoff leaves a positive survival tail. That report treated this as a limitation of the finite-transcript proof. The present topology check shows it is stronger: for full-tree total variation from finite graphs, the same survival tail is a **mathematical lower bound on the target distance**. No improved echo estimate can remove it.

---

# 9. Prior-art / current-status qualification

Dated bounded search: 2026-09-18 UTC.

Queries/scope:

- exact source title and arXiv id `2608.15987`;
- `Conjecture 11.8`, `Front-Markov`, `strong coupling`, `total variation`, `supercritical`;
- author name and later work;
- companion arXiv `2608.21125`;
- sparse interacting-process local weak convergence / locality literature.

Results:

- arXiv:2608.15987 remains v1 dated 17 August 2026 and still prints Conjecture 11.8 in the form used above;
- arXiv:2608.21125 (21 August 2026) addresses different front/continuous-type questions and does not correct this scope;
- no later source-matching correction or resolution was recovered in the bounded search;
- Oliveira--Reis--Stolerman and Lacker--Ramanan--Wu are prior art for local/fixed-time continuity of interacting systems on sparse graphs, not for this absorbing-threshold projective theorem;
- the support argument `finite approximants versus positive mass at infinity in TV` is elementary and should be treated as **folklore**, not as a novelty claim.

Publication novelty of the projective repair theorem is **UNVERIFIED**. The report's value is primarily source correction and a rigorous source-valid repair, not a claim of a new general probability principle.

---

# 10. Closure, audits, and next step

The mathematical source statement is now labelled **REFUTED AS WRITTEN**, but repository closure is **not** declared because the required independent audits have not occurred.

Required outside audits remain:

1. P26 — end-to-end source-scope and proof audit;
2. NM13-12 — independent secondary audit, specifically checking that the literal finite-`G_n`/infinite-GW state spaces and the source's supercritical quantifier are read correctly.

No audit is presumed to pass. No paper folder is created before those audits. No checker-only artifact is created: the decisive claim is a theorem-sized support argument with its complete proof on this page, and the repair theorem is likewise proved on the page.

The next useful action is **audit/intent verification, not another echo lemma**. In particular, an auditor should check whether the author intended an unstated truncation, extinction conditioning, or local topology. If not, the literal refutation is complete mathematically; if yes, that corrected statement becomes a distinct target and must be frozen explicitly rather than silently substituted for Conjecture 11.8.

This run does not trigger Section-I: `A_echo` has been unchanged for two runs since its last movement, not three. More importantly, the printed source statement has now been decided, so metric stagnation must not be used to manufacture unrelated lemmas while audits are pending.

---

# 11. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  category: HARD_OUTSIDE
  source_id: H0003
  canonical_dedup_key: arxiv_2608_15987::conjecture_11.8
  claim_id: H0003
  claim_path: operations/claims/H0003.md
  source_status_before: OPEN
  source_status_after: REFUTED_AS_WRITTEN_AUDIT_PENDING
  source_verdict_movement: true
  metric_name: A_echo
  metric_before: 0
  metric_after: 0
  metric_movement: false
  metric_scope: bounded-degree locally-tree-like source-valid slice previously proved by NM13-11
  methods_attempted: [1, 19, 25]
  method_outcomes:
    1: "success: whole-tree TV is impossible in any supercritical parameter point; natural corrected category is projective/local convergence"
    19: "success: finite-depth reveal algorithm proves all-regime fixed-generation TV convergence on the bounded-degree source-valid slice"
    25: "success: total finite-genealogy mass is 1 for every finite G_n cluster but extinction mass q(M)<1 for supercritical GW, giving exact TV deficit s(M)"
  theorem_claims:
    - NM13-11-H0003-SUPPORT-OBSTRUCTION-06
    - NM13-11-H0003-PROJECTIVE-REPAIR-07
  unchanged_runs_since_metric_movement: 2
  stuck_recoveries_used: 0
  outside_audits_completed: []
  audits_required_for_closure: [P26, NM13-12]
  closure_status: NOT_CLOSED_AUDITS_PENDING
  checker_artifact: null
  checker_reason: "no finite enumeration claim; both decisive claims have complete written proofs on report page"
  literature_check_date: 2026-09-18
  literature_check_result: "source still v1; companion does not repair Conjecture 11.8; no later source-matching correction recovered in bounded search; support mechanism folklore; projective-repair novelty unverified"
  next_step: "Independent P26 and NM13-12 audits of literal source scope/support argument. Do not replace the source silently by a local/projective conjecture; if author intent requires such a correction, freeze it as a distinct target after audit."
```

No shared root, peer file, claim file, schedule, audit verdict, or public posting was changed in this invocation.

**End of complete run report.**