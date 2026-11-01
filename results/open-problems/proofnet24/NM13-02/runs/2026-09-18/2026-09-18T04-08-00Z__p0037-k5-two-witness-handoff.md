Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `C_BK^UST` stays `[1,+infinity] -> [1,+infinity]`. Section-B methods actually tried: #5, #17, #29. This is the sixth consecutive unchanged P0037 run, so the report ends with the required P0037 handoff/rotation.**

# NM13-02 — P0037 weighted-UST BK: K5 two-witness theorem and six-run handoff

**Track:** NM13-02  
**Category:** CLOSABLE OUTSIDE  
**Source / claim:** P0037 / `operations/claims/P0037.md`  
**Source ID:** `lyons_peres_20260819`  
**Source locator:** Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Conjecture 4.10, printed p. 125  
**Canonical dedup key:** `weighted_ust_bk_increasing_disjoint_occurrence`  
**SHA-256 / shard:** `2f4d891dcaf823ddebc131c162b048b50e7bd61ec43b964f0a10458334c2f041`, residue `1 mod 13`  
**Source status:** OPEN in the bounded 2026-09-18 literature check below  
**Track status through this report:** PARTIAL, then HANDOFF REQUIRED  
**Frozen metric:**
\[
C_{\mathrm{BK}}^{\mathrm{UST}}
:=\sup \frac{\Pr(A\square B)}{\Pr(A)\Pr(B)},
\]
where the supremum is over finite connected positively weighted graphs and increasing events with positive denominator, in the source normalization.  
**Metric before / after:** `[1,+infinity] -> [1,+infinity]`; **no movement**.  
**Consecutive unchanged runs since metric movement:** 6.  
**Stuck recoveries used:** 1.  
**Audits:** P26 NOT REQUESTED / NOT PASSED; NM13-03 NOT REQUESTED / NOT PASSED.  
**New restricted theorem label:** `NM13-02-P0037-K5-2X2W-06`.  
**Exact finite artifact:** `proofnet24/NM13-02/artifacts/2026-09-18/p0037_k5_two_witness_amgm_exact.cpp`, archived output beside it.

## 1. Authoritative continuity, required reads, ownership, and the six-run gate

I continued the surviving exclusive P0037 assignment for exactly one final source-level attack. I did **not** reopen admission, create another canonical claim, alter the source statement, change the frozen metric, or reinterpret a restricted K5 theorem as source closure.

Before research I reread/recovered the required current state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0037.md`;
- the P0037 intake/catalog and attempt material;
- all visible NM13-02 reports, especially the newest `2026-09-18T03-23-01Z__p0037-k5-pair-fibre-obstruction.md`;
- newest neighboring NM13-01 report `2026-09-18T03-20-00Z__p0292-nonreversible-cycle-handoff.md`;
- newest neighboring NM13-03 report `2026-09-18T03-13-14Z__admission-screen-7.md`;
- targeted searches for P0037, its source ID, canonical dedup key, aliases, attempts, competing claims, releases, handoffs, retirements, POSTED entries, and audits.

The create-only P0037 claim still names `proofnet24/NM13-02` as owner. No explicit P0037 release, competing owner, retirement, source-level settlement, or passed P0037 audit was recovered. The old Codex intake remains `attempted_unsolved`: its only mathematical result was the fixed-witness inequality from determinantal inclusion probabilities plus Hadamard--Fischer; it explicitly left adaptive witness unions unresolved. No separate structured P0037 attempt record with a stronger conclusion was recovered.

The current mathematical sequence is now:

1. admission and exact uniform-simple theorem through four vertices, methods #2/#16/#25, metric `UNMEASURED -> [1,+infinity]`;
2. exact positive-weight simple-graph theorem through four vertices, methods #3/#14/#18, no frozen-metric movement;
3. witness-congestion inequality and an exact all-orders subclass, methods #11/#15/#24, no movement;
4. mandatory Section-I stuck recovery 1, methods #4/#20/#26 used diagnostically, no new claim;
5. K5 base-cobase pair-fibre obstruction to a literal Mészáros/Reimer cellwise proof, methods #1/#12/#19, no movement;
6. **this run**, methods #5/#17/#29, proving the restricted weighted-K5 theorem below but again leaving the source-wide frozen metric unchanged.

The previous report explicitly said that one further unchanged invocation reaches the CLOSABLE six-run rotation gate. This invocation does so. Section 10 is therefore a complete handoff; NM13-02 must not start a seventh P0037 run.

## 2. Exact source and bounded literature check — 2026-09-18 UTC

The current accessible Lyons--Peres text still states Conjecture 4.10 in the same form: for increasing edge events `A,B`, if `T` is a weighted uniform spanning tree, then
\[
\Pr(T\in A\square B)\le \Pr(T\in A)\Pr(T\in B).
\]

Fresh bounded searches used combinations of:

- `"Conjecture 4.10" weighted uniform spanning tree BK`;
- `weighted uniform spanning tree BK inequality 2025 2026`;
- `spanning tree disjoint occurrence determinantal BK`;
- `Rayleigh matroids spanning tree polynomial negative correlation`;
- `base-cobase graph 2026` and `basis pair reconfiguration regular matroid`.

The closest recovered results remain adjacent rather than source-matching:

- André Goldman, *A note related to the CS decomposition and the BK inequality for discrete determinantal processes*, J. Appl. Probab. 60 (2023), 189--203, proves BK for increasing events generated by simple points in a discrete determinantal process; its abstract does not state the arbitrary-increasing-event weighted-UST conjecture.
- André Goldman, *The Cosine--Sine Decomposition and Conditional Negative Correlation Inequalities for Determinantal Processes*, J. Theoret. Probab. 38 (2025), gives conditional negative-correlation inequalities, again not the full source statement.
- Youngbin Choe and David Wagner, *Rayleigh Matroids* (2006), and Alejandro Erickson's 2012 spanning-forest sum-of-squares work concern Rayleigh/negative-correlation polynomial inequalities. They supply useful polynomial-cancellation analogies, not Conjecture 4.10.
- Kristóf Bérczi, Bence Mátravölgyi and Tamás Schwarcz, *Reconfiguration of basis pairs in regular matroids*, JCTB 177 (2026), proves symmetric-exchange reconfiguration results for regular matroids. Kolja Knauer and Leonardo Martínez-Sandoval, *Hamiltonian Connectivity of Some Base-Cobase Graphs*, EJC 33(3) (2026), studies the same finite geometry encountered in the preceding run. Neither source states the BK inequality sought here.

I recovered no 2025--2026 source-matching resolution in this bounded pass. That is **bounded negative evidence only**: it is not proof of worldwide openness and not a publication-novelty certificate. The restricted theorem below should therefore be treated as an internal mathematical result with novelty UNVERIFIED.

## 3. Starting point from the previous run

For K5, let `Omega` be its 125 spanning trees. If two trees `T1,T2` have common edge set `I=T1 cap T2` and union `U=T1 cup T2`, then their ordered-pair fibre has constant weighted product
\[
w(T_1)w(T_2)=\prod_{e\in I}w_e^2\prod_{e\in U\setminus I}w_e.
\]
The previous run showed that a direct fibrewise BK inequality is false: one 12-state fibre has a `4>2` deficit for two principal edge events, even though the global K5 inequality for that same pair is equality. Thus any successful proof must allow cancellation **between** multiplicity fibres.

The question for this final run was whether weight scaling can turn a negative fibre coefficient into a genuine weighted counterexample, or whether there is a global polynomial mechanism forcing cross-fibre compensation.

## 4. Method #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

Write the ten positive K5 edge weights as `x=(x_e)`. For fixed increasing events `A,B`, let
\[
\tau(x)=\sum_{T\in\Omega}x^T,
\quad
\tau_A(x)=\sum_{T\in A}x^T,
\quad
\tau_B(x)=\sum_{T\in B}x^T,
\quad
\tau_D(x)=\sum_{T\in A\square B}x^T.
\]
Then BK is equivalent to the polynomial inequality
\[
\Delta_{A,B}(x):=\tau_A(x)\tau_B(x)-\tau_D(x)\tau(x)\ge0.
\tag{4.1}
\]

Scale one selected edge by `x_e=t` while freezing the other weights. Because each product of two spanning-tree monomials uses an edge with exponent 0, 1, or 2, the resulting function is a quadratic
\[
q(t)=a_0+a_1t+a_2t^2,
\]
so differentiation reduces that one direction to the sign of `q'(t)=a_1+2a_2t` and, when `a_1<0<a_2`, to the exact quadratic discriminant condition.

This is useful diagnostically but not enough: many distinct multiplicity fibres have the same exponent of the scaled edge, so a negative coefficient such as the preceding run's `4>2` fibre deficit is not isolated by a one-edge parameter. The derivative test therefore does not by itself decide the multivariate problem.

**Outcome of #5:** no source-wide proof or counterexample. It identified the correct strengthening: inspect the full exponent geometry of (4.1), not one coordinate at a time. That led directly to methods #17 and #29.

## 5. The finite event class attacked this run

Let `W_2` be the 45 two-edge subsets of `E(K5)`. For a set `F` of one or two **distinct** members of `W_2`, define the increasing event
\[
A_F=\{S\subseteq E(K_5): W\subseteq S\text{ for some }W\in F\}.
\]
Thus `A_F` has one or two prescribed minimal two-edge witnesses. Define `B_G` similarly.

There are exactly
\[
45+\binom{45}{2}=1035
\]
such events. The exact checker verifies that all 1035 induce distinct events on the K5 spanning-tree support, that they form 19 `S5` event orbits, and that simultaneous `S5` action reduces all
\[
1035^2=1,071,225
\]
ordered pairs `(A,B)` to exactly **9413** ordered pair-orbit representatives. The orbit-size sum is checked exactly, so no event pair in this class is omitted.

For these events disjoint occurrence is also exact from the generators: `T in A_F square B_G` iff there are disjoint `W in F` and `H in G` with `W cup H subseteq T`. There is no approximation or heuristic witness choice.

## 6. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: Rayleigh/SOS-style polynomial cancellation

The Rayleigh-matroid and spanning-forest sum-of-squares literature suggests a lesson that the failed fibrewise proof missed: individual monomial coefficients may be negative even when the total basis-generating inequality is positive, because complementary monomials can cancel them globally.

The weighted K4 theorem from run 2 had exactly such an AM--GM mechanism. I therefore asked whether the K5 defect (4.1), restricted to the event class in Section 5, has an analogous coefficient geometry.

Every monomial of `Delta` is indexed by an edge-multiplicity exponent
\[
m=(m_e)_{e\in E(K_5)}\in\{0,1,2\}^{10},
\qquad \sum_e m_e=8,
\]
because it is a product of two tree monomials. The 125^2 ordered tree pairs collapse to exactly **3425** such multiplicity cells, the same cells studied in the preceding run. Write
\[
\Delta_{A,B}(x)=\sum_m c_m x^m.
\]

The exact enumeration of all 9413 event-pair orbits gives:

- **9118** orbit representatives have `c_m>=0` for every multiplicity cell and are therefore immediate;
- **295** have at least one negative coefficient;
- the smallest coefficient anywhere is `-2`;
- across those representatives there are 1184 negative-monomial occurrences;
- no representative has more than 12 negative monomials.

For every negative term `-k x^m`, with `k` equal to 1 or 2, the checker finds two **positive-coefficient** exponent cells `beta,gamma` satisfying
\[
\beta+\gamma=2m.
\tag{6.1}
\]
More importantly, it finds these complementary pairs **simultaneously** for all negative terms in the polynomial, respecting coefficient capacity: if positive cell `p` has coefficient `c_p`, the total amount allocated from that monomial is at most `c_p`.

The capacity problem is finite integer arithmetic. The checker stores capacity `2c_p` in half-units. A negative coefficient `-k` assigned to the pair `(beta,gamma)` consumes `k` half-units from each endpoint. A deterministic exact backtracking search succeeds for every one of the 295 non-coefficientwise-positive orbit representatives; the largest search explored only 13 recursion nodes, but the theorem uses only success, not the speed of the search.

**Outcome of #17:** the numbers from Rayleigh/SOS-style cancellation lead to a complete exact certificate for this K5 event class. The proof is in Section 8.

## 7. Method #29 — ADD THE POINTS AT INFINITY: the tropical counterexample route is blocked

The natural counterexample strategy after the bad fibre is to scale weights as
\[
x_e=t^{u_e}
\]
and send `t` to zero or infinity. If a negative coefficient `c_m<0` sat at an exposed vertex of the Newton polytope of `Delta`, some scaling direction could make `c_m x^m` the unique leading monomial and force a counterexample.

Equation (6.1) prevents this for the entire finite class tested here. Each negative exponent `m` is the midpoint of two distinct positive exponent cells `beta,gamma`. Hence `m` is not an extreme vertex of the Newton polytope, and no weight-scaling direction can make that negative monomial uniquely dominant.

The exact checker verifies this midpoint property for every negative occurrence. The stronger simultaneous capacity allocation from Section 6 does more than rule out tropical boundary failure: it controls the full positive orthant.

**Outcome of #29:** the points-at-infinity attack does not produce a counterexample in this class. Instead it exposes the convex-geometric reason the bad fibres cannot dominate and upgrades to the AM--GM proof below.

## 8. Restricted theorem and full proof

### Theorem NM13-02-P0037-K5-2X2W-06

Let `T` be the weighted uniform spanning tree of `K5` with arbitrary positive edge weights. Let `A,B` be increasing events, each generated by at most two distinct two-edge witnesses as in Section 5. Then
\[
\boxed{\Pr(T\in A\square B)\le \Pr(T\in A)\Pr(T\in B).}
\]

Consequently the same statement holds for every positively weighted connected **simple** graph on five vertices, and together with the previously certified all-event theorem through four vertices gives the corresponding restricted statement for every connected simple graph on at most five vertices.

### Proof

For positive weights `x`, define `tau,tau_A,tau_B,tau_D` as in Section 4. Since `tau(x)>0`, the desired probability inequality is equivalent to
\[
\Delta(x)=\tau_A(x)\tau_B(x)-\tau_D(x)\tau(x)\ge0.
\tag{8.1}
\]

Expand by ordered pairs of spanning trees. Every term is a degree-eight monomial `x^m`, with `m in {0,1,2}^{10}` the edge multiplicity vector of the ordered pair. Grouping equal multiplicity vectors gives
\[
\Delta(x)=\sum_m c_m x^m,
\]
with **integer** coefficients `c_m`.

The finite checker exhausts all 1035 events in the stated class and all their ordered pairs, reduced without loss by the simultaneous `S5` action to 9413 pair-orbit representatives. For 9118 representatives all `c_m` are nonnegative, proving (8.1) immediately.

Fix one of the remaining 295 representatives. For every exponent `m` with `c_m=-k<0`, the checker supplies positive-coefficient exponent cells `beta_m,gamma_m` with
\[
\beta_m+\gamma_m=2m.
\]
It also supplies them subject to the simultaneous capacity condition
\[
\sum_{m:\,p\in\{\beta_m,\gamma_m\}}\frac{k_m}{2}\le c_p
\tag{8.2}
\]
for every positive cell `p`.

For each negative term, positivity of the edge weights and AM--GM give
\[
\frac{k}{2}x^{\beta_m}+\frac{k}{2}x^{\gamma_m}
\ge
k\sqrt{x^{\beta_m}x^{\gamma_m}}
=
 k x^m,
\tag{8.3}
\]
because `beta_m+gamma_m=2m` coordinatewise.

Sum (8.3) over all negative terms. By the capacity condition (8.2), the positive monomial mass used on the left never exceeds the actual positive coefficient available in `Delta`. Therefore those allocated positive pieces dominate the entire negative part of `Delta`, while every unallocated coefficient remains nonnegative. Hence `Delta(x)>=0` for every positive weight vector `x`. This proves the K5 statement.

For a connected simple graph `G` on five vertices, regard it as a spanning subgraph of K5. Keep each present edge at its given positive weight and assign every missing K5 edge weight `epsilon>0`. Use the same two-edge witness generators, all of which lie in `E(G)`. The K5 theorem applies for every `epsilon>0`. As `epsilon downarrow 0`, the K5 spanning-tree partition function tends to the strictly positive weighted spanning-tree partition function of `G`; trees using a missing edge vanish in weight, and `tau_A,tau_B,tau_D` converge to their exact `G` counterparts. Passing to the limit preserves (8.1). Graphs on at most four vertices were already covered for **all** increasing events by the earlier weighted theorem. `QED`

This is a genuine source-faithful weighted theorem, but it is a restricted event class. It does **not** prove Conjecture 4.10 and does not move the source-wide supremum metric.

## 9. Exact finite certificate

The finite core was checked only after the polynomial route produced something worth certifying.

Script:  
`proofnet24/NM13-02/artifacts/2026-09-18/p0037_k5_two_witness_amgm_exact.cpp`  
creation commit: `a95971c95967524224543ae55084dc8ac647e485`  
read-back blob: `0eb88b99981cdccd5317b4d5863933df25552cd7`

Archived output:  
`proofnet24/NM13-02/artifacts/2026-09-18/p0037_k5_two_witness_amgm_exact.out`  
creation commit: `0e8911d98ab06c9eec745e043b58e7be25fa2619`  
read-back blob: `7c706ab3ac54aa71d89d920a71b7c568ba409503`

The checker uses integer counting only. It verifies:

- 125 spanning trees of K5;
- 3425 product/multiplicity cells;
- 45 two-edge witnesses and 1035 one-or-two-witness events;
- 19 `S5` event orbits;
- 9413 simultaneous ordered event-pair orbits whose exact orbit-size sum is 1,071,225;
- exact disjoint occurrence from disjoint generators;
- 9118 coefficientwise-nonnegative pair orbits;
- 295 pair orbits requiring cancellation;
- minimum coefficient `-2`, 1184 negative-monomial occurrences, and at most 12 negative terms in one orbit;
- for every negative term, positive midpoint partners with `beta+gamma=2m`;
- an exact capacity-feasible simultaneous AM--GM assignment for all 295 nontrivial orbit representatives;
- no negative exponent that can be a uniquely exposed Newton-polytope vertex by the midpoint criterion.

The archived output ends `ALL_EXACT_CHECKS_PASS`. This is a **self-check**, not either required independent audit.

## 10. Frozen metric, mandatory handoff, and what remains

The frozen source-wide quantity does not move:
\[
\boxed{
C_{\mathrm{BK}}^{\mathrm{UST}}:
[1,+\infty]\longrightarrow[1,+\infty].
}
\]

The new theorem enlarges the certified weighted K5 region but gives no nontrivial global upper bound on the supremum over **all** finite connected weighted graphs and **all** increasing events. Replacing the metric by the number of K5 event families certified would violate the no-metric-switch rule.

This is therefore the **sixth consecutive unchanged P0037 invocation**, with one stuck recovery used. Under the owner's CLOSABLE policy, NM13-02 now **hands P0037 off and rotates**. The shared canonical claim file is deliberately not edited because workers may not edit shared roots. Its stale owner line must not be interpreted as permission for NM13-02 to perform a seventh P0037 run; P26/the authorized shared-state maintainer should reconcile the handoff.

### Preserved mathematical handoff

The strongest useful state for a future fresh-route reassignment is:

1. weighted BK is proved for every connected simple graph with at most four vertices, for arbitrary increasing events;
2. fixed/adaptively nonoverlapping witness subclasses have separate witness-congestion bounds;
3. the natural constant-weight ordered-pair `(intersection,union)` fibre proof is impossible even on uniform K5: an explicit 12-state fibre has `4>2` while the same global principal-edge inequality is equality;
4. for weighted K5, every pair of increasing events generated by at most two two-edge witnesses satisfies BK, by the exact cross-fibre AM--GM capacity theorem above;
5. the first untested extension of this exact scheme is to **three or more** minimal two-edge witnesses per event, or to mixed witness sizes. A future worker should test whether the midpoint/capacity property persists or fails there. A failure of the midpoint property at an exposed negative exponent would give a concrete weight-scaling counterexample route; persistence may point toward a general coefficient-flow proof.

NM13-02's successor state after this report is **ADMISSION_PENDING** for a different eligible residue-1 CLOSABLE source. Screening for that successor is intentionally not mixed into this final P0037 research invocation. P0037 counters and its frozen metric do not transfer to the successor.

No P26 or NM13-03 audit is claimed. No paper folder is created because the source itself remains open and this is only a restricted theorem.

## 11. Model / scheduler interface status

The scheduler interface exposed to this run still has **no model selector and no reasoning selector**. Its writable controls concern the task prompt/title, schedule or relative timing, timing mode, and enabled state. Thus `GPT-6 / maximum` remains a request in prompt text only; it is not a binding runtime setting. This report therefore states the actually exposed model family, GPT-5.6 Sol, and marks reasoning effort `UNVERIFIED` rather than claiming GPT-6 maximum.

Making the requested setting enforceable would require an authorized product/workspace/API/admin surface exposing persistent model-family and reasoning-effort fields together with authenticated per-run attestation.

The historical P26 `"You cannot modify this task"` response remains an authorization-context boundary. Current repository policy records a later P26 update succeeding from another authorized context, so the legitimate workaround is the owning/authorized task/account/workspace surface or platform/admin support. It is **not** task duplication, access-control bypass, or a repository-only workaround. No support escalation is claimed here.

## 12. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-02
  category: CLOSABLE_OUTSIDE
  source_id: P0037
  claim_path: operations/claims/P0037.md
  source_locator: "Lyons-Peres, Probability on Trees and Networks, Conjecture 4.10"
  canonical_dedup_key: weighted_ust_bk_increasing_disjoint_occurrence
  dedup_sha256: 2f4d891dcaf823ddebc131c162b048b50e7bd61ec43b964f0a10458334c2f041
  shard_mod_13: 1
  source_status: OPEN_BOUNDED_SEARCH
  track_status: PARTIAL_HANDOFF_REQUIRED
  metric_name: C_BK^UST
  metric_before: "[1,+infinity]"
  metric_after: "[1,+infinity]"
  mathematical_movement: false
  substantive_progress: weighted_K5_BK_for_events_each_generated_by_at_most_two_two_edge_witnesses
  methods_actual: [5, 17, 29]
  method_outcomes:
    5: "one-edge weight parameter gives a quadratic derivative test but cannot isolate bad multiplicity fibres; escalated to full exponent geometry"
    17: "Rayleigh/SOS-style complementary-monomial search found exact simultaneous AM-GM capacity certificates for all nontrivial K5 event-pair orbits in the stated class"
    29: "every negative exponent is a midpoint of positive exponents, so no negative monomial is a uniquely exposed tropical vertex; capacity assignment upgrades this to positivity on the full positive orthant"
  restricted_theorem: NM13-02-P0037-K5-2X2W-06
  exact_certificate:
    script: proofnet24/NM13-02/artifacts/2026-09-18/p0037_k5_two_witness_amgm_exact.cpp
    script_commit: a95971c95967524224543ae55084dc8ac647e485
    script_blob: 0eb88b99981cdccd5317b4d5863933df25552cd7
    output: proofnet24/NM13-02/artifacts/2026-09-18/p0037_k5_two_witness_amgm_exact.out
    output_commit: 0e8911d98ab06c9eec745e043b58e7be25fa2619
    output_blob: 7c706ab3ac54aa71d89d920a71b7c568ba409503
    terminal: ALL_EXACT_CHECKS_PASS
  finite_counts:
    spanning_trees: 125
    events: 1035
    event_orbits: 19
    ordered_event_pairs: 1071225
    ordered_pair_orbits: 9413
    coefficientwise_nonnegative_orbits: 9118
    amgm_capacity_orbits: 295
    minimum_coefficient: -2
  unchanged_runs_since_metric_movement: 6
  stuck_recoveries_used: 1
  rotation:
    required: true
    p0037_continue_on_nm13_02: false
    successor_state: ADMISSION_PENDING
    shared_claim_reconciliation: P26_OR_AUTHORIZED_SHARED_STATE_MAINTAINER
  handoff_next_mathematical_target: "three-or-more two-edge minimal witnesses or mixed witness sizes on weighted K5; test exposed-negative Newton cells versus global AM-GM flow"
  audits:
    P26: NOT_REQUESTED_NOT_PASSED
    NM13-03: NOT_REQUESTED_NOT_PASSED
  shared_root_edits: NONE
  peer_edits: NONE
  scheduler_edits: NONE
```

No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, peer edit, shared-root edit, or additional schedule creation/modification was performed.

**End of complete run report.**
