Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; Section-B methods #2/#14/#16 remain unspent because no source crossed admission.**

# NM13-13 — successor admission screen 2

Date: 2026-09-18 UTC  
Track / namespace: `NM13-13` / `proofnet24/NM13-13/`  
Category: `HARD OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Exclusive shard: `int(SHA256(UTF-8 canonical_dedup_key).hexdigest(),16) mod 13 = 12`

## 1. Runtime disclosure and authoritative continuity

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still has prompt/title, timing/schedule and enabled-state controls but no bindable model-family selector and no bindable reasoning-effort selector. Enforcing GPT-6/maximum would require an owner-authorized product/workspace/API/admin surface that exposes those controls plus authenticated per-run runtime attestation. The historical `You cannot modify this task` scheduler response is an authorization-context boundary; later repository history records that P26 was editable from another authorized context. The lawful workaround is the owning/authorized scheduler context or platform/admin support, not duplication or bypass. No schedule was modified in this invocation.

The controlling NM13-13 predecessor is

`proofnet24/NM13-13/runs/2026-09-18/2026-09-18T06-06-00Z__f0013-degree-support-handoff.md`.

It records the mandatory third-stuck-episode handoff of F0013 after both permitted HARD recoveries, so this worker may not resume F0013 without an explicit fresh owner reassignment. It leaves the successor state `ADMISSION_PENDING`, successor metric `UNMEASURED`, and the durable screening cursor at **F0066**. It also preserves the initial successor methods #2 ATTACK THE NEGATION FIRST, #14 FIND THE GROUP ACTING, #16 COMPUTE EVERY SMALL CASE as unspent.

Before advancing the cursor I reread/recovered the owner-required current surfaces: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the newest own report; newest neighboring NM13-12 report; newest proposed-audit-partner NM13-01 report; F/G/H intake material reached below; source-attempt ledgers; canonical claim searches; and current branch head. Immediately before this report write, the observed master head was `cfdcc4c63a2e300fe02a85020338706506efffd5`.

Large JSONL files are connector-bounded when rendered wholesale. I therefore advanced from the immutable cursor with exact line-range fetches, literal F/G canonical `dedup_key` values, exact hash recomputation, exact-ID attempt/claim searches, and source-specific web checks. I do not claim a byte-for-byte reread of every historical repository object in one connector response.

## 2. F intake F0066--F0140: shard screen completed through EOF

The F ledger supplies explicit canonical `dedup_key` fields. I hashed those keys, not problem IDs or titles. In the entire remaining F range F0066--F0140, exactly three canonical rows land in residue 12:

| ID | canonical dedup key | SHA-256 | disposition |
|---|---|---|---|
| F0073 | `velenik_interfaces_2006::open_problem_6` | `b2dfa27434195f08b78847d7f70b1670d2cf8e11f7126d7cc9164ef6efea9d96` | source-wide 2D pinned-positive convex-interface height problem; prior substantive attempt; **HARD but no realistic finite/source-relevant exact milestone for this worker** |
| F0107 | `talagrand_small_2016::conjecture_8.4` | `ed617d2eadf3b49b6f501717ce0b7871701b7f2de9adb1c6e5425dd79ed23763` | **literature-resolved by a direct corollary of Pham's sharp selector theorem; exclude** |
| F0121 | `mossel_info_flow_trees_2004::conjecture_1_local_algorithms` | `512b1603bfe2a038a96c47d4577862835efa054582ea52ab279513f96dca6e98` | **resolved/known in the intake and later fleet screens; exclude** |

No other F0066--F0140 canonical key hashes to residue 12.

### 2.1 F0073 — open-looking but not an admissible finite hard milestone

F0073 is Velenik, *Localization and delocalization of random interfaces*, Open Problem 6, “Height of the two-dimensional field pinned at the origin and kept positive, for convex interactions.” It asks for the asymptotic height/fluctuation behavior of a two-dimensional positive interface with a pin at the origin for general convex interactions. The intake already records a substantive attempt. The source target is an infinite-volume/asymptotic interface theorem; there is no smallest unresolved finite order, exact construction, certified extremal cardinality, or finite SAT/SMT obstruction whose completion would decide a source clause. A finite box computation would be route selection only and would not establish the requested asymptotic height law.

A bounded 2026-09-18 search by exact title/source wording did not surface a source-matching later theorem, but this negative search is not proof of worldwide openness. Even assuming the source remains open, it fails this worker's explicit admission gate requiring a realistically movable finite or quantitative hard milestone. I therefore did not claim it.

### 2.2 F0107 — current-status correction: Pham's sharp selector theorem implies Conjecture 8.4

F0107 is Talagrand's Conjecture 8.4. In the intake's exact normalization: an `m`-uniform family `B` carries a `delta`-spread probability measure `nu`, and the conjecture asks for a universal `L` such that for every `p >= delta`,

`E_p sup_{I in B} |X intersect I| >= m(1 - L exp(-p/(L delta)))`.

The old intake attempt `F0107-A001` recognized that the conjecture interpolates between the one-round spread bound and the logarithmic-density full-containment theorem, but left an iteration/uniformity gap. That historical attempt is preserved and is not credited as NM13-13 work.

A fresh dated literature check found Huy Tuan Pham, *A sharp version of Talagrand's selector process conjecture, with applications to rounding fractional covers and Bernoulli Sudakov minoration*, arXiv:2412.03540, originally 4 December 2024 and updated on arXiv through 9 September 2026; the published conference version appears in STOC 2025 (ACM DOI 10.1145/3717823.3718256). The paper's Theorem 1.4 says, in the paper's terminology, that if a family `H` is not `q`-small, then at density `C s q` a selector captures all but a `2^{-s}` fraction of the weight of some member with probability at least `1-2^{-s-1}`. The paper explicitly emphasizes that the captured fraction approaches one exponentially in the density multiplier and that this dependence is optimal up to constants.

For F0107 the implication is immediate and source-normalization preserving:

1. A `delta`-spread probability measure `nu` on `B` forces `B` to be **not delta-small**. Otherwise, if a cylinder cover `G` had `sum_{J in G} delta^{|J|} <= 1/2`, then

   `1 = nu(B) <= sum_{J in G} nu({I: J subset I}) <= sum_{J in G} delta^{|J|} <= 1/2`,

   a contradiction.

2. Apply Pham's Theorem 1.4 with base density `q=delta` and the uniform weight vector `lambda_I(x)=1/m` on each `I in B`. For each positive integer `s`, at density `C s delta` there is, with probability at least `1-2^{-s-1}`, an `I in B` with at least `(1-2^{-s})m` selected points.

3. Therefore

   `E_{C s delta} sup_{I in B}|X intersect I| >= m(1-2^{-s})(1-2^{-s-1})`,

   hence at least `m(1-c 2^{-s})` for a universal `c`.

4. For arbitrary `p >= delta`, choose `s=floor(p/(C delta))` whenever this is at least one and couple the smaller-density set inside the `p`-set. After enlarging the universal constant to absorb the bounded range `1 <= p/delta < 2C`, this is exactly

   `E_p(B) >= m(1 - L exp(-p/(L delta)))`.

Thus **F0107 is no longer an open admission candidate: the current sharp selector theorem gives Talagrand Conjecture 8.4 as a direct corollary up to the universal-constant normalization already allowed by the source.** This is a literature-status correction, not a new NM13-13 theorem or metric movement. I found no canonical `operations/claims/F0107.md`, so there is no ownership conflict to resolve; there is simply nothing open to claim. Shared-root status reconciliation belongs to P26/coordinator, not this worker.

### 2.3 F0121 — preserved resolution exclusion

F0121 is Mossel's Conjecture 1 on local bounded-memory reconstruction algorithms for the Ising model on a regular tree. The current F intake marks it `[EXCLUDED]` as resolved in the literature, and later fleet admission screens independently preserve F0121 as resolved/known. I did not reopen it under a new title or alias.

## 3. G intake G0001--G0015: complete shard scan

The G ledger also supplies explicit canonical `dedup_key` fields. Exactly one G row hashes to residue 12:

`G0006 = fernley_jacob_contact_tree_2026::lambda_1_lt_lambda_p_zd`

with SHA-256

`6f8df1efd12989fdcd8425a54e781ed8a05a82afb90bd168d9690866e4c51fa7`.

The exact source question asks whether the contact process on `Z^d`, `d>=2`, has strict separation `lambda_1 < lambda_p` between the survival threshold and the percolation threshold of the upper invariant infected set. The September 2026 Fernley/Jacob source proves the strict separation on regular trees and explicitly says the lattice problem remains difficult and, to their knowledge, had not previously been proved on any graph with finite `lambda_p`. A fresh 2026-09-18 exact-phrase search again surfaced that source framing and no later primary resolution. This is bounded negative evidence only.

Ownership checks found no canonical `operations/claims/G0006.md`, but the G attempt ledger contains substantive `G0006-A001`, so the source is not previously unattempted. More importantly, G0006 is a global infinite-lattice phase-transition separation problem. The source does not expose a finite graph order, explicit algebraic construction, exact extremal cardinality, or finite certificate whose completion would decide a source clause. Introducing a finite-volume proxy would change the metric rather than move the source statement. Under the HARD admission rule “admit only where the quantity can realistically move or a finite certificate can decide a source-relevant clause,” G0006 does not pass.

No other G0001--G0015 canonical key belongs to residue 12.

## 4. H canonical-identity caution and durable cursor

The next intake family is H. Unlike F and G, the H rows do **not** carry explicit `dedup_key` fields. The neighboring NM13-01 screen has already demonstrated why blindly hashing an H row's title or nominal `source_id::locator` fallback is unsafe: H0010 is an alias of earlier canonical G0014, and its nominal H fallback lands in a different shard from the explicit earlier canonical key. H0013/H0014 also have campaign-status corrections. Therefore I did **not** hash H aliases merely to extend a table.

The next NM13-13 cursor is accordingly **H0001 canonical reconciliation**: for each H row, first search earlier F/G/I/Codex identities and canonical claims/attempts, adopt the existing canonical dedup key when an alias exists, and only then apply residue 12. Rows with no earlier canonical representation require a stable source identity established from the original source before hashing. This preserves the owner's explicit instruction that a missing dedup key must be recovered rather than replaced by a convenient alias.

This run therefore advances the durable successor screen from F0066 to **H0001**, with F0066--F0140 and G0001--G0015 complete under canonical keys.

## 5. Admission verdict

**ADMISSION_PENDING. No canonical claim was created.**

No reached candidate simultaneously passed all of:

1. canonical identity and exact residue 12;
2. present source statement still unresolved after current-status review;
3. no posted/settled/retired/claimed/handoff conflict;
4. a source-relevant HARD milestone that can realistically move in finite/exact/quantitative form;
5. no exhausted source reopened under a different ID.

Accordingly:

- admitted source ID: **none**;
- claim ID/path: **none**;
- metric before: **UNMEASURED**;
- metric after: **UNMEASURED**;
- mathematical movement: **none**;
- screening movement: **F0066 -> H0001**;
- Section-B #2 ATTACK THE NEGATION FIRST: **not tried**;
- Section-B #14 FIND THE GROUP ACTING: **not tried**;
- Section-B #16 COMPUTE EVERY SMALL CASE: **not tried**;
- successor unchanged-run counter: **0 / not started**;
- successor stuck-recovery counter: **0 / not started**;
- P26 audit: **not applicable / not presumed passed**;
- NM13-01 audit: **not applicable / not presumed passed**.

Screening does not count as mathematical progress and does not start a stagnation counter. No checker, proof artifact, SAT/SMT certificate, paper package, audit request, or claim file was manufactured merely to document screening.

## 6. Bounded literature checks and access limits

Dated 2026-09-18 searches included:

- exact F0107/Talagrand Conjecture 8.4 language, `spread family`, and `sharp selector`; recovered Pham arXiv:2412.03540 / STOC 2025 and its sharp selector theorem;
- exact F0073/Velenik pinned-positive interface wording; no source-matching later theorem surfaced in the bounded result set;
- exact G0006 `lambda_1 < lambda_p`, contact process, `Z^d`, Fernley/Jacob; recovered the September 2026 source framing the lattice strict-separation problem as still open;
- repository source/attempt/claim searches for all four shard hits F0073/F0107/F0121/G0006.

Web search is bounded and not an openness or novelty certificate. For F0107 the exclusion is positive rather than negative evidence: a current published theorem supplies the needed exponential partial-coverage estimate directly. For the other unresolved-looking rows, failure to locate a resolution did not override the finite-milestone admission gate.

## 7. Neighbor and fleet continuity

The newest NM13-12 report remains `2026-09-18T06-06-00Z__successor-admission-screen-1.md`; it is also in `ADMISSION_PENDING` and preserves its own residue-11 exclusions rather than releasing them. The newest NM13-01 report `2026-09-18T06-00-57Z__admission-screen-3.md` completed F/G/H residue-0 screening and explicitly documents H alias reconciliation before hashing. Neither neighboring state releases ownership to NM13-13 or counts as an audit.

Root `POSTED.md`, campaign `INDEX.md`/`RANKING.md`, and `RESULTS.md` exclusions were preserved. In particular, the retired/settled source families named by the owner remain off limits, and F0013's own terminal hard handoff remains binding.

## 8. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-13
  category: HARD_OUTSIDE
  status: ADMISSION_PENDING
  source_id: null
  claim_id: null
  canonical_dedup_key: null
  shard_mod_13: 12
  metric_name: successor_metric
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  mathematical_movement: false
  screening_cursor_before: F0066
  screening_cursor_after: H0001_CANONICAL_RECONCILIATION
  completed_screen:
    - probability_1000_intake_F_20260908:F0066-F0140
    - probability_1000_intake_G_20260910:G0001-G0015
  status_corrections:
    - id: F0107
      disposition: KNOWN_BY_DIRECT_COROLLARY
      evidence: Pham sharp selector theorem, arXiv:2412.03540 / STOC 2025
  methods_actual: []
  methods_reserved: [2, 14, 16]
  unchanged_runs: 0
  recovery_count: 0
  p26_audit: NOT_APPLICABLE
  secondary_audit_nm13_01: NOT_APPLICABLE
  next_step: Recover H canonical identities and aliases before hashing; screen only canonical residue-12 rows, then continue into I if H yields no admissible source.
```

No shared root, peer namespace, existing claim, workflow, permission, public surface, email/Drive item, paid-compute resource, or schedule was modified in this invocation.