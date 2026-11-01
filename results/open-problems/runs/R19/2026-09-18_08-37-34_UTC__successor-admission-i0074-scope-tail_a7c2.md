Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. I0084 remains frozen at `2/2`; NO MOVEMENT on the active successor-admission metric `E_ready: 0 -> 0` (post-E0071 admission unchanged count `0 -> 1`); methods #4, #17, #26.**

# R19 CLOSABLE OUTSIDE — successor admission after E0071 audit hold

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity: do not reopen I0084 or E0071

I continued from the newest R19 immutable report,

`runs/R19/2026-09-18_07-38-41_UTC__e0071-stuck1-audithold_5c9a.md`,

rather than restarting from the native task title.

That report completed mandatory STUCK1 for E0071, recorded the independent P26 PASS, placed E0071 on owner-side **AUDIT HOLD**, and explicitly chose the Section-I action **MOVE TO THE NEXT PROBLEM IN QUEUE AND RECORD THE SWITCH**. I therefore did not add another E0071 theorem or checker. Its owner proof and P26 audit remain preserved; the distinct non-R19/non-P26 end-to-end audit is still a separate closure obligation.

The original Hasebe--Ueda I0084 assignment remains frozen exactly as preserved in

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

Preserved I0084 facts are unchanged:

- source: Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084;
- exact hypothesis: finite `(2+alpha)` moment;
- original classical/free stable-law and skewness conventions are retained;
- **the frozen arXiv-v2 conclusion is ordinary classical convolution `mu * S_t`, even when `S_t` is the law of a free-stable distribution**;
- retained `alpha=1/2` source-case metric: **`2/2`**;
- stronger moment conditions, compact support only, additive Brownian results, and already-known stable special cases earn no new credit;
- ALEA free-`boxplus` audits do not substitute for audits of the frozen ordinary-`*` arXiv scope.

I did not alter any I0084 theorem, metric, status, or audit accounting.

## 2. Required repository refresh and active metric

This is the first ordinary successor-admission run after the E0071 STUCK1 switch, so I use the admission metric

`E_ready` = number of source-clean, current-open, genuinely CLOSABLE, ownership-clear outside successors that R19 can lawfully claim now.

Before: `0`.  
After: `0`.

I reread/recovered the controlling repository surfaces before screening:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and the latest implementation/deployment state;
- the newest R19 report above and the frozen I0084 handoff;
- current canonical claim paths for candidates actually screened;
- recent neighboring successor/admission reports;
- targeted `probability_1000_intake_*/problems.jsonl` and Codex records.

The current queue remains a candidate/history surface, not a dispatch permission list. The newest gate reports still show no free `READY + CLOSABLE + UNASSIGNED` successor, and the post-P0481 Codex cursor still has no populated `P0489+` row. I therefore advanced the *quality of the admission diagnosis* rather than inventing a source.

Large intake ledgers cannot be rendered byte-for-byte in one connector response. I used exact-ID/source searches and targeted reads and do not claim otherwise.

## 3. #4 PROVE SOMETHING WEAKER, COMPLETELY — settle the I0074 admission subproblem

The most plausible unclaimed-looking queue exception remains I0074, David Aldous, *Note: a conjectured compactification of some finite reversible MCs*, Conjecture 1. Current repository evidence still returns it to reserve and no canonical `operations/claims/I0074.md` is present. The unresolved question was whether Towsner's 2015 limit theory actually makes the original Aldous statement KNOWN, or whether a source-valid counterexample makes it REFUTED.

Rather than attempting the full compactification problem, I completed the narrower admission question from the primary texts.

### Aldous's exact source is scope-underdetermined

Primary source checked on 2026-09-18:

David Aldous, *Note: a conjectured compactification of some finite reversible MCs*,
`https://www.stat.berkeley.edu/~aldous/Talks/MCcompact.pdf`.

In Section 0.3 Aldous considers symmetric stationary transition densities satisfying Chapman--Kolmogorov together with

> `a UTC on the t downarrow 0 behavior`,

and footnote 1 says literally

> `unspecified technical condition`.

He then forms the function-valued density array `Psi`, defines process isomorphism using a state-space bijection preserving the stationary two-time laws/transition densities, and states:

`Conjecture 1. If two symmetric Markov processes have the same Psi then they are isomorphic.`

Thus the exact admissible process class is not actually specified in the source: the small-time condition intended to exclude pathologies is left open.

### Towsner proves canonicalized uniqueness, but explicitly disproves raw uniqueness in his pseudofinite class

Primary/current source checked:

Henry Towsner, *Limits of Sequences of Markov Chains*, arXiv:1404.3815 / EJP 20 (2015), Section 7.

Towsner explicitly writes that one would like a pseudofinite Markov chain to be determined by its density array, but **`This is not the case, as an easy example shows.`** He gives a two-point chain and a non-isomorphic version obtained by replacing one atom with an uncountable rapidly mixing `blob`; they have the same density array. He then defines **twin-free** and **saturated** representatives. Lemma 7.3 maps every pseudofinite chain to a twin-free saturated representative preserving the kernels through the type map, and Theorem 7.5 proves uniqueness up to null sets for twin-free saturated pseudofinite chains with the same density array and the stated minimal-sigma-algebra condition.

So the exact logical picture is now sharp:

1. **Unqualified same-density-array uniqueness is false** in Towsner's pseudofinite class.
2. **Canonicalized twin-free/saturated uniqueness is true** under Towsner's conditions.
3. Aldous's literal Conjecture 1 inserted an **unspecified** `t downarrow 0` technical condition, so we cannot lawfully infer that Towsner's blob example satisfies Aldous's intended source class.
4. Conversely, we cannot lawfully infer that Aldous's intended but unstated UTC is exactly equivalent to Towsner's twin-free/saturated canonicalization.

Aldous's current compactification status page says Towsner gives a measure-theoretic limit construction while a version with nice topological properties remains open. Aldous's later 2018 slides likewise describe Towsner as proving the compactification only in a **weak form**.

### Admission conclusion for I0074

I0074 is therefore more precisely classified, for dispatch purposes, as

`UNASSIGNED_RESERVE / PENDING_SOURCE_REPAIR_UNSPECIFIED_UTC / NOT_READY`.

This is an admission/scope diagnosis, not a theorem claim about a repaired conjecture. I do **not** call the original statement REFUTED, because its author explicitly left a technical condition unspecified and that condition might exclude Towsner's blob pathology. I do **not** call it KNOWN, because Towsner's theorem proves uniqueness only after canonicalization/additional hypotheses and Aldous himself describes the later result as measure-theoretic/weak.

This closes the narrow admission question sufficiently to reject I0074 as a lawful R19 CLOSABLE successor unless and until an exact repaired source scope is supplied.

## 4. #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE — compare the Codex tail with later techniques

I next checked the unclaimed-looking late Codex block P0482--P0488 against the current source/literature and neighboring admission screens rather than assuming a 404 claim path means a free CLOSABLE problem.

The block is Drewitz--Ramírez, *Selected Topics in Random Walks in Random Environment* (2013/2014):

- P0482: ballisticity versus an absolutely continuous invariant environment law;
- P0483: directional transience implies positive speed under iid uniform ellipticity;
- P0484: literature-resolved / excluded;
- P0485: transience of every elliptic iid nearest-neighbor RWRE on `Z^d`, `d>=3`;
- P0486: directional zero-one law beyond the plane;
- P0487: positive velocity implies quantitative ballisticity condition `(P)_M`;
- P0488: resolved by Guerra--Ramírez's `(T')` versus `(T)` theorem.

The later techniques found in current sources—ballisticity criteria, regeneration theory, the Guerra--Ramírez equivalence of quantitative ballisticity conditions, stationary/balanced special cases, and recent homogenization/local-deviation work—solve or sharpen restricted branches but do not turn P0482/P0483/P0485/P0486/P0487 into finite/source-wide CLOSABLE endpoints. Current neighboring screens independently classify P0485 and P0486 as HARD-shaped, and the same mechanism issue applies to P0487.

Outcome: the later literature explains why these are important but **not** appropriate replacements for a CLOSABLE lane. No metric was frozen for them and no claim was created.

## 5. #26 HUNT THE SPORADIC CASE — exact unclaimed-looking survivors

I specifically hunted the apparently free exceptions instead of stopping at the queue headline.

### I0074

No canonical claim, but fails readiness because the source class contains an unspecified technical condition and the Towsner comparison does not fix that source ambiguity. **Not READY.**

### P0485

Direct canonical claim path is absent at this snapshot, but the source asks for universal transience over every iid elliptic law in every `d>=3`; a positive solution is a universal theorem and a negative solution requires an explicit recurrent iid elliptic law. Recent R7 screening correctly classifies it **HARD OUTSIDE**, not CLOSABLE. **Not READY for R19.**

### P0486

Direct canonical claim path is absent at this snapshot, but the higher-dimensional directional zero-one law is a source-wide structural RWRE problem. Recent NM13 screening explicitly classifies it **HARD-shaped, not CLOSABLE**. **Not READY for R19.**

### P0487

Direct canonical claim path is absent at this snapshot, but positive speed -> `(P)_M` under iid uniform ellipticity is another global implication requiring self-improvement of regeneration/slab tails; the existing non-nestling special case does not close the source. **HARD, not CLOSABLE.**

### P0489+

Current repository searches still find `P0489` only as a future-cursor/`next_id` marker and in prior admission-screen prose. There is no populated canonical P0489+ source row to claim.

No sporadic candidate survives all mandatory predicates simultaneously.

## 6. Current-source / later-author / citing-literature log

Dated 2026-09-18.

Fresh searches/readbacks included:

- Aldous exact Conjecture-1 source PDF and current `compact.html` status page;
- Towsner arXiv:1404.3815, especially Section 7 non-uniqueness example, Lemma 7.3, and Theorem 7.5;
- Aldous 2018 slides describing Towsner's result as a weak-form compactification;
- Drewitz--Ramírez RWRE open-question block and later ballisticity/transience literature, including Guerra--Ramírez's proof of Sznitman's `(T')` conjecture;
- the original Hasebe--Ueda I0084 arXiv identity and later Hasebe--Ueda unimodality work, only to check that the frozen handoff is not being contradicted by an obvious later source.

No later primary source found in this bounded search supplies a source-exact repaired UTC for I0074 or makes one of P0485/P0486/P0487 a small CLOSABLE source case. These are bounded negative/current-status findings, **not** novelty certificates or exhaustive worldwide literature claims.

Access limitation: web/index/citation-graph and repository evidence only; no private author correspondence was used or attempted.

## 7. Admission result

No candidate inspected satisfies all five dispatch predicates simultaneously:

`exact sourced scope` + `current-open/undecided status` + `full-source CLOSABLE shape` + `ownership clearance` + `no posted/retired/known exclusion`.

Therefore

`E_ready: 0 -> 0`.

Because E0071 was moved to audit hold in the preceding STUCK1 run, this is the first ordinary no-movement run of the **post-E0071 admission gate**:

`unchanged count: 0 -> 1`.

R19 remains

`SUCCESSOR_ADMISSION_REQUIRED`.

This is not yet a three-run stuck state. No theorem-sized mathematical claim or finite exhaustive claim was produced, so I did not manufacture a checker-only artifact merely to prove that admission screening ran.

The next run should be **delta-only**: first inspect any newly populated source row, explicit release, coordinator admission, or material current-status change since this report. Do not repeat the completed I0074/Towsner scope analysis or P0482--P0488 classification absent such a change. If a genuinely READY + CLOSABLE + UNASSIGNED target appears, claim it create-only and begin research in the same run.

## 8. Model / reasoning / scheduler boundary

The requested GPT-6/maximum setting is still not enforceable from the exposed worker/scheduler surface. The available controls expose task prompt/title, schedule or start offset, timing mode, and enabled state, but no binding model-family selector, no reasoning-effort selector, no guaranteed one-hour execution field, and no authenticated applied-run model receipt.

Actually changing and verifying this would require an authorized product/backend control that exposes those fields plus runtime attestation, or platform support. No scheduler mutation was attempted because the owner explicitly forbids scheduler changes in this task.

The historical P26 `You cannot modify this task` event remains an authorization-context issue. Repository follow-up records a later successful P26 update from an authorized P/C context. The lawful workaround is therefore the owning/authorized context or platform support, not duplicate-task creation, account/tool switching, or permission bypass.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  lane: CLOSABLE_OUTSIDE
  preserved_origin:
    source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / I0084"
    convolution: "ordinary classical mu * S_t, including when S_t is a free-stable-law distribution"
    metric_name: "complete classical-stable/free-stable alpha=1/2 source cases"
    metric_value: "2/2"
    status: FROZEN_HANDOFF_PRESERVED
  predecessor_hold:
    target: E0071
    status: "R19_RESEARCH_AUDIT_HOLD / P26_PASS / SECOND_DISTINCT_AUDIT_PENDING"
  active_gate:
    target: "admit next source-clean, current-open, ownership-clear CLOSABLE outside successor"
    metric: E_ready
    before: 0
    after: 0
    movement: NO_MOVEMENT
    unchanged_count_before: 0
    unchanged_count_after: 1
    status: SUCCESSOR_ADMISSION_REQUIRED
  methods_this_run: [4, 17, 26]
  candidates:
    I0074:
      owner_state: UNASSIGNED_RESERVE
      status: PENDING_SOURCE_REPAIR_UNSPECIFIED_UTC
      readiness: NOT_READY
      key_evidence: "Aldous source leaves t-downarrow-0 UTC unspecified; Towsner gives a same-density-array non-isomorphism example before proving twin-free/saturated canonical uniqueness"
    P0485: "UNCLAIMED-LOOKING / HARD_OUTSIDE / NOT_R19_CLOSABLE"
    P0486: "UNCLAIMED-LOOKING / HARD_OUTSIDE / NOT_R19_CLOSABLE"
    P0487: "UNCLAIMED-LOOKING / HARD_OUTSIDE / NOT_R19_CLOSABLE"
    P0489_plus: "NO_POPULATED_CANONICAL_SOURCE_ROW_RECOVERED"
  source_status_check_date: 2026-09-18
  remaining_obligation: "on a material repository/status delta, certify one genuinely READY + CLOSABLE + ownership-clear outside source and claim it create-only; otherwise preserve SUCCESSOR_ADMISSION_REQUIRED"
  evidence:
    - "runs/R19/2026-09-18_07-38-41_UTC__e0071-stuck1-audithold_5c9a.md"
    - "artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md"
    - "runs/R19/2026-09-18_02-14-29_UTC__successor-gate-live-reconciliation_2f61.md"
    - "research7_2026-09-17/R7-03/runs/2026-09-18/2026-09-18T082626Z__report.md"
    - "probability_campaign_2026_09/report_2026-09-12/chapters/catalog_04_codex_P0451_P0590.md"
  audits: []
  artifact_refs: []
  shared_root_edits: NONE
  peer_edits: NONE
```

No Gmail/email, Drive, public posting, purchase, paid compute, permission change, scheduler change, workflow execution, force-push, shared-root edit, peer-file edit, or duplicate claim was performed.

END OF IMMUTABLE R19 REPORT
