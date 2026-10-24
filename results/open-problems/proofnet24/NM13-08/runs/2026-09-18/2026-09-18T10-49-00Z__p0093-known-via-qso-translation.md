Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `D_fix = 1 -> 1`; Section-B methods actually tried: #6 DEFORM TO A POINT YOU CAN SOLVE, #15 BREAK THE SYMMETRY ON PURPOSE, #26 HUNT THE SPORADIC CASE. SOURCE-STATUS MOVEMENT: P0093 -> KNOWN VIA TRANSLATION (Rozikov–Xudayarov 2022).**

# NM13-08 — P0093 source resolution: exact 2022 QSO translates to the three-colour binary automaton

Date: 2026-09-18 UTC  
Track / namespace: `proofnet24/NM13-08/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Canonical source / claim: `P0093`, `operations/claims/P0093.md`  
Canonical dedup key: `infinitely_many_fixed_points_of_a_finite_color_automaton`  
Selection shard: `7 mod 13`  
Frozen metric before / after: **`D_fix = 1 -> 1`**  
Source status after this run: **KNOWN VIA TRANSLATION**  
Worker action after this run: **retire P0093 from active research and rotate on the next invocation**  
Consecutive unchanged metric runs on P0093: **3 -> 4 (terminal because source status resolved)**  
Stuck recoveries used: **1 -> 1**; this run executes the recovery route selected in stuck recovery 1 rather than opening a second stuck episode.  
Required novelty auditors named at admission: **P26 and NM13-09; neither is claimed to have passed.** No novelty closure is asserted because the source answer is prior art.

## 1. Runtime and task-control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed scheduler/task-control schema still offers title, prompt, schedule or relative-start data, timing mode, enabled state, and task identifiers. It exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model-family and reasoning-effort controls together with authenticated per-run runtime attestation.

The repository records that the historical P26 `You cannot modify this task` event was authorization-context-specific and that a later P26 update succeeded from another authorized context. If such a denial recurs, the lawful workaround is the owning/otherwise-authorized scheduler context or an authorized platform/admin/support path for that same task, not task duplication, permission changes, or access-control bypass. I did not create, modify, disable, duplicate, or probe a schedule in this invocation.

## 2. Authoritative continuity and ownership

This run continues the already admitted exclusive target `P0093`; it does **not** perform a new admission and does not create another claim.

Before new research I reread or targeted-recovered the current controlling state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the Codex P0093 source/attempt catalogue and current canonical claim `operations/claims/P0093.md`;
- the newest own report `proofnet24/NM13-08/runs/2026-09-18/2026-09-18T09-49-00Z__p0093-stuck-recovery-1-vallander-scope-conflict.md`;
- newest neighboring NM13-07 report `proofnet24/NM13-07/runs/2026-09-18/2026-09-18T10-41-00Z__p0282-n75-long-sector-recurrence.md`;
- newest neighboring NM13-09 report `proofnet24/NM13-09/runs/2026-09-18/2026-09-18T10-45-30Z__post-p0245-admission-delta-screen-4.md`;
- exact P0093/canonical-key claim, handoff, attempt, audit, POSTED, and campaign-status searches.

The claim still records owner `NM13-08`, canonical SHA256 `84caf950f79fd055bda2417e9c2735953d88fd93dc73ee53fdc6ec38f8a9d753`, and residue 7. No competing owner, owner-authorized release, retirement, P0093 POSTED entry, P0093 campaign settlement, P26 PASS, or NM13-09 P0093 audit PASS was recovered. The newest NM13-09 report is still an admission screen on its own lane, not an audit of P0093.

Large append-only ledgers can be connector-bounded when rendered wholesale. Exact canonical identity, current claim ownership, immutable report continuity, source text, and targeted attempt/audit searches are the anchors; truncation is not treated as evidence of absence.

A fresh pre-write branch read showed concurrent fleet commits continuing on `master`; this does not release P0093 or alter its frozen metric.

## 3. Exact source question and standing hypotheses

Johnson–Podder–Skerman, *Random tree recursions: which fixed points correspond to tangible sets of trees?*, Random Structures & Algorithms 56(3) (2020), 796–837, DOI `10.1002/rsa.20895`, arXiv `1808.03019v2`, Section 6 asks:

> when `3 <= |Sigma| < infinity`, can an automaton have infinitely many fixed points?

The source defines a tree automaton as a deterministic map `A: N_0^Sigma -> Sigma`. For a child law `chi`, its distributional map `Psi` sends a probability vector on the colours to the induced parent-colour distribution. The paper's standing assumption is that `chi` gives positive probability to `{2,3,...}`. Therefore the deterministic binary child law

`chi = delta_2`

is source-admissible.

This point matters: for `delta_2`, every deterministic unordered rule on the six two-child colour multisets gives a quadratic stochastic operator whose heredity coefficients are all exactly `0` or `1`.

## 4. Frozen mathematical state before this run

The admitted metric is

`D_fix = certified lower bound on the real dimension of the fixed-point set of one explicit source-admissible finite-colour automaton/child-law pair.`

The first P0093 research run had already constructed the three-colour binary rule

```text
00 -> 0
01 -> 1
02 -> 2
11 -> 0
12 -> 0
22 -> 0
```

with `chi=delta_2`. Writing a colour distribution as `(x,y,z)`, its exact distributional map is

```text
Psi_0 = x^2 + y^2 + z^2 + 2yz
Psi_1 = 2xy
Psi_2 = 2xz.
```

Its fixed set is exactly

```text
{(1,0,0)} union {(1/2,t,1/2-t): 0 <= t <= 1/2},
```

so `D_fix >= 1`. The archived exact self-check

`proofnet24/NM13-08/artifacts/2026-09-18/p0093_exact_checker.out`

at commit `ac4551b7f8d8a7a25c11755aa84b12c55f96b732` ends `ALL_EXACT_CHECKS_PASS` and records the tangent vector `[0,1,-1]` and `D_fix_lower_bound: 1`.

Thus the mathematical existence answer itself was already exact. The unresolved obligation entering this run was **literature status**: whether this exact binary QSO, or an equivalent one, was already in print. The previous run's older Vallander attribution chain was too ambiguous to support a safe novelty claim.

## 5. Idea-before-code record for this run

No new checker was written. The selected recovery route from the preceding stuck report was to **port the nearest quadratic-stochastic-operator literature back to the source automaton language** and settle attribution before doing more theorem-building.

That route succeeded. Since the mathematical map and fixed set did not change, manufacturing a second certificate would violate the 90/10 instruction. This run therefore spends its substantive effort on the exact literature-to-source identification below and reuses the already archived exact checker only as an independent algebra guard.

## 6. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: the parameter endpoint `a=0`

Fresh literature search on 2026-09-18 recovered the peer-reviewed paper

U. A. Rozikov and S. S. Xudayarov, *Quadratic non-stochastic operators: examples of splitted chaos*, **Annals of Functional Analysis 13:17 (2022)**, DOI `10.1007/s43034-021-00162-5`; preprint arXiv `2106.15958`.

In Section 4.1 they study, for `a in [0,2]`, the simplex map

```text
x' = x^2 + y^2 + z^2 - axy - axz + 2yz
 y' = (2+a)xy
 z' = (2+a)xz.                                      (RX 4.1)
```

They solve its fixed points explicitly: besides `(1,0,0)`, there is the family

```text
(1/(2+a), y, 1 - 1/(2+a) - y),
0 <= y <= 1 - 1/(2+a).                              (RX fixed family)
```

The deformation endpoint `a=0` is therefore

```text
x' = x^2 + y^2 + z^2 + 2yz
 y' = 2xy
 z' = 2xz,
```

with fixed segment

```text
(1/2, y, 1/2-y),  0 <= y <= 1/2.
```

This is **literally the P0093 map already certified in our archive**, after only renaming coordinates. The source question is from 2019/2020; the Rozikov–Xudayarov preprint is June 2021 and the journal paper is 2022, so this is later literature.

Outcome of method #6: **decisive**. The prior-art question is no longer an attribution risk; an exact later published map contains our construction as a parameter endpoint.

## 7. Method #15 — BREAK THE SYMMETRY ON PURPOSE: recover the deterministic heredity table

The paper is framed around quadratic operators, so an exact source translation still has to verify that the `a=0` endpoint is not merely a general simplex-preserving quadratic map with fractional heredity coefficients.

At `a=0`, each unordered child-colour pair contributes to exactly one output coordinate:

```text
xx -> x       yy -> x       zz -> x
xy -> y       xz -> z       yz -> x.
```

Equivalently, the heredity coefficients are `0/1`, one `1` for each unordered input pair. The mixed terms carry coefficient `2` only because the two ordered child sequences occur with the same probability. In particular,

```text
x' + y' + z'
 = x^2+y^2+z^2+2xy+2xz+2yz
 = (x+y+z)^2
 = 1
```

on the simplex.

Relabeling `x,y,z` as colours `0,1,2` gives exactly

```text
00->0, 01->1, 02->2, 11->0, 12->0, 22->0.
```

With `chi=delta_2`, this is a deterministic Johnson–Podder–Skerman tree automaton, not a relaxed or randomized rule.

Outcome of method #15: **successful source-language transfer**. The asymmetry of the `4-1-1` allocation is precisely what makes the published QSO a valid deterministic three-colour automaton.

## 8. Method #26 — HUNT THE SPORADIC CASE: the stochastic boundary hidden inside a non-stochastic family

The useful case is the boundary `a=0`. Although the Rozikov–Xudayarov paper is titled and organized around quadratic **non-stochastic** operators, its family is stated for `a in [0,2]`, and the endpoint `a=0` has no negative coefficients at all. It is an ordinary deterministic quadratic stochastic operator with the exact continuum of fixed points above.

This is the sporadic/source-valid case that the previous broad QSO searches did not isolate. No chaos theorem from the paper is needed. Only the displayed operator and its exact fixed-point family are used.

Outcome of method #26: **successful boundary extraction**. The source question is answered by the simplest endpoint of a family studied for a different dynamical purpose.

## 9. Complete source translation

Here is the source answer in one self-contained chain.

Take `Sigma={0,1,2}`, `chi=delta_2`, and define the deterministic automaton on two-child multisets by

```text
00->0, 01->1, 02->2, 11->0, 12->0, 22->0.
```

If child colours are iid with probabilities `(x,y,z)`, the parent law is

```text
Psi(x,y,z)=(x^2+y^2+z^2+2yz, 2xy, 2xz).
```

Rozikov–Xudayarov (2022), their equation (4.1) and fixed-point calculation in Section 4.1, give for the parameter endpoint `a=0` exactly this map and the fixed family

```text
(1/2,t,1/2-t), 0<=t<=1/2.
```

There are uncountably many such probability vectors. Hence the answer to the Johnson–Podder–Skerman Section-6 existence question is **YES**.

This is not a new NM13 theorem. It is an exact translation of later published literature into the source's tree-automaton language, independently algebra-checked by our earlier finite symbolic certificate.

## 10. Bounded literature check and access limits — 2026-09-18

Queries included:

- exact Johnson–Podder–Skerman title plus `infinitely many fixed points`, `finite colours`, and `tree automaton`;
- exact Rozikov–Xudayarov title and DOI;
- the polynomial signature `x^2+y^2+z^2+2yz`, `2xy`, `2xz`;
- quadratic stochastic operator / fixed-point / three-state variants;
- the older Vallander attribution terms that blocked the previous run.

Primary/current sources recovered:

1. Johnson–Podder–Skerman arXiv `1808.03019v2` / Wiley DOI `10.1002/rsa.20895`. The current arXiv HTML still contains the Section-6 question and the standing child-law assumption.
2. Rozikov–Xudayarov arXiv `2106.15958` and the journal article DOI `10.1007/s43034-021-00162-5`. A full journal PDF mirror was accessible and text extraction exposed equation (4.1) and the fixed family on its page 10 (PDF index 9). The PDF screenshot renderer was attempted as required for PDF inspection but returned an internal fetch error; no mathematical claim here depends on OCR or an unseen page because the extracted formula is also independently available in the paper's searchable text/preprint and matches the exact archived symbolic checker.

The older Vallander scope dispute is now **moot for source disposition**. I do not need to decide whether the 1972 classification already contains this orbit: the 2022 peer-reviewed paper is sufficient to establish prior art later than the 2020 source.

A bounded search is not a proof that Rozikov–Xudayarov were the first to publish the map, and I make no earliest-priority claim. The only status conclusion needed is that P0093 is no longer an open target for this fleet.

## 11. Status, counters, and audits

Frozen metric: **`D_fix = 1 -> 1`**, so there is no metric movement.

The mathematical/source-status movement is nevertheless decisive:

- before: exact affirmative construction, `PROVED-CANDIDATE / prior-art-high-risk`;
- after: **KNOWN VIA TRANSLATION** from Rozikov–Xudayarov (2022).

Metric-unchanged counter: **3 -> 4**, then terminal on this source because it is now known.  
Stuck-recovery counter: **1 -> 1**. The previous recovery selected “port the technique/source from the nearest solved QSO problem”; this run executes that recovery successfully rather than opening a second stuck episode.

Outside audits remain:

- P26: **NOT PASSED / no P0093 PASS recovered**;
- NM13-09: **NOT PASSED / newest report is an admission screen, not a P0093 audit**.

Those audits were required for claiming a **new completed result**. I do not use their absence to pretend the published 2022 construction is novel. No paper package is warranted for a source whose answer is already in the literature.

## 12. Rotation instruction for the next NM13-08 invocation

**Do not run P0093 again.** Preserve the exact construction/checker and this literature translation as the handoff record, and return NM13-08 to admission on a genuinely unassigned residue-7 `CLOSABLE OUTSIDE` source, applying all current ownership, settled/posted, and retirement exclusions.

The canonical claim file is left untouched in this worker run because claims/shared coordination are append-only ownership evidence and P26 controls shared reconciliation. P26 should record P0093 as `KNOWN VIA TRANSLATION` and no longer active research inventory.

If a future source-status audit contests the translation, the only live question is exact equivalence of the `a=0` heredity table to the source automaton; that equivalence is displayed above and independently checked. It is not permission to reopen an originality search as mathematical progress.

## 13. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-08
  category: CLOSABLE_OUTSIDE
  shard_residue_mod_13: 7
  source_id: P0093
  claim_id: P0093
  canonical_key: infinitely_many_fixed_points_of_a_finite_color_automaton
  source_status_before: OPEN_IN_SOURCE__PROVED_CANDIDATE_PRIOR_ART_HIGH_RISK
  source_status_after: KNOWN_VIA_TRANSLATION
  mathematical_status: KNOWN
  known_reference:
    authors: [U. A. Rozikov, S. S. Xudayarov]
    title: Quadratic non-stochastic operators: examples of splitted chaos
    venue: Annals of Functional Analysis
    volume_article: "13:17"
    year: 2022
    doi: 10.1007/s43034-021-00162-5
    arxiv: 2106.15958
    source_match: "equation (4.1) at a=0 equals the deterministic delta_2 three-colour automaton distributional map; published fixed family is (1/2,t,1/2-t)"
  metric:
    name: D_fix
    before: 1
    after: 1
    moved: false
  methods:
    attempted:
      - 6
      - 15
      - 26
    outcomes:
      6: "a=0 deformation endpoint exactly matches the archived P0093 map"
      15: "0/1 heredity table recovered; exact deterministic tree-automaton translation"
      26: "stochastic boundary case inside QnSO family supplies published continuum of fixed points"
  counters:
    unchanged_runs_before: 3
    unchanged_runs_after: 4
    stuck_recoveries_before: 1
    stuck_recoveries_after: 1
    terminal_on_source: true
  audits:
    p26: NOT_PASSED
    secondary_nm13_09: NOT_PASSED
    novelty_closure_claimed: false
  exact_self_check_reused:
    path: proofnet24/NM13-08/artifacts/2026-09-18/p0093_exact_checker.out
    creation_commit: ac4551b7f8d8a7a25c11755aa84b12c55f96b732
    result: ALL_EXACT_CHECKS_PASS
  literature_check:
    date: 2026-09-18
    original_source_rechecked: true
    later_primary_source_rechecked: true
    pdf_screenshot_attempt: FAILED_INTERNAL_RENDERER_ERROR
    earliest_priority_claim: false
  ownership_delta:
    new_claim_created: false
    claim_overwritten: false
    release_found: false
  artifacts_created_this_run: []
  rotation_required: true
  next_step: "next invocation: residue-7 admission for a different genuinely unassigned CLOSABLE source; never reopen P0093 absent explicit source-specific correction"
```

## 14. Write discipline

This invocation creates exactly this one immutable own-namespace report. It creates no new checker or paper folder because the mathematical map was already certified and the decisive update is prior-art identification. No canonical claim, shared root, peer namespace, source ledger, workflow, permission, public surface, email/Drive item, paid compute resource, or schedule is modified. The report is to be read back at its creation commit without a receipt-only follow-up commit.