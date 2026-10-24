Model: GPT-5.6 Sol. Reasoning: UNVERIFIED. NO MOVEMENT: `R_unique=+infinity -> +infinity`; methods #6 DEFORM TO A POINT YOU CAN SOLVE, #21 ASK WHO ELSE HAS THIS SHAPE, #27 SWAP THE QUANTIFIERS.

# R06 — I0079 stuck/thinking run: vertex-labelled versus edge-measured IPVT

## Continuity and scope

The scheduler prompt still names I0056 (Lyons–Peres Question 6.20), but R06 already reached the six-unchanged-run rotation threshold on I0056 and preserved that handoff in `runs/R06/20260916T2020Z_i0056_rotation_i0079.md`. I therefore did **not** restart I0056. Its frozen result remains preserved: the selected `H_{5,5}` outer-vertex constant has certified interval `[sqrt(5),sqrt(5)]`, while the full source question remains PARTIAL/audit-gated.

The active canonical R06 claim is I0079, Jardón-Sánchez–Mellick–Poulin–Wróbel, *Exactness and the topology of the space of invariant random equivalence relations*, Question 2. The frozen test class is `Gamma=F_2 x F_2`, standard product Cayley graph `T_4 x T_4` with the l1 graph metric, and iid continuous **nucleus labels** used to refine distance ties. The fixed metric is

`R_unique = max{R>=1 : all subsequential refined IBVT limits agree on every IRE cylinder supported in B_R(e)}`.

The previous three I0079 reports moved this metric from UNMEASURED to `+infinity` and then left it unchanged twice. This run is the third consecutive unchanged value, so under `operations/NEW_METHODS_2026-09-16.md` this is a formal **stuck/thinking run**. I make no new theorem-sized claim below.

## Current source/status check — 2026-09-17

The accessible author PDF of the source still defines a Bernoulli Voronoi tessellation by first choosing a Bernoulli subset of the group and then fixing an equivariant refinement of distance ties. It explicitly says one may, for example, let each boundary point pick among tied nuclei at random, and then says “we fix one” refinement. Its Question 2 is: “In what generality can one say that there is a unique ideal Bernoulli Voronoi tessellation on a group?”

D’Achille–Khezeli, arXiv:2606.30517 (June 2026), is now the closest later primary source. Their graph Theorem 1.3 gives the discrete one-parameter phase family with delay intensity

`beta_v^(xi)(m)=(p-1)p^(m-1+xi), m in Z`,

and Lemma 4.9 identifies Poisson and Bernoulli vertex-nucleus models at the level of subsequential limits under their growth hypothesis. Their edge-measured Theorem 1.4 has continuous delay intensity

`beta_e^(xi)(d delta)=sum_j (p-1)p^(j+xi) 1_[j,j+1)(delta) d delta`.

Their Theorem 4.14 proves phase-independence after restriction to graph vertices/midpoints under a diagonal-boundary hypothesis, and Corollary 1.6 explicitly says that the equal product `T(p) x T(p)` satisfies this independence. Their product proof identifies the vertex boundary law and the edge diagonal boundary law with the same harmonic boundary mixture.

D’Achille–Grebík–Khezeli–Recke–Wilkens, arXiv:2511.23317, Section 4.4 / Theorem 25, treats the exact Bernoulli product-tree partition with iid `Unif[0,1]` nucleus labels: ties at a graph vertex are won by the tied nucleus with minimum label, and any subsequential Bernoulli partition limit equals the ideal labelled Poisson boundary partition corresponding to the subsequential boundary intensity.

Dated queries checked this run included the exact source title + Question 2, arXiv:2606.30517 with Theorem 4.14/Corollary 1.6/Lemma 4.9, and arXiv:2511.23317 Theorem 25. Direct arXiv PDF extraction was not available for every paper; the source author PDF was accessible, and searchable full text for the 2026 D’Achille–Khezeli preprint and the product-tree preprint was available through indexed full-text mirrors. I did not find a later primary paper explicitly stating the source’s **vertex-Bernoulli + iid nucleus-label** `T(p)xT(p)` uniqueness as a named corollary. That absence is not evidence of novelty by itself.

## Stuck report

### (a) Exact blocking statement

The novelty/status obstruction is no longer the phase-cancellation algebra. It is the precise model-identification step

\[
\boxed{
\mathcal L\!\left(P^{\mathrm{vertex,label}}_{\xi}\right)
\stackrel{?}{=}
\mathcal L\!\left(P^{\mathrm{edge}}_{\xi-1}\big|_{G}\right),
\qquad G=T(p)\times T(p),
}
\]

where the left side is the source-admissible ideal **vertex-nucleus** partition with iid nucleus labels used only to resolve integer-distance ties, while the right side is D’Achille–Khezeli’s **edge-measured** IPVT restricted to graph vertices. The `xi-1` is the harmless index shift suggested by the published delay intensities.

If this equality in law is accepted with the exact topology/refinement convention, Corollary 1.6 of arXiv:2606.30517 makes the frozen R06 `T_4 x T_4` result a direct **KNOWN** corollary rather than a new theorem. If it fails, the reason for failure is precisely the piece that could remain new.

### (b) Routes tried and the precise reason each is not yet a source-level closure

1. **Direct discrete phase unfolding (earlier R06).** For an integer delay `m` and iid label `u`, the map `t = c p^m(1+(p-1)u)/(p-1)` removes the phase from the marked point process and proves the refined partition law is phase-independent. Mathematically this works, but after the 2026 literature check it is too close to the published edge-measured phase-smoothing mechanism to support a novelty claim without the model comparison above.

2. **Global marked coupling / general graph criterion (earlier R06).** The same unfolding was written as a global phase-free PPP coupling. This strengthens presentation but does not resolve whether the statement is already an immediate corollary of the edge-measured theorem.

3. **Method #6 — deform vertex labels into an edge fractional coordinate.** The two published intensity formulas line up almost exactly: replacing the iid label `u` by the fractional delay in `m+u` turns the vertex intensity on `[m,m+1)` into `(p-1)p^(m-1+xi) d delta`, which is the edge intensity with phase/index shifted by one. Since `h(v)+m` is integer-valued, numeric order of `h(v)+m+u` is exactly lexicographic order of `(h(v)+m,u)`. This strongly suggests the equality in (a), but the exact source-level statement also has to identify the boundary law and convergence/tie-refinement topology, not just the delay marginal.

4. **Method #21 — ask who else has this shape.** D’Achille–Khezeli Corollary 1.6 is essentially the same phase-independence geometry for the edge-measured equal product of regular trees, while DGKRW Theorem 25 is exactly the iid-label Bernoulli partition limit. The two papers together sit immediately adjacent to the frozen R06 statement. I therefore no longer regard “no prior statement found” as meaningful novelty evidence.

5. **Method #27 — swap the quantifiers.** The source does not canonically prescribe iid nucleus labels; it says to fix an equivariant refinement and even gives pointwise random tie resolution as an example. R06 proved only **there exists a natural fixed refinement** (iid nucleus labels) for which the frozen product class is unique. It did not prove uniqueness for **every** source-admissible refinement. Therefore even a perfect identification in (a) cannot close the full Question 2.

### (c) What a proof/status resolution must contain that the tried routes do not yet contain

A definitive prior-art reduction must put all of the following on one page:

- identify the vertex-limit boundary law `nu_0` for `T(p)xT(p)` with the boundary law used by the edge-measured Corollary 1.6;
- convert each integer delay plus iid nucleus label `(m,U)` into the edge fractional delay and verify equality of the resulting marked PPP law, including the one-unit phase/index shift;
- verify that on graph vertices the two winner rules agree **jointly for all vertices**, hence induce the same IRE, not merely the same one-point winner distribution;
- connect the Bernoulli partitions to that ideal process using the actual partition topology in DGKRW Theorem 25 / D’Achille–Khezeli Lemma 4.9;
- keep the refinement scope explicit: iid per-nucleus labels are one fixed equivariant refinement, not all possible refinements allowed by the source.

Until that bridge is independently checked, the honest frozen label is **PROVED / AUDIT-GATED / VERY CLOSE PRIOR ART; KNOWNNESS RESOLUTION PENDING**, not “new”.

### (d) Simplest source-valid special case still unproved here

Keep the same graph `T_4 x T_4`, but replace global iid nucleus labels by the source’s other natural example: an equivariant **pointwise random resolution of each distance tie**. The phase-unfolding proof relies on a single scalar mark attached to each nucleus, so it does not automatically apply to fresh tie randomness attached to boundary vertices. This is the smallest change that stays inside the exact source definition while testing whether uniqueness is a property of the group/metric or of the chosen refinement.

### (e) Nearest solved problem and the ingredient it has that the present source scope lacks

Nearest solved result: D’Achille–Khezeli Theorem 4.14 + Corollary 1.6 for the edge-measured equal product `T(p)xT(p)`, combined with DGKRW Theorem 25 for labelled Bernoulli product-tree diagrams. The edge-measured model has a built-in continuous fractional delay along every edge. That continuous coordinate globally orders competitors and smooths the discrete phase. An arbitrary equivariant boundary-refinement rule in the source need not arise from one globally consistent per-nucleus scalar coordinate, which is exactly why the published edge theorem does not automatically settle the full source question.

## Exactly one recovery choice

**Chosen recovery: port the technique from the nearest solved problem.** On the next I0079 research run, do not search for another phase-cancellation lemma. First write and audit the exact finite-cylinder equivalence between the iid nucleus-label vertex model and the edge-measured model on `T_4 x T_4`. If that bridge passes, reclassify the frozen iid-label subclass as KNOWN and move immediately to the simplest different source-admissible refinement (or rotate if ownership/current-status rules require it). If the bridge fails, the first failing equality becomes the new mathematical obstruction.

Next methods (not used in this run): **#12 FIND WHAT IS CONSERVED**, **#25 COUNT THE SAME THING TWICE**, **#30 DO ONE SCALE / ONE DIRECTION AT A TIME**.

## Audit gate and R07 independent audit

For frozen I0079, the existing independent audit remains

`R05-AUDIT-R06-I0079-PHASE-CANCELLATION-01-20260916T221717Z: PASS_CORE_MATH / SOURCE-HANDOFF_SCOPED / NOVELTY_UNVERIFIED`.

A fresh repository search found no `P26-AUDIT-R06-I0079` record. Closure therefore remains blocked regardless of the mathematical argument.

Newest R07 package audited: `runs/R07/20260916T2322Z_i0077_aperiodic_asymmetric_pulses_07.md`, theorem `I0077-R07-T8` (aperiodic asymmetric parabolic-scale pulse obstruction). I checked the static killed-OU Rayleigh/Poincare bound, the conversion from a uniform log-gap bound to a linear count of complete pulses, the product/Markov contraction across pulses, the summable continuum-terminal-time reduction using Brownian modulus control, time-reversal symmetry of the asymmetric tube after reflecting the walls, and the final FBM witness-time contradiction. At the stated scope I found no gap. In particular, the final random witness time does not need to be a stopping time for a fixed forward Brownian piece: for each fixed `j`, the event at random `T_j` is contained in the event that **some** terminal time beyond `N` satisfies the tube constraint, and that latter event has probability tending to zero uniformly as `N->infinity`.

Verdict:

`R06-AUDIT-R07-I0077-T8-20260917T0017Z: PASS_SCOPED / NOVELTY_UNVERIFIED`.

This audits T8 mathematically only; it is not a prior-art audit and does not close all of Burdzy–Scheutzow Problem 7.8.

## Model / task-control escalation

The limitation is still real. Direct inspection of the exposed task-control surface this run shows fields for title/prompt, schedule, timing mode and enabled state, but **no model-family selector and no reasoning-effort selector**. The repository policy file `operations/NEW_METHODS_2026-09-16.md` records the same limitation. Therefore `GPT-6 / maximum` remains a prompt request, not a verified runtime setting. Making it enforceable requires the product/backend to expose those fields (and ideally authenticated runtime telemetry), or an authorized owner/admin/platform-support context to migrate the task.

The same policy records prior native modification denials including `You cannot modify this task`. That is an ownership/context permission boundary. The permitted workaround is the owning authorized task-control context or platform support; do not duplicate the task or bypass the permission boundary. No scheduler mutation was attempted.

## Structured ledger_delta

```yaml
ledger_delta:
  source:
    intake: I0079
    authors: "Jardon-Sanchez, Mellick, Poulin, Wrobel"
    work: "Exactness and the topology of the space of invariant random equivalence relations"
    problem: "Question 2: uniqueness of ideal Bernoulli Voronoi tessellations"
  target: "Frozen iid-nucleus-label refined IBVT on F_2 x F_2 = T_4 x T_4; full Question 2 retained"
  metric:
    name: R_unique
    before: "+infinity"
    after: "+infinity"
  movement: "NO MOVEMENT"
  unchanged_count: 3
  status:
    frozen_subclass: "PROVED / AUDIT-GATED / VERY CLOSE PRIOR ART; KNOWNNESS RESOLUTION PENDING"
    full_source: PARTIAL
    novelty: UNVERIFIED
  tried_moves: [6, 21, 27]
  stuck_trigger: true
  recovery_choice: "port the technique from the nearest solved problem"
  remaining_obligation: "Audit exact equality in law between iid-label vertex model and edge-measured restriction; then reclassify frozen scope or isolate first obstruction. Full source additionally requires other refinements/groups."
  next_moves: [12, 25, 30]
  exact_evidence:
    - "artifacts/R06/20260916T2121Z_i0079_phase_unfolding_exact.py"
    - "artifacts/R06/20260916T2121Z_i0079_phase_unfolding_exact.txt"
    - "D'Achille-Khezeli arXiv:2606.30517 Theorem 1.3, Lemma 4.9, Theorem 4.14, Corollary 1.6"
    - "D'Achille-Grebik-Khezeli-Recke-Wilkens arXiv:2511.23317 Theorem 25"
  audit_ids:
    - "R05-AUDIT-R06-I0079-PHASE-CANCELLATION-01-20260916T221717Z: PASS_CORE_MATH / SOURCE-HANDOFF_SCOPED / NOVELTY_UNVERIFIED"
    - "P26-AUDIT-R06-I0079: NOT_FOUND"
    - "R06-AUDIT-R07-I0077-T8-20260917T0017Z: PASS_SCOPED / NOVELTY_UNVERIFIED"
```
