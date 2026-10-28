SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T06:30:13Z.
attacking: the uncovered two-sheet/near-coloop coarea interface; test whether the exact-rank-three residual projection may be replaced by a bounded three-dimensional joint density, and identify the first genuinely product-linear factor that a successful reciprocal-shear estimate must retain.

# account01/B05 QFORM r27 — a cap-one three-dimensional hidden-shear falsifier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound; uncovered indefinite two-sheet curved integral.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / REFUTED_INTERMEDIATE_MECHANISM / PRECISE_MISSING_FACTOR_IDENTIFIED`.  
**Full QFORM:** `OPEN_NOT_PROVED`.  
**Continuity:** `NOT_PROVED` for the full target.

## 1. Compact end-to-end question attacked first

The true-near-coloop exact-rank-three chamber can be written, after rotating only the deterministic spectral basis so that the hub cross arm points along the second spectral coordinate, in the schematic form

```
Q = q W^2 + 2 beta W Y + alpha Y^2 + 2 delta Y Z + gamma Z^2,
W = sqrt(c) X_0 + T,
```

where `X_0` is a genuine original coordinate, independent of the residual product block, while `(T,Y,Z)` are simultaneous linear projections of that residual product block.  In the exact-null model one may read the hard two-sheet geometry already from

```
Q = 2 B (sqrt(c) X_0 + T) Y + Z^2.                                (1.1)
```

A tempting extension of the exact-coloop theorem is to forget how `(T,Y,Z)` was generated and retain only:

1. `X_0` is independent of `(T,Y,Z)`;
2. `(T,Y,Z)` has a bounded three-dimensional density;
3. its one- and two-dimensional marginals are bounded;
4. the homogeneous coefficient matrix still has three singular/eigenvalue directions of target size.

This run proves that this entire replacement is false, even with all density caps equal to one and with a coefficient matrix already satisfying the three-large-eigenvalue spectral condition.  Hence the missing factor is not another projection-density cap: it is the **simultaneous linear-product provenance** of `T,Y,Z`, used inside the reciprocal-shear trace before any joint-density relaxation.

## 2. Main falsifier

Fix

```
c = 127/128,
B = c^(-1/2).
```

Let `X,Y,Z` be independent `Uniform[-1/2,1/2]`.  Let `U` be independent of them and uniform on

```
[-1/(2 sqrt(c)), 1/(2 sqrt(c))]
```

with density `sqrt(c) <= 1`.

For `Y != 0` define

```
T = sqrt(c) U - sqrt(c) Z^2/(2Y),                                  (2.1)
```

and define it arbitrarily on the null event `Y=0`.

### Lemma 2.1 — the residual triple has density cap one

The map

```
(u,y,z) -> (t,y,z)
```

in (2.1) has Jacobian determinant `sqrt(c)`.  Since the density of `(U,Y,Z)` equals `sqrt(c)` on its rectangular support, the joint density of `(T,Y,Z)` is exactly

```
g(t,y,z)
 = 1_{|y|<=1/2}
   1_{|z|<=1/2}
   1_{|t/sqrt(c) + z^2/(2y)| <= 1/(2sqrt(c))}                     (2.2)
```

for `y != 0`, up to a null set.  Therefore

```
boxed: ||g||_infinity = 1.                                         (2.3)
```

Moreover every coordinate and coordinate-pair marginal is also bounded by one.  Indeed, for fixed `(y,z)` the permitted `t`-interval has length one, so `p_(Y,Z)=1` on the unit square.  Integrating the indicator (2.2) in either `y` or `z` gives at most the length-one integration interval, hence

```
||p_(T,Y)||_infinity <= 1,
||p_(T,Z)||_infinity <= 1,
||p_T||_infinity <= 1.                                             (2.4)
```

Finally `X` is genuinely independent of the whole triple `(T,Y,Z)`.

Thus this model satisfies strictly more marginal-density information than any argument that keeps only generic one-, two-, and three-dimensional density caps.

## 3. The quadratic form has target-scale spectrum but unbounded output density

Consider

```
Q_c = 2 B (sqrt(c) X + T)Y + Z^2.                                  (3.1)
```

In the coordinate order `(X,T,Y,Z)`, the homogeneous symmetric matrix is

```
A_c = [[0,0,1,0],
       [0,0,c^(-1/2),0],
       [1,c^(-1/2),0,0],
       [0,0,0,1]].                                                  (3.2)
```

The three nonzero eigenvalues are exactly

```
1, +sqrt(1+c^(-1)), -sqrt(1+c^(-1)).                               (3.3)
```

Hence all three have absolute value at least one.  This is intentionally the same spectral scale as the QFORM target.  It is **not** a QFORM counterexample because `T,Y,Z` are not independent original coordinates and are not asserted to arise as simultaneous linear projections of a product law.

Substituting (2.1) into (3.1) cancels the curvature exactly:

```
Q_c
 = 2 c^(-1/2)
   [sqrt(c)X + sqrt(c)U - sqrt(c)Z^2/(2Y)]Y + Z^2
 = 2Y(X+U).                                                         (3.4)
```

Put `V=X+U`.  Since `X,U,Y` are independent, `V` is independent of `Y`.  The density `h_c` of `V` is the convolution of the unit interval density with the density `sqrt(c)` on an interval of length `1/sqrt(c)`.  For `|v|<=1/4`, the two defining intervals overlap in length at least `3/4`, so

```
h_c(v) >= (3/4)sqrt(c) > 1/2.                                     (3.5)
```

For a.e. nonzero `q`, the product coarea formula for `Q_c=2YV` gives

```
p_(Q_c)(q)
 = integral_R h_c(v)
     1_{|q/(2v)|<=1/2}
     dv/(2|v|).                                                     (3.6)
```

When `0<|q|<1/4`, restrict to positive `v in [|q|,1/4]`.  By (3.5),

```
p_(Q_c)(q)
 >= (1/4) integral_|q|^(1/4) dv/v
 =  (1/4) log(1/(4|q|)).                                           (3.7)
```

Therefore

```
boxed: ||p_(Q_c)||_infinity = infinity.                             (3.8)
```

This is a genuine essential-supremum divergence on every sufficiently small punctured neighborhood of zero, not a value assigned at a single point.

I record the correction as

`QFORM-SCALAR-PLUS-3D-JOINT-CAP-INSUFFICIENT-v1`:

> Even if a cap-one scalar is independent of a residual three-vector whose joint density and every coordinate/pair marginal density are all bounded by one, and even if the associated four-variable quadratic coefficient matrix has three eigenvalues of absolute value at least one, the quadratic pushforward need not have bounded density.  Therefore the true residual product projection `(T,Y,Z)` may not be replaced by an arbitrary bounded three-dimensional joint density.

## 4. Exact geometric reason: a reciprocal quadratic shear straightens the two-sheet curvature

The mechanism is transparent.  For the model (1.1), define the reciprocal-shear coordinate

```
U_* = T + Z^2/(2 B Y).                                              (4.1)
```

Then

```
Q = 2 B Y (sqrt(c)X_0 + U_*).                                      (4.2)
```

The counterexample chooses the residual law so that `U_*` is an independent interval variable.  The map

```
(t,y,z) <-> (u_*,y,z)
```

has unit Jacobian in the `t` direction, so a three-dimensional density cap does not see the nonlinear straightening at all.  Once straightened, (4.2) is merely a product and the usual logarithmic singularity reappears.

This pinpoints why generic two-sheet X-ray or bounded-projection-density arguments cannot close the problem.  A successful estimate must forbid the nonlinear relation

```
T approximately -Z^2/(2 B Y) + free interval variable              (4.3)
```

**using the fact that `T,Y,Z` are simultaneous linear forms of the same independent original coordinates.**  Neither `||p_(T,Y,Z)||_infinity`, the three coordinate-pair caps, nor independence of the hub scalar contains that information.

The exact unpaid object can therefore be stated without a fiber supremum:

`QFORM-PRODUCT-LINEAR-RECIPROCAL-SHEAR-CARLESON-v1`.

For simultaneous product-linear projections `(T,Y,Z)` with the Parseval/orthogonality relations of the exact-rank-three near-coloop normal form, prove a translation-uniform bound on

```
sup_q integral_R [1/(2|B y|)]
       p_(sqrt(c)X_0 + T + [Z^2 + lower-order YZ,Y^2 terms - q]/(2By), Y)
       (0,y) dy,                                                     (4.4)
```

or an equivalent interval formulation, **before** replacing the induced curved trace by a generic joint density.  The counterexample shows that (4.4) is false for arbitrary cap-one residual triples, so the proof must spend the product-linear origin itself.

## 5. Actual application of the designated account02/B05 result

The completed designated-partner theorem `QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1` is in

`yspennstate/math-open-problems@c661893c05a7fd40d7f1e9b0a0a81a6f08f242a6`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T035943Z-account02-B05-QFORM-r21/REPORT.md`,

and is retained in the partner's later exact-coloop closure.  It states, in particular, that when a cap-one scalar `X` is independent of a dependent pair `(C,D)` with joint density cap `M`, the sparse matrix

```
[[a,beta,0],[beta,alpha,delta],[0,delta,gamma]]
```

obeys

```
||p_Q||_infinity
 <= 31 M^(2/3)|beta^2 gamma det B|^(-1/6).                         (5.1)
```

Apply this to the **same physical control variables** `X,Y,Z` from Sections 2--3 but with the hidden residual coordinate removed:

```
Q_control = 2XY + Z^2.                                              (5.2)
```

Here `(Y,Z)` is in fact an independent uniform pair, so `M=1`, while

```
a=0, beta=1, alpha=delta=0, gamma=1, det B=-1.
```

Thus the partner theorem gives the concrete full-line estimate

```
boxed: ||p_(Q_control)||_infinity <= 31.                            (5.3)
```

This is an equation-level use of the assigned partner result.  Comparing (5.3) with (3.8) shows exactly what the third hidden coordinate can do if its actual product-linear provenance is discarded: it can perform the nonlinear reciprocal shear that cancels `Z^2` and resurrects the hyperbolic logarithm.

## 6. Actual application of the newest Claude source

The required newest package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`

proves Theorem C: for exact rank-three signature `(+,+,-)` with absolute eigenvalues at least one, the ruled one-sheet side satisfies

```
p_Q(s) <= pi sqrt(2),  s>=0.                                      (6.1)
```

The independent control (5.2) has spectrum `{1,1,-1}`.  Hence the source theorem applies directly and gives

```
boxed: p_(Q_control)(s) <= pi sqrt(2),  s>=0.                       (6.2)
```

The new falsifier therefore does not contradict the ruled theorem: it leaves the source's product-law hypothesis exactly at the point where the nonlinear hidden shear is introduced.  This is a useful source-matching check that the obstruction belongs specifically to the unresolved two-sheet/product-provenance interface.

## 7. Consequence for the current near-coloop campaign

Fresh neighboring work has already narrowed exact rank three to a true-near-coloop chamber with an order-one diffuse physical hub star; the exact-coloop endpoint is paid, and the one-sheet side is paid by Theorem C.  The calculation above rules out the most direct remaining relaxation:

```
true residual product projection
   -> bounded 3D joint density + bounded 2D marginals.
```

That replacement loses precisely the nonlinear-cancellation information needed on the minority/two-sheet side.  The next B05 mechanism should therefore work on the original residual coordinates or their characteristic-function factorization and prove a **curved reciprocal-shear trace estimate for simultaneous linear projections**, not for arbitrary `g(t,y,z)`.

A promising exact target is the zero-pivot kernel (4.4); the nonzero near-null pivot should then be treated by the partner's selector-preserving interpolation rather than a raw square/half-Riesz peel, which is already known to lose logarithmically.

## 8. Scope

- This report does **not** prove or disprove full QFORM.
- It does **not** assert that `(T,Y,Z)` in (2.1) is a product projection; it is deliberately a source-valid mechanism falsifier outside that premise.
- It keeps all target-law restrictions explicit and does not rotate random-coordinate independence.
- It proves a precise impossibility statement for a tempting coarea relaxation and identifies the factor that the next true estimate must retain.
- Continuity of the full target remains open.
