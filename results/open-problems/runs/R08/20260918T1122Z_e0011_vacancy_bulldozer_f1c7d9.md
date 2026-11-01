Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `B_cat: 0 -> 0` (unchanged count 2). Methods used: B15, B19, B24.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: a worst-boundary vacancy bulldozer

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, and what I did not reopen

I continued from the newest R08 state actually present on `master`, namely

`runs/R08/20260918T0526Z_e0011_block_certificate_b71626.md`.

The active source is still **E0011**, Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5, under the exclusive claim `operations/claims/E0011.md`. The target is the original two-dimensional catalyst/ZGB process with no stirring, instantaneous reaction `r=infinity`, and source normalization `q/2=1-p`. The source asks for a nondegenerate interval of `p` on which both species coexist.

I did **not** reopen Hasebe--Ueda Problem 3.11 (`I0082`). Its old candidate metric remains frozen at `2/3` after six unchanged runs and the R08 handoff remains controlling despite the stale historical `ADMITTED_ACTIVE` label still present in `operations/claims/I0082.md`. I also did not reopen the retired F0083 route or the old FPP strict-convexity route.

Before research I refreshed the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the current NEW-METHODS owner directive, the E0011 and I0082 claim files, the newest own report, current E0011 ownership/admission screens, and neighboring Durrett/E0010 material. Current ownership screens still identify E0011 as R08-owned and do not show a competing owner.

## 2. Dated source/current-literature check

I refreshed the original Durrett source and bounded current literature on 2026-09-18 before doing the finite search.

The source model is the ZGB/catalyst process with states `0=vacant`, `1=CO`, `2=O`, transitions `0 -> 1` at rate `p`, neighboring `00 -> 22` at rate `q/4`, and unlike neighboring particles reacting at rate `r/4`; the physical no-stirring problem takes `r=infinity` and `q/2=1-p`. Durrett states Problem 5 as finding `0<p_1<p_2<1` with coexistence for every `p in (p_1,p_2)`. The source explicitly separates the original model from the large-polymer and fast-stirring results.

Fresh bounded searches for the exact catalyst / ZGB / CO-oxidation model, `Durrett Problem 5`, no-stirring coexistence, and later Durrett--Swindle work again recovered the perturbative fast-stirring / modified-model literature but no later primary source matching theorem settling the original zero-stirring Problem 5. Durrett's currently served notes still treat the catalytic surface model through the fast-stirring route and retain the numerical ZGB phase-window discussion. This is **bounded negative evidence only**, not a worldwide-open or priority certificate.

The source's `r=infinity` convention also matters for today's finite lemma: after a newly attached object has opposite-type neighbors, it reacts immediately; if there are several possible reaction partners, one is chosen at random. I therefore condition the finite word below on one fixed legal sequence of tie choices rather than silently replacing the source by a deterministic reaction model.

## 3. Frozen metric remains unchanged

The metric from the E0011 claim is

\[
B_{\rm cat}=\sup_C b(C),
\]

where `C` must be a complete source-valid finite block certificate: one incoming two-species seed, a finite protected Harris block, a deterministic implication reproducing the seed into **both** forward oriented children, translated blocks arranged to be 1-dependent, and `b(C)` an exact certified lower bound on the good-block probability at the frozen anchor `p_0=1/2`.

The preceding run proved that a concrete certificate with

\[
b(C)>63/64
\]

would be enough, and that a strict one-point certificate at `p=1/2` opens to a genuine interval of `p` by an explicit Lipschitz coupling bound.

Today's result is a robust **control primitive**, not yet a two-child seed-reproduction block. Therefore the honest metric remains

\[
\boxed{B_{\rm cat}:0\longrightarrow 0.}
\]

This is the second unchanged E0011 run. I do not count a positive-probability local word as metric movement when it does not yet satisfy the frozen two-child block obligation.

## 4. B15 — BREAK THE SYMMETRY: use a vacancy cursor, not a density block

The no-stirring dynamics is hostile to a symmetric density-block approach. At `r=infinity`, a CO/O contact is annihilated immediately, while O2 adsorption itself requires a neighboring vacant pair. Thus the local resource that can actually be transported and manipulated is **vacancy geometry**.

The asymmetric seed language I tested is therefore an interface with a vacancy cursor: a small vacant rectangle separates / mediates the two chemical types, rather than asking a square block to carry prescribed positive densities of both types at every intermediate time.

The smallest cursor that exposes both O2 and CO reaction mechanisms cleanly is a `2 x 2` vacant square. The question for this run was deliberately stronger than a friendly-boundary calculation:

> Can a fixed finite Harris word shift a `2 x 2` vacant cursor one lattice step through an *arbitrary stable exterior configuration*?

If the answer had been no even locally, the interface route would have been a poor candidate for a rigorous block construction. It is yes.

## 5. B19 — MAKE IT AN ALGORITHM: finite synchronizing-word formulation

Condition on the reaction tie breaker always choosing the first available opposite-type neighbor in the fixed priority

\[
E,W,N,S.
\]

Every such choice is a legal outcome of the source's random tie rule; the event that all finitely many relevant ties realize these choices has positive probability.

Consider the active `2 x 3` rectangle

\[
\{-1,0,1\}\times\{0,1\}
\]

and include every nearest-neighbor site of that rectangle. This gives a 16-site local patch. Initially require only

\[
\{-1,0\}\times\{0,1\}
\]

to be vacant. The remaining 12 local sites may be `0,1,2` arbitrarily, subject only to the source's instantaneous-reaction stability condition: no nearest-neighbor `1/2` pair is present.

I then searched for a **nonadaptive synchronizing word**: the same adsorption-attempt sequence must work for every such stable environment. The following length-12 word works:

1. `CO(1,0)`
2. `CO(0,0)`
3. `CO(1,0)`
4. `CO(0,0)`
5. `CO(1,0)`
6. `CO(0,1)`
7. `CO(0,1)`
8. `CO(0,0)`
9. `O2[(-1,0),(-1,1)]`
10. `O2[(0,0),(0,1)]`
11. `CO(-1,0)`
12. `CO(-1,1)`.

Here a CO mark is harmless if its site is occupied; an O2 mark is harmless unless both edge endpoints are vacant. Whenever an accepted newly adsorbed particle has an opposite-type neighbor, instantaneous reaction is resolved by the conditioned priority above.

### Finite lemma — vacancy bulldozer

For **every** stable local state of the 16-site patch whose left/middle `2 x 2` square

\[
\{-1,0\}\times\{0,1\}
\]

is vacant, the 12-mark word leaves the translated middle/right square

\[
\{0,1\}\times\{0,1\}
\]

vacant.

Equivalently, a `2 x 2` vacancy cursor can be shifted one step to the right through any stable one-neighborhood, with no favorable boundary assumption.

This is a finite universal statement, so I checked it exactly rather than calling a simulation a proof. There are 12 free sites and therefore exactly

\[
3^{12}=531441
\]

raw assignments. Exactly **50,785** satisfy the local `r=infinity` stability constraint. The checker applies the exact deterministic transition map induced by the conditioned tie choices to all 50,785 stable states, verifies that every final state remains stable, and verifies that all four target sites are vacant in every case.

Archived checker:

`artifacts/R08/20260918T1122Z_e0011_vacancy_bulldozer_check.py`

creation commit:

`bf4b7a8e087a2dfec42259387d161aa00d5360ef`.

Archived output:

`artifacts/R08/20260918T1122Z_e0011_vacancy_bulldozer_check.out`

creation commit:

`4d273a634caf79971e9d6eac7c1537c07f868908`.

The executed output is

```
PASS exact exhaustive vacancy-bulldozer check
local_cells=16 variable_cells=12
assignments=531441 stable_assignments=50785
word_length=12
initial_vacancy_window=[-1,0]x[0,1]
final_vacancy_window=[0,1]x[0,1]
all_50785_stable_environments_pass=True
```

### Why the finite patch really covers arbitrary exterior states

Every globally stable source configuration with the indicated `2 x 2` vacancy window restricts to one of the 50,785 locally stable states. Every adsorption in the word occurs inside the active `2 x 3` rectangle, and every site that can be consulted as an immediate reaction partner lies in its one-neighborhood, which is exactly the 16-site patch enumerated by the checker.

Boundary sites of the patch are never newly occupied by the word; they can only be left unchanged or removed by an instantaneous reaction with an active-site deposition. Hence an unseen site beyond the enumerated one-neighborhood cannot become a new reaction partner for one of the prescribed marks. The local transition computation is therefore closed under arbitrary globally stable exterior completions.

For an O2 mark, the two new oxygens have no common CO neighbor on the square lattice, so the fixed endpoint-processing order in the checker does not create a hidden conflict between the two instantaneous reactions.

This is a **self-check**, not an independent audit.

## 6. B24 — FIND THE EXTREMAL OBJECT: the worst local boundary disappears for translation

The previous run left a serious block-design question: a certificate cannot assume a friendly exterior, so perhaps the worst boundary state destroys every small interface seed.

For the translation primitive above, that concern is now eliminated completely. There is no special extremal boundary configuration to optimize against: the same word succeeds on **all 50,785** stable local boundary environments compatible with the incoming vacancy cursor.

This is stronger than proving a favorable-boundary path and then trying to add a monotonicity argument. The catalyst model has no convenient monotone order simultaneously controlling CO and O, so a boundary-uniform synchronizing word is the right replacement for attractiveness at this local scale.

It also changes the algorithmic search problem. Instead of estimating a success probability separately for thousands of boundary conditions, one can search the finite transition semigroup for words that synchronize an entire class of stable states to a desired vacancy pattern. The checker then validates the resulting word exhaustively.

## 7. What this buys, and the precise remaining obstruction

The local word is a genuine new route ingredient:

- a vacancy corridor can be **moved through arbitrary stable material** rather than requiring pre-cleared fresh fringe;
- the move is constructive and finite;
- it is compatible with exact certification;
- it uses only source transitions at zero stirring and `N=1`, so it does not smuggle in either of the known perturbative models.

But it does **not** yet duplicate the cursor. The frozen block metric requires one incoming seed to reproduce into two forward children. A word that merely translates one `2 x 2` vacancy square can carry a control resource to one place but does not yet branch it into two independent descendants.

That is the exact obstruction now:

\[
\boxed{\text{construct a boundary-uniform synchronizing word that BRANCHES one finite vacancy/interface seed into two.}}
\]

I attempted to turn translation into expansion during the exploratory search, but no exact branching/expansion word was certified this run. I therefore record no such claim and no numerical near-miss.

A fixed finite word has strictly positive Harris probability at `p=1/2`: prescribe its finitely many required clock marks in disjoint small time windows, exclude interfering protected-region marks in those windows, and prescribe the finitely many tie choices. I deliberately do **not** turn that observation into `B_cat>0`, because the metric is tied to the complete two-child block certificate, not to an isolated local maneuver.

## 8. Why this is research movement despite metric stagnation

The frozen number did not move, but the route did. The previous state said in effect: “choose an interface-oriented seed and identify the worst boundary.” The present state contains an exact answer to that local worst-boundary problem:

\[
\text{one }2\times2\text{ vacancy cursor}
\xrightarrow[\text{same 12 marks}]{\text{every stable local environment}}
\text{translated }2\times2\text{ vacancy cursor}.
\]

That is the kind of finite primitive from which a source-valid renormalization can plausibly be assembled. It is materially different from producing another probability checker for an unchanged candidate block.

No closure claim is made. Current source status remains **OPEN / track PARTIAL** under bounded current-literature checking.

## 9. Next distinct methods if E0011 continues

Do not repeat B15/B19/B24 immediately. The next research triple is:

- **B3 PROVE SOMETHING STRONGER:** search for a boundary-uniform *branching* synchronizing word, not merely another translated cursor. A successful primitive should map one finite vacancy/interface seed to two separated copies before any probability optimization.
- **B20 FIND WHY THE ALGORITHM FAILS:** if no brancher appears, characterize an invariant of the finite transition semigroup that prevents vacancy duplication. An impossibility theorem for the current seed class would justify changing the seed rather than enlarging the same search forever.
- **B25 COUNT THE SAME THING TWICE:** represent the synchronizing-word problem both as a set-valued automaton on stable local states and as a backwards preimage calculation from the desired two-child target. Agreement of the forward and backward reachable sets gives an exact finite obstruction/certificate and may expose a smaller state quotient.

If the metric is still unchanged after the next run, E0011 will have three consecutive unchanged runs and the following run must obey the Section-I stuck protocol rather than adding another routine local lemma.

## 10. Structured ledger delta (own report only)

```yaml
ledger_delta:
  worker: R08
  predecessor: I0082
  predecessor_state: RETIRED_FROZEN
  predecessor_metric: 2/3
  predecessor_retirement_count: 6
  target: E0011
  source: Durrett_2009_Problem_5
  allocation: CLOSABLE_OUTSIDE
  owner: R08
  metric: B_cat
  before: 0
  after: 0
  movement: none
  unchanged_count: 2
  source_status: OPEN_CURRENT_BOUNDED
  track_status: PARTIAL
  methods: [15, 19, 24]
  research_delta:
    - exact_length_12_boundary_uniform_vacancy_cursor_translation
    - stable_local_environments_checked_50785_of_531441_raw_assignments
    - worst_local_boundary_eliminated_for_translation_primitive
  finite_core:
    checker: artifacts/R08/20260918T1122Z_e0011_vacancy_bulldozer_check.py
    output: artifacts/R08/20260918T1122Z_e0011_vacancy_bulldozer_check.out
    checker_commit: bf4b7a8e087a2dfec42259387d161aa00d5360ef
    output_commit: 4d273a634caf79971e9d6eac7c1537c07f868908
  remaining_obligation: boundary_uniform_two_child_seed_branching_plus_high_probability_block_certificate
  next_methods: [3, 20, 25]
```

## 11. Model / reasoning / scheduler-control status

The actual model available to this run is GPT-5.6 Sol; authenticated reasoning-effort telemetry is not exposed, so the reasoning level is reported as `UNVERIFIED`. I do not claim GPT-6 maximum.

The exposed task-management schema still has prompt/title/schedule/timing/enabled controls but no binding model-family or reasoning-effort field and no authenticated completed-run model telemetry. Consequently, guaranteeing GPT-6 at maximum would require a native model/effort selector (and run telemetry) in the authorized scheduler/product surface; prompt text alone cannot enforce it.

There is one useful repository update to the older permission story: current `RESULTS.md` records that P26's full prompt update **did succeed in an authorized P/C context**, while historical permission failures were context-specific; it also records that the R-series edits were denied in another reconciliation context. Thus “You cannot modify this task” should be treated as an authorization-context boundary, not proof that the task is globally immutable. The lawful workaround remains to use the task's authorized owning context, a supported ownership/admin transfer, or platform support. No scheduler change was attempted in this run.
