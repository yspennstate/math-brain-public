SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B18, 2026-09-22T18:25:00Z.

# fleet04/B18 — sharp rearrangement transfer into the zero-pivot trace theorem

**Run:** `20260922T182500Z-fleet04-B18-QFORM-r2`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Classification:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / ESSENTIAL_STEP_APPLIED`  
**Full target:** `OPEN / NOT PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Result

This report transfers the sharp one-dimensional maximum-density theorem of
Juškevičius--Lee (the sharp Rogozin rearrangement theorem) into the completed
fleet01/B18 zero-pivot nonlinear estimate.  It gives a distribution-free,
continuous-density bound for a genuinely rotated indefinite target family.

Let `X_0,X_1,...,X_6` be independent real random variables, each with a
probability density bounded by one.  Put

```
U=(X_1+X_2+X_3)/sqrt(3),
V=(X_4+X_5+X_6)/sqrt(3),
Q=2X_0U+2X_0V+2UV.
```

Then `Q` has a continuous density and

```
||p_Q||_infinity <= 27/4 = 6.75.                 (1.1)
```

The physical-coordinate matrix is `A=W H W^T`, where the columns of `W` are
the three disjoint unit vectors defining `X_0,U,V`, and

```
H=[[0,1,1],[1,0,1],[1,1,0]].
```

Thus the nonzero eigenvalues of `A` are exactly `2,-1,-1`.  The family is
indefinite, rank three, target-normalized, and rotated across six original
coordinates.  All physical diagonal coefficients are zero, so this is not the
three-large-diagonal control case.

## 2. Primary source and exact hypothesis audit

Primary source: T. Juškevičius and J. D. Lee, *Small ball probabilities,
maximum density and rearrangements*, arXiv:1503.09190 (2015).

Its one-dimensional sharp maximum-density consequence says that if independent
real variables `Z_j` have densities bounded by `K_j`, then the essential
supremum of the density of their sum is no larger than that obtained by
replacing the summands with centered uniform variables having density caps
`K_j`.  Applied to `u_j X_j`, the cap is `1/|u_j|`, so for a coefficient bank
`u` the bound is

```
R(u)=|| *_{j:u_j!=0} |u_j|^(-1) 1_{[-|u_j|/2,|u_j|/2]} ||_infinity.   (2.1)
```

There are no moment, centering, compact-support, log-concavity, identical-law,
or connected-support hypotheses on the original inputs.  This is an integrated
rearrangement statement, not pointwise oscillatory decay.

For the flat three-coordinate bank `u=(1,1,1)/sqrt(3)`, let
`S=Z_1+Z_2+Z_3` for independent `Unif[-1/2,1/2]` variables.  The density at
zero is the area in the unit square cut out by `|z_1+z_2|<=1/2`, namely
`1-2(1/2)(1/2)^2=3/4`.  The convolution is symmetric unimodal, hence its
maximum is `3/4`.  Scaling by `1/sqrt(3)` gives

```
R(u)=3sqrt(3)/4.                                  (2.2)
```

The blocks defining `U` and `V` are disjoint.  Therefore `U,V` are genuinely
independent in the original product coordinates, and their joint density is
the product of their marginal densities.  Equations (2.1)--(2.2) give

```
||p_(U,V)||_infinity <= (3sqrt(3)/4)^2=27/16.     (2.3)
```

For comparison, the general two-dimensional marginal theorem of
Livshyts--Paouris--Pivovarov, arXiv:1507.07949, would give only the cap `2`.
The sharp product-bank rearrangement therefore retains useful structure that a
generic projection cap discards.

## 3. Application of the completed partner result

The designated completed partner result is fleet01/B18
`QFORM-ZEROPIVOT-1PLUS2-DENSITY-v1`, scientific commit
`dd94932dae1791af1bca9396c062e17d0e55142a`.  It states:

> If a cap-one scalar `X` is independent of a two-dimensional vector `Y`
> having arbitrary joint density cap `M`, and
> `K=[[0,ell^T],[ell,B]]` is a nonsingular real symmetric `3x3` matrix, then
> `(X,Y)^T K (X,Y)` has a continuous density satisfying
> `||p||_infinity <= 6 M^(2/3)|det K|^(-1/3)`.

This result does not assume that the coordinates of `Y` are independent.  It
uses genuine scalar-versus-vector independence, an affine integration away
from the zero-coupling fiber, and an integrable square-Jacobian estimate near
that fiber.

Apply it with `X=X_0`, `Y=(U,V)`, `K=H`, and `M=27/16` from (2.3).  The matrix
`H` is nonsingular, has the required zero pivot, and

```
det H=2.
```

Therefore

```
||p_Q||_infinity
 <= 6(27/16)^(2/3) 2^(-1/3)
 = 6 [9/2^(8/3)] 2^(-1/3)
 = 54/8
 = 27/4.                                           (3.1)
```

Continuity follows directly from the partner theorem.  This proves (1.1).

The same splice gives the general banked zero-pivot inequality.  Let `X` be a
cap-one scalar and let `U=<u,X_I>`, `V=<v,X_J>` be normalized linear banks on
disjoint original-coordinate sets, also disjoint from `X`.  For every
nonsingular symmetric zero-pivot matrix `K`,

```
||p_((X,U,V)^T K (X,U,V))||_infinity
 <= 6 [R(u)R(v)]^(2/3)|det K|^(-1/3),              (3.2)
```

and the density is continuous.  Formula (3.2) is the actual inequality in
which the literature theorem is used; it is not a standalone projection
claim.

## 4. Quantifier and correction audit

- The seven original coordinates are independent and have arbitrary densities
  between zero and one.  No moment or support assumption is made.
- Independence is never asserted after a general rotation.  It is retained
  only because the two displayed banks use disjoint original-coordinate
  blocks.
- The nonlinear step is supplied by the partner theorem.  A bounded joint
  projection density is not treated as sufficient by itself.
- No pointwise van-der-Corput/Fresnel decay, fiber-supremum integration,
  Gaussian comparison, interval extremality for the quadratic event, or
  Monte Carlo evidence is used.
- Repeated eigenvalues `-1,-1` are harmless: the Hessian is nonsingular and
  `det H=2`.

## 5. Scope and remaining implication

This closes a concrete rotated, indefinite, exact-rank-three family and proves
the general disjoint-two-bank inequality (3.2).  It does not close the full
theorem.  In particular, the fleet01/B18/fleet02/B18 zero-pivot case 3
still has a genuine three-dimensional product projection in the
Schur-isotropic configuration; a two-bank factorization need not exist there.
General matrices with extra spectrum also require the product-preserving
structural extraction in the collective argument.

The first unpaid implication for this literature route is therefore:

`QFORM-ZEROPIVOT-CASE3-SHARP-PRODUCT-TRACE-v1`: exploit the actual
three-dimensional product-projection provenance in the Schur-isotropic case,
rather than replacing it by an arbitrary bounded joint density.

The full bounded-density conjecture remains open.  Continuity is proved for the
new branch, not for the full target.  No claim of external novelty is made.

## 6. Source pins

- Juškevičius--Lee primary source: https://arxiv.org/abs/1503.09190
- Livshyts--Paouris--Pivovarov primary source:
  https://arxiv.org/abs/1507.07949
- Partner report: `yspennstate/math-open-problems@dd94932dae1791af1bca9396c062e17d0e55142a`,
  `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260922T175509Z-qform-B18-a01-r15/REPORT.md`.
- Fresh owner control observed at run start:
  `yspennstate/math-research-brain@f3d6df2bd8d4f570cad5861e8de863f80fa0ff0a`,
  revision `2026-09-22.11`.

Repository synchronization is not native learned-memory ingestion; status is
`WITHOUT_VERIFIED_BRAIN`.
