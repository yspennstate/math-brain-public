Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING; no mathematical movement; B2/B15/B29 were not attempted because no source passed admission.

# NM13-07 research invocation — admission screen 2

Date: 2026-09-17 UTC
Track: `proofnet24/NM13-07`
Category: CLOSABLE OUTSIDE
Exclusive shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 6`
Status: **ADMISSION_PENDING**
Claim created this run: **none**
Metric: **UNMEASURED -> UNMEASURED**
Mathematical progress: **none; screening is not mathematical progress**
Unchanged-run count: **0 (not started before admission)**
Stuck-recovery count: **0**

## 1. Continuity and policy read

I continued from `proofnet24/NM13-07/runs/2026-09-17/2026-09-17T21-47-00Z__admission-screen.md`; I did not restart intake. I read the required current policy/ledger files `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, `QUEUE.md`, `POSTED.md`, `RESULTS.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, and `probability_campaign_2026_09/LOCAL_INVENTORY.md`, plus the NM13 deployment record and the newest neighboring NM13-06/NM13-08 reports. A bounded repository search did not surface a later owner-authorized amendment changing this worker's shard/category rules.

I also checked exact candidate IDs/dedup identities against `operations/claims/`, attempt/report history, posted/campaign material, and historical assignment references. The GitHub connector gives default-branch file/search access rather than a literal local clone; required ledgers and candidate-specific history used below were accessible. This is not a claim that every byte in the repository was materialized in this run.

Current branch head observed during screening was `39531dfe960619daf05dc19c724f81b00f32dc23` (`R12 I0102 terminal stuck handoff after fresh reassignment`, 2026-09-17T22:51:05Z); candidate ownership was checked against current `master`, not against the older start-of-run snapshot.

## 2. Canonical identity / shard rule

For intakes carrying `dedup_key`, I hashed that exact UTF-8 key. For H/I rows that omit `dedup_key`, I first recovered the canonical source identity as the exact `source_id::locator` pair and hashed that, rather than hashing the intake alias. No claim was created merely from an intake `problem_id`.

This run completed the residue-6 pass over the C/G/H families, the currently source-checked I0001–I0117 range, and the F0001–F0140 intake. It also revisited the strongest pending E lead from the previous run. The remaining durable cursor is the unscreened residue-6 portion of D/E plus raw/Codex identities not already represented by these intake rows.

## 3. Strongest geometric candidates and ownership/status exclusions

### F0083 — stable allocation nonuniqueness

Canonical key: `hhp_stable_marriage_2006::open_problem_i_nonuniqueness`.

This is an unusually good subject match: the source asks for a discrete Euclidean set of centers admitting two stable Lebesgue allocations, hence an explicit geometric construction could close it. It is **not available**. `operations/claims/F0083.md` is an active exclusive claim owned by R08, with an admitted explicit d=4 candidate and an open second obligation. A disabled or inaccessible scheduler would not release that ownership. I did not touch the target.

### I0097 — MUB(6)<7

Canonical identity recovered from the Randomstrasse source/locator. It is **not available**: `operations/claims/I0097.md` is owned by C29 for the unrestricted seven-MUB-in-C^6 question. This is HARD OUTSIDE in any event, and cannot be duplicated under an NM13 alias.

### F0063 — Janson Conjecture 20.1

Canonical key: `janson_simply_generated_2012::conjecture_20.1`.

Although it hashes to residue 6 and has a short-theorem flavor, it has substantial fleet history and is already a campaign result, not an untouched source. The archived 2026-09-14 attempt proves the conjecture for all integer r>=1 and more generally real r>=1, with only a fractional-moment infinite-variance remainder; multiple campaign reviews audited the argument. Reopening it would violate the settled/attempted-source rule.

## 4. Pending E0057 corrected by later literature

Canonical key: `bandeira::op_10_4_mra` (Open Problem 10.4, multireference alignment).

The previous run left E0057 `PENDING_SOURCE_CURRENT` because the exact quasi-MLE/MLE formulation had not been reconciled with later work. Fresh bounded literature checking now gives a decisive correction for at least the MLE branch: Emmanuel Abbe, Joao M. Pereira and Amit Singer, *Estimation in the group action channel* (arXiv:1801.04366 / ISIT 2018), motivated explicitly by multireference alignment, proves that the maximum-likelihood estimator is consistent when `N/sigma^(2d)` diverges (with d the moment-order cutoff), while also giving the matching information-theoretic obstruction when that ratio is bounded.

Therefore E0057 is **not admissible as an untouched MLE-consistency problem**. A surviving quasi-MLE clause, if any, still requires exact reconciliation of Bandeira's estimator definition, normalization, and quantifiers with the later theorem before it could even become READY. I found no canonical `operations/claims/E0057.md`, but absence of a claim does not make a stale/mixed source admissible. It remains `PENDING_SOURCE_CURRENT`, not selected.

Literature query date: 2026-09-17. Bounded query family: exact title/authors plus `multireference alignment maximum likelihood consistent N sigma 2d`; source accessed through arXiv search metadata/abstract. This is bounded evidence, not a worldwide literature certificate.

## 5. Residue-6 screens completed this run

### C intake

Residue-6 rows recovered: C0036, C0060, C0076, C0085, C0100, C0124, C0127, C0132, C0141. None is an admissible CLOSABLE target. C0124 and C0141 are resolved; the remainder are broad/infinite or genuinely HARD (determinantal positive-contraction classification, interlacements on gasket x Z, critical-percolation scaling, invasion-percolation asymptotics, sandpile scaling, chaos/superconcentration, balanced excited walk). No finite source-level geometric extremal deliverable survives.

### G intake

No G0001–G0015 canonical identity hashes to residue 6. There is therefore no G candidate for this worker in that intake.

### H intake

Because H omits `dedup_key`, exact `source_id::locator` identities were recovered before hashing. Residue 6 gives H0004 (sensitive regime), H0007 (beyond trees), H0020 (Pólya-urn clause already settled/refuted in campaign material), and H0022 (cycle-factor universality). The live rows are asymptotic HARD programs, not CLOSABLE finite/certificate targets.

### I intake, source-checked I0001–I0117

Again I used exact `source_id::locator` identities. Residue 6 gives I0003 and I0004 (orientation-dependent transience/recurrence: HARD environment classification), I0018 (resolved parking result), I0035 (broad charged-particle relaxation problem), and I0097 (claimed by C29). No eligible target remains in this range. Owner-deployment I0120–I0129 rows remain explicitly `PENDING`, not READY, and were not treated as allocatable intake.

### F intake, F0001–F0140

The residue-6 rows are F0010, F0025, F0036, F0038, F0063, F0079, F0083, F0086, F0114, F0125, F0133 and F0136.

- F0010: random-matrix normality, asymptotic HARD.
- F0025: RSW/crossing estimates on all planar or quasi-planar lattices, broad HARD. Current RSW work covers large important classes but not the source's unrestricted scope.
- F0036: Brownian-net local finiteness of potential most recent common ancestors, infinite stochastic geometry; no short finite target recovered.
- F0038: Brownian-web black-noise maximal factorization, broad HARD.
- F0063: substantial prior fleet proof/audits; excluded from reopening.
- F0079: resolved in literature (quartic-interface localization).
- F0083: excellent geometric candidate but actively owned by R08.
- F0086: historical fleet screening already rejected it as a clean finite CLOSABLE successor; positive-alpha interval remains broad.
- F0114: resolved in literature (fractional threshold theorem).
- F0125: scenery-reconstruction entropy criterion, HARD asymptotic.
- F0133: Voiculescu free-entropy unification problem, famous HARD.
- F0136: 2D Dirichlet-RW ballisticity sharpness, HARD.

For F0025, a bounded current search checked Köhler-Schindler–Tassion's general RSW theorem and related planar/random-cluster work; these enlarge the covered symmetry/model classes but do not turn the source's all-planar/quasi-planar request into a short closable statement. For F0036, a bounded exact-title/problem-language search recovered the Brownian-net source but no later primary paper claiming this local-finiteness conjecture; that negative result is not evidence of worldwide openness.

## 6. Why no admission occurred

After exact canonical hashing, the geometrically attractive residue-6 sources are either already owned (most notably F0083 and I0097), already settled/heavily attempted (F0063, F0079, F0114, H0020, I0018), stale/mixed pending source reconciliation (E0057), or honestly HARD/infinite problems. I will not relabel one of the latter CLOSABLE merely to produce a claim.

Accordingly there is no source/claim ID, no frozen geometric objective, and no baseline other than `UNMEASURED`. The initial methods B2/B15/B29 remain reserved for the first admitted target and are **not** marked tried here.

## 7. Scheduler/model control disclosure

The task-control interface available to this run exposes prompt text, scheduling/timing, title, enable/disable state and related task metadata; it exposes **no binding model-family selector and no reasoning-effort selector**. Thus `Model: GPT-6. Reasoning: maximum` can presently be requested only in prompt text, not enforced by this interface. This run actually identifies itself as GPT-5.6 Sol with reasoning level UNVERIFIED.

Repository/task history records a P26 scheduler edit returning `You cannot modify this task`. I did not attempt to bypass it. The lawful remedy is an owning account/workspace or product/admin surface with permission to modify that task and, if desired, a scheduler implementation that actually exposes model/reasoning fields. Duplicating a protected task or changing repository files does not fix the scheduler permission/model-control issue.

## 8. Next screening cursor

Next invocation should continue, without repeating this screen, by:

1. enumerating every remaining canonical residue-6 identity in the D and E intake files not already dispositioned in the two NM13-07 reports;
2. screening raw/Codex source identities that are not mirrors of C/F/G/H/I rows, recovering canonical identity before hashing;
3. checking any resulting finite geometric/convexity/packing/network candidate against exact source text, current primary literature, all claim/attempt/handoff history, POSTED and campaign ledgers;
4. revisiting E0057 only if the quasi-MLE estimator can be source-reconciled to a genuinely unresolved clause, never treating the already-covered MLE-consistency branch as open.

No target becomes READY merely because it is unclaimed.

## ledger_delta

```yaml
track: NM13-07
category: CLOSABLE_OUTSIDE
status: ADMISSION_PENDING
source_id: null
claim_id: null
dedup_key: null
selection_shard_mod_13: 6
metric_name: null
metric_before: UNMEASURED
metric_after: UNMEASURED
movement: none
mathematical_progress: none
methods_actual: []
methods_reserved_initial: [2, 15, 29]
unchanged_run_count: 0
stuck_recovery_count: 0
claim_created: false
audit_p26: NOT_REQUESTED
audit_nm13_08: NOT_REQUESTED
screening_cursor: "remaining canonical residue-6 D/E rows, then non-mirrored raw/Codex identities; E0057 only after quasi-MLE source/current reconciliation"
next_step: "continue admission screening; create a claim only after exact source/current-literature/history/ownership clearance, then immediately begin counterexample-first substantive work"
literature_check_date: 2026-09-17
literature_access_limit: "bounded web/arXiv search plus repository source/status records; not a worldwide-openness certificate"
```

END_REPORT
