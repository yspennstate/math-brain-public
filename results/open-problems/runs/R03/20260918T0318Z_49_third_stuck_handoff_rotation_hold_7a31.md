Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated applied-model/reasoning telemetry and no GPT-6/reasoning selector, so GPT-6 maximum is not claimed. F0097 NO MOVEMENT on the frozen source metric: `Omega_3 <= 0.9698` remains; F0097 unchanged count `6 -> 7`. This is the THIRD stuck episode after two permitted recoveries, so F0097 is HANDED OFF and R03 enters ROTATION / SUCCESSOR-ADMISSION HOLD rather than beginning a third recovery. Methods actually executed: #8 DISCRETIZE; #19 MAKE IT AN ALGORITHM; #28 REPLACE FOR ALL WITH FOR TYPICAL.**

# R03 run49 — F0097 terminal handoff: the proposed dual-witness recovery is already Scott–Sorkin below the pure-literal threshold

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **F0097 OPEN / R03 PARTIAL / THIRD STUCK EPISODE / TERMINAL HANDOFF / ROTATION HOLD.**

The native task title/prompt still names F0001 / sharp iid Rademacher singularity, but the canonical R03 state handed F0001 off after its own third stuck episode in `runs/R03/20260917T1907Z_41_third_stuck_handoff_f0097.md`. The create-only claim `operations/claims/F0097.md` assigned F0097 to R03 and explicitly prohibited returning to F0001 without reassignment. I therefore do not reopen F0001. This report terminates the permitted R03 recovery cycle on F0097.

## 1. Continuity and current source status

Before research I reread/recovered the required campaign state: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/F0097.md`, newest own report `runs/R03/20260918T0205Z_48_stuck_thinking_02_d7c1.md`, the preceding F0097 reports 42--47, targeted intake/attempt hits for F0097, and current neighboring rotation/admission material. No metric, killed route, finite certificate, or stagnation count is reset.

The outside source remains Alan Frieze, *Random Structures and Algorithms* / ICM 2014 random-k-SAT open-problem discussion: determine the satisfiability threshold for fixed `k=O(1)`. The current R03 source-matching target remains uniform threshold existence for every fixed `k>=3`, with `k=3` the first unresolved case.

Fresh bounded primary-status checking dated 2026-09-18 found no source-level closure:

- Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *The random k-SAT Gibbs uniqueness threshold revisited*, CPC 35 (published online 27 March 2026), still treats precise small-fixed-k satisfiability thresholds as open.
- Gaia Carenini, *The Scaling Window of Random k-SAT*, ECCC TR26-145 (publication 16 August 2026), proves an `O(n/log n)` scaling window for every fixed `k>=3`; this does not prove convergence of the threshold centers.

This is bounded dated evidence, not a worldwide novelty certificate.

The frozen metric remains

\[
\theta_{k,n}=\frac1n\min\{m:\Pr(F_k(n,m)\text{ SAT})\le1/2\},\qquad
\Omega_k=\limsup_n\theta_{k,n}-\liminf_n\theta_{k,n},
\]

with the retained conservative rigorous bracket

\[
\boxed{0\le \Omega_3\le 0.9698.}
\]

No argument below narrows this interval.

## 2. The selected second-recovery action and the decisive prior-art collision

Run48 selected exactly one final recovery action: port the quantitative dual-witness philosophy from random 2-SAT. The intended new foothold was to stratify minimal UNSAT 3-CNF cores/refutation witnesses by size/excess, build an explicit witness-exploration algorithm, and ask only for a typical-random structural theorem. Its first milestone was a summable zero-boundary estimate

\[
\Pr(F_3(n,\lfloor c n\rfloor)\text{ UNSAT})
\le C_c(\log n)^{-1-\varepsilon_c}
\tag{TAIL-c}
\]

for some fixed `c>1` in a rigorously satisfiable regime.

The fresh literature read shows that this proposed recovery, in its clean below-pure-literal form, is not new. Alexander D. Scott and Gregory B. Sorkin, *Structure of random r-SAT below the pure literal threshold*, arXiv:1008.1260, already execute all three planned moves simultaneously.

Their binomial model has each proper `r`-clause present independently with

\[
p=\alpha n^{-(r-1)}.
\]

In clause-density normalization this corresponds asymptotically to

\[
c=\frac{2^r}{r!}\alpha,
\]

because there are `2^r binom(n,r)` possible clauses. Their paper also explicitly couples the binomial and fixed-clause-count models on density intervals strictly below the pure-literal threshold, so the qualitative conclusion transfers to the standard fixed-`m` model for our purpose.

This changes the assessment of run48's proposed `TAIL-c`: **as written, it was not the simplest still-unproved special case.** A much stronger estimate is already available throughout the regime strictly below the pure-literal threshold. The genuinely unsolved dual-witness frontier starts only above that threshold.

## 3. #8 DISCRETIZE — excess stratification is already the Scott–Sorkin theorem

The intended discretization was to rank minimal unsatisfiable subformulae (MUFs) by a finite complexity such as support, excess, and exploration depth. Scott--Sorkin use exactly

\[
\operatorname{ex}(H)=(r-1)e(H)-v(H).
\]

They prove there are only finitely many MUFs of any fixed excess. More sharply, their Theorem 10 says that below the pure-literal threshold, if one conditions on UNSAT while excluding all MUFs of excess below a specified value, then with probability `1-O(1/n)` the random formula has a **unique** MUF and it has the smallest remaining admissible excess. The type distribution of that MUF is explicitly weighted by its automorphism count and clause parameter.

Thus the exact structural statement I intended to seek -- typical random UNSAT is controlled by a finite excess stratum rather than by arbitrary deterministic cores -- is already a theorem in the sparse side of the regime.

More decisively, their Theorem 12 proves, for any fixed truncation order `s_max` and uniformly for clause parameters bounded strictly below the pure-literal threshold,

\[
\Pr(F\text{ UNSAT})
=
\sum_{s=1}^{s_{\max}}p_s(\alpha)n^{-s}
+O(n^{-s_{\max}-1}),
\]

with explicitly computable polynomial coefficients. In particular

\[
\Pr(F\text{ UNSAT})=O(n^{-1})
\]

in that regime. By their monotone binomial/fixed-`M` coupling, for every fixed standard clause density `c` strictly below the 3-SAT pure-literal threshold one likewise obtains a polynomially small UNSAT tail (in particular an `O(n^{-1})` upper bound after bracketing by a slightly denser binomial model still below the threshold).

Therefore the planned polylogarithmic `TAIL-c` milestone is far weaker than known literature on a nontrivial interval `c>1`.

**Outcome of #8:** prior-art collision, not progress on `Omega_3`. The excess language is useful for the handoff, but it cannot be presented as a new R03 mechanism below the pure-literal threshold.

## 4. #19 MAKE IT AN ALGORITHM — the witness algorithm is also already present

Run48 proposed making the dual witness constructive: start from an exposed clause/variable neighborhood, grow a candidate minimal UNSAT core, and attempt to dominate the exploration by a subcritical process.

Scott--Sorkin again already reach the algorithmic version in their regime. Their introduction states that a typical rare UNSAT formula below the pure-literal threshold has a quickly findable witness, and they give efficient algorithms (for sufficiently sparse random formulae) that decide satisfiability and, on UNSAT inputs, output a minimal unsatisfiable subformula. Their analysis is powered precisely by the fact that large/full subformulae are strongly suppressed below the pure-literal threshold and bounded-excess obstructions form a finite catalogue.

The point where this algorithmic philosophy ceases to solve the problem is also identified by the paper: between the pure-literal threshold and the satisfiability threshold, they explicitly state that the structure remains open. Above the pure-literal threshold, a linear core persists, so the finite-excess catalogue no longer captures all rare UNSAT events. A new algorithm would need to see a genuinely nonlocal obstruction inside that core.

This is exactly the obstruction run48 needed to discover. The missing certificate is not “a better enumeration of small MUFs.” It must explain rare UNSAT **inside the extensive pure-literal core**.

**Outcome of #19:** the proposed local exploration is already optimal enough below the pure-literal threshold and loses its subcriticality at the boundary; no source-metric movement.

## 5. #28 REPLACE FOR ALL WITH FOR TYPICAL — this is literally Theorem 10, and it still stops at the same boundary

The intended quantifier swap was to abandon false structural statements about every deterministic minimally UNSAT 3-CNF and prove one only for a typical rare UNSAT random formula.

Scott--Sorkin's Theorem 10 is precisely that swap. It is conditional on the random formula being UNSAT and then asserts, with probability `1-O(1/n)`, a unique smallest-excess MUF under the corresponding excess exclusion. This is substantially stronger and cleaner than the generic “typical minimal core has controlled exploration” statement I planned.

The theorem's hypothesis contains the decisive limitation:

\[
\sup_n\alpha(n)<\alpha_r^*,
\]

where `alpha_r^*` is the pure-literal threshold in their normalization. That is not a proof artifact removable by relabeling. It is where their full-subformula suppression and finite-excess asymptotics are available. Their abstract explicitly says that what happens between the pure-literal and satisfiability thresholds remains open.

So the correct new target, if F0097 is ever reassigned, is not the run48 `TAIL-c` statement in an arbitrary “rigorously satisfiable regime.” It must explicitly lie **above the pure-literal threshold**, for example:

\[
\Pr(F_3(n,\lfloor c n\rfloor)\text{ UNSAT})
\le (\log n)^{-1-\varepsilon}
\quad
\text{for one fixed }c>c_{\mathrm{PL},3},
\tag{TAIL+}
\]

or a structural substitute strong enough to control the exact atom `Z=0` there.

I am not claiming `(TAIL+)` is sufficient by itself to prove `Omega_3=0`, nor that it is new for every possible `c`; this is the corrected frontier for the dual-witness route after reading Scott--Sorkin.

**Outcome of #28:** a genuinely useful boundary identification, but no metric movement.

## 6. Why this forces the third-stuck handoff

The source-level blocker is unchanged:

\[
\boxed{\limsup_{n\to\infty}\theta_{3,n}=\liminf_{n\to\infty}\theta_{3,n}.}
\]

Runs 42--47 plus this run have now killed or sharply delimited all attempted R03 routes:

1. one-variable cavity pays a constant loss per variable;
2. fractional partition-function martingale controls only bounded local Fourier energy;
3. random native blocks retain an exponential overlap cost;
4. low-collision boosters randomize, collision-rich ones do not;
5. generic helper-to-native replacement is false;
6. essential boosters force mesoscopic correlation without a bounded-local transfer;
7. loose-hypertree formulas give a concrete exponential counterexample to generic mesoscopic-to-local transfer;
8. thermodynamic limits erase the exact `Z=0` boundary;
9. the final dual-witness recovery is already Scott--Sorkin below the pure-literal threshold and becomes nonlocal above it.

No fixed source metric moved during the two allowed recovery cycles. Under the controlling hard-task lifecycle rule, this is therefore the **third stuck episode**, not permission to invent recovery 3.

F0097 remains mathematically **OPEN**. R03's contribution remains **PARTIAL**. The canonical claim file is preserved as historical ownership evidence; this terminal immutable report is the newer own-track lifecycle state. R03 is not authorized to perform another F0097 research recovery unless explicitly reassigned with a genuinely fresh route.

## 7. Handoff package for a future fresh assignee

A future owner should not restart from Friedgut, cavity, or small-MUF enumeration. The most concrete surviving route is:

- work in the density interval **above the pure-literal threshold and below a rigorous satisfiability lower bound**;
- expose the extensive pure-literal core;
- seek a boundary-sensitive statistic on that core that controls exact UNSAT rather than normalized energy;
- prove either a summable UNSAT tail such as `(TAIL+)` at at least one nontrivial density, or a cross-size comparison with summable defect;
- connect that statistic to the finite-size threshold centers rather than merely to one fixed-density SAT probability.

The nearest positive literature template is Scott--Sorkin below the pure-literal threshold: finite excess classification, suppression of large full subformulae, factorial-moment/inclusion-exclusion asymptotics, and algorithmic witness extraction. What is missing above the boundary is exactly the suppression theorem: the pure-literal core is extensive, and the rare UNSAT witness need not be a bounded-excess local defect.

That is a materially sharper handoff than “find a quantitative dual certificate.”

## 8. Rotation / successor admission

I did not create a fake successor claim merely to satisfy the word “rotate.” A fresh neighboring HARD rotation screen from R14 at `runs/R14/2026-09-18T02-59-30Z_h0017_terminal_handoff_rotation_gate_91c4.md` checked the current hard reserve and found no source-current, exact-scope, unowned READY target among the natural candidates. I independently rechecked several likely rows during this run:

- `I0112` is/was R16-owned and already has a hard handoff history;
- `I0043` has an R16 canonical claim/history;
- `I0060` has R12 claim/history and exhausted a hard cycle;
- `I0054` has R11 claim/history;
- `I0078` has a current C27 claim/history;
- `I0115` has a current R12 claim/history;
- `I0061` was worked through both hard recoveries by the former PROB20-21 slot; a missing canonical claim file does not make that exhausted history fresh reserve;
- `I0062` is P11-owned;
- `I0067` has an active claim/history;
- `I0089` has R14 claim/history;
- `I0047` has a broad residual after Jorritsma--Komjáthy 2020 and is explicitly screened `PARTIAL_KNOWN / BROAD_RESIDUAL_NOT_READY` rather than a clean source-frozen successor.

The contemporaneous R14 gate also screened I0073, RS-2026-CL-A, I0087, I0006, I0105, I0106, I0048 and I0049 as owned, later-covered, or not READY in exact scope.

Accordingly R03 rotates off F0097 into

`ROTATION_HOLD — SUCCESSOR_ADMISSION_REQUIRED`.

The next invocation must re-read the fresh queue/claims/current literature and may claim only a newly eligible HARD OUTSIDE target. It must **not** resume F0097 or F0001 merely because the native title is stale.

## 9. Model / scheduler escalation status

The interface limitation is unchanged. The exposed scheduled-task control surface has prompt/title/schedule/timing/enabled controls but no model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry. `GPT-6 / maximum` is therefore a prompt request only; this report truthfully records GPT-5.6 Sol and reasoning `UNVERIFIED`.

The historical P26 `You cannot modify this task` result is authorization-context dependent: repository reconciliation records that P26 later updated successfully from another authorized P/C context, whereas R-series edits were denied in another context. The lawful workaround for any still-denied task is the owning/authorized task-management context or platform support, not permission bypass, duplicate scheduling, or a repository edit masquerading as a runtime setting.

No scheduler, permission, email, Drive, public-posting, purchase, workflow, shared-root, or peer-file state was changed in this run.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R03
  lane: HARD_OUTSIDE
  deployment: NEW-METHODS-2026-09-16
  lifecycle_action: THIRD_STUCK_HANDOFF_AND_ROTATION_GATE
  predecessor:
    target: F0097
    source_target: "uniform random-k-SAT satisfiability threshold for every fixed k>=3"
    first_unresolved_case: k=3
    metric: "Omega_3 = limsup theta_{3,n} - liminf theta_{3,n}"
    before: "Omega_3 <= 0.9698"
    after: "Omega_3 <= 0.9698"
    movement: NO_MOVEMENT
    unchanged_count_before: 6
    unchanged_count_after: 7
    status: OPEN_PARTIAL_HANDOFF
    stuck_episode: 3
    stuck_recovery_cycles_used: "2/2"
    further_R03_recovery_authorized: false
    methods_this_run: [8, 19, 28]
    selected_recovery_result: "PRIOR_ART_COLLISION_BELOW_PURE_LITERAL_THRESHOLD"
    correction: "run48 TAIL-c was not an unproved milestone below c_PL; Scott-Sorkin gives polynomial asymptotics and typical MUF structure there"
    corrected_dual_frontier: "above the pure-literal threshold, inside the extensive core"
  rotation:
    successor_target: NONE_ADMITTED_THIS_RUN
    successor_metric: UNMEASURED
    successor_status: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  theorem_claims_new: 0
  finite_claims_new: 0
  checker: none
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```
