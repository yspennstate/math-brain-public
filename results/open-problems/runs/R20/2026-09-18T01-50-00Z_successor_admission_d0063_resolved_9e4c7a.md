Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SUCCESSOR-METRIC MOVEMENT: `E_ready: 0 -> 0`; retired I0100 remains frozen at `p_max = 1213`, retirement count `6`; methods #6 DEFORM TO A POINT YOU CAN SOLVE, #13 FIND WHAT ONLY INCREASES, #18 SAY IT IN ANOTHER LANGUAGE.**

# R20 successor admission — D0063 is already resolved in the literature

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Worker: R20, CLOSABLE OUTSIDE.

## 1. Continuity: I0100 remains a handoff, not a live target

I did **not** reopen Afonso S. Bandeira / Randomstrasse 2025 Conjecture 26 (`I0100`). R20 reached the mandatory six-unchanged CLOSABLE boundary and wrote the controlling handoff at

`runs/R20/2026-09-17T20-50-47Z_i0100_stuck_recovery2_rotation_handoff_c6f2a9.md`

(commit `180262308c3aba578200af96694ea6ba85606df6`). The exact-certified frontier remains frozen at

`p_max = 1213`

with retained covered set

`{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`.

A fresh dated source check on 2026-09-18 still finds the current Jig root titled “Is the Lovasz theta of the Paley 1-localization asymptotic to sqrt(p/2)? — Randomstrasse101 Conjecture 26” marked **Open**. The source asymptotic therefore remains mathematically OPEN/PARTIAL; this run does not increment its retirement count or claim a seventh attack.

The neighboring Paley scopes remain distinct: P04/I0101 is the two-localization, R12/I0102 is the degree-four SoS problem, and the old C28/I0103 scope is the Paley-ETF problem. None is reassigned here.

## 2. Required repository state and admission front

Before screening I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the current NEW-METHODS deployment manifest, the latest own R20 report, current claim/search state, neighboring Paley ownership, intake-D problem/attempt material, and the newest successor-admission work surfaced by the repository.

The freshest neighboring admission report recovered in this pass is

`proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T01-03-25Z__successor-admission-delta-screen.md`.

It records that the latest coordinator reconciliation it found (`operations/task_health/runs/2026-09-18T005000Z/root_reconciliation_delta.md`) certified **zero free READY + CLOSABLE OUTSIDE + UNASSIGNED successors** in its bounded pass and that several CLOSABLE slots remain in admission gaps. I treat that as a current front-of-queue fact, not as a proof that no lawful successor exists anywhere in the intake.

R20 therefore advanced the intake cursor rather than recycling stale queue labels.

## 3. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: D0063 collapses to the exact case already proved in 2016

Candidate: `D0063`, Rhodes–Vargas, *Gaussian multiplicative chaos and applications: a review* (2014), Conjecture 6.3, Section 6.2.

The intake records the source statement as follows. For `gamma > sqrt(2d)`, after the stated supercritical normalization, the cutoff chaos measure should converge in law to `d_gamma N_alpha`, where

`alpha = sqrt(2d)/gamma`,

`N_alpha` is the alpha-stable atomic random measure indexed by derivative/critical chaos, the normalized Gibbs measure converges to `N_alpha/N_alpha(B)`, and the ranked atoms have Poisson–Dirichlet law.

The useful deformation is not a new proof. It is to identify the source's approximation class exactly. The source uses the star-scale / martingale cutoff model. Madaule–Rhodes–Vargas,

Thomas Madaule, Rémi Rhodes, Vincent Vargas, **“Glassy phase and freezing of log-correlated Gaussian potentials,”** Ann. Appl. Probab. 26 (2016), 643–690, arXiv:1310.5574,

proved the supercritical convergence for precisely star-scale invariant fields with the martingale approximation. Their limit is a purely atomic random measure whose random intensity is given by critical Gaussian multiplicative chaos.

This is not an inference from title similarity. Bertacco–Hairer (2025), in the introduction of *Uniqueness of supercritical Gaussian multiplicative chaos*, explicitly summarize the state of the art: before their paper, the continuum result of Madaule–Rhodes–Vargas already **“establishes this convergence for a particular class of log-correlated Gaussian fields known as star-scale invariant fields, using a specific approximation called the martingale approximation.”** That is the approximation in the D0063 source conjecture.

Therefore D0063 is not a current open successor. Its source-scope convergence theorem was proved in 2016.

## 4. Method #18 — SAY IT IN ANOTHER LANGUAGE: the modern notation matches the source's `N_alpha` exactly

A second scope check prevents a false positive caused by notation changes.

Bertacco–Hairer, arXiv:2504.07552 (2025), define for supercritical `gamma` an integrated atomic random measure from a Poisson point measure with jump intensity

`nu(dx) tensor z^{-(1 + gamma_c/gamma)} dz`,

where `gamma_c = sqrt(2d)` and the spatial intensity `nu` is the critical GMC (up to the deterministic local covariance factor used in their general-field setting). Thus the stable index is

`gamma_c/gamma = sqrt(2d)/gamma = alpha`,

exactly the `alpha` in Rhodes–Vargas Conjecture 6.3.

Their Theorem A proves, for a large class of log-correlated Gaussian fields and convolution approximations, stable convergence of the properly normalized supercritical measure to a positive constant times this integrated atomic measure. Their introduction also states that the 2016 theorem is the star-scale/martingale special case.

So the source's `N_alpha` and the modern `P_gamma[mu_{gamma_c}]` notation describe the same alpha-stable Poissonian atomic mechanism. The unspecified positive source constant `d_gamma` is exactly the kind of multiplicative normalization constant allowed in the later formulation; after normalizing to a Gibbs probability measure it cancels. The Poisson–Dirichlet ranked-weight consequence is the standard normalized stable-subordinator consequence and is part of the glassy-phase result.

This is strong scope evidence that the old intake label `current_status: unverified` is stale, rather than evidence for a still-open residual hidden behind notation.

## 5. Method #13 — FIND WHAT ONLY INCREASES: theorem strength strictly expanded after the source

The relevant monotone quantity here is **scope of the proven theorem**, not a mathematical scalar:

1. 2014 Rhodes–Vargas: D0063 posed the star-scale / martingale supercritical atomic-limit statement as a conjecture.
2. 2016 Madaule–Rhodes–Vargas: proved that star-scale / martingale case.
3. 2025 Bertacco–Hairer: extended the same atomic limit to general convolution approximations of a broad class of log-correlated fields, with stable convergence and uniqueness up to a multiplicative constant.

The later theorem class contains the source model rather than merely resembling it. Hence no present-day admission can honestly classify the literal D0063 source target as OPEN.

Disposition:

`D0063 = KNOWN / RESOLVED_IN_LITERATURE (source-scope theorem proved by MRV 2016; later BH 2025 substantially generalizes it)`.

This is a **literature/status correction only**, not an original result of R20, and it creates no ownership claim.

## 6. Other cursor checks and why no successor is claimed

The surrounding rows do not provide a lawful free CLOSABLE replacement in this pass:

- `D0055` is already excluded/resolved in the intake by the Chen–Dagard–Derrida–Hu–Lifshits–Shi Derrida–Retaux theorem.
- `D0056` is the exact critical Derrida–Retaux survival constant asymptotic; prior admission work classifies it as a genuine hard asymptotic-constant problem, not a finite/short CLOSABLE lane.
- `D0057` has a canonical R01 claim and a six-run handoff; it is not free inventory.
- `D0058` asks critical Derrida–Retaux moment asymptotics and remains part of the same hard critical package.
- `D0059` has a canonical R7-02 claim and source-level refutation package; it is not free inventory.
- `D0060` and `D0061` are the classical nonamenable-percolation uniqueness/nonuniqueness conjectures (`p_u<1` for one-ended transitive nonamenable graphs; `p_c<p_u` for every transitive nonamenable graph). Their universal graph quantifiers are theorem-scale and not honestly CLOSABLE by a bounded certificate.
- `D0062` is general-lattice conformal invariance/Cardy's formula, likewise a major universality problem rather than a bounded CLOSABLE target.

I did not convert any of these into a synthetic finite subproblem, steal an owner, or promote a PENDING/HARD row merely to fill the slot.

## 7. Current-source / literature query log and limitations

Dated 2026-09-18.

Source/status checks:

- current Jig / Randomstrasse Conjecture 26 status and exact root wording;
- `D0063` canonical intake entry and the campaign catalog;
- Madaule–Rhodes–Vargas, arXiv:1310.5574 / Ann. Appl. Probab. 26 (2016), “Glassy phase and freezing of log-correlated Gaussian potentials”;
- Bertacco–Hairer, arXiv:2504.07552 (2025), “Uniqueness of supercritical Gaussian multiplicative chaos,” especially the introduction's explicit description of the 2016 star-scale/martingale result and Theorem A / Definition 1.8.

Web queries included:

- `atomic limit supercritical glassy Gaussian multiplicative chaos Rhodes Vargas 2014 open problem solved freezing stable atomic measure`
- `supercritical Gaussian multiplicative chaos atomic measure Poisson Dirichlet stable limit`
- `Conjecture 6.3 Rhodes Vargas Gaussian multiplicative chaos supercritical solved`

Search is bounded and is not a general novelty search. Here, however, the positive later theorem and its explicit statement that MRV 2016 proves the star-scale/martingale case are enough to classify the literal source scope as known.

## 8. Model/runtime control

The runtime actually available to this report identifies as **GPT-5.6 Sol**. Reasoning effort is not exposed as authenticated runtime metadata, so it is **UNVERIFIED**. The task text asks for GPT-6 / maximum, but the scheduler/task-management controls exposed to this worker still do not provide a binding model-family selector, a reasoning-effort selector, authenticated per-run applied-model telemetry, or a guaranteed one-hour execution field.

The historical P26 `You cannot modify this task` event remains an authorization-context boundary. The lawful remedy is an owning/admin-authorized product or backend surface, or platform support that exposes those controls; there is no legitimate permission-bypass workaround. No scheduler or permission setting was changed in this run.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R20
  allocation: CLOSABLE_OUTSIDE
  repository: yspennstate/math-open-problems
  branch: master
  continuity:
    I0100:
      source: Bandeira_Randomstrasse_2025_Conjecture_26
      status: OPEN_PARTIAL_RETIRED_HANDOFF_DO_NOT_REOPEN
      metric_name: largest_admissible_prime_with_matching_exact_primal_dual_certificates
      metric_before: 1213
      metric_after: 1213
      unchanged_count_at_handoff: 6
      active_research_this_run: false
      covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
  successor:
    status: SUCCESSOR_ADMISSION_REQUIRED
    active_source: NONE
    claim_created: false
    metric_name: E_ready
    metric_before: 0
    metric_after: 0
    movement: none
  methods_actually_tried: [6,13,18]
  material_status_correction:
    problem_id: D0063
    source: Rhodes_Vargas_GMC_review_2014_Conjecture_6_3
    previous_intake_status: current_status_unverified
    corrected_status: KNOWN_RESOLVED_IN_LITERATURE
    exact_source_scope: star_scale_martingale_supercritical_atomic_limit
    resolved_by:
      - Madaule_Rhodes_Vargas_2016_glassy_phase_freezing
    later_generalization:
      - Bertacco_Hairer_2025_uniqueness_supercritical_GMC
    ownership_claim: false
  screened_near_cursor:
    D0055: KNOWN_EXCLUDED
    D0056: HARD_ASYMPTOTIC_NOT_CLOSABLE
    D0057: OWNED_AND_HANDED_OFF_NOT_FREE
    D0058: HARD_CRITICAL_ASYMPTOTIC_PACKAGE
    D0059: OWNED_SOURCE_LEVEL_REFUTATION_NOT_FREE
    D0060: HARD_GLOBAL_PERCOLATION
    D0061: HARD_GLOBAL_PERCOLATION
    D0062: HARD_UNIVERSALITY
    D0063: KNOWN_RESOLVED_IN_LITERATURE
  remaining_obligation: >-
    Continue successor admission beyond D0063. Claim only a current-open,
    ownership-clear, source-level CLOSABLE outside target; do not reopen I0100.
  next_methods: [10,16,24]
  closure_claim: false
  github_delivery: pending_readback
```

## 10. Next cursor

Advance beyond D0063 using **#10 DERANDOMIZE, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #24 FIND THE EXTREMAL OBJECT**, looking specifically for a source whose full quantifiers can be closed by one explicit construction/counterexample, a finite extremal classification, or one short sharp inequality. Do not revisit D0055–D0063 absent a material status or ownership change.

**NO I0100 CLOSURE CLAIM. NO SUCCESSOR CLAIM THIS RUN. R20 remains `SUCCESSOR_ADMISSION_REQUIRED`.**