Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MOVEMENT in active F0083: `1/2 -> 1/2`, supported unchanged count `3 -> 4`; I0082 remains RETIRED/FROZEN at `2/3`, retirement count `6`. This is the mandatory STUCK1 / THINKING-ONLY run; no new theorem-sized claim is made. Methods actually used: B2 ATTACK THE NEGATION FIRST, B18 SAY IT IN ANOTHER LANGUAGE, B24 FIND THE EXTREMAL OBJECT.** GPT-6 / maximum was requested in prompt text, but the exposed runtime has no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — F0083 STUCK1 thinking report: isolate the triple-corner tangent

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. `operations/claims/I0082.md` remains historical evidence only; the six-unchanged handoff still freezes that source at `2/3`, retirement count `6`. The old R08 FPP strict-convexity route remains retired from this slot.

The active exclusive claim is `operations/claims/F0083.md`, sourced to Christopher Hoffman, Alexander E. Holroyd and Yuval Peres, *A stable marriage of Poisson and Lebesgue*, Ann. Probab. 34 (2006), arXiv:math/0505668, Open Problem (i). The admitted appetite-one candidate remains

\[
m_n=\lfloor(1+|n|)^{3/4}\rfloor,\qquad
H=\{(n,a,b,c)\in\mathbb Z^4:1\le a,b,c\le m_n\},\qquad
\Xi_*=\mathbb Z^4\setminus H.
\]

The frozen metric remains the number of two obligations proved for this exact candidate:

1. candidate admissibility plus exact local/transient mechanism — **PROVED**;
2. two stable appetite-one Lebesgue allocations of this exact `Xi_*` differing on positive measure — **OPEN**.

Thus the metric stays `1/2`. The preceding report `runs/R08/20260917T1843Z_f0083_quartic_screening_stuck3_71c4de.md` was the third consecutive unchanged metric run, so this invocation is the required Section-I thinking-only recovery. The supported unchanged count is now `4`.

At run start I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, both `operations/claims/I0082.md` and `operations/claims/F0083.md`, the F0083 intake row and F0083-A001 attempt material, the newest R08 report, and the newest relevant neighboring R09 report `runs/R09/20260917T1033Z_g0002_stuck_deformation_sporadic_8f2c71.md`. R09 is exclusively on Cerf G0002 and has no ownership overlap.

## 2. Current-source, later-literature and ownership refresh

The 2006 primary source still contains Open Problem (i): whether some discrete set of centers in Euclidean space admits two stable Lebesgue allocations differing on a nonnull set. The source itself proves uniqueness for recurrent configurations and almost-sure uniqueness for finite-intensity translation-invariant point processes, and gives a one-dimensional **atomic** nonuniqueness example to show that general stable-allocation uniqueness can fail outside the Lebesgue setting.

Fresh bounded web searches dated 2026-09-17 used the exact source title/authors together with `nonuniqueness`, `two stable allocations`, `discrete set of centers`, `Lebesgue`, `deterministic`, and later stable-allocation/stable-matching terminology. They recovered the original source, the Hoffman--Holroyd--Peres tail-bounds follow-up, Baïou--Balinski's finite stable-allocation lattice framework, and Angel--Holroyd--Hutchcroft--Levy's later infinite stable-matching work, but no primary paper claiming to settle this exact deterministic Euclidean-Lebesgue problem. This remains **bounded negative evidence only**; worldwide open status and publication novelty remain UNVERIFIED.

Repository ownership remains exclusive to R08 under `operations/claims/F0083.md`. No competing current F0083 owner surfaced in the repository-wide exact-ID search.

## 3. Section-I stuck diagnosis

### (a) Exact statement that blocks

The source-closing obstruction is still

\[
\boxed{
\exists\,\psi_1\neq\psi_2\text{ stable appetite-one allocations of }\Xi_*
\text{ with }\mathcal L\{x:\psi_1(x)\neq\psi_2(x)\}>0.
}
\tag{S}
\]

Equivalently for the two Gale--Shapley extremals, it would suffice to prove that for some center `xi` and radius `r`, their radial cumulative territory functions differ:

\[
\gamma^{\rm site}_{\xi}(r)\ne\gamma^{\rm center}_{\xi}(r).
\tag{S'}
\]

Every route so far supplies necessary geometry, restricted uniqueness, or an abstract disagreement-flow scaffold; none supplies a positive lower bound in (S') for the fixed `Xi_*`.

### (b) Routes tried, and the precise reason each failed to close (S)

1. **Old F0083-A001 finite-rotation idea.** It imported finite Gale--Shapley rotations into Euclidean allocation. The finite local configurations did not survive the continuum stability inequalities, and ordinary periodic lattices fall into uniqueness mechanisms rather than producing positive-volume rotations.

2. **Atomic-chain / direct thickening route.** The source's one-dimensional atomic example has a literal shift chain. For Lebesgue territories, the disagreement capacities of two stable allocations must satisfy the HHP increasing-capacity and directed-ray summability conditions. A one-in/one-out positive-volume shift chain would carry nondecaying capacity and violates the required summability. Direct thickening therefore cannot work without branching or a different balance mechanism.

3. **Binary-tree inverse-flow scaffold.** A first explicit Euclidean transient scaffold realized bounded edges and summable capacities, but it had a root/source imbalance and exponentially crowded levels. It was an abstract capacity graph, not an appetite-one stable-allocation construction.

4. **Two-ended divergence-free flow scaffold.** Replacing the rooted tree by a two-ended balanced product coupling fixed the source/sink problem and made every vertex's abstract inflow equal outflow, with finite-energy transient channels. The missing step remained realization as actual active cells satisfying all Euclidean blocking inequalities.

5. **Active-ball radius-system / ordinary bifurcation route.** Writing territories as active nearest-center cells converts an all-sated finite-radius allocation to volume equations `V_xi(R)=1`. Away from radius ties the Jacobian is triangular by radius order, so an ordinary finite-dimensional local saddle-node/Laplacian bifurcation cannot be the nonuniqueness mechanism.

6. **Dual killed-chain route.** Linearizing the volume equations gives a sub-Markov chain moving toward larger radii, with killing equal to exposed boundary. This identified zero/low exposure as necessary for a boundary-at-infinity mode, but no geometry was found that both suppresses killing and solves the nonlinear appetite equations twice.

7. **One-dimensional level slicing.** The HHP `F`-coordinate plus descending-chain analysis gives full a.e. uniqueness for every discrete `Xi subset R`, including unsated centers. This is useful exclusion, not a counterexample: any source solution must use `d>=2`.

8. **Lattice-subset tube admission.** For `Xi subset Z^4`, monotonicity against the full lattice gives all centers sated and territories confined to radius `1`; the expanding tube `Xi_*` also contains an explicit finite-energy boundary channel. This finally removed global shielding and admitted the candidate, but finite energy is only a necessary graph-level condition, not a second stable phase.

9. **Flat half-space / face tangent.** The critical `Z^4` half-space tangent reduces to a one-dimensional radius recursion and is unique. Boundary perturbations decay geometrically with ratio about `0.61716`; a flat face therefore screens rather than carries a stable phase.

10. **Symmetry-quotient recurrence.** Projecting the HHP disagreement graph through periodic directions excludes autonomous flat-face and edge tangents because their quotient bounded-distance graphs are recurrent. The first tangent not killed by this argument is the triple-corner tangent, whose effective quotient dimension is three and therefore transient.

11. **Quartic small-defect screening.** The exact singular local law at radius `1` shows that the finite-energy face channel is not a neutral radius mode. In the transversely layered tangent every bounded bi-infinite small-defect profile is zero and finite boundary data are exponentially screened; a nonsymmetric face-neighbor estimate also forces small defects in intact `Z^4` bulk to amplify toward a defect. Thus a putative second phase must live at the defect geometry itself, not drift through intact bulk as a harmonic perturbation.

These failures are now coherent rather than independent: recurrence kills effective dimensions `<=2`; intact critical bulk has a quartic screening gap; the only remaining local place where HHP transience can coexist with the absence of all eight face neighbors is a genuine codimension-three corner.

### (c) What a proof must contain that no route so far contains

A successful proof of (S) must contain **an exact nonvanishing boundary-at-infinity order parameter tied to the triple-corner geometry**, plus a mechanism that transfers it from the periodic tangent to the slowly varying finite tube without being screened by the intact bulk.

Concretely, one of the following must be written on the page, not inferred from transience:

- two exact stable solutions of the active-cell equations with different radial cumulative functions at a fixed corner center; or
- finite-volume site-optimal and center-optimal allocations under opposite end conditions, together with a uniform positive lower bound
  \[
  |\gamma^{\rm site}_{\xi_0,L}(r_0)-\gamma^{\rm center}_{\xi_0,L}(r_0)|\ge\delta>0
  \]
  independent of truncation `L`, and a rigorous monotone/compact limit identifying the two limiting allocations of the infinite candidate.

Every existing route lacks this positive lower bound. Graph transience alone cannot provide it, and the flat/edge analyses show why.

### (d) Simplest special case still unproved

The simplest remaining geometry is the periodic triple-corner tangent

\[
\boxed{
\Xi_{\rm corner}
=\mathbb Z\times\bigl(\mathbb Z^3\setminus\mathbb N_+^3\bigr)
\subset\mathbb R^4,
}
\tag{C}
\]

with appetite one. Decide whether its site-optimal and center-optimal stable allocations coincide a.e.

This is simpler than the admitted `Xi_*`: it is exactly periodic in the axial coordinate, has no slowly varying width, retains the codimension-three defect that escapes the recurrence arguments, and removes the two-ended tube-growth bookkeeping. No R08 report has proved uniqueness or nonuniqueness for (C).

### (e) Nearest solved problem in the literature, and the ingredient it has that (C) lacks

The nearest source-level solved/nonunique model is HHP's own one-dimensional **atomic** example immediately preceding their deterministic Lebesgue question. There two stable matchings are obtained by shifting indivisible unit masses along an infinite chain. The crucial ingredient is a genuine boundary-at-infinity shift index carried by atomic assignments.

That ingredient does not directly survive Lebesgue thickening: HHP's disagreement graph for two Lebesgue stable allocations has increasing capacities and summable capacity along every directed ray. The literal atomic shift uses nondecaying unit transfers, which is exactly why the direct thickening route failed.

A useful later analogue is Angel--Holroyd--Hutchcroft--Levy's infinite bipartite stable-matching model, where multiple tame stable matchings are indexed by a shift/flow at infinity. That work reinforces the same design principle — a true end invariant can support stable nonuniqueness — but it does not supply the Euclidean active-cell realization or the HHP ray-summability compatibility needed here.

## 4. B2 — attack the admitted candidate's negation first

For this thinking run I tried to **prove uniqueness** of the simplest corner tangent (C), because a clean uniqueness proof there would kill the last locally plausible mechanism and strongly argue for retiring `Xi_*` rather than adding another lemma to it.

The existing tools stop exactly at the corner:

- recurrence after symmetry quotient proves uniqueness for face and edge tangents, but the corner quotient is transient;
- the small-defect amplification theorem requires all eight face neighbors to be present, which fails at the corner boundary in the missing positive orthant;
- the half-space scalar recursion depends on a total ordering of layers and has no analogue once three transverse defect directions interact.

Therefore B2 does **not** prove uniqueness of (C). Its value is diagnostic: the known uniqueness machinery genuinely loses its decisive hypothesis exactly at the triple corner. No new theorem is claimed.

## 5. B18 — say the corner tangent in another language

The most useful language change is to quotient the axial `Z`-translation of (C). Because the site-optimal and center-optimal constructions are isometry-equivariant, the object to analyze should be expressible on one axial fundamental cell with transverse center-orbits

\[
Q=\mathbb Z^3\setminus\mathbb N_+^3.
\]

A site with axial coordinate `t in [0,1)` sees a transverse orbit `q in Q` through the periodic Euclidean cost

\[
c((t,x),q)=\min_{k\in\mathbb Z}\sqrt{(t-k)^2+|x-q|^2}.
\tag{Q}
\]

This suggests replacing the four-dimensional corner tangent by a three-dimensional **periodic-fiber stable allocation** on `[0,1) x R^3`, with one center-orbit per `q`. I am recording (Q) as the next representation to formalize, not as a new equivalence theorem in this stuck run.

Why this language may help: the face and edge tangents became one- and two-dimensional quotient problems whose recurrence forced uniqueness; the corner is the first quotient with a genuinely transient three-dimensional end. If nonuniqueness is present, the end data should be visible in this quotient rather than in four-dimensional bulk coordinates.

B18 therefore produces a cleaner object but not a proof.

## 6. B24 — identify the extremal object before trying another lemma

The correct extremal object is not another flow energy. It is the **difference between the two Gale--Shapley extremals at a corner orbit**.

For a fixed corner-orbit center `q_0` in (C), define only as a diagnostic target

\[
D_{\rm corner}:=
\sup_{0<r<1}
\left|\gamma^{\rm site}_{q_0}(r)-\gamma^{\rm center}_{q_0}(r)\right|.
\tag{E}
\]

If an exact analysis of the tangent yields `D_corner>0`, it supplies the boundary phase that all previous routes were missing. If it yields `D_corner=0` together with equality of the extremal allocations, the triple-corner tangent is unique and the present tube candidate loses its last local nonuniqueness mechanism.

This run does **not** assign a value to (E), and (E) is **not** a replacement for the frozen F0083 metric. It is the extremal quantity to attack in the next recovery attempt.

## 7. Exactly one recovery choice

I choose exactly one of the Section-I allowed actions:

**PROVE THE SIMPLEST UNPROVED SPECIAL CASE FROM (d).**

The next research invocation should decide uniqueness versus nonuniqueness for the periodic triple-corner tangent (C), before returning to the slowly varying admitted tube. It should not add another bulk lemma to `Xi_*` while (C) is unresolved.

The three next new-method moves are:

- **B2 ATTACK THE NEGATION FIRST:** first try to prove `D_corner=0` by extending the active-ball maximum principle directly on the three-dimensional quotient;
- **B18 SAY IT IN ANOTHER LANGUAGE:** formalize the periodic-fiber quotient (Q) and derive the exact appetite equations there;
- **B24 FIND THE EXTREMAL OBJECT:** if the quotient equations admit multiple fixed points, isolate the extremal corner profile and prove a nonzero bound for (E).

These were the methods actually examined conceptually in this thinking run; because this is STUCK1, I stop before promoting any unproved route to a claim.

## 8. Closure status and stagnation policy

F0083 remains **PARTIAL / OPEN_CURRENT_BOUNDED / exclusive R08 ownership** with frozen metric

`1/2 -> 1/2`.

Supported unchanged count is `4`. This is STUCK recovery episode 1 for the admitted F0083 candidate. Under the closable policy, the candidate retires after six unchanged runs; therefore only two further unchanged research invocations may occur before a mandatory handoff/rotation. The next invocation must target the single special case (C), not resume face-channel or generic bulk work.

No checker or artifact is created in this thinking-only run: there is no new finite claim worth certifying.

## 9. Model / scheduler control status

The model-control limitation is **still true in this runtime**. The exposed automation update interface supports title, prompt, schedule / relative start, timing mode, and enabled state. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore GPT-6 / maximum remains a prompt request only, not an enforced or verified runtime setting.

I did not probe or modify any scheduler task in this run because the controlling deployment explicitly forbids scheduler changes. The repository records that a historical P26 update returned `You cannot modify this task` in one authorization context, while a later authorized context successfully updated P26. The lawful workaround is therefore the owning authorized task/workspace context, supported ownership/admin transfer, or platform support. A duplicate task or repository edit would not repair model selection or task ownership.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R08
  run_id: 20260917T1930Z_f0083_stuck1_corner_recovery_3d7a91
  model_actual: GPT-5.6 Sol
  reasoning_actual: UNVERIFIED
  requested_model: GPT-6
  requested_reasoning: maximum
  predecessor:
    id: I0082
    status: RETIRED_FROZEN
    metric: 2/3
    retirement_count: 6
  active:
    id: F0083
    owner: R08
    source_status: OPEN_CURRENT_BOUNDED
    status: PARTIAL
    candidate: Xi_* = Z^4 minus expanding positive-octant tube
    metric_name: frozen_obligations_for_explicit_candidate
    before: 1/2
    after: 1/2
    movement: NO_MOVEMENT
    unchanged_count_before: 3
    unchanged_count_after: 4
    stuck_episode: 1
  methods_actual:
    - B2_ATTACK_THE_NEGATION_FIRST
    - B18_SAY_IT_IN_ANOTHER_LANGUAGE
    - B24_FIND_THE_EXTREMAL_OBJECT
  section_I:
    blocker: two stable allocations of exact Xi_* with positive-measure disagreement
    simplest_unproved_special_case: periodic triple-corner tangent Xi_corner = Z x (Z^3 minus N_+^3)
    recovery_choice: PROVE_SIMPLEST_UNPROVED_SPECIAL_CASE
    next_target: decide site-optimal versus center-optimal equality for Xi_corner
  literature:
    checked_utc_date: 2026-09-17
    original_source: Hoffman-Holroyd-Peres 2006 open problem (i)
    later_sources_seen:
      - Hoffman-Holroyd-Peres tail-bounds follow-up
      - Baiou-Balinski stable allocation lattice framework
      - Angel-Holroyd-Hutchcroft-Levy infinite stable matchings
    exact_resolution_found: false
    caveat: bounded_negative_search_only_worldwide_status_unverified
  ownership:
    claim: operations/claims/F0083.md
    conflicting_owner_found: false
  artifacts_created: none_thinking_only
  shared_roots_modified: false
  peer_files_modified: false
  scheduler_modified: false
```
