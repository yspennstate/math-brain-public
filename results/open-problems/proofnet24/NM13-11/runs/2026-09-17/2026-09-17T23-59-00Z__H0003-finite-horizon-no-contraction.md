Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MOVEMENT in the frozen `A_echo` metric: on the same bounded-degree, Benjamini–Schramm-to-tree, strictly subcritical source class, the previously required coefficient `2*sqrt(Delta_max-1)` can be replaced by `0`, meaning that no linear echo-stability inequality is needed at all for the iterated-limit front reduction. Methods actually tried this run: #11 DUALIZE, #15 BREAK THE SYMMETRY ON PURPOSE, #22 READ THE FAILURES, NOT THE SUCCESSES.**

# NM13-11 fourth run — H0003 finite-horizon cutoff removes the echo-contraction condition in the strictly subcritical regime

Date: 2026-09-17 UTC  
Track: `NM13-11` / HARD OUTSIDE  
Repository: `yspennstate/math-open-problems`, branch `master`  
Canonical source/claim: `H0003` / `operations/claims/H0003.md`  
Canonical dedup identity: `arxiv_2608_15987::conjecture_11.8`, residue 10 mod 13  
Overall source status: **OPEN**  
Local status after this run: **PARTIAL; full bounded-degree strictly-subcritical saturated slice now covered without any `kappa`/echo-contraction restriction**

## 1. Runtime honesty and control-plane status

The requested task header asks for GPT-6 with maximum reasoning. That is not what I can verify ran. The actual model exposed to this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The exposed task-control surface still has prompt/title, schedule or relative offset, timing mode, and enabled-state controls, but **no bindable model-family selector and no reasoning-effort selector**. Hence `GPT-6 / maximum` remains prompt text rather than a scheduler-enforced setting here. Making it binding requires an authorized scheduler/product surface that actually exposes model and reasoning fields. I did not create, disable, or modify any schedule.

Current `RESULTS.md` also corrects the old P26 permission story: one historical context returned `You cannot modify this task`, while a later authorized context successfully updated P26. Thus a future refusal is task/context specific, not evidence of global immutability. The lawful workaround is the owning account/workspace or another authorized product/admin/support surface; duplicating the task or bypassing ACLs is not acceptable.

## 2. Continuity recovered before new mathematics

This is a continuation of the live H0003 assignment, not a new admission. The create-only claim `operations/claims/H0003.md` still names NM13-11 as the exclusive owner, and no release, handoff, retirement, POSTED entry, source closure, or outside audit for H0003 was recovered.

Before working I reread or targeted-search-recovered the owner-required current surfaces:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the H-intake/verification material for arXiv:2608.15987;
- `operations/claims/H0003.md`;
- all three preceding NM13-11 reports, newest first;
- newest neighboring reports for NM13-10 and NM13-12;
- targeted repository searches for H0003 ownership, aliases, audits, handoffs, attempts, and later source-status corrections.

The newest prior NM13-11 report is

`proofnet24/NM13-11/runs/2026-09-17/2026-09-17T22-53-04Z__H0003-local-tree-semigroup.md`.

It proved `NM13-11-H0003-LOCAL-TREE-ECHO-03`, replacing the source row-sum coefficient `Delta_max` by the local-tree coefficient

`a_Delta = 2*sqrt(Delta_max-1)`

on bounded-degree locally-tree-like instances with ideal offspring mean matrix `rho(M)<1`, provided

`alpha_min > gamma_max L_sigma a_Delta`.

The second run's `NM13-11-H0003-PF-COBOUNDARY-TV-02` remains complementary: it is a critical branching-process perturbation lemma for a special Perron-coboundary score and did not change `A_echo`.

Large repository surfaces are connector-bounded, so I do not claim an omniscient byte-for-byte reread. The source-specific continuity needed here was accessible.

## 3. Fresh source and literature check

Dated bounded check: **2026-09-17 UTC**.

The exact source remains Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1, submitted 17 August 2026. Its abstract still says that the front reduction is unconditional only in the dissipative regime `kappa<1` and that the strong-coupling regime remains open. The source's Conjecture 11.8 asks for the saturated front-Markov / multitype-Galton–Watson reduction in the full regime, including strong coupling and critical-window uniformity.

A fresh exact-title / author / arXiv search still recovered only v1 as the source. The companion Kumar–Duddala paper arXiv:2608.21125v1 (21 August 2026) develops front propagation/Bramson and continuous-type questions; it does not close Conjecture 11.8. No source-matching later theorem was recovered in this bounded search. This is bounded negative evidence, not a worldwide-openness or novelty certificate.

For the method diagnosis I also checked the pre-existing sparse-diffusion literature. Oliveira–Reis–Stolerman, arXiv:1812.11924 / EJP 25 (2020), prove a fixed-time locality lemma for Lipschitz interacting diffusions: influence from a graph boundary at radius `r` is bounded by a term of the form

`C |partial B_r| exp(-(r-s) log(r-s))`

on a fixed time interval. Lacker–Ramanan–Wu, arXiv:1904.02585, prove continuity of interacting-process laws under local weak convergence, and their arXiv:2009.11667 work develops marginal dynamics on UGW trees. These papers do **not** directly prove the absorbing-threshold statement here, and I do not import them across the discontinuous first-passage event. They are prior art for the conceptual fact that fixed-time local behavior need not require a dissipative contraction. The proof below instead uses the source's own stopped comparison inequality and first-passage stability lemma.

Novelty of the synthesis below is **UNVERIFIED**.

## 4. Frozen metric and exact movement

The metric remains exactly the claim-file metric:

`A_echo` = the coefficient in a rigorously proved sufficient linear echo-stability condition

`gamma_max * L_sigma * A_echo < alpha_min`

that is actually carried through to a source-relevant front-decoupling theorem.

Historical values:

- source Theorem 11.5: `A_echo = Delta_max`;
- first NM13-11 theorem on a uniform-global-spectral subclass: `A_echo = Lambda_*`;
- third run on the bounded-degree BS-to-tree strictly-subcritical class: `A_echo = 2*sqrt(Delta_max-1)`.

This run proves that, **on that same bounded-degree BS-to-tree strictly-subcritical class**, no such linear echo-stability inequality is needed at all. In the frozen sufficient-condition normalization this means

`A_echo : 2*sqrt(Delta_max-1)  --->  0`.

The interpretation is important: `0` does **not** assert that physical echoes vanish. It means that the iterated-limit theorem below holds for every fixed finite coupling strength permitted by the source assumptions, irrespective of the sign of

`alpha_min - gamma_max L_sigma Delta_max`.

This is genuine movement and not a metric change.

The full source conjecture remains open because the constants in the proof below explode with the cutoff horizon and do not give the source's uniform critical-window rate or a joint `n,delta` estimate. Unbounded degrees also remain uncovered.

---

# 5. Method #11 — DUALIZE: replace the infinite cascade by a finite decision transcript

The preceding route treated the echo through an infinite-time resolvent. That is exactly where positivity of a spectral gap such as

`alpha_min - c a_Delta > 0`,  with `c = gamma_max L_sigma`,

entered. I dualized the law-comparison problem before applying the resolvent.

For total variation, it suffices to construct one coupling of the true cascade and the ideal directed/GW exploration and bound the probability that their **finite decision transcripts** disagree. Stop both breadth-first explorations at the first of:

1. a mismatch;
2. discovery of `K` failed vertices;
3. any active one-cell transmission decision lasting longer than `T`.

Before this stopping event, at most

`N_K := 1 + Delta_max K`

one-cell transmission decisions can matter. A deliberately loose deterministic upper bound on elapsed comparison time is therefore

`H := N_K T`.

The decisive observation is that after `K,T` are frozen, **the comparison only needs a finite-time semigroup, not an infinite-time resolvent**.

### Lemma 5.1 — finite-horizon echo bound with no contraction hypothesis

Put

`c := gamma_max L_sigma`, `alpha := alpha_min`, `Delta := Delta_max`,

and let `A=A(G_n)`. Reuse the source-derived synchronous comparison inequality from the preceding report:

`D^+ x(t) <= (-alpha I + c A) x(t) + g(t)`                         (5.1)

coordinatewise up to the stopped exploration, where `x_v(t)=|D_v(t)|`, the two systems start from the same state, and

`0 <= g_v(t) <= gamma_max epsilon(delta)`.

Let

`lambda := c Delta - alpha`

and define

`J_H(lambda) := integral_0^H exp(lambda u) du
              = (exp(lambda H)-1)/lambda`, if `lambda != 0`,
`J_H(0) = H`.

Then for every `t<=H`,

`||x(t)||_infty <= gamma_max epsilon(delta) J_H(lambda)`.          (5.2)

No sign condition on `lambda` is required.

#### Proof

The matrix `-alpha I+cA` is Metzler, so variation of constants is positive. Since every row sum of `A` is at most `Delta`,

`||exp[(-alpha I+cA)u]||_(infty->infty) <= exp((cDelta-alpha)u)`.

Therefore

`||x(t)||_infty
 <= integral_0^t exp(lambda(t-s)) ||g(s)||_infty ds
 <= gamma_max epsilon(delta) J_H(lambda)`.

The integral is finite for every fixed `H`, even when `lambda>0`. QED.

This is the whole new mechanism. The old `1/g_tree` denominator arose only after allowing the time integral to run to infinity. Once long decisions and large clusters are charged to cutoff tails first, the finite-horizon integral is finite for every fixed strong-coupling parameter.

### Lemma 5.2 — one-decision mismatch on the cutoff event

The interaction drift difference at an active vertex is bounded by

`r_H(delta)
 <= gamma_max epsilon(delta)
    + c Delta ||x||_infty
 <= gamma_max epsilon(delta) [1 + c Delta J_H(lambda)]`.           (5.3)

The source's Lemma 11.3 is precisely a bounded-horizon first-passage stability statement under a bounded drift perturbation. Because there are finitely many source types, for each fixed `T` there is a common constant `C_FP(T)` such that, for all sufficiently large `delta`, the true and directed decision can be coupled with mismatch probability at most

`C_FP(T) r_H(delta)`.                                              (5.4)

Nothing in (5.2)--(5.4) asks `lambda<0`, `kappa<1`, or `alpha>c a_Delta`.

Outcome of method #11: **success**. Moving to finite stopped transcripts replaces an infinite resolvent by a finite semigroup integral and eliminates the contraction hypothesis for the strict-subcritical iterated limit.

---

# 6. Method #15 — BREAK THE SYMMETRY ON PURPOSE

I tested whether the preceding observation was secretly a regular-tree/symmetric-adjacency artefact by forcing a two-type asymmetric system.

On a bipartite semiregular tree, suppose type `A` vertices have `d_A` opposite-type neighbors and type `B` vertices have `d_B`, with possibly unequal dissipation and directed Lipschitz coupling bounds. The type-envelope comparison has generator

`Q = [ -alpha_A,       d_A c_AB
      d_B c_BA,       -alpha_B ]`.

Its upper eigenvalue is

`lambda_+(Q)
 = -(alpha_A+alpha_B)/2
   + sqrt( ((alpha_A-alpha_B)/2)^2 + d_A d_B c_AB c_BA )`.

For strong enough asymmetric coupling, `lambda_+(Q)>0`; hence every infinite-time contraction argument fails. Nevertheless on a fixed horizon `H`,

`||int_0^H exp(Qs) ds|| < infinity`,

and an `O(epsilon(delta))` forcing still produces an `o(1)` perturbation as `delta->infinity` for fixed `H`.

The full vertex-level proof in Lemma 5.1 is stronger: it only uses the maximum row sum `Delta` and bounded coupling, so it automatically covers this asymmetric test without diagonalizing `Q`.

Outcome of method #15: **success as a falsification test for the route**. The cutoff argument survives a deliberately asymmetric two-type setting even when the finite-time error grows exponentially in `H`. Thus the new theorem is not an artefact of regular-tree symmetry or the `2 sqrt(Delta-1)` spectral estimate.

---

# 7. Method #22 — READ THE FAILURES, NOT THE SUCCESSES

I then asked why the source needed `kappa<1` if the finite-horizon estimate is this simple.

The answer is visible in the quantifiers. The source seeks a reduction uniform enough to pass through the critical window and to avoid a bad joint condition such as `n epsilon(delta_n)->0`. At criticality there is no exponential progeny tail, and a cutoff `K` capable of making the unexplored cluster negligible must diverge. Then the finite-horizon constant

`J_H(lambda)` with `H~KT`

can grow like `exp((cDelta-alpha)KT)` in strong coupling. Thus the order

`fix K,T  ->  delta->infinity`

is harmless, while the source's desired uniform limit with `K` diverging is not.

This diagnosis matches the closest older sparse-diffusion results. Oliveira–Reis–Stolerman obtain very strong locality on every **fixed** time interval without a source-style `kappa<1` condition; Lacker–Ramanan–Wu similarly obtain continuity under local weak convergence for fixed interacting-process systems. Those successes stop exactly before the present source's critical-window/unbounded-exploration issue. I therefore do not treat them as a proof of the threshold theorem; they isolate the missing uniformity.

Outcome of method #22: **success diagnostically**. The obstruction is not strong coupling at fixed subcritical cutoff. It is controlling strong coupling while the exploration/time cutoff itself diverges, especially as `rho(M) -> 1`.

---

# 8. Main theorem — all fixed strong coupling in the bounded-degree strict-subcritical slice

## Theorem `NM13-11-H0003-FINITE-HORIZON-NOCONTRACTION-04`

Let `(G_n,o_n)` be the bounded-degree finite rooted graph sequence in the source setting, with

`deg(G_n) <= Delta < infinity`,

and assume its marked rooted neighborhoods converge in the source's Benjamini–Schramm/local-weak sense to the stated unimodular random tree. Assume the source's saturated regime and finite type set, and let `M` be the ideal multitype Galton–Watson mean matrix. Suppose only

`rho(M) < 1`.                                                       (8.1)

Keep all fixed source parameters finite and admissible, including `alpha_min>0`, `gamma_max<infinity`, and `L_sigma<infinity`, but impose **no condition** on

`kappa = gamma_max L_sigma Delta / alpha_min`.

Then the failed cluster of a uniformly rooted finite graph converges in total variation to the source's ideal finite-type Galton–Watson genealogy in the iterated limit

`lim_(delta->infinity) limsup_(n->infinity)
 d_TV( Law(S_(n,delta)), Law(S_GW) ) = 0`.                          (8.2)

In particular, throughout this bounded-degree strictly-subcritical source slice, the front reduction holds for every fixed strong-coupling value `kappa>=1` as well as for `kappa<1`.

A stopped quantitative form is the following. Let `epsilon=epsilon(delta)` be the source's cellwise saturation error, let `N_K=1+Delta K`, `H=N_K T`, `lambda=cDelta-alpha`, and let `eta_(n,K+1)` denote the finite-radius local-coupling error already used in the source/local-weak reduction (so for each fixed `K`, `eta_(n,K+1)->0`). Then constants `C_exit,lambda_exit>0` and the source first-passage constant `C_FP(T)` give

`d_TV( Law(S_(n,delta)), Law(S_GW) )
 <= P(|S_GW|>K)
    + eta_(n,K+1)
    + N_K C_exit exp(-lambda_exit T)
    + N_K C_FP(T) gamma_max epsilon(delta)
      [1 + c Delta J_H(lambda)]`.                                  (8.3)

The constants in (8.3) are not asserted uniform in `K,T`.

### Proof

**Step 1: strict subcriticality supplies the cluster cutoff.**  
The ideal process has finitely many types and bounded offspring because the source graph degree is bounded. Under `rho(M)<1`, its total progeny has an exponential tail. This fact was already used in the preceding report; equivalently, the finite-type bounded-offspring total-progeny generating functions are analytic at a point strictly larger than one because the Jacobian at the fixed point `1` is `M` with spectral radius below one. Hence for every `zeta>0` one can first choose `K` so that

`P(|S_GW|>K) < zeta`.                                               (8.4)

**Step 2: cap long one-cell decisions.**  
The preceding report proved, using bounded drift on the decision interval and the source's uniformly nondegenerate finite-type diffusion coefficients, a uniform exponential tail for an active one-cell transmission decision. Thus after `K` failures, a union bound over at most `N_K` relevant decisions gives

`P(any relevant decision lasts >T)
 <= N_K C_exit exp(-lambda_exit T)`.                               (8.5)

For the fixed `K`, choose `T` so that (8.5) is below `zeta`.

**Step 3: on the cutoff event, compare true and directed dynamics for finite time only.**  
The deterministic elapsed comparison horizon is at most `H=N_KT`. Lemma 5.1 gives the pathwise state discrepancy (5.2) for **every** sign of `lambda=cDelta-alpha`. Consequently the perturbation of the drift of each active decision is bounded by (5.3). Applying the source's bounded-horizon first-passage stability Lemma 11.3 and union-bounding the `N_K` decisions yields the final term in (8.3).

For the already fixed `K,T`, the factor

`N_K C_FP(T) gamma_max [1+cDelta J_H(lambda)]`

is a finite number. Since the saturated source has `epsilon(delta)->0`, this entire mismatch contribution tends to zero as `delta->infinity`, regardless of whether `lambda` is negative, zero, or positive.

**Step 4: identify the directed finite transcript with the ideal GW transcript.**  
Up to `K` discovered failures, only a finite rooted neighborhood is inspected. Couple that marked neighborhood to the source limiting tree using the same finite-radius local convergence term as in the source/preceding report. The coupling fails with probability at most `eta_(n,K+1)`, which goes to zero as `n->infinity` for fixed `K`. On a successful local coupling, the directed front exploration is exactly the first `K` vertices/offspring decisions of the source's ideal multitype GW construction.

**Step 5: convert transcript coupling to total variation.**  
If the local neighborhood couples, no decision exceeds `T`, the true/directed decisions never mismatch, and `|S_GW|<=K`, then the complete true failed cluster and the ideal GW cluster agree. The coupling characterization of total variation therefore gives (8.3).

Now take `n->infinity` with fixed `K,T,delta`, then `delta->infinity`; the local-coupling and saturation terms vanish. Finally use the previously selected `K,T` and let `zeta->0`. This proves (8.2). QED.

## 8.1 What this does and does not settle

The theorem is stronger than the preceding local-tree spectral theorem on the same strict-subcritical class: its hypothesis does not contain

`alpha_min > 2 gamma_max L_sigma sqrt(Delta-1)`

or any replacement contraction inequality.

It is still only **PARTIAL** relative to Conjecture 11.8. In particular it does not prove:

- uniform error `C(epsilon(delta)+eta_n)` through `rho(M)=1`;
- a joint `n,delta_n` limit with source-optimal quantitative rate;
- critical total-variation control when the needed `K` diverges;
- the full supercritical infinite-cluster statement;
- unbounded-degree UGW limits.

The proof makes the missing critical obstruction explicit: for `lambda>0`, the finite-horizon amplification behaves like `exp(lambda H)`, and `H` must grow with the exploration cutoff. A new critical argument has to cancel or avoid that growth rather than merely estimate it.

---

# 9. Prior-art / novelty discipline

Queries run on 2026-09-17 UTC included the exact source title/arXiv id, `strong coupling`, `front-Markov`, `Conjecture 11.8`, the Kumar–Duddala companion, and older combinations of `interacting diffusions sparse graphs locality local weak convergence`.

Recovered primary/near-primary works:

1. Kumar, arXiv:2608.15987v1 — source; strong-coupling reduction still stated open.
2. Kumar–Duddala, arXiv:2608.21125v1 — companion front/continuous-type work; not a resolution of Conjecture 11.8.
3. Oliveira–Reis–Stolerman, arXiv:1812.11924, EJP 2020 — fixed-time locality for sparse interacting diffusions, with the superexponential-in-distance locality factor described above.
4. Lacker–Ramanan–Wu, arXiv:1904.02585, Ann. Appl. Probab. 2023 — local weak convergence for sparse networks of interacting processes.
5. Lacker–Ramanan–Wu, arXiv:2009.11667, PTRF 2023 — marginal dynamics on UGW trees.

The finite-horizon Gronwall observation itself is elementary. I make **no novelty claim for finite-time Gronwall, cutoff coupling, or fixed-time locality**. The potentially new point is their exact use with the source's first-passage stability to remove the echo-contraction hypothesis from the complete bounded-degree strictly-subcritical saturated slice. A bounded search did not find that source-matching theorem, but publication novelty remains **UNVERIFIED**.

# 10. Counters, audit state, and next route

Because the frozen metric moved this run:

- `unchanged_runs = 0`;
- `stuck_recoveries_used = 0`;
- no handoff or rotation is triggered.

No P26 or NM13-12 audit is counted. This report is a self-proof, not an independent audit. No finite claim was introduced, so no exact-arithmetic checker was warranted; the theorem-sized argument is written in full above.

The next obligation is now sharply different from the previous one: **replace the exponentially growing finite-horizon factor by a critical quantity whose expectation remains summable while the exploration cutoff diverges**.

Next Section-B methods:

- **#3 PROVE SOMETHING STRONGER:** seek a critical estimate directly uniform in the exploration cutoff rather than patching strict-subcritical estimates as `rho(M)↑1`.
- **#12 FIND WHAT IS CONSERVED:** derive the Perron-weighted front-energy/mismatch martingale or supermartingale suggested by the source branching structure.
- **#27 SWAP THE QUANTIFIERS:** control expected mismatch generation-by-generation before summing over total cluster volume, instead of demanding a pathwise uniform bound over every explored vertex first.

# 11. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-11
  category: HARD_OUTSIDE
  source_id: H0003
  claim_path: operations/claims/H0003.md
  canonical_identity: arxiv_2608_15987::conjecture_11.8
  source_status: OPEN
  local_status: PARTIAL
  metric:
    name: A_echo
    meaning: sufficient graph-amplification coefficient in gamma_max*L_sigma*A_echo < alpha_min carried through to a source-relevant front-decoupling theorem
    scope: bounded-degree BS/local-weak-to-tree saturated finite-type instances with rho(M)<1, iterated n->infinity then delta->infinity
    before: 2*sqrt(Delta_max-1)
    after: 0
    after_interpretation: no linear echo-stability inequality is required on this restricted strict-subcritical scope; physical echo is not zero
    movement: true
  new_internal_theorem:
    id: NM13-11-H0003-FINITE-HORIZON-NOCONTRACTION-04
    statement: in the bounded-degree saturated finite-type source setting with rho(M)<1, the failed-cluster law converges in total variation to the ideal multitype GW law in the iterated n->infinity then delta->infinity limit for every fixed admissible coupling strength, with no kappa<1 or spectral echo-contraction condition
  methods_tried: [11, 15, 22]
  method_outcomes:
    11: success_finite_transcript_duality_replaces_infinite_resolvent_by_finite_semigroup
    15: success_two_type_asymmetric_positive_growth_test_still_converges_after_fixed_cutoff
    22: success_identified_diverging_cutoff_critical_uniformity_as_actual_remaining_obstruction
  unchanged_runs: 0
  stuck_recoveries_used: 0
  audits:
    P26: NOT_COUNTED
    NM13-12: NOT_COUNTED
  finite_checker: not_applicable_theorem_sized_analytic_claim
  literature_status: bounded_search_no_source_matching_resolution_found_novelty_unverified
  next_obligation: obtain a critical-window mismatch estimate uniform as the exploration cutoff diverges, ideally via Perron-weighted front energy rather than pathwise echo contraction
  next_methods: [3, 12, 27]
```
