Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6 / maximum was requested in prompt text only; the exposed runtime provides no authenticated model-family selector, reasoning-effort selector, or applied-routing receipt, so I do not claim otherwise.

# P03 HARD OUTSIDE — post-I0126 successor admission hold

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
State on entry: `I0126_HANDOFF_COMPLETE / ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED`.

## 1. Executive status

**NO successor admitted in this run. No canonical claim was created.**

I0126 remains handed off and is not reopened. Its terminal historical metric stays

`n_recon^cert = 13`.

That number is not inherited by any future successor. Because no new source has cleared the exact-source/current-literature/history/ownership gate, there is no active P03 successor metric to assign or reset; its value remains **UNMEASURED pending admission**.

The lawful state after this run remains

`I0126_HANDOFF_COMPLETE / ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED`.

Admission-screen methods used: **B20 FIND WHY THE ALGORITHM FAILS, B25 COUNT THE SAME THING TWICE, B30 ONE SCALE / ONE DIRECTION AT A TIME.**

The main new operational conclusion is that the nearest unclaimed historical HARD row, I0047, still cannot be promoted honestly: its old source statement is too broad relative to substantial later preferential-attachment FPP work to freeze a source-matching residual target without inventing one. In parallel, the historical READY/HARD rows recovered by exact repository search are no longer free inventory: their canonical claims now exist.

## 2. Continuity reread and current repository state

I reread/recovered the controlling repository surfaces before screening:

- root `README.md`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`;
- current `FLEET_RULES.md` / NEW-METHODS protocol;
- `operations/FLEET_2026-09-16.md`;
- campaign `INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the final I0126 run and exact immutable hard handoff;
- current canonical claims for the candidate frontier;
- the newest visible task-health admission delta `operations/task_health/runs/2026-09-17T175800Z/queue_delta.md`;
- fresh later admission/rotation reports, including P15/P16 terminal admission holds and current R7 shard admission work;
- the newest P04/I0101 report for the directed audit duty.

Large connector-returned ledgers were not treated as byte-for-byte visual rereads when truncated. For decisions below I used exact paths, exact claim files, commit history, and source-specific searches.

The controlling I0126 handoff is

`proofnet24/P03-fei/handoffs/2026-09-17T18-37-02Z__I0126-hard-handoff.md`

at creation commit `c35478245466ef984c3c4c89381be62e54a1cf48`, blob `fc6799e9f66e38c21ec7a8fd0e234023fb2e1225`.

It explicitly forbids a third P03 I0126 recovery and requires successor admission rather than silent restart.

## 3. Admission screen: historical READY labels are not current availability

Exact repository search for the historical phrase `READY / HARD / UNASSIGNED` recovers the old admission table and subsequent owner claims. In particular:

- I0028 now has a canonical HARD claim;
- I0078 now has a canonical HARD claim;
- I0079 has a canonical claim under another track;
- I0002, I0007, I0008, I0043, I0067, I0073 and I0089 all have current canonical owner claims.

Thus no old READY/HARD label can be reused as current dispatch permission.

This agrees with the fresh cross-track admission reports: current queue rows are historical inventory until exact source, later-literature, history, ownership, exclusion and lane gates all pass.

## 4. Highest unclaimed HARD frontier: I0047 remains NOT READY

### Exact source

I0047 is Remco van der Hofstad, Saint-Flour / *Random Graphs and Complex Networks*, old Open Problem 3.8:

> Determine the asymptotics [of] first-passage percolation on the preferential attachment model.

The statement is broad: it does not freeze one weight-tail regime, one PA variant, one endpoint notion, or one particular asymptotic observable.

### Current literature check — 2026-09-17

A fresh dated search again recovered Joost Jorritsma and Júlia Komjáthy, *Weighted distances in scale-free preferential attachment models*, Random Structures & Algorithms 57 (2020), 823–859, DOI `10.1002/rsa.20947` / arXiv:1907.01907. They study three preferential-attachment models in the infinite-variance power-law regime with i.i.d. nonnegative edge weights and prove a two-class theory:

- in the explosive class, typical weighted distance converges to a sum of two iid finite variables;
- in the conservative class, they give the main growth term for typical weighted distance and hopcount, with tight fluctuations under a mild assumption.

This is substantial direct progress on the old broad FPP-on-PA request, not merely neighboring literature.

I also checked van der Hofstad's current 2025/2026 long-form random-graph notes, which now contain a dedicated multi-chapter first-passage-percolation treatment and updated preferential-attachment material. That current book is not a clean verbatim preservation of the old OP3.8 as a single frozen target.

### Admission verdict

`I0047 = HARD / PENDING SOURCE NARROWING / NOT READY`.

The exact remaining obstruction is semantic, not merely bibliographic: to claim I0047 one would have to choose a residual model/tail/observable not covered by the later theorems. The old source did not select such a residual. P03 will not invent one and call it the source problem.

A search miss for a still-broader all-regimes theorem is not used as proof of openness or novelty.

## 5. Next frontier rows: no lawful successor emerged

### I0049

Current repository screening records the old uniformly-grown-graph critical-threshold/window request as source-exactly resolved by later work. It is not an open successor.

### I0050

The historical row bundles several annealed configuration-model Ising clauses (limit theorems, pressure comparison, critical-value comparison). Current repository screening has already recovered substantial later work, notably Can--Giardinà--Giberti--van der Hofstad on annealed Ising models on configuration models, giving variational pressure formulas and annealed critical values in major deterministic/iid degree settings. Without a source-exact residual clause, I0050 remains a scope-reconciliation item, not READY.

### I0061

Direct fetch of `operations/claims/I0061.md` is currently 404, but that does **not** make it free. PROB20-21 already performed a full HARD run sequence on Auffinger--Damron--Hanson Question 18, including both permitted stuck recoveries, then committed `I0061 handoff: rotate hard slot to RS-2026-CL-C` at commit `741fbd7cfb72c67c8552321da171eb5b383dc1f1`. P03 therefore does not restart it as a supposedly virgin target.

The mathematical source status is also only partial: Basu--Ganguly--Sly prove upper-tail rate-function existence under an added regularity assumption, not for every bounded non-point-mass law. This makes I0061 interesting, but operationally handed off rather than available.

### I0031

Repository commit `11e9a0823189d0443c5d46bc252ae4b6a8a82205` contains the source-exact correction: Markowsky--Koolen (2010) prove `H_{uv} <= 2(n-1)` for distance-regular graphs of valency greater than two, which closes Aldous--Fill's requested `tau_0=O(n)` clause once cycles are excluded. I0031 is KNOWN for that queued clause and is not admissible.

### I0055

Current queue/admission material records the queued scope as literature-resolved. It is excluded unless a distinct exact source clause is separately re-admitted.

### I0115

The SIRSN line remains scope-sensitive. Kahn's 2016 Poisson-line construction proves a SIRSN in any dimension under its parameter conditions; Kendall's related 2017 paper constructs the scale-invariant geodesic metric/pre-SIRSN framework. The queued old source wording and the later construction must be reconciled exactly before any residual question is claimed. Status remains source-scope ambiguous / NOT READY.

### I0129 and other new finite/celebrated rows

Current canonical ownership excludes I0129 and the other recently admitted I012x rows. Recent R7 shard screens likewise create real ownership/exclusion constraints; their unclaimed source-scope investigations are not free P03 inventory.

### I0045 / I0046 / I0048

The freshest task-health delta keeps these at `HOLD_SCOPE_KNOWN_LIKELY` or equivalent source-reconciliation status after later preferential-attachment local-limit/percolation work. None is READY.

## 6. Why the admission algorithm currently fails

B20 isolates the precise failure: **unownedness and mathematical openness are both weaker than READY**. The nearest unowned HARD-looking rows fail because later literature changed the source landscape enough that a worker must choose a new residual scope. That choice is not licensed by the original source.

B25 counts availability two ways:

1. historical queue/admission labels; and
2. present canonical claims plus immutable handoffs/current-status corrections.

The first count suggests free inventory; the second removes it. Current ownership/history wins.

B30 advances one frontier at a time rather than rescanning retired P03 topics. This run advanced the I0047/I0049/I0050/I0061 frontier and found no honest promotion.

Therefore no create-only successor claim is written.

## 7. Directed P04/I0101 second audit

### Audited claim

`P04-I0101-POSITIVE-MARKOV-S3-REDUCTION-30 = PROVED / STRUCTURAL-PARTIAL`

Peer path:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T18-46-27Z__run-report.md`

Creation commit:

`6305ca5be46b08bee6f70de8b0d0cd1b20d6b291`

Blob:

`b37d0d16469174ce3aeb9d475aeadf11bf06f157`.

P03 audit ID:

`P03-AUDIT-P04-I0101-POSITIVE-MARKOV-S3-REDUCTION-255`.

### Independent derivation — positive Markov reduction

Let `H` be a graph on `n` vertices and `0<t<n`. Assume

`P=P^T`, `P 1 = 1`, `P_ii=0`, `P_ij>=0`,

with `P_ij=0` whenever `ij` is not an edge of the complement of `H`, and

`P >= -delta I`, `delta=t/(n-t)`.

Set

`A=(n-t)P`, `B=J-A`.

Then `B` is feasible for the theta dual used in the report:

- `B_ii=1`, since `A_ii=0`;
- on every edge of `H`, `A_ij=0`, hence `B_ij=1`;
- `B` is symmetric.

Now

`tI-B = tI+(n-t)P-J`.

Because `P` is symmetric stochastic, `1` is an eigenvector of eigenvalue one and `1^perp` is invariant. On `span{1}` the displayed slack has eigenvalue

`t+(n-t)-n=0`.

On `1^perp`, `J=0`, so the slack is

`tI+(n-t)P`,

which is positive semidefinite exactly when the least eigenvalue of `P` is at least `-t/(n-t)`. Hence `tI-B >=0`, so `lambda_max(B)<=t`, proving `theta(overline H)<=t`.

Conversely, inside the stated constant-row positive complement cone, if `A1=(n-t)1` and `A` is symmetric, then `P=A/(n-t)` is symmetric stochastic and the same orthogonal decomposition shows

`tI-(J-A)>=0  iff  lambda_min(A)>=-t`.

Thus the positive-cone equivalence is correct.

### Independent derivation — automorphism averaging and the free-S3 Fourier reduction

Conjugating a feasible `P` by any graph automorphism preserves symmetry, zero diagonal, nonnegativity, row sums, complement support and the PSD lower bound. Convex averaging therefore preserves feasibility.

For the clean family `p=5 mod 24`, prior P04 work establishes a free anharmonic `S_3` action. With `m=(p-5)/24`, identify vertices as `(a,h)` with `a in [m]`, `h in S_3`. Every equivariant operator has convolution form

`P_{(a,h),(b,k)} = w_ab(h^{-1}k)`.

Symmetry is exactly

`w_ba(g^{-1})=w_ab(g)`;

stochasticity is

`sum_b sum_g w_ab(g)=1`;

and complement support is the stated six-channel support mask.

The real regular representation of `S_3` decomposes as

`1 direct_sum sgn direct_sum std direct_sum std`.

For the orbit-indexed convolution operator, Fourier transform therefore gives:

- one `m x m` trivial block `Q_ab=sum_g w_ab(g)`;
- one `m x m` sign block `S_ab=sum_g sgn(g) w_ab(g)`;
- one `2m x 2m` standard block `R_ab=sum_g w_ab(g) rho_std(g)`, repeated with multiplicity two.

Hence

`P ~= Q direct_sum S direct_sum (I_2 tensor R)`,

with dimensions `m+m+2(2m)=6m`. The symmetry relation on `w` makes the three Fourier blocks self-adjoint in the corresponding real orthogonal model. Consequently

`P+delta I >=0`

is equivalent to simultaneous PSD of

`Q+delta I_m`, `S+delta I_m`, and `R+delta I_{2m}`.

This verifies the theorem's S3 reduction, not merely its first Markov step.

### Audit verdict

`P03-AUDIT-P04-I0101-POSITIVE-MARKOV-S3-REDUCTION-255 = PASS (CLAIM-SCOPED)`.

The audit does **not** certify Randomstrasse Conjecture 27, does not prove existence of the required positive chain for all large primes, and does not promote the report's future moment strategy. It certifies only the structural reduction theorem actually stated.

## 8. Exact remaining P03 obligation

P03 needs a successor whose exact primary-source quantifiers are still current, whose later literature leaves that exact scope unresolved, whose repository history does not show exhausted/retired work, and whose canonical ownership is genuinely free.

The current highest-priority unresolved admission issue is still source narrowing rather than mathematics: I0047 is the nearest unclaimed historical HARD row, but current literature already answers large natural portions of the old broad source request. It must not be claimed until an exact source-authorized residual is identified.

If a new coordinator admission delta produces a genuinely READY + HARD + UNASSIGNED row, P03 should claim it create-only and begin the first mathematical attack immediately. Until then, admission hold is the honest state.

## 9. ledger_delta for P26

```yaml
ledger_delta:
  track: P03
  category: HARD_OUTSIDE
  predecessor: I0126 / Kelly-Ulam Graph Reconstruction
  predecessor_state: HANDED_OFF_AFTER_TWO_HARD_RECOVERIES
  predecessor_metric:
    name: n_recon^cert
    value: 13
  predecessor_reopened: false
  active_successor: NONE_ADMITTED
  successor_metric: UNMEASURED_PENDING_ADMISSION
  state_before: I0126_HANDOFF_COMPLETE / ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  state_after: I0126_HANDOFF_COMPLETE / ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  successor_claim_created: false
  admission_frontier:
    I0047: HARD_PENDING_SOURCE_NARROWING_NOT_READY
    I0049: KNOWN_SOURCE_EXACT_RESOLUTION_IN_REPOSITORY_SCREEN
    I0050: LATER_LITERATURE_SCOPE_RECONCILIATION_NOT_READY
    I0061: HARD_HANDOFF_ALREADY_EXHAUSTED_BY_OTHER_TRACK
    I0031: KNOWN_SOURCE_CLAUSE_RESOLVED_2010
    I0055: QUEUED_SCOPE_LITERATURE_RESOLVED
    I0115: SOURCE_SCOPE_AMBIGUOUS_NOT_READY
    I0129: OWNED
  p04_audit:
    claim: P04-I0101-POSITIVE-MARKOV-S3-REDUCTION-30
    audit_id: P03-AUDIT-P04-I0101-POSITIVE-MARKOV-S3-REDUCTION-255
    verdict: PASS_CLAIM_SCOPED
    peer_path: proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T18-46-27Z__run-report.md
    creation_sha: 6305ca5be46b08bee6f70de8b0d0cd1b20d6b291
    blob: b37d0d16469174ce3aeb9d475aeadf11bf06f157
  shared_root_ledger_edits_by_P03: NONE
  gmail_drive_public_posting_paid_compute_workflows: NONE
```

**End of complete run report.**