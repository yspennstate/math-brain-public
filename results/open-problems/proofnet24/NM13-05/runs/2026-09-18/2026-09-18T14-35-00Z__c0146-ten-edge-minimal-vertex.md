Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `m_cert = 9 -> 9`; secondary source-relevant sharpness moved from UNMEASURED to `7` vertices among 10-edge simple counterexamples. Section-B methods actually tried: #15 BREAK THE SYMMETRY ON PURPOSE, #26 HUNT THE SPORADIC CASE, #4 PROVE SOMETHING WEAKER, COMPLETELY. Source status: REFUTED; fleet closure still pending P26 + NM13-06.**

# NM13-05 / C0146 — exact 10-edge low-vertex theorem and sharp vertex order within the minimum-edge obstruction

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-05/`  
Category: **CLOSABLE OUTSIDE**  
Canonical source / claim: **C0146**, `operations/claims/C0146.md`  
Canonical dedup key: `fk_q_less_than_1_monotone_coupling`  
SHA-256: `dd817e3ec8169668456ed767e35982573675498dec1367239155a22daa3f4ec6`  
Selection residue: `4 mod 13`  
Frozen metric: `m_cert`  
Metric before / after: **9 -> 9**  
Secondary quantity (not a replacement metric): minimum vertex count among **10-edge** finite simple counterexamples, **UNMEASURED -> 7**  
Unchanged-run counter: **2 -> 3**  
Stuck recoveries: **0 -> 0**  
Required eventual auditors: **P26 and NM13-06; neither is presumed to pass**

## 1. Runtime and control-plane disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, a guaranteed hour-long execution, or a support escalation.

The exposed task-control surface still offers task title/prompt, schedule or relative-start fields, timing mode, enabled state and task identity, but **no bindable model-family selector and no bindable reasoning-effort selector**. Therefore `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model/effort controls plus authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` result remains an authorization-context boundary; repository continuity records a later successful P26 update from another authorized context. The lawful workaround is the owning/otherwise-authorized context or authorized platform/admin support for the same task, never duplication or access-control bypass. No schedule was modified here.

## 2. Authoritative continuity and ownership

This is **not a new admission**. C0146 remains the exclusive lawful NM13-05 target, so I did not reopen QUEUE selection or create another claim.

Before new mathematics I reread or exact-target-recovered the required current state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/C0146.md`;
- the C0146 intake identity and historical attempt `C0146-A001`;
- newest own report `proofnet24/NM13-05/runs/2026-09-18/2026-09-18T13-36-00Z__c0146-algebraic-edge-threshold.md`;
- newest neighboring NM13-04 report `proofnet24/NM13-04/runs/2026-09-18/2026-09-18T14-28-30Z__successor-admission-screen-f0001-f0140.md`;
- newest neighboring/designated-auditor NM13-06 report `proofnet24/NM13-06/runs/2026-09-18/2026-09-18T13-32-30Z__post-p0195-admission-delta-screen-4.md`;
- current exact-ID/canonical-key/audit searches for C0146;
- the exact Git comparison from the preceding own report creation commit.

Immediately before report writing I captured master head `97c2dc9cbd7edfb834f8e9876ec1f7790b8d236e`. Relative to the preceding NM13-05 report creation commit `4d113ae1bdf6dee87e21ce2a9f34f0046b259629`, that head was **69 commits ahead and 0 behind**. Current exact searches recover no competing C0146 owner, no owner-authorized release/retirement, no POSTED/campaign settlement, and no C0146 source-level PASS from either P26 or NM13-06. The newest NM13-06 report is an admission-delta screen for its own successor and contains no C0146 audit.

Large append-only JSONL/root surfaces can be connector-truncated when rendered wholesale. I therefore do not claim a byte-for-byte visual rendering of every source row. Exact canonical files, current root reads, targeted source/attempt searches, path-scoped histories and the exact predecessor-to-head comparison are the continuity basis; missing/truncated history is never treated as permission.

## 3. Exact source and current literature check — 2026-09-18

The current primary source remains Gábor Pete, *Probability and Geometry on Groups*, current PDF dated April 3, 2024. The source still prints:

> Question 13.2. Is there a monotone coupling `(omega_p)_{p in [0,1]}` of the `FK(p,q)` measures for any `q in [0,1)`?

Fresh dated searches included the exact source wording/title, `random-cluster q<1 monotone coupling stochastic monotonicity finite graph`, `arboreal gas not stochastically monotone`, `Rémy Poudevigne arboreal gas`, and current 2026 q<1 negative-dependence work.

The nearest recovered current literature remains consistent with the conservative status used in the previous reports:

- Tang–Zhang, arXiv:2609.11578, submitted 2026-09-10, proves strict pairwise negative correlation on broad high-degree regular classes and explicitly says even pairwise negative correlation is open on general finite graphs. This is related dependence structure, not a source-matching monotone-in-`p` theorem.
- Halberstam's 2023 Cambridge thesis explicitly records that the finite-graph arboreal gas is **not** stochastically monotone in its fugacity, citing Rémy Poudevigne by private correspondence.
- Halberstam–Hutchcroft (Probability and Mathematical Physics 5 (2024)) identifies arboreal gas as the `q -> 0`, `p = beta q` random-cluster limit.

Thus the qualitative forest-boundary mechanism is not claimed as novel. The bounded search did not surface this report's exact 10-edge/low-vertex classification or the previously certified explicit 10-edge positive-`q` witness, but that is **negative evidence only**. Worldwide prior art and publication novelty remain **UNVERIFIED**, particularly because the antecedent forest counterexample is private-correspondence prior art.

## 4. Frozen metric and the exact target of this run

The frozen quantity remains

`m_cert = max m such that every finite simple graph with at most m edges admits a monotone grand FK(p,q) coupling in p for every q in (0,1)`.

It is already exactly pinned at `9`: the preceding finite theorem certifies every graph with at most nine edges, while the existing seven-vertex ten-edge graph

`E = {01,02,03,04,05,12,13,14,16,56}`

has an exactly verified increasing one-edge event whose probability decreases with `p` for a nonempty positive-`q` interval. Therefore this run cannot honestly move `m_cert` upward.

The new question is source-relevant structural sharpness **inside the first failing edge count**:

> Can a finite simple 10-edge counterexample already occur on at most six vertices, or is the known seven-vertex witness vertex-minimal among all 10-edge counterexamples?

This does not replace the frozen metric. It is a secondary finite classification designed to understand the exact obstruction rather than manufacture another certificate for an unchanged number.

## 5. Method #15 — BREAK THE SYMMETRY ON PURPOSE

The highly symmetric 5-vertex candidate is just `K5`, and checking only `K5` would be nearly content-free. I therefore deliberately broke that symmetry by exhaustively including **every asymmetric six-vertex 2-connected simple graph with ten edges**, quotienting only by exact graph isomorphism.

The canonicalization is exact. Graph isomorphisms preserve vertex degrees, so it suffices to search all permutations within equal-degree classes after ordering the degree classes. Exhaustive enumeration gives:

- on 5 vertices: `1` labeled and `1` unlabeled 2-connected ten-edge graph (`K5`);
- on 6 vertices: `2697` labeled and exactly **12** unlabeled 2-connected ten-edge graphs.

Thus the search space consists of exactly **13** 2-connected isomorphism types. This avoids the common failure mode in which only the obvious symmetric dense graph is tested and a sporadic asymmetric obstruction is missed.

Outcome of #15: **the low-order search is symmetry-complete rather than symmetry-biased: 13 exact block types, including all 12 asymmetric/symmetric six-vertex possibilities.**

## 6. Method #26 — HUNT THE SPORADIC CASE

I next treated those 13 types as a direct hunt for a sporadic ten-edge obstruction.

For a 2-connected graph `H=(V,E)` with `|E|=10`, condition the FK measure on `|A|=r` and write

`c(A) = |A| - |V| + k(A)`,

`nu_r(A) = q^{c(A)} / W_r(q)`,

`W_r(q) = sum_{|C|=r} q^{c(C)}`.

For every adjacent layer `r -> r+1`, use the unnormalized inclusion-transport margins

`row_A(q) = q^{c(A)} W_{r+1}(q)`,

`col_B(q) = q^{c(B)} W_r(q)`.

For any degree `N` at least the polynomial degrees, expand each margin in the Bernstein basis

`B_{j,N}(q) = binom(N,j) q^j (1-q)^{N-j}`,

using the exact identity

`q^k = sum_{j=k}^N [binom(j,k)/binom(N,k)] B_{j,N}(q)`.

Every Bernstein coefficient is a nonnegative rational number. For each coefficient index `j`, existence of an inclusion transport is therefore a finite bipartite max-flow question with exact rational row and column masses. A feasible flow for every `j` yields, by the Bernstein-weighted sum of those flows, an inclusion coupling for every `q in [0,1]` simultaneously.

The exact calculation finds:

- the 12 six-vertex types require Bernstein degree `N=9`;
- `K5` requires `N=11`;
- adjacent fixed-size layer pairs checked: **130**;
- exact Bernstein coefficient-flow instances checked: **1320**;
- every one of the 1320 exact rational inclusion-flow instances is feasible.

The checker reconstructs each realized flow and independently re-sums every row and column margin after max-flow, so feasibility is not inferred from a floating-point optimizer or a sampled `q` grid.

Outcome of #26: **no sporadic 10-edge obstruction exists on five or six vertices. The known obstruction first appears at seven vertices within the minimum-edge class.**

## 7. Method #4 — PROVE SOMETHING WEAKER, COMPLETELY

The obstruction search above gives a clean restricted theorem rather than another heuristic.

**Theorem.** Let `G` be a finite simple graph with exactly ten edges and at most six non-isolated vertices (equivalently, after deleting isolated vertices, at most six vertices). For every `q in (0,1)`, the family `{FK_G(p,q): 0<=p<=1}` admits a monotone grand coupling in `p`.

**Proof.** Decompose `G` into graph blocks. Random-cluster weights factor over one-vertex sums, and a one-edge bridge block has an open probability increasing in `p`. Hence it suffices to couple every nontrivial 2-connected block independently and take the product of the block couplings.

If a nontrivial block has at most nine edges, the already certified C0146 nine-edge theorem supplies its monotone grand coupling for every `q in (0,1)`. The only new case is therefore a 2-connected block containing all ten edges of `G`. Such a block has at most six vertices and is one of the 13 isomorphism types classified exactly in Section 5.

Fix one of those 13 blocks. For every `r=0,...,9`, Section 6's 1320 exact coefficient-flow checks give an inclusion coupling `nu_r <=_st nu_{r+1}` for every `q in (0,1)`. Compose these adjacent kernels to obtain a nested random chain

`A_0 subset A_1 subset ... subset A_10`

with `A_r ~ nu_r`.

For fixed `q`, the FK law conditioned on `|A|=r` is exactly `nu_r`; all dependence on `p` outside the conditional law is through the scalar factor `[p/(1-p)]^r`. Therefore the FK size distributions have monotone likelihood ratio in `r` as `p` increases. Couple those sizes monotonically by one common quantile and evaluate the nested chain at the coupled size. The resulting process is increasing in `p` and has the exact `FK_G(p,q)` marginal for every `p`. This proves the theorem. `□`

The existing seven-vertex, ten-edge positive-`q` counterexample supplies the matching upper witness. Therefore:

**Corollary (sharp within the minimum-edge class).** Among finite simple **10-edge** counterexamples to Pete Question 13.2, the minimum possible number of non-isolated vertices is exactly

`7`.

I do **not** claim that seven is the minimum vertex count among counterexamples with arbitrary edge count: a denser graph on at most six vertices would require a separate theorem. I also do not replace `m_cert` with this secondary quantity.

Outcome of #4: **complete restricted theorem plus an exact sharp structural parameter inside the already-minimal 10-edge obstruction class.**

## 8. Exact finite certificate

New deterministic exact checker:

`proofnet24/NM13-05/artifacts/2026-09-18/c0146_m10_n6_bernstein_checker.py`

creation commit:

`b133845787f6fe81821016d97ac84703050dc94b`

Archived executed output:

`proofnet24/NM13-05/artifacts/2026-09-18/c0146_m10_n6_bernstein_checker.out`

creation commit:

`0c35fa6032fb8364aabde798becb04d0cd5c9819`

The checker uses only Python's standard library, integers and `fractions.Fraction`; no floating point, random search, external graph library, solver package or downloaded script enters the finite claim. Its terminal output is:

```text
labeled_biconnected_n5_n6 [1, 2697]
unlabeled_biconnected_n5_n6 {5: 1, 6: 12}
representatives_total 13
bernstein_degree_counts {9: 12, 11: 1}
adjacent_layer_transport_pairs 130
coefficient_flow_instances 1320
theorem every finite simple graph with exactly 10 edges and at most 6 vertices is FK-monotone in p for q in (0,1)
existing_10_edge_counterexample_vertices 7
minimum_vertices_among_10_edge_simple_counterexamples 7
ALL_EXACT_CHECKS_PASS
```

This certificate is a self-check of the finite core. It is not an external audit.

## 9. Status, audit gate, and mandatory next run

The source remains mathematically **REFUTED** by the already exact positive-`q` witness. The frozen metric nevertheless remains `m_cert = 9`, so this is the **third consecutive frozen-metric unchanged run** under the current counter history: `unchanged_runs 2 -> 3`.

Current independent-audit state recovered this invocation:

- **P26: NOT PASSED / no C0146 source-level PASS recovered**;
- **NM13-06: NOT PASSED / no C0146 source-level PASS recovered**.

Therefore C0146 is not fleet-CLOSED and no paper folder is created yet.

Because the frozen metric has now been unchanged for three consecutive runs, **the next NM13-05 invocation is mandatory Section-I stuck recovery / thinking-only**. It must not add another ordinary lemma or another census. It must write the required stuck report with the exact blocking closure obligation, every route tried and failure mode, the missing ingredient, the simplest unresolved special case, and nearest solved literature, then choose one permitted recovery action. For this already-refuted source, the useful recovery decision should be driven by the actual remaining obligation—independent audit/prior-art reconciliation—rather than by further sharpening `q_*` or extending a finite graph census merely to manufacture activity.

## 10. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-05
  category: CLOSABLE_OUTSIDE
  runtime:
    model: GPT-5.6_Sol
    reasoning: UNVERIFIED
    requested_model: GPT-6
    requested_reasoning: maximum
  source:
    problem_id: C0146
    claim_path: operations/claims/C0146.md
    dedup_key: fk_q_less_than_1_monotone_coupling
    shard_residue: 4
    source_status: REFUTED
    ownership: EXCLUSIVE_NM13_05
  metric:
    name: m_cert
    before: 9
    after: 9
    movement: NONE
  secondary_result:
    quantity: minimum_vertices_among_10_edge_simple_counterexamples
    before: UNMEASURED
    after: 7
    frozen_metric_replaced: false
  theorem:
    statement: "Every finite simple 10-edge graph with at most six non-isolated vertices admits a monotone grand FK(p,q) coupling for every q in (0,1)."
    exact_2connected_types: 13
    exact_labeled_counts_n5_n6: [1, 2697]
    exact_unlabeled_counts_n5_n6: [1, 12]
    adjacent_layer_pairs: 130
    exact_coefficient_flow_instances: 1320
    minimum_vertices_in_10_edge_counterexample_class: 7
  methods:
    - 15: "BREAK THE SYMMETRY ON PURPOSE — enumerate all 12 six-vertex asymmetric/symmetric block types, not only K5"
    - 26: "HUNT THE SPORADIC CASE — exact obstruction search finds none on <=6 vertices"
    - 4: "PROVE SOMETHING WEAKER, COMPLETELY — complete 10-edge <=6-vertex theorem"
  artifacts:
    checker: proofnet24/NM13-05/artifacts/2026-09-18/c0146_m10_n6_bernstein_checker.py
    checker_commit: b133845787f6fe81821016d97ac84703050dc94b
    output: proofnet24/NM13-05/artifacts/2026-09-18/c0146_m10_n6_bernstein_checker.out
    output_commit: 0c35fa6032fb8364aabde798becb04d0cd5c9819
    terminal: ALL_EXACT_CHECKS_PASS
  prior_art:
    qualitative_q0_nonmonotonicity: HALBERSTAM_THESIS_CITING_POUDEVIGNE_PRIVATE_CORRESPONDENCE
    exact_10_edge_low_vertex_classification_novelty: UNVERIFIED
    bounded_search_is_not_worldwide_openness_proof: true
  audits:
    P26: NOT_PASSED
    NM13_06: NOT_PASSED
    closure: false
  counters:
    unchanged_runs_before: 2
    unchanged_runs_after: 3
    stuck_recoveries_before: 0
    stuck_recoveries_after: 0
  next_step: "MANDATORY Section-I stuck-recovery thinking-only run; closure/audit and prior-art obligation first, no ordinary census/threshold sharpening"
```

No canonical claim, shared root, peer namespace, permission, workflow, public surface, email/Gmail, Drive resource, paid compute, force-push, or schedule was created or modified. The only new substantive artifacts are the exact checker/output above, warranted by the new finite theorem, plus this single immutable run report.