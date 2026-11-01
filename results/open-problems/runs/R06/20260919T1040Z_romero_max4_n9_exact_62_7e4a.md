Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO FIXED-METRIC MOVEMENT: `ROMERO-2025-SPLIT8` has `R_SPLIT8: 0 -> 0`; closure audit gate for the claimed n=8 layer remains `1/2 -> 1/2`; frozen I0056/H_{5,5} width remains `0 -> 0`; methods #14 FIND THE GROUP ACTING, #27 SWAP THE QUANTIFIERS, #30 DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME.**

# R06 — Romero split reliability: exact first source-new max-minus-four case T_{9,32}

Run date: 2026-09-19.
Repository / branch: private `yspennstate/math-open-problems` / `master`.
Lane: **CLOSABLE OUTSIDE**.
Active canonical successor claim: `operations/claims/ROMERO-2025-SPLIT8.md`.

## 1. Continuity, required reread, and frozen metrics

I continued from the newest own immutable report

`runs/R06/20260919T0830Z_romero_max3_all_n_bridge_61_f6c2.md`,

whose creation commit is recorded by the independent P26 audit as

`0f57e67510e34395009a5908c44f58340ea204a3`.

Before new mathematics I reread/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- canonical `operations/claims/I0056.md` and active successor `operations/claims/ROMERO-2025-SPLIT8.md`;
- the newest R06 report;
- the newest neighboring P26 audit/stuck reports for the Romero packages;
- the I0056 intake history surfaced from `probability_1000_intake_I_20260914/problems.jsonl` and its canonical claim.

The original R06 source remains Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The current online edition itself records Haslegrave--Panagiotis as solving the codegree-3 and codegree-4 regular cases. Those triangular/quadrangular cases remain prior art and are not relabelled as R06 work.

The frozen predecessor remains

`Phi_V(H_{5,5}) = sqrt(5)`, interval `[sqrt(5),sqrt(5)]`, width `0`,

under the original outer-vertex-boundary normalization. The full Lyons--Peres Question 6.20 remains **PARTIAL**.

The active finite successor `ROMERO-2025-SPLIT8` is already mathematically candidate-complete at

`R_SPLIT8 = 0`,

but fleet closure is still blocked by the missing second genuinely distinct OTHER-task full-proof audit. The one qualifying audit remains

`P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64 = PASS_FULL_MATHEMATICAL_PROOF`.

Repository-wide search still found no distinct non-R06/non-P26 second full-proof audit of the exact `n=8,m=14,...,26` package. The fixed metric therefore remains `0 -> 0` and the closure gate remains `1/2 -> 1/2`.

The newest P26 mathematical diagnosis is directly relevant: its Section-I thinking run isolates the next unresolved diagonal `m=C(n,2)-4` as a distinguished-edge reliability-derivative problem and identifies `n=9,m=32` as the first source-new finite scale after R06's complete n=8 layer and all-n max-minus-two/max-minus-three theorems.

## 2. Fresh source, current-status, and prior-art check

Primary source rechecked 2026-09-19:

Pablo Romero, *Characterization of locally most split reliable graphs*, Theoretical Computer Science 1047 (2025), 115327, DOI `10.1016/j.tcs.2025.115327`, arXiv `2503.15453`.

The current source still states the Brown--McMullin remaining simple-graph cases as open and proves nonexistence only for

`n >= 7,  n <= m <= C(n-3,2)+3`.

Thus `T_{9,32}`, where `32=C(9,2)-4`, remains inside the source-open region. Fresh bounded searches used exact title/arXiv/author/follow-up queries and the phrases

- `uniformly most split reliable K_9 32`;
- `split reliability 9 32 Romero`;
- `split reliability binom(n,2)-4`;
- `max-minus-four split reliability`.

They recovered Romero 2025 and adjacent ordinary/two-terminal reliability literature, but no later primary source resolving the exact `T_{9,32}` split-reliability class or the full max-minus-four simple-graph diagonal. This is bounded negative evidence only; publication priority remains **UNVERIFIED**.

The nearest classical machinery remains all-terminal reliability transformation/extremal theory. It is prior art, not a new R06 claim. P26 correctly notes that ordinary compression controls total reliability but not automatically the distinguished-edge marginal needed for an all-n max-minus-four proof.

A repository search for `T_{9,32} split reliable` returned no existing R06/other proof package. The only max-minus-four repository hit was P26's new diagnostic report, which explicitly made **no theorem claim** and selected the first source-new finite scale as the next laboratory. Thus this run does not duplicate a claimed theorem.

## 3. Idea before code

The all-n max-minus-four obstruction is harder than the two preceding diagonals, but its **combinatorial type space is already finite and stable**.

Let `M=C(n,2)` and consider `G in T_{n,M-4}` with terminals `s,t`.

The terminal-edge swap lemma from the preceding R06 work is elementary and I reprove it here because it is needed for the finite theorem. If `st` is present and `e` is a missing edge, set

`G' = G-st+e`.

Condition on every common edge. A successful split state of `G` necessarily has `st` failed, and the common edges already form exactly two components separating `s,t`. In `G'`, failure of `e` preserves that same split, while operation of `e` can only add additional successful states when `e` lies inside one of the two components. Hence

`SR_{G'}(p) >= SR_G(p)` for every `p in [0,1]`.

Deleting four edges from `K_9` cannot disconnect it, so the swap remains inside `T_{9,32}`. Therefore it suffices to consider missing sets

`F = {st} union D`,

where `D` consists of exactly three edges not equal to `st`.

This is where the new methods enter.

## 4. Method #14 — FIND THE GROUP ACTING: 21 stable terminal types

A three-edge set `D` involves at most six nonterminal endpoints. Therefore for **every n>=8**, every terminal-isomorphism type can be represented using only the two terminals plus six nonterminals. The type universe stabilizes already on eight labeled vertices.

Quotient the 3-edge subsets of `K_8-{st}` by

`S_6 x C_2`,

where `S_6` permutes the six nonterminals and `C_2` swaps the terminals. Exact exhaustive canonicalization of all

`C(27,3)=2925`

labeled defect sets gives exactly

`21`

terminal-isomorphism types.

Grouped by the abstract shape of `D`, these are

- 3-star `S_3`: 4 terminal types;
- path `P_4`: 5;
- `P_3 union K_2`: 7;
- triangle `K_3`: 2;
- matching `3K_2`: 3.

Thus the max-minus-four diagonal is not an ever-growing graph-classification problem. Its parent defect space is a fixed 21-state family for all `n>=8`. What grows with `n` is only the reliability polynomial attached to each stable type.

This is a genuine structural reduction beyond simply enumerating n=9.

## 5. Method #27 — SWAP THE QUANTIFIERS: prove coefficientwise domination

For a fixed `m`-edge two-terminal graph `X`, let

`N_j(X)`

be the number of spanning `j`-edge subgraphs having exactly two connected components, one containing each terminal. Then

`SR_X(p) = sum_j N_j(X) p^j (1-p)^{m-j}`.

Instead of checking the continuum of `p`, I prove the stronger finite statement

`N_j(A) >= N_j(X) for every j`

for a single candidate `A` and every terminal type `X`. Since every basis function `p^j(1-p)^{m-j}` is nonnegative on `[0,1]`, coefficientwise domination implies uniform split-reliability domination immediately.

The candidate is

`A = K_9 - {st,su,sv,sw}`,

a four-edge star defect centered at one terminal.

## 6. Exact coefficient recurrence

The checker does not enumerate the `2^32` operational states. It computes the exact split coefficient vector by a connected-spanning-subgraph recurrence.

For each nonempty vertex set `A`, let

`C_A(z) = sum_F z^{|F|}`,

where the sum is over connected spanning subgraphs `F` of the induced graph `G[A]`. Fix a root `r in A`. The component of `r` in an arbitrary spanning subgraph is unique, so

`C_A(z) = (1+z)^{e(A)} - sum_{B proper subset A, r in B} C_B(z)(1+z)^{e(A\B)}`.       (1)

Once all `C_A` are known, the split polynomial is

`F_G(z) = sum_{A: s in A, t notin A} C_A(z) C_{V\A}(z)`

and

`[z^j]F_G(z) = N_j(G)`.                              (2)

Equations (1)-(2) use integer addition, subtraction and binomial coefficients only.

## 7. Method #30 — one scale completely: T_{9,32}

The exact checker

`artifacts/R06/20260919T1040Z_romero_max4_n9_exact_62_7e4a.py`

was executed locally with Python integer arithmetic and its output archived as

`artifacts/R06/20260919T1040Z_romero_max4_n9_exact_62_7e4a.out`.

It independently performs all of the following:

1. generates all `2925` labeled three-edge defect sets on the stable 8-vertex core;
2. canonicalizes them under `S_6 x C_2` and asserts exactly `21` classes;
3. verifies the `4,5,7,2,3` abstract-shape type counts above;
4. lifts each representative to `n=9`;
5. computes its complete exact split coefficient vector by (1)-(2);
6. compares every coefficient against the terminal-centered four-star candidate.

The result is

`types_checked=21`,

`coefficientwise_violations=0`,

`exact_ties=1`.

The only full coefficient-vector tie inside the terminal-missing quotient is the candidate's own terminal-isomorphism type. The smallest positive coefficient gap among noncandidate types is still an exact integer gap of `1` (at operational-edge count `j=28`), so no floating-point separation is involved.

### Theorem

In the simple connected two-terminal class

`T_{9,32}`,

the graph

`A = K_9 - {st,su,sv,sw}`

with distinct nonterminals `u,v,w` is uniformly most split reliable:

`SR_A(p) >= SR_G(p)`

for every `G in T_{9,32}` and every `p in [0,1]`.

### Proof

Apply the terminal-edge swap lemma to reduce any `G` to one with `st` missing without decreasing split reliability. Its other three missing edges fall into one of the 21 terminal-isomorphism classes proved exhaustive in Section 4. The exact recurrence (1)-(2), evaluated for every class, gives coefficientwise domination by `A`. Therefore

`SR_A(p)-SR_G(p) = sum_j (N_j(A)-N_j(G)) p^j(1-p)^{32-j} >= 0`

for all `p in [0,1]`. `square`

This is a **PROVED finite source case with an executed exact finite core**, subject to the fleet's separate novelty and independent-audit requirements. It is not a claim that the all-n max-minus-four diagonal is solved.

## 8. What this teaches about the all-n obstruction

The stable 21-type reduction is stronger than the single n=9 theorem. For every `n>=8`, the all-n max-minus-four problem reduces to those same 21 parent defect types.

Write `R(H;p)` for all-terminal reliability and

`Delta_st R(H;p)=R(H;p)-R(H-st;p)`.

For the terminal-centered 3-star parent defect `D_*={su,sv,sw}`, an all-n proof would follow from

`Delta_st R(K_n-D;p) <= Delta_st R(K_n-D_*;p)`          (3)

for each of the 21 stable defect types `D` and all `0<p<1`.

The exact n=9 coefficientwise theorem proves (3) at the first source-new finite scale, but does not prove (3) symbolically in `n`. P26's diagnosis is therefore confirmed rather than bypassed: the missing all-n ingredient is a derivative-level compression/majorization theorem or an exact positive-cone decomposition for the 20 noncandidate stable types.

The next useful attacks, if the active metric/audit state does not change, are #13 FIND WHAT ONLY INCREASES (seek monotonicity of `Delta_st R` under terminal-preserving compression), #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE (identify the 21 marginal gaps in reliability-importance literature), and #22 READ THE FAILURES (classify precisely which compressions fail to preserve the distinguished-edge derivative).

## 9. Honest status, audit gate, and stagnation rule

Fixed claimed metric:

`R_SPLIT8: 0 -> 0`.

The claimed n=8 layer remains mathematically candidate-complete but not fleet-closed:

- P26 full-proof audit: PASS;
- second genuinely distinct OTHER-task full-proof audit: MISSING.

Auxiliary source progress in this run:

`T_{9,32}: OPEN -> PROVED finite case in this package`,

with exact checker/output but **0/2 independent audits specifically for this new n=9 theorem**. The unrestricted Romero/Brown--McMullin source remains **PARTIAL / OPEN**.

Supported fixed-metric unchanged count is now `2 -> 3` (the three no-movement R06 runs after the `7 -> 0` completion run are the max-minus-two, max-minus-three, and this n=9 max-minus-four run). Therefore Section I applies to the **next** R06 run if no fixed-metric or closure-state event intervenes: it must be a thinking/stuck run, not another ordinary auxiliary-lemma/checker run.

The frozen I0056 predecessor remains `0 -> 0`; it is not reopened.

## 10. Model / scheduler truth

The requested model line remains a prompt request, not a scheduler control. The actual model in this run is GPT-5.6 Sol and the reasoning level is UNVERIFIED. The exposed task-control interface offers title/prompt, schedule/timing, and enabled-state controls, but no binding model-family selector, reasoning-effort selector, authenticated applied-model/reasoning receipt, or guaranteed hour-long execution setting. Thus GPT-6/maximum cannot be honestly asserted from this surface.

The historical P26 `You cannot modify this task` response was an authorization-context boundary, not a mathematical issue and not proof that P26 is permanently immutable. Repository deployment records show later successful P26 modification from a different authorized context while another context still recorded denial. The lawful workaround is to use the owning/authorized product/workspace/backend context that has modification authority; there is no worker-side permission bypass. Per the current owner addendum, this R06 run attempted no scheduler or permission change.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  original_source: "Lyons-Peres, Probability on Trees and Networks, Question 6.20 / intake I0056"
  frozen_original_target: "H_{5,5}, degree 5, face-degree 5, outer vertex boundary"
  frozen_original_metric_before: 0
  frozen_original_metric_after: 0
  frozen_original_interval: "[sqrt(5),sqrt(5)]"
  original_status: PARTIAL_FULL_SOURCE
  active_claim: ROMERO-2025-SPLIT8
  active_source: "Pablo Romero, Characterization of locally most split reliable graphs, TCS 1047 (2025), 115327"
  fixed_metric: R_SPLIT8
  metric_before: 0
  metric_after: 0
  fixed_metric_unchanged_count_before: 2
  fixed_metric_unchanged_count_after: 3
  claimed_layer_status: CANDIDATE_COMPLETE_AUDITS_PENDING
  closure_audit_gate_before: "1/2"
  closure_audit_gate_after: "1/2"
  tried_moves: [14, 27, 30]
  new_auxiliary_result: "T_{9,32}: K_9-{st,su,sv,sw} is uniformly most split reliable"
  auxiliary_status: PROVED_FINITE_EXACT_CORE__SOURCE_PARTIAL_OPEN__PRIORITY_UNVERIFIED__AUDITS_0_OF_2
  stable_max_minus_four_terminal_types: 21
  exact_types_checked_n9: 21
  coefficientwise_violations: 0
  remaining_obligation: "For active claim closure: one second genuinely distinct OTHER-task full-proof audit of the exact n=8 layer. For the unrestricted source: many cases remain open; the next-diagonal all-n obstruction is terminal-edge derivative monotonicity across the 21 stable 3-defect types."
  audit_ids:
    - "P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64_PASS_FULL_MATHEMATICAL_PROOF"
    - "SECOND_DISTINCT_N8_AUDIT_MISSING"
    - "P26-AUDIT-R06-ROMERO-MAX3-ALLN-66_PASS_FULL_MATHEMATICAL_PROOF"
  evidence:
    - "runs/R06/20260919T0830Z_romero_max3_all_n_bridge_61_f6c2.md"
    - "proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_12-59-00__run-report.md"
    - "artifacts/R06/20260919T1040Z_romero_max4_n9_exact_62_7e4a.py"
    - "artifacts/R06/20260919T1040Z_romero_max4_n9_exact_62_7e4a.out"
```
