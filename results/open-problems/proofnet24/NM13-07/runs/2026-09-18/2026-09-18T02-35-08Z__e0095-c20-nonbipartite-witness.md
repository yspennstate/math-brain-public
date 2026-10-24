Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `g_16^*` stayed `1 - sqrt(3)/3 -> 1 - sqrt(3)/3`. Section-B methods actually tried: #2, #19, #26.**

# NM13-07 run — E0095 / exact nonbipartite `C_20` witness beyond the bipartite boundary

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-07`  
Category: CLOSABLE OUTSIDE  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Canonical source / claim: `E0095`, `operations/claims/E0095.md`  
Parent source status after this run: **OPEN**  
NM13-07 status after this run: **PARTIAL**  
Unchanged-run count since the frozen metric last moved: **3**  
Stuck-recovery count: **0**  
Designated eventual outside auditors: **P26 and NM13-08; neither is counted as passed**

## 1. Runtime/control disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I therefore do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The exposed task-control surface still offers prompt/title, schedule or relative-start fields, timing mode, and enabled state. It exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only in this interface. Making the requirement binding would require an owner-authorized product/workspace/API/admin surface that exposes those controls and per-run runtime attestation. The historical P26 `You cannot modify this task` refusal is an authorization/context boundary, not a release of mathematical ownership; the lawful workaround is the owning or otherwise authorized surface (or platform support), not duplicating the task or bypassing access controls. No schedule was created, modified, or disabled in this run.

## 2. Continuity, ownership, and required repository read

This invocation continues the already admitted **E0095 — Diaconis Question 4** assignment. It does **not** reopen intake, create another claim, alter the source clause, or reset the frozen metric.

Before the mathematical attack I reread or targeted-recovered the current controlling and continuity surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/E0095.md`;
- exact-key intake recovery for `diaconis_mcmc::q4` in `probability_1000_intake_E_20260908/problems.jsonl` and its mirrored archive;
- attempt `E0095-A001`, the 2026-09-09 E0095 campaign memo, and historical E0095 artifacts;
- newest own report `proofnet24/NM13-07/runs/2026-09-18/2026-09-18T01-58-46Z__e0095-c20-bipartite-boundary.md`;
- newest visible neighboring NM13-06 and NM13-08 reports.

Exclusive ownership remains unchanged:

- problem ID: `E0095`;
- source: Persi Diaconis, *Some things we've learned (about Markov chain Monte Carlo)*, Bernoulli 19 (2013), Section 5, Question 4;
- canonical dedup key: `diaconis_mcmc::q4`;
- SHA256: `82e47bd0a497f76f9f11eff1c70aa5a13afed8c2f65ad0c9723e03e6c86652a5`;
- residue: `6 mod 13`, matching NM13-07's exclusive shard;
- owner: `proofnet24/NM13-07`.

I recovered no release, handoff, competing owner, retirement, `POSTED.md` source-level closure, campaign closure, or audit completion for E0095. The source remains broader than the finite cycle slices studied here. Repository-wide code search and large JSONL/root-file rendering are indexed/bounded and may truncate; I used exact IDs, canonical keys, claim paths, report paths, and current root views and do not represent that as a byte-for-byte scan of every historical commit. No material continuity item needed below was inaccessible.

## 3. Exact source and frozen metric

Diaconis Question 4 asks: start from a connected `d`-regular graph on an even number of vertices, add `n/2` edges forming a perfect matching, and ask which choice of edges gives fastest mixing. The source specifically uses the cycle as the motivating `d=2` example and asks for accurate rates of convergence rather than only diameter translations.

The admitted frozen metric remains

`g_16^* = max_M (1 - lambda_2(A(C_16 union M))/3)`,

where `M` is a perfect matching containing no cycle edge. The exact `C_16` run already proved

`g_16^* = 1 - sqrt(3)/3`.

Before this run:

`g_16^* = 1 - sqrt(3)/3`.

After this run:

`g_16^* = 1 - sqrt(3)/3`.

Therefore the frozen metric has **no movement**. The `C_20` witness below is substantive source-relevant progress but is not used to rename or replace the admitted metric.

## 4. New idea before code

The preceding immutable report proved that every **bipartite** source-admissible `C_20 + matching` graph has `lambda_2 >= 2`, with equality, and identified one precise frontier: published ambient cubic data contain an order-20 girth-6 graph with `lambda_2 approximately 1.935432 < 2`, but source relevance required a Hamiltonian presentation.

So this run did not begin by manufacturing another equality certificate. It attacked the missing implication directly:

> Find a genuine perfect matching `M` on the fixed labelled cycle `C_20` such that `C_20 union M` is nonbipartite and has `lambda_2 < 2`.

A source-admissible witness would automatically resolve the Hamiltonicity boundary constructively because the fixed `C_20` itself is already the Hamilton cycle.

## 5. Method #2 — ATTACK THE NEGATION FIRST: beat every bipartite `C_20` construction

A source-valid counterexample to the hypothesis “the bipartite `C_20` optimum might also be the full `C_20` optimum” was found:

`M = {(0,6),(1,15),(2,9),(3,18),(4,13),(5,10),(7,14),(8,17),(11,16),(12,19)}`.

Every vertex occurs exactly once and no matching edge is a cycle edge. Hence

`G = C_20 union M`

is a connected cubic Hamiltonian graph in the exact Diaconis cycle-plus-matching subclass. It is nonbipartite and has girth 6.

The exact characteristic polynomial factors as

`chi_G(x) = (x-3)(x^2-x-1)^2(x^3-4x+1)(x^4-5x^2+5)`

`            *(x^3+2x^2-4x-7)(x^5+3x^4-3x^3-11x^2-3x+1)`.

Let `alpha` be the real root of

`p(x)=x^3+2x^2-4x-7`

in the exact rational interval

`19354/10000 < alpha < 19355/10000`.

Exact Sturm counts certify that every other non-Perron factor has no real root in `[1.93,3)`, while `p` has exactly one root in `(1.93,2)` and no root in `[2,3)`. Since `G` is connected and cubic, the Perron eigenvalue is 3. Therefore

`lambda_2(A_G) = alpha < 2`.

Consequently

`gap(G) = 1 - alpha/3 > 1/3`.

Numerically, only for readability,

`alpha = 1.935432331970030...`

and

`gap(G) = 0.354855889343323...`.

The preceding run's exact theorem established that **every bipartite** source-admissible `C_20 + matching` graph has gap at most `1/3`. Hence this witness proves a new exact source-relevant conclusion:

> **No bipartite matching is optimal for the full `C_20` cycle-plus-perfect-matching spectral-gap problem.**

Equivalently, if

`g_20^* = max_M (1 - lambda_2(A(C_20 union M))/3)`,

then

`g_20^* >= 1-alpha/3 > 1/3`,

so every maximizer must lie outside the bipartite subclass.

This is a restricted finite theorem inside the broader Diaconis source, not a solution of Question 4 and not a proof that this witness is the exact global `C_20` optimizer.

Outcome of #2: **success**. The precise negation target survived exact certification and crosses the previous bipartite boundary.

## 6. Method #19 — MAKE IT AN ALGORITHM: search the Hamiltonian subclass itself

Instead of searching arbitrary cubic graphs and then asking whether they happen to be Hamiltonian, I searched directly in source coordinates: perfect matchings on the fixed labelled `C_20`. The local move was a matching two-switch: choose two matching edges and reconnect their four endpoints in one of the other perfect-matching pairings, rejecting cycle edges or repeated edges, and score the resulting cubic graph by its second adjacency eigenvalue.

That algorithmic formulation forces every candidate to retain the source's Hamiltonian cycle throughout the search. The heuristic phase was used **only to select a route/candidate**. It is not part of the proof. Once the displayed matching was found, every proof-critical assertion was independently rechecked by the exact certificate described below.

The same witness has Hamiltonian LCF offsets relative to the source cycle

`[6,-6,7,-5,9,5,-6,7,9,-7,-5,5,7,-9,-7,6,-5,-9,5,-7]`.

Outcome of #19: **success**. Encoding the source constraint into the search removed the previous “ambient optimum may be non-Hamiltonian” failure mode entirely.

## 7. Method #26 — HUNT THE SPORADIC CASE: target the rare high-connectivity girth-6 stratum

Exoo--Kolokolnikov--Janssen--Salamon's published exhaustive/high-girth table records maximum algebraic connectivity `1.064568` for cubic graphs with `n=20`, girth 6. Since for a cubic graph

`AC(G)=3-lambda_2(A_G)`,

the displayed exact witness has

`AC(G)=3-alpha=1.064567668029970...`,

which agrees with that published decimal to six places. This is strong route validation: the source-valid Hamiltonian construction lands directly in the rare high-connectivity stratum that the previous report identified from the ambient cubic literature.

I do **not** identify the witness with a particular database graph ID, claim uniqueness, or infer a global `C_20` optimum from a rounded table. The House of Graphs census reports only 32 cubic order-20 graphs of girth at least 6 and none of girth at least 7, making the stratum genuinely small, but cubic graphs with smaller girth remain part of the source optimization unless separately bounded.

Outcome of #26: **success as a sporadic-family locator**. It found the right stratum and supplied a source-valid exact witness, while preserving the distinction between a candidate-selection heuristic and a global optimum proof.

## 8. Exact finite self-check

New artifacts, both in this track's namespace:

- `proofnet24/NM13-07/artifacts/2026-09-18/e0095_c20_nonbipartite_exact.py`
  - creation commit `f479893946d3969d79c42c198a63cae4eabd6d9e`;
- `proofnet24/NM13-07/artifacts/2026-09-18/e0095_c20_nonbipartite_exact.out`
  - creation commit `84ca35233f2c6dd7ad233bc213ff6d42b717cb57`.

The checker was executed before archival. It verifies with exact combinatorics/integer-rational algebra:

- `M` is a perfect matching and contains no cycle edge;
- the graph is connected and 3-regular;
- the fixed `0,1,...,19,0` cycle is a Hamilton cycle;
- the graph is nonbipartite and has girth exactly 6;
- the full characteristic polynomial factorization above;
- exact Sturm root counts isolating the second eigenvalue;
- exact bracket `19354/10000 < lambda_2 < 19355/10000`;
- therefore `lambda_2<2` and `gap>1/3`.

The archived output ends `ALL_EXACT_CHECKS_PASS`. Decimal eigenvalues are printed only for readability and are not used as proof.

This is a **self-check**, not an independent audit.

## 9. Fresh bounded literature/status check — 2026-09-18

I rechecked the original source and current/nearby literature using dated queries for the exact Diaconis title and Question 4, `cycle + perfect matching`, deterministic fastest mixing/spectral gap, cubic Hamiltonian algebraic connectivity, and later random-matching work.

Recovered source/status items:

1. **Persi Diaconis, 2013, Question 4.** The current arXiv text still asks which perfect matching gives fastest mixing on a connected regular graph and explicitly highlights the cycle case and the desire for accurate convergence rates. The source wording is unchanged in the retrieved version.
2. **Hermon--Sly--Sousi, Annals of Probability 50 (2022), “Universality of cutoff for graphs with an added random matching.”** This proves a typical-random-matching cutoff theorem for broad bounded-degree base graphs. It does not give the deterministic finite optimizer asked for here.
3. **Baran--Hermon--Šarković--Sousi, Probability Theory and Related Fields 193 (2025), “Phase transition for random walks on graphs with added weighted random matching.”** This studies weighted random matchings and cutoff/phase transition, again not the exact deterministic `C_20` optimization.
4. **Exoo--Kolokolnikov--Janssen--Salamon, Journal of Graph Theory (2024), “Attainable bounds for algebraic connectivity and maximally-connected regular graphs.”** Their cubic table gives, at order 20 and girth 6, maximum algebraic connectivity `1.064568`, matching the present witness's exact value to six decimals.
5. **House of Graphs cubic census.** Its current cubic census page reports 510489 connected cubic graphs on 20 vertices, 32 of girth at least 6, and none of girth at least 7.
6. The Flinders cubic-graph property database documentation advertises Hamiltonicity, Hamilton-cycle count, girth, bipartiteness, second-largest eigenvalue, and diameter on common rows through 20 vertices. The web surface did not expose the binary census payload in a form I could inspect during this run, so I did not infer any graph ID or database Hamiltonicity result from it. The explicit source construction above makes that join unnecessary for the theorem proved here.

This bounded search recovered **no source-wide resolution of Diaconis Question 4 and no prior exact statement of the displayed matching/witness**. That is negative evidence only; it is not proof of worldwide openness or publication novelty. Publication novelty of the finite `C_20` corollary is **UNVERIFIED**.

## 10. Status, metric discipline, and mandatory next run

The parent source remains **OPEN**. NM13-07 remains **PARTIAL**. The new exact theorem is:

> There exists a source-admissible nonbipartite `C_20 +` perfect matching with `lambda_2<2`, hence spectral gap `>1/3`; since every bipartite source matching has gap at most `1/3`, no bipartite matching is globally optimal at `C_20`.

The frozen metric remains

`g_16^* = 1 - sqrt(3)/3 -> 1 - sqrt(3)/3`.

This is now the **third consecutive run without movement of the frozen metric**. Under the controlling Section-I rule, the **next NM13-07 invocation must be a thinking-only stuck-recovery run with no new mathematical claim**. It must state the exact blocker, all routes tried and why they stopped, the missing proof ingredient, the simplest still-unproved special case, and the nearest solved problem/technique, then choose exactly one allowed recovery action. No prospective Section-B methods are credited as tried in advance.

Neither P26 nor NM13-08 is counted as an audit. No paper folder is created. No shared root, peer namespace, workflow, email, Drive item, public site, permission, or schedule was modified.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-07
  source_id: E0095
  claim_id: E0095
  canonical_dedup_key: diaconis_mcmc::q4
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: g_16^*
  metric_before: 1 - sqrt(3)/3
  metric_after: 1 - sqrt(3)/3
  metric_movement: none
  new_claim_scope: >-
    Explicit source-admissible nonbipartite C20-plus-perfect-matching
    construction with second adjacency eigenvalue alpha<2, where alpha is
    the unique root of x^3+2x^2-4x-7 in (19354/10000,19355/10000), hence
    gap 1-alpha/3>1/3; combined with the prior exact bipartite C20 theorem,
    no bipartite matching is globally optimal at C20.
  finite_certificate:
    checker: proofnet24/NM13-07/artifacts/2026-09-18/e0095_c20_nonbipartite_exact.py
    output: proofnet24/NM13-07/artifacts/2026-09-18/e0095_c20_nonbipartite_exact.out
    result: ALL_EXACT_CHECKS_PASS
  methods_actual:
    - 2: source-valid counterexample to bipartite optimality; succeeded
    - 19: two-switch algorithm in fixed Hamiltonian/source coordinates; succeeded
    - 26: targeted rare order-20 girth-6 high-connectivity stratum; succeeded
  unchanged_runs_since_metric_movement: 3
  stuck_recoveries_used: 0
  audits_passed:
    P26: false
    NM13-08: false
  next_step: >-
    Mandatory Section-I thinking-only stuck-recovery invocation with no new
    mathematical claim; preserve E0095 and the frozen g_16^* metric.
```
