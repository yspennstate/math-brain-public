Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen source metric `D_MI: 2 -> 2`. Methods tried: B12 / B15 / B30.**

# HARD7-01 — maximal-intersection uniqueness, cube-collar iteration

**Status:** PARTIAL / source OPEN. **Unchanged-source-metric streak on this admitted target: 2.** This run produces a source-relevant exact theorem for an all-dimensional family, but it does **not** prove the full `n=3` source statement and therefore does not move `D_MI`.

## 1. Continuity, ownership, and required readback

I resumed the exact admitted target from

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T17-06-00Z__weakB_handoff_ak_equality_refutation_mi_admission.md`

and the exclusive claim

`operations/claims/MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS.md`.

I reread `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest own checkpoint, current claim record, and bounded repository/intake/neighbor searches around the Artstein-Avidan--Katzin / maximal-intersection aliases. The repository collision state still identifies **HARD7-01** as the owner. No competing owner was found, so this run continues the existing claim rather than creating a bypass alias.

The active source question remains the Artstein-Avidan--Katzin maximal-intersection uniqueness question: for a centrally symmetric convex body and an intermediate prescribed ellipsoid volume, is the maximum-intersection ellipsoid unique? The verified universal baseline remains Bochi's planar theorem, hence `D_MI=2`.

## 2. Current-literature delta, 2026-09-19

Fresh bounded searches checked the canonical phrases `maximal intersection ellipsoid`, `maximal intersection position`, `strong B equality`, and the 2026 stability literature.

Relevant sources checked:

1. Shiri Artstein-Avidan and David Katzin, *Isotropic Measures and Maximizing Ellipsoids: Between John and Loewner*, Proc. AMS 146 (2018), arXiv:1612.01128. This is the primary source and defines maximal-intersection position by
   `Vol(K cap r B_2^n) >= Vol(K cap r T B_2^n)` for every `T in SL_n`.
2. Jairo Bochi, *On the approximation of convex bodies by ellipses with respect to the symmetric difference metric*, arXiv:1702.03808. Its abstract explicitly says general uniqueness is open and proves `d=2`.
3. Dario Cordero-Erausquin and Liran Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), DOI 10.1214/22-AOP1604. Their strong `(B)` theorem includes the uniform probability measure on the Euclidean ball and gives log-concavity of `t -> mu(e^{tA}K)` for symmetric `A`.
4. **Bibliographic correction to the prior checkpoint:** *Stability and the equality case in the B-theorem*, arXiv:2305.17794, is by **Orli Herscovici, Galyna V. Livshyts, Liran Rotem, and Alexander Volberg**, not by Putterman. It treats Gaussian strong-`(B)` equality/stability and explains that uniqueness for maximal-intersection position of the uniform ball would follow from the corresponding no-nontrivial-equality statement; it leaves that uniform-ball problem for future work.
5. Eli Putterman, *Sharp stability for the (B)-theorem*, arXiv:2608.08472 (submitted 2026-08-09, updated 2026-08-11), gives dimension-free Gaussian / `1`-log-concave strong-`(B)` stability. Its abstract does **not** state the uniform-ball maximal-intersection uniqueness theorem. I therefore do not treat it as a resolution of the present source question.
6. A 2024 functional maximal-intersection analogue (Hoehner--Roysdon, arXiv:2401.01033) appeared in the bounded search but does not state a resolution of the original uniqueness problem.

Searches for the exact phrases `cube maximal intersection ellipsoid` and `box maximal intersection position` returned the original maximal-intersection source but no theorem matching the cube-collar result below. This is **bounded negative evidence only, not a novelty certificate**.

## 3. Counterexample candidate selected

The natural stationary test family is the hypercube. It has enough symmetry that the first variation at a Euclidean ball is forced to vanish, so unlike the slack-coordinate product box from the preceding run, it is a serious candidate for a flat strong-`(B)` direction.

The question attacked in this run is therefore:

> Can a cube in genuine intermediate maximal-intersection position have a nontrivial volume-preserving ellipsoidal flat direction?

The answer is **no** in an explicit all-dimensional collar near the John radius.

## 4. Exact cube-collar theorem

### Theorem (centered maximal-intersection uniqueness for the cube collar)

Let `n>=2`, `a>0`, and

`K_a=[-a,a]^n`.

Fix a prescribed radius `r` with

`a < r < sqrt(2) a`.

Among all **origin-centered** ellipsoids of volume `kappa_n r^n` (equivalently the exact `r T B_2^n`, `T in SL_n`, family used in the source definition of maximal-intersection position), the Euclidean ball `r B_2^n` is the **unique** maximizer of

`Vol_n(K_a cap E)`.

Moreover, after scaling `r=1` and writing `s=a/r in (1/sqrt(2),1)`, for every nonzero symmetric trace-zero matrix `A`, if

`F_A(t)=Vol_n(K_s cap e^{tA} B_2^n)`,

then

`F_A'(0)=0`

and

`F_A''(0)
 = -2 kappa_{n-1} s (1-s^2)^((n-3)/2)
   [ (n s^2-1) D(A) + 2(1-s^2) O(A) ] < 0`,

where

`D(A)=sum_i A_ii^2`,

`O(A)=sum_{i != j} A_ij^2`.

Thus the cube has an explicit strict strong-`(B)` curvature gap in every nontrivial determinant-one ellipsoidal direction in this collar.

### Proof

Scale by `r`, so it is enough to treat `r=1` and `K_s=[-s,s]^n` with

`1/sqrt(2) < s < 1`.

Fix symmetric `A` with `tr A=0`. Put

`F_A(t)=Vol_n(K_s cap e^{tA}B_2^n)`.

Since `det(e^{tA})=1`, changing variables gives

`F_A(t)=Vol_n(B_2^n cap e^{-tA}K_s)`.

By the Cordero-Erausquin--Rotem strong `(B)` theorem for the uniform probability measure on `B_2^n`, the function

`t -> F_A(t)`

is log-concave on the full real line.

It remains to prove that `t=0` is a strict local maximum in every nonzero direction. This is where the cube and the collar `s>1/sqrt(2)` give an exact calculation.

Write `e_1,...,e_n` for the standard basis and, for small `t`, set

`v_i(t)=e^{tA}e_i`,

`u_i(t)=v_i(t)/|v_i(t)|`,

`h_i(t)=s/|v_i(t)|`.

After the same determinant-one change of variables, membership in the transformed cube is

`|<u_i(t),x>| <= h_i(t)` for every `i`, with `x in B_2^n`.

At `t=0`, `u_i(0)=e_i` and `h_i(0)=s`. The excluded two-sided spherical-cap regions

`{|x_i|>s} cap B_2^n`

are pairwise disjoint: if both `|x_i|>s` and `|x_j|>s`, then

`|x|^2 > 2s^2 > 1`,

impossible in the unit ball. The inequality is strict, so compactness/continuity gives `epsilon(A,s)>0` such that these moving cap regions remain pairwise disjoint for `|t|<epsilon`.

Let `C_n(h)` be the volume of the two opposite unit-ball caps cut off at signed coordinate distance `h`:

`C_n(h)=2 kappa_{n-1} integral_h^1 (1-z^2)^((n-1)/2) dz`.

Hence, for sufficiently small `t`, the cap regions do not overlap and

`F_A(t)=kappa_n - sum_i C_n(h_i(t))`.        (1)

The cap derivatives are exact:

`C_n'(h)=-2 kappa_{n-1}(1-h^2)^((n-1)/2)`,

`C_n''(h)=2 kappa_{n-1}(n-1)h(1-h^2)^((n-3)/2)`.        (2)

Now put

`q_i(t)=|e^{tA}e_i|^2=<e_i,e^{2tA}e_i>`.

Then `h_i=s q_i^{-1/2}`. At zero,

`q_i(0)=1`,

`q_i'(0)=2A_ii`,

`q_i''(0)=4(A^2)_ii`.

Therefore

`h_i'(0)=-s A_ii`,        (3)

and, because

`(log h_i)''(0)=-2 sum_{j != i} A_ij^2`,

we obtain

`h_i''(0)=s [ A_ii^2 - 2 sum_{j != i} A_ij^2 ]`.        (4)

Differentiate (1). From (3) and `tr A=0`,

`F_A'(0)=-C_n'(s) sum_i h_i'(0)=s C_n'(s) tr A=0`.        (5)

For the second derivative, define

`D=sum_i A_ii^2`,

`O=sum_i sum_{j != i} A_ij^2`.

Equations (3)--(4) give

`sum_i (h_i'(0))^2=s^2 D`,

`sum_i h_i''(0)=s(D-2O)`.

Using (2),

`F_A''(0)
 = -C_n''(s)s^2D - C_n'(s)s(D-2O)`

`= -2 kappa_{n-1}s(1-s^2)^((n-3)/2)
   [ (n s^2-1)D + 2(1-s^2)O ]`.        (6)

Because `n>=2` and `s^2>1/2`, we have `n s^2-1>0`; also `1-s^2>0`. For a nonzero symmetric matrix, `D+O=||A||_F^2>0`, so (6) is strictly negative.

Now use global log-concavity. Equation (5) says the derivative of `log F_A` at zero is zero, hence log-concavity implies

`F_A(t) <= F_A(0)` for every real `t`.

If equality held for some `t_0 != 0`, concavity plus equality at both `0` and `t_0` would force `log F_A` to be constant on the intervening segment. That contradicts `(log F_A)''(0)=F_A''(0)/F_A(0)<0`. Thus

`F_A(t)<F_A(0)` for every `t != 0` whenever `A != 0`.

Every origin-centered ellipsoid of unit-ball volume can be written `e^A B_2^n` with `A` symmetric and `tr A=0` (positive-definite polar representative and matrix logarithm). Therefore `B_2^n` is the unique centered maximum-intersection ellipsoid. Scaling back gives the theorem. QED.

### Quantitative local defect

Since `F_A'(0)=0`, (6) also gives the explicit coercive bound

`-(log F_A)''(0) >= c_{n,s} ||A||_F^2`,

with

`c_{n,s}
 = [2 kappa_{n-1}s(1-s^2)^((n-3)/2) / F_A(0)]
   min{n s^2-1, 2(1-s^2)} > 0`.

This is a rigorous all-covariance-direction bound, not a finite sampling statement.

## 5. B12 — conserved quantity / stationarity

The conserved determinant is the right first-order quantity: `tr A=0`. In the cap-separated regime, the cube symmetry makes every coordinate cap carry the same first-variation weight, so the entire first variation collapses to a constant times `tr A` and vanishes exactly.

This is materially different from the preceding slack-coordinate example: there the flat direction survived because some constraints were inactive, but the body was not stationary against all determinant-one deformations. The cube **is** stationary, so it is a genuinely stronger counterexample candidate.

## 6. B15 — break the symmetry rather than only testing diagonal deformations

Keeping `A` fully symmetric rather than diagonal is decisive. Formula (6) splits the Hessian into

- a diagonal anisotropy term `(n s^2-1)D`, and
- an off-diagonal rotation/shear term `2(1-s^2)O`.

Both coefficients are strictly positive. Thus no hidden off-diagonal deformation creates a flat direction. The exact second variation rules out **every** nonzero symmetric trace-zero direction, not only coordinate scalings.

## 7. B30 — one boundary scale at a time: the disjoint-cap collar

The threshold `s>1/sqrt(2)` is not guessed from numerics. It is the exact geometric threshold at which two different coordinate face caps of the unit ball cannot overlap. Localizing to this one boundary scale converts the intersection into the additive cap formula (1), and the entire Hessian becomes explicit.

This suggests the next obstruction cleanly: below `s=1/sqrt(2)` pairwise cap intersections appear, so the missing ingredient is an exact inclusion-exclusion / curvature control for the overlap terms. In dimension three, pushing that calculation down to `s>1/sqrt(3)` would cover the entire cube's intermediate John--Loewner window.

## 8. Stronger counterexample-screening corollary: stationary boxes collapse to cubes

The same cap calculation eliminates a larger obvious counterexample family.

Let

`K_svec=product_i [-s_i,s_i]`

with every `s_i in (1/sqrt(2),1)`. If the unit ball is stationary for the volume-preserving **diagonal** ellipsoidal deformations, then all `s_i` are equal.

Indeed, for diagonal `A=diag(a_i)` with `sum a_i=0`, the exact first variation is

`F_A'(0)=sum_i a_i s_i C_n'(s_i)`.

Vanishing for every zero-sum vector `(a_i)` forces all weights `s_i C_n'(s_i)` to be equal. Up to the same negative constant these are

`g_n(s)=s(1-s^2)^((n-1)/2)`.

But

`g_n'(s)=(1-s^2)^((n-3)/2)(1-ns^2)<0`

throughout `(1/sqrt(2),1)` for every `n>=2`. Hence all `s_i` coincide.

So in the disjoint-cap regime the only axis-aligned product box that can even pass the source first-variation test is the cube; the theorem above then shows that this surviving symmetric candidate is strictly unique in the centered ellipsoid family.

## 9. What this does and does not prove

**Proved in this run:** an exact, theorem-sized all-dimensional uniqueness statement for the source's centered `rTB`, `T in SL_n`, family when the body is a cube and `a<r<sqrt(2)a`, together with an explicit Hessian gap and a rigidity statement for stationary boxes in the same cap-separated regime.

**Not proved:** uniqueness for every centrally symmetric body in dimension three; uniqueness for the full cube window `sqrt(2)a <= r < sqrt(n)a`; or a complete equality characterization for uniform-ball strong `(B)`.

I also do **not** silently upgrade centered-position uniqueness to a statement about possible translated equal-volume ellipsoids. The primary source reduces maximization for symmetric bodies to centered ellipsoids for the position problem, but a full translated-equality rigidity statement would need its own equality argument. The frozen universal metric therefore remains unchanged.

### Frozen metric

`D_MI: 2 -> 2` — **NO MOVEMENT**.

Status remains **PARTIAL / source OPEN**.

The result is nevertheless genuine route progress: the most symmetric stationary product-body candidate fails by a strict, computable curvature gap, and the first new geometric barrier is now precisely the pairwise-cap-overlap regime.

## 10. Scheduler/model capability statement

The native scheduler interface exposed to this worker still has **no model selector, no reasoning-effort selector, and no guaranteed run-duration field**. GPT-6 / maximum reasoning is therefore still prompt-requested only. This invocation actually identifies itself as GPT-5.6 Sol; reasoning metadata is not exposed and is reported as UNVERIFIED.

The repository policy records prior native modification probes for P26/P01/P03 returning `You cannot modify this task.` The authorized workaround is not a repository edit and not a duplicate automation: the task must be changed from an account/workspace context that owns the native job, or through platform support/authorized task ownership. This worker does not attempt to bypass that restriction and does not create or modify any other schedule.

## 11. Checkpoint for the next execution

If the frozen universal metric is still `D_MI=2` next run, that will be the third unchanged run on this target and Section I must trigger rather than another routine lemma.

The strongest next mathematical route is the **three-dimensional overlap layer**. Normalize a cube by `s in (1/sqrt(3),1/sqrt(2)]`, write the exact inclusion-exclusion formula for single caps and pairwise cap intersections, and determine the full trace-zero Hessian. A positive Hessian gap throughout that interval would settle centered uniqueness for the **entire cube intermediate window in `n=3`**; a sign change would produce a concrete stationary instability candidate.

Next B-triple if still on this target: **B6** (deform continuously from the solved disjoint-cap collar), **B18** (rewrite the overlap Hessian as spherical/covariance geometry), **B24** (identify the extremal contact/overlap pattern).

## ledger_delta

```yaml
track: HARD7-01
target: MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS
source_status: OPEN
research_status: PARTIAL
metric: D_MI
before: 2
after: 2
movement: none
unchanged_streak: 2
methods: [B12, B15, B30]
new_result: >-
  For every n>=2 and cube [-a,a]^n, the Euclidean ball of prescribed radius r
  is the unique centered maximum-intersection ellipsoid whenever a<r<sqrt(2)a;
  exact second variation and stationary-box rigidity proved on the page.
finite_sampling_used: false
exact_checker_required: false
closure_claimed: false
next_obligation: >-
  In n=3, control the pairwise-cap-overlap Hessian for
  1/sqrt(3)<a/r<=1/sqrt(2), or follow Section I if the universal metric remains unchanged.
```
