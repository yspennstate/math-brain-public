Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `n_edge^* >= 6 -> n_edge^* >= 6`. Section-B methods actually tried, transparently reused because all thirty have already been used on P0195: #18 SAY IT IN ANOTHER LANGUAGE, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #20 FIND WHY THE ALGORITHM FAILS. This is the sixth consecutive unchanged P0195 invocation, so NM13-06 records a terminal handoff and rotates; there must not be a seventh P0195 research run on this track.**

# NM13-06 research invocation — P0195 communication-barrier theorem and six-run handoff

Run date: 2026-09-18 UTC  
Track / namespace: `proofnet24/NM13-06`  
Category: CLOSABLE OUTSIDE  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Canonical source / claim: `P0195`, `operations/claims/P0195.md`  
Canonical dedup key: `monotonicity_of_the_ferromagnetic_ising_spectral_gap`  
Shard: `5 mod 13`  
Parent source status after this run: **OPEN (bounded status check only)**  
NM13-06 status after this run: **PARTIAL / HANDOFF / ROTATE**  
Frozen metric before / after: **`n_edge^* >= 6 -> n_edge^* >= 6`**  
Consecutive unchanged P0195 invocations: **5 -> 6**  
Stuck-recovery episodes used: **1 -> 1**  
Designated eventual outside auditors: **P26 and NM13-07; neither is counted as passed**

## 1. Runtime and task-control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The currently exposed task-control surface still offers title/prompt, schedule or relative-start fields, timing mode, enabled state, and ordinary task identifiers, but **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. Making it enforceable would require an owner-authorized product/workspace/API/admin surface that exposes persistent model and reasoning fields together with authenticated per-run runtime attestation.

The historical P26 `You cannot modify this task` event remains an authorization-context boundary, not a release of mathematical ownership. Current repository state records that a later P26 update succeeded from another authorized context. The lawful workaround for a denied modification is therefore the owning/otherwise-authorized account, workspace, product/admin/API surface, or platform support; never task cloning or an access-control bypass. No task, schedule, workflow, permission, email, Drive item, or public surface was changed in this invocation.

## 2. Authoritative continuity and required repository read

This is **not a new admission**. It continues the already admitted P0195 target under the immutable claim `operations/claims/P0195.md`. Before substantive work I reread or targeted-recovered the current controlling material required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0195.md`;
- exact-ID/title/dedup-key claim, attempt, handoff, POSTED, campaign, and audit searches for P0195;
- the full current NM13-06 report chain through the immediately preceding report `2026-09-18T08-42-00Z__p0195-split-lowtemp-tail.md`;
- newest recovered neighboring NM13-05 and NM13-07 reports.

The canonical identity remains P0195 with SHA256 `102de34178ace6c6ebb4f5b99308978b4b29fae78f3af1988614584ee288c807`, residue `5 mod 13`, and exclusive owner `proofnet24/NM13-06`. I recovered no competing claim, owner-authorized release, source retirement, POSTED source closure, campaign settlement, or passed P0195 audit. The neighboring workers are on other admitted targets and do not supply a P0195 audit.

Large append-only JSONL/root surfaces can be connector-bounded when fetched wholesale. I therefore used current root views together with exact source/key/claim/history searches and the immutable claim as continuity anchors; I do not infer that inaccessible or unrendered history is empty. No material P0195 continuity needed below was inaccessible.

The previous P0195 run proved, for the unique densest six-vertex cutwidth tie `K_3 join 3K_1 -> + one independent-part edge`, strict low-temperature ordering for `beta >= (1/2) log 19`, but correctly left the frozen metric at `n_edge^* >= 6` and advanced the unchanged counter to five. It also stated explicitly that a sixth unchanged run must hand off and rotate.

## 3. Exact source and bounded current literature check — 2026-09-18

The exact source remains Levin--Peres--Wilmer, *Markov Chains and Mixing Times*, open-problem chapter, Question 2 (second-edition locator Chapter 26; older public edition Chapter 23). Under the chapter's Glauber-dynamics convention it asks whether the ferromagnetic Ising spectral gap is monotone increasing in temperature and monotone decreasing when edges are added. This worker preserves only the literal **edge-addition clause** in the frozen zero-field, common-`beta`, random-scan one-site heat-bath model.

Fresh bounded public-web searches on 2026-09-18 included:

- `monotonicity ferromagnetic Ising spectral gap adding edges Glauber dynamics 2026`;
- the exact Shirai title `A remark on monotonicity for the Glauber dynamics on finite graphs`;
- the exact Nacu title `Glauber Dynamics On The Cycle Is Monotone`;
- `Ising Glauber spectral gap cutwidth low temperature finite graph`;
- `communication height Glauber dynamics Ising spectral gap finite graph cutwidth`;
- `canonical paths Ising cutwidth spectral gap low temperature`.

The search recovered Nacu's 2003 theorem that relaxation time on a finite cycle is increasing in each coupling, and Shirai's 2010 paper, which explicitly describes the general spectral-gap coupling-monotonicity question as open there while disproving a stronger fixed-time single-spin expectation monotonicity statement. It also recovered later spectral-gap/mixing work in high-temperature or geometric regimes, including Eldan--Koehler--Zeitouni's high-temperature Poincare theorem, but no theorem or counterexample settling the exact LPW edge-addition clause and no source matching the six-vertex barrier result below.

This is **bounded negative evidence only**. It is not proof of worldwide openness or publication novelty. The energy-barrier, canonical-path, bottleneck, and conductance mechanisms used below are standard/folklore Markov-chain machinery; publication novelty of this particular finite classification is **UNVERIFIED**.

## 4. Frozen model and metric

For a finite simple graph `G=(V,E)`, `|V|=n`, let

`mu_G,beta(sigma) proportional exp(beta * sum_{uv in E} sigma_u sigma_v)`

on `{−1,+1}^V`, and let `P_G(beta)` be random-scan one-site heat-bath dynamics with one uniformly selected site per discrete step. For an absent edge `e`, compare `G` and `G+e` at the same finite `beta>=0` and the same normalization.

The frozen metric remains

`n_edge^* = min{|V(G)| : there exist an absent edge e and finite beta>=0 with gap_beta(G+e) > gap_beta(G)}`,

with `n_edge^*=+infinity` if no counterexample exists.

Before this run: `n_edge^* >= 6`.  
After this run: **`n_edge^* >= 6`**.

The theorem below resolves a large low-temperature six-vertex stratum but not all temperatures and not the 162 barrier-tie marked types. It therefore does **not** justify changing the frozen metric.

## 5. Refutation-first check and idea before code

Before trying to prove another monotonicity theorem I looked for a low-temperature obstruction. Write a configuration as the subset `S subseteq V` of minus spins relative to all-plus, and define the cut-energy height

`h_G(S) = |delta_G(S)|`.

Adding an edge can only increase each individual cut height by zero or one, so any low-temperature counterexample cannot come from a *smaller* energy communication barrier after edge addition. The remaining possibility is that the relevant slow spectral mode is not controlled sharply enough by that barrier.

The new route was written **before code** in

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_barrier_idea.md`

creation commit `9836c1de04f715ef935f56e13e9a5d81aa8f3b30`, blob `7527a9637d3cd8da7469602d4901efc7b983b8b4`.

The proposal was to translate the chain to the configuration hypercube, prove a two-sided exponential comparison between the spectral gap, communication barrier, and graph cutwidth, and only then perform the exact six-vertex barrier census.

## 6. Method #18 reused — SAY IT IN ANOTHER LANGUAGE: configuration energy barriers

For `S subseteq V`, after removing the common ground-state factor from the Ising weight, set

`a_beta(S) = exp(-2 beta h_G(S))`,
`Z_beta = sum_S a_beta(S)`.

If `S,T` differ at exactly one vertex, the heat-bath transition and reversible edge conductance satisfy the exact identity

`Q_beta(S,T) := mu_beta(S) P_beta(S,T)
 = [1/(n Z_beta)] * a_beta(S)a_beta(T)/(a_beta(S)+a_beta(T))`.        (6.1)

If `M(S,T)=max(h_G(S),h_G(T))`, then

`[1/(2 n Z_beta)] exp(-2 beta M(S,T))
 <= Q_beta(S,T)
 <= [1/(n Z_beta)] exp(-2 beta M(S,T))`.                         (6.2)

Also `2 <= Z_beta <= 2^n`, because the all-plus and all-minus states both have height zero and every normalized weight is at most one.

Define the exact communication barrier

`b(G) = min_gamma max_{S in gamma} h_G(S)`,                        (6.3)

where the minimum is over all nearest-neighbor hypercube paths from `emptyset` to `V`. Let `cw(G)` denote graph cutwidth.

Every monotone path induced by a vertex ordering is an admissible hypercube path, so

`b(G) <= cw(G)`.                                                   (6.4)

The point of the next theorem is that the spectral gap can be sandwiched between these two graph/configuration barriers with constants depending only on `n`, not on `beta`.

## 7. New theorem — two-sided finite-graph low-temperature barrier bound

### Theorem `NM13-06-P0195-BARRIER-LOWTEMP-10`

Let `G` be a connected nontrivial simple graph on `n` vertices. For every `beta>=0`, zero-field random-scan one-site heat-bath Glauber dynamics satisfies

`[1/(n^2 4^n)] exp(-2 beta cw(G))
 <= gap_beta(G)
 <= 2^(3n-2) exp(-2 beta b(G))`.                                 (7.1)

Consequently, for two graphs `G,H` on the same `n` vertices, if

`Delta := b(H) - cw(G) > 0`,                                      (7.2)

then

`gap_beta(H)/gap_beta(G)
 <= n^2 2^(5n-2) exp(-2 beta Delta)`,                             (7.3)

and in particular `gap_beta(H) < gap_beta(G)` whenever

`beta > [log(n^2 2^(5n-2))]/(2 Delta)`.                           (7.4)

### Proof: upper bound

Let `b=b(G)`. Consider the subgraph of the configuration hypercube induced by states with `h_G(S)<b`, and let `A` be the connected component containing `emptyset`. By the definition of `b`, the all-minus state `V` is not in `A`; otherwise there would be an `emptyset`-to-`V` path of maximal height below `b`.

Both `A` and `A^c` therefore contain a height-zero ground state. Since `Z_beta<=2^n`,

`mu_beta(A) >= 2^(-n)`,
`mu_beta(A^c) >= 2^(-n)`.                                        (7.5)

If a hypercube edge crosses from `A` to `A^c`, at least one endpoint has height at least `b`; otherwise both endpoints would lie in the same sublevel component. By (6.2), every crossing conductance is at most

`[1/(n Z_beta)] exp(-2 beta b)`.

The `n`-cube has `n 2^(n-1)` undirected edges and `Z_beta>=2`, so

`Q_beta(A,A^c) <= 2^(n-2) exp(-2 beta b)`.                        (7.6)

Use the test function `1_A` in the Poincare/Rayleigh characterization. Its variance is `mu(A)mu(A^c) >= 2^(-2n)`, while its Dirichlet form is exactly `Q(A,A^c)`. Thus

`gap_beta(G) <= 2^(3n-2) exp(-2 beta b(G))`.                      (7.7)

### Proof: lower bound

Choose a vertex ordering `v_1,...,v_n` realizing `cw(G)=c`. For each ordered pair of spin configurations `X,Y`, define a canonical path from `X` to `Y` by scanning this fixed ordering and flipping exactly those coordinates on which `X` and `Y` differ.

At any intermediate stage corresponding to a prefix `P={v_1,...,v_k}`, the current configuration `Z` agrees with `Y` on `P` and with `X` outside `P`. Every disagreeing graph edge internal to `P` is already counted by `h_G(Y)`; every disagreeing edge internal to `P^c` is counted by `h_G(X)`; and there are at most `c` graph edges crossing `P,P^c`. Therefore

`h_G(Z) <= h_G(X)+h_G(Y)+c`.                                     (7.8)

The same bound holds at both endpoints of every transition on this canonical path. Let `q=(z,z')` be one such state-space edge. From the lower half of (6.2),

`1/Q_beta(q) <= 2 n Z_beta exp(2 beta max(h(z),h(z')))`.          (7.9)

For every ordered pair `(X,Y)` whose canonical path uses `q`, multiply (7.9) by

`mu_beta(X) mu_beta(Y) |gamma_XY|`.

Using `|gamma_XY|<=n`, (7.8), and

`mu_beta(X)mu_beta(Y)=exp(-2 beta(h(X)+h(Y)))/Z_beta^2`,

we obtain the uniform bound

`[mu(X)mu(Y)|gamma_XY|]/Q(q)
 <= [2 n^2/Z_beta] exp(2 beta c)
 <= n^2 exp(2 beta c)`.                                          (7.10)

There are at most `4^n` ordered pairs `(X,Y)`. Hence the standard canonical-path congestion bound gives

`gap_beta(G)^(-1) <= n^2 4^n exp(2 beta c)`,                      (7.11)

which is the lower bound in (7.1).

Finally divide the upper bound for `H` by the lower bound for `G` to obtain (7.3), and solve the strict inequality in (7.3) to obtain (7.4). QED.

### Scope and folklore warning

This theorem is written out here because it is used quantitatively below. Its ingredients—energy barriers, bottleneck test functions, and canonical-path congestion—are standard Markov-chain machinery. I do **not** claim that the general form (7.1) is publication-novel.

## 8. Method #16 reused — COMPUTE EVERY SMALL CASE: exact six-vertex barrier census

Only after the theorem was in hand did I execute the finite computation proposed in the idea note.

The checker is

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_barrier_exact.py`

creation commit `efc323689d9a60fda667b4892e037b67a94b76fa`, blob `d5a24e04307f10d9dbe1a9dd59564a275a2275e1`.

The executed output is

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_barrier_exact.out`

creation commit `d75c4edf617c7ab5e0bf33cf366dd295afd7beec`, blob `8f9703ca8a41d038268a7dd6d56f38127fd35c15`.

The checker uses exact integer arithmetic only. It independently reconstructs all `156` unlabeled six-vertex graphs, the `112` connected classes, exact `S_6` automorphism orbits of absent edges, graph cutwidth by all `6!` orderings, and the communication barrier by exact minimax shortest-path search on the 64-state configuration hypercube.

It certifies:

- `b(G)=cw(G)` for **all 112 connected unlabeled six-vertex graphs**;
- the same previously certified **402 connected marked edge-addition types**;
- **240** strict cutwidth transitions and **162** ties;
- every strict transition has `cw(H)=cw(G)+1` and therefore `b(H)>cw(G)`;
- the unique 12-edge tie remains the split graph `K_3 join 3K_1`, mask `4095`, with transition `(cw,b): (7,7) -> (7,7)`.

The archived run ends `ALL_EXACT_CHECKS_PASS`. I also read the archived output back at its creation commit. This is a **self-check**, not an independent outside audit.

## 9. Source-relevant six-vertex consequence with an explicit uniform temperature

For every one of the 240 connected six-vertex marked edge additions with strict cutwidth increase, the exact checker gives

`Delta = b(H)-cw(G) = 1`.

Apply (7.4) with `n=6`. The constant simplifies exactly:

`6^2 * 2^(5*6-2) = 36 * 2^28 = 9 * 2^30 = 98304^2`.

Therefore:

### Corollary `NM13-06-P0195-N6-STRICTCW-LOWTEMP-11`

For every connected six-vertex source graph `G` and absent edge `e` such that

`cw(G+e)=cw(G)+1`,

zero-field random-scan one-site heat-bath dynamics satisfies

`gap_beta(G+e) < gap_beta(G)`

for every finite

`beta > log(98304)`.

Numerically `log(98304)=11.495819997...`.

This covers **240 of the 402 connected six-vertex marked edge-addition isomorphism types** with one common rigorous low-temperature threshold. It is a source-valid restricted theorem, not a source closure.

## 10. Method #20 reused — FIND WHY THE ALGORITHM FAILS: the exact obstruction is the 162 barrier ties

The barrier route now fails for a precise reason rather than an unspecified missing lemma.

For all 162 remaining connected marked types,

`cw(H)=cw(G)`

and the exact census gives

`b(H)=b(G)=cw(G)=cw(H)`.

Thus the exponent comparison in (7.3) has `Delta=0` and cannot force either spectral-gap ordering at low temperature, regardless of how much the constants in (7.1) are improved while only the exponent is tracked. The unique densest tie was already pushed one level deeper in the preceding report, where exact quotient algebra separated its low-temperature prefactors and proved the desired sign for `beta >= (1/2)log 19`.

For the other 161 ties, a successful continuation would need information absent from this route: exact leading prefactors/capacities, a direct all-temperature comparison, or a new structural theorem that groups many ties at once. Repeating cutwidth or barrier certificates would be bookkeeping, not progress.

Outcome of #20: **success as a route diagnosis, not as frozen-metric movement.** It identifies exactly which marked types the exponent method can and cannot touch.

## 11. Mandatory six-run handoff

This is the **sixth consecutive P0195 invocation without movement of the frozen metric** after it reached `n_edge^* >= 6`. Under the owner's CLOSABLE rotation rule, this is the terminal P0195 research invocation for NM13-06. The next NM13-06 research state is **ADMISSION_PENDING for a different genuinely unassigned residue-5 CLOSABLE source**. NM13-06 must not execute a seventh P0195 research run unless a later explicit owner-authorized reassignment overrides this handoff.

The canonical claim is intentionally left immutable; this report records the handoff/rotation and does not pretend that a worker can release or overwrite shared ownership state by fiat. P26/shared-state maintenance may reconcile root ledgers separately.

### Preserved P0195 handoff state

Exact source clause retained: zero-field ferromagnetic Ising, common finite `beta`, random-scan one-site heat-bath, test whether adding an edge can ever increase the spectral gap.

Frozen metric at handoff:

`n_edge^* >= 6`.

Certified progress to preserve:

1. exact all-temperature edge-addition monotonicity for every graph through five vertices;
2. universal first-order high-temperature expansion controlled by the adjacency Perron root, and a source-valid small-`beta` interval for every finite edge addition;
3. universal bridge-addition theorem and connected-source reduction for a minimal counterexample;
4. exact all-temperature theorem for the three connected six-vertex marked types with at least 13 source edges;
5. exact connected six-vertex frontier: 402 marked types = 240 strict-cutwidth transitions + 162 cutwidth ties;
6. the unique densest tie `K_3 join 3K_1 -> + independent-part edge` has strict desired ordering for `beta >= (1/2)log 19` with exact low-temperature prefactors;
7. this run's theorem: all 240 strict-cutwidth types have strict desired ordering for the uniform range `beta > log(98304)`; exact barrier census proves `b=cw` on all 112 connected six-vertex graph classes.

Remaining source obligation at handoff:

- full all-temperature comparison for the connected six-vertex frontier, especially the 162 barrier/cutwidth ties (161 beyond the split tie's certified low-temperature interval), before the frozen metric can move to `n_edge^* >= 7`;
- after order six, the unrestricted source remains open unless a general proof or counterexample is found.

No outside closure audit has passed for P0195: **P26 = NOT PASSED; NM13-07 = NOT PASSED**. No paper folder is created because the parent source is not closed and the required audit gate is unmet.

## 12. Why the metric does not move

The frozen quantity is the smallest vertex order of an actual source counterexample. It moved earlier only when all graphs through order five were certified for all finite temperatures. This run gives a strong uniform low-temperature theorem for 240 six-vertex connected marked types, but a counterexample could still exist at order six in one of the unresolved temperature/type regions. Therefore the only honest metric statement is

`n_edge^* >= 6 -> n_edge^* >= 6`.

The six-run rotation rule is triggered by that unchanged source metric even though substantial restricted theorems were proved along the way.

## 13. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-06
  category: CLOSABLE_OUTSIDE
  source_id: P0195
  claim_id: P0195
  canonical_dedup_key: monotonicity_of_the_ferromagnetic_ising_spectral_gap
  shard_mod_13: 5
  source_status: OPEN
  worker_status: PARTIAL_HANDOFF_ROTATE
  metric_name: n_edge^*
  metric_before: ">= 6"
  metric_after: ">= 6"
  movement: false
  unchanged_runs_before: 5
  unchanged_runs_after: 6
  stuck_recoveries_before: 1
  stuck_recoveries_after: 1
  methods_actual_reused_transparently:
    - 18
    - 16
    - 20
  new_theorems:
    - id: NM13-06-P0195-BARRIER-LOWTEMP-10
      statement: "For connected nontrivial n-vertex G, (n^2 4^n)^(-1)e^(-2 beta cw(G)) <= gap_beta(G) <= 2^(3n-2)e^(-2 beta b(G)); hence b(H)>cw(G) implies an explicit eventual strict edge-addition ordering."
    - id: NM13-06-P0195-N6-STRICTCW-LOWTEMP-11
      statement: "All 240 connected six-vertex marked edge additions with strict cutwidth increase satisfy gap_beta(G+e)<gap_beta(G) for beta>log(98304)."
  exact_certificate:
    idea_path: proofnet24/NM13-06/artifacts/2026-09-18/p0195_barrier_idea.md
    checker_path: proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_barrier_exact.py
    output_path: proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_barrier_exact.out
    checker_result: ALL_EXACT_CHECKS_PASS
    certified_connected_graphs: 112
    certified_marked_types: 402
    strict_barrier_separations: 240
    barrier_ties: 162
  audits:
    P26: NOT_PASSED
    NM13-07: NOT_PASSED
  literature_check_date: 2026-09-18
  novelty: UNVERIFIED
  terminal_handoff: true
  rotation_reason: SIX_CONSECUTIVE_UNCHANGED_CLOSABLE_RUNS
  next_state: ADMISSION_PENDING_FOR_DIFFERENT_RESIDUE_5_CLOSABLE_SOURCE
```

No shared root, peer namespace, canonical claim, task/schedule, workflow, permission, public surface, email/Drive resource, or paid compute was modified. This report is the one immutable run report for this invocation; its creation commit is to be read back directly, with no receipt-only follow-up commit.
