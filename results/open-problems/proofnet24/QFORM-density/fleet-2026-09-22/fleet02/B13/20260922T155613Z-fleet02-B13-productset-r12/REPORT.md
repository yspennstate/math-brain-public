# fleet02/B13 — no operator-norm slab continuity at the four-direction collar

**Run:** `20260922T155613Z-fleet02-B13-productset-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Extremal product laws  
**Classification:** `PROVED MECHANISM COUNTEREXAMPLE / SUPPORTING STRUCTURAL NECESSITY / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full quadratic-form conjecture remains **OPEN / NOT PROVED**.

## 1. First unpaid implication attacked

The fresh designated partner result is fleet03/B13

`yspennstate/math-open-problems@6fd070b11f649461fc4e25163e6289d7585232b6`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/fleet03-B13-20260922T153142Z-r11/REPORT.md`.

It proves that, in the exact-rank-three nested-heavy obstruction away from leverage one, any sequence with unbounded density must approach an exact four-projective-direction frame: three physical rows capture asymptotically all planar spectral mass and the remaining transverse mass is diffuse. Its first unpaid implication is a dimension-free **four-direction stability collar** for arbitrary cap-one product laws.

This run tests the most direct stability mechanism early: compare the slab kernel of the nearly four-direction matrix to the slab kernel of its exact four-direction endpoint using only small operator/frame perturbation. The theorem below gives a genuine target-normalized product-indicator counterexample to that mechanism, even when every one-dimensional support is a single interval. Therefore the collar cannot be proved by a support-free `o(1)` continuity estimate in the matrix coefficients. Any successful collar theorem must instead be affine-uniform/nonperturbative and retain product provenance.

The exact bang-bang reduction from this slot remains available at

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`:
for every slab kernel, the supremum over independent densities `0<=f_i<=1`, `int f_i=1`, equals the supremum over unit-measure product indicators. Hence a product-indicator obstruction is the correct extremal class; no interval extremality is assumed by the reduction.

## 2. Exact four-direction endpoint

Let

```
R0 = (1/2) * [
  [ 1,  1,  1],
  [ 1, -1, -1],
  [-1,  1, -1],
  [-1, -1,  1]
]
```

and `Lambda=diag(1,1,-1)`. Then `R0^T R0=I_3`. Embed this in five physical coordinates by appending a zero fifth row, and define

`A0 = R Lambda R^T`,  `R=[R0;0]`.

Thus `A0` has spectrum `{1,1,-1,0,0}` and its nonzero spectral-frame rows occupy exactly four projective directions. Explicitly its active `4 x 4` block is

```
(1/4) * [
 [ 1,  1,  1, -3],
 [ 1,  1, -3,  1],
 [ 1, -3,  1,  1],
 [-3,  1,  1,  1]
].
```

Put

`w=(e1+e2)/sqrt(2)`.

A direct calculation gives

`w^T A0 w = 1/2`.                                           (2.1)

For `0<theta<1`, let `O_theta` be the orthogonal rotation in `span{w,e5}` defined by

`O_theta w = cos(theta) w + sin(theta) e5`,

`O_theta e5 = -sin(theta) w + cos(theta) e5`,

and fixing the orthogonal complement. Define

`A_theta = O_theta A0 O_theta^T`.                             (2.2)

Then every `A_theta` has exactly the same spectrum `{1,1,-1,0,0}`, so it is a genuine target-normalized rank-three matrix. Moreover

`||A_theta-A0||_op <= 2 ||O_theta-I||_op ||A0||_op`
`                     = 4 sin(theta/2) <= 2 theta`.          (2.3)

For `theta>0` the fifth physical spectral-frame row is

`sin(theta) w^T R0`,

so (2.2) is literally a small extra physical row-direction leakage from the four-direction endpoint.

## 3. The counterexample to uniform slab-kernel continuity

Fix `L=11`. For each `theta`, take the five unit-measure interval supports

`E_1=E_2=E_3=E_4=[0,1]`,

`E_5(theta)=[L/sin(theta), L/sin(theta)+1]`,                 (3.1)

and let `E(theta)=prod_i E_i(theta)`.

### Theorem 3.1 — `QFORM-NO-OPNORM-SLAB-CONTINUITY-v1`

There is no modulus `omega(delta)->0` such that for every pair of target-normalized symmetric matrices `A,B`, every unit-measure product set `E`, and every unit interval `J`,

`| |{x in E: x^T A x in J}| - |{x in E: x^T B x in J}| |`
`    <= omega(||A-B||_op).`                                  (3.2)

Indeed, the explicit `A_theta,A0,E(theta)` above satisfy `||A_theta-A0||_op->0`, while for every sufficiently small `theta` there is a unit interval `J_theta subset [6,115]` such that

`|{x in E(theta): x^T A_theta x in J_theta}| >= 1/109`,      (3.3)

but

`|{x in E(theta): x^T A0 x in J_theta}| = 0`.               (3.4)

Moreover, along a sequence `theta_n->0`, one may pass to a subsequence for which the **same fixed integer unit interval** `J_*` works in (3.3)-(3.4).

### Proof

Write any `x in E(theta)` as

`x = (L/sin(theta)) e5 + u`,  with `u in [0,1]^5`.

By the definition of `O_theta`,

`O_theta^T e5 = sin(theta) w + cos(theta) e5`.

The vector `e5` lies in the kernel of `A0`. Hence, with `v=O_theta^T u`,

`x^T A_theta x`
` = (L w + v)^T A0 (L w + v)`
` = L^2/2 + 2L w^T A0 v + v^T A0 v`,                       (3.5)

using (2.1). Since `||A0||_op=1`, `||w||=1`, and `||v||=||u||<=sqrt(5)`,

`|x^T A_theta x - L^2/2| <= 2L sqrt(5)+5`.                 (3.6)

For `L=11`,

`L^2/2-(2L sqrt(5)+5) > 6`,

`L^2/2+(2L sqrt(5)+5) < 115`.

Thus the entire unit-volume set `E(theta)` maps into `[6,115]`. Partition `[6,115]` into its 109 integer unit intervals. One of them, call it `J_theta`, must carry at least `1/109` of the volume, proving (3.3).

For `A0`, the fifth coordinate is completely absent. For `x in E(theta)`, its first four coordinates lie in `[0,1]^4`, and therefore

`|x^T A0 x| <= ||A0||_op ||(x_1,...,x_4)||_2^2 <= 4`.      (3.7)

Every `J_theta subset [6,115]` is disjoint from this range, proving (3.4).

Finally there are only 109 possible integer unit intervals. For any sequence `theta_n->0`, infinite pigeonhole gives a subsequence on which one fixed `J_*` is selected infinitely often. Equations (2.3), (3.3), and (3.4) contradict any modulus in (3.2). QED.

## 4. Why this does not refute QFORM

This is a counterexample to a **mechanism**, not to the target theorem. Each `A_theta` has only five physical rows and hence at most five projective row directions. The completed finite-direction theorem from this slot,

`yspennstate/math-open-problems@8a21bd3d25ce1622121616ce789589e1e073f68d`,

proves for exact rank three with at most `m` projective directions

`||p_Q||_infinity <= 2(2pi+3sqrt(3)) binom(m,3)`.

Therefore every matrix in the counterexample family is in fact uniformly paid by

`||p_{Q_theta}||_infinity`
` <= 20(2pi+3sqrt(3))`
` = 229.5867545977...`.                                     (4.1)

The product supports (3.1) are single intervals; no fragmentation is needed. What diverges is their **translation**, which is allowed by the owner's hypotheses.

## 5. Exact affine lesson for the partner's stability collar

Translation is the obstruction. For any vector `m` and product variable `u`,

`(m+u)^T A (m+u)`
` = u^T A u + 2(Am)^T u + m^T A m`.                         (5.1)

Thus a matrix leakage of size `epsilon` cannot be treated as a uniformly small phase/sublevel perturbation when an admissible support may sit at distance `epsilon^{-1}` or larger. In (3.1), the fifth-coordinate translation is `asymp 1/theta`, exactly compensating the `sin(theta)` spectral leakage.

Consequently the partner implication

`QFORM-RANK3-FOUR-DIRECTION-STABILITY-COLLAR-v1`

must be formulated and proved **uniformly in arbitrary induced affine terms** (or by an equivalent translation-free product argument). Raw operator-norm closeness, small row angle, small coefficient leakage, and endpoint slab-kernel comparison are insufficient by themselves.

This also identifies why the finite-direction theorem is the correct endpoint interface: its proof conditions outside independent aggregate banks and invokes the three-variable affine quadratic theorem **uniformly in the resulting linear term**. The missing collar step is therefore not continuity of the quadratic kernel. It is an affine-uniform aggregation theorem that tolerates many slightly misaligned rows while keeping the original-coordinate product structure.

## 6. Product-indicator interpretation and the exact remaining debt

By the exact fleet02/B13 bang-bang theorem at `604a080...`, every universal small-ball proof may work on arbitrary unit-measure product indicator sets with zero constant loss. The present construction shows that even restricting those indicators to connected intervals does not justify perturbative comparison with a nearby endpoint matrix.

The first unpaid implication after this run is therefore sharper:

`QFORM-RANK3-AFFINE-UNIFORM-FOUR-BANK-COLLAR-v1` — in the partner's rank-three four-direction collar, aggregate the diffuse transverse bank and the three planar-heavy physical directions in a way whose density/slab estimate is uniform under arbitrary linear terms generated by remote product supports, without rotating the independent inputs or imposing support/moment bounds.

A valid proof of that implication, combined with the partner profile-overlap forcing and the already-paid exact four-direction endpoint, would close the non-leverage-one nested-heavy exact-rank-three terminal branch. Leverage-one and arbitrary additional spectrum remain separate full-target debts.

## 7. Source status

Fresh controls and the correction inbox were reread before publication at brain `main` commit `9f6b5b5888a78296b602605434a363864cf6f5ac`; no later stop or correction invalidating the argument was present in that snapshot. This report uses no pointwise oscillatory-decay claim, no fiber-supremum bound, no conditional-density substitute for independence, no single-minor dichotomy, no bounded-diameter localization, and no fixed-fragment-count reduction.

The result is analytic. A deterministic checker accompanying this report verifies the exact Parseval/frame algebra and the stated numerical support bounds; it is corroborative only.
