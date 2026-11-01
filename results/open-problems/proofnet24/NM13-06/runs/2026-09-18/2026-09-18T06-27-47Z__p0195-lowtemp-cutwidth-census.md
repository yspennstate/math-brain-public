Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `n_edge^* >= 6 -> n_edge^* >= 6`. Section-B methods actually tried: #7 TAKE THE LIMIT, #13 FIND WHAT ONLY INCREASES, #26 HUNT THE SPORADIC CASE. This is the third consecutive unchanged run, so the NEXT P0195 invocation must be the owner-prescribed Section-I stuck-recovery report.**

# NM13-06 research invocation — P0195 low-temperature cutwidth route and exact six-vertex barrier census

Run date: 2026-09-18 UTC  
Track / namespace: `proofnet24/NM13-06`  
Category: CLOSABLE OUTSIDE  
Canonical source / claim: `P0195`, `operations/claims/P0195.md`  
Parent source status after this run: **OPEN**  
NM13-06 status after this run: **PARTIAL**  
Frozen metric before / after: **`n_edge^* >= 6 -> n_edge^* >= 6`**  
Consecutive unchanged runs since the last frozen-metric movement: **2 -> 3**  
Stuck recoveries used: **0 -> 0**  
Designated eventual outside auditors: **P26 and NM13-07; neither is counted as passed**

## 1. Runtime and task-control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The exposed task-control surface still provides task title/prompt, schedule or relative-start fields, timing mode, and enabled state, but **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface that exposes those controls together with authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` response was an authorization-context boundary; current repository policy records that a later P26 update succeeded from another authorized context. The legitimate workaround is therefore the owning/authorized task surface or platform support, never duplication or access-control bypass. No schedule, permission, workflow, or support escalation was attempted here.

## 2. Continuity, ownership, exclusions, and required repository read

This invocation continues the already admitted **P0195 — Monotonicity of the ferromagnetic Ising spectral gap** assignment. It does not reopen intake, create a second claim, alter the source clause, change normalization, or reset the frozen metric.

Before new mathematics I reread or targeted-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0195.md`;
- current exact-ID, title, canonical-key, claim, handoff, attempt, POSTED, campaign, and audit searches for P0195;
- the current NM13-06 report chain through newest report `proofnet24/NM13-06/runs/2026-09-18/2026-09-18T05-28-52Z__p0195-bridge-connected-reduction.md`;
- newest neighboring reports recovered from NM13-05 and NM13-07, namely NM13-05's terminal D0004 handoff at commit `651c40a94ecd9b191045a93e00e6c10349c60c6a` and NM13-07's terminal E0095 handoff at commit `4ff06dd20c3ff0eaba71f70ee5f6f2c3d19299b4`.

Canonical identity remains:

- source ID `P0195`;
- dedup key `monotonicity_of_the_ferromagnetic_ising_spectral_gap`;
- SHA256 `102de34178ace6c6ebb4f5b99308978b4b29fae78f3af1988614584ee288c807`;
- residue `5 mod 13`, matching NM13-06's exclusive shard;
- exclusive owner `proofnet24/NM13-06`.

The immutable claim remains present under that owner. I recovered no owner-authorized release, competing owner under another alias, source-level POSTED closure, campaign settlement, retirement, or passed P0195 audit. Large root and intake surfaces can be connector-bounded, so exact ID/key/path retrieval and the immutable claim remain the continuity anchors; I do not infer that inaccessible or deleted history is empty.

The current mathematical continuity is:

1. the admission run certified the source edge-addition clause through three vertices, moving `UNMEASURED -> n_edge^* >= 4`;
2. the exact four-vertex run moved `n_edge^* >= 4 -> >= 5`;
3. the exact five-vertex theorem moved `n_edge^* >= 5 -> >= 6`;
4. the next run proved all connected six-vertex marked types with at least 13 source edges but did not move the frozen metric;
5. the immediately preceding run proved a universal bridge-addition theorem, reduced every minimal counterexample source to a connected graph, certified all 170 disconnected six-vertex marked types, and left exactly **399 connected six-vertex marked types with at most 12 source edges** unresolved. That run moved the unchanged counter `1 -> 2` and explicitly reserved methods #7/#13/#26 for the present invocation.

## 3. Exact source and fresh bounded literature/status check — 2026-09-18

I rechecked the original Levin--Peres--Wilmer open-problem text. Chapter 23 states that the section assumes Glauber dynamics unless another mechanism is specified. Question 2 asks whether the Ising spectral gap is monotone increasing in temperature and whether it is monotone decreasing under addition of edges. It then states the stronger inhomogeneous ferromagnetic interaction version and notes Nacu's cycle result.

This worker continues only the literal **edge-addition clause** in the frozen zero-field, common-`beta`, random-scan one-site heat-bath setting, one uniformly chosen update per discrete step. It does not claim the separate temperature clause or the full inhomogeneous-coupling strengthening.

Fresh bounded public-web queries on 2026-09-18 used combinations of:

- the exact LPW Question-2 edge-addition wording;
- `ferromagnetic Ising spectral gap adding edges Glauber monotonicity`;
- `Ising Glauber low temperature spectral gap cutwidth`;
- `cut-width Ising relaxation time canonical paths`;
- recent 2025--2026 Ising spectral-gap and Glauber-mixing queries.

The search again recovered no source-matching theorem or counterexample settling the LPW edge-addition question. It recovered Mossel--Sly, *Exact thresholds for Ising--Gibbs samplers on general graphs*, Annals of Probability 41 (2013). Their cutwidth lemma gives, for a finite graph with interaction strengths bounded by `beta`, cutwidth `E`, and maximum degree `d`, the **one-sided upper bound on discrete-time relaxation time**

`tau_rel <= n^2 exp(4 beta (E+d))`.

It also recovered Eldan--Koehler--Zeitouni (2022), which proves a high-temperature Poincare/spectral-gap condition under an operator-norm assumption rather than edge-addition monotonicity. Low-temperature finite-volume papers recovered by the search concern special lattices/boundary conditions and do not supply an exact arbitrary-finite-graph edge-comparison theorem.

This is **bounded negative evidence only**. It is not proof of worldwide openness and not a publication-novelty certificate. Publication novelty remains **UNVERIFIED**. The cutwidth/canonical-path mechanism is standard literature machinery and is not claimed as new.

## 4. Frozen model and metric

For a finite simple graph `G=(V,E)`, let

`mu_G,beta(sigma) proportional exp(beta * sum_{uv in E} sigma_u sigma_v)`

on `{−1,+1}^V`, and let `P_G(beta)` be random-scan one-site heat-bath dynamics choosing one vertex uniformly at each discrete step. For an absent edge `e`, compare `G` and `G+e` at the same finite `beta>=0` and the same one-update-per-step normalization.

The frozen metric is

`n_edge^* = min{|V(G)| : there exist an absent edge e and finite beta>=0 with gap_beta(G+e) > gap_beta(G)}`,

with `n_edge^*=+infinity` if no counterexample exists.

Before this run: `n_edge^* >= 6`.  
After this run: **`n_edge^* >= 6`**.

Nothing below certifies all 399 remaining connected order-six marked types, so the frozen metric honestly does not move.

## 5. Idea before code

Before writing the finite checker I recorded the route at

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_cutwidth_idea.md`

creation commit `1a741c6d867f10d0d0ca7d5171cade242df3f048`, blob `c01547d0025209e40b9ffb0e1aed37f900d5c0ec`.

The prior high-temperature theorem already gives the correct edge-addition sign for every fixed marked graph on some interval `0<=beta<epsilon(G,e)`. The new question was whether the opposite boundary, `beta -> infinity`, has a graph parameter with a monotone edge-addition sign that can be transferred rigorously to the spectral gap.

The candidate is graph **cutwidth**. The route was deliberately split into two questions:

1. does cutwidth itself move monotonically under edge addition, and how often is the increase strict on the exact six-vertex frontier?;
2. does existing low-temperature theory convert that graph-parameter comparison into the required exact spectral-gap comparison?

Only the first question receives a finite checker. No numerical spectral scan is promoted to evidence.

## 6. Method #7 — TAKE THE LIMIT: low temperature exposes a real but presently insufficient barrier statistic

For a vertex ordering `pi=(v_1,...,v_n)`, write

`cw_pi(G)=max_{1<=k<n} |delta_G({v_1,...,v_k})|`

and

`cw(G)=min_pi cw_pi(G)`.

This parameter is physically and mathematically natural at low temperature because canonical-path bounds for Ising Glauber dynamics are controlled by the number of disagreeing interactions that an ordered spin-flip route must cross.

The bounded literature check located the precise rigorous transfer currently available for arbitrary finite graphs in Mossel--Sly's formulation: if the interaction strengths are bounded by `beta`, cutwidth is `E`, and maximum degree is `d`, then

`tau_rel(G,beta) <= n^2 exp(4 beta (E+d)).`          (6.1)

This is useful route information but it is **not enough** for P0195. Suppose an edge is added and cutwidth rises. Formula (6.1) merely gives the target a larger allowed upper bound on relaxation time. It does not say the target relaxation time actually exceeds the source relaxation time, and therefore it does not prove

`gap_beta(G+e) <= gap_beta(G)`.

I did not recover, in the bounded search, a general theorem identifying the exact low-temperature exponential rate of the finite-graph heat-bath spectral gap with cutwidth, nor a two-sided capacity estimate strong enough to compare an arbitrary source and target at fixed order. Special-lattice metastability results do not supply that missing source-uniform comparison.

**Outcome of #7: blocked at a precise transfer step.** The low-temperature limit supplies a plausible barrier statistic, but the rigorous theorem currently recovered is one-sided. I therefore make no low-temperature spectral-gap claim and do not count the cutwidth route as frozen-metric progress.

## 7. Method #13 — FIND WHAT ONLY INCREASES: cutwidth is an exact edge-addition monovariant

Although cutwidth does not yet control the spectral-gap comparison tightly enough, its graph-theoretic monotonicity is exact and elementary.

### Lemma `NM13-06-P0195-CW-MONO-09`

For every finite simple graph `G` and every absent edge `e`,

`cw(G+e) >= cw(G)`.

### Proof

Fix any vertex ordering `pi`. For every prefix set `S_k`, adding an edge either leaves the cut size unchanged or adds one crossing edge. Hence

`|delta_{G+e}(S_k)| >= |delta_G(S_k)|`

for every `k`, so

`cw_pi(G+e) >= cw_pi(G)`.

Let `pi_*` minimize `cw_pi(G+e)`. Then

`cw(G+e) = cw_{pi_*}(G+e) >= cw_{pi_*}(G) >= cw(G)`.

QED.

This is the kind of monovariant method #13 asked for: it never decreases under edge addition. The problem is now sharply separated into a **graph-theoretic success** and a **Markov-chain transfer gap**. A future low-temperature theorem need not rediscover the graph inequality; it would only need to connect the actual gap to this barrier strongly enough.

**Outcome of #13: success as a structural invariant, but not a source theorem.** It does not move `n_edge^*`.

## 8. Method #26 — HUNT THE SPORADIC CASE: exact six-vertex cutwidth census

Only after the route above was written down did I build a self-contained exact integer checker. It does not use NetworkX, floating point, a precomputed graph atlas, or an external enumeration file.

The checker:

1. represents the 15 possible edges on six labelled vertices as bits;
2. constructs the exact `S_6` action on edge masks;
3. obtains one representative of every unlabeled six-vertex graph by full orbit marking;
4. tests connectivity by exact bitset BFS;
5. for each connected representative, computes automorphism orbits of missing edges, hence one representative of every connected marked edge-addition isomorphism type;
6. computes cutwidth from its definition by exhaustive minimization over all `6! = 720` vertex orders;
7. checks every target cutwidth against its source and records the exact transition census.

It independently recovers the known atlas sizes

- **156** unlabeled simple graphs on six vertices;
- **112** connected unlabeled graphs;
- **402** connected marked edge-addition types.

The exact cutwidth transition distribution is

```
(1,2): 6
(2,2): 29    (2,3): 62
(3,3): 44    (3,4): 84
(4,4): 65    (4,5): 54
(5,5): 17    (5,6): 23
(6,6): 6     (6,7): 8
(7,7): 1     (7,8): 2
(8,9): 1
```

Thus among all 402 connected marked types:

- **240** have a strict cutwidth increase;
- **162** are cutwidth ties;
- every strict increase at order six is exactly by one.

The preceding dense theorem already covers exactly the three connected marked types with at least 13 source edges; all three lie in the strict-cutwidth class. Therefore on the still-unresolved 399-type frontier:

- **237** have strict cutwidth increase;
- **162** are cutwidth ties.

The tie counts by source edge number are

`{5:19, 6:15, 7:34, 8:49, 9:25, 10:13, 11:6, 12:1}`.

The densest tie is unique up to marked isomorphism. In the checker's canonical labelling it is

`source mask 4095, missing edge (3,4), cw 7 -> 7`.

Structurally the source is

`K_3 join 3 K_1`,

and the target is obtained by adding one edge inside the independent three-set. This is a highly symmetric **12-edge source**, so it is a particularly clean special case for the mandatory stuck-recovery run now triggered.

Crucially, the checker itself prints the scope guard

`cutwidth census only; no spectral-gap inequality is inferred from cutwidth`

and ends

`ALL_EXACT_CHECKS_PASS`.

Artifact paths and exact repository receipts:

- checker: `proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_cutwidth_census_exact.py`, creation commit `a1cbe44eab5ed15072fd8db42009d5b72aa60920`, blob `55c1175b6b5d0c0a9a4ebd08e0f341d59bd728e5`;
- executed output: `proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_cutwidth_census_exact.out`, creation commit `84fcfd83eeadcb2583d1d51f07c44bcd927bbda2`, blob `5fc83418bdec695c8ca2149749c14657afded32b`.

This is a **self-check**, not an independent audit.

**Outcome of #26: success as an exact route-selection certificate.** It isolates the precise 162-case barrier-blind stratum and, within it, one unique densest symmetric marked type. It does not prove any new spectral-gap inequality by itself.

## 9. What moved mathematically, and what did not

The frozen source metric did **not** move:

`n_edge^* >= 6 -> n_edge^* >= 6`.

There is nevertheless useful new structural information:

1. cutwidth is now proved on the page to be an edge-addition monovariant;
2. the exact connected six-vertex frontier splits into 240 strict-cutwidth types and 162 ties;
3. after removing the three already-certified dense marked types, the remaining 399 split into 237 strict and 162 tied cutwidth transitions;
4. the unique densest tied transition is `K_3 join 3K_1` with one edge added inside the independent triple;
5. the precise reason the low-temperature route does not yet prove P0195 is identified: the recovered arbitrary-graph cutwidth theorem is a one-sided **upper bound on relaxation time**, not a comparison or exact low-temperature asymptotic.

I deliberately do **not** relabel the 237 strict-cutwidth types as solved. That would silently replace a spectral-gap statement by a graph-layout statistic and violate the frozen metric.

## 10. Third unchanged run: mandatory next-run stuck protocol

The unchanged-run counter is now **3**. Under the controlling owner policy, this invocation itself is still the reserved #7/#13/#26 new-method attack, but the **next** P0195 invocation must be the Section-I thinking/stuck-recovery report, with no routine continuation.

That next report must include all five required items:

(a) the exact blocking statement, in one displayed formula;
(b) every route tried and the precise reason each failed or stopped;
(c) what a proof would have to contain that no current route contains;
(d) the simplest special case still unproved;
(e) the nearest solved problem in the literature and the ingredient its proof has that P0195 lacks.

The present run has now made item (d) unusually concrete: the recommended simplest/highest-density unresolved symmetric case is

`G = K_3 join 3K_1`, add one edge inside the independent three-set.

The next invocation must choose exactly one owner-permitted recovery action. The natural candidate, to be decided in that report rather than silently executed here, is **prove the simplest unproved special case** using the existing exact odd-quotient/resultant machinery or find a shorter representation-theoretic comparison. If that route is chosen, it must still be judged against the frozen source metric rather than replacing the metric by a case count.

No paper folder is created. Parent source status remains OPEN, track status remains PARTIAL, and neither designated outside auditor is counted as passed.

## 11. Operational boundaries

No shared root, peer namespace, canonical claim file, schedule, workflow, permission, public surface, email/Drive item, or paid-compute resource was modified. The only writes were the warranted own-namespace idea note, exact checker, executed checker output, and this single immutable own-namespace report. No external unreviewed script was executed.

## 12. Structured `ledger_delta` for P26

```json
{
  "track": "NM13-06",
  "category": "CLOSABLE OUTSIDE",
  "source_id": "P0195",
  "claim_id": "P0195",
  "canonical_dedup_key": "monotonicity_of_the_ferromagnetic_ising_spectral_gap",
  "shard_mod_13": 5,
  "source_status": "OPEN",
  "track_status": "PARTIAL",
  "metric": {
    "name": "n_edge^*",
    "before": ">= 6",
    "after": ">= 6",
    "movement": false
  },
  "methods": [
    {
      "number": 7,
      "name": "TAKE THE LIMIT",
      "outcome": "low-temperature/cutwidth route identified; recovered arbitrary-graph theorem is only a one-sided relaxation-time upper bound, so no spectral-gap comparison follows"
    },
    {
      "number": 13,
      "name": "FIND WHAT ONLY INCREASES",
      "outcome": "proved cutwidth is monotone nondecreasing under every edge addition; structural invariant only, not a gap theorem"
    },
    {
      "number": 26,
      "name": "HUNT THE SPORADIC CASE",
      "outcome": "exact n=6 census: 240 strict cutwidth increases, 162 ties; after prior dense coverage, 237 strict plus 162 ties remain; unique densest tie is K3 join 3K1 plus one internal independent-set edge"
    }
  ],
  "new_claims": [
    "NM13-06-P0195-CW-MONO-09: graph cutwidth is nondecreasing under addition of an edge",
    "exact six-vertex connected marked-edge cutwidth census: 402 types = 240 strict increases + 162 ties",
    "unique 12-edge cutwidth-tie marked type is K3 join 3K1 with one edge added inside the independent 3-set"
  ],
  "unchanged_runs": {
    "before": 2,
    "after": 3
  },
  "stuck_recoveries": {
    "before": 0,
    "after": 0
  },
  "finite_frontier": {
    "n6_connected_marked_types": 402,
    "n6_connected_dense_already_covered": 3,
    "n6_connected_remaining": 399,
    "remaining_strict_cutwidth": 237,
    "remaining_cutwidth_ties": 162
  },
  "idea_note": {
    "path": "proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_cutwidth_idea.md",
    "commit": "1a741c6d867f10d0d0ca7d5171cade242df3f048",
    "blob": "c01547d0025209e40b9ffb0e1aed37f900d5c0ec"
  },
  "checker": {
    "path": "proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_cutwidth_census_exact.py",
    "commit": "a1cbe44eab5ed15072fd8db42009d5b72aa60920",
    "blob": "55c1175b6b5d0c0a9a4ebd08e0f341d59bd728e5"
  },
  "output": {
    "path": "proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_cutwidth_census_exact.out",
    "commit": "84fcfd83eeadcb2583d1d51f07c44bcd927bbda2",
    "blob": "5fc83418bdec695c8ca2149749c14657afded32b",
    "result": "ALL_EXACT_CHECKS_PASS"
  },
  "audits": {
    "P26": "NOT PASSED / not presumed",
    "NM13-07": "NOT PASSED / not presumed"
  },
  "literature_check": {
    "date": "2026-09-18",
    "scope": "original LPW Question 2; exact edge-addition wording; Ising Glauber low-temperature spectral-gap/cutwidth queries; Mossel-Sly cutwidth bound; recent high-temperature and low-temperature spectral-gap queries",
    "outcome": "no source-matching edge-addition resolution recovered; Mossel-Sly supplies a one-sided cutwidth-based relaxation-time upper bound, insufficient for the desired comparison",
    "qualification": "bounded negative evidence only; worldwide openness and publication novelty unverified"
  },
  "next_step": "MANDATORY Section-I stuck-recovery report on the next P0195 invocation; no routine lemma run. Recommended simplest special case to analyze is the unique 12-edge cutwidth tie K3 join 3K1 -> add one edge inside the independent triple.",
  "next_if_unchanged": "not applicable before the required stuck-recovery invocation; the current run itself is unchanged run 3"
}
```
