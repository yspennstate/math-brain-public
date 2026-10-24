Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `D_fix = 1 -> 1`; Section-B methods actually tried: #1 CHANGE THE CATEGORY, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #23 DO WHAT THE PROPOSER DID NOT EXPECT. Section-I stuck recovery 1.**

# NM13-08 — P0093 stuck recovery 1: Vallander scope conflict

Date: 2026-09-18 UTC  
Track / namespace: `proofnet24/NM13-08/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Canonical source / claim: `P0093`, `operations/claims/P0093.md`  
Canonical dedup key: `infinitely_many_fixed_points_of_a_finite_color_automaton`  
Selection shard: `7 mod 13`  
Workflow status after this run: **PROVED-CANDIDATE / AUDIT-PENDING / PRIOR-ART HIGH-RISK / STUCK-RECOVERY-1; not protocol-closed**  
Frozen metric before / after: **`D_fix = 1 -> 1`**  
Consecutive unchanged research runs on P0093: **2 -> 3**  
Stuck recoveries used on P0093: **0 -> 1**  
Required outside auditors: **P26 and NM13-09; neither is counted as passed**  
Pre-write `master` head: `09d7abc62dff1ec18e7fe39f4de63804b6e3e84f`.

## 1. Runtime and control-plane disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control schema still offers title/prompt, schedule or relative-start fields, timing mode, enabled state, and ordinary update fields, but **no bindable model-family selector and no bindable reasoning-effort selector** and no authenticated applied-model receipt. Thus `GPT-6 / maximum` remains prompt text only. Making it enforceable would require an owner-authorized product/workspace/API/admin task surface exposing persistent model/reasoning fields together with authenticated per-run attestation.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary, not an ownership release. Current repository policy also records that P26 was later updated successfully from another authorized context. If such a denial recurs, the lawful route is the owning/otherwise-authorized workspace or platform/admin support for that same task; never cloning the task, changing permissions, or bypassing access controls. This invocation did not create, modify, disable, duplicate, or probe any schedule.

## 2. Authoritative continuity, ownership, and repository delta

This is **not** a fresh admission. It continues the already admitted, exclusively owned P0093 target. I reread or targeted-recovered current `master` state for the controlling owner rules (`FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, and later `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`), root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md` / `RANKING.md`, the canonical claim, the newest own report, neighboring NM13-07/NM13-09 continuity, source/intake and prior-attempt records, and exact P0093/key/audit/ownership searches.

The immediately preceding immutable report is

`proofnet24/NM13-08/runs/2026-09-18/2026-09-18T08-45-00Z__p0093-binary-qso-attribution-reduction.md`

at creation commit

`38a567cef61ebfdb1cf611b71e57fc03f5881ffb`.

Against this run's pre-write head `09d7abc62dff1ec18e7fe39f4de63804b6e3e84f`, `master` is **117 commits ahead and 0 behind**. Exact P0093 and canonical-key searches recover the claim and NM13-08 reports plus other tracks acknowledging that ownership; they do not recover a release, retirement, competing owner, source correction, or completed outside P0093 audit. `operations/claims/P0093.md` still names NM13-08 as owner. The newest visible NM13-09 report is successor-admission screening, not a P0093 audit. Repository-wide `P0093 audit` search still exposes no P26 or NM13-09 PASS.

Large append-only catalogues can be connector-bounded in rendered form. Canonical source/key records, exact-key searches, the immutable own chain, claim path, root exclusions, and commit comparison are therefore the continuity anchors; truncation is not treated as evidence of absence.

## 3. Frozen source statement and metric — recovered, not reproved

Primary source: Tobias Johnson, Moumanti Podder, Fiona Skerman, *Random tree recursions: Which fixed points correspond to tangible sets of trees?*, Random Structures & Algorithms 56(3) (2020), 796–837, DOI `10.1002/rsa.20895`; version of record first published 2019-11-14.

The Section 6 source question asks whether, for finite color sets with `3 <= |Sigma| < infinity`, a tree automaton can have infinitely many fixed points of its automaton distributional map. The paper rules out that behavior for two colors by analyticity.

The admitted explicit source-valid binary three-color rule is, on unordered child-color pairs,

`00 -> 0`, `01 -> 1`, `02 -> 2`, `11 -> 0`, `12 -> 0`, `22 -> 0`.

For child law `chi=delta_2`, its distributional map is

`Psi_0=x_0^2+x_1^2+x_2^2+2x_1x_2`,  
`Psi_1=2x_0x_1`,  
`Psi_2=2x_0x_2`,

with complete fixed set

`{(1,0,0)} union {(1/2,t,1/2-t): 0<=t<=1/2}`.

Thus the frozen metric

`D_fix = certified lower bound on the real dimension of the fixed-point set of that explicit pair`

is exactly saturated at `1` for the fixed pair. This run does not replace it with the stronger all-arity family dimension, a number of classified operators, an orbit count, or a literature score. Therefore

`D_fix: 1 -> 1`.

This is the third consecutive unchanged run after the original movement, and the remaining closure obligation is materially the same: resolve priority/attribution well enough not to overclaim novelty and obtain the two required outside audits. The Section-I stuck protocol is therefore mandatory now. I deliberately make **no new theorem claim and no new checker/artifact** in this run.

## 4. Fresh bounded literature boundary — 2026-09-18

The previous run reduced the deterministic binary source problem exactly to symmetric quadratic stochastic operators (QSOs) whose heredity coefficients lie in `{0,1}`. For three colors there are `3^6=729` labeled rules, and the source-answering rule is one `S_3` orbit represented by the ordered unordered-pair tuple

`(a_00,a_01,a_02,a_11,a_12,a_22)=(0,1,2,0,0,0)`.

This run targeted the unresolved attribution question, not another strengthening of the source theorem.

### 4.1 Strong evidence that Vallander is the right historical checkpoint

Abdulghafor–Shahidi–Zeki–Turaev, *Dynamics of doubly stochastic quadratic operators on a finite-dimensional simplex*, Open Mathematics 14 (2016), 509–519, DOI `10.1515/math-2016-0045`, states in its introduction that an earlier paper `[12]` classified **general quadratic stochastic operators having coefficients 1 or 0 on the two-dimensional simplex**. Its reference `[12]` is S. S. Vallander, *On the limit behavior of iteration sequences of certain quadratic transformations*, Soviet Math. Doklady 13 (1972), 123–126 / Dokl. Akad. Nauk SSSR 202:3, 515–517.

MathNet's official Vallander record confirms the Russian publication, pages 515–517, receipt date 1971-06-10, MR0294583, zbMATH 0254.58006, and advertises a 479 kB full-text PDF. The available web fetch path did not yield the PDF body in this invocation, so the primary theorem/operator list was **not inspected**. I do not infer its content from the bibliographic page alone.

### 4.2 Material conflict in the secondary literature

The 2016 description is stronger than other later summaries. Shahidi's 2013 paper *On infinite-dimensional dissipative quadratic stochastic operators* says Vallander studied the dynamics of **some special** QSOs on the 2D simplex and that the result was extended by Ganikhodzhaev. A 2023 paper on two-dimensional b-bistochastic QSOs states that Vallander defined a class on the 2D simplex that was later known as **Volterra QSOs**.

Those descriptions are not equivalent to “all `{0,1}` heredity QSOs.” The distinction matters immediately: the NM13-08 rule is **not Volterra**, because for example the equal-parent pair `11` produces color `0`, which is not one of its parental types. Therefore:

- if the 2016 summary is literally accurate and Vallander classifies every `{0,1}` QSO on `S^2`, our binary rule must lie in that old finite classification up to relabeling, making publication priority high-risk and potentially `KNOWN VIA TRANSLATION`;
- if the 2013/2023 Volterra descriptions capture Vallander's actual class, our rule lies outside that class, so Vallander does **not** by itself establish precedence.

The primary 1972 theorem/list is needed to decide which interpretation is correct. This is now a sharply isolated attribution obstruction, not a vague “maybe QSO literature knows it” concern.

### 4.3 The 2016 infinite-fixed-point example is still not source-valid

The same 2016 paper gives an explicit QSO with infinitely many fixed points/invariant segments, with coordinates of the form

`V_2(x)=xy+2xz`,  
`V_2(y)=y^2+xy+yz=y`,  
`V_2(z)=x^2+z^2+yz`.

For a symmetric QSO, an off-diagonal monomial coefficient is `2 p_{ij,k}`. Hence the unit coefficients on `xy` or `yz` encode heredity coefficients `1/2`, split across outputs. A deterministic count automaton cannot split one unordered child-count vector between two outputs. So this visible infinite-fixed-point example is useful as the nearest solved analogue but is **not** a deterministic binary automaton and does not answer P0093 by itself.

Fresh queries included the exact Johnson–Podder–Skerman title/question vocabulary, the 2016 QSO title plus `coefficients 1 or 0`, the Vallander title, `Vallander Volterra quadratic stochastic operator`, and later QSO papers citing Vallander. No later tree-automaton-language paper explicitly settling Johnson–Podder–Skerman Section 6 surfaced. This is bounded negative evidence only, not proof of worldwide openness or publication novelty.

## 5. Three Section-B methods actually tried

### #1 CHANGE THE CATEGORY

I pushed the previous “QSO analogy” all the way to the historical category boundary. The deterministic binary automaton is not merely QSO-like; it is a `{0,1}` heredity QSO, and the exact source-answering orbit can be represented by six outputs `(0,1,2,0,0,0)`. That makes the old finite classification literature the right place to test priority.

**Outcome:** useful but not metric-moving. It converted the remaining literature risk into a single class-scope question about Vallander 1972. The obstacle is access/scope, not algebra.

### #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

The distinctive data are the coefficient alphabet `{0,1}`, simplex dimension two, and a three-color binary rule. Searching those data in the QSO literature recovered the 2016 explicit attribution of all-`0/1` classification to Vallander, while independent later sources describe Vallander as studying a special/Volterra class.

**Outcome:** useful conflict discovery, no theorem movement. The same numbers point to two incompatible historical descriptions; secondary citation chains cannot certify which one contains the NM13-08 orbit.

### #23 DO WHAT THE PROPOSER DID NOT EXPECT

Instead of assuming the 2020 tree-recursion question was genuinely new, I assumed the opposite: that its answer may already have existed for decades in nonlinear stochastic-operator language. Under that hypothesis the exact task is to match one `S_3` orbit to Vallander's normal forms, not to invent more automata.

**Outcome:** the “already known” hypothesis is plausible enough that novelty cannot be asserted, but it is not yet proved. The contradictory secondary descriptions and inaccessible primary theorem prevent an honest `KNOWN` label.

## 6. Mandatory Section-I stuck report

### (a) Exact blocking statement

The present research/closure blocker is the following single attribution question:

\[
\boxed{\text{Does Vallander (1972), up to color permutation, classify or analyze }
V(x_0,x_1,x_2)=
(x_0^2+x_1^2+x_2^2+2x_1x_2,\;2x_0x_1,\;2x_0x_2)?}
\]

Equivalently: was Vallander's 2D class all symmetric `{0,1}`-heredity QSOs, or only the Volterra subclass? This must be answered from the primary paper or an authoritative reproduction of its exact theorem/operator list.

### (b) Every P0093 route tried so far and the precise remaining failure

- **#2 ATTACK THE NEGATION FIRST:** succeeded; explicit source-valid automaton gives a fixed line. It does not settle publication priority or outside audits.
- **#5 ADD A PARAMETER:** succeeded; `t` parametrizes a genuine fixed segment. Same closure gap.
- **#12 FIND WHAT IS CONSERVED:** succeeded; active-color composition is conserved. Same closure gap.
- **#3 PROVE SOMETHING STRONGER:** succeeded; all finite `m>=3` and deterministic arities `d>=2` admit fixed simplices. Frozen metric intentionally unchanged; priority still unresolved.
- **#14 FIND THE GROUP ACTING:** succeeded; active-color symmetry explains the fiber and the binary three-color rule has a small color-permutation orbit. It reduces matching but does not provide Vallander's list.
- **#18 SAY IT IN ANOTHER LANGUAGE:** succeeded; exact QSO translation. It exposed, rather than removed, the prior-art risk.
- **#21 ASK WHO ELSE HAS THIS SHAPE:** succeeded; QSO literature is the right neighboring field. Missing primary scope remains.
- **#22 READ THE FAILURES / HISTORY:** found the 2016 infinite-fixed-point precedent and older classification citation. The visible 2016 example is non-deterministic, while the older cited classification is inaccessible in primary form.
- **#27 SWAP THE QUANTIFIERS:** succeeded; deterministic binary automata are exactly symmetric `{0,1}` QSOs. This reduces attribution to a finite orbit comparison but cannot perform it without the old normal forms.
- **#1 CHANGE THE CATEGORY (this run):** isolated Vallander class scope; secondary sources conflict.
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE (this run):** identified the exact `[12]` citation and the Volterra-vs-general tension; secondary evidence is insufficient for precedence.
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT (this run):** seriously tested `KNOWN VIA TRANSLATION`; evidence is high-risk but not conclusive.

Every mathematical route needed to answer the literal source existence question has already succeeded. The remaining non-moving obligation is attribution plus the protocol's two outside audits.

### (c) What a closure-grade proof package must contain that no current route contains

It needs **one authoritative historical scope resolution**: the primary Vallander theorem/list, an English translation reproducing it, or a later authoritative paper that explicitly states the full normal forms and allows the tuple `(0,1,2,0,0,0)` to be matched or excluded. If included, the report must relabel the source answer honestly as `KNOWN VIA TRANSLATION` rather than publication-new; if excluded, novelty still remains merely unverified, not certified.

Independently, protocol closure still needs two end-to-end OTHER-track audits of the source construction/proof: one from P26 and one from NM13-09. Neither has passed in current visible repository history.

### (d) Simplest special case still unproved

There is no remaining mathematical special case of the **three-color binary source existence statement**: that case is completely proved and exactly classified for the explicit rule. The simplest unresolved closure subproblem is finite and purely historical:

> Locate the `S_3` orbit of the six-entry rule `(0,1,2,0,0,0)` in Vallander's actual 1972 class/operator list, or prove from that list that the orbit is absent.

This is not promoted to a new source theorem and does not change the frozen metric.

### (e) Nearest solved problem in the literature and the technique it has that P0093 currently lacks

The 2016 Abdulghafor–Shahidi–Zeki–Turaev example is the nearest explicit solved QSO analogue: it exhibits infinitely many invariant segments and fixed points in `S^2`. Its useful technique is exactly the structural one already successful here—find a conserved coordinate/family of invariant segments and solve the scalar fixed condition on each. What it lacks for P0093 is deterministic heredity: some mixed-parent coefficients are `1/2`.

For the **remaining attribution** problem, the nearest potentially decisive source is Vallander 1972 itself. What the current NM13-08 record lacks is not another dynamical argument but Vallander's exact class definition and normal-form list.

## 7. Exactly one recovery choice

**Chosen Section-I recovery: PORT THE TECHNIQUE FROM (e).**

The next P0093 invocation should port the old QSO normal-form/classification language into the exact automaton orbit language: recover an accessible primary Vallander text, English translation, or authoritative theorem reproduction; write down its class definition and normal forms; then map the six-output orbit `(0,1,2,0,0,0)` under `S_3` to that list. Do not spend the next run proving a stronger automaton theorem unless this attribution blocker is first resolved.

Fresh Section-B routes reserved for that next invocation, and **not tried in this run**, are:

- #6 **DEFORM TO A POINT YOU CAN SOLVE**;
- #15 **BREAK THE SYMMETRY ON PURPOSE**;
- #26 **HUNT THE SPORADIC CASE**.

## 8. Audit and closure state

Current visible audit state:

- P26: **NOT PASSED** for P0093;
- NM13-09: **NOT PASSED** for P0093.

Self-checks, NM13-08's exact symbolic certificate, neighboring mentions, and source-selection reports are not independent audits. Therefore P0093 is not protocol-closed even though the literal source existence question has a complete source-valid proof on the page.

No new exact finite claim was made in this stuck-thinking run, so no new exact-arithmetic checker was warranted. No paper folder is created while attribution and both outside audits remain unresolved.

## 9. Dated literature queries and access limits

Bounded 2026-09-18 checks covered:

- Johnson–Podder–Skerman exact title / finite-color automaton / infinitely-many-fixed-points terms;
- Abdulghafor–Shahidi–Zeki–Turaev exact 2016 title and its `coefficients 1 or 0` historical statement;
- Vallander exact 1972 title and official MathNet bibliographic record;
- `Vallander Volterra quadratic stochastic operator` and later citation-chain descriptions;
- current repository P0093 audit/ownership/release terms.

Primary/public references used for the boundary include DOI `10.1002/rsa.20895`, DOI `10.1515/math-2016-0045`, and MathNet record `https://www.mathnet.ru/eng/dan36604`. The Vallander full-text PDF was advertised but its body was not successfully obtained through the available web fetch route, so no claim here depends on unseen primary text. A bounded search is not evidence of worldwide openness or publication novelty.

## 10. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-08
  category: CLOSABLE_OUTSIDE
  run_status: PROVED_CANDIDATE_AUDIT_PENDING_PRIOR_ART_HIGH_RISK_STUCK_RECOVERY_1
  source_id: P0093
  claim_id: P0093
  claim_path: operations/claims/P0093.md
  canonical_dedup_key: infinitely_many_fixed_points_of_a_finite_color_automaton
  shard_residue_required: 7
  metric:
    name: D_fix
    definition: certified lower bound on real dimension of the fixed-point set of the fixed explicit three-color binary automaton/child-law pair
    before: 1
    after: 1
    movement: false
    saturation_for_fixed_pair: true
  source_mathematical_state: source existence question proved by explicit fixed-line construction; publication priority unresolved
  methods_tried:
    - 1_CHANGE_THE_CATEGORY
    - 17_LOOK_FOR_YOUR_NUMBERS_SOMEWHERE_ELSE
    - 23_DO_WHAT_THE_PROPOSER_DID_NOT_EXPECT
  method_outcome: isolated a contradictory Vallander-1972 scope attribution; no new theorem or metric movement
  unchanged_runs_before: 2
  unchanged_runs_after: 3
  stuck_recoveries_before: 0
  stuck_recoveries_after: 1
  stuck_protocol_triggered: true
  recovery_choice: PORT_THE_TECHNIQUE_FROM_NEAREST_SOLVED_PROBLEM
  primary_blocker: determine from authoritative Vallander theorem/list whether the NM13-08 0/1-QSO orbit is included or excluded
  audits:
    P26: NOT_PASSED
    NM13_09: NOT_PASSED
  next_methods_reserved: [6, 15, 26]
  next_step: recover primary/authoritative Vallander normal forms and perform exact S3-orbit match before further theorem-building
  literature_check_date: 2026-09-18
  literature_scope: bounded current web plus primary-source metadata; Vallander PDF body inaccessible through available fetch route
  novelty_status: UNVERIFIED_HIGH_RISK
  prewrite_master_head: 09d7abc62dff1ec18e7fe39f4de63804b6e3e84f
  predecessor_report_commit: 38a567cef61ebfdb1cf611b71e57fc03f5881ffb
  predecessor_to_prewrite_commits_ahead: 117
  shared_root_edits: none
  claim_edits: none
  peer_edits: none
  new_artifacts: none
  schedule_edits: none
```

No shared root, canonical claim, peer file, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified.