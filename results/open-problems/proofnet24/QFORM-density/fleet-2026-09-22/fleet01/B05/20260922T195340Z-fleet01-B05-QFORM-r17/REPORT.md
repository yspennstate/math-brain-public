# fleet01/B05 — zero-level curvature tail is uniformly paid

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T195340Z-fleet01-B05-QFORM-r17`  
**Assignment:** Quadratic coarea bound  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / PRECISE_MISSING_FACTOR_IDENTIFIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope

The full target remains open: independent real coordinates with densities at most one; real symmetric `A` with at least three eigenvalues of modulus at least one; prove a universal essential density bound for `X^T A X`, or give a valid counterexample. Continuity is separate and is not proved here.

This report works only in the exact-rank-three heavy-isotropic branch isolated in the preceding fleet01/B05 run. It proves a uniform bound at the cone vertex `q=0`, including the entire curvature-dominant radial tail. This does **not** imply a uniform bound for arbitrary output levels `q`.

The proof preserves an original independent coordinate. It does not use the false arbitrary-joint rank-three coarea lemma, any positive conditional-projection-height moment, a conditional density supremum, or pointwise van-der-Corput decay.

## 2. Structural normal form and an inverse-matrix identity

Use the preceding heavy-isotropic normal form. The exact nonzero spectral block is a symmetric invertible `3 x 3` matrix `M` with every eigenvalue magnitude at least one. A physical row of the spectral frame is

`u_i=sqrt(c)e`, with `1/2<c<=1`, `||e||=1`, and `e^T M e=0`.

Choose an orthonormal basis `(e,f,g)` with `f` parallel to `Me`. Then

```
M = [ 0  B   0 ]
    [ B  r   s ]
    [ 0  s  tau]
```

with `B=||Me||>=1`. Put

`kappa=s/tau`,

`gamma=(r-s^2/tau)/(2B)`.

The residual original-coordinate linear forms `T,Y,Z0` have mutually orthogonal coefficient vectors with squared norms `1-c,1,1`. Define

`T'=T+gamma Y`, `Z=Z0+kappa Y`, `W=sqrt(c)X_i+T'`.

Then

`Q=2 B W Y + tau Z^2`.                                             (2.1)

The determinant identity is `det M=-B^2 tau`.

A useful exact identity, not used in the preceding run, comes from writing the inverse explicitly:

```
M^{-1} = [ -2gamma/B   1/B   -kappa/B ]
         [  1/B        0       0       ]
         [ -kappa/B    0       1/tau   ].
```

Since every eigenvalue of `M` has modulus at least one, `||M^{-1}||op<=1`. Hence

`|tau|>=1`,                                                        (2.2)

and the first-row Euclidean norm gives

`4 gamma^2 + kappa^2 + 1 <= B^2`.                                 (2.3)

In particular `|gamma|<=B/2` and `|kappa|<=B`. These inequalities are exact consequences of the target spectral hypothesis; no moment or support assumption is involved.

## 3. Partner theorem and its scaled form

Assigned partner fleet02/B05 proved `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1` in

`yspennstate/math-open-problems@e74a5d8fabe1c914be1ca2d3689a2cd65ba58f5a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T155206Z-b05-qform-779c4c9b/REPORT.md`.

If a two-dimensional linear image of independent cap-one coordinates has coefficient Gram matrix `I_2`, its density is at most `e`. Therefore, by normalizing an arbitrary full-rank coefficient matrix `C`, the following scaled form is immediate:

> If `G=C C^T` is positive definite and `V=C X`, then
> `||p_V||infinity <= e / sqrt(det G)`.                             (3.1)

Indeed `G^{-1/2}C` is Parseval and the linear change of variables contributes exactly `det(G)^(-1/2)`.

The same partner report gives the normalized one-dimensional projection cap `sqrt(e)`.

## 4. Radial coarea formula

Let `h(t,y,z)` be a joint density of `(T',Y,Z)`. Integrating the untouched original coordinate `X_i` and writing `z=rho y` gives

`p_Q(q)=1/(2B sqrt(c)) * integral_R I_rho(q) d rho`,                (4.1)

where

`I_rho(q)=integral integral h(t,y,rho y)
  f_i((q-2Bty-tau rho^2 y^2)/(2B sqrt(c)y)) dt dy`.                (4.2)

The null set `y=0` is irrelevant.

The preceding run already proved that the balanced sector

`|Z|<=B^2 c |Y|`

has density at most `sqrt(2e)` at every output level. Thus the curvature sector corresponds to

`|rho|>R`, `R=B^2 c`.                                               (4.3)

The new issue is whether the radial tail can be paid without losing the logarithm from the crude X-ray bound.

## 5. Moderate curvature radii are uniformly paid at q=0

First restrict to

`R<|rho|<=4B`.                                                      (5.1)

At `q=0`, simply discard `f_i<=1` in (4.2). Then

`I_rho(0)<=integral p_(Y,Z)(y,rho y) dy
          =p_(Z-rho Y)(0)`.

Since `Z-rho Y=Z0+(kappa-rho)Y`, its coefficient-vector norm is

`sqrt(1+(kappa-rho)^2)`.

The one-dimensional part of the assigned partner theorem therefore gives

`I_rho(0)<=sqrt(e)/sqrt(1+(kappa-rho)^2)<=sqrt(e)`.                (5.2)

The set (5.1) has total length at most `8B`. Consequently its contribution to `p_Q(0)` is at most

`[1/(2B sqrt(c))] 8B sqrt(e)
 <=4 sqrt(2e)`.                                                     (5.3)

No localization of the input supports is used.

## 6. Far curvature radii acquire a full extra radial power at q=0

Now assume

`|rho|>4B`.                                                        (6.1)

Put

`alpha=tau/(2B)`,

`S_rho=T'+alpha rho^2 Y=T+(gamma+alpha rho^2)Y`,

`L_rho=Z-rho Y=Z0+(kappa-rho)Y`.                                  (6.2)

Because the coefficient vectors of `T,Y,Z0` are mutually orthogonal with squared norms `1-c,1,1`, the coefficient Gram determinant of `(S_rho,L_rho)` is exactly

`D(rho)
 =[(1-c)+(gamma+alpha rho^2)^2][1+(kappa-rho)^2]
  -[(gamma+alpha rho^2)(kappa-rho)]^2
 =(1-c)[1+(kappa-rho)^2]+(gamma+alpha rho^2)^2`.                   (6.3)

In particular

`sqrt(D(rho))>=|gamma+alpha rho^2|`.                               (6.4)

By (2.2), `|alpha|>=1/(2B)`, while (2.3) gives `|gamma|<=B/2`. Hence for `|rho|>4B`,

`|gamma+alpha rho^2|
 >=rho^2/(2B)-B/2
 >=rho^2/(4B)`.                                                     (6.5)

Apply the scaled partner theorem (3.1):

`||p_(S_rho,L_rho)||infinity
 <=e/sqrt(D(rho))
 <=4eB/rho^2`.                                                      (6.6)

At the special output level `q=0`, the translated cap-one factor becomes linear in `S_rho`. Indeed (4.2) gives

`I_rho(0)
 =integral integral h(t,y,rho y)
   f_i(-(t+alpha rho^2 y)/sqrt(c)) dt dy`.

Set `s=t+alpha rho^2 y`. Since `(s,0)` are the values of `(S_rho,L_rho)` on the radial slice,

`I_rho(0)
 =integral f_i(-s/sqrt(c)) p_(S_rho,L_rho)(s,0) ds`.

Therefore, using `int f_i(-s/sqrt(c)) ds=sqrt(c)`,

`I_rho(0)
 <=sqrt(c) ||p_(S_rho,L_rho)||infinity
 <=4eB sqrt(c)/rho^2`.                                             (6.7)

Substitute into (4.1). The far-tail contribution is at most

`1/(2B sqrt(c)) * integral_(|rho|>4B) 4eB sqrt(c)/rho^2 d rho
 =2e integral_(|rho|>4B) rho^(-2) d rho
 =e/B
 <=e`.                                                            (6.8)

This is the missing radial power: the crude X-ray estimate is `O(1/|rho|)`, while the retained original-coordinate factor plus the partner two-dimensional projection theorem produces `O(1/rho^2)` at the cone vertex.

## 7. New theorem

### `QFORM-HEAVY-ISOTROPIC-ZERO-LEVEL-CURVATURE-v1`

In the exact-rank-three heavy-isotropic normal form (2.1), under the full target assumptions on the independent input densities,

`p_curv(0) <= e + 4 sqrt(2e) < 12.045`,                            (7.1)

where `p_curv` is the subdensity from `|Z|>B^2 c|Y|`.

Combining with the preceding balanced-sector estimate `p_bal(q)<=sqrt(2e)` yields

`boxed( p_Q(0) <= e + 5 sqrt(2e) < 14.377 ).`                      (7.2)

Thus the cone vertex itself is uniformly controlled in this formerly unpaid heavy-isotropic branch, for arbitrary fragmented cap-one input laws.

This is a pointwise statement at `q=0`; it is not a full `L^infinity` theorem.

## 8. Exact translation-uniform debt

The proof above exposes why `q=0` is special. For general `q`, after the same substitution `s=t+alpha rho^2y`, the retained scalar factor is

`f_i((q/(2B y)-s)/sqrt(c))`.                                      (8.1)

Equivalently, after substituting the original coordinate `x`, the far-radial trace requires control of the nonlinear curve

`t = q/(2B y) - sqrt(c)x - alpha rho^2 y`,
`z = rho y`.                                                       (8.2)

At `q=0`, (8.2) is an affine line and the assigned partner's two-dimensional projection cap applies exactly. At `q!=0`, the reciprocal term `q/y` turns it into a hyperbola. An arbitrary fiber supremum is forbidden by the live corrections, and discarding the translated factor falls back to the nonintegrable `1/|rho|` X-ray tail.

Therefore the first unpaid implication is now sharply

`QFORM-TRANSLATION-UNIFORM-HYPERBOLIC-CURVE-TRACE-v1`:

> For simultaneous original-product linear projections `(T,Y,Z0)` with orthogonal coefficient vectors as above, prove a dimension-free bound on the integrated traces of the hyperbolas (8.2), strong enough to retain the `rho^{-2}` (or any integrable) radial gain uniformly in `q`.

A successful result here, combined with the already-paid balanced sector, would close the exact-rank-three heavy-isotropic branch. The remaining full-matrix problem would still require handling additional spectral directions.

The exact missing factor is no longer the cone-vertex singularity: that is paid by (7.2). It is **translation-uniform control of the curved `q/y` trace while retaining product provenance**.

## 9. Conditional end-to-end map

Within this branch:

1. heavy isotropic pivot -> exact normal form (2.1);
2. partner 2D Parseval projection theorem -> balanced sector bounded by `sqrt(2e)`;
3. this run -> all curvature contribution at `q=0` bounded by `e+4sqrt(2e)`;
4. if `QFORM-TRANSLATION-UNIFORM-HYPERBOLIC-CURVE-TRACE-v1` is proved, then the curvature sector is uniformly bounded for every `q` and the branch closes.

Full QFORM remains `OPEN_NOT_PROVED`. Continuity remains `NOT_PROVED`.

## 10. Source ledger

- Previous B05 normal-form/coarea report: `yspennstate/math-open-problems@ff4ac4c0e30ef241b9347aa764965e8f7842450d`, exact path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B05/20260922T192559Z-fleet01-B05-QFORM-r16/REPORT.md`.
- Assigned partner actually applied: fleet02/B05, `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1`, `yspennstate/math-open-problems@e74a5d8fabe1c914be1ca2d3689a2cd65ba58f5a`, exact report path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T155206Z-b05-qform-779c4c9b/REPORT.md`.
- Relevant corrections retained: arbitrary-joint rank-three coarea false; conditional projection-height positive moments false; scalar-remainder conditional sup false; pointwise phase decay false; X-ray-only curved trace false; hidden-shift pair-cap sufficiency false.

No scheduler, notification, email, Drive, public release, paid model/API, remote workflow, permission, or installation mutation is made by this report.
