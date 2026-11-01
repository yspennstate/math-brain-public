Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: metric `UNMEASURED -> UNMEASURED`; Section-B methods #2/#11/#30 were not attempted because no source passed admission.**

# NM13-10 — sixth admission screen, delta-only

Date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Own namespace: `proofnet24/NM13-10/`  
Category: `CLOSABLE OUTSIDE`  
Exclusive shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 9`

## 1. Continuity recovered before screening

This invocation continues the newest immutable NM13-10 report,

`proofnet24/NM13-10/runs/2026-09-18/2026-09-18T00-51-30Z__admission-delta-screen-5.md`, creation commit `260f6c674406e18d7ced7b26b3d493313420e34b`.

That report had already completed the archived front-catalog residue-9 screen through P0488, remained `ADMISSION_PENDING`, and installed a **delta-only** cursor. I therefore did not restart unchanged P0001--P0488 inventory, did not silently promote the retained near-leads P0133/P0254/P0283, and did not count screening as mathematical progress.

Before evaluating the post-report delta I reread or targeted-recovered the owner-required state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the newest own report above;
- newest visible neighboring NM13-09 report `2026-09-18T00-45-12Z__p0245-cross-foster-symmetric-hitting.md`;
- newest visible neighboring NM13-11 report `2026-09-18T00-52-14Z__H0003-critical-finite-transcript.md`;
- current claim changes, source rows implicated by releases, and the repository delta after the previous immutable report.

Large root/catalog files are connector-bounded when displayed wholesale. Where necessary I used exact path/range reads and source-ID/claim-ID searches rather than pretending every repository byte had been rendered in one response. No inaccessible NM13-10 history was discovered.

Captured pre-save master for this screen: `eef4c3ef875c9fae6ff1aab86b5c96b49447ea11`.

## 2. Repository delta since screen 5

A commit comparison from the previous report commit `260f6c674406e18d7ced7b26b3d493313420e34b` through captured master `eef4c3ef875c9fae6ff1aab86b5c96b49447ea11` contains 88 subsequent commits.

For NM13-10 admission, the decisive fact is that this interval contains **no modification to**:

- `QUEUE.md`;
- any `probability_1000_intake_*/problems.jsonl` source ledger;
- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- root `POSTED.md` or `RESULTS.md`;
- campaign `probability_campaign_2026_09/INDEX.md` or `RANKING.md`.

There is therefore no newly added or materially changed queue/intake source identity to screen under residue 9.

The interval does contain claim-state changes, so I checked those rather than treating a report title or disabled task as a release:

- `operations/claims/H0021.md` was modified to an explicit R16 release/handoff;
- `operations/claims/H0022.md`, `operations/claims/P0024.md`, and `operations/claims/P0279.md` were newly created claims, so they are ownership additions, not reserve releases;
- a D0033 handoff report was added, but the current canonical `operations/claims/D0033.md` still names **R7-01** as owner and explicitly forbids reassignment without an immutable release. D0033 is therefore not available to NM13-10.

No other report-only transition in this delta was treated as permission to steal ownership.

## 3. Explicit H0021 release: canonical shard check before any admission attempt

The only explicit newly visible release was H0021. I therefore recovered its exact source identity before deciding whether it belongs to this worker.

Source row: `probability_1000_intake_H_20260914/problems.jsonl`, H0021.  
Source: Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1.  
Locator: `Conjecture 1.4 (Sharp threshold for tree universality); Section 1.6, "Further challenges"`.  
Exact source statement: for every `epsilon>0` and integer `Delta>=2`, whp `G(n,(1+epsilon) ln n/n)` is universal for all `n`-vertex trees of maximum degree at most `Delta`.

The H-intake schema supplies no `dedup_key`. Following the established NM13 canonical-identity fallback for such rows, I used the source identity plus the exact locator, not the convenient alias `H0021`:

`arxiv_2608_06358::Conjecture 1.4 (Sharp threshold for tree universality); Section 1.6, "Further challenges"`.

Its exact SHA256 is

`5eb8894c6c85250561d00c39076bfe48a685892ea6abedc719f36bacaf537fcd`,

and

`int(hash,16) mod 13 = 3`.

So H0021 is **not in NM13-10's residue-9 shard**. Independently, its handoff says R16 exhausted both allowed HARD stuck recoveries with frozen metric `Delta_near=2`; the source remains a hard asymptotic random-graph universality conjecture. A future worker may use the preserved genuinely fresh route required by the handoff, but NM13-10 cannot acquire it by relabeling it CLOSABLE or by hashing the alias. No claim was created.

## 4. Fresh bounded source/literature status on the strongest retained residue-9 near-lead

Owner policy requires current source/literature checks rather than assuming a prior screen remains current indefinitely. I therefore refreshed **P0133**, still the strongest retained residue-9 near-lead from the completed catalog screen.

### Exact source

Oded Schramm, *Conformally invariant scaling limits: an overview and a collection of problems*, ICM 2006 proceedings / arXiv `math/0602151`, Problem 6.2 (attributed there to Russell Lyons).

The problem asks for the distribution of the three homotopy classes carried by the dual complement of a UST on a fine square-grid approximation of a torus; the square torus is explicitly singled out as interesting, with an expected dependence on torus geometry.

Primary source URL checked by exact-title/problem-number search:  
`https://arxiv.org/abs/math/0602151`

### Dated bounded searches: 2026-09-18 UTC

Queries included:

- `"Schramm Problem 6.2" torus spanning tree dual homotopy distribution Russell Lyons`;
- `"uniform spanning tree" torus dual homotopy classes distribution Schramm Problem 6.2`;
- `"Conformally invariant scaling limits" "Problem 6.2" UST torus`.

The search recovered the original Problem 6.2 text and nearby later UST literature, including high-dimensional-torus Gromov--Hausdorff--Prokhorov scaling work and recent planar/topological-polygon UST/SLE8 work, but no theorem matching the requested two-dimensional fine-torus triple-of-homotopy-classes distribution. This is bounded negative evidence only, not a worldwide-openness or novelty certificate.

Most importantly, the category verdict does not change. P0133 is still an **asymptotic fine-grid distribution problem**, not a source-posed finite/sharp-constant/counterexample question with a realistic short deciding certificate. Existing finite-torus enumeration can guide research but does not answer the literal scaling-limit source. Admitting it to this `CLOSABLE OUTSIDE` worker would violate the owner's anti-relabeling rule.

The other retained residue-9 near-leads P0254 and P0283 remain rejected under the unchanged prior screens: respectively a growing-particle mixing-order problem and the famous asymptotic binary-LCS constant problem. The repository delta contains no source correction making either an honest closable target.

## 5. Admission verdict

**ADMISSION_PENDING.**

No candidate passes all gates in this invocation:

1. there is no new or materially changed queue/intake source row after screen 5;
2. the one explicit newly visible release, H0021, hashes to residue **3**, not residue 9, and is a HARD source with an exhausted prior route;
3. D0033 has a handoff artifact but no canonical ownership release;
4. P0024/P0279/H0022 are newly claimed, not unassigned;
5. the strongest retained residue-9 lead P0133 remains honestly outside the CLOSABLE class after a fresh literature check.

Consequences:

- no canonical `operations/claims/<ID>.md` was created or overwritten;
- no source metric was frozen or invented;
- no theorem/checker artifact was manufactured;
- no audit was requested;
- no shared-root or peer file was edited.

## 6. Metric and Section-B accounting

Before admission there is no source-specific research metric. The only honest entry is:

- **before:** `UNMEASURED`;
- **after:** `UNMEASURED`;
- **movement:** none;
- **unchanged research runs:** `0` — admission screenings do not count as research stagnation;
- **stuck recoveries:** `0`.

The prescribed initial methods remain unspent:

- **#2 ATTACK THE NEGATION FIRST:** not attempted on an admitted target;
- **#11 DUALIZE:** not attempted on an admitted target;
- **#30 ONE PRIME / SCALE / DIRECTION AT A TIME:** not attempted on an admitted target.

Repository diffs, hashing, source-currentness checks, ownership checks, and category screening are bookkeeping, not mathematical movement.

## 7. Model/runtime controls and the historical P26 denial

The prompt requests GPT-6 with maximum reasoning, but this invocation did **not** verify that setting. The actual model exposed to the run is **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**.

The currently exposed task-control schema offers title/prompt, schedule or relative-start information, timing mode, and enabled state. It still exposes **no bindable model-family field and no reasoning-effort field**. Therefore GPT-6/maximum remains a prompt request only. Enforcing it would require an owner-authorized scheduler/product/workspace/API surface whose schema actually exposes model and reasoning controls together with runtime attestation; a GitHub edit cannot change the runtime model.

The repository's corrected history is preserved: one P26 modification attempt returned `You cannot modify this task`, while a later authorized context successfully updated P26. The refusal is therefore context/authorization-specific, not evidence that the task is globally immutable. If the refusal recurs, the legitimate workaround is to use the owning account/workspace or another authorized product/admin surface with permission to modify the original task. Do not clone the task or bypass access controls. No support escalation is claimed because no such action was taken.

## 8. Durable screening cursor

The cursor remains **delta-only**.

Next invocation:

1. compare forward from this report's creation commit;
2. inspect only newly added/materially changed `QUEUE.md` or `probability_1000_intake_*/problems.jsonl` identities, or explicit canonical claim releases/status corrections;
3. recover canonical source identity before hashing — never hash an alias merely because it has an ID;
4. reject current/historical ownership, unreleased handoffs, POSTED/INDEX settled scopes, owner projects, and claimed Agresti--Veraar targets before admission;
5. admit only if the literal source supplies a realistic finite certificate, explicit counterexample, exact sharp constant, or complete short restricted-class theorem in residue 9;
6. after admission, freeze the source inequality and one rigorously certified constant/interval and immediately continue to substantive methods #2/#11/#30.

Do **not** restart the completed P0001--P0488 residue-9 catalog screen absent a material source/status change.

## 9. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-10
  category: CLOSABLE_OUTSIDE
  run_status: ADMISSION_PENDING
  source_id: null
  canonical_dedup_key: null
  claim_id: null
  claim_path: null
  metric_name: null
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  movement: false
  methods_attempted: []
  prescribed_methods_not_attempted: [2, 11, 30]
  screenings_count_as_mathematical_progress: false
  unchanged_research_run_count: 0
  recovery_count: 0
  outside_audits: []
  screening_cursor_before: "delta-only after screen 5 / completed archived residue-9 catalog through P0488"
  screening_cursor_after: "post-screen-5 delta through captured master eef4c3ef875c9fae6ff1aab86b5c96b49447ea11 checked; no QUEUE/intake-source delta; H0021 explicit release rejected by canonical residue 3 and HARD scope; D0033 handoff has no claim release; continue delta-only"
  strongest_near_lead: "P0133 Schramm Problem 6.2 torus UST dual homotopy triple distribution; bounded 2026-09-18 search still found no source-matching resolution, but target remains asymptotic and is not honest CLOSABLE"
  next_step: "Compare from this report commit forward; inspect only new/materially changed source rows or explicit releases/status corrections; admit only after exact-source/current-literature/prior-attempt/exclusive-ownership gates pass."
```

No substantive artifact was warranted because no source passed admission.

**End of complete run report.**
