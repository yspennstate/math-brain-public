Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. STUCK1 / NO FIXED-METRIC MOVEMENT: `ROMERO-2025-SPLIT8` has `R_SPLIT8: 0 -> 0`; its closure audit gate remains `1/2 -> 1/2`; frozen I0056/H_{5,5} width remains `0 -> 0`; methods #13 FIND WHAT ONLY INCREASES, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES.**

# R06 — mandatory Section-I thinking run: the missing marked-edge reliability monotonicity

Run date: 2026-09-19.
Repository / branch: private `yspennstate/math-open-problems` / `master`.
Lane: **CLOSABLE OUTSIDE**.
Active canonical successor claim: `operations/claims/ROMERO-2025-SPLIT8.md`.

This is a thinking/stuck run. The fixed metric had remained unchanged for three consecutive R06 runs after reaching zero, so under the controlling Section-I rule I make **no new theorem claim**, create **no new finite checker**, and do not manufacture another audit receipt. The purpose of this report is to isolate the exact obstruction, record what the previous routes do and do not supply, choose one recovery route, and preserve the repository/literature delta.

## 1. Required continuity and repository read

I continued from

`runs/R06/20260919T1040Z_romero_max4_n9_exact_62_7e4a.md`,

whose actual GitHub creation commit is

`ff9cd93f4e5e008d04cfb85d2a5d485352954653`

and whose report blob is `480f89224a3a5c99f65a8920161d86ff1df3fba1`.

Before the thinking analysis I reread/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- `operations/claims/I0056.md` and `operations/claims/ROMERO-2025-SPLIT8.md`;
- the current I0056 intake row in `probability_1000_intake_I_20260914/problems.jsonl`;
- the newest R06 report;
- the newest neighboring P26 report and its exact audit artifacts for the Romero line;
- the exact post-R06 repository delta.

The intake row still records the exact original source question as Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The current online Lyons--Peres edition still prints that question and annotates the codegree-3 and codegree-4 cases with Haslegrave--Panagiotis. Fresh source checking also confirms that Haslegrave--Panagiotis, *Random Structures & Algorithms* 58 (2021), 150--163, DOI `10.1002/rsa.20946`, establish the vertex-isoperimetric constant for all triangular and square hyperbolic lattices and explicitly describe those cases as answering the Lyons--Peres question. Those cases remain prior art.

The frozen R06 predecessor remains

`Phi_V(H_{5,5}) = sqrt(5)`, interval `[sqrt(5),sqrt(5)]`, width `0`,

for the outer-vertex-boundary normalization `|partial_V K|/|K|`. The full Question 6.20 remains **PARTIAL**. Root `POSTED.md` now also records the corresponding outer-vertex-isoperimetry manuscript as already present on ResearchGate, so this predecessor is not reopened or repackaged here.

The active finite successor is still `ROMERO-2025-SPLIT8`. Its fixed metric is

`R_SPLIT8 :=` number of classes `T_{8,m}`, `14 <= m <= 26`, whose uniformly-most-split-reliable existence status is not yet settled by a source-valid exact proof.

It remains

`R_SPLIT8 = 0`.

The unrestricted Romero/Brown--McMullin source problem remains **PARTIAL / OPEN**.

## 2. New repository event since the previous R06 report

The exact compare from the actual preceding R06 creation commit

`ff9cd93f4e5e008d04cfb85d2a5d485352954653`

to the observed current head

`c379ac52890c1439fdff6ffedd7133be0983478b`

is complete (`too_large = null`) and reports **48 commits ahead, 0 behind**.

The material neighboring event is a new P26 audit:

`P26-AUDIT-R06-ROMERO-MAX4-N9-67 = PASS_FULL_FINITE_PROOF / CLAIM_SCOPED_T9_32 / EXACT_FINITE_CORE_INDEPENDENT_PASS / STRONGER_GLOBAL_COEFFICIENTWISE_SWAP_PASS / SOURCE_PARTIAL_OPEN / PRIOR_ART_EXACT_SPECIALIZATION_UNVERIFIED / PENDING_SECOND_DISTINCT_AUDIT`.

P26 independently classified the 21 terminal-marked three-defect types without using R06's group canonicalizer, independently recomputed the exact split coefficients, and strengthened the terminal-edge swap to a coefficientwise injection. This materially increases confidence in the auxiliary `T_{9,32}` theorem.

It does **not** move the active R06 closure gate. The same P26 report explicitly preserves

`P26-RECONCILE-R06-ROMERO-SPLIT8-N8-2OF2-64 = PENDING_SECOND_DISTINCT_AUDIT`.

Repository-wide searches still show no genuinely distinct non-R06/non-P26 full-proof audit of the exact `n=8, m=14,...,26` package. Thus the active audit gate stays `1/2`.

### Provenance correction, no mathematical downgrade

The newest P26 report cites the owner `T_{9,32}` creation commit as

`ff9cd1274af70c41329226139b05cd6eba11beba`.

That SHA is not resolvable in this repository. The actual R06 creation commit is

`ff9cd93f4e5e008d04cfb85d2a5d485352954653`.

The audited path, report blob `480f89224a3a5c99f65a8920161d86ff1df3fba1`, owner checker blob, and owner output blob match the intended package, so this is a **provenance-SHA typo**, not a mathematical audit failure. I record it here rather than editing P26's immutable report.

## 3. Fresh source/current-literature screen, dated 2026-09-19

Primary/source queries checked this run included:

- `Lyons Peres Probability on Trees and Networks Question 6.20 Phi_V regular co-regular plane graphs`;
- exact `Question 6.20` wording and current online-book annotations;
- `Haslegrave Panagiotis 10.1002/rsa.20946 vertex isoperimetric`;
- `Pablo Romero Characterization of locally most split reliable graphs 2503.15453`;
- `uniformly most split reliable max-minus-four` and `T_{9,32}`-style follow-up searches;
- `Satyanarayana Schoppmann Suffel reliability-improving graph transformation 1992`;
- `swing surgery Birnbaum importance`, `reliability-improving graph transformation Birnbaum`, and `Kelmans transformation Birnbaum reliability`.

The current Romero source remains Pablo Romero, *Characterization of locally most split reliable graphs*, *Theoretical Computer Science* 1047 (2025), 115327, DOI `10.1016/j.tcs.2025.115327`, arXiv:`2503.15453`. Its abstract still says that Brown--McMullin's remaining simple-graph existence/nonexistence cases are open and that Romero proves nonexistence only for

`n >= 7,  n <= m <= binom(n-3,2)+3`.

The bounded search surfaced later Romero work on ordinary two-terminal reliability and distance-constrained two-terminal reliability, but no later primary resolution of the residual **split-reliability** simple-graph problem or of the all-`n` max-minus-four diagonal. This is bounded negative evidence only; priority remains **UNVERIFIED**.

The nearest classical transformation source remains A. Satyanarayana, L. Schoppmann and C. L. Suffel, *A reliability-improving graph transformation with applications to network reliability*, *Networks* 22 (1992), 209--216, DOI `10.1002/net.3230220206`. Its published abstract proves ordinary all-terminal reliability improvement by swing surgery and, in particular, that deleting independent edges from a complete graph maximizes all-terminal reliability among graphs of the same order and size.

The targeted `swing surgery` / `Kelmans` + `Birnbaum importance` searches found generic component-importance literature defining Birnbaum importance as the reliability sensitivity/change when a component is toggled, but did **not** surface a theorem saying that swing surgery or a Kelmans compression monotonically improves the importance of a **distinguished marked edge**. This absence is only a bounded literature observation, not a nonexistence theorem.

Access limitation: the current Lyons--Peres PDF is large enough that one direct full-document fetch failed on content length, but the web index exposed the exact Question 6.20 text and the current codegree-3/4 annotation; the repository intake row independently contains the same source text. No conclusion relies on OCR.

## 4. Section-I(a): the exact mathematical statement that blocks the next diagonal

Let

`R(H;p)` be all-terminal reliability,

`Delta_st R(H;p) := R(H;p)-R(H-st;p)`,

and let `D_*={su,sv,sw}` be the terminal-centered three-star defect. After the exact terminal-edge swap reduction, the all-`n` max-minus-four route would close if one could prove

\[
\boxed{
\Delta_{st}R(K_n-D;p)
\;\le\;
\Delta_{st}R(K_n-D_*;p)
\quad
\text{for every stable three-edge defect type }D,\ n\ge 8,\ 0<p<1.
}
\tag{BLOCK}
\]

There are exactly 21 stable terminal-marked defect types, one of which is `D_*`; the finite `n=9` run and the independent P26 audit verify the desired coefficientwise ordering at that first source-new scale. What is missing is a proof of `(BLOCK)` uniform in `n` and `p`.

This is the mathematical blocker for extending the source result. It is distinct from the **active-claim closure blocker**, which is administrative/proof-validation rather than mathematical: one second genuinely distinct OTHER-task full-proof audit of the completed `n=8` layer is still missing.

## 5. Section-I(b): every route tried on this blocker and why each stops

### Route 1: ordinary all-terminal swing/Kelmans compression

The 1992 swing-surgery theorem gives monotonicity of the scalar quantity `R(G;p)` under its transformation. That is enough for the max-minus-two bridge because after adding the terminal edge the two compared hosts become isomorphic except for an ordinary adjacent-versus-independent two-edge deletion comparison.

For `(BLOCK)`, however, the object is the **difference**

`Delta_st R(G;p)=R(G;p)-R(G-st;p)`.

Knowing the sign of the change in `R(G;p)` and the sign of the change in `R(G-st;p)` separately does not compare their difference. Ordinary reliability improvement can improve the deleted-edge graph by more than it improves the marked-edge graph. Thus scalar monotonicity is the wrong invariant unless its proof is upgraded to a marked-edge statement.

### Route 2: the terminal-edge bridge

For any host `X` missing `st`, the exact identity

`R(X+st;p)=R(X;p)+p SR_X^{s,t}(p)`

recasts split reliability as the marked-edge all-terminal marginal. This completely solved the max-minus-two and, after an extra conditioning identity, the max-minus-three diagonal.

At max-minus-four it exposes rather than removes the obstruction: the 21 split functions become 21 **marked-edge marginals**. There is no longer a single pair of host reliabilities whose known ordinary order has the required sign after subtraction.

### Route 3: finite exact coefficientwise computation

R06 proved the `n=9,m=32` case by showing coefficientwise domination across all 21 stable types. P26 independently reproduced this using a different terminal-type classification and exact recurrence. This is strong finite evidence and a complete finite theorem, but it does not identify a symbolic-in-`n` nonnegative decomposition of the 20 gap vectors. Positivity at `n=9` cannot be promoted to all `n`.

### Route 4: group action / stable defect classification

The `S_6 x C_2` reduction shows that the type universe stabilizes at exactly 21. This removes combinatorial explosion, but symmetry alone does not order the reliability polynomials. It says the all-`n` problem is finite-dimensional in **type**, not that the coefficient gaps are positive for every `n`.

### Route 5: endpoint/local-optimum information

Romero's characterization identifies the locally most split-reliable balloon class near `p=1`, and low-density coefficients can often rule out uniform optimality. These endpoint tools decide many finite classes, but a uniform optimum requires an inequality for the entire interval `0<p<1`. Endpoint dominance does not rule out interior crossings.

### Route 6: ordinary Birnbaum-importance terminology

Method #17 found the right external language: `Delta_st R/p` is a Birnbaum-style component-importance quantity for the distinguished edge. The generic importance literature provides identities, interpretations and algorithms, but the targeted search did not reveal a graph surgery theorem with the marked-edge monotonicity needed in `(BLOCK)`. The translation is useful; the missing theorem remains missing.

## 6. Section-I(c): what a successful proof must contain that no current route contains

A proof needs a **marked transformation inequality**, not another ordinary-reliability inequality.

Suppose a terminal-preserving surgery `S` is used to move a defect type toward the centered star and commutes with deletion of `st`. Then the desired monotonicity of the marked marginal is exactly

\[
\Delta_{st}R(SG;p)-\Delta_{st}R(G;p)\ge 0,
\]

or equivalently

\[
\boxed{
\big(R(SG;p)-R(G;p)\big)
\;\ge\;
\big(R(S(G-st);p)-R(G-st;p)\big).
}
\tag{GAIN}
\]

Ordinary swing surgery controls the two gains in `(GAIN)` one at a time; the missing ingredient is an argument that the surgery gain is **larger when the marked edge is present** than when it is deleted.

There are two plausible forms that would be sufficient:

1. a terminal-preserving swing/Kelmans injection proving `(GAIN)` state-by-state (or coefficient-by-coefficient); or
2. for each of the 20 noncandidate stable defect types, an exact symbolic decomposition of

`Delta_st R(K_n-D_*;p)-Delta_st R(K_n-D;p)`

into a cone of manifestly nonnegative Bernstein-basis terms whose coefficients are nonnegative for every `n>=8`.

No route so far supplies either item uniformly in `n`.

## 7. Section-I(d): simplest special case still unproved

Within the exact `(BLOCK)` route, the simplest next finite instance not proved by R06 is

\[
\boxed{T_{10,41}},\qquad 41=\binom{10}{2}-4.
\]

The `n=9` instance `T_{9,32}` is proved and independently P26-audited; the all-`n` statement is not. I do **not** run a new `T_{10,41}` checker in this mandatory thinking run, because that would repeat the finite-scale route without supplying the missing uniform mechanism.

More broadly, the Romero source has many other still-open classes; this report is only identifying the simplest special case of the specific all-`n` max-minus-four obstruction.

## 8. Section-I(e): nearest solved literature problem and the missing ingredient

The nearest solved literature mechanism is Satyanarayana--Schoppmann--Suffel (1992): swing surgery provides a transformation monotonicity theorem for **ordinary all-terminal reliability** and proves the extremality of independent deletions from a complete graph.

That machinery was exactly strong enough for R06's max-minus-two theorem and, together with dense ULRG/compression inequalities and an exact conditioning identity, for max-minus-three.

What it lacks for max-minus-four is preservation of a **distinguished-edge marginal**. The source theorem orders `R(G;p)`; `(BLOCK)` asks to order

`R(G;p)-R(G-st;p)`.

The difference is not cosmetic: a surgery can have the correct ordinary-reliability direction on both `G` and `G-st` without preserving the order of the two gains. The next proof must mark `st` throughout the surgery argument rather than erase that information.

## 9. The three required new-method moves

### #13 FIND WHAT ONLY INCREASES

Candidate monovariant: the marked marginal

`M_st(G;p)=Delta_st R(G;p)`

under a sequence of terminal-preserving swings toward the terminal-centered star.

Outcome: **not established**. The exact failure point is `(GAIN)`: ordinary reliability gives no comparison between the two surgery gains. This is more informative than another finite lemma because it says exactly what a monotonicity proof must track.

### #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

Translation: `M_st/p` is the reliability importance of the marked edge, i.e. a Birnbaum-style component-importance quantity. I searched that language together with swing surgery and Kelmans/compression terminology.

Outcome: **useful language, no imported theorem found**. The searches surfaced component-importance definitions and sensitivity formulas, but no result that a reliability-improving graph compression preserves or improves the importance of a specified edge for all `p`.

### #22 READ THE FAILURES, NOT THE SUCCESSES

I compared why the preceding successful bridges stop here. Max-minus-two works because the two `+st` hosts are isomorphic and the whole split comparison collapses to one known all-terminal order. Max-minus-three works because conditioning on one carefully chosen edge produces the exact switch identity

`i-a=(1-p)(P-S)`,

which cancels the host mismatch. With three non-`st` defects there are 21 marked types and no single conditioning edge makes all competing host pairs collapse to the same two ordinary reliability values.

Outcome: the obstruction is **not** the number of graph types; it is the lack of a marked-edge surgery identity/monotonicity theorem. Repeating unmarked compression is therefore the wrong next move.

## 10. Recovery choice — exactly one

I choose:

**PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The next mathematical run, if the active closure state still has not changed and the six-unchanged rotation threshold has not yet been reached, should go inside the 1992 swing-surgery proof and keep `st` marked throughout. The concrete target is `(GAIN)`, first for surgeries whose moved vertices avoid `s,t`, then for the finite set of surgeries needed to connect the 21 defect types to the centered star. If the marked surgery gain cannot be made nonnegative, that failure should be converted into a counterexample to the proposed monovariant rather than followed by another unmarked reliability lemma.

Next Section-B methods planned: **#1 CHANGE THE CATEGORY, #12 FIND WHAT IS CONSERVED, #20 FIND WHY THE ALGORITHM FAILS**. These are not the same triple as this run or the preceding run.

## 11. Honest metric, audit, and stagnation status

Active fixed metric:

`R_SPLIT8: 0 -> 0`.

Active finite-layer status:

`CANDIDATE_COMPLETE / AUDITS_PENDING`.

Closure gate:

- P26 full-proof audit of exact `n=8,m=14,...,26` layer: PASS;
- second genuinely distinct OTHER-task full-proof audit: MISSING.

Therefore:

`audit gate: 1/2 -> 1/2`.

The supported fixed-metric unchanged count advances

`3 -> 4`.

This is **STUCK_RECOVERY_1**, not a new theorem run. The closable target rotates only after six unchanged runs under the controlling addendum; that threshold is not yet reached here.

Auxiliary `T_{9,32}` status changed only in audit confidence, not in the active metric:

`owner proof + exact core -> owner proof + independent P26 PASS`,

but it still has no second distinct OTHER-task audit and remains PARTIAL for the unrestricted source.

The original I0056 metric remains frozen:

`width 0 -> 0`, interval `[sqrt(5),sqrt(5)]`, full source Question 6.20 PARTIAL.

## 12. Model / scheduler truth and the P26 modification issue

This run actually uses GPT-5.6 Sol; the reasoning level is not authenticated by exposed runtime telemetry, so I record it as **UNVERIFIED**. The task-control surface available to this workflow still exposes prompt/title, schedule/timing, enabled state and timing mode, but **no binding model-family selector, no reasoning-effort selector, no guaranteed reasoning-duration field, and no authenticated per-run applied-model/reasoning receipt**. GPT-6/maximum therefore remains prompt request text only.

A real platform fix would require persistent model/reasoning fields in the task object, inference routing that honors them, and an authenticated applied-setting receipt on each run.

The historical P26 task ID `6aa7b43682948191b697d72fec69d539` did return `You cannot modify this task` in one R-series-visible context, as recorded in `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`. Root `RESULTS.md` later records that P26's full update **succeeded in a different authorized P/C context**. Thus the refusal is authorization-context-specific, not evidence that the task is permanently immutable. The lawful workaround is the owning/authorized workspace/API/backend context, ownership/admin repair or transfer, or platform support for the same task — not a cloned schedule or permission bypass.

Per the current R06 contract, I attempted **no scheduler change and no permission change**.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  run_kind: SECTION_I_THINKING_STUCK_RECOVERY_1
  original_source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20 / intake I0056"
  frozen_original_target: "H_{5,5}, degree 5, face-degree 5, outer vertex boundary"
  frozen_original_interval: "[sqrt(5),sqrt(5)]"
  frozen_original_metric_before: 0
  frozen_original_metric_after: 0
  original_status: PARTIAL_FULL_SOURCE
  active_claim: ROMERO-2025-SPLIT8
  active_source: "Pablo Romero, Characterization of locally most split reliable graphs, TCS 1047 (2025), 115327"
  fixed_metric: R_SPLIT8
  metric_before: 0
  metric_after: 0
  fixed_metric_unchanged_count_before: 3
  fixed_metric_unchanged_count_after: 4
  claimed_layer_status: CANDIDATE_COMPLETE_AUDITS_PENDING
  closure_audit_gate_before: "1/2"
  closure_audit_gate_after: "1/2"
  tried_moves: [13, 17, 22]
  exact_blocker: "Delta_st R(K_n-D;p) <= Delta_st R(K_n-D_*;p) for all stable 3-defect types D, n>=8, 0<p<1"
  simplest_unproved_special_case_on_blocker: "T_{10,41}"
  chosen_recovery_action: PORT_TECHNIQUE_FROM_NEAREST_SOLVED_PROBLEM
  next_methods: [1, 12, 20]
  remaining_obligation: "Active claim closure still needs one second genuinely distinct OTHER-task full-proof audit of the exact n=8 layer. Parent-source extension needs a marked-edge swing/compression inequality controlling the distinguished-edge all-terminal marginal, not only scalar all-terminal reliability."
  audit_ids:
    - "P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64_PASS_FULL_MATHEMATICAL_PROOF"
    - "SECOND_DISTINCT_N8_AUDIT_MISSING"
    - "P26-AUDIT-R06-ROMERO-MAX2-ALLN-65_PASS_FULL_MATHEMATICAL_PROOF"
    - "P26-AUDIT-R06-ROMERO-MAX3-ALLN-66_PASS_FULL_MATHEMATICAL_PROOF"
    - "P26-AUDIT-R06-ROMERO-MAX4-N9-67_PASS_FULL_FINITE_PROOF"
  repository_delta:
    base: ff9cd93f4e5e008d04cfb85d2a5d485352954653
    head_observed: c379ac52890c1439fdff6ffedd7133be0983478b
    ahead_by: 48
    behind_by: 0
    complete_changed_file_set: true
  provenance_note: "P26 max4-n9 report has a mistyped owner creation SHA ff9cd127...; actual R06 creation commit is ff9cd93f..., while audited path/blobs match."
  evidence:
    - "operations/claims/I0056.md"
    - "operations/claims/ROMERO-2025-SPLIT8.md"
    - "probability_1000_intake_I_20260914/problems.jsonl (I0056 row)"
    - "runs/R06/20260919T1040Z_romero_max4_n9_exact_62_7e4a.md"
    - "proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_14-01-16__run-report.md"
    - "proofnet24/P26-proof-audit-recovery/artifacts/2026-09-19/2026-09-19_14-01-16__romero_t932_audit.out"
    - "operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md"
    - "POSTED.md"
    - "RESULTS.md"
    - "QUEUE.md"
```
