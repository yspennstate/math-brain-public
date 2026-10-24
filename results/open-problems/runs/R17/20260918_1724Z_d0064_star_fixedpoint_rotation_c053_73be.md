Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is not GPT-6 at maximum, and I do not claim otherwise. **NO SOURCE-METRIC MOVEMENT: D0064 `R_class: 0/3 -> 0/3`; ROTATION MOVEMENT: `NO_ACTIVE_HARD_SUCCESSOR -> D0064 CLAIMED / HARD OUTSIDE`; methods #2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #29 ADD THE POINTS AT INFINITY.**

# R17 C053 — D0064 star-equation classification: first counterexample-first run

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Lifecycle transition; binary LCS remains handed off

R17 does **not** reopen the binary Chvátal--Sankoff constant after the two permitted HARD recoveries were exhausted. Its frozen handoff remains

\[
0.792665992\le \gamma_2\le0.826275942762282626,
\qquad U-L=0.033609950762282626.
\]

The previous R17 report, `runs/R17/20260918_1612Z_h0021_reassignment_gate_delta_c052_4c2e.md`, correctly refused to overwrite the already-existing H0021 ownership record. H0021 still says `UNASSIGNED AFTER R16 HANDOFF`; it was not seized here.

Instead I screened an ownership-clear HARD target that had already been source-clarified by another lane: `D0064`. Immediately before claiming it, direct fetch of `operations/claims/D0064.md` at fresh `master` returned 404. R15's existing screen classified the source as `OPEN-LOOKING / SOURCE-SCOPE-CLARIFIED / HARD / NOT CLOSABLE-READY / NOT CLAIMED`; that was a mismatch for R15's CLOSABLE lane, not for R17's HARD lane.

I therefore created the canonical create-only claim

`operations/claims/D0064.md`

at commit

`678e22354f4a1b6515353d4f35af3646d6605ce1`.

This is the first lawful active target after the LCS handoff.

## 2. Exact source and frozen metric

Source: Rémi Rhodes and Vincent Vargas, *Gaussian multiplicative chaos and applications: a review*, arXiv:1305.6221, Section 6.3, Conjecture 6.4.

The source conjectures that every non-trivial ergodic lognormal star-scale-invariant random measure, under the source's strengthened dependence-decay assumptions, belongs up to a multiplicative constant to one of four families. The first family (`alpha=1`, `gamma^2<2d`) is the already-classified subcritical GMC regime. The source explicitly calls situations 2--4 conjectural:

1. `alpha=1`, `gamma^2=2d`: derivative/critical chaos;
2. `alpha<1`, `gamma^2<2d`: atomic GMC of the dual phase;
3. `alpha<1`, `gamma^2=2d`: atomic GMC of the frozen phase.

The fixed R17 metric is

\[
R_{\rm class}:=\#\{\text{the three conjectural regimes classified under the full source assumptions}\}.
\]

Before: `0/3`. After: `0/3`.

A theorem with an extra finite-moment, independently-scattered, regularisation, or representation hypothesis is PARTIAL and does not move this metric.

## 3. Source / later-literature check, 2026-09-18

I checked the primary Rhodes--Vargas record and the exact Conjecture 6.4 text, together with the nearest uniqueness literature:

- Allez--Rhodes--Vargas, arXiv:1102.1895: continuous lognormal star-equation uniqueness in the integrable/subcritical regime;
- Rhodes--Sohier--Vargas, arXiv:1201.5219: Lévy multiplicative-chaos/star-equation uniqueness under the paper's regularity and moment hypotheses;
- Bertacco--Hairer, arXiv:2504.07552, EJP 30 (2025), Paper 188: for broad convolution regularisations of log-correlated Gaussian fields, properly normalized supercritical GMC converges stably, with regularisation dependence only through a multiplicative constant, to the predicted integrated atomic measure driven by critical GMC.

The 2025 theorem is strong canonical-construction uniqueness, but the checked statement does **not** say that an arbitrary ergodic star-equation fixed point must come from such a regularisation. Thus it does not discharge Conjecture 6.4's universal fixed-point quantifier. This is a bounded dated prior-art check, not a worldwide novelty certificate.

## 4. Prior attempt recovered before research

The old D0064 intake attempt already recognized the continuous smoothing-transform viewpoint and the fact that ordinary positive-moment methods fail in the atomic regimes. R15's newer screen sharpened this to the exact `1+delta`-moment barrier and the distinction between canonical approximation universality and all-fixed-point classification.

I therefore did **not** repeat “try the existing smoothing-transform proof without its moment assumption.” The present run instead attacks possible *extra* fixed points and asks which deformation freedoms are actually available.

## 5. Method #2 — ATTACK THE NEGATION FIRST

The negation of Conjecture 6.4 would be an ergodic star-equation fixed point outside the four listed families. I tried three natural ways to manufacture one.

### 5.1 Random global scalar: not a route

Theorem 2.19 already contains an independent nonnegative scalar factor in the integrable representation, and the source explicitly imposes ergodicity to remove precisely this irrelevant degree of freedom. Thus mixing the predicted chaos by a non-degenerate global amplitude is not a source-valid counterexample route.

### 5.2 Multiply by a new stationary exact-scale random environment

A more serious attempt is to take a predicted solution `M_0` and twist it by an independent positive stationary field `H(x)`, hoping `H(x)M_0(dx)` still solves the same all-scale equation while leaving the four-family class.

This route collapses under a very small rigidity lemma.

**Lemma A (stationary exact-scale fields are spatially constant).**  Let `H=(H(x))_{x in R^d}` be a stochastically continuous random field. Suppose its finite-dimensional laws are stationary and, for every `c>0`,

\[
(H(cx_1),\ldots,H(cx_m))\stackrel d=(H(x_1),\ldots,H(x_m))
\]

for every finite tuple. Then for every fixed `x,y`, `H(x)=H(y)` almost surely. If the translation action on the law of `H` is ergodic, this common random value is deterministic.

**Proof.** Fix `x,y`. For `c_n downarrow 0`, stochastic continuity gives

\[
(H(c_nx),H(c_ny))\to(H(0),H(0))
\]

in probability. But every pair on the left has the same law as `(H(x),H(y))`. Hence for every `eta>0`,

\[
P(|H(x)-H(y)|>\eta)
=P(|H(c_nx)-H(c_ny)|>\eta)\to0.
\]

Thus `H(x)=H(y)` a.s. A spatially constant random field has every event determined by its common value invariant under translations, so ergodicity forces that value to be deterministic. QED.

This does not prove Conjecture 6.4 because a hypothetical exotic fixed point need not factor as an independent multiplicative twist. It does rule out a broad and otherwise tempting counterexample mechanism without any moment assumption.

### 5.3 Replace stable subordination by a different Lévy subordinator

The atomic families suggest another negation: keep the correct base chaos but subordinate it by some other independently scattered positive Lévy basis, e.g. a tempered-stable or gamma-type subordinator.

Exact all-scale homogeneity rules this out inside the independently-scattered class.

**Lemma B (homogeneous Lévy bases are stable).** Let `N_mu` be a nonnegative independently scattered Lévy random measure with deterministic control measure `mu`, with conditional Laplace functional

\[
E\exp\{-\int f\,dN_\mu\}
=\exp\{-\int \Phi(f(x))\,\mu(dx)\},
\]

where `Phi` is a Bernstein exponent. Suppose that for some `alpha in (0,1]` and every `c>0`,

\[
N_{c\mu}\stackrel d=c^{1/\alpha}N_\mu.
\]

Then

\[
\Phi(q)=Kq^\alpha
\]

for some `K>=0`; hence the only nontrivial such basis is positive `alpha`-stable (with the linear deterministic case at `alpha=1`).

**Proof.** Apply the scaling identity to one measurable set `A` with `0<mu(A)<infinity` and test `q 1_A`. Equality of Laplace transforms gives

\[
c\Phi(q)=\Phi(c^{1/\alpha}q)
\]

for every `c,q>0`. Writing `s=c^{1/\alpha}` yields `Phi(sq)=s^alpha Phi(q)`. Taking `q=1` gives `Phi(s)=Phi(1)s^alpha`. QED.

Again, this is a PARTIAL rigidity statement, and the mechanism is standard Lévy--Khintchine folklore rather than a novelty claim. Its value here is diagnostic: merely enlarging “stable subordinator” to “arbitrary Lévy subordinator” cannot produce a fifth family while preserving exact scaling.

**Outcome #2.** Three obvious counterexample freedoms collapse: global mixtures conflict with source ergodicity; independent stationary exact-scale multiplicative twists are trivial; independently-scattered exact-homogeneous subordinators are forced to be stable. A genuine counterexample, if one exists, must exploit *non-factorisable dependence* between spatial locations and/or between coarse and fine scales.

## 6. Method #18 — SAY IT IN ANOTHER LANGUAGE

The useful language is not “a mysterious random measure satisfying a functional equation,” but a **fixed point of a continuous smoothing semigroup acting on Laplace functionals**.

For a nonnegative random measure `M`, write

\[
\mathcal L_M(f)=E\exp\{-\langle f,M\rangle\}.
\]

The star equation at scale `epsilon=e^{-t}` makes `mathcal L_M` a fixed point of an operator `T_t` that first samples the coarse Gaussian multiplier and then applies a rescaled independent copy of the fine measure. The operators inherit the multiplicative scale law `T_{s+t}=T_s T_t` once the Gaussian increments are represented consistently.

The three conjectural families then have a common structural description:

- the base non-atomic control measure is the subcritical or critical GMC singled out by the Gaussian cocycle;
- the atomic phases are obtained from that control measure by a power-law Laplace exponent `q^alpha`;
- Lemma B says that this power law is forced as soon as a conditional independently-scattered representation exists.

So the source conjecture can be split into two conceptually different obligations:

**Representation obligation.** Show that every ergodic low-moment fixed point of the Gaussian smoothing semigroup admits a disintegration over the canonical subcritical/critical base chaos whose conditional fine measure is independently scattered (or prove an equivalent structural statement strong enough for Lévy--Khintchine).

**Rigidity obligation.** Once that representation exists, exact scale homogeneity forces the stable power law and leaves only the source's listed atomic phases.

The second obligation is elementary in the Lévy-basis formulation; the first is the genuinely hard missing theorem. This split is stronger than merely saying “the `1+delta` moment proof breaks”: it says exactly what structural fact would replace the missing moment argument.

## 7. Method #29 — ADD THE POINTS AT INFINITY

The low-moment barrier is awkward if one works with moments, because moments literally disappear at the regimes of interest. I therefore projectivized the Laplace exponent instead.

For an independently-scattered candidate with exponent `Phi`, quotient out the irrelevant multiplicative constant and compactify the Laplace variable by adjoining `q=0` and `q=infinity`. Exact scaling acts by translation on `log q`, while the normalized power law has

\[
\frac{\log \Phi(q)}{\log q}\to\alpha
\]

at both scale ends whenever it is exactly homogeneous. The conjectural parameter `alpha` becomes a boundary slope rather than a finite moment.

This suggests a route that remains meaningful when `E[M(A)]` is infinite: prove that the star semigroup forces a unique projective boundary slope and then upgrade regular variation to exact homogeneity using the *all-scales* equation. In scalar smoothing-transform theory, analogous boundary fixed-point classifications are often driven by regular variation rather than moments. Here the hard part is spatial: one must show that the Laplace functional asymptotically factorizes over separated sets strongly enough that a scalar Bernstein exponent emerges.

I do **not** have that factorization theorem in this run. The result of #29 is therefore a precise new proof target, not a claimed source advance:

\[
\boxed{\text{derive conditional independent scattering / asymptotic Laplace additivity from the source's dependence decay and exact star semigroup.}}
\]

If this can be proved, Lemma B closes the atomic rigidity step without any `1+delta` moment.

## 8. What moved and what did not

Mathematical source metric:

`R_class: 0/3 -> 0/3` — **no movement**.

Research-state movement:

`NO ACTIVE HARD SUCCESSOR -> D0064 canonically claimed by R17`.

Substantive mathematical output:

- exact rejection of stationary exact-scale multiplicative twists (Lemma A);
- exact rejection of non-stable independently-scattered homogeneous subordinators (Lemma B);
- reduction of the atomic-classification route to a representation theorem converting arbitrary low-moment star fixed points into a conditionally independently-scattered form;
- a moment-free Laplace-boundary formulation for the next attack.

No finite claim arose, so no exact-arithmetic checker was manufactured merely for bookkeeping. The two lemmas are proved on the page. Neither is asserted novel; Lemma B in particular is standard homogeneity/Lévy--Khintchine folklore.

## 9. Next run

Next Section-B methods: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #11 DUALIZE, #25 COUNT THE SAME THING TWICE.**

The most promising concrete target is to interpolate between separated test sets in the Laplace functional and differentiate a scale/coupling parameter to see whether the source's stronger dependence-decay assumption forces vanishing mixed Lévy cumulants. If it does, that would establish conditional independent scattering rather than assume it.

A second route is to dualize the fixed-point equation at the level of the logarithmic Laplace functional and seek an additive cocycle whose only projective eigenfunctions are `q^alpha`. Any theorem still assuming the desired disintegration will remain PARTIAL and will not move `R_class`.

## 10. Model / scheduler-control truth

The exposed task-management surface still provides title, prompt, timing/schedule and enablement controls, but no bindable model-family selector, reasoning-effort selector, authenticated completed-run model receipt, or guaranteed-duration field. Therefore GPT-6/maximum remains prompt text only on this surface.

Making it enforceable requires an owner-authorized product/workspace/API/admin surface that actually exposes and attests those settings, or a platform change. The historical P26 `You cannot modify this task` response was an authorization-context boundary; the lawful workaround is its owning/authorized context or platform support, not a duplicate task or permission bypass.

No scheduler, permission, email, Drive, public-posting, workflow, purchase, or peer-file mutation was performed.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R17
  allocation: HARD_OUTSIDE
  run_kind: ROTATION_AND_FIRST_SUBSTANTIVE_ATTACK
  predecessor:
    source: binary_Chvatal_Sankoff_constant
    lifecycle: HANDED_OFF_AFTER_HARD_RECOVERY_LIMIT
    research_reopened: false
    frozen_width: 0.033609950762282626
  skipped_released_candidate:
    id: H0021
    reason: EXISTING_CANONICAL_HISTORY_NOT_REASSIGNED_TO_R17
    overwritten: false
  active_target:
    id: D0064
    source: Rhodes_Vargas_arXiv_1305_6221_Conjecture_6_4
    lane: HARD_OUTSIDE
    claim_path: operations/claims/D0064.md
    claim_commit: 678e22354f4a1b6515353d4f35af3646d6605ce1
    claim_mode: CREATE_ONLY_AFTER_FRESH_404
    status: OPEN_LOOKING_PARTIAL
  metric:
    name: R_class
    before: 0
    after: 0
    denominator: 3
    movement: none
  methods_this_run: [2, 18, 29]
  method_outcomes:
    2:
      - GLOBAL_RANDOM_SCALAR_EXCLUDED_BY_ERGODIC_SOURCE_SCOPE
      - STATIONARY_EXACT_SCALE_MULTIPLICATIVE_TWIST_TRIVIAL
      - HOMOGENEOUS_INDEPENDENTLY_SCATTERED_LEVY_BASIS_FORCED_STABLE
    18: ARBITRARY_FIXED_POINT_CLASSIFICATION_SPLIT_INTO_REPRESENTATION_PLUS_STABLE_RIGIDITY
    29: MOMENT_FREE_PROJECTIVE_LAPLACE_BOUNDARY_ROUTE_IDENTIFIED
  new_source_level_regimes_closed: 0
  new_partial_lemmas: 2
  finite_checker_needed: false
  novelty_claim: false
  closure_claim: false
  next_methods: [5, 11, 25]
  shared_roots_edited: false
  peer_files_edited: false
  scheduler_or_permission_edits: false
  email_or_drive_used: false
```

**R17 has lawfully left the exhausted binary-LCS source, claimed D0064 in the HARD lane, and identified the new core obstruction: derive conditional independent scattering / Laplace additivity from the source assumptions rather than assuming it.**