Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this was not GPT-6 at maximum; GPT-6/maximum was requested, but the exposed runtime provides no authenticated model-family/reasoning-effort receipt. **AUDIT GATE UNCHANGED: `T_CI241 1 -> 1`; independent full-proof audits `0/2 -> 0/2`; no new theorem/checker claim.**

# P20 — Fokam–Bitjoka Conjecture 2.41 audit-recovery report

Date: **2026-09-18 UTC**.  
Repository: `yspennstate/math-open-problems`, branch `master`.  
Category: **CLOSABLE OUTSIDE / SOURCE-LITERAL YES PROOF CANDIDATE / AUDITS PENDING**.

## 1. Continuity and controlling state

I continued from the canonical P20 proof-candidate report rather than restarting the mathematics:

`proofnet24/P20-closure-log-unimodality/successors/FOKAM-BITJOKA-2026-CYCLIC-INTERVAL/runs/2026-09-18/2026-09-18T06-13-00Z__run-report.md`

at creation commit `ed6e0a90cf05accdbf3b617137ac80762091778b`, verified blob `6bbf365cb4f5aded37f798d5c3b7b9c81b5fad8e`.

The frozen source metric remains

`T_CI241 = 1`, target `1`,

with proof candidate

`P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01`.

Before any action I reread/recovered campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FLEET_2026-09-16.md`, `operations/NEW_METHODS_2026-09-16.md`, the canonical Fokam–Bitjoka claim, the canonical proof report, the exact supplementary checker/output, the newest recovered P19 state, the newest recovered P26 report, the newest P21 state, and the freshest coordinator/task-health state. No retired P20 predecessor was reopened.

## 2. Exact proof candidate preserved, not re-proved

The exact source statement remains:

> for every odd integer `m` and every nonempty proper `x subset Z_m`, there exists a cyclic interval `W subset Z_m` such that
>
> `|W triangle x| < min(|W|,m-|W|)`.

The canonical proof writes `m=2h+1`, chooses the odd-cardinality side `Y` among `x,x^c`, sets `s=|Y|`, and double-counts incidences with the `m` cyclic intervals of length `h`:

`sum_t |I_t cap Y| = h s = s(m-1)/2 > m(s-1)/2`.

Hence some `I` contains strictly more than `s/2` points of `Y`. If `Y=x`, take `W=I`; if `Y=x^c`, take `W=I^c`. In both cases the source inequality is strict. The stronger prescribed-length conclusion is unchanged: `|W|=h` when `|x|` is odd and `|W|=h+1` when `|x|` is even.

The supplementary exact sanity artifacts remain unchanged and are not counted as the universal proof:

- checker @ `5bd30c46a709989496d5b84410896ef835f056c9`, blob `80b0c0e0bd2d27b076132bfefa325769f07b8c27`;
- output @ `9ecfcce03409512f7c8b4b1e7287969fc24c120d`, blob `e32bf3e4066ee6c4652001a0e7ec1e426a3a7844`;
- output ends `P20-CI241-SEMICIRCLE-SANITY: ALL_EXACT_CHECKS_PASS` after `699030` exact subsets for odd `m<=19`.

No additional P20 self-check, theorem, witness, or checker was created in this audit-recovery run.

## 3. Fresh P26 audit search — still absent for CI241

Repository-wide searches for the exact proof ID

`P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01`

and for combinations of `CI241`, `FOKAM`, `BITJOKA`, `P26`, `P19`, `audit`, and `semicircle` recovered only the P20 claim/admission/proof material, not an independent audit report.

A genuinely newer P26 report exists after the P20 proof candidate:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_10-00-00__run-report.md`

at creation commit `b3272e967779946ca1aad32f7dbfbef1d3548dc1`.

It audits **R19 / E0071 / Björklund Problem 3**, with audit ID

`P26-AUDIT-R19-E0071-BJORKLUND-P3-ENDTOEND-40`,

not P20's Fokam–Bitjoka proof. Therefore it contributes **zero** to the CI241 audit count.

No P26 full-proof/source-quantifier audit of `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01` was recovered in this bounded repository pass.

## 4. Fresh distinct-OTHER audit search — P19 still absent for CI241

No P19 report or commit dated 2026-09-18 was recovered in the current repository search, and no P19 audit of CI241 was found by exact-proof-ID or source-name searches.

The newest recovered P19 material relevant to P20 remains the earlier independent D0072 audit from 2026-09-17,

`proofnet24/P19-closure-smr-optimal/runs/2026-09-17/2026-09-17T17-56-34Z__rotation-hold-d0072-audit.md`

at creation commit `8debd604cb2090d04a64564ba6d29a8d70198bde`.

That audit is for Grimmett–Li Question 4.5 / D0072 and cannot be reused for CI241. Thus the distinct OTHER-track CI241 audit is also still missing.

Current independent audit count therefore remains exactly:

`0/2`.

P20's own continuity reread found no defect in the averaging proof, but a P20 reread is a **self-check**, not an OTHER-track audit, and is not counted.

## 5. Fresh literature/current-status recheck

Dated **2026-09-18**. Fresh bounded web queries included:

- exact primary title plus `2606.29391`;
- `"2606.29391" "Conjecture 2.41"`;
- `"2607.07939" Fokam Bitjoka "cyclic interval"`;
- `"cyclic interval conjecture for odd cycles" Fokam Bitjoka`.

The searches recovered the 28 June 2026 primary arXiv record, the July 2026 same-author companion/reduction, and the current MathDB entry. MathDB still describes the general cyclic-interval statement as open, records the source's bounded verification through odd `m<=17`, and lists no solution. The July companion still describes the arbitrary odd-cycle result as depending on/reduced to the cyclic-interval lemma.

No later source-matching published proof or counterexample was recovered in this bounded pass. These misses are **bounded negative evidence only**. Publication novelty and exhaustive worldwide openness remain **UNVERIFIED**. No public posting is claimed.

## 6. P21 directed second-audit duty

The newest recovered P21 state remains

`proofnet24/P21-closure-mub-sos/runs/2026-09-17/2026-09-17T18-15-00Z__rotation-hold-refresh.md`

at commit `e3f7e538c3d129ad83e5eabfc9736d28b12d672b`.

It is a rotation-hold/admission report and explicitly makes no new theorem/checker claim. Therefore P20 creates no directed P21 audit receipt in this run.

## 7. Fresh task-health state

The newest recovered coordinator reconciliation is

`operations/task_health/runs/2026-09-18T065500Z/status.md`

created at commit `f6a8a366a534ab3dbea1764c81946ac5837d9503`.

It records current fleet health/admission state but does not record either required CI241 audit or shared-ledger closure of this source. No root-ledger change is inferred from scheduler/configuration state.

## 8. Closure disposition

There is no substantive defect to repair and no qualifying outside audit to count. Accordingly:

- `T_CI241` stays `1 -> 1`;
- exact mathematical status stays `SOURCE_LITERAL_YES_PROOF_CANDIDATE`;
- supplementary exact sanity stays `PASS`;
- independent audit count stays `0/2`;
- closure package remains **NOT BUILT**;
- source remains **ACTIVE / AUDITS PENDING**, not retired;
- publication novelty remains **UNVERIFIED**.

P20 made no edit to shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md`.

```yaml
ledger_delta:
  worker: P20
  lane: CLOSABLE_OUTSIDE
  source:
    id: FOKAM-BITJOKA-2026-CYCLIC-INTERVAL
    status: SOURCE_LITERAL_YES_PROOF_CANDIDATE_AUDITS_PENDING
    proof_id: P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01
  metric:
    name: T_CI241
    before: 1
    after: 1
    target: 1
  audits:
    independent_required: 2
    before: 0
    after: 0
    p26_ci241: MISSING
    distinct_other_ci241: MISSING
    newest_p26_report_seen: proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_10-00-00__run-report.md
    newest_p26_target: R19_E0071_NOT_CI241
    request_p26: FULL_PROOF_SOURCE_QUANTIFIER_AUDIT
    request_p19: FULL_PROOF_SOURCE_QUANTIFIER_AUDIT
  literature:
    checked_utc_date: 2026-09-18
    later_source_matching_resolution_recovered: false
    evidence_scope: bounded_negative_only
    novelty: UNVERIFIED
  p21_directed_audit:
    new_p21_mathematical_claim_found: false
    receipt_created: false
  package:
    closure_package_built: false
    reason: independent_audits_0_of_2
  shared_root_edits: none
  email_drive_public_posting: none
```

## 9. Next-run continuity

**Audits first again.** Search for a new P26 full-proof/source-quantifier audit and a genuinely distinct OTHER-track audit, naturally P19, of `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01`. Read any found audit at its creation commit. If both independent audits PASS, immediately build/read back the narrow self-contained Conjecture 2.41 closure package, request shared-ledger closure through `ledger_delta`, retire the source, and rotate in that same run. If the audits are still absent, do not manufacture another P20 theorem, checker, or self-audit.

**End of P20 CI241 audit-recovery report.**