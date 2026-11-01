Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `W_sigma = 0.08401759857884 -> 0.08401759857884`; C0021 unchanged-run count `0 -> 1`. Methods actually tried: B2, B6, B25.**

# P13 CLOSABLE OUTSIDE — C0021 admission and first counterexample-first research

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Own root: `proofnet24/P13-outside-successor/`.  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`.

## 1. Continuity, exclusions, and lawful successor admission

The controlling owner directive remains `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, together with `operations/NEW_METHODS_2026-09-16.md`. I preserved all mandatory P13 boundaries:

- I0051 / Aldous--Janson Open Problem 9 clade-covariance work remains **RETIRED** and was not reopened;
- P0082 remains at its six-run handoff and was not reopened;
- D0093 remains at its six-run handoff and received no seventh refinement;
- POSTED/INDEX exact-scope exclusions remain exclusions;
- P13 remains entirely outside work.

The owner's mandatory first-screen lead I0054 was rechecked and remains actively owned by R11; P13 did not duplicate or race that claim.

The next source-clean CLOSABLE candidate surfaced by the current intake cursor was **C0021**, Christophe Garban and Jeffrey E. Steif, *Noise Sensitivity of Boolean Functions and Percolation*, Chapter VIII exercise sheet, Exercise VIII.5 in the current book version: determine the exponent `sigma` for the revealment of depth-`k` iterated 3-majority on `n=3^k` leaves. The current author-hosted book still states that the revealments decay like `1/n^sigma` for some `sigma` and that the value of `sigma` is open.

A same-day R7-01 admission screen had independently recovered C0021, but explicitly **rejected it solely because of that worker's shard rule**, stated that no ownership claim could be created from that screen, and observed that `operations/claims/C0021.md` was absent. P13 has no such shard restriction. A fresh direct fetch of `operations/claims/C0021.md` immediately before acquisition returned 404, and the bounded repository search recovered no competing canonical C0021 claim.

P13 therefore acquired the source by the required create-only operation. The canonical claim was created at commit

`81b5300114f5d26af962e9cc1acd69f1feadaa09`

and read back there with blob

`f6b71f7801658cfed434d34d89e6cd25ef1d0a5b`.

This acquisition is an ownership fact only. It does not assert a solution, global openness, or novelty.

## 2. Complete source object and frozen source-faithful metric

Let `f_k` be iterated majority-of-three on the `3^k` leaves of the complete ternary tree of depth `k`, under the source's unbiased product input. For a zero-error randomized algorithm `A` determining `f_k`, let

`delta_A = max_i P(i is queried)`,

and let `delta_{f_k}` be the infimum over such algorithms.

The recovered repository memo proves the exact symmetry reduction

`delta_{f_k} = D_k / 3^k`,

where `D_k` is the minimum expected number of queried leaves under the unbiased product law among deterministic exact decision trees. It also proves submultiplicativity `D_{k+m} <= D_k D_m`, hence

`c := lim_k D_k^(1/k)`

exists and

`sigma = 1 - log(c)/log(3)`.

The supported prior exact values are

`D_1 = 5/2`,

`D_2 = 393/64`,

`D_3 = 15796051/1048576`,

and the explicit depth-4 policy upper bound is

`U_4 = 20871140813662641/562949953421312`.

Together with the O'Donnell--Servedio influence lower bound, these give the rigorous interval

`sigma_L = 1 - log(U_4)/(4 log 3) = 0.17784190856407478...`,

`sigma_U = log(4/3)/log 3 = 0.2618595071429148...`.

I freeze the P13 metric and domain as

`W_sigma := sigma_U - sigma_L`,

for this **single source exponent, the source's unbiased iterated-3-majority domain, and zero-error revealment definition**. Thus

`W_sigma = 0.08401759857884...`, target `0`.

No restricted variant, worst-case query complexity, biased-input analogue, Brownian relaxation, auxiliary lemma, or larger finite computation changes this metric unless it yields a rigorous new endpoint for this exact source `sigma`.

## 3. Dated literature and source-status correction

The original/current source was accessed on 2026-09-18. The author-hosted current book PDF text layer contains the exact Exercise VIII.5 wording above. A screenshot request to that PDF failed with a cache miss; the same exercise was independently recovered from the Clay Mathematics Proceedings version, whose text layer also states the open exponent question. A screenshot request to the Clay PDF likewise returned a cache miss. These are recorded access failures, not evidence about mathematical status.

The closest later computational paper found is Julia Jansson and Patrik Jansson, *Level-p-complexity of Boolean functions using thinning, memoization, and polynomials*, J. Functional Programming 33 (2023), e13. It computes the level-`p` complexity of **two-level** iterated majority; at `p=1/2` its value agrees with `D_2=393/64`. It does not determine the asymptotic exponent.

A material prior-art correction was found in Saul Jacka, Jon Warren and Peter Windridge, *Minimizing the time to a decision*, Ann. Appl. Probab. 21 (2011), 1795--1826 (working-paper PDF dated 2010). Their Section 6.2 studies the same discrete recursive-majority expected optimal cost `r_n` (our `D_n`) and `gamma = lim r_n^(1/n)`. They record the published lower bound `9/4`, numerics near `2.45`, and an upper bound `2.472`; a footnote says that Oded Schramm and Mark Braverman communicated a lower-bound improvement to `2.28` but **did not publish details**. The unpublished communication is therefore not a usable theorem for P13's frozen metric. Their paper also introduces a Brownian-tree relaxation as a possible route to a lower bound on `gamma`.

The same paper proves, for three independent diffusions, that the optimal continuous allocation strategy is to run the component whose current value is the middle order statistic. That continuous theorem is the starting point of B6 below. The page containing Section 6.2 and the unpublished-2.28 footnote was successfully inspected as an image in this run.

Dated bounded search queries included variants of:

- `"iterated 3-majority" revealment exponent Garban Steif`;
- `"recursive majority" revealment decision tree exponent 3-majority`;
- `"Level-p-complexity" iterated majority Jansson Jansson`;
- `"Minimising the time to a decision" recursive majority Jacka Warren Windridge`;
- `"2.28" recursive majority Braverman Schramm`;
- recent `Jeffrey Steif recursive majority revealment` and `Christophe Garban recursive majority revealment` queries through 2026.

The recent author searches surfaced unrelated 2026 work but no source-matching determination of `sigma`. The worst-case recursive-majority query-complexity literature (Jayram--Kumar--Sivakumar, Magniez et al., Leonardos and successors) concerns a different objective/distribution and cannot be substituted for the source's uniform expected-cost exponent. No checked primary source in this bounded search states the exact value of the C0021 exponent. This is negative bounded evidence only; it is **not** a worldwide-openness or novelty certificate.

C0021 is admitted as CLOSABLE because its source object is self-similar, finite-state at every depth, already has an exact submultiplicative reduction, and admits a credible short recurrence/duality route. That classification is operational and may still rotate after six unchanged runs; it is not a promise that the problem is easy.

## 4. B6 — deform the solved Brownian allocation rule to the discrete tree

### Idea before computation

Jacka--Warren--Windridge prove that, for three continuous diffusions, the optimal controller always runs the diffusion whose current value lies between the other two. A natural discrete deformation is therefore:

> At every unresolved majority node, attach to each child its posterior probability `q` of eventually evaluating to `+` under the still-unrevealed unbiased leaves. Query recursively inside the child whose posterior is the median of the three child posteriors; repeat this rule down the tree.

Call this the **recursive median-posterior policy**. If it were optimal at every depth, it would collapse the source problem to a one-dimensional recursive cost calculation and plausibly determine `c`.

The deformation is source-faithful: it queries actual leaves, uses no lookahead outside the current information state, and computes the same exact Boolean function.

### Outcome

It **fails**. B6 produced a concrete candidate rule, and B2 below attacks it exactly. The failure occurs already at depth 3, so a direct discrete transfer of the continuous `run-the-middle` theorem cannot solve C0021.

This is useful negative movement in the method space but does not alter `W_sigma`.

## 5. B2 — attack the negation first: exact depth-3 counterexample to recursive median-posterior optimality

I wrote the counterexample before coding it and then executed an exact rational Bellman checker.

### Proposition P13-C0021-MEDIAN-FAIL-01

The recursive median-posterior policy is not optimal for depth-3 iterated 3-majority under the unbiased product law.

### Proof

Represent an unqueried leaf by `u` and a determined subtree by `+` or `-`. For every partial subtree state `s`, let `q(s)` be the exact conditional probability that the subtree value is `+`; because unrevealed leaves are still independent fair bits, `q(s)` is an exact rational number. Let `V(s)` be the exact minimum expected number of additional leaf queries needed to determine the subtree from `s`.

The Bellman recurrence is

`V(s)=0` when `s` is determined,

and otherwise

`V(s) = 1 + min_e (V(s_e^+) + V(s_e^-))/2`,

where `e` ranges over all currently unqueried leaves and `s_e^+`, `s_e^-` are the two successor states. This recurrence is exact because every deterministic exact decision tree chooses one unqueried leaf next, and randomization cannot improve the expectation under a fixed input distribution.

Start from the full depth-3 tree and follow the recursive median-posterior rule for three successive `+` query outcomes. The resulting three depth-2 root-child posteriors are exactly

`3/4, 5/8, 1/2`.

The median-posterior rule therefore selects the child of posterior `5/8`, and inside it selects an untouched grandchild; in the checker's canonical 0-indexed path notation its next leaf is

`(1,1,0)`.

Exhausting all legal next leaf queries from this same information state and then using the exact Bellman value for each continuation gives

`Q_median = 3031947/262144`,

whereas querying a leaf inside the already biased grandchild, at path `(1,0,1)` or `(1,0,2)`, gives

`Q_opt = 3028131/262144`.

Thus

`Q_median - Q_opt = 477/32768 > 0`.

The median-posterior action is strictly suboptimal at a reachable depth-3 state, proving the proposition. ∎

### Exact finite self-check

The checker independently recomputes the full Bellman DP values

`D_1=5/2`, `D_2=393/64`, `D_3=15796051/1048576`,

reconstructs the `+++` witness, exhausts every next-leaf choice at the witness state, and verifies the strict rational gap above. Its executed output ends `ALL_EXACT_CHECKS_PASS`.

Artifacts:

- `proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_median_counterexample_check.py`, creation commit `2e75ad44dab02cf59e25a0d098c023075c1f29d4`;
- `proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_median_counterexample_check.out`, creation commit `a186485e6b386941124175642e4269fb7f2506a7`.

Both were read back at their returned commits. This is a **self-check**, not an independent audit.

B2 outcome: **the strongest natural Brownian-to-discrete candidate is exactly refuted; no counterexample to the source exponent's existence or to the prior interval was found.**

## 6. B25 — count the same queries two ways: a residual-completion lower-bound decomposition

The Brownian deformation fails because a discrete child cannot be summarized by its scalar posterior: two states with the same posterior can have different future query costs. B25 therefore keeps the full child state but double-counts how much local work a global root algorithm has purchased.

### Lemma P13-C0021-RESIDUAL-COMPLETION-02

Let `f_h` be depth-`h` recursive majority, and let `D_h` be its optimal uniform expected exact decision-tree cost. Consider any randomized exact algorithm `A` computing `f_{h+1}` from its three independent depth-`h` child subtrees. For child `i`, let

- `N_i` be the number of leaf queries made by `A` inside child `i`;
- `S_i` be the local information state left in child `i` when `A` stops;
- `V_h(S_i)` be the optimal expected number of additional child-local queries needed to determine that child from `S_i`.

Then

`D_h <= E[N_i + V_h(S_i)]` for each `i`,

and hence

`E T_A >= 3 D_h - E[sum_i V_h(S_i)]`.

At the stopping time of an exact majority algorithm at least two child values are individually determined and agree. Therefore at most one child is undetermined; defining `J` to be that possible leftover child and putting `V_h(S_J)=0` if all three are determined,

`E T_A >= 3 D_h - E[V_h(S_J)]`.            (RC)

### Proof

Fix a child index `i`. Construct a randomized exact algorithm `B_i` for one fresh depth-`h` target subtree. Internally sample two independent fair depth-`h` subtrees at no query cost and simulate `A` on the triple consisting of the target plus those two simulated subtrees. Whenever `A` queries a target leaf, `B_i` makes the same query and pays one; queries to the two simulated subtrees are answered from `B_i`'s private randomness and cost nothing. When `A` stops, the target may or may not yet be determined. From its resulting local state `S_i`, finish the target by an optimal local decision tree of expected additional cost `V_h(S_i)`.

This always determines the target exactly. Its expected target-query cost is `E[N_i+V_h(S_i)]`. Randomization cannot beat the deterministic distributional optimum `D_h` under the fixed unbiased product law, so

`D_h <= E[N_i+V_h(S_i)]`.

Summing over `i=1,2,3` and using `T_A=N_1+N_2+N_3` gives the first displayed global inequality.

It remains to justify the one-leftover statement. If fewer than two child values were individually determined and agreeing when `A` stopped, then because the three child subtrees use disjoint leaves, every locally undetermined child state has at least one completion to `+` and at least one completion to `-`, independently of the others. One can therefore construct two completions of the unqueried leaves giving opposite root majorities, contradicting exact termination. Thus two agreeing children are determined, their `V_h` values are zero, and at most one residual term remains. This proves (RC). ∎

### Why this is the right missing quantity

For an optimal depth-`h+1` algorithm, a bound

`E[V_h(S_J)] <= rho D_h`

would imply

`D_{h+1} >= (3-rho) D_h`.

Therefore:

- `rho < 3/4` would strictly beat the classical recurrence-scale constant `9/4` and immediately move the rigorous source interval;
- a bound near `rho ≈ 0.55` would place the resulting growth constant near the observed `2.45` scale.

This formulation exposes exactly what scalar-posterior approaches throw away: the **completion value of the one child that root majority did not need to finish**.

### Exact small-depth self-check of the residual quantity

A second exact rational checker computes, among **all Bellman-cost-optimal deterministic root policies**, the minimum and maximum expected residual completion value. For `h=0,1,2` the range collapses to a single value in every case:

- `h=0`: residual `1/2`, ratio to `D_0` = `1/2`;
- `h=1`: residual `87/64`, ratio to `D_1` = `87/160 = 0.54375`;
- `h=2`: residual `3539117/1048576`, ratio to `D_2` = `3539117/6438912 = 0.5496451885...`.

For `h=0,1`, (RC) is exact. At `h=2`, the resulting accounting lower bound is

`15777619/1048576`,

while

`D_3 = 15796051/1048576`,

so the inequality has only the exact slack `9/512`. These small cases are evidence for a stable residual coefficient around `0.55`, not a proof of any uniform bound.

Artifacts:

- `proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_residual_completion_check.py`, creation commit `7527245a503d3d12418a7979c59802671667a5b7`;
- `proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_residual_completion_check.out`, creation commit `6137790ddb05cc683940dd632b035836bf45070f`.

The output ends `ALL_EXACT_CHECKS_PASS`; both files were read back at their returned commits. Again this is a **self-check**, not an outside audit.

B25 outcome: **a rigorous lower-bound decomposition succeeds and isolates one scalar residual obligation; no uniform `rho<3/4` theorem is yet proved, so the frozen source metric does not move.**

## 7. What worked, what failed, and exact next obstruction

The three methods are genuinely distinct:

- **B6 (deform):** transferred the continuous `run-the-middle` structural idea to a discrete posterior policy. The deformation is natural and source-faithful, but not optimal.
- **B2 (attack negation):** searched for and found an exact reachable depth-3 obstruction to that policy, with a strict rational Bellman gap `477/32768`.
- **B25 (double count):** abandoned scalar posterior as the state variable and instead counted local queries plus residual completion value, yielding the full lemma (RC) and a single missing coefficient.

The run therefore produced real mathematical progress in understanding the source but **no source-metric movement**. In particular, neither a failed candidate policy nor an auxiliary lower-bound identity narrows the certified interval for `sigma`.

The exact blocking formula is now

`D_{h+1} >= 3D_h - E[V_h(S_J)]`.

The missing ingredient is a source-uniform upper bound

`E[V_h(S_J)] <= rho D_h`

with some explicit `rho < 3/4`, for an optimal or suitably symmetrized optimal algorithm at every depth `h`. The simplest unproved case is not another finite depth; `h<=2` is now exact. It is a **structural inequality valid for arbitrary h** controlling the value left in the unneeded child.

The nearest solved analogues are:

1. the O'Donnell--Servedio influence lower bound, which supplies the current `9/4` growth-scale lower endpoint but does not see the leftover child's internal state;
2. Jacka--Warren--Windridge's continuous run-the-middle theorem, which fully solves the one-level diffusion allocation problem but whose naive recursive discrete deformation is now refuted;
3. the finite Bellman dynamic program for `D_1,D_2,D_3`, which supplies exact local data but scales too quickly to determine the asymptotic exponent directly.

This is only unchanged run 1 for C0021, so the Section-I three-run recovery trigger does not yet apply.

## 8. Next research triple

The next P13 C0021 run should not repeat B2/B6/B25. The recorded triple is:

- **B11 — dualize:** seek a potential/dual certificate whose drift under every leaf query lower-bounds the lost completion value and converts (RC) into a uniform residual bound;
- **B12 — conserved quantity:** track posterior martingales together with `V_h(S)` and identify a conserved or supermartingale quantity at the root stopping time;
- **B24 — extremal object:** characterize which local subtree states maximize `V_h(S)` at a given posterior or certificate status; prove that the leftover child cannot concentrate on those extremizers under an optimal global policy.

The immediate target is not `sigma` numerically. It is the first rigorous constant `rho<3/4` in the exact residual-completion inequality. Any such constant would create genuine movement in the frozen source interval.

## 9. Directed audit duty and closure status

P13's secondary directed-audit duty remains P14. No new P14 source-closing theorem requiring a repeat P13 end-to-end audit was recovered in this run; prior completed P13-to-P14 audits remain preserved.

C0021 status after this run is **CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL / NO SOURCE-METRIC MOVEMENT**. Closure is not remotely claimed. It would require an exact determination of the source exponent (or an exact source-equivalent result), current prior-art reconciliation, and the owner-required two independent OTHER-track end-to-end audits including P26 and one distinct research track.

No shared root ledger, historical report, peer file, workflow, public surface, email/Gmail item, Drive item, paid-compute resource, credential, permission, or schedule was modified.

## 10. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: P13
  native_id: "6aa7b253b37c8191b693d8dc79298d37"
  lane: CLOSABLE_OUTSIDE
  state: ACTIVE_CLAIM_PARTIAL
  canonical_id: C0021
  source: "Garban-Steif, Noise Sensitivity of Boolean Functions and Percolation, Chapter VIII Exercise VIII.5"
  claim:
    path: operations/claims/C0021.md
    creation_commit: 81b5300114f5d26af962e9cc1acd69f1feadaa09
    readback_blob: f6b71f7801658cfed434d34d89e6cd25ef1d0a5b
  source_status: CURRENT_OPEN_LOOKING_BOUNDED_SEARCH_ONLY
  metric:
    name: W_sigma
    exact_definition: "log(4/3)/log(3) - (1 - log(U_4)/(4 log(3)))"
    U_4: "20871140813662641/562949953421312"
    before: 0.08401759857884
    after: 0.08401759857884
    target: 0
  mathematical_progress: false
  substantive_auxiliary_progress: true
  unchanged_runs: 1
  recoveries_used: 0
  methods_this_run: [2, 6, 25]
  method_results:
    B2: "Exact depth-3 reachable counterexample to recursive median-posterior optimality; Bellman gap 477/32768"
    B6: "Brownian run-the-middle deformation formulated source-faithfully, then refuted at depth 3"
    B25: "Residual-completion lemma D_(h+1) >= 3 D_h - E[V_h(S_J)] proved; exact h<=2 residual self-checks"
  artifacts:
    median_checker_commit: 2e75ad44dab02cf59e25a0d098c023075c1f29d4
    median_output_commit: a186485e6b386941124175642e4269fb7f2506a7
    residual_checker_commit: 7527245a503d3d12418a7979c59802671667a5b7
    residual_output_commit: 6137790ddb05cc683940dd632b035836bf45070f
  prior_art_delta:
    - "Jacka-Warren-Windridge 2011 studies the same uniform expected-cost growth constant; 9/4 published lower bound, 2.472 then-known upper bound, unpublished communication of 2.28"
    - "Jansson-Jansson 2023 computes only two-level level-p complexity; p=1/2 agrees with D_2=393/64"
  exact_blocker: "Prove E[V_h(S_J)] <= rho D_h uniformly with an explicit rho < 3/4"
  next_methods: [11, 12, 24]
  next_step: "Dualize the residual-completion inequality and seek a stopping-time potential controlling the leftover child's completion value; characterize extremal local states before more brute-force depth growth."
  preserved_retirements:
    I0051: RETIRED_DO_NOT_REOPEN
    P0082: SIX_RUN_HANDOFF_PRESERVED
    D0093: SIX_RUN_HANDOFF_PRESERVED
  first_screen_lead:
    I0054: OWNED_ACTIVE_R11_SKIP
  p14_directed_audit: "NO_NEW_SOURCE_CLOSING_P14_THEOREM_RECOVERED; PRIOR_AUDITS_PRESERVED"
  closure_claimed: false
```
