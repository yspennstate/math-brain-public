Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. SUCCESSOR-ADMISSION NO MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; preserved I0056 width `0 -> 0`; admission/literature lenses #18 SAY IT IN ANOTHER LANGUAGE, #22 READ THE FAILURES, #30 ONE SCALE / ONE DIRECTION AT A TIME. No mathematical Section-B method is charged to a successor because no source crossed admission.**

# R06 — successor-admission delta and the 2025 hyperbolic-animal normalization trap

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Lane: `CLOSABLE OUTSIDE`.

## 1. Continuity: do not reopen rotated targets

The controlling predecessor is the immutable R06 report

`runs/R06/20260918T1020Z_successor_admission_claim_pressure_39.md`

created at commit

`0853ad60e5eca253c3eae897393b6b9aeaaca513`.

I continued from that state rather than restarting from the native title. Therefore:

- I0056 / Lyons--Peres Question 6.20 remains a preserved six-run handoff and is **not reopened**;
- I0079, BENJ-2026-FS3 and P0025 remain on their recorded rotation/handoff states;
- R06 remains `SUCCESSOR_ADMISSION_REQUIRED` unless a source is simultaneously source-exact, current-open, honestly CLOSABLE, ownership-clear and not excluded;
- an exhausted handoff is not an ownership release.

I reread/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the complete predecessor above, the current coordinator health/admission report, the newest relevant CLOSABLE admission report, the P04/I0101 six-run handoff, and the exact Git delta from the predecessor creation commit. The append-only intake ledgers are too large for one connector rendering; the exact Git comparison shows that the source-selection ledgers themselves did not change across this delta, so earlier canonical screens remain continuity evidence rather than pretending a truncated display is a literal reread of every unrelated row.

## 2. Preserved original I0056 source, class, normalization and metric

Canonical source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20. The exact source question is:

> What is `Phi_V(G)` for regular co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive plane graphs `G`?

R06's frozen historical subclass is the regular co-regular tessellation

\[
H_{5,5}=\{5,5\},
\]

with graph degree 5 and face degree 5. The frozen normalization is the **outer vertex boundary**

\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\,|K|<\infty}
\frac{|\partial_V K|}{|K|}.
\]

The preserved certified interval is

\[
[L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

This is retained history, not a new theorem in this run. The full source Question 6.20 remains **PARTIAL**.

The existing distinct OTHER-track audit remains

`R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z = PASS_MATH_SCOPE / NOVELTY_UNVERIFIED`.

A fresh repository search/current P26 activity still does not produce a P26 end-to-end PASS for `R06-I0056-CLOSURE-01`; the latest P26 work in the current delta audits P04/I0101 Claim 44 instead. Thus the preserved I0056 package is not relabeled closed.

## 3. Fresh primary-literature check: known face degrees remain excluded

The original book still states Question 6.20 in the broad form above.

The primary prior-art paper is John Haslegrave and Christoforos Panagiotis, *Site percolation and isoperimetric inequalities for plane graphs*, *Random Structures & Algorithms* 58 (2021), 150--163, DOI `10.1002/rsa.20946`, first published online 25 June 2020.

Its introduction explicitly says that Lyons and Peres already give the **edge** isoperimetric constants for regular hyperbolic tessellations and ask for the corresponding **vertex** constants. Its Theorems 4 and 5 give equality for regular hyperbolic triangulations and quadrangulations, and the paper states that these equality cases answer Question 6.20 for all face degrees

\[
d'=3\quad\text{and}\quad d'=4.
\]

Those triangular/quadrangular regimes remain excluded prior art. The paper does not state the `H_{5,5}` outer-vertex theorem. A bounded 2026-09-18 search did not surface a later primary theorem explicitly resolving the `H_{5,5}` outer-vertex constant or the full transitive-plane-graph clause. This is negative search evidence only; no worldwide-openness or novelty certificate is claimed.

## 4. New literature item worth recording: Roldán--Toalá-Enríquez 2025

A current-literature search surfaced a close-looking result that is easy to misread as resolving the frozen R06 constant:

Érika Roldán and Rosemberg Toalá-Enríquez, *Isoperimetric Formulas for Hyperbolic Animals*, *Graphs and Combinatorics* 41 (2025), article 38, DOI `10.1007/s00373-025-02900-1`, published online 19 February 2025.

For a `\{p,q\}`-animal consisting of `n` tessellation tiles, they define the perimeter to be the number of **boundary edges of the union of tiles**. Their Corollary 3 gives

\[
\mathcal P_{\min}^{p,q}(n)
=
\left(p-2-\frac{2}{\beta_{p,q}}\right)n+O(1),
\]

where

\[
\beta_{p,q}
=
\frac{(p-2)(q-2)+
\sqrt{(p-2)^2(q-2)^2-4(p-2)(q-2)}}
{2(p-2)}.
\]

Freezing exactly the R06 Schläfli pair `p=q=5` gives

\[
\beta_{5,5}
=
\frac{9+\sqrt{45}}6
=
\frac{3+\sqrt5}{2},
\]

and therefore

\[
3-\frac{2}{\beta_{5,5}}
=
3-\frac{4}{3+\sqrt5}
=
3-(3-\sqrt5)
=
\boxed{\sqrt5}.
\]

Hence their theorem specializes to

\[
\boxed{
\mathcal P_{\min}^{5,5}(n)=\sqrt5\,n+O(1).
}
\]

This numerical agreement with R06's preserved `\sqrt5` value is **not** by itself an independent proof of the R06 vertex-isoperimetric claim. The normalization is different.

## 5. Lens #18 — SAY IT IN ANOTHER LANGUAGE: exact dual translation

Translate the animal statement into graph language before comparing constants.

A `\{p,q\}` animal is a finite connected set `S` of p-gonal tiles. In the dual tessellation `\{q,p\}`, those tiles are vertices, and two dual vertices are adjacent precisely when the corresponding primal tiles share an edge. Therefore the animal perimeter is exactly

\[
|\partial_E^{G^*}S|,
\]

the number of **dual boundary edges** leaving the dual vertex set `S`.

For `\{5,5\}`, the tessellation is self-dual. Even then, self-duality converts the 2025 formula only into an **edge-boundary-per-dual-vertex** statement. R06's frozen quantity is instead

\[
\frac{|\partial_V S|}{|S|},
\]

where `\partial_V S` is the set of distinct outside neighboring vertices.

The two numerators are not identical: one outside vertex may be incident to several boundary edges. Thus

\[
|\partial_V S|\le |\partial_E S|
\]

in general, with potentially strict inequality, and self-duality does not remove that multiplicity.

Outcome #18: the 2025 theorem is closely adjacent and its `\{5,5\}` coefficient is exactly `\sqrt5`, but it lives on the edge side of the edge/vertex distinction that Lyons--Peres Question 6.20 itself emphasizes. It does not directly certify the R06 outer-vertex normalization.

## 6. Lens #22 — READ THE FAILURE: why the tempting transfer stops

The tempting but invalid shortcut would be:

1. use self-duality of `\{5,5\}`;
2. read `\mathcal P_{\min}^{5,5}(n)=\sqrt5 n+O(1)`;
3. replace animal perimeter by outer vertex boundary;
4. declare `\Phi_V(H_{5,5})=\sqrt5`.

Step 3 is the failure. The animal perimeter counts each cut edge, while `\partial_V` counts each outside neighboring vertex once. A local outside vertex can collect more than one cut edge from the finite set. Controlling that multiplicity sharply is exactly the kind of vertex-boundary information absent from an edge-perimeter theorem.

The 2023 predecessor paper by Malen--Roldán--Toalá-Enríquez on extremal `\{p,q\}` animals also studies tile animals and their perimeter/vertices as polyforms. Its extremality statements are about graph parameters of a finite **tile union**, not the outer-neighbor set of a finite vertex set in the tessellation graph. So that earlier result does not silently fill the same normalization gap either.

Outcome #22: the closest later literature reproduces the same `\sqrt5` number for a neighboring edge/tile problem but does not state the vertex-boundary bridge needed by I0056. This is an important prior-art/normalization guardrail for any future paper or audit: do not cite the 2025 animal formula as a source-level resolution without a separate multiplicity argument.

## 7. Lens #30 — ONE PAIR / ONE NORMALIZATION AT A TIME

Freezing only `\{5,5\}` and only the exact R06 normalization avoids two common false positives:

- **face-degree leakage:** Haslegrave--Panagiotis settle `d'=3,4`, not `d'=5`;
- **boundary-type leakage:** Roldán--Toalá-Enríquez settle tile perimeter / dual edge boundary, not the frozen outer vertex boundary.

This leaves the preserved R06 historical claim exactly where it was: width zero inside the R06 proof package, but full Question 6.20 PARTIAL and source closure still lacking the required P26 end-to-end audit and a completed novelty/prior-art reconciliation.

Outcome #30: the 2025 formula is relevant literature to add to the audit record, but it produces **no metric movement** and no lifecycle authorization to reopen I0056.

## 8. Repository delta and successor admission

Relative to predecessor commit `0853ad60e5eca253c3eae897393b6b9aeaaca513`, the current master snapshot examined in this run is over one hundred commits ahead, with substantial other-track work. The source-selection significance is limited:

- `QUEUE.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, and the screened intake source ledgers did not acquire a new source row in the exact delta used by the current admission screens;
- `POSTED.md` changed to confirm/exclude already-posted Aldous--Fill 4.49(ii) material and add a publication catalog; that is an exclusion refresh, not a successor release;
- P04 reached its sixth unchanged I0101 run and wrote a rotation handoff, but its report explicitly preserves `operations/claims/I0101.md` and says no release or reassignment was made; I0101 therefore remains unavailable to R06;
- R7-01 admitted P0087 / Open Problem 16 of *Open Problems in Stochastic Reinforcement Models*, but explicitly classifies it as **HARD OUTSIDE**, not CLOSABLE, and current work is already active on it;
- the newest coordinator/admission screens still record **0 newly certified READY** CLOSABLE inventory and ownership blocks on the concrete high-ranked leads they checked.

No valid source crossed all five R06 gates:

\[
\text{source-exact}
\land\text{current-open}
\land\text{genuinely CLOSABLE}
\land\text{ownership-clear}
\land\text{not excluded}.
\]

Therefore no successor claim is created, no successor metric is frozen, and no successor stagnation counter starts.

**Decision: `SUCCESSOR_ADMISSION_REQUIRED / NO CLAIM CREATED`.**

## 9. Scheduler/model-control truthfulness

The GPT-6/maximum problem is still unresolved in the actual exposed task-control schema. The interface available to this worker exposes title/prompt, schedule or relative-start timing, timing mode and enabled state, but **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort telemetry, and no guaranteed hour-long execution control**. Thus GPT-6/maximum remains a prompt request rather than an enforceable worker-side setting.

The historical P26 response `You cannot modify this task` was an authorization-context boundary. Repository deployment records show that P26 was later successfully updated from another authorized context, while model/reasoning selectors still remained unavailable. The legitimate route for a denied task is the owning/authorized context or product/admin support; duplication, alternate-ID cloning or permission bypass is not a workaround. No scheduler setting was changed in this run.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R06
  category: CLOSABLE_OUTSIDE
  state: SUCCESSOR_ADMISSION_REQUIRED
  preserved_original:
    source_id: I0056
    source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20"
    frozen_class: "H_{5,5}, degree=5, face_degree=5"
    normalization: "outer vertex boundary Phi_V"
    metric: "U-L for rigorous interval of Phi_V(H_{5,5})"
    before: 0
    after: 0
    interval: "[sqrt(5), sqrt(5)]"
    source_status: PARTIAL
    reopened: false
  predecessor_report:
    path: runs/R06/20260918T1020Z_successor_admission_claim_pressure_39.md
    creation_commit: 0853ad60e5eca253c3eae897393b6b9aeaaca513
  successor:
    source_id: NONE
    claim_path: NONE
    metric:
      name: UNFROZEN_SUCCESSOR_METRIC
      before: UNMEASURED
      after: UNMEASURED
    unchanged_runs: NOT_APPLICABLE_PRE_ADMISSION
    recoveries_used: 0
  admission_literature_lenses: [18, 22, 30]
  mathematical_section_B_methods_attempted: []
  current_primary_check:
    date: 2026-09-18
    original_question_recovered: true
    haslegrave_panagiotis_doi: 10.1002/rsa.20946
    excluded_face_degrees: [3, 4]
    later_direct_H55_vertex_resolution_found_in_bounded_search: false
    novelty_certificate_claimed: false
  newly_logged_related_literature:
    citation: "Roldan and Toala-Enriquez, Isoperimetric Formulas for Hyperbolic Animals, Graphs Combin. 41 (2025) 38"
    doi: 10.1007/s00373-025-02900-1
    exact_H55_animal_perimeter_coefficient: "sqrt(5)"
    normalization: "tile perimeter / dual edge boundary"
    resolves_frozen_outer_vertex_metric: false
  ownership_delta:
    I0101_p04_handoff: SIX_RUN_ROTATION_WITHOUT_RELEASE
    P0087: ACTIVE_HARD_OUTSIDE_NOT_R06_CLOSABLE_SUCCESSOR
    newly_certified_READY_closable_seen: 0
  audits:
    existing_other: R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z
    p26_end_to_end_i0056: PENDING_NOT_FOUND
  remaining_obligation: >-
    Admit an exact-source current-open ownership-clear genuinely CLOSABLE outside
    successor, or receive explicit lifecycle authorization changing the preserved
    R06 handoff state. For I0056 publication/closure history, separately reconcile
    the 2025 hyperbolic-animal edge-normalization paper and obtain the required P26
    end-to-end audit; do not confuse tile perimeter with outer vertex boundary.
  new_exact_artifact: NONE_LITERATURE_NORMALIZATION_ANALYSIS_ONLY
  new_audit: NONE
  shared_root_edits: NONE
  peer_edits: NONE
  scheduler_model_selector: null
  scheduler_reasoning_selector: null
  authenticated_runtime_model_telemetry: false
  guaranteed_duration_control: false
```

**End of immutable R06 run report.**