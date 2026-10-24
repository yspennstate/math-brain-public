Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / no mathematical movement; Section-B methods #2/#6/#18 were NOT attempted because no source crossed admission.**

# NM13-03 — second admission screen

Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: `CLOSABLE OUTSIDE`  
Own namespace: `proofnet24/NM13-03/`  
Run date: 2026-09-17 UTC

## 1. Runtime, policy, and continuity recovered

The requested `GPT-6 / maximum` setting remains prompt text only in the automation surface exposed to this invocation. The callable scheduler interface exposes task title/prompt, schedule or relative start, timing mode, and enable/disable state; it exposes no model-family field and no reasoning-effort field. Therefore I cannot truthfully bind this task to GPT-6 maximum from this interface. Doing so would require the product/scheduler schema and authorized UI/API to expose model and reasoning selectors for this task class. The historical `You cannot modify this task` response is an authorization/context failure, not permission to bypass ownership: the lawful remedy is to use an owning account/workspace or an authorized product/admin surface. I did not create, duplicate, migrate, or modify any schedule in this run.

I reread/recovered the controlling state before screening, including:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the later NM13 deployment material surfaced by repository search;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the newest NM13-03 report, `proofnet24/NM13-03/runs/2026-09-17/2026-09-17T21-13-25Z__admission-screen.md`;
- the newest neighboring NM13-04 report recovered, `proofnet24/NM13-04/runs/2026-09-17/2026-09-17T21-20-42Z__p0457-k-nminus2-classification.md`;
- the neighboring NM13-02 admission report, whose I-series canonicalization rule is relevant below;
- current intake rows, claim searches, attempt/rotation histories, and task-health admission screens for candidates that survived long enough to require them.

Continuity is therefore authoritative: the prior NM13-03 state was `ADMISSION_PENDING`, with no claim and no mathematical baseline. This run resumes that screening cursor; it does not restart F0001/F0007/F0012 or treat a missing claim path as a release of historical ownership.

## 2. Canonical shard discipline

Eligibility remains

`int(SHA256(UTF-8 canonical_dedup_key).hexdigest(), 16) mod 13 = 2`.

For D/E/G rows carrying a `dedup_key`, I hashed exactly that field. For I-series rows, whose schema does not carry `dedup_key`, I followed the current fleet canonical-identity fallback already recorded by NM13-02: exact `source_id::locator`, preserving the source locator rather than hashing the intake ID, display title, or an alias. I did not infer a shard from a problem number.

This matters materially. For example, Randomstrasse Matrix Spencer (`I0090`) is residue 9 under its canonical source identity and is not NM13-03 inventory; Aldous–Fill `I0025` and `I0026` are residue 2, but the former is resolved in later literature and the latter contains the explicitly retired/excluded Open Problem 4.49(ii) route.

## 3. Screening advanced in this run

### E-series: completed the remaining canonical-key pass through E0113

The residue-2 rows encountered were:

- `E0031` — Chatterjee lower-bounds open problem item 3: an asymptotic fluctuation lower-bound problem, genuinely HARD rather than CLOSABLE.
- `E0044` — Bandeira/Duchi norm-inside-average conjecture: superficially an excellent norm-inequality fit, but **not unassigned**. Repository history shows the exact corrected source statement is the active/historical PROB20-17 target. Its missing-or-changing scheduler status does not release ownership. Excluded without touching its files.
- `E0046` — monotonic singular values: intake status is resolved in 2026. Excluded.
- `E0067`, `E0068` — quadratic stochastic operator classification/dynamics questions: source-wide classification problems, not finite/sharp CLOSABLE targets.
- `E0070` — quotient/quasi-harmonic construction: infinite structural problem, not closable-shaped.
- `E0075` — polling-system renewal asymptotics: theorem-sized asymptotic problem.
- `E0088` — bootstrap-percolation noise dichotomy: asymptotic hard target.
- `E0100`, `E0102` — branching-random-walk limiting-measure sigma-algebra / multifractal problems: broad hard targets.

No E-series row passed the combined shard + source + current status + ownership + CLOSABLE gate.

### G-series: complete residue check

Among `G0001`–`G0015`, the only residue-2 row is `G0004`, Lucas Flammant's Conjecture 2.2 on increasing boundary events in finite-graph Bernoulli percolation. A fresh 2026-09-17 primary-source search recovered arXiv:2609.03492, posted 2026-09-03, still presenting the statement as the paper's central conjecture and proving only the planar outer-face case with the explicit `1-2 sqrt(epsilon)` bound. The exact source conjecture is finite-graph in formulation but source-wide and strong enough to imply `theta(p_c)=0` for every `d>=2`; treating it as a short finite certificate problem would be category laundering. Disposition: **OPEN-looking but HARD, not CLOSABLE**.

### D-series: random-matrix/operator front and later residue-2 rows

The strongest focus-matching lead was `D0041`, Virag's Problem 3 (“Mo's formulas”). It is residue 2 and is exactly the sort of short analytic verification this worker would otherwise prefer. However, current repository search recovered canonical `operations/claims/D0041.md` plus an extensive PROB20-07 rotation history on 2026-09-17, including the normalized-formula proof route and later stuck/rotation reports. This source is historically owned/exhausted for present allocation purposes. **No claim was created and ownership was not duplicated.**

Other later D-series residue-2 rows checked here include:

- `D0069`, Grimmett–Li Question 2.2 on the `sqrt(Delta-1)` connective-constant lower bound for non-simple transitive multigraphs of degree at least five. A fresh bounded 2026-09-17 search found later Grimmett–Li connective-constant work and Grimmett's August 2026 Grigorchuk-graph paper, but no source-matching theorem removing the non-simple `Delta<=4` restriction. The target remains an unrestricted infinite-graph theorem and is not honestly CLOSABLE.
- `D0078`, embedded spanning-tree random planar-map convergence to `sqrt(2)`-LQG: hard scaling-limit problem.
- `D0092`, the activated-random-walk finite-cycle fast/slow toppling dichotomy off the critical curve: despite the finite-cycle statement at each `n`, the source asks an all-parameter asymptotic theorem, not a finite deciding certificate.

The early D tranche `D0001`–`D0035` still needs an exact canonical-key rehash before I will claim that the D ledger is exhausted; an earlier scratch shortcut based on aliases was discarded rather than used as evidence.

### I-series: canonical source identity, not intake IDs

I advanced the source-identity hash screen through the early Aldous–Fill block and the later `I0072`–`I0103` block.

Notable residue-2 rows:

- `I0025`, Aldous–Fill Open Problem 4.38: the intake itself records the later Hermon characterization as resolving the conjecture. Excluded.
- `I0026`, Aldous–Fill Open Problem 4.49: explicitly excluded by owner policy, including the 4.49(ii) diameter route. Excluded regardless of scheduler accessibility.
- `I0031`, Aldous–Fill Open Problem 7.31: current task-health screening already classifies the exact `tau_0=O(n)` distance-regular-graph statement as **HARD / pending ownership**, not CLOSABLE. A fresh bounded literature query found modern Kemeny-constant work but no source-matching short resolution; that negative search is not a novelty certificate.
- `I0037`, Schramm Problem 2.10 on the scaling limit of an asymmetric percolation interface: hard conformal-scaling problem, not CLOSABLE.
- `I0084`, eventual unimodality under stable convolution: residue 2, but it is already represented in current fleet work (R19/HU5.5) and is asymptotic analytic rather than a fresh closable source. Excluded by ownership/category.

The Randomstrasse matrix/discrepancy block `I0090`–`I0103` was also canonical-hashed in this pass; **none is residue 2**. In particular, Matrix Spencer is residue 9 and cannot be taken by NM13-03 even apart from the posted/owner exclusions.

## 4. Original/current literature and access limits

The fresh external checks in this run were deliberately concentrated on unowned or apparently source-current candidates that could otherwise affect admission:

- Query family for Flammant Conjecture 2.2 / arXiv:2609.03492. Primary arXiv result dated 2026-09-03 still states the conjecture and the planar partial theorem.
- Query family for Grimmett–Li Question 2.2, the non-simple transitive multigraph connective-constant bound, including 2024–2026 author work. The search recovered related strict-inequality/locality literature and Grimmett's 2026 Grigorchuk result, but no exact removal of the source restriction.
- Query family for Aldous–Fill Open Problem 7.31 / distance-regular Kemeny constants. Search recovered recent general Kemeny work but no exact source-level short theorem; the repository's current task-health screen independently classifies it HARD.

Ownership was already decisive for `E0044` and `D0041`, so I did not spend literature budget trying to rehabilitate a target this worker cannot own. Search coverage is bounded and does not prove worldwide openness. I did not execute or import external scripts.

## 5. Admission decision and metric

**Decision: `ADMISSION_PENDING`. No canonical claim was created.**

No candidate screened this run simultaneously passed:

1. canonical residue 2;
2. exact source statement recovered;
3. present-source/current-literature plausibility;
4. no current or historical ownership / exhaustion / retirement;
5. honest `CLOSABLE OUTSIDE` shape.

Accordingly the mathematical metric is still unfrozen:

- before: `UNMEASURED`;
- after: `UNMEASURED`.

There is **no mathematical movement**. Screening counts, hashes, literature lookups, and ownership exclusions are not being counted as progress on a mathematical target.

The reserved first research methods **#2 ATTACK THE NEGATION, #6 DEFORM TO A SOLVABLE POINT, and #18 SAY IT IN ANOTHER LANGUAGE were not attempted**, because no source crossed admission. Reporting them as attempted would be false.

## 6. Durable cursor for the next invocation

Do not repeat the candidates above unless source status or ownership changes. Resume in this order:

1. exact rehash of `D0001`–`D0035` from their literal `dedup_key` fields, discarding all alias-based scratch calculations;
2. finish the unscreened I-series intervals using exact `source_id::locator` identity (`I0040`–`I0071`, then `I0104+`), while respecting current claims and task-health HOLD/HARD flags;
3. screen the H-series using recovered canonical source identities, not H aliases; several H rows are already owned and must remain excluded;
4. only then advance into the raw/Codex source catalog for a genuinely new residue-2 source;
5. if a candidate survives, perform the full current-source/later-author/citing-paper check, create `operations/claims/<ID>.md` create-only, read it back, freeze one source-faithful metric, and immediately start B2/B6/B18 mathematics in that same run.

This cursor is continuity, not pre-authorization of any future claim.

## 7. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-03
  category: CLOSABLE_OUTSIDE
  source_target: UNASSIGNED
  status: ADMISSION_PENDING
  metric:
    name: UNFROZEN_UNTIL_ADMISSION
    before: UNMEASURED
    after: UNMEASURED
  mathematical_movement: false
  section_B_methods:
    attempted: []
    reserved_first_after_admission: [2, 6, 18]
  claim_created: false
  screening_run_count: 2
  notable_exclusions:
    - E0044: OWNED_PROB20_17_EXACT_CORRECTED_DUCHI_SCOPE
    - E0046: RESOLVED_2026
    - G0004: OPEN_LOOKING_BUT_HARD_NOT_CLOSABLE
    - D0041: HISTORICALLY_OWNED_AND_EXTENSIVELY_WORKED_PROB20_07
    - D0069: OPEN_LOOKING_BUT_INFINITE_GRAPH_THEOREM_NOT_CLOSABLE
    - I0025: RESOLVED_IN_LITERATURE
    - I0026: OWNER_EXCLUDED_ALDOUS_FILL_4_49
    - I0031: CURRENT_TASK_HEALTH_HARD_NOT_CLOSABLE
    - I0084: CLAIMED_OR_REPRESENTED_R19_AND_HARD
    - I0090: WRONG_SHARD_RESIDUE_9
  unchanged_run_count: NOT_APPLICABLE_BEFORE_ADMISSION
  stuck_recovery_count: 0
  next_cursor: "rehash D0001-D0035 exactly; then I0040-I0071 and I0104+ via source_id::locator; then H and raw/Codex shard-2 inventory"
  audit_status:
    P26: NOT_REQUESTED
    NM13-04: NOT_REQUESTED
  shared_root_edits: none
```

No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, peer-track edit, shared-root edit, or schedule creation/modification was performed.

**End of complete run report.**
