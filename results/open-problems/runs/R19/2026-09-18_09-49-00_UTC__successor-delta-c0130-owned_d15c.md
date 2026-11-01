Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. I0084 remains frozen at `2/2`; NO MOVEMENT on active successor-admission metric `E_ready: 0 -> 0`; post-E0071 admission unchanged count `1 -> 2`; methods #2, #20, #27.**

# R19 CLOSABLE OUTSIDE — delta-only successor admission after new CLOSABLE claim activity

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity: preserve I0084 and E0071 exactly

I continued from the newest complete R19 report

`runs/R19/2026-09-18_08-37-34_UTC__successor-admission-i0074-scope-tail_a7c2.md`

rather than restarting from the native task title.

The original Hasebe--Ueda assignment I0084 remains frozen exactly as recorded in

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

Preserved facts:

- source: Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084;
- exact hypothesis: finite `(2+alpha)` moment;
- original skewness conventions retained;
- **for the frozen arXiv-v2 target, the displayed conclusion is ordinary classical convolution `mu * S_t`, even when `S_t` is the law of a free stable process**;
- retained alpha=`1/2` source-case metric: **`2/2`**;
- stronger-moment or compact-support-only results are PARTIAL, and additive Brownian / already-known stable special cases earn no new credit;
- published-version free-`boxplus` audits do not silently substitute for the frozen arXiv ordinary-`*` audit scope.

I did not alter any I0084 theorem, metric, skewness convention, or audit accounting.

E0071 / Bjorklund Problem 3 also remains on owner-side **AUDIT HOLD**. Its source statement is refuted as printed; P26 independently passed it under

`P26-AUDIT-R19-E0071-BJORKLUND-P3-ENDTOEND-40`,

while repository-wide exact-package search still recovers no genuinely distinct non-R19/non-P26 end-to-end PASS. Thus the E0071 closure gate remains `1/2`; no further R19 strengthening was attempted.

## 2. Fresh source/version check for the frozen I0084 scope

Dated check: 2026-09-18.

I re-opened the current arXiv record `https://arxiv.org/abs/1710.08240` and its experimental HTML for v2. The record still identifies v2 as the latest arXiv version, revised 14 September 2018. In the current v2 HTML, Conjecture 5.5 literally says:

- `S_t` is the law of a **classical or free** alpha-stable process;
- under the `(2+alpha)` moment condition;
- `mu * S_t` is unimodal for sufficiently large `t`.

So the frozen ordinary-`*` reading is not a transcription artifact in the R19 handoff: it is still what the current arXiv-v2 HTML displays.

I also checked the published ALEA rendering surfaced by current search. Its displayed formulation distinguishes the branches and writes classical convolution for the classical stable law and free convolution for the free stable law. Therefore the source-version distinction is real and must stay explicit: this R19 handoff is intentionally the **arXiv-v2 ordinary-`*`** target, not an implicit replacement by the published free-`boxplus` branch.

A bounded current search using the exact paper title/arXiv number, `Conjecture 5.5`, stable-process unimodality, and later Hasebe/Ueda work surfaced the original paper and later multiplicative-unimodality work, but no later primary source explicitly announcing a resolution of this exact frozen arXiv-v2 ordinary-`*` formulation. This is bounded negative evidence only, not a novelty or worldwide-openness certificate.

## 3. Required repository delta since the previous R19 report

The previous R19 report was created at commit

`85fa9f37e1591ba360bbe5f381a547e67448e6ab`.

A fresh compare from that commit to current `master` showed a large concurrent delta. I did not infer freedom from missing claim files; I inspected the material admission/ownership changes.

The key new CLOSABLE event is **C0130**:

- source: Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, Problem 3.12;
- current admission record classifies it `CLOSABLE OUTSIDE (qualified)`;
- however, it was immediately create-only claimed by **R7-05** in `operations/claims/C0130.md`.

Thus C0130 is evidence that the discovery machinery is producing a genuine CLOSABLE source, but it is **not available to R19**.

The newest independent CLOSABLE admission/release screen I recovered also checked two superficially tempting terminal handoffs:

- `E0010`: source remains open/partial, but the canonical claim is explicitly retained; terminal handoff is **not** an ownership release;
- `D0004`: source remains open, but no owner-authorized release was recovered and the canonical claim remains controlling.

The same current screens report:

- `I0130`: claimed elsewhere;
- no populated `I0131+` source row recovered;
- no populated Codex `P0489+` source row recovered;
- no candidate crossed the strict `READY + CLOSABLE + ownership-clear` gate in the newest coordinator delta;
- new claims only shrink free inventory; they do not constitute releases.

A final pre-write refresh of current `master` showed only ongoing research/report commits, not a new owner-authorized R19-eligible release.

## 4. Method #2 — ATTACK THE NEGATION FIRST

I tried to falsify the predecessor conclusion `E_ready=0` rather than assume the gate was still empty.

The strongest falsification candidate is the newly admitted C0130 because it has already passed a genuine CLOSABLE classification. If the predecessor conclusion were stale in the useful direction, C0130 would be exactly the kind of row that should witness it.

It fails the R19 admission conjunction at the ownership predicate: R7-05 created the canonical claim immediately. I then tested the other new-looking CLOSABLE events E0010 and D0004. Both fail for the same logically independent reason: a research handoff is not a release, and neither has an owner-authorized transfer to unassigned reserve/R19.

**Outcome:** the negation attack found real new CLOSABLE inventory, but every such candidate is already owned. It does not move `E_ready`.

## 5. Method #20 — FIND WHY THE ALGORITHM FAILS

The naive successor algorithm

`take the newest problem that is CLOSABLE or whose previous worker handed it off`

is invalid. The precise missing step is **post-classification ownership clearance**.

C0130 demonstrates the admission branch: a problem may become genuinely CLOSABLE and still be unavailable because another worker wins the create-only claim race. E0010 and D0004 demonstrate the handoff branch: a worker may stop ordinary research while the canonical owner record survives, so the source is not automatically returned to reserve.

The correct admission predicate remains

`source-exact AND current-undecided AND genuinely-CLOSABLE AND ownership-clear AND not posted/retired/known`.

Current delta candidates fail the fourth predicate. This is why repeated queue scanning without release semantics produces false vacancies.

**Outcome:** obstruction sharpened; no source admitted.

## 6. Method #27 — SWAP THE QUANTIFIERS

The current repository now satisfies

`there exists x such that x is newly admitted CLOSABLE`,

witnessed by C0130.

What R19 needs is the stronger and differently quantified statement

`there exists x such that x is newly/currently CLOSABLE AND x is ownership-clear for R19`.

The first statement does not imply the second. Likewise,

`there exists a CLOSABLE worker that handed off x`

does not imply

`there exists an ownership release of x`.

C0130, E0010, and D0004 give concrete current-delta witnesses separating these quantifiers.

**Outcome:** the delta contains progress at fleet level but no R19-dispatchable successor.

## 7. Active metric and status

The active post-E0071 admission metric remains

`E_ready` = number of source-clean, current-undecided, genuinely CLOSABLE, ownership-clear outside successors R19 can lawfully claim now.

Before: `0`.  
After: `0`.

Therefore:

- movement: **NO MOVEMENT**;
- post-E0071 admission unchanged count: **`1 -> 2`**;
- R19 state: **`SUCCESSOR_ADMISSION_REQUIRED`**;
- no canonical claim created;
- no theorem-sized mathematical claim made;
- no finite claim made;
- no checker-only artifact manufactured.

This is not yet the three-consecutive-no-movement stuck trigger for the post-E0071 admission gate. If the next ordinary admission run is also unchanged, the supported count becomes three; the invocation after that must follow the Section-I thinking-only stuck protocol.

The durable next action remains **delta-only**. Do not repeat the completed I0074/Towsner scope analysis, the P0482--P0488 classification, or static queue scans absent a material change. Re-enter full dispatch only on a newly populated source row, a genuine READY certification, an explicit owner-authorized non-exhausted release/transfer, or a material current-status correction. Any candidate must still pass exact-source, current literature/later-author/citing, prior-attempt, posted exclusion, and exclusive-ownership checks before create-only claiming.

## 8. Model / reasoning / scheduler boundary

The requested GPT-6/maximum setting is still not enforceable from the exposed worker/scheduler surface. The available task controls expose title/prompt, schedule or relative-start fields, timing mode, and enabled state, but no binding model-family selector, no binding reasoning-effort selector, no guaranteed hour-long execution field, and no authenticated applied-run model receipt.

Actually enforcing and verifying GPT-6/maximum requires an owner-authorized product/workspace/API/admin surface that exposes persistent model/reasoning controls plus authenticated per-run attestation, or platform support.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary. Repository follow-up records a later successful P26 update from an authorized P/C context. The lawful workaround is the owning/authorized context or platform/admin support, never cloning the task or bypassing permissions. No scheduler mutation was attempted in this run.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  lane: CLOSABLE_OUTSIDE
  preserved_origin:
    source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / I0084"
    convolution: "ordinary classical mu * S_t in the frozen arXiv-v2 formulation, including when S_t is a free-stable-law distribution"
    metric_name: "complete classical-stable/free-stable alpha=1/2 source cases"
    metric_value: "2/2"
    status: FROZEN_HANDOFF_PRESERVED
  frozen_source_recheck:
    date: 2026-09-18
    arxiv_current_version: v2
    arxiv_last_revised: 2018-09-14
    arxiv_display: "classical or free stable S_t; conclusion mu * S_t"
    published_version_difference: "ALEA display distinguishes classical * and free boxplus branches; do not substitute it for frozen arXiv scope"
    later_resolution_found: false
    caveat: "bounded negative search only"
  predecessor_hold:
    target: E0071
    status: "R19_RESEARCH_AUDIT_HOLD / SOURCE_REFUTED_AS_PRINTED"
    audits:
      P26:
        id: P26-AUDIT-R19-E0071-BJORKLUND-P3-ENDTOEND-40
        verdict: PASS
      distinct_other: MISSING
  active_gate:
    target: "admit next source-clean, current-open, ownership-clear CLOSABLE outside successor"
    metric: E_ready
    before: 0
    after: 0
    movement: NO_MOVEMENT
    unchanged_count_before: 1
    unchanged_count_after: 2
    status: SUCCESSOR_ADMISSION_REQUIRED
  methods_this_run: [2, 20, 27]
  delta_screen:
    C0130: "NEWLY_ADMITTED_CLOSABLE_QUALIFIED / CLAIMED_R7-05 / NOT_FREE_FOR_R19"
    E0010: "CLOSABLE_HANDOFF / CLAIM_EXPLICITLY_RETAINED / NO_RELEASE"
    D0004: "CLOSABLE_HANDOFF / NO_OWNER_AUTHORIZED_RELEASE / CLAIM_CONTROLLING"
    I0130: "CLAIMED_ELSEWHERE"
    I0131_plus: "NO_POPULATED_SOURCE_ROW_RECOVERED"
    P0489_plus: "NO_POPULATED_SOURCE_ROW_RECOVERED"
  source_status_check_date: 2026-09-18
  evidence:
    - "runs/R19/2026-09-18_08-37-34_UTC__successor-admission-i0074-scope-tail_a7c2.md"
    - "artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md"
    - "operations/claims/C0130.md"
    - "proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T09-25-00Z__successor-admission-release-gate-delta.md"
    - "proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_10-00-00__run-report.md"
  remaining_obligation: >-
    On a material repository/status delta, certify one genuinely READY + CLOSABLE +
    ownership-clear outside source and claim it create-only. Otherwise preserve the
    gate honestly; one further ordinary no-movement run reaches the three-run
    stagnation threshold and makes the following invocation a Section-I thinking run.
```

No shared root ledger, peer file, prior report, existing claim, email/Gmail item, Drive object, public surface, purchase, credential, permission, workflow, or scheduler state was modified.