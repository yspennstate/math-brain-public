Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime/scheduler surface still provides no authenticated model-family selector or reasoning-effort selector; I do not claim otherwise. **NO MOVEMENT in the retired I0076 metric: positive-route gates remain `2/4`, unchanged count remains frozen at `6`. This is a successor-admission run, not a seventh Burdzy--Scheutzow lemma. Section-B methods used: #22 READ THE FAILURES, #27 SWAP THE QUANTIFIERS, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R15 post-I0076 rotation — I0074 held on source scope, I0055 confirmed literature-resolved, no lawful successor claim

Repository / branch: `yspennstate/math-open-problems` / `master`.
Run date: 2026-09-17 UTC.

## 1. I0076 continuity: mandatory retirement remains in force

I continued from the current R15 state rather than restarting Burdzy--Scheutzow Problem 7.2.

Authoritative R15 predecessor reports:

- `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md` — six-run CLOSABLE handoff;
- `runs/R15/20260917_0058Z_rotation_scope_i0074_a21.md` — first post-retirement admission pass.

Preserved I0076 state:

- source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (2014), arXiv:1302.6958, Problem 7.2;
- exact source hypotheses: FBM + BBM + existence of an arbitrary finite random real seam `T` at which the complete centered future and past processes are independent; no stopping-time assumption and no assumption that either half at `T` is Brownian;
- source conclusion asked: does this force two-sided Brownian motion?;
- original Theorem-6.1 counterexample candidate was eliminated because it has no source-independent real seam;
- alternating Brownian-prefix/BES candidate was eliminated because Palm de-biasing gives a 2BM re-rooting;
- positive-route gates P1/P2 are proved; P3/P4 remain open;
- unresolved source obstruction is a diagonal/common-shift relative-phase invariant joining;
- active positive-route metric is frozen at `2/4`; six consecutive unchanged active runs already triggered operational retirement.

Problem 7.5 remains excluded as already settled. No new I0076 theorem or candidate is introduced here.

## 2. Required repository recovery

Before successor screening I read/recovered current `master` state including:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`, `operations/RFLEET_2026-09-16.md`, and `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the newest own R15 report;
- newest neighboring R07 report `runs/R07/20260917T0122Z_i0077_sparse_drifting_pulses_09.md`;
- newest R17 report `runs/R17/20260917_0115Z_h8exact_3d6a.md`;
- latest independent R08 successor-admission report `runs/R08/20260917T0128Z_rotation_i0074_scope_hold_7c4e21.md`;
- latest P21 six-run rotation report and current canonical ownership files on the high-ranked CLOSABLE queue front.

The intake JSONL corpus is too large for one connector rendering. I used exact-ID/source searches and current claim/admission records for the candidates touched here and do not falsely claim a byte-for-byte visual reread of all roughly 780 intake rows.

## 3. Method #22 — READ THE FAILURES: I0074 is not a clean queued open problem

The immediately preceding R15 run left I0074 at

`PENDING_EXACT_SCOPE_RECONCILIATION_WITH_TOWSNER_2015`.

I independently rechecked the original Aldous note and current status material, then read the newer R08 adjudication.

### Exact source issue

David Aldous, *Note: a conjectured compactification of some finite reversible MCs*, Section 0.3, defines the density-array law `Psi` from iid stationary samples and states Conjecture 1:

> If two symmetric Markov processes have the same `Psi` then they are isomorphic.

But immediately before the conjecture the source assumes a `UTC` on `t downarrow 0`, with the footnote literally saying `unspecified technical condition`. Its notion of isomorphism is presented as a bijection preserving the relevant two-time laws.

Henry Towsner, *Limits of Sequences of Markov Chains* (EJP 2015; arXiv:1404.3815), Section 7, identifies the exact measurable-category obstruction:

- arbitrary density arrays do **not** uniquely determine arbitrary pseudofinite Markov-chain presentations;
- Lemma 7.3 passes to a twin-free saturated quotient preserving all transition densities;
- Theorem 7.5 proves uniqueness for twin-free saturated representatives with minimal sigma-algebras, by a measure-preserving bijection up to null sets.

Aldous's current status page says Towsner gives the measure-theoretic limit construction, while a version with desirable topological properties remains open.

Therefore the queued literal Conjecture 1 does not have a clean source-exact open scope suitable for R15: omitting the unspecified UTC makes raw uniqueness false in Towsner's class; imposing the canonical quotient gives a known measurable uniqueness theorem; the remaining advertised topological problem is a different refinement and is not the literal queue target.

The newest independent R08 report reaches the same conclusion and upgrades the operational status to

`I0074 = HOLD_SOURCE_SCOPE_NOT_READY`.

I accept that current evidence rather than creating a competing R15 claim.

**Outcome of #22:** useful admission resolution; no mathematical source claim, no new R15 metric.

## 4. Method #27 — SWAP THE QUANTIFIERS: why the obvious I0074 counterexample is not source-valid

The tempting negation route is to duplicate each state by an invisible fiber so that sampled density arrays see only the quotient. This produces non-isomorphic raw presentations with identical density arrays.

The quantifier/scope problem is precisely the source's missing small-time condition. If the hidden fiber is forgotten instantaneously for every `t>0`, the construction can violate the intended `t downarrow 0` regularity. If the fiber evolves at a finite rate, the additional modes become visible in `Psi`. Towsner's quotient theorem formalizes this: the density array canonically sees types, not arbitrary multiplicities of indistinguishable points.

Thus a literal-presentation counterexample is not a valid resolution of Aldous's intended statement unless the missing UTC is first specified and verified. Conversely, imposing twin-freeness/saturation changes the quantifier/domain to a class where Towsner already proves the measurable uniqueness theorem.

**Outcome of #27:** confirms I0074 must remain a source-scope hold rather than being called OPEN, REFUTED, or KNOWN without qualification.

## 5. Method #30 — one candidate at a time: I0055 is literature-resolved, not reserve inventory

I next checked the highest queue row that still looked superficially like a probability CLOSABLE candidate but had inconsistent stale queue status: I0055, Lyons--Peres, *Probability on Trees and Networks*, Question 5.16.

The current book text states the Kahn-modified bond-percolation question and already notes that Pengfei Tang gave a positive answer. Tang's paper

Pengfei Tang, *A note on some critical thresholds of Bernoulli percolation*, arXiv:2012.01135 (2020)

states in its abstract that Kahn constructed the counterexample to the old first-moment conjecture, proposed the modification, and **the paper gives a positive answer to Kahn's modified question**.

This matches current repository successor screens (including P19/P15 records) that already exclude I0055 as literature-resolved.

Therefore:

`I0055 = KNOWN / RESOLVED in the corrected bond-percolation modified-question scope`.

It is not eligible for an R15 claim even though the stale QUEUE candidate row still appears in the preserved reserve list. R15 does not edit shared root ledgers; P26/main fleet reconciliation should remove or relabel the stale candidate row when next updating `QUEUE.md`.

**Outcome of #30:** one stale candidate conclusively removed from the admissible successor set; no claim created.

## 6. Current successor gate

I did not manufacture ownership just to keep the slot busy. Current high-ranked CLOSABLE evidence now excludes, among others:

- `I0011`: P16-owned;
- `I0035`: C31-owned;
- `I0054`: R11 provisional owner;
- `I0055`: literature-resolved by Tang 2020;
- `I0066`: P15-owned;
- `I0068`: P19-owned;
- `I0070`: owned in the current fleet;
- `I0077`: R07-owned and actively moving;
- `I0079`: R06-owned;
- `I0082`: R08 history/retirement, not free reserve;
- `I0095`: R02-owned;
- `I0098`: claimed-resolution hold;
- `I0110`: current P19 successor ownership;
- `I0113`: R01-owned;
- `I0074`: `HOLD_SOURCE_SCOPE_NOT_READY` after exact Aldous/Towsner reconciliation;
- `I0105/I0106`: source metadata/current-status admission incomplete;
- `I0003`: source-open but broad and not presently certified `READY / CLOSABLE OUTSIDE`.

The latest independent R08 and P21 rotation screens reach the same operational conclusion: no currently evidenced `READY + unassigned + CLOSABLE OUTSIDE` successor is available on the screened front. I therefore create no canonical claim in this run.

This is an admission/ownership gate, not a GitHub-access failure. The correct action is to preserve the R15 rotation hold until a genuinely admitted successor appears, rather than reopening I0076 or stealing a PENDING/HARD/owned target.

## 7. R17 independent-audit trigger

The newest R17 report is

`runs/R17/20260917_0115Z_h8exact_3d6a.md`.

It contains genuine metric movement for the binary Chvatal--Sankoff constant, improving the certified upper endpoint to

`34945/42292 = 0.8262792017402818...`

and shrinking its rigorous interval width. It also archives an exact all-state h=8 Collatz--Wielandt certificate.

However the report is explicitly **OPEN / PARTIAL** and is not a source-closure paper package. The R15 instruction is to independently audit R17 when a package is ready. That trigger has therefore **not** fired. I do not invent an audit ID or duplicate its self-check.

## 8. Model/reasoning selector and protected-task status

The implementation limit is still unchanged and is now directly supported by the current fleet manifests. The exposed task-management surface provides title/prompt/schedule/timing/enabled-state controls, but no authenticated model-family selector, reasoning-effort selector, or completed-run model telemetry. GPT-6 / maximum is therefore a prompt request only in this runtime.

Actually changing and verifying it requires a product/owner scheduler surface exposing explicit model and reasoning fields plus authenticated run metadata, or platform support. There is no worker-side setting in the currently exposed interface that can enforce it.

The historical P26 `You cannot modify this task` response is recorded as an authorization/context boundary; later repository evidence records successful edits from another authorized context. The legitimate workaround remains the owning authorized context, workspace/admin permission transfer/change, or platform support — not task duplication or a bypass. No scheduler modification is attempted here, consistent with the operative R15 contract.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R15
  run_id: 20260917_0156Z_rotation_hold_scope_a22
  predecessor:
    source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), Problem 7.2"
    intake: I0076
    status: OPEN_PARTIAL_RETIRED_AFTER_SIX_UNCHANGED_RUNS
    active_positive_metric: "P1-P4 gates proved"
    before: "2/4"
    after: "2/4"
    unchanged_count_before: 6
    unchanged_count_after: 6
    movement: "NO_MOVEMENT_RETIRED_METRIC"
    remaining_obligation: "P3 continuous diagonal/common-shift relative-phase obstruction; then P4 closure/audits"
  methods_this_run: [22, 27, 30]
  successor_screen:
    I0074:
      source: "David Aldous, compactification note, Conjecture 1"
      ownership: UNCLAIMED
      status: HOLD_SOURCE_SCOPE_NOT_READY
      reason: "UTC at t->0 explicitly unspecified; raw measurable uniqueness fails before Towsner quotient; canonical twin-free/saturated measurable uniqueness is known; open topological refinement is a different target"
      claim_created: false
    I0055:
      source: "Lyons--Peres, Probability on Trees and Networks, Question 5.16 / Kahn modified bond-percolation question"
      status: KNOWN_RESOLVED
      resolution: "Pengfei Tang, arXiv:2012.01135 (2020), positive answer to Kahn's modified question"
      claim_created: false
  successor_metric: UNMEASURED
  overall: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  R17_audit:
    newest_report: "runs/R17/20260917_0115Z_h8exact_3d6a.md"
    trigger: NOT_TRIGGERED
    reason: "genuine partial metric movement, but no source-closure package yet"
    audit_ids: []
```

No theorem-sized I0076 claim and no new finite mathematical claim is made in this admission run, so no decorative checker is created. No numerical path sample is treated as Brownian verification. No Gmail, email, Drive, public posting, purchase, permission change, shared-root edit, peer-file edit, workflow execution, or scheduler change was performed.
