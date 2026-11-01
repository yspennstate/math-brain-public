Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO R01 SOURCE-METRIC MOVEMENT: Aldous–Fill I0024 remains `C=1`, already audit-complete; TFIK22 remains owner-side `R_TFIK22=0` with `1/2` independent audits. CURRENT-OWNER-POLICY MOVEMENT: the 2026-09-20 PROGRESS20 deployment supersedes the old R01 audit/intake/rotation loop and does not include R01 in LIVE20. Methods #3 PROVE SOMETHING STRONGER, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #29 ADD THE POINTS AT INFINITY.**

# R01 supersession / handoff report — 20 September 2026

Repository / branch: `yspennstate/math-open-problems` / `master`.
Role: R01 historical CLOSABLE OUTSIDE worker.

## 1. Exact recovered mathematical state

The canonical I0024 claim remains `operations/claims/I0024.md`, owned by R01, source David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 3.44. The live Aldous–Fill Chapter 3 page still asks whether relaxation time has a characterization **exactly as an infimum over flows**, distinguishing that from the known nonexact Chapter-4 flow upper bound.

The frozen R01 theorem remains

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

on the original finite irreducible reversible-chain domain, with fixed metric

\[
C_{\min}=1.
\]

The qualifying independent audits remain

- `R20-AUDIT-R01-I0024-03 = PASS`;
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS_FULL_MATHEMATICAL_PROOF`.

Thus I0024 remains `PROVED / AUDIT-COMPLETE / FROZEN`. Exact equality leaves no smaller multiplicative distortion to pursue.

The historical R01 successor TFIK22 also remains unchanged. Current repository search still finds the qualifying P26 audit

`P26-AUDIT-R01-KMO2026-TFIK22-RESIDUE-68 = PASS_FULL_MATHEMATICAL_PROOF`

and no distinct `R20-AUDIT-R01-KMO...` completion. Hence its state is still

`CANDIDATE_COMPLETE / R_TFIK22=0 / 1_OF_2_AUDITS / NOT_CLOSED`.

No owner-side recheck can fill that independent slot.

## 2. New controlling owner policy supersedes the old R01 loop

I read the newer owner policy `operations/PROGRESS20_2026-09-20.md` and its deployment receipt `operations/PROGRESS20_2026-09-20_DEPLOYMENT.md`.

That policy explicitly says it supersedes conflicting compulsory audits, whole-repository rereading, intake-only loops, thinking-only stagnation rules, and unrelated automatic rotation in older prompts. Its verified LIVE20 contains exactly P01, P02, P03, P04, P13, P20, P26 and NM13-01 through NM13-13. R01 is not a LIVE20 assignment. The deployment receipt further records that no primary audit-only or intake-only job remains in the final active set.

Therefore the correct R01 action is preservation/handoff, not another neighboring audit, another empty CLOSABLE admission scan, or an invented successor. This is a configuration reconciliation, not mathematical progress.

There is a native-state inconsistency worth preserving explicitly: the presently exposed scheduler list still shows the historical R01 schedule as enabled even though the repository's newer verified LIVE20 deployment excludes it. This report does not reinterpret that stale native state as mathematical authorization to continue the superseded R01 portfolio.

## 3. Three fresh method probes

### #3 PROVE SOMETHING STRONGER

I tested whether there was a legitimate stronger source-adjacent theorem to pursue without reopening the solved metric. The natural strengthening is an abstract minimum-energy right-inverse theorem behind

\[
R_*=CB^TL^+.
\]

That operator statement is useful explanatory structure, but it cannot improve the fixed source metric below `C=1`; claiming movement would therefore be false. Extending the theorem to a different chain class would be a new scope and requires separate admission rather than silently changing I0024.

**Outcome:** no source-level movement; do not reopen I0024.

### #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

Dated bounded search on 2026-09-20 used the exact source phrase `relaxation time exactly an inf over flows`, variants with `spectral gap`, `right inverse`, `divergence`, and `Markov chain`. The maintained Aldous–Fill HTML still states Open Problem 3.44 verbatim. The search did not locate an indexed later paper explicitly announcing resolution of the numbered problem by this formula. Closely related right-inverse/divergence principles exist in other areas, so **publication priority remains UNVERIFIED**; absence from this bounded search is not a novelty certificate.

**Outcome:** source page remains textually open; no priority claim.

### #29 ADD THE POINTS AT INFINITY

I checked the most obvious boundary extension: singular/reducible limits of the reversible-chain operator. Those limits leave the source's finite irreducible domain, may make the mean-zero Laplacian inverse nonunique/infinite across communicating classes, and therefore cannot count as improvement of the frozen I0024 metric. Any such extension would need its own exact statement and ownership.

**Outcome:** boundary extension rejected as invalid source-metric movement.

## 4. Scheduler/model-control reconciliation

The currently exposed task-control surface still has no binding model-family selector or reasoning-effort selector. It exposes task text/title, schedule/timing, enablement and timing mode; there is no authenticated applied-model/effort receipt or guaranteed execution duration. The newer PROGRESS20 deployment states the same limitation. Therefore `GPT-6 / maximum` remains a prompt request only on this surface.

The historical P26 `You cannot modify this task` event was an authorization-context failure, not evidence of a universal inability to update P26: later authorized native updates succeeded. A binding model/effort fix would require an authorized product/workspace/API/admin scheduler surface exposing persistent model and reasoning fields plus runtime attestation. Prompt text cannot enforce it.

## 5. Handoff

R01 should not generate more audit-only work or queue scans under the superseded portfolio. Preserve:

1. I0024: `C=1`, proved, two independent audits, frozen.
2. TFIK22: owner-side complete at `R_TFIK22=0`, one qualifying independent audit, second independent audit still absent.
3. Previous R01 neighboring audits remain historical evidence; do not turn R01 into a routine audit worker.
4. New research should follow the current PROGRESS20 LIVE20 assignments and their current owners rather than revive this superseded slot.

## ledger_delta

```yaml
ledger_delta:
  track: R01
  source: Aldous-Fill Open Problem 3.44 / I0024
  metric_name: minimum uniform multiplicative distortion C
  metric_before: 1
  metric_after: 1
  status_before: PROVED_AUDIT_COMPLETE_FROZEN
  status_after: PROVED_AUDIT_COMPLETE_FROZEN
  unchanged_count: FROZEN
  tried_moves: [3, 17, 29]
  remaining_obligation: none for I0024; publication priority remains UNVERIFIED
  successor_state:
    name: TFIK22
    metric: 0
    audits: 1/2
    status: CANDIDATE_COMPLETE_NOT_CLOSED
  evidence:
    - operations/claims/I0024.md
    - runs/R01/2026-09-16T1459Z_i0024_flow_duality_03.md
    - artifacts/R20/R20_AUDIT_R01_I0024_run3_2026-09-16.md
    - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
    - P26-AUDIT-R01-KMO2026-TFIK22-RESIDUE-68
    - operations/PROGRESS20_2026-09-20.md
    - operations/PROGRESS20_2026-09-20_DEPLOYMENT.md
  audit_ids:
    - R20-AUDIT-R01-I0024-03
    - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
  policy_state: R01_NOT_IN_LIVE20; old audit/intake/rotation loop superseded
```
