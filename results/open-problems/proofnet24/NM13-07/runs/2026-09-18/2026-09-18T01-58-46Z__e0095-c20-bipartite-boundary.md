Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `g_16^*` stayed `1 - sqrt(3)/3 -> 1 - sqrt(3)/3`. Section-B methods actually tried: #1, #17, #30.**

# NM13-07 run — E0095 / exact bipartite `C_20` optimum and the Hamiltonian boundary

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-07`  
Category: CLOSABLE OUTSIDE  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Canonical source / claim: `E0095`, `operations/claims/E0095.md`  
Parent source status after this run: **OPEN**  
NM13-07 status after this run: **PARTIAL**  
Unchanged-run count since the frozen metric last moved: **2**  
Stuck-recovery count: **0**  
Designated eventual outside auditors: **P26 and NM13-08; neither is counted as passed**

## 1. Runtime/control disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. The reasoning-effort telemetry exposed to this report is **UNVERIFIED**, so I do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The currently exposed task-control surface offers title/prompt, schedule or relative-start fields, timing mode, and enabled state. It still exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Consequently `GPT-6 / maximum` remains prompt text only. Making that requirement enforceable would require an owner-authorized scheduler/product/workspace/API surface that exposes those fields and provides per-run runtime attestation. The historical P26 `You cannot modify this task` refusal is an authorization/context boundary, not a release of mathematical ownership; the valid workaround is the owning or otherwise authorized account/workspace/product/admin surface, not cloning the task or bypassing access controls. No support escalation is claimed, and no schedule was created or modified in this run.

## 2. Continuity, ownership, and required repository read

This invocation continues the already admitted **E0095 — Diaconis Question 4** assignment. It does not reopen intake, create another claim, change the source clause, or reset the metric.

Before the mathematical attack I reread or targeted-recovered the controlling and continuity surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and targeted current `RESULTS.md` / report-state searches;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- current claim `operations/claims/E0095.md`;
- `probability_1000_intake_E_20260908/problems.jsonl` exact-key recovery and the E0095 prior attempt / campaign memo;
- my newest immutable report `proofnet24/NM13-07/runs/2026-09-18/2026-09-18T00-31-52Z__e0095-c18-pappus-transfer.md`;
- newest visible neighboring NM13 reports from NM13-06 and NM13-08;
- historical E0095 report and artifact searches, including the earlier `n<=14` campaign work, the exact `C_16` report, and the exact `C_18` report.

The canonical identity remains:

- problem ID: `E0095`;
- source: Persi Diaconis, *Some things we've learned (about Markov chain Monte Carlo)*, Bernoulli 19 (2013), Section 5, Question 4;
- canonical dedup key: `diaconis_mcmc::q4`;
- SHA256: `82e47bd0a497f76f9f11eff1c70aa5a13afed8c2f65ad0c9723e03e6c86652a5`;
- residue: `6 mod 13`, matching NM13-07's exclusive shard;
- owner: `proofnet24/NM13-07`.

I recovered no release, handoff, retirement, alternate-ID owner, source-level `POSTED.md` closure, campaign closure, or competing claim. The source remains broader than the finite cycle slices studied here.

Large root files and JSONL inventories can be connector-truncated when rendered wholesale. I used current root views plus exact-ID, exact-dedup-key, claim-path, and report-path searches. I do not treat bounded repository indexing as proof that inaccessible history is empty. No material E0095 continuity item needed below was inaccessible.

## 3. Exact source clause and frozen metric

Diaconis asks, for a connected `d`-regular graph on an even number of vertices, which perfect matching should be added to make the resulting `(d+1)`-regular walk mix fastest. The cycle is an explicit motivating base graph. NM13-07's admitted finite milestone specializes to cycle-plus-perfect-matching graphs without replacing the parent source question.

The frozen metric, fixed at admission and not silently changed, is

`g_16^* = max_M (1 - lambda_2(A(C_16 union M))/3)`,

where `M` ranges over perfect matchings containing no cycle edge. The exact `C_16` run established

`g_16^* = 1 - sqrt(3)/3`.

Before this run:

`g_16^* = 1 - sqrt(3)/3`.

After this run:

`g_16^* = 1 - sqrt(3)/3`.

Therefore the frozen metric has **no movement**. The `C_20` theorem below is substantive source-relevant progress but is not a license to replace the admitted metric.

## 4. New idea before code

The preceding immutable `C_18` report explicitly recorded the next route before any `C_20` checker was built: do **not** enumerate all matchings first; instead transfer published global cubic spectral classifications to the Hamiltonian `C_20 + matching` subclass, and only then build a small checker for constructions worth certifying.

That methods-first route paid off. Two distinct published viewpoints meet exactly at order 20:

1. Koledin--Stanić classify bipartite cubic graphs with small second adjacency eigenvalue, giving a complete `lambda_2 <= 2` boundary.
2. Exoo--Kolokolnikov--Janssen--Salamon tabulate algebraic-connectivity maxima for cubic graphs by order and girth, showing that the **unrestricted** order-20 cubic world already contains nonbipartite graphs with `lambda_2 < 2`.

So the right question is not “can I certify another equality graph?” but:

> What is the exact optimum in the bipartite source subclass, and is the first nonbipartite cubic improvement Hamiltonian (hence actually representable as `C_20 + M`)?

Only after the published classification isolated the six relevant order-20 bipartite types did I use the existing exact checker to verify that each published LCF presentation is genuinely a source-admissible `C_20 +` noncycle perfect matching and has the asserted exact spectrum.

## 5. Method #1 — CHANGE THE CATEGORY: from mixing to algebraic connectivity

For any connected cubic graph `G`,

`L_G = 3 I - A_G`,

so the Laplacian algebraic connectivity satisfies

`AC(G) = 3 - lambda_2(A_G)`.

For the non-lazy simple random walk `P=A_G/3`, the Poincare gap used in the admitted cycle objective is

`gap(G) = 1 - lambda_2(A_G)/3 = AC(G)/3`.

Thus minimizing the second adjacency eigenvalue is exactly the same finite optimization as maximizing algebraic connectivity. This recoding imports a literature that does not present itself as a matching problem.

The immediate `C_20` lesson is important. Exoo--Kolokolnikov--Janssen--Salamon's exhaustive-order table records, among cubic graphs of order 20 and girth 6, a maximum algebraic connectivity approximately

`1.064568`,

corresponding to

`lambda_2 approximately 3 - 1.064568 = 1.935432 < 2`.

Therefore **the bipartite value `lambda_2=2` cannot be promoted to the unrestricted order-20 cubic optimum**. To become a counterexample to the bipartite threshold inside the actual Diaconis cycle slice, however, such a graph must be Hamiltonian. A cubic Hamiltonian graph is automatically `C_20 union M` relative to any chosen Hamilton cycle, because the edges outside the Hamilton cycle form a perfect matching. Hamiltonicity is therefore the precise missing admissibility test.

Outcome of #1: **successful category change**. It produced a complete restricted theorem below and identified the exact source-valid boundary separating that theorem from the full `C_20` objective.

## 6. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: exact bipartite `C_20` optimum

### Theorem (complete bipartite `C_20` source subclass)

Let `M` be a perfect matching of the vertices of `C_20`, with no matching edge equal to a cycle edge, and let

`G_M = C_20 union M`.

Assume `G_M` is bipartite. Then

`lambda_2(A(G_M)) >= 2`.

Equality is attained. More precisely, if `lambda_2(A(G_M)) <= 2`, then `G_M` is isomorphic to one of exactly six Koledin--Stanić order-20 types `J10,...,J15`; all six satisfy `lambda_2=2` and all six admit the required Hamiltonian `C_20 +` noncycle-matching presentation. Consequently

`min_{M: G_M bipartite} lambda_2(A(G_M)) = 2`

and

`max_{M: G_M bipartite} gap(G_M) = 1/3`.

### Proof

A graph `G_M` in this subclass is connected, cubic, bipartite, and has exactly 20 vertices.

Suppose first that `lambda_2(G_M) <= 2`. Koledin--Stanić's Theorem 8 classifies **all bipartite reflexive cubic graphs**, i.e. all bipartite cubic graphs with second adjacency eigenvalue at most 2. Their lower-eigenvalue tables contain no 20-vertex cubic graph: in the range `sqrt(2) < lambda_2 <= sqrt(3)`, the cubic entries have orders 12, 16, and 18, while their Theorem 7 / Table 3 handles `sqrt(3) < lambda_2 <= 2`.

In Table 3 the **only** order-20 graphs are `J10,J11,J12,J13,J14,J15`, and the printed nonnegative spectra give second adjacency eigenvalue exactly 2 for each. Therefore any bipartite 20-vertex cubic graph with `lambda_2<=2` must have `lambda_2=2` and be one of those six isomorphism types. In particular no bipartite source graph can have `lambda_2<2`.

It remains to show that equality occurs inside the source subclass rather than merely in the ambient cubic classification. Koledin--Stanić give LCF presentations for all six order-20 graphs. The exact self-check in this namespace reconstructs each presentation, verifies that the distinguished 20-cycle plus the ten remaining edges is exactly a perfect matching containing no cycle edge, verifies cubicity and bipartiteness, and computes the characteristic polynomial over the integers. Each has exact second eigenvalue 2. Hence all six are source-admissible equality examples.

Finally, for cubic simple random walk,

`gap = 1 - lambda_2/3`,

so the exact optimum in this restricted subclass is `1 - 2/3 = 1/3`. QED.

### What is and is not novel

The global classification is published mathematics, not an NM13-07 discovery. The source-specific theorem is a short transfer/corollary plus an exact verification that all six tabulated LCF graphs genuinely lie in Diaconis's `C_20 + matching` slice. I make **no publication-novelty claim** for that corollary.

Outcome of #17: **complete restricted-class theorem** with a published lower-bound classification and an exact source-admissibility certificate.

## 7. Exact finite self-check already warranted by the theorem

Artifacts:

- `proofnet24/NM13-07/artifacts/2026-09-18/e0095_c20_bipartite_six_exact.py`
- `proofnet24/NM13-07/artifacts/2026-09-18/e0095_c20_bipartite_six_exact.out`

Artifact commits on current `master`:

- checker: `32b354b51be459b2c29b067d90158b850b668c28`;
- archived output: `120fedd2d8a736904245bae977d0d1f3d97256b9`.

The checker uses exact integer/symbolic arithmetic for the proof-critical spectral claims. For the six Koledin--Stanić LCF representatives it verifies:

- a simple 20-cycle plus exactly ten noncycle matching edges;
- degree 3 at every vertex;
- bipartiteness;
- exact characteristic-polynomial factorization;
- exact second adjacency eigenvalue `2`.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

The three exact characteristic-polynomial patterns recovered are:

- `J10,J11`: `(x-3)(x-2)^4(x-1)^5(x+1)^5(x+2)^4(x+3)`;
- `J12,J14`: `x^2(x-3)(x-2)^3(x-1)^3(x+1)^3(x+2)^3(x+3)(x^2-3)^2`;
- `J13,J15`: `(x-3)(x-2)^2(x-1)(x+1)(x+2)^2(x+3)(x^3-3x-1)^2(x^3-3x+1)^2`.

This is a **self-check**, not an independent audit and not a re-proof of Koledin--Stanić's exhaustive classification.

## 8. Method #30 — ONE SCALE / ONE DIRECTION AT A TIME: isolate the nonbipartite Hamiltonian frontier

The published order-20 algebraic-connectivity data now give a much sharper next obligation than brute-force enumeration.

For the bipartite direction, the theorem above is complete: the optimum is `lambda_2=2`.

For the full source slice, the Exoo--Kolokolnikov--Janssen--Salamon table shows that the ambient cubic class contains a girth-6 order-20 graph with `lambda_2 approximately 1.935432`. Thus the only question that matters first is:

`Does an order-20 cubic graph with lambda_2 < 2 in that high-AC stratum have a Hamilton cycle?`

If YES, choose such a Hamilton cycle; the ten leftover edges form a perfect matching, immediately giving a `C_20 + M` source witness strictly beating every bipartite matching.

If NO for all cubic graphs with `lambda_2<2`, then the bipartite value `2` may still be the exact source optimum even though it is not the ambient cubic optimum.

This is a clean gluing failure: the spectral optimum is known in a larger category, but the source asks for the Hamiltonian subcategory.

A particularly relevant public census is the Flinders Hamiltonian Cycle Project's cubic-graph property database. Its documentation says the census covers **all cubic graphs through 20 vertices** and records, on the same row, Hamiltonicity, the number of Hamilton cycles, girth, bipartiteness, second-largest eigenvalue, and diameter. That is exactly the join needed here. In this run the web surface exposed the database documentation and a ZIP download endpoint, but the available browser could not inspect the binary census payload. I therefore did **not** infer Hamiltonicity from the spectral table or manufacture an ID. This is an access limitation, not evidence one way or the other.

Outcome of #30: **the full `C_20` problem is reduced to an exact census join / finite witness extraction**, with the bipartite half completely settled.

## 9. Fresh bounded literature/status check — 2026-09-18

I checked the original Diaconis source and bounded current searches for the exact matching question, cycle-plus-perfect-matching spectral optimization, cubic Hamiltonian graphs with small second eigenvalue, and later algebraic-connectivity maximization work. The specific sources used in the mathematical route were:

1. Persi Diaconis, *Some things we've learned (about Markov chain Monte Carlo)*, Bernoulli 19 (2013), arXiv:1309.7754 — original Question 4 source.
2. Tamara Koledin and Zoran Stanić, *Regular graphs with small second largest eigenvalue*, Applicable Analysis and Discrete Mathematics 7 (2013), 235--249 — exact classification of bipartite cubic graphs with `lambda_2<=2`; Table 3 contains `J10--J15` at order 20.
3. Sebastian Cioabă, Jack Koolen, Hiroshi Nozaki, Jason Vermette, *Maximizing the Order of a Regular Graph of Given Valency and Second Eigenvalue*, SIAM J. Discrete Math. 30 (2016) — the global small-second-eigenvalue route already used in the preceding `C_18` run.
4. Geoffrey Exoo, Theodore Kolokolnikov, Jeanette Janssen, Timothy Salamon, *Attainable bounds for algebraic connectivity and maximally-connected regular graphs*, J. Graph Theory 107 (2024), arXiv:2307.07308 — exhaustive small-order / girth data, including order 20, girth 6, maximum AC approximately `1.064568`.
5. Masashi Kurahashi, Najd Salaani, Tsuyoshi Migita, Norikazu Takahashi, *Algebraic Connectivity Maximizing Regular Graphs: Special Case Analysis and Depth-First Search*, Concurrency and Computation: Practice and Experience 37 (2025), e70357 — later exact-search framework, but its reported exhaustive execution is only through order 12, so it does not settle the order-20 Hamiltonian join.
6. Flinders Hamiltonian Cycle Project, *Properties for Cubic Graphs* — public census documentation stating all cubic graphs up to 20 vertices are covered and that Hamiltonicity and second-largest eigenvalue are both recorded.

I did **not** recover a later paper explicitly resolving Diaconis Question 4 in general or the exact unrestricted `C_20 + matching` optimum. That statement is **bounded negative evidence only**, not proof of worldwide openness and not a novelty certificate. Publication novelty of the source-specific bipartite corollary remains **UNVERIFIED** and should be presumed low-risk only as a useful internal reduction, not advertised as new mathematics.

## 10. Honest status and remaining obligation

Parent source `E0095`: **OPEN**.

NM13-07 contribution after this run: **PARTIAL**.

What is now complete:

- exact `C_16` optimum: `lambda_2=sqrt(3)`, frozen metric `g_16^*=1-sqrt(3)/3`;
- exact `C_18` optimum: `lambda_2=sqrt(3)`, Pappus equality orbit;
- exact **bipartite** `C_20` optimum: `lambda_2=2`, gap `1/3`, exactly six ambient isomorphism types `J10--J15`, each certified source-admissible.

What is not complete:

- the unrestricted `C_20` cycle matching optimum;
- the general Diaconis matching question;
- novelty review beyond the bounded searches above;
- either required independent audit.

Frozen metric movement this run: **none**.

`unchanged_runs_since_metric_movement = 2`.

`stuck_recoveries_used = 0`.

The task is not yet at the three-run stuck trigger.

## 11. Next attack

Do **not** repeat #1/#17/#30 next run. Proposed next methods:

- **#2 ATTACK THE NEGATION FIRST:** search specifically for a Hamiltonian order-20 cubic graph with `lambda_2<2`; one exact witness would immediately show the bipartite value is not the full `C_20` optimum.
- **#19 MAKE IT AN ALGORITHM:** join the exhaustive cubic spectral census to Hamiltonicity (or reconstruct one candidate graph and an explicit Hamilton cycle) and output a source-normalized matching witness.
- **#26 HUNT THE SPORADIC CASE:** isolate the order-20 high-AC girth-6 extremizers and determine which, if any, are Hamiltonian; if none are, descend to the next spectral stratum rather than enumerate all `20`-vertex matchings indiscriminately.

If that run leaves the frozen metric unchanged, it will be the third consecutive unchanged run and the following invocation must obey the Section-I stuck protocol.

## 12. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-07
  category: CLOSABLE_OUTSIDE
  source_id: E0095
  claim_id: E0095
  canonical_dedup_key: diaconis_mcmc::q4
  parent_source_status: OPEN
  worker_status: PARTIAL
  frozen_metric:
    name: g_16^*
    normalization: "max over noncycle perfect matchings M of C16 of 1-lambda_2(A(C16 union M))/3"
    before: "1 - sqrt(3)/3"
    after: "1 - sqrt(3)/3"
    movement: false
  substantive_progress:
    - "Exact restricted theorem: among bipartite C20+matching source graphs, min adjacency lambda_2 = 2 and max Poincare gap = 1/3."
    - "Published classification plus exact LCF check isolates six equality isomorphism types J10--J15 and verifies all six are source-admissible."
    - "Ambient cubic order-20 data contain lambda_2 about 1.935432, reducing the unrestricted C20 question to Hamiltonicity of the high-AC stratum."
  methods_tried:
    - 1
    - 17
    - 30
  method_outcomes:
    1: "Recast cubic mixing gap as algebraic connectivity AC=3-lambda_2; exposed nonbipartite ambient improvement below 2."
    17: "Transferred Koledin--Stanic classification to prove the exact bipartite C20 source-subclass optimum."
    30: "Localized the unresolved problem to the Hamiltonicity join for order-20 cubic graphs with lambda_2<2."
  exact_artifacts:
    checker: proofnet24/NM13-07/artifacts/2026-09-18/e0095_c20_bipartite_six_exact.py
    checker_commit: 32b354b51be459b2c29b067d90158b850b668c28
    output: proofnet24/NM13-07/artifacts/2026-09-18/e0095_c20_bipartite_six_exact.out
    output_commit: 120fedd2d8a736904245bae977d0d1f3d97256b9
    output_terminal: ALL_EXACT_CHECKS_PASS
  audits:
    P26: NOT_REQUESTED_NOT_PASSED
    NM13-08: NOT_REQUESTED_NOT_PASSED
  literature_check_date: 2026-09-18
  literature_scope: "Original Diaconis source; exact matching/cycle queries; Koledin--Stanic cubic-reflexive classification; Cioaba--Koolen--Nozaki--Vermette; Exoo--Kolokolnikov--Janssen--Salamon; Kurahashi et al.; Flinders cubic Hamiltonicity/spectrum census documentation."
  literature_access_limits: "Bounded web search is not a worldwide-openness or novelty proof. Flinders documentation was readable but the binary census download was not inspectable in this run's browser surface."
  unchanged_runs_since_metric_movement: 2
  stuck_recoveries_used: 0
  next_methods:
    - 2
    - 19
    - 26
  next_step: "Extract or reconstruct an order-20 cubic lambda_2<2 candidate and decide Hamiltonicity exactly; if Hamiltonian, produce its Hamilton cycle, complementary matching, exact characteristic polynomial, and source-normalized gap."
```

No root/shared ledger, peer file, audit request, email, Drive object, public post, permission, workflow, or additional schedule was modified by this report.
