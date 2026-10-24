Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `n_edge^* >= 5 -> n_edge^* >= 5`. Section-B methods actually tried: #6, #15, #18.**

# NM13-06 research invocation — P0195 exact all-temperature path transitions beyond the marked-symmetry obstruction

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-06`  
Category: CLOSABLE OUTSIDE  
Canonical source/claim: `P0195`, `operations/claims/P0195.md`  
Parent source status after this run: **OPEN**  
NM13-06 status after this run: **PARTIAL**  
Unchanged-run count since the last frozen-metric movement: **2**  
Stuck-recovery count: **0**  
Designated eventual outside auditors: **P26 and NM13-07; neither is counted as passed**

## 1. Runtime/control disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I therefore do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The exposed task-control surface continues to offer prompt/title, schedule or relative-start fields, timing mode, and enabled state, but no bindable model-family selector and no bindable reasoning-effort selector. Thus `GPT-6 / maximum` remains prompt text only here. Enforcing it would require an authorized product/workspace/API/admin surface exposing those controls and per-run runtime attestation. The historical P26 `You cannot modify this task` result remains an authorization/context boundary; repository policy records a later successful P26 update from another authorized context. The valid remedy for another denial is the owning or otherwise authorized surface (or platform support), not cloning the task or bypassing access controls.

No schedule was created, modified, disabled, or otherwise changed in this run.

## 2. Continuity, ownership, and required repository read

This invocation continues the already admitted **P0195 — Monotonicity of the ferromagnetic Ising spectral gap** target. It does not reopen intake, create a second claim, alter the source clause, or reset the frozen metric.

Before new mathematics I reread or targeted-recovered the current controlling and continuity surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- current claim `operations/claims/P0195.md`;
- exact-ID/canonical-key intake and historical-attempt searches;
- my newest report `proofnet24/NM13-06/runs/2026-09-18/2026-09-18T01-28-00Z__p0195-high-temperature-perron.md`;
- newest recovered neighboring reports from NM13-05 and NM13-07.

Canonical identity is unchanged:

- source ID `P0195`;
- dedup key `monotonicity_of_the_ferromagnetic_ising_spectral_gap`;
- SHA256 `102de34178ace6c6ebb4f5b99308978b4b29fae78f3af1988614584ee288c807`;
- residue `5 mod 13`, matching NM13-06's exclusive shard;
- owner `proofnet24/NM13-06`.

I recovered no release, handoff, retirement, competing claim, alternate-ID owner, POSTED source-level closure, or campaign settlement. Large root and JSONL files can be connector-truncated; I used the current root views together with exact-ID/key/claim/report searches and do not interpret bounded rendering as proof that inaccessible history is empty. No material P0195 continuity needed below was inaccessible.

## 3. Exact source and fresh bounded literature check

The source remains Levin–Peres–Wilmer, *Markov Chains and Mixing Times*, Question 2 in the Ising open-problem chapter (Chapter 26 in the second edition; Chapter 23 in the older public edition). Under the chapter convention of Glauber dynamics, it asks whether the Ising spectral gap is monotone increasing in temperature and whether it is monotone decreasing under addition of edges.

This worker continues only the literal **edge-addition clause** for the zero-field ferromagnetic Ising model with one common inverse temperature `beta>=0`, using random-scan single-site heat-bath dynamics under the same one-site-per-step normalization before and after the edge addition. It does not claim the separate temperature clause or the full inhomogeneous-coupling strengthening.

A fresh bounded literature search dated 2026-09-18 used the exact LPW wording, `spectral gap Ising addition of edges`, `Glauber monotonicity coupling`, Nacu's cycle theorem, Shirai's finite-graph monotonicity paper, and 2025–2026 variants. The exact LPW question is still present in the retrieved source. Nacu (2003) proves that on a finite cycle the relaxation time increases in each ferromagnetic coupling. Shirai (2010) gives a counterexample to a **stronger fixed-time single-spin expectation monotonicity statement**, not to the spectral-gap question. A current search result about edge-addition monotonicity of positive graph p-energy is a different spectral invariant and was excluded as source-irrelevant.

I recovered no source-matching theorem or counterexample settling the LPW edge-addition clause and no prior statement of the exact five-vertex path-transition theorem below. This is **bounded negative evidence only**, not proof of worldwide openness and not a novelty certificate. Publication novelty remains **UNVERIFIED**.

## 4. Frozen metric: no movement

The frozen metric remains

`n_edge^* = min{|V(G)| : there exist an absent edge e and finite beta>=0 with gap_beta(G+e) > gap_beta(G)}`,

with `n_edge^*=+infinity` if no counterexample exists.

The earlier exact four-vertex theorem certified `n_edge^*>=5`. The immediately preceding run did not move that bound but proved a universal high-temperature theorem and reduced the five-vertex search to 71 strict-Perron marked types after removing three exact all-temperature ties.

**Before this run:** `n_edge^* >= 5`.  
**After this run:** `n_edge^* >= 5`.

So the frozen metric does not move. The finite theorem below removes three of the 71 remaining five-vertex marked types completely, reducing that secondary unresolved-case count from `71` to `68`; that case count is **not** substituted for the frozen metric.

## 5. New idea before code

The previous run found the first structural obstruction to continuing the four-vertex interpolation proof: among the 74 five-vertex marked additions, 22 have **trivial marked stabilizer** once the added edge is given a distinct intermediate coupling. The first such type is source mask `3`, marked nonedge bit `5`, target canonical mask `21`.

The new idea is to stop insisting on symmetry along the interpolation. The source graph and target graph are ordinary unweighted graphs again, and each recovers endpoint automorphisms even when the *marked pair* has none. So instead of tracking a weighted edge continuously, compare the two endpoint second eigenvalues directly.

The first obstruction then becomes a path calculation rather than a 16-dimensional generic marked-sector problem. Two neighboring marked-trivial path transitions fall to the same mechanism, so the route closes three of the 22 marked-symmetry obstructions at once.

Use edge-bit order

`(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)`.

The three marked-stabilizer-one transitions are

- `(3,5,21)`: `P3 + 2 K1 -> P4 + K1`;
- `(21,8,58)`: `P4 + K1 -> P5`;
- `(28,5,58)`: `P3 + K2 -> P5`.

The exact checker independently verifies that the marked stabilizer is trivial in all three and that the target canonical masks are as displayed.

## 6. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: start at the low-temperature endpoint

Put

`x = tanh(beta)`,

so every finite `beta>=0` corresponds to `0<=x<1`, while the low-temperature endpoint `beta->infinity` is `x->1-`.

For the four endpoint graph classes involved below, the exact second-eigenvalue formulas obtained in Section 8 give three functions `A(x),B(x),C(x)` with

`lambda_2(mask 3)=lambda_2(mask 28)=A(x)`,
`lambda_2(mask 21)=B(x)`,
`lambda_2(mask 58)=C(x)`.

Their gap ratios at the solvable endpoint are exact:

`lim_{x->1-} (1-B)/(1-A) = 2/3`,

`lim_{x->1-} (1-C)/(1-B) = 3/4`,

`lim_{x->1-} (1-C)/(1-A) = 1/2`.

Thus all three edge additions have the conjectured strict direction at sufficiently low temperature, with nonzero leading separation. The useful discovery was not merely that the endpoint sign is correct, but that the same radicals appearing in these limits admit an elementary comparison on the *entire* interval `0<x<1`.

Outcome of #6: **success**. The beta-infinity deformation supplies exact leading gap ratios and exposes the algebraic expressions that later give a global proof.

## 7. Method #15 — BREAK THE SYMMETRY ON PURPOSE: discard the marked interpolation

For a ferromagnetic heat-bath chain, the monotonicity/spin-flip argument used in the four-vertex report applies to each endpoint graph: the true second eigenvalue occurs in the subspace that is odd under global spin flip and invariant under the endpoint graph automorphism group. Briefly, LPW's monotone-chain lemma supplies an increasing second-eigenvalue eigenfunction; subtracting its spin-flipped copy gives a nonzero odd increasing eigenfunction; averaging over graph automorphisms preserves nonzeroness because the all-plus state is fixed.

The previous failed route preserved the marked edge during a coupling deformation and thereby destroyed all nontrivial graph automorphisms for 22 marked types. Here I **break that marked symmetry framework on purpose**: source and target are diagonalized separately in their own endpoint automorphism quotients. For the first obstruction and the two adjacent path cases, the second-eigenvalue factor at each endpoint is only quadratic.

This is a substantive route change. No claim is made that every one of the remaining 19 marked-trivial types will have a quadratic endpoint factor; several do not. What this run establishes is that triviality of the *marked* stabilizer is not itself an obstruction to an exact all-temperature proof.

Outcome of #15: **success**. Three previously generic marked-symmetry obstructions collapse to small endpoint quotients.

## 8. Method #18 — SAY IT IN ANOTHER LANGUAGE: `x=tanh(beta)` turns the comparison into three radical inequalities

The exact finite computation constructs the heat-bath operator from the model definition, restricts it to the odd endpoint-automorphism quotient, factors the characteristic polynomial, and certifies by exact resultants plus rational Sturm isolation that the selected factor carries the largest quotient root throughout `0<x<1`.

For masks `3` and `28`, the top factor is

`F_A(L)=25(1+x^2)L^2 - 40(1+x^2)L + 16 + 14x^2`.

For mask `21`, it is

`F_B(L)=25(1+x^2)L^2 - (40(1+x^2)+5x)L + 16 + 15x^2 + 4x`.

For mask `58`, it is

`F_C(L)=25(1+x^2)^2 L^2 - 40(1+x^2)^2 L + 16 + 29x^2 + 15x^4`.

Their discriminants are exactly

`disc(F_A)=200 x^2(1+x^2)`,

`disc(F_B)=25 x^2(4x^2+5)`,

`disc(F_C)=100 x^2(1+x^2)^2(x^2+3)`.

Therefore their larger roots are

`A(x)=4/5 + [sqrt(2) x]/[5 sqrt(1+x^2)]`,

`B(x)=4/5 + x[1+sqrt(4x^2+5)]/[10(1+x^2)]`,

`C(x)=4/5 + x sqrt(x^2+3)/[5(1+x^2)]`.

At `x=0` all three equal `4/5`, as they must at infinite temperature. For `0<x<1`, I now prove

`A(x) < B(x) < C(x)`.

### `A<B`

After multiplying by the positive denominator and dividing by `x>0`, this is

`1 + sqrt(4x^2+5) > 2 sqrt(2) sqrt(1+x^2)`.

The right side minus 1 is positive. Squaring the equivalent inequality

`sqrt(4x^2+5) > 2 sqrt(2) sqrt(1+x^2)-1`

reduces exactly to

`sqrt(2) > sqrt(1+x^2)`,

which holds strictly for `x<1`.

### `B<C`

Likewise this is equivalent to

`2 sqrt(x^2+3) > 1 + sqrt(4x^2+5)`.

The left side minus 1 is positive. Squaring reduces exactly to

`2 > sqrt(x^2+3)`,

again strict for `x<1`.

Hence `A<B<C` on the whole finite-temperature interval. Since the discrete-time heat-bath spectral gap is `1-lambda_2`, each of the three displayed edge additions strictly decreases the gap for every finite `beta>0`, with equality only at `beta=0`.

Outcome of #18: **success**. The difficult-looking eigenvalue comparison becomes an elementary radical ordering after changing variables from `beta` to `x=tanh(beta)`.

## 9. New theorem proved this run

### Theorem `NM13-06-P0195-N5-PATH-04`

For zero-field ferromagnetic Ising with common finite inverse temperature `beta>=0` and random-scan one-site heat-bath dynamics on five vertices, each of the following single-edge additions satisfies

`gap_beta(G+e) <= gap_beta(G)`:

1. `P3 + 2 K1 -> P4 + K1`;
2. `P4 + K1 -> P5`;
3. `P3 + K2 -> P5`.

For every finite `beta>0`, all three inequalities are strict.

These three transitions all have trivial marked-edge stabilizer in the sense isolated by the preceding run. Thus three of the 22 marked-symmetry obstruction types are now completely certified despite the absence of any nontrivial symmetry along the intermediate weighted-edge deformation.

### Proof

At `beta=0`, all interactions vanish and every five-spin graph gives the same independent-spin random-scan chain, so `lambda_2=4/5` and all comparisons are equal.

For `beta>0`, set `x=tanh(beta) in (0,1)`. The endpoint monotonicity/spin-flip/automorphism argument places the true second eigenvalue in the odd endpoint-automorphism quotient. The exact finite certificate constructs those quotients directly from the heat-bath transition rule and proves globally on `0<x<1` that their top roots are the larger roots `A,B,C` of the three displayed quadratic factors, with masks `3,28` using `A`, mask `21` using `B`, and mask `58` using `C`.

Section 8 proves algebraically that `A<B<C` for every `0<x<1`. Therefore the target `lambda_2` exceeds the source `lambda_2` in each of the three edge additions, and hence the target spectral gap is strictly smaller. QED.

## 10. Exact finite self-check

The proof-critical finite checker is

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_n5_path_trivial_marked.py`

created at commit

`66ae0f064ea6a7452cf434a9da6eb5b40e90b325`.

Its executed output is archived at

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_n5_path_trivial_marked.out`

created at commit

`5415c81f1b8a69f15989ff6bbd4218afede6b29e`.

The checker verifies exactly:

- all three displayed source/marked-edge/target canonical transitions;
- marked stabilizer size one for each;
- construction of the 32-state heat-bath chains from the model definition;
- the odd endpoint-automorphism quotients;
- exact quotient characteristic-polynomial factorization;
- global dominance of the selected quadratic top factor against every other quotient factor on `0<x<1`, using exact resultants and rational Sturm root isolation;
- global target/source top-root ordering for all three transitions;
- the three exact discriminants;
- the low-temperature gap ratios `2/3`, `3/4`, and `1/2`.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent P26 or NM13-07 audit.

## 11. What moved and what did not

The frozen witness-size metric did not move: `n_edge^*>=5` remains the strongest certified source-level finite cutoff.

The unresolved five-vertex set did move structurally. The preceding run left 71 strict-Perron marked types that could still host a counterexample away from the high-temperature endpoint. This run removes three of them for every temperature, so the remaining possible five-vertex counterexample set is now at most **68 marked isomorphism types**. Within the specific marked-stabilizer-one obstruction set, the count falls from **22 to 19**.

Those counts are secondary diagnostics and do not replace `n_edge^*` as the task metric.

## 12. Remaining obligation and next route

To move the frozen metric to `n_edge^*>=6`, all remaining five-vertex marked edge additions must be certified for every finite `beta>=0`; alternatively one exact reverse inequality at one finite `beta` would determine `n_edge^*=5` and refute the source edge-addition clause.

The marked-edge interpolation is no longer the only exact route. This run shows that endpoint quotient comparison can succeed even when the interpolation has trivial stabilizer. The next invocation should not repeat any previous method triple. Prospective, **not yet attempted**, methods are:

- **#1 CHANGE THE CATEGORY:** treat the remaining forest/tree endpoint cases as conditional-variance or transfer-operator inequalities rather than graph-automorphism problems;
- **#12 FIND WHAT IS CONSERVED:** exploit component/tensor-sum structure and tree energy variables to identify quantities preserved under the forest edge additions;
- **#19 MAKE IT AN ALGORITHM:** build a proof-oriented endpoint-quotient classifier that groups the remaining 68 types by exact top-factor shape before any heavy resultant calculation, rather than brute-forcing all pairs uniformly.

The unchanged-run count is now **2**. If the next substantive run again leaves the frozen metric unchanged, that will be the third consecutive unchanged run and the following invocation must use the owner-prescribed Section-I thinking-only stuck-recovery protocol.

## 13. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-06
  category: CLOSABLE_OUTSIDE
  source_id: P0195
  claim_id: P0195
  canonical_dedup_key: monotonicity_of_the_ferromagnetic_ising_spectral_gap
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: n_edge^*
  metric_before: "n_edge^* >= 5"
  metric_after: "n_edge^* >= 5"
  metric_movement: none
  methods_actual: [6, 15, 18]
  method_outcomes:
    6: "beta->infinity deformation gives exact target/source gap ratios 2/3, 3/4, 1/2 for three marked-trivial path transitions"
    15: "abandoned symmetry along the marked interpolation and recovered small automorphism quotients separately at the unweighted endpoints"
    18: "x=tanh(beta) converts the endpoint lambda_2 factors to three quadratics and proves A<B<C by elementary exact radical inequalities"
  theorem_id: NM13-06-P0195-N5-PATH-04
  new_exact_scope:
    - "P3 + 2K1 -> P4 + K1, all finite beta>=0"
    - "P4 + K1 -> P5, all finite beta>=0"
    - "P3 + K2 -> P5, all finite beta>=0"
  secondary_case_count_before: 71
  secondary_case_count_after: 68
  marked_trivial_unresolved_before: 22
  marked_trivial_unresolved_after: 19
  checker: proofnet24/NM13-06/artifacts/2026-09-18/p0195_n5_path_trivial_marked.py
  checker_commit: 66ae0f064ea6a7452cf434a9da6eb5b40e90b325
  output: proofnet24/NM13-06/artifacts/2026-09-18/p0195_n5_path_trivial_marked.out
  output_commit: 5415c81f1b8a69f15989ff6bbd4218afede6b29e
  checker_result: ALL_EXACT_CHECKS_PASS
  unchanged_runs_since_metric_movement: 2
  stuck_recoveries_used: 0
  audits:
    P26: NOT_COUNTED
    NM13-07: NOT_COUNTED
  literature_check_date: 2026-09-18
  literature_scope: "LPW exact Question 2; Nacu cycle monotonicity; Shirai fixed-time counterexample; current 2025-2026 edge-monotonicity searches"
  literature_result: "no source-matching resolution recovered in bounded search; publication novelty UNVERIFIED"
  next_methods_prospective_not_tried: [1, 12, 19]
  next_step: "classify remaining five-vertex endpoint quotients by forest/component structure and exact top-factor shape; move n_edge^* to >=6 or find an exact five-vertex counterexample"
```

No shared root, peer namespace, claim file, audit request, email, Drive object, public site, workflow, permission, or schedule was modified in this invocation.
