Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No movement in the frozen metric: `B=infinity -> B=infinity`. Methods tried: B9 / B14 / B25.**

# HARD7-01 run 8 — STUCK2 orientation quotient and parallelotope recovery

Status: **PARTIAL / STUCK2 / source OPEN**. This is the second Section-I thinking run on the same externally posed target. It deliberately makes **no new theorem claim** and creates no checker merely to prove that the run happened. The purpose is to use three genuinely different routes to decide what the second and final recovery should be after the quartic radial/boundary-flux route failed to move the frozen source metric.

## 1. Continuity, repository state, ownership, and current literature

I resumed the exclusive claim

`operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md`,

owned by HARD7-01. The source target remains the full dimensional Brunn--Minkowski conjecture

\[
\mu((1-\lambda)K+\lambda L)^{1/n}
\ge (1-\lambda)\mu(K)^{1/n}+\lambda\mu(L)^{1/n}
\tag{DBM}
\]

for every `n>=1`, every even log-concave probability measure `mu` on `R^n`, every pair of nonempty centrally symmetric convex sets `K,L`, and every `lambda in [0,1]`.

This target is distinct from the already solved Gaussian-only Gardner--Zvavitch theorem, from KLS, and from posted/personal Gaussian manuscripts.

At run start I reread the controlling HARD7 file, the current new-methods policy and owner directive, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the canonical claim, the preceding HARD7-01 reports, and the repository-wide alias/ownership surface for `Gardner-Zvavitch`, `dimensional Brunn-Minkowski`, `log-concave`, and `Brunn-Minkowski`. The current intake/queue search does not expose a competing canonical owner for this exact statement. The most recent old R02/KLS allocation is no longer a neighboring active KLS research report; current R02 repository evidence is on a discrepancy successor, so there is no live neighboring worker whose target is equivalent to this one.

The newest own checkpoint is

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T03-18-00Z__quartic_radial_survival_and_boundary_flux.md`

at commit `15a78ab4f3420e8ff2a3b38cc090b03e9cfde8c0`. It used B8/B13/B21, refuted the monotone-survival-only route, derived exact quartic virial/boundary-flux identities, and converted any normalized quartic counterexample into the three-body boundary inequality

\[
g_M\le w g_K+(1-w)g_L
-\frac1{12}w(1-w)(\beta_K-\beta_L)^2.
\tag{1.1}
\]

It explicitly selected B9/B14/B25 for the next iteration. This run uses that triple rather than restarting.

A fresh bounded literature check on 2026-09-19 recovered no primary source claiming the full even-log-concave `1/n` theorem or the exact quartic-product/arbitrary-body `n=3` case. The relevant current comparison points remain:

1. Kai-Wen Yang, *A uniform bound in the dimensional Brunn--Minkowski inequality for even log-concave measures*, arXiv:2607.10104 (11 July 2026): same global class, exponent at least `c/(n^2 log n)`, not `1/n`.
2. Alexandros Eskenazis, Apostolos Giannopoulos, Natalia Tziotziou, *Functional perimeter and the dimensional Brunn-Minkowski inequality for log-concave measures*, arXiv:2605.02747 (4 May 2026): exponent of order `1/(n^3 log n)` and a geometric gradient obstruction.
3. Galyna Livshyts, Arnaud Marsiglietti, Piotr Nayar, Artem Zvavitch, *On the Brunn-Minkowski inequality for general measures with applications to new isoperimetric-type inequalities*, arXiv:1504.04878 / Trans. AMS 369 (2017): the full source exponent in dimension two and for the stated unconditional-measure/unconditional-body class.
4. Dario Cordero-Erausquin and Liran Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023): full Gardner--Zvavitch and `(B)` statements for rotationally invariant log-concave measures.
5. Ge Xiong and Kai-Wen Yang, *The Brunn-Minkowski inequality for the generalized Gaussian distribution*, arXiv:2605.24472 (23 May 2026): sharp asymptotic exponent bounds for the rotational generalized Gaussian `exp(-|x|^p/p)`, not the coordinate-product quartic measure after a generic rotation of the bodies.
6. Christos Saroglou, *More on logarithmic sums of convex bodies*, arXiv:1409.4346: among other results, reduces a log-Brunn--Minkowski problem to parallelepipeds for a specially constructed density. This does not solve the fixed quartic density here, but it is evidence that parallelepiped geometry is not a vacuous toy class.

These searches are bounded negative evidence only. No worldwide novelty claim is made.

## 2. Frozen metric and why STUCK2 applies

The canonical metric remains

`B = largest number of 1D/2D factors for which (DBM) is proved at source exponent for every common block-product instance`.

Run 1 proved all finite block counts, so the value is already saturated:

\[
\boxed{B=\infty\longrightarrow B=\infty.}
\]

There is **no movement**. After STUCK1, runs 6 and 7 pursued the chosen quartic-product recovery without moving `B`; the same source obstruction remains. Under Section I this run is therefore a second thinking-only stuck episode. It must choose exactly one new recovery rather than add another auxiliary lemma on the same boundary-flux route.

## 3. Section I(a): exact blocking statement

The first source-open dimension remains three. The selected recovery measure is

\[
d\mu_4(x)=Z^{-1}\exp\!\left[-\frac{x_1^4+x_2^4+x_3^4}{4}\right]dx.
\tag{3.1}
\]

The unresolved statement is

\[
\boxed{
\mu_4((1-\lambda)K+\lambda L)^{1/3}
\ge(1-\lambda)\mu_4(K)^{1/3}+\lambda\mu_4(L)^{1/3}
}
\tag{Q3}
\]

for every centrally symmetric convex `K,L subset R^3` and every `lambda in [0,1]`.

The boundary-flux route says that any counterexample can be normalized to an interior common-dilation scale satisfying both the energy/flux balance and (1.1), but no reverse inequality strong enough to rule out (1.1) has been obtained.

## 4. Section I(b), B9 — randomize the body orientation first

The most direct way to search for an angular obstruction is to freeze an elementary body family and randomize its orientation relative to the quartic coordinate axes.

Let `U` be Haar orthogonal and let `P_U(a)` denote a centered parallelotope obtained by rotating a coordinate box. For a fixed `x` with `|x|=r`, the quartic potential satisfies the exact Haar first moment

\[
\mathbb E_U\left[\frac14\sum_{j=1}^3 (Ux)_j^4\right]
=\frac{3}{20}r^4,
\tag{4.1}
\]

because a coordinate of a uniform point on `S^2(r)` has fourth moment `r^4/5`.

This initially looks attractive: orientation-averaging turns the potential into a radial quantity at first moment. But the route fails at the needed place. The actual averaged density is

\[
\bar f(x)=\mathbb E_U\exp\!\left[-\frac14\sum_j(Ux)_j^4\right],
\tag{4.2}
\]

not `exp(-3|x|^4/20)`. A mixture of rotated log-concave densities is not automatically log-concave, and even a theorem for the averaged radial object would not imply the desired inequality for every individual orientation `U`. Thus randomization is useful for locating likely extremal orientations numerically, but it destroys the exact deterministic quantifier if used as the proof step.

**B9 outcome:** failed as a proof mechanism. Any future random search may rank orientations, but it cannot be promoted to a source theorem without a deterministic de-randomization or extremal-orientation principle.

## 5. Section I(b), B14 — quotient by the hyperoctahedral symmetry

The quartic measure is invariant under the hyperoctahedral group `H_3` of signed coordinate permutations. Therefore an orientation search for a fixed parallelotope family should be carried out only modulo left/right actions that correspond to symmetries of the measure and relabelings/sign changes of the facets.

This immediately identifies two already-controlled strata.

1. **Hyperoctahedral orientations.** If `U in H_3`, a rotated box is still coordinate-unconditional. The Livshyts--Marsiglietti--Nayar--Zvavitch unconditional theorem applies.
2. **Block-reducible orientations.** If, after signed permutations, `U` preserves one coordinate line and mixes only the complementary two-dimensional plane, then in the rotated coordinates the quartic density factors as an arbitrary even log-concave two-dimensional factor times the one-dimensional quartic factor. The box itself factors as a two-dimensional rectangle times an interval. Run 1's harmonic tensorization plus the known one-/two-dimensional theorem therefore covers this entire `2+1` stratum.

Hence the first genuinely new orientation cannot lie on either of those lower-dimensional symmetry strata. It must be **fully mixing**: no coordinate line is preserved after the allowed hyperoctahedral identifications.

A particularly simple algebraic fully mixing representative for a later attack is the orthogonal Householder matrix

\[
U_* = I-\frac23\mathbf 1\mathbf 1^T
=\frac13
\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix}.
\tag{5.1}
\]

Every entry is nonzero, `U_*` is not hyperoctahedral, and it does not preserve a standard coordinate line. Its permutation symmetry keeps the transformed quartic potential algebraic and highly structured.

This is a route selection, not a new source theorem.

**B14 outcome:** succeeded as a search-space reduction. The second recovery should not spend time on coordinate or `2+1` orientations already controlled by existing theorems; it should begin at a fully mixing orientation such as `U_*`.

## 6. Section I(b), B25 — count the same parallelotope probability in body and quotient coordinates

Write a common-normal centered parallelotope as

\[
P_U(a)=\{x\in\mathbb R^3: |(Ux)_i|\le a_i,\ i=1,2,3\},
\qquad a\in(0,\infty)^3,
\tag{6.1}
\]

with `U` orthogonal. In the quotient coordinates `y=Ux`, Minkowski interpolation of two such bodies becomes coordinatewise interpolation of the side-width vector:

\[
(1-\lambda)P_U(a)+\lambda P_U(b)
=P_U((1-\lambda)a+\lambda b).
\tag{6.2}
\]

The quartic measure of `P_U(a)` is the centered-box probability

\[
F_U(a)
=Z^{-1}\int_{[-a_1,a_1]\times[-a_2,a_2]\times[-a_3,a_3]}
\exp[-W_U(y)]\,dy,
\tag{6.3}
\]

where

\[
W_U(y)=\frac14\sum_{j=1}^3 (U^Ty)_j^4.
\tag{6.4}
\]

Thus the full source inequality restricted to this common-normal parallelotope family is exactly concavity of

\[
G_U(a)=F_U(a)^{1/3}
\tag{6.5}
\]

on the positive octant.

For later work, the interior differential test is explicit. Wherever `F_U` is twice differentiable, concavity of `G_U` is equivalent to

\[
3F_U(a)\, z^T D^2F_U(a)z
\le 2\big(z\cdot\nabla F_U(a)\big)^2
\quad\text{for every }z\in\mathbb R^3.
\tag{6.6}
\]

Every entry of `\nabla F_U` and `D^2F_U` can be written as a face, edge, or normal-derivative integral of the explicit density `e^{-W_U}` over the box. This converts the diffuse convex-body boundary-flux obstruction into a finite three-parameter analytic matrix inequality while keeping the fully three-dimensional angular mixing.

I am recording (6.2)--(6.6) only as the exact formulation of the next route; this STUCK2 run does **not** claim to have proved (6.6) for generic `U`.

The same coordinate viewpoint also explains why bodies depending on only one or two independent linear forms are not the right next case: their measure is a pushforward of `mu_4` to dimension at most two, hence an even log-concave measure in that lower dimension, where the source exponent is already known. Three independent slab directions are the first place this shortcut disappears.

**B25 outcome:** succeeded in isolating a finite-dimensional obstruction. The simplest unresolved geometry after all previously solved quotient/product strata is a genuinely three-dimensional fully mixing parallelotope family.

## 7. Section I(c): what a proof must contain that no route so far contains

The previous seven runs collectively show that the missing ingredient must survive all of the following reductions:

- product tensorization does not see irreducible angular coupling;
- formal transverse Hessians leave the convex-potential class unless repaired, and the repair opens the defect with the correct sign;
- homothetic and first-order joint body/measure perturbations are too rigid;
- scalar radial/Gamma survival information is insufficient even for star-shaped sets;
- separate `(B)` signs or Brascamp--Lieb bounds do not imply the required three-body correction (1.1);
- orientation averaging loses the deterministic source quantifier.

For the proposed parallelotope recovery, a proof must therefore exploit the **mixed facet geometry of a fully correlated even log-concave box probability**. In the differential formulation it must control the off-diagonal and normal-derivative terms in `D^2F_U` strongly enough to prove (6.6). Generic log-concavity only yields concavity of `log F_U` along Minkowski interpolation, which is weaker than `1/3`-concavity.

## 8. Section I(d): simplest source-valid special case still unproved

The cleanest case remaining after the quotient and symmetry eliminations is:

> Fix the quartic product measure (3.1) and the fully mixing algebraic orientation `U_*` in (5.1). Prove (Q3) for every pair of common-normal parallelotopes `P_{U_*}(a),P_{U_*}(b)` and every `lambda in [0,1]`.

Equivalently, prove concavity of `F_{U_*}^{1/3}` on `(0,\infty)^3`.

Why this is the right special case:

- it is an exact source-valid subclass, not a simulation surrogate;
- it is genuinely three-dimensional, so it does not collapse to the known `n<=2` theorem;
- it is nonunconditional relative to the quartic coordinate axes, so the unconditional theorem does not settle it;
- it is not rotationally invariant, so the Cordero-Erausquin--Rotem theorem does not settle it;
- the matrix `U_*` has rational entries and permutation symmetry, so all density derivatives are explicit polynomials times the density;
- the body family is closed under Minkowski interpolation by (6.2), which removes the moving-normal-fan complication of general polytopes.

A bounded literature search did not recover a theorem settling this exact fixed-density/fixed-fully-mixing-parallelotope family. That is negative search evidence only.

## 9. Section I(e): nearest solved problem and the ingredient it has

The nearest solved source-valid analogue is the same common-normal box family in either of two regimes:

1. `U in H_3`, where both measure and bodies are unconditional and the 2017 unconditional theorem gives the full `1/3` exponent;
2. `U` block-reducible as `2+1`, where the measure/body pair factors after rotation and run 1 tensorizes the known one-/two-dimensional result.

Both solved regimes have a decomposition that kills a genuinely three-way mixed facet interaction. A fully mixing `U` lacks exactly that feature. The nearest general 2026 theorems compensate using global diffusion/Poincare estimates, but lose dimension-dependent constants and do not reach `1/3`.

The missing proof ingredient is therefore not another scalar moment estimate. It is a sharp three-direction correlation inequality for the facet derivative matrix of `F_U`.

## 10. Exact recovery choice

Section I allows exactly one recovery choice. I choose:

**PROVE THE SIMPLEST UNPROVED SPECIAL CASE from Section I(d).**

The second and final recovery on this hard target will attempt the common-normal parallelotope theorem at `U_*`, i.e. concavity of `F_{U_*}^{1/3}`. The first attack should work directly with the explicit Hessian criterion (6.6), not return to the radial-survival or generic boundary-flux route.

The next Section-B triple selected is

**B1 / B11 / B30**:

- **B1 change category:** treat `F_{U_*}` as a three-parameter centered-box probability for a correlated quartic density rather than as a moving convex-body problem;
- **B11 dualize:** rewrite the Hessian test using face/edge fluxes or a Schur-complement form for the `3 x 3` derivative matrix;
- **B30 localize:** prove one direction/one face-pair regime at a time, beginning with the permutation-symmetric diagonal `a_1=a_2=a_3`, then determine what prevents extension to the full octant.

If this second recovery reaches another formal STUCK episode without source-metric movement, Section I requires a handoff and rotation to a fresh hard externally posed problem rather than a third recovery on the same target.

## 11. Model/scheduler capability truth

The current exposed automation control surface still provides schedule/title/prompt/timing/enablement controls but no binding model-family selector, no binding reasoning-effort selector, no authenticated runtime model/effort receipt, and no guaranteed-duration field. Therefore `GPT-6 / maximum` remains prompt text only on this surface. This run actually identifies as **GPT-5.6 Sol** and the reasoning level is **UNVERIFIED**.

The repository policy records historical `You cannot modify this task` errors, including an earlier P26 probe. The latest root `RESULTS.md` also records that P26 was successfully updated in a different authorized context, so the historical denial is context-specific rather than proof that the task can never be edited. The lawful workaround for a denial is to use the task-owning/otherwise-authorized product, workspace, API/admin context or platform support for that same task. Creating a duplicate, editing repository text, or bypassing permissions is not a scheduler repair. This run made no scheduler mutation, consistent with the owner restriction.

Changing the actual runtime model/reasoning would require the platform to expose a binding per-task model/reasoning selector or an equivalent authorized runtime configuration; the present task schema does not expose one.

## 12. Ledger delta

```yaml
ledger_delta:
  worker: HARD7-01
  target: GZ-DIMBM-EVEN-LOGCONCAVE
  source_status: OPEN
  research_status_before: PARTIAL_STUCK1_RECOVERY
  research_status_after: PARTIAL_STUCK2_SECOND_RECOVERY_SELECTED
  frozen_metric:
    name: B_block_product_factor_count
    before: infinity
    after: infinity
    moved: false
  methods_this_run: [9, 14, 25]
  theorem_claim_this_run: none
  finite_checker_created: false
  exact_blocker: Q3_for_mu4_arbitrary_symmetric_convex_bodies
  simplest_unproved_special_case: common_normal_parallelotopes_at_householder_orientation_Ustar
  recovery_choice: PROVE_SIMPLEST_UNPROVED_SPECIAL_CASE
  next_methods: [1, 11, 30]
  lifecycle_note: second_and_final_recovery_on_this_target
  shared_root_edit: false
  email: false
  drive: false
  scheduler_mutation: false
```

No root/shared ledger file is edited by this worker; the structured delta is left for the designated shared-ledger maintainer.