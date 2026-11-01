Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `D_fix = 1 -> 1`; Section-B methods actually tried: #21 ASK WHO ELSE HAS THIS SHAPE, #22 READ THE FAILURES, NOT THE SUCCESSES, #27 SWAP THE QUANTIFIERS.**

# NM13-08 research invocation — P0093 exact binary-QSO equivalence and attribution reduction

Date: 2026-09-18 UTC  
Track / namespace: `proofnet24/NM13-08/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Canonical source / claim: `P0093`, `operations/claims/P0093.md`  
Canonical dedup key: `infinitely_many_fixed_points_of_a_finite_color_automaton`  
Selection shard: `7 mod 13`  
Workflow status after this run: **PROVED-CANDIDATE / AUDIT-PENDING / PRIOR-ART HIGH-RISK; not protocol-closed**  
Frozen metric before / after: **`D_fix = 1 -> 1`**  
Consecutive unchanged research runs on P0093: **1 -> 2**  
Stuck recoveries used on P0093: **0 -> 0**  
Required eventual outside auditors: **P26 and NM13-09; neither is counted as passed**

## 1. Runtime / control-plane disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control schema still offers prompt/title, scheduling or relative-start fields, timing mode, and enabled state, but **no bindable model-family selector and no bindable reasoning-effort selector**, and no authenticated per-run applied-model receipt. Therefore `GPT-6 / maximum` remains a prompt request only. Making it binding would require an owner-authorized product/workspace/API/admin task surface that exposes persistent model and reasoning controls together with authenticated runtime attestation.

The repository's current policy records the historical P26 `You cannot modify this task` event as authorization-context-specific and also records that P26 was later updated successfully from another authorized context. If a denial recurs, the lawful route is the owning/otherwise-authorized workspace or platform/admin support for that same task, never task cloning, permission changes, or access-control bypass. This invocation did not create, modify, disable, duplicate, or probe any schedule.

## 2. Authoritative continuity and required repository read

This invocation continues the already admitted P0093 target. It is **not a new admission**, and no second claim was created.

Before new work I reread or targeted-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0093.md`;
- the newest own report, `proofnet24/NM13-08/runs/2026-09-18/2026-09-18T07-46-00Z__p0093-all-arity-fixed-simplex.md`;
- newest visible neighboring NM13-07 report, `proofnet24/NM13-07/runs/2026-09-18/2026-09-18T08-34-05Z__p0282-sqrt-defect-window.md`;
- newest visible neighboring NM13-09 report, `proofnet24/NM13-09/runs/2026-09-18/2026-09-18T07-56-00Z__post-p0245-codex-p0001-p0096-screen.md`;
- newest visible P26 audit report, `proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_11-00-00__run-report.md`;
- exact P0093 / canonical-key / audit / PASS / ownership searches and the repository delta from the preceding NM13-08 report.

The preceding NM13-08 report was created at commit

`1602fe7359c68d3f0c6c48a3276a233ba57a9803`.

The pre-write `master` head observed for this invocation was

`4a407847d513c8f3b07f2419ddb06c6bee843577`.

The latter is **94 commits ahead, 0 behind** the preceding report commit. The changed-file surface contains other workers' reports, artifacts, and new claims, but no modification of `operations/claims/P0093.md`, no P0093 handoff/release/retirement, and no P0093 source correction. No owner-authorized release or competing P0093 owner was recovered.

The newest NM13-09 report explicitly says its mention of the neighboring P0093 result is **not an independent P0093 audit**; that run is successor admission screening. The newest P26 report audits a different P20 cyclic-interval target. Exact repository searches for `P0093 audit PASS` recovered the two NM13-08 reports and neighboring mentions, not a completed P26 or NM13-09 end-to-end audit. Thus the required P0093 audits remain:

- P26: **NOT PASSED**;
- NM13-09: **NOT PASSED**.

Large root and JSONL surfaces can be connector-bounded when rendered wholesale. Canonical claim identity, exact source/key searches, immutable reports, and exact commit comparison are therefore the continuity anchors; truncation is never treated as evidence of absence.

## 3. Exact source and fresh literature boundary — 2026-09-18

Primary source: Tobias Johnson, Moumanti Podder, Fiona Skerman, *Random tree recursions: which fixed points correspond to tangible sets of trees?*, Random Structures & Algorithms 56(3) (2020), 796–837; arXiv:1808.03019v2.

The source's Section 6, p.40 asks:

> when `3 <= |Sigma| < infinity`, can an automaton have infinitely many fixed points?

and notes that the two-state case is ruled out by analyticity.

The already admitted construction answers this existence question mathematically: with three colors and deterministic binary offspring, its fixed set is exactly

`{(1,0,0)} union {(1/2,t,1/2-t): 0<=t<=1/2}`.

The preceding invocation strengthened this to every `m>=3` and every deterministic arity `d>=2`, with exact fixed set

`{e_0} union {x in Delta_{m-1}: x_0=d^(-1/(d-1))}`.

This run's literature search did **not** try to re-prove that theorem. It targeted the remaining priority question identified in the preceding report: whether the binary three-color construction is already present, perhaps in another language, in the older quadratic-stochastic-operator literature.

Fresh 2026-09-18 queries included:

- the exact Johnson--Podder--Skerman title plus `infinitely many fixed points`;
- `coefficients 1 or 0 quadratic stochastic operators`;
- `0/1 quadratic stochastic operator Vallander`;
- `Dynamics of doubly stochastic quadratic operators on a finite-dimensional simplex` plus `fixed points`;
- `Vallander quadratic stochastic fixed points`;
- the exact 1972 Vallander title.

The primary 2020 source was recovered directly, including the Section 6 question. The 2016 Open Mathematics article by Abdulghafor--Shahidi--Zeki--Turaev was recovered in HTML. Its introduction explicitly states that an earlier paper `[12]` classified **general quadratic stochastic operators having coefficients 1 or 0 on the two-dimensional simplex**, and contrasts that class with extreme doubly stochastic QSOs whose coefficients may be `1`, `1/2`, or `0`.

The official MathNet record for S. S. Vallander, *On the limit behavior of iteration sequences of certain quadratic transformations*, Dokl. Akad. Nauk SSSR 202:3 (1972), 515–517, was recovered. The previous NM13-08 report had already identified this as the older `[12]` reference requiring reconciliation. The MathNet page exposes a 479 kB full-text PDF link, but the available fetch surface returned a **cache miss** when that PDF was requested, so I did not obtain or inspect the primary theorem text in this invocation. This access failure is disclosed rather than filled by inference.

A bounded current search still did not surface a later paper explicitly answering the Johnson--Podder--Skerman Section 6 question in tree-automaton language. That remains **bounded negative evidence only**, not proof of worldwide openness or novelty.

## 4. Frozen metric and saturation

The canonical claim freezes

`D_fix = a certified lower bound on the real dimension of the fixed-point set of the one explicit source-admissible three-color binary automaton/child-law pair`.

The first P0093 run proved the **complete** fixed set of that pair is a point plus a line segment, so its real dimension is exactly `1`. Consequently the frozen metric is not merely unchanged; it is mathematically saturated for the fixed pair:

`D_fix: 1 -> 1`.

I do not replace it by the dimension `m-2` of the stronger family, by a count of classified binary operators, or by a prior-art score. The supported unchanged-run counter therefore advances honestly

`1 -> 2`.

No stuck recovery is consumed yet. If the same metric and remaining closure obligation persist through the next invocation, the owner's three-unchanged-run / same-obligation Section-I protocol becomes mandatory.

## 5. Method #21 — ASK WHO ELSE HAS THIS SHAPE: exact external category identified

The preceding report observed that the deterministic binary case resembles a `0/1` quadratic stochastic operator. This run makes that identification exact, rather than heuristic.

A quadratic stochastic operator on the `(m-1)`-simplex has the form

`(Vx)_k = sum_{i,j in Sigma} p_{ij,k} x_i x_j`,

with

`p_{ij,k}=p_{ji,k} >= 0`,  `sum_k p_{ij,k}=1`.

A deterministic binary tree automaton under child law `chi=delta_2` sees only the unordered multiset of its two child colors. For each unordered pair it chooses exactly one parent color. Therefore its heredity tensor has exactly one `1` and the rest `0` for every pair.

This is not just an analogy: Section 6 proves the converse as well. Thus the source-valid deterministic-binary subproblem is **exactly the symmetric 0/1-QSO category**.

The external literature is consequently much closer than a generic fixed-point analogy. The source question's three-color binary construction lives inside an older finite classification universe on `S^2`.

**Outcome of #21:** success. It identifies the correct external category and turns a vague prior-art risk into a precise finite classification/attribution question.

## 6. Method #27 — SWAP THE QUANTIFIERS: exact binary automaton <-> 0/1-QSO theorem

### Theorem `NM13-08-P0093-03` — exact binary-QSO equivalence

Fix a finite color set `Sigma` of size `m` and deterministic offspring law `chi=delta_2`.

There is a bijection between:

1. deterministic count-based tree automata restricted to child-count vectors of total size `2`; and
2. symmetric quadratic stochastic operators on `Delta_{m-1}` whose heredity coefficients all belong to `{0,1}`.

Under this bijection, the tree automaton distributional map is exactly the QSO itself.

### Proof

Let `A` be a deterministic tree automaton. For each unordered pair of child colors `{i,j}`, let

`a(i,j) in Sigma`

be the parent color assigned by `A` to the corresponding count vector (`2e_i` if `i=j`, `e_i+e_j` if `i!=j`). Define

`p_{ij,k} = 1{a(i,j)=k}`.

Then `p_{ij,k}=p_{ji,k}` and, for each pair `(i,j)`, exactly one value of `k` has coefficient `1`, so

`p_{ij,k} in {0,1}`,  `sum_k p_{ij,k}=1`.

If the two children are i.i.d. with law `x`, the probability of an ordered color pair `(i,j)` is `x_i x_j`. Hence the parent law is

`Psi_k(x)=sum_{i,j} p_{ij,k} x_i x_j`.

That is exactly the associated symmetric 0/1 QSO.

Conversely, let a symmetric QSO have `p_{ij,k} in {0,1}` and `sum_k p_{ij,k}=1`. For every unordered pair `{i,j}`, there is a unique `k` for which `p_{ij,k}=1`. Define the deterministic automaton to output that `k` on the corresponding total-size-two count vector. Define the automaton arbitrarily on count vectors of other totals, which are never observed under `chi=delta_2`. The same probability calculation gives its distributional map equal to the original QSO.

The two constructions are inverse to each other. `QED`.

### Three-color finite atlas consequence

For three colors there are exactly

`binom(3+2-1,2)=6`

unordered child-color multisets of size two. Each independently chooses one of three outputs. Thus the source-valid deterministic-binary category contains exactly

`3^6 = 729`

labeled rules before quotienting by color permutations.

The NM13-08 source-answering rule is

`00 -> 0`, `01 -> 1`, `02 -> 2`, `11 -> 0`, `12 -> 0`, `22 -> 0`,

hence

`Psi_0 = x_0^2+x_1^2+x_2^2+2x_1x_2`,

`Psi_1 = 2x_0x_1`,

`Psi_2 = 2x_0x_2`.

The color `0` is the unique idempotent color of this binary operation, so every color automorphism fixes `0`; swapping active colors `1` and `2` is an automorphism. The stabilizer therefore has order two and the labeled color-permutation orbit has size three.

This finite reduction is useful for attribution: to decide whether the base construction is already present in a complete three-color 0/1-QSO classification, one need only identify this single color-permutation orbit, not compare vague qualitative descriptions of infinitely many fixed points.

The equivalence mechanism is elementary and should be regarded as folklore/category translation unless literature establishes otherwise. I make **no novelty claim** for the equivalence itself.

**Outcome of #27:** success. Swapping from “find some automaton” to “classify the fixed binary 0/1-QSO universe” produces an exact finite attribution target and a complete theorem on the page.

## 7. Method #22 — READ THE FAILURES, NOT THE SUCCESSES: why the obvious 2016 precedent does not yet settle the source

The 2016 Abdulghafor--Shahidi--Zeki--Turaev paper is especially informative because it contains an explicit QSO with infinitely many fixed points.

Their Example 4.4 gives, on `S^2`,

`V_2(x) = xy + 2xz`,

`V_2(y) = y^2 + xy + yz = y`,

`V_2(z) = x^2 + z^2 + yz`,

and their Theorem 4.5 proves infinitely many invariant segments and one fixed point on each segment.

At first glance that looks like a direct pre-2020 answer to P0093. It is **not** a deterministic binary tree automaton distributional map.

In QSO normalization, the coefficient of an off-diagonal monomial `x_i x_j` is `2p_{ij,k}` because both ordered pairs `(i,j)` and `(j,i)` appear. Therefore the coefficient `1` on the `xy` term in `V_2(x)` means

`p_{xy,x}=1/2`,

and the coefficient `1` on the same pair's `xy` term in `V_2(y)` means

`p_{xy,y}=1/2`.

Likewise the `yz` pair is split with half-coefficients. A deterministic count automaton cannot do this: a single count vector with one `x` child and one `y` child must choose one parent color, not split probability `1/2`--`1/2` between two outputs.

So the 2016 infinite-fixed-point example is **general-QSO prior art but not source-valid deterministic-binary prior art**. This corrects a possible over-reading of the previous run's broad QSO overlap.

The same 2016 article is more important for a different reason: its introduction says that **general QSOs with all heredity coefficients in `{0,1}` had already been classified on the 2D simplex** in an older reference. By Theorem `NM13-08-P0093-03`, that is exactly the source-valid three-color deterministic-binary category.

The previous run identified the relevant older reference as Vallander 1972. Fresh MathNet metadata confirms the primary article and full-text link, but the actual PDF could not be fetched through the available surface in this invocation. Without reading Vallander's theorem text, I cannot responsibly answer the decisive question:

> Does Vallander's classification merely enumerate/organize the 0/1 maps, or does it explicitly give enough dynamics/fixed-set information to identify the NM13-08 three-map orbit as having a continuum of fixed points?

If yes, then P0093 should be recorded as **KNOWN VIA TRANSLATION** with full attribution, not as a publication-novel construction. If no, the current source-level proof may still be a new application/translation even though the operator lies in an old classified universe.

**Outcome of #22:** success as a failure diagnosis. It rules out the tempting but invalid direct use of the 2016 half-coefficient example, while isolating one exact inaccessible primary source as the remaining priority bottleneck.

## 8. Why no new checker was manufactured

This run's new theorem is an exact category equivalence proved directly from definitions. Its finite count `3^6` is an immediate count of six unordered child-pair types, not the output of a search or an exhaustive UNSAT/SAT claim. The fixed set of the actual source-answering rule was already proved exactly and has an archived symbolic self-check from the first P0093 run.

No new numerical candidate, finite extremal search result, or certificate-dependent claim arose here. Creating another checker for a metric already saturated at one would invert the owner's 90/10 research order. The proof on this page is a self-proof, not an independent audit.

## 9. Current mathematical and closure verdict

The mathematical source existence question remains answered internally by a complete explicit construction, and the stronger all-arity/all-color theorem from the preceding report remains valid.

But P0093 is **not called protocol-closed** and is **not relabeled KNOWN** on this evidence.

Current gate state:

- source-level explicit proof: **COMPLETE internally**;
- frozen metric: **`D_fix=1`, saturated, no movement this run**;
- P26 independent end-to-end audit: **NOT PASSED**;
- NM13-09 independent end-to-end audit: **NOT PASSED**;
- deterministic 0/1-QSO prior-art overlap: **MATERIAL / EXACT PRECEDENCE UNRESOLVED**;
- Vallander 1972 primary metadata: **RECOVERED**;
- Vallander 1972 primary full theorem text: **INACCESSIBLE THIS RUN (PDF fetch cache miss)**;
- publication novelty: **UNVERIFIED / HIGH RISK**.

No paper folder is created before those gates are resolved.

## 10. Next step and approaching stuck trigger

This is the **second consecutive unchanged research run** after the initial `UNMEASURED -> 1` movement. The frozen metric cannot increase for the fixed pair because its exact fixed set has dimension one.

The highest-value next obligation is therefore not another automaton family or finite checker. It is:

1. recover an accessible primary copy, translation, or authoritative full theorem statement of Vallander 1972 and compare its 0/1 `S^2` classification to the explicit orbit in Section 6;
2. if exact precedence is established, change the research verdict honestly to `KNOWN VIA TRANSLATION` rather than claiming novelty;
3. if exact precedence is not established, preserve the source proof but continue to label novelty unverified;
4. check for actual P26 and NM13-09 full-proof audits, counting neither self-checks nor neighboring mentions;
5. if the next invocation still has `D_fix=1` and the same remaining obligation, execute the owner's mandatory five-part Section-I stuck report before any further theorem-building.

Fresh Section-B routes for that next stuck/recovery invocation must not simply repeat this run's `#21/#22/#27` triple.

## 11. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-08
  category: CLOSABLE_OUTSIDE
  run_status: PROVED_CANDIDATE_AUDIT_PENDING_PRIOR_ART_HIGH_RISK
  source_id: P0093
  claim_id: P0093
  claim_path: operations/claims/P0093.md
  canonical_dedup_key: infinitely_many_fixed_points_of_a_finite_color_automaton
  shard_residue_required: 7
  source_question: finite_color_tree_automaton_infinitely_many_distributional_fixed_points
  metric:
    name: D_fix
    definition: certified_real_dimension_lower_bound_for_the_fixed_three_color_binary_pair
    before: 1
    after: 1
    movement: false
    saturated_for_frozen_pair: true
  unchanged_research_runs:
    before: 1
    after: 2
  stuck_recoveries_used:
    before: 0
    after: 0
  methods_attempted:
    - 21
    - 22
    - 27
  method_outcomes:
    21: EXACT_EXTERNAL_CATEGORY_IDENTIFIED_AS_SYMMETRIC_0_1_QSO
    22: 2016_INFINITE_FIXED_QSO_HAS_HALF_COEFFICIENTS_NOT_DETERMINISTIC_BINARY;_VALLANDER_PRIMARY_TEXT_REMAINS_BOTTLENECK
    27: BINARY_TREE_AUTOMATON_IFF_SYMMETRIC_0_1_QSO_THEOREM_AND_FINITE_THREE_COLOR_ATTRIBUTION_ATLAS
  new_theorem:
    id: NM13-08-P0093-03
    statement: deterministic_binary_count_automata_are_exactly_symmetric_0_1_quadratic_stochastic_operators
    theorem_proof_on_report_page: true
    source_relevant: true
    novelty_claimed: false
    essential_finite_core: false
  prior_art:
    date_checked: 2026-09-18
    source_question_primary_recovered: true
    2016_infinite_fixed_qso_direct_source_precedent: false
    reason: example_4_4_uses_half_heredity_coefficients_on_mixed_pairs
    material_0_1_classification_overlap: true
    primary_reference: Vallander_1972_Dokl_Akad_Nauk_SSSR_202_3_515_517
    primary_metadata_recovered: true
    primary_full_text_recovered_this_run: false
    access_failure: MathNet_full_text_PDF_fetch_cache_miss
    exact_precedence: UNRESOLVED
    novelty_status: UNVERIFIED_HIGH_RISK
    worldwide_openness_claimed: false
  audits:
    P26: NOT_PASSED
    NM13-09: NOT_PASSED
  previous_report_commit: 1602fe7359c68d3f0c6c48a3276a233ba57a9803
  prewrite_master_head: 4a407847d513c8f3b07f2419ddb06c6bee843577
  repo_delta_from_previous_report:
    commits_ahead: 94
    commits_behind: 0
    p0093_claim_changed: false
    p0093_release_found: false
    p0093_competing_owner_found: false
    p0093_audit_pass_found: false
  next_step: resolve_Vallander_1972_exact_0_1_QSO_precedence_and_check_P26_NM13_09_audits;_next_unchanged_run_triggers_section_I
```

## 12. Operational safeguards observed

This invocation writes only this immutable NM13-08 run report. It does not edit shared root ledgers, the canonical claim, another track's namespace, workflows, permissions, schedules, public surfaces, email/Gmail, Drive, or paid-compute resources. It does not run or import unreviewed external scripts. No substantive artifact was warranted beyond the theorem and prior-art analysis on the report page. The report is to be read back at its creation commit; no receipt-only follow-up commit is authorized.