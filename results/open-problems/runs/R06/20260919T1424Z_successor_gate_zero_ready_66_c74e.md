Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. ROTATED / NO SUCCESSOR METRIC STARTED: frozen `ROMERO-2025-SPLIT8` remains `R_SPLIT8: 0 -> 0`, its exact `n=8` closure gate remains `1/2 -> 1/2`, frozen I0056/H_{5,5} width remains `0 -> 0`, and successor-admission metric `E_ready: 0 -> 0`; methods #22 READ THE FAILURES, #27 SWAP/KEEP THE QUANTIFIERS EXACT, #4 PROVE SOMETHING WEAKER COMPLETELY (settle the admission subproblem rather than invent a theorem).**

# R06 CLOSABLE OUTSIDE — mandatory post-ROMERO successor gate

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only.

## 1. Lifecycle first: ROMERO owner-side research is rotated

I continued from the immutable R06 handoff

`runs/R06/20260919T1320Z_romero_max4_nextcoeff_rotation_65_6d2e.md`

created at commit

`aec5e3df7b046ede3befb6cda1e280977575ac53`.

That report is controlling for this run: the canonical `ROMERO-2025-SPLIT8` metric had already reached zero and then remained unchanged for six supported runs. The CLOSABLE lifecycle therefore requires rotation. I did **not** add another Romero theorem, coefficient computation, enumeration, or checker.

The retained exact finite-layer state is:

- target `ROMERO-2025-SPLIT8`, `n=8`, `m=14,...,26`;
- metric `R_SPLIT8=0`;
- mathematical package `CANDIDATE_COMPLETE`;
- P26 audit `P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64 = PASS_FULL_MATHEMATICAL_PROOF`;
- genuinely distinct OTHER-task audit still absent, so closure gate remains `1/2`;
- unrestricted Romero/Brown--McMullin problem remains PARTIAL/OPEN.

The newest visible P26 chain still preserves the Romero second-audit gate as pending and explicitly rotates P26 away from redundant Romero rechecks. P26 cannot count itself twice.

No canonical claim is silently released by this report. The predecessor is preserved for a future distinct audit or explicit owner-authorized handoff.

## 2. Required repository refresh

Before screening a successor I reread/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the canonical `operations/claims/ROMERO-2025-SPLIT8.md` and the newest R06 report;
- the newest P26 report and current coordinator/admission screens;
- targeted intake/claim history for candidates actually screened;
- the exact Git delta from the preceding R06 creation commit.

The pre-write delta from `aec5e3df...` to the then-current master was **86 commits ahead, 0 behind**. Subsequent master activity was also inspected before this write. The visible delta contains new research/checker reports, a release of HARD target H0008, a release/reassignment history for HARD target P0157, and a retirement handoff for P0336 that current admission screens explicitly say is **not** a canonical release. It contains no new source-current, ownership-clear CLOSABLE successor for R06.

The freshest coordinator status recovered in this run likewise reports **zero newly certified free READY CLOSABLE inventory** and several targetless CLOSABLE gates. Root `QUEUE.md` still distinguishes sixty listed sourced candidates from certified READY/unassigned inventory; a listed row is not dispatch permission.

Therefore this run uses

`E_ready` = number of source-clean, current-open, genuinely CLOSABLE, ownership-clear outside successors that R06 can lawfully claim now.

Before: `0`.  
After: `0`.

No new source metric is started.

## 3. Original I0056 source remains frozen exactly

The preserved source is Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

R06's frozen source-exact subclass remains the regular co-regular tessellation `H_{5,5}` with outer vertex-boundary normalization

\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_V K|}{|K|},
\]

and

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad
[L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

The **full** Question 6.20 remains PARTIAL. A fresh 2026-09-19 primary-literature check again confirms that Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, establish the vertex-isoperimetric constants for the triangular and square hyperbolic lattices, i.e. codegree 3 and 4. Those regimes remain prior art and are not relabelled as fleet results.

Root `POSTED.md` also records the outer-vertex-isoperimetry manuscript as already posted, so the I0056 predecessor is not reopened merely because this native title still names it.

## 4. Method #22 — read the failed admission work instead of recycling a stale queue row

The most plausible unclaimed-looking historical queue exception remains I0074, David Aldous, *A conjectured compactification of some finite reversible MCs*, Conjecture 1. Multiple previous gates stopped on a source-scope issue rather than a lack of ideas.

I refreshed the primary sources on 2026-09-19 rather than treating a missing canonical claim as readiness.

Aldous's current status page still says that Henry Towsner's *Limits of Sequences of Markov Chains* provides a **measure-theoretic** limit construction, while construction of a version with nice topological properties remains open. Towsner's Section 7 also makes the uniqueness issue precise: raw density-array uniqueness for pseudofinite Markov chains is false; he gives two non-isomorphic chains with the same density array. He then canonicalizes by twin-freeness and saturation, and Theorem 7.5 proves uniqueness up to null sets for twin-free saturated pseudofinite chains under the stated sigma-algebra hypothesis.

This does not repair Aldous's source into a dispatchable finite CLOSABLE target. The original note leaves its small-time technical condition unspecified, so one cannot honestly assert either that Towsner's blob counterexample satisfies Aldous's intended class or that Towsner's canonical hypotheses are exactly the missing condition.

Current dispatch classification therefore remains:

`I0074 = UNASSIGNED_RESERVE / PENDING_SOURCE_REPAIR_UNSPECIFIED_UTC / NOT_READY`.

This is an admission diagnosis, not a new theorem and not a claim that the author's intended statement is refuted.

## 5. Method #27 — keep the source quantifiers rather than manufacture closability

The current reserve contains many mathematically attractive rows that become easy only after changing their quantifiers. That is not allowed.

Concrete current examples from the repository delta/current screens:

- **H0008** has an explicit release, but current gate reports classify it HARD OUTSIDE; release does not change category.
- **P0157** has release/handoff evidence, but it is HARD-shaped and does not become a CLOSABLE successor for R06.
- **P0336** has a six-run retirement handoff, but current R02/NM13 admission records explicitly say `retired not released`; R06 cannot steal it.
- **I0106** has improved source metadata from the 2023 stochastic-reinforcement open-problem collection, but the current source analysis still leaves it `PENDING_SCOPE`/not READY rather than a certified finite CLOSABLE endpoint.
- **I0074** becomes much cleaner after adding Towsner's twin-free/saturated hypotheses, but that would replace the source's unspecified intended class by a repaired problem of our own.

Thus neither weakening `for every source-admissible object` to `for one convenient subclass`, nor replacing a source's missing hypothesis by a modern canonical one, is accepted as a new assignment.

## 6. Method #4 — completely settle this run's smaller obligation: is there a lawful successor now?

The smaller obligation for a post-rotation run is not to solve another famous theorem before ownership is established. It is to decide the dispatch predicate completely on the material current delta:

`exact outside source` + `current-open exact scope` + `CLOSABLE shape` + `ownership clearance` + `no posted/retired/known exclusion`.

On the current repository state the answer is **no**.

Evidence used in this run includes:

1. the coordinator's current `newly_certified_free_ready_closable = 0` result;
2. fresh claim checks showing front-queue candidates such as I0011, I0035, I0066, I0095, and I0032 are already owned;
3. I0055 is literature-resolved/KNOWN in its corrected queued scope;
4. RS-2026-DC34 is owned by C29;
5. the current I0074/Towsner source repair obstruction above;
6. newly released H0008/P0157 are HARD rather than CLOSABLE;
7. P0336 is retired but explicitly not canonically released;
8. the current Romero package itself cannot be recycled because its owner-side lifecycle reached the mandatory six-run rotation threshold.

Therefore

\[
\boxed{E_{ready}:0\longrightarrow0}
\]

and R06 remains

`SUCCESSOR_ADMISSION_REQUIRED / TERMINAL_WAIT_ON_CANONICAL_CLOSABLE_ADMISSION`.

No claim file is created. No finite mathematical claim is newly asserted, so no checker-only artifact is manufactured.

The next invocation should be **delta-only first**: inspect newly populated source rows, explicit canonical releases, coordinator admissions, or material literature-status changes after this report. If a genuinely READY + CLOSABLE + unassigned target appears, claim it create-only and begin research in that same run. Otherwise preserve the gate rather than repeat the completed Romero work or this I0074 scope analysis.

## 7. Model / reasoning / scheduler truth

The limitation remains unchanged in the control surface actually available here. It exposes task identity/title, prompt, schedule/timing mode, enabled state and run timestamps, but **no binding model-family selector, no binding reasoning-effort selector, no guaranteed hour-long-execution field, and no authenticated applied-run model/reasoning receipt**. GPT-6/maximum therefore remains a prompt request only.

Making GPT-6/maximum enforceable would require an owner/admin/product/API scheduling surface that persists explicit model-family and reasoning-effort fields into inference routing and returns trustworthy per-run attestation, or a platform-side feature change exposing those controls.

The historical P26 `You cannot modify this task` result remains an authorization-context boundary, not something to bypass. Repository deployment evidence records that another authorized context later updated P26 successfully. The lawful workaround is the owning/authorized context, supported ownership transfer, or platform support for the same task; not duplicate-task creation or permission circumvention.

No scheduler mutation is attempted in this worker run.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  track: R06
  lane: CLOSABLE_OUTSIDE
  run_id: 20260919T1424Z_successor_gate_zero_ready_66_c74e
  original_source:
    id: I0056
    source: "Lyons--Peres, Probability on Trees and Networks, Question 6.20"
    frozen_regime: "H_{5,5}, outer vertex-boundary normalization |partial_V K|/|K|"
    interval_before: "[sqrt(5), sqrt(5)]"
    interval_after: "[sqrt(5), sqrt(5)]"
    width_before: 0
    width_after: 0
    source_status: "PARTIAL; triangular/quadrangular Haslegrave--Panagiotis cases excluded as prior art"
  rotated_predecessor:
    target: ROMERO-2025-SPLIT8
    metric: R_SPLIT8
    before: 0
    after: 0
    supported_unchanged_count: 6
    audit_gate_before: "1/2"
    audit_gate_after: "1/2"
    status: "CANDIDATE_COMPLETE / AUDITS_PENDING / OWNER-SIDE ROTATED"
  active_gate:
    metric: E_ready
    before: 0
    after: 0
    movement: NO_MOVEMENT
    status: SUCCESSOR_ADMISSION_REQUIRED
  methods_this_run: [22, 27, 4]
  material_delta:
    - "fresh coordinator/admission state still certifies zero free READY CLOSABLE successors"
    - "H0008 released but HARD OUTSIDE"
    - "P0157 released/handoff but HARD OUTSIDE"
    - "P0336 retired handoff is explicitly not a canonical release"
    - "I0074 remains NOT_READY after fresh Aldous/Towsner source-scope check"
  successor_claim_created: false
  new_checker_created: false
  audit_ids:
    - "P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64=PASS_FULL_MATHEMATICAL_PROOF"
  remaining_obligation: "on a material repository/source-status delta, admit the next exact source-current ownership-clear CLOSABLE outside target create-only; otherwise preserve the terminal admission gate"
  delivery: "own immutable R06 report only; no shared-root edit"
```
