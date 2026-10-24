Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; methods actually tried: B17, B21, B22.**

# P13 outside successor — current-author status correction for I0074

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Own root: `proofnet24/P13-outside-successor/`.  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`.

## 1. Continuity and exclusions

This run continues from the terminal D0093 handoff

`proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T07-12-48Z__d0093-sixrun-handoff-empty-gate.md`.

That report is controlling: D0093 reached six consecutive unchanged source-metric runs at `beta_fast=2` and must not receive a seventh refinement. Its clean-flush, periodic regenerative accounting, and empty-corridor results remain preserved as PARTIAL mathematics. P0082 was already handed off after six unchanged runs. I0051 / Aldous--Janson Open Problem 9 is owner-retired and was not reopened.

I reread the owner directive at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the newest P13 report above, current claims, neighboring admission reports, and the newest task-health reconciliation available on `master`. The current queue remains a PENDING candidate inventory rather than a READY certificate; stale queue titles are not dispatch authority.

P13's secondary directed-audit duty remains P14. Repository search still recovers the previously completed P13-to-P14 exact component audits and no new 2026-09-18 P14 theorem-sized package requiring a repeated audit. Those completed audits are retained rather than rerun for bookkeeping.

## 2. Mandatory first lead I0054 remains occupied and active

The owner's first successor-screen lead is I0054, Aldous--Janson arXiv:2303.02529v3, Open Problem 18, section 6.3, concerning genuinely different **DISCRETE** models with the same CTCS(infinity) scaling limit.

P13 cannot take it. The canonical file

`operations/claims/I0054.md`

names a different native owner, R11. More importantly, the newest R11 report recovered in this run is

`runs/R11/2026-09-18T07-41-04Z_i0054-fugacity-unicyclic-u018-c039-3a7d.md`,

which is active current work and moves that track's frozen obligation count `38 -> 39`. This is not a stale abandoned claim and there is no release. P13 therefore skips I0054 without duplicating its mathematics.

## 3. Live CLOSABLE front before the new screen

The next high-ranked CLOSABLE-looking rows are not free inventory. Current canonical claims cover, among others, I0075, I0012, I0032, I0027, RS-2026-DC34, RS-2026-CL-B, D0007, D0008, D0009, and D0010. The neighboring RS-2026-DC35 / CL-A / CL-C / BIS32 / TH17 / TH18 and most later famous rows are either claimed HARD targets or otherwise unavailable. The later owner-added finite rows I0120--I0127 are claimed where still open; I0128 / Sendov is now current-status corrected to KNOWN/RESOLVED; I0129 is a claimed HARD target. The newest coordinator reconciliation also records no newly certified READY source in the bounded current cursor.

That leaves I0074 as the strongest high-ranked **unclaimed-looking** CLOSABLE-shaped row worth a fresh delta screen rather than merely repeating old ownership checks.

## 4. Exact original I0074 source statement

I0074 is David Aldous, *A conjectured compactification of some finite reversible Markov chains*, Conjecture 1.

The original note considers a symmetric stationary Markov process on a probability space with transition densities `p(x,y,t)` satisfying symmetry and Chapman--Kolmogorov. Immediately after Chapman--Kolmogorov the note adds the phrase

> `with a UTC on the t downarrow 0 behavior`

and the footnote expands `UTC` only as

> `unspecified technical condition`.

For iid stationary samples `xi_i`, the note forms the infinite sampled transition-density array

`Psi = ( p(xi_i, xi_j, t) : i,j >= 1, t > 0 )`

(in the source's countable-time encoding) and states Conjecture 1: if two symmetric Markov processes have the same `Psi`, then they are isomorphic.

The missing small-time predicate is part of the admissible process class. A measurable counterexample is not source-valid unless one can prove it satisfies whatever Aldous intended by that omitted condition.

Source checked 2026-09-18:
`https://www.stat.berkeley.edu/~aldous/Research/OP/compact.html`
and linked original note / slides.

## 5. B17 — follow the source's own later formulation, not the stale queue title

**Idea before calculation.** The old queue row freezes the 2014-era uniqueness wording. Before trying to construct another counterexample, ask whether the proposer still regards that literal statement as the open endpoint.

Aldous's current Berkeley open-problem page now says, in substance, that Henry Towsner's *Limits of Sequences of Markov Chains* gives the limit construction **at the measure-theoretic level**, while it remains open to construct a version with **nice topological properties**. The page links a later slide deck (`talk_towsner_2018.pdf`).

Those slides sharpen the distinction:

1. the sampled transition-density data identify the finite chain up to state relabeling;
2. in the limit, the analogous data identify a process on `[0,1]` up to measure-preserving transformation, in the measure-theoretic sense;
3. the explicitly displayed remaining conjecture is topological: define a natural metric, suggested by an `L^2` distance between the transition kernels integrated over state and time, so that the state space becomes complete separable and the process is Feller.

The displayed candidate has the form

`d(x1,x2)^2 = int int (p^infty(x1,y,t)-p^infty(x2,y,t))^2 e^{-t} dy dt`,

with the conjectural requirements that the induced space be complete separable and that the process have the Feller property.

This is a material current-author status correction. The author no longer presents the raw old measure-theoretic compactification as the remaining problem; the open remainder is a **topological/Feller regularization**. That remainder is a different, broad analytic target and is not honestly a short CLOSABLE counterexample problem.

Result of B17: **worked as an admission discriminator.** It does not prove a new theorem, but it blocks a false admission of the stale I0074 wording.

## 6. B21 — compare the exact Towsner shape

**Idea.** The closest analogue is graphon/pseudofinite uniqueness: sampled finite statistics can fail to distinguish literal points when the state space contains twins, but a canonical twin-free quotient can be unique.

Towsner's current arXiv record for *Limits of Sequences of Markov Chains* (arXiv:1404.3815) gives exactly that shape. In Section 7 he explains that the raw density array does **not** determine an arbitrary pseudofinite chain: a two-point chain and an uncountable blob blow-up can have the same density data without being isomorphic as the original spaces. He then canonicalizes:

- Lemma 7.3 sends a pseudofinite chain to a twin-free saturated representative while preserving the transition-density information;
- Theorem 7.5 gives uniqueness, up to the appropriate measure-preserving null-set notion and minimal sigma-algebra hypotheses, for twin-free saturated representatives with the same density array.

This confirms that there are really three different statements that the stale queue title can conflate:

(A) literal isomorphism of arbitrary measurable representatives — false in Towsner's broad class;

(B) measure-theoretic uniqueness after canonical twin-free/saturated reduction — known in Towsner's framework;

(C) a canonical **topological/Feller** representative compatible with the limit construction — the current Aldous remainder.

The original note's unspecified `UTC` is exactly what prevents one from deciding, from the old page alone, whether its intended Conjecture 1 should be identified with (A), (B), or a regular subclass anticipating (C).

Result of B21: **worked as a scope decomposition.** It makes a source-faithful P13 claim impossible without rewriting the target; rewriting it to (C) would be an owner-invented reclassification from CLOSABLE to a broad topological programme, which this slot is not authorized to do.

## 7. B22 — recover the failed/partial admission history and isolate the delta

Prior R08, R15, P03 and NM13 screens already noticed two important facts and should not be relabeled as this run's discoveries:

- Towsner has a measurable blob/twin obstruction to naive raw uniqueness;
- Aldous's original `UTC` is unspecified, so a literal source counterexample cannot be certified without deciding the intended regularity class.

Those screens correctly left I0074 on scope hold. This run therefore did **not** repeat the blob calculation as new mathematics.

The useful delta is the later **current-author formulation**: Aldous's live page explicitly says the measure-theoretic limit construction is supplied by Towsner and points to the topological/Feller conjecture as what remains. A bounded 2026-09-18 search for the exact Aldous/Towsner compactification plus `Feller`/`topology` recovered the current page, Towsner's paper, and unrelated Aldous-diffusion work, but no later source-matching theorem settling this topology/Feller remainder. That is bounded negative evidence only, not a worldwide-open or novelty certificate.

Result of B22: **worked as a status correction.** I0074 should not be promoted from the queue as `READY / CLOSABLE / unassigned` merely because its canonical claim path is absent.

## 8. Admission verdict for I0074

P13 records the following current disposition:

`I0074 = NOT READY / CURRENT-AUTHOR MEASURE-THEORETIC PART SUBSTANTIALLY COVERED / ORIGINAL UTC UNDERSPECIFIED / RESIDUAL TOPOLOGICAL-FELLER PROBLEM HARD-SHAPED`.

This is deliberately not the stronger claim `I0074 solved`:

- Towsner's theorem uses a canonical twin-free/saturated measurable framework and an up-to-null-set measure-preserving notion;
- Aldous's literal old isomorphism wording plus unspecified `UTC` is not formally identical to that framework;
- the topological/Feller remainder is explicitly still open on the current author page.

But these same distinctions are enough to reject I0074 as P13's next CLOSABLE successor. No canonical claim was created.

## 9. Cursor after I0074

The immediately following ranked rows are not available to P13:

- I0027: provisional exclusive R04 reservation;
- RS-2026-DC34: C29 exclusive reservation;
- RS-2026-DC35: active HARD claim;
- RS-2026-CL-A: active HARD claim;
- RS-2026-CL-B: R15 exclusive CLOSABLE claim, source-as-printed counterexample already owned;
- RS-2026-CL-C: active HARD claim;
- RS-2026-BIS32: active HARD claim;
- RS-2025-TH17 and TH18: claimed;
- D0007, D0008, D0009, D0010: claimed CLOSABLE targets;
- D0012: current coordinator / R09 evidence leaves it HOLD_SCOPE / PENDING because later work resolves at least the standard-uniform subcase and the exact residual source scope has not been reconciled;
- I0120--I0127: claimed where active/open;
- I0128: current evidence says KNOWN/RESOLVED;
- I0129: claimed HARD.

No later populated I0131+ source row was recovered in the newest admission delta, and the newest task-health reconciliation records no newly certified READY source. Therefore P13 remains honestly **ADMISSION_PENDING** rather than taking a peer target or inventing a source.

This admission screen does **not** start a new successor stagnation counter. The successor metric is still `UNMEASURED`, never zero.

## 10. P14 secondary audit duty

P13's directed audit duty remains P14. Existing exact P13 audits of P14 components are preserved. No new P14 theorem-sized end-to-end claim appeared in the checked 2026-09-18 P14 path, so repeating the old finite audits would be audit theater rather than useful work.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  lane: CLOSABLE_OUTSIDE
  state: ADMISSION_PENDING
  predecessor:
    source_id: D0093
    state: SIX_UNCHANGED_CLOSABLE_HANDOFF_PRESERVED
    metric: beta_fast
    value: 2
    reopened: false
  retired_exclusions:
    I0051: OWNER_RETIRED_NOT_REOPENED
    P0082: SIX_RUN_HANDOFF_PRESERVED
  mandatory_first_lead:
    source_id: I0054
    disposition: OWNED_ACTIVE_R11_SKIP
    latest_obligation_count_seen: 39
  screened_lead:
    source_id: I0074
    claim_created: false
    prior_claim_path_present: false
    disposition_before: PENDING_SOURCE_CLASS_UNDERSPECIFIED_NOT_READY
    disposition_after: NOT_READY_MEASURE_THEORETIC_PART_COVERED_RESIDUAL_TOPOLOGICAL_FELLER_HARD
    current_author_delta: >-
      Aldous current page says Towsner supplies the measure-theoretic limit construction;
      linked slides state the remaining conjecture as a natural complete-separable topology
      making the process Feller.
  metric:
    name: UNFROZEN_UNTIL_ADMISSION
    before: UNMEASURED
    after: UNMEASURED
  mathematical_movement: false
  admission_status_movement: true
  section_B_methods:
    attempted: [17, 21, 22]
    notes:
      B17: followed current-author formulation and separated stale uniqueness wording from current topology/Feller remainder
      B21: decomposed raw/twin-free/topological uniqueness using Towsner pseudofinite-chain structure
      B22: recovered prior failed admission screens and isolated the new current-author status delta
  successor_unchanged_runs: NOT_APPLICABLE_PRE_ADMISSION
  successor_recoveries_used: 0
  audits:
    P26: NOT_APPLICABLE_PRE_CLAIM
    P14_directed: NO_NEW_END_TO_END_PACKAGE_FOUND; PRIOR_COMPONENT_AUDITS_RETAINED
  next_step: >-
    Continue the strict delta-only CLOSABLE admission cursor. Do not restart I0054,
    I0074, D0093, P0082, or I0051. Admit only a genuinely free source whose exact
    current statement, ownership, prior attempts and literature all pass and whose
    full endpoint has a credible finite/counterexample/short-theorem route.
```

No shared root ledger, peer file, historical report, existing claim, workflow, permission, credential, email/Gmail item, Drive item, public surface, paid-compute resource, or schedule was modified. This report is the single immutable P13 file for this invocation.