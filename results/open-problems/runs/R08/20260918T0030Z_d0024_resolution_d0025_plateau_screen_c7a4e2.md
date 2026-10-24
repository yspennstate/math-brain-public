Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **ROTATION-SCREEN MOVEMENT: D0024 moved from `source_says_open / current_status=unverified` to `KNOWN / resolved in later literature` in the source's intended one-dimensional ergodic site-disorder scope; D0025's site-disordered K=1 plateau clause is KNOWN but its full general-K/source scope is not certified closed and is HARD rather than CLOSABLE. No successor metric was admitted. I0082 remains RETIRED/FROZEN at `2/3`, retirement count `6`. Methods actually used: B20 FIND WHY THE ALGORITHM FAILS, B22 READ THE FAILURES, B30 ONE SCALE/ONE ROW AT A TIME.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — successor screen through D0024/D0025

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. The canonical claim file still contains its old `ADMITTED_ACTIVE` wording from 16 September, but the later immutable R08 history is controlling for this worker: the frozen metric is `2/3`, the six-unchanged retirement limit was reached, and I0082 is RETIRED/FROZEN. The fixed F0083 expanding-tube candidate is likewise RETIRED/HANDED OFF at `1/2` after six unchanged runs and is not reopened.

The newest complete R08 report recovered before this run is

`runs/R08/20260917T2326Z_i0048_threshold_comparison_73b9e1.md`.

That report finished the I0048 threshold-comparison screen and left R08 with no active successor metric. I preserved that state rather than fabricating `0` for an unadmitted quantity.

I reread the required campaign and fleet surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the I0082 claim, the newest own reports, the newest relevant neighboring admission reports, and the D-intake tranche around D0016--D0026. The latest task-health reconciliation available in the repository still certifies **no** free `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor; D0012 is `HOLD_SCOPE / PENDING`, not READY. R15 independently removed D0019 as KNOWN and classified D0016--D0018 as hard simultaneous-exceptional-slice problems. R7-03 independently classified D0026 as a genuinely infinite-volume/all-q KCM theorem, HARD rather than CLOSABLE.

The root queue is therefore treated only as a source list. I did not create a claim merely because an old intake row says `admitted=true`.

## 2. B30 — advance one source row at a time instead of jumping to a convenient theorem

After the already-screened D0012--D0019 tranche, the next relevant rows are:

- D0020: Khoshnevisan Open Problem 5, multiplicative-noise hyperbolic SPDE slice theory. The intake's own obstruction is uniform multi-point Malliavin-density control replacing the additive Brownian-sheet independent-rectangle structure. This is a broad continuum theorem, not an honest CLOSABLE endpoint.
- D0021: Khoshnevisan Open Problem 6, slice theory for a linear parabolic SPDE. Neighboring screens also classify it as broad/HARD.
- D0022: already resolved in later literature; excluded.
- D0023: Seppaläinen Problem 2, a rigorous finer-scale description of condensation/excess mass on exceptionally slow sites. There is substantial later zero-range condensation literature, but the source request is a broad dynamical/finer-scale description rather than a single frozen endpoint. I did not silently replace it by a static finite-volume condensate-location theorem.
- D0024: Seppaläinen Problem 3, weak convergence from a spatially ergodic start. This is where the current-literature check produced a direct source-level answer.
- D0025: Seppaläinen Problem 4, phase transition / flat segment of the disordered exclusion flux. Its K=1 site-disorder core has later rigorous solutions, but its larger K formulation is not thereby closed.
- D0026: FA-1f convergence from every initial law with the stated infection-gap tail, every q>0; already independently screened as HARD.

This row-by-row localization prevents two recurring admission errors: treating a broad programme as a closable theorem because one special case has a clean formula, and starting research on a source whose literal question was already answered later.

## 3. D0024 — source statement

The intake source is Timo Seppaläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes* (arXiv:math/9906194; 1999), Problem 3, Section 4. In the source's site-disordered zero-range setting it asks, after fixing the rate environment `alpha` and taking the initial distribution spatially ergodic with density `rho`:

1. does the distribution of `eta(t)` converge weakly as `t -> infinity` to one of the product equilibria `nu_phi^alpha`?;
2. in the phase-transition regime, if `rho > rho_*`, does it converge to the critical equilibrium of density `rho_*`?

The source's surrounding setup is a random/ergodic site-rate environment, subsequently fixed in the quenched problem. I do **not** reinterpret the question as quantifying over arbitrary pathological deterministic environments outside those standing assumptions.

## 4. B22 — later literature directly answers D0024

The decisive later paper is:

Christophe Bahadoran, Thomas Mountford, Krishnamurthi Ravishankar, Ellen Saada, **“Quenched convergence and strong local equilibrium for asymmetric zero-range process with site disorder,”** *Probability Theory and Related Fields* 176 (2020), 149--202, DOI `10.1007/s00440-019-00916-2`, arXiv:1804.06148.

Primary source: https://arxiv.org/abs/1804.06148

This is the same one-dimensional nearest-neighbour asymmetric zero-range model with site disorder, and it is more general in the jump-rate function: `g` may be any bounded nondecreasing rate function satisfying their standard normalization. The paper explicitly states that its environment assumptions are satisfied almost surely for a spatially ergodic random environment (in particular i.i.d. disorder), which is the source setting.

Its large-time convergence theorem treats a **given initial configuration** with an asymptotic density of particles to the left. The paper explains the conclusion in precisely the source's language: an out-of-equilibrium configuration converges to the product invariant measure of density `rho` for `rho < rho_c`, and to the critical invariant measure for `rho >= rho_c`. The abstract itself states that convergence from given initial configurations with an asymptotic left density is obtained as a byproduct of the quenched strong-local-equilibrium theorem.

This is already stronger than requiring the initial state to be sampled from a spatially ergodic law.

### 4.1 Exact quantifier reduction from the source's random initial law

Let `Lambda` be the source's spatially ergodic initial law of density `rho`. By the ergodic theorem, for `Lambda`-almost every initial configuration `eta_0`,

`lim_{n->infinity} (1/(n+1)) sum_{x=-n}^0 eta_0(x) = rho`

(with the standard integrability implicit in the finite-density hypothesis).

For every such realization, the later quenched convergence theorem applies to the deterministic initial configuration `eta_0`, yielding

`Law_alpha(eta_t | eta_0) => mu^{alpha, rho wedge rho_c}`.

For any bounded cylinder observable `F`, bounded convergence then integrates this conditional convergence over `eta_0 ~ Lambda`:

`E_Lambda E_alpha[F(eta_t) | eta_0] -> int F d mu^{alpha, rho wedge rho_c}`.

Hence the process started from the source's spatially ergodic initial law converges weakly to exactly the equilibrium requested in Problem 3, and for `rho > rho_c` the limit is the critical equilibrium.

No additional stochastic-independence trick is required after the environment is fixed: the later theorem is configuration-by-configuration for every initial configuration satisfying the asymptotic-density hypothesis.

### 4.2 Honest scope label

Therefore, in the source's intended quenched ergodic-disorder setting,

`D0024 = KNOWN / RESOLVED_IN_LATER_LITERATURE`.

This is a source-status correction, **not** a new R08 theorem. I am not claiming a theorem for deterministic environments excluded by the later paper's environment assumptions; that would be a broader question than the historical source's random-environment formulation.

No canonical `operations/claims/D0024.md` exists at the captured master state, and none is created because a resolved source is not admissible inventory.

## 5. B20 — why the admission algorithm would have failed on D0025

The next row, D0025, is Seppaläinen Problem 4. The intake records the source question as asking whether the disordered totally asymmetric exclusion process has a phase transition analogous to the disordered ZRP and whether its flux `f_K(rho)` has a flat segment around `rho=K/2`.

A naive queue-driven admission would treat the old `current_status=unverified` label as permission to begin a new proof. That is wrong: the K=1 site-disorder core has already been proved.

Two later primary results are decisive for that core:

1. Christophe Bahadoran and Thierry Bodineau, *Quantitative estimates for the flux of TASEP with dilute site disorder* / earlier preprint *Existence of a plateau for the flux function of TASEP with site disorder*, proved a plateau under quantitative disorder assumptions.
2. Allan Sly, **“Note on the flux for TASEP with general disorder,”** arXiv:1609.06589, then removed those special-tail/dilution restrictions for i.i.d. site disorder and proved that the flux **always has a plateau of densities around `1/2`**.

Primary source: https://arxiv.org/abs/1609.06589

Thus the literal plateau phenomenon for ordinary site-disordered TASEP (`K=1`) is not an open target.

But the historical source writes the bounded-occupancy flux as `f_K` and asks in a general K-exclusion formulation. The K=1 theorem does not by itself prove the corresponding statement for every finite capacity `K`, nor does it automatically answer every model variant suggested in the surrounding discussion. The newest independent admission screen in this repository likewise classifies D0025 as an infinite asymptotic classification / genuinely HARD problem rather than a CLOSABLE assignment.

So the honest disposition is:

`D0025 = SITE_K1_PLATEAU_KNOWN / FULL_SOURCE_GENERAL_K_SCOPE_UNFROZEN / HARD_NOT_CLOSABLE`.

I did not create a D0025 claim and did not pretend the K=1 theorem closes the general-K source wording.

## 6. Method accounting

### B20 — FIND WHY THE ALGORITHM FAILS

The obvious admission algorithm is “take the next unclaimed source-says-open row.” D0024 and D0025 show why that algorithm fails. D0024 is stale and solved; D0025 contains a major solved core but a broader residual scope. Admission must be source- and scope-aware rather than row-label-aware.

### B22 — READ THE FAILURES, NOT THE SUCCESSES

Instead of trying a fresh convergence proof for D0024, I followed the exact difficulty named by the source—large-time weak convergence in a quenched disordered ZRP—into the later Bahadoran--Mountford--Ravishankar--Saada line. Their 2020 theorem is exactly the missing convergence result and is stronger on initial conditions.

### B30 — ONE SCALE / ONE ROW AT A TIME

I advanced only through the next source rows and separated D0024's literal convergence predicate from D0025's plateau predicate and from D0023's much broader condensate-profile programme. This prevented cross-problem results from being counted as closure.

No exact-arithmetic checker was created: the substantive output of this run is a source/current-literature/quantifier determination, not a finite mathematical claim. A checker here would be bookkeeping without a finite core to certify.

## 7. Admission result

There is still no lawful R08 successor at the end of this run.

- D0020: open-looking but broad/HARD.
- D0021: broad/HARD.
- D0022: KNOWN.
- D0023: broad condensation-profile programme; no source-frozen CLOSABLE endpoint admitted.
- D0024: **KNOWN / resolved in later literature**.
- D0025: K=1 site plateau KNOWN; full general-K residual scope HARD / not certified CLOSABLE.
- D0026: HARD by independent full-row screen.

Therefore no ownership claim, no candidate-specific metric, and no stagnation count are instantiated. Unknown/uninstantiated quantities remain unknown; I do not reset them to zero.

The next lawful R08 action is to continue the exact source/current-literature/ownership cursor beyond this tranche and look specifically for a source whose **literal full statement** is a sharp constant, explicit construction/counterexample, or finite/parametric endpoint. Do not return to I0082, F0083, I0048 threshold scope, or these resolved D0024/K=1 D0025 clauses.

## 8. Model / scheduler-control status

The model-control situation is unchanged. The exposed task-management schema provides title, prompt, schedule, timing mode and enablement, but no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run telemetry. Hence GPT-6/maximum remains request text only and cannot be certified by this worker.

The repository's current deployment record also says that an earlier P26 “You cannot modify this task” result was an authorization-context boundary rather than a mathematical issue; later work succeeded from another authorized context. The lawful remedies for a task that still refuses modification are its authorized owning context, supported ownership/admin transfer, or platform support. Duplicating a task or editing GitHub does not enforce its runtime model.

No scheduler, permission, email, Drive, public-posting, purchase, workflow or access change was made.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R08
  model_actual: GPT-5.6 Sol
  reasoning_actual: UNVERIFIED
  preserved_retired_source:
    id: I0082
    metric: "2/3"
    status: RETIRED_FROZEN
    retirement_count: 6
  preserved_retired_route:
    id: F0083
    metric: "1/2"
    status: RETIRED_HANDOFF
    unchanged_count: 6
  active_successor: null
  active_metric: null
  methods: [20, 22, 30]
  material_status_changes:
    - id: D0024
      before: "source_says_open / current_status=unverified"
      after: "KNOWN / RESOLVED_IN_LATER_LITERATURE"
      resolver: "Bahadoran-Mountford-Ravishankar-Saada, Quenched convergence and strong local equilibrium for asymmetric zero-range process with site disorder, PTRF 176 (2020), 149-202"
      source_match: "spatially ergodic initial law reduces a.s. by Birkhoff to the later theorem's deterministic asymptotic-left-density hypothesis; rho>=rho_c converges to critical invariant measure"
    - id: D0025
      before: "source_says_open / current_status=unverified"
      after: "SITE_K1_PLATEAU_KNOWN / FULL_SOURCE_GENERAL_K_SCOPE_UNFROZEN / HARD_NOT_CLOSABLE"
      known_core: "Allan Sly, arXiv:1609.06589: iid site-disordered TASEP flux always has a plateau around density 1/2"
  ownership:
    D0024: "no canonical operations/claims/D0024.md at captured master; no claim created because source resolved"
    D0025: "no canonical operations/claims/D0025.md at captured master; no claim created because full scope is HARD/not CLOSABLE"
  successor_admitted: null
  stagnation_count: UNKNOWN_NOT_APPLICABLE_PRE_ADMISSION
  exact_checker: none_required_for_literature_status_correction
  remaining_obligation: "Find a current-open, source-exact, ownership-clean, genuinely CLOSABLE outside successor beyond the D0020-D0026 tranche."
```
