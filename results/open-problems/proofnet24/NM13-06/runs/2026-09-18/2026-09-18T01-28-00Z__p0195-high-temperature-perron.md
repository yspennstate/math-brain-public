Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `n_edge^* >= 5 -> n_edge^* >= 5`. Section-B methods actually tried: #5, #11, #20.**

# NM13-06 research invocation — P0195 high-temperature Perron reduction and the exact five-vertex obstruction

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-06`  
Category: CLOSABLE OUTSIDE  
Canonical source/claim: `P0195`, `operations/claims/P0195.md`  
Parent source status after this run: **OPEN**  
NM13-06 status after this run: **PARTIAL**  
Unchanged-run count since the last frozen-metric movement: **1**  
Stuck-recovery count: **0**  
Designated eventual outside auditors: **P26 and NM13-07; neither is counted as passed**

## 1. Runtime/control disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**; the reasoning-effort telemetry exposed to this report is **UNVERIFIED**. I therefore do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The exposed task-control surface continues to offer title/prompt, schedule or relative-start fields, timing mode and enabled state, but no bindable model-family selector and no bindable reasoning-effort selector. Thus `GPT-6 / maximum` is still only prompt text here. Making it enforceable would require an authorized product/workspace/API surface that actually exposes those controls and runtime attestation. The historical P26 `You cannot modify this task` result remains an authorization/context boundary rather than an ownership release; current `RESULTS.md` records that a later P26 update succeeded from another authorized context. The valid workaround for another denial is the owning/authorized account, workspace, product or admin surface, not task cloning or a permission bypass. No support escalation is claimed.

No schedule was created, modified, disabled, or otherwise changed in this run.

## 2. Continuity, ownership, and required repository read

This run continues the already admitted P0195 target from

`proofnet24/NM13-06/runs/2026-09-18/2026-09-18T00-25-49Z__p0195-n4-orbit-sturm.md`.

It does **not** reopen intake, create another claim, change the source clause, or reset the metric. The preceding run proved edge-addition monotonicity for every graph on at most four vertices and every finite common inverse temperature, moving the frozen metric to `n_edge^* >= 5`.

Before new mathematics I reread or targeted-recovered the current controlling and continuity surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the current P0195 claim;
- exact-ID/dedup searches over the intake/campaign material and historical limited attempt;
- my newest P0195 report;
- newest recovered neighboring reports from NM13-05 and NM13-07.

The canonical identity remains

`P0195 — Monotonicity of the ferromagnetic Ising spectral gap`,

with dedup key

`monotonicity_of_the_ferromagnetic_ising_spectral_gap`,

SHA256

`102de34178ace6c6ebb4f5b99308978b4b29fae78f3af1988614584ee288c807`,

whose integer value is `5 mod 13`, NM13-06's exclusive shard. Current `master` still has the create-only P0195 claim owned by `proofnet24/NM13-06`. I recovered no release, handoff, retirement, alternate-ID owner, POSTED source settlement, or competing claim.

Large root files and JSONL inventories can be connector-truncated when fetched wholesale. I therefore used the current root views plus exact-ID/key and focused claim/report reads. I do not interpret connector truncation or bounded code search as proof that inaccessible history is empty. No critical P0195 continuity used below was inaccessible.

## 3. Exact source and fresh bounded literature check

The exact source remains Levin–Peres–Wilmer, *Markov Chains and Mixing Times*, second edition, Chapter 26 Question 2 (same wording in the older public edition as Chapter 23 Question 2). Under the chapter convention of Glauber dynamics, it asks whether the Ising spectral gap is monotone increasing in temperature and whether it is monotone decreasing under addition of edges. This worker continues only the literal **edge-addition** clause for zero-field ferromagnetic Ising with one common coupling `beta >= 0`, under random-scan one-site heat-bath dynamics. It does not claim the temperature clause or the full inhomogeneous-coupling strengthening.

The bounded literature check dated 2026-09-18 UTC included the exact LPW wording, the addition-of-edges phrase, coupling-monotonicity searches, Nacu's cycle theorem, and later papers citing or discussing those monotonicity questions. It recovered:

- S. Nacu, *Glauber dynamics on the cycle is monotone*, Probab. Theory Relat. Fields 127 (2003), 177–185, DOI `10.1007/s00440-003-0279-x`; this proves monotonicity in individual couplings for a cycle.
- T. Shirai, *A remark on monotonicity for the Glauber dynamics on finite graphs*, Proc. Japan Acad. Ser. A 86 (2010), 33–37, DOI `10.3792/pjaa.86.33`. Shirai explicitly treats the spectral-gap monotonicity as open and refutes a **stronger fixed-time single-spin expectation monotonicity conjecture**, not the spectral-gap statement. In particular, the existence of Shirai's finite-graph counterexample is not a counterexample to LPW Question 2.
- Later high-temperature spectral-gap/spectral-independence and finite-system critical-gap papers, none recovered as a theorem or counterexample settling the LPW edge-addition clause.

I did not recover a later source-matching proof or counterexample, nor a publication stating the exact high-temperature theorem or the five-vertex finite classification proved below. This is **bounded negative evidence only**, not proof of worldwide openness and not a novelty certificate. Publication novelty remains **UNVERIFIED**.

## 4. Frozen metric: no movement

The frozen model is unchanged: for a finite simple graph `G`, zero-field ferromagnetic Ising at common inverse temperature `beta >= 0`, random-scan one-site heat-bath dynamics, and an absent edge `e`, compare `G` and `G+e` at the same `beta` and the same one-site-per-step normalization.

The frozen metric is

`n_edge^* = min{|V(G)| : there exist an absent edge e and finite beta>=0 with gap_beta(G+e) > gap_beta(G)}`,

with `n_edge^*=+infinity` if no counterexample exists.

Before this run:

`n_edge^* >= 5`.

After this run:

`n_edge^* >= 5`.

So there is **no frozen-metric movement**. The new theorems are source-relevant progress, but they do not certify all five-vertex graphs for all temperatures and therefore do not justify changing `n_edge^*`.

## 5. New idea before code

The four-vertex proof used an exact odd/automorphism quotient and then compared algebraic top-root branches globally in `z=e^{2 beta}`. Pushing that machinery blindly to five vertices would reverse the owner's priority: it would create a large certificate before understanding what should be true.

The intended methods #5/#11/#20 suggested a different question first:

> What is the **universal infinitesimal effect** of adding a ferromagnetic edge at `beta=0`, and exactly which five-vertex edge-addition types are invisible to that first-order test?

At infinite temperature, the heat-bath operator has a highly degenerate but completely explicit Walsh spectrum. That makes `beta=0` the point where one can differentiate exactly, identify the dual object controlling the slow-mode slope, and then use an exact five-vertex calculation only to classify the exceptional first-order ties.

This route produced a theorem valid for **every finite graph**, not just order five, plus a precise reason why the previous automorphism quotient ceases to be an efficient deformation method at order five.

## 6. Method #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

Let `G=(V,E)`, `|V|=n`, and write

`H_G(sigma)=sum_{uv in E} sigma_u sigma_v`,

`mu_beta(sigma) = Z_beta^{-1} exp(beta H_G(sigma))`.

Let `P_beta` be one random-scan heat-bath step. Put

`S_beta = D_beta^(1/2) P_beta D_beta^(-1/2)`,

where `D_beta=diag(mu_beta)`. Reversibility makes `S_beta` real symmetric, and all its entries are analytic near `beta=0`.

At `beta=0`, the chain independently resamples one uniformly chosen spin. On Walsh characters

`chi_A(sigma)=prod_{i in A} sigma_i`,

we have

`P_0 chi_A = (1-|A|/n) chi_A`.

Thus the second-eigenvalue cluster is

`alpha = 1-1/n`

with multiplicity `n`, on the linear-spin space

`E_1 = span{sigma_1,...,sigma_n}`.

Let `Pi` denote the orthogonal projection to `E_1` in the uniform inner product. Differentiating the heat-bath action on a coordinate spin gives, exactly,

`P_beta sigma_j = (1-1/n) sigma_j + (1/n) tanh(beta sum_{u~j} sigma_u)`,

hence

`P'_0 sigma_j = (1/n) sum_{u~j} sigma_u`.

Therefore, in the basis `(sigma_1,...,sigma_n)`,

`Pi P'_0 Pi = A_G/n`,

where `A_G` is the ordinary adjacency matrix.

The similarity transform does not alter this first-order compression. Indeed `S'_0=P'_0+[K,P_0]` for a diagonal `K` coming from differentiating `D_beta^(1/2)`, while `P_0=alpha I` on `E_1`; hence

`Pi [K,P_0] Pi = 0`.

Finite-dimensional symmetric degenerate perturbation theory now says that the `n` eigenvalue branches issuing from `alpha` have first derivatives equal to the eigenvalues of `A_G/n`. All other Walsh eigenvalues are separated from `alpha` at `beta=0`, so the actual second eigenvalue is the top branch for sufficiently small positive `beta`.

### Theorem `NM13-06-P0195-HT-01` — universal high-temperature expansion

For every finite simple graph `G` on `n` vertices,

`lambda_2(P_G(beta)) = 1 - 1/n + (beta/n) rho(A_G) + O_G(beta^2)`

as `beta downarrow 0`, and therefore

`gap_beta(G) = 1/n - (beta/n) rho(A_G) + O_G(beta^2)`.

This also gives a source-faithful edge-coupling deformation. If the absent edge is `{u,v}`, put strength `t in [0,1]` on that edge and define

`J_t=A_G+t(e_u e_v^T+e_v e_u^T)`.

Then

`gap_{beta,t}=1/n-(beta/n)rho(J_t)+O(beta^2)`.

Where the top eigenvalue of `J_t` is simple, Hellmann–Feynman gives

`d rho(J_t)/dt = 2 q_u(t) q_v(t) >= 0`

for a nonnegative unit Perron vector `q(t)`. Thus the first-order slow-mode effect of increasing a ferromagnetic coupling has the conjectured sign.

Outcome of #5: **success. The high-temperature derivative is controlled exactly by adjacency Perron data, for every finite graph, and the edge-strength deformation has a nonnegative first-order derivative.**

## 7. Method #11 — DUALIZE

The same first-order theorem has a useful dual/Rayleigh formulation:

`rho(J_t)=max_{||x||_2=1} x^T J_t x`.

Because `J_t` is entrywise nonnegative, a maximizing vector may be chosen entrywise nonnegative. Hence increasing the edge `{u,v}` changes the objective by

`2 dt x_u x_v >= 0`

at every nonnegative test vector. This is the positive dual witness the previous run was looking for: the first-order high-temperature gap comparison is not a graph-by-graph polynomial accident; it is the Rayleigh monotonicity of the Perron root.

This dual picture also resolves a subtle equality case. Write the connected components of `G` as `G_i`, of sizes `m_i`. Random-scan heat bath on the disjoint union has the exact tensor-sum form

`P_G = sum_i (m_i/n) P_{G_i} tensor I_{others}`,

so

`gap_G(beta) = min_i (m_i/n) gap_{G_i}(beta)`.

Suppose an added edge does **not** strictly increase the global adjacency spectral radius. Perron–Frobenius strictness implies that every component touched by the new edge had adjacency spectral radius strictly below the old global maximum; otherwise modifying or joining a maximizing irreducible block would increase the Perron root. Therefore at least one untouched component still carries the old global Perron radius.

Using the expansion componentwise,

`(m_i/n) gap_{G_i}(beta) = 1/n - (beta/n) rho(A_{G_i}) + O(beta^2)`.

For sufficiently small positive `beta`, the source minimum is attained among the untouched Perron-maximizing components. Those same components remain present after the edge is added, so the target gap is at most the source gap.

### Corollary `NM13-06-P0195-HT-EDGE-02`

For every finite simple graph `G` and every absent edge `e`, there exists `epsilon(G,e)>0` such that

`gap_beta(G+e) <= gap_beta(G)`

for all `0 <= beta < epsilon(G,e)`.

If `rho(A_{G+e})>rho(A_G)`, the inequality is strict for all sufficiently small `beta>0`.

Outcome of #11: **success. Every finite edge addition has the conjectured sign on a nontrivial high-temperature interval; the only first-order ties are explained by untouched Perron-dominant components.**

## 8. Method #20 — FIND WHY THE ALGORITHM FAILS

Only after the structural theorem was in hand did I use exact finite computation at order five.

Use canonical edge-bit order

`(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)`.

Exact `S_5` canonicalization gives:

- `34` unlabeled simple graphs on five vertices;
- `74` isomorphism classes of **marked edge additions** `(G,e)`.

Comparing adjacency Perron roots exactly, via integer characteristic polynomials and exact rational root isolation/gcd, gives:

- `71` marked types with `rho(A_{G+e}) > rho(A_G)`;
- exactly `3` Perron-radius ties.

The three canonical tied transitions are

`1 -> 20`, `3 -> 28`, `19 -> 184`.

Their graph structures are:

1. `K_2 + 3 K_1  ->  2 K_2 + K_1`;
2. `P_3 + 2 K_1  ->  P_3 + K_2`;
3. `K_3 + 2 K_1  ->  K_3 + K_2`.

The common top adjacency factors are respectively

`x(x-1)(x+1)`, `x(x^2-2)`, and `(x-2)(x+1)^2`.

These are not merely first-order ties: they are **exact all-temperature equality cases** for the Glauber spectral gap.

For a two-vertex edge at common `beta`,

`gap_{K_2}(beta) = (1-tanh beta)/2`.

For a three-vertex graph `H`, the previous NM13-06 theorem proves exact edge-addition monotonicity through three vertices. In particular, for `H=P_3` or `K_3`, comparing down to `K_2+K_1` gives

`gap_H(beta) <= gap_{K_2+K_1}^{(3)}(beta) = (1-tanh beta)/3`.

Now apply the exact disjoint-union formula. For `H+2K_1` on five vertices, the `H` contribution is `(3/5)gap_H`. For `H+K_2`, the newly added `K_2` contribution is `(2/5)gap_{K_2}=(1-tanh beta)/5`, while

`(3/5)gap_H <= (1-tanh beta)/5`.

So the same `H` contribution remains the global minimum and the gap is unchanged. The `K_2+3K_1 -> 2K_2+K_1` case is immediate from the same formula.

### Theorem `NM13-06-P0195-N5-TIES-03`

Among the 74 five-vertex marked edge-addition isomorphism types, exactly three have equal source/target adjacency Perron radius, and all three satisfy

`gap_beta(G+e)=gap_beta(G)`

for **every** finite `beta>=0`.

Hence any five-vertex counterexample, if one exists, must lie among the remaining **71** strict-Perron types and must occur away from a sufficiently small high-temperature interval.

### Why the four-vertex automorphism/Sturm algorithm does not port cleanly

The previous run gained a large reduction from graph automorphisms. A coupling deformation `t in (0,1)` must preserve not only the unweighted base graph but the marked edge whose weight differs from the others. Exact stabilizer enumeration on the 74 marked five-vertex types shows:

`22`

have **trivial marked stabilizer**. The first canonical example is source mask `3`, marked nonedge bit `5` (edge `(1,3)`), target canonical mask `21`.

For such a generic intermediate weight, there is no nontrivial graph automorphism left. Spin flip still halves the 32-state chain, but the odd invariant sector has dimension `16`; the small automorphism quotients that made the four-vertex all-`beta` Sturm proof efficient disappear.

Outcome of #20: **success. The exact first obstruction is now identified: 22/74 marked deformations lose all graph symmetry, and the first-order theorem leaves 71 strict-Perron types requiring a genuinely different global-in-beta idea.**

## 9. Exact finite self-check

The theorem-sized high-temperature perturbation argument above is written on the page and does not depend on finite enumeration. The order-five classification is finite and therefore has an exact checker.

Checker:

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_n5_high_temp_structure.py`

creation commit:

`8a18b92fa5beecc244963c2e01c775c17487893d`

Archived executed output:

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_n5_high_temp_structure.out`

creation commit:

`398c32690342090891af91d1bc87870003333929`

The checker independently/exactly verifies:

- 34 unlabeled five-vertex graph classes;
- 74 marked edge-addition types;
- exact Perron comparison: 71 strict and 3 ties;
- the exact three tied canonical transitions and their component structures;
- exact common characteristic-polynomial top factors for the ties;
- 22 marked types with trivial marked stabilizer;
- the first explicit trivial-stabilizer marked type `(source mask 3, marked bit 5, target mask 21)`.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent P26 or NM13-07 audit.

## 10. What moved mathematically, and what did not

The frozen witness-size metric did not move. What did move is the structure of the unresolved five-vertex problem:

- before this run, five vertices meant 74 marked types with an all-temperature continuum parameter and no general endpoint control;
- after this run, **every** finite graph is certified in a source-valid high-temperature neighborhood, the three five-vertex first-order ties are removed completely by exact all-temperature equality, and only 71 strict-Perron five-vertex types remain as possible counterexamples away from `beta=0`;
- a direct continuation of the previous automorphism/Sturm deformation route is now known to encounter 22 marked types with no graph symmetry at intermediate coupling.

This is substantive source-relevant progress but not enough to change `n_edge^* >= 5`.

## 11. Remaining obligation

To move the frozen metric to `n_edge^* >= 6`, one must still certify

`gap_beta(G+e) <= gap_beta(G)`

for the 71 strict-Perron five-vertex marked types for **all** `beta>=0`, not merely in a type-dependent high-temperature neighborhood.

Alternatively, one exact five-vertex pair and one rigorously certified finite `beta` with the reverse inequality would determine `n_edge^*=5` and refute the source's edge-addition clause.

The present theorem gives no uniform explicit `epsilon` and no low-temperature comparison. I do not silently promote the first-order sign into a global sign.

## 12. Next research route

The next run must not repeat any of the three preceding triples `#2/#9/#10`, `#14/#16/#24`, or `#5/#11/#20`. The next intended methods are:

- **#6 DEFORM TO A POINT YOU CAN SOLVE:** analyze the `beta -> infinity` endpoint for the 71 strict-Perron five-vertex types and derive exact low-temperature exponents/leading coefficients; the goal is to eliminate an interval from the opposite end rather than enlarge a mid-temperature certificate blindly.
- **#15 BREAK THE SYMMETRY ON PURPOSE:** start with the first trivial-marked-stabilizer type and use an energy-level/spin-coordinate basis instead of graph automorphisms; if a generic asymmetric pair is tractable, it addresses the precise obstruction identified this run.
- **#18 SAY IT IN ANOTHER LANGUAGE:** rewrite the five-vertex gap comparison as a reversible Dirichlet/conditional-variance generalized eigenvalue inequality and look for a positive determinant or Loewner witness that remains meaningful without graph symmetry.

The concrete next milestone remains the frozen metric: certify all five-vertex additions and move `n_edge^*` to at least 6, or produce an exact five-vertex counterexample and determine `n_edge^*=5`.

## 13. Structured ledger_delta for P26

```json
{
  "track": "NM13-06",
  "source_id": "P0195",
  "claim_id": "P0195",
  "category": "CLOSABLE OUTSIDE",
  "source_status": "OPEN",
  "worker_status": "PARTIAL",
  "metric": "n_edge^* = minimum vertex count of a common-beta zero-field heat-bath edge-addition counterexample",
  "metric_before": "n_edge^* >= 5",
  "metric_after": "n_edge^* >= 5",
  "movement": false,
  "methods_actual": [5, 11, 20],
  "method_outcomes": {
    "5": "proved universal beta->0 second-eigenvalue expansion and nonnegative edge-strength Perron derivative",
    "11": "Rayleigh/Perron duality yields source-valid high-temperature edge monotonicity for every finite graph, including equality-case component analysis",
    "20": "exact n=5 classification: 74 marked types, 71 strict Perron increases, 3 exact all-beta ties; 22 marked deformations have trivial stabilizer"
  },
  "theorem_ids": [
    "NM13-06-P0195-HT-01",
    "NM13-06-P0195-HT-EDGE-02",
    "NM13-06-P0195-N5-TIES-03"
  ],
  "finite_scope": "all 74 five-vertex marked edge-addition isomorphism types classified by adjacency Perron behavior; three ties removed exactly for all beta",
  "checker": "proofnet24/NM13-06/artifacts/2026-09-18/p0195_n5_high_temp_structure.py",
  "checker_commit": "8a18b92fa5beecc244963c2e01c775c17487893d",
  "output": "proofnet24/NM13-06/artifacts/2026-09-18/p0195_n5_high_temp_structure.out",
  "output_commit": "398c32690342090891af91d1bc87870003333929",
  "checker_result": "ALL_EXACT_CHECKS_PASS",
  "unchanged_runs_since_metric_movement": 1,
  "stuck_recoveries_used": 0,
  "p26_audit": "NOT_COUNTED",
  "secondary_audit_nm13_07": "NOT_COUNTED",
  "next_methods": [6, 15, 18],
  "next_step": "attack the 71 strict-Perron five-vertex types from beta=infinity and through an asymmetric Dirichlet/generalized-eigenvalue formulation",
  "literature_check_date": "2026-09-18",
  "literature_scope": "LPW exact question; Nacu 2003 cycle monotonicity; Shirai 2010 stronger fixed-time monotonicity counterexample; later spectral-gap/mixing papers",
  "literature_result": "no source-matching resolution recovered in bounded search; novelty UNVERIFIED"
}
```

No shared root, peer file, audit request, public post, email, Drive object, workflow, permission, or schedule was changed in this invocation.
