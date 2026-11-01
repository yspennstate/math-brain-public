# fleet01/B05 — endpoint coarea and a uniformly bounded balanced sector

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T192559Z-fleet01-B05-QFORM-r16`  
**Assignment:** Quadratic coarea bound  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / PRECISE_MISSING_FACTOR_IDENTIFIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction discipline

The target is the full product-law statement: independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and a real symmetric `A` with at least three eigenvalues of modulus at least one; prove a universal essential density bound for `X^T A X`, or give a valid counterexample. Continuity is a separate desired conclusion.

This report does **not** use the refuted arbitrary-joint rank-three coarea bound, any positive moment of conditional projection heights, pointwise van-der-Corput decay, or a fiberwise supremum. In particular, an arbitrary 3D density cap is not treated as sufficient for an indefinite quadratic pushforward. The purpose here is narrower: in the exact-rank-three heavy-isotropic state, keep one original independent coordinate until the coarea step, use the assigned partner's valid aggregate two-dimensional product-projection theorem, and identify exactly what part of the coarea integral is already uniformly paid.

## 2. Assigned partner theorem actually used

The assigned partner fleet02/B05 proved `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1` in

`yspennstate/math-open-problems@e74a5d8fabe1c914be1ca2d3689a2cd65ba58f5a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T155206Z-b05-qform-779c4c9b/REPORT.md`.

If independent cap-one coordinates are projected by a `2 x m` coefficient matrix `C` satisfying `C C^T=I_2`, the resulting two-dimensional density is at most `e`. The same proof supplies the normalized one-dimensional linear-form cap `sqrt(e)`. These statements preserve original-coordinate product provenance; no input rotation is asserted to preserve independence.

I apply the two-dimensional theorem below to the residual spectral pair before a determinant-one shear, and the one-dimensional theorem to the exact radial X-ray diagnostic.

## 3. Structural normal form for the heavy isotropic pivot

Let the exact nonzero spectral block be a real symmetric invertible `3 x 3` matrix `M` with all three eigenvalue magnitudes at least one. Let a physical row of the orthonormal spectral frame be

`u_i=sqrt(c) e`, with `c>1/2`, `||e||=1`, and `e^T M e=0`.

Choose an orthonormal basis `(e,f,g)` with `f` parallel to `M e`. In this basis

```
M = [ 0  B   0 ]
    [ B  r   s ]
    [ 0  s  tau]
```

where

`B=||M e||>=1`,

because the least singular value of `M` is at least one. Also

`det M=-B^2 tau`, hence `B^2 |tau|=|det M|>=1`.                 (3.1)

Writing the three spectral coordinates as `(E,Y,Z0)`, removal of the physical coordinate `i` gives

`E=sqrt(c) X_i+T`,

where the residual coefficient vectors of `T,Y,Z0` are mutually orthogonal, with squared norms `1-c,1,1` respectively. The original variable `X_i` is independent of all three residual linear forms.

Complete the square in the last two spectral coordinates. Put

`Z=Z0+(s/tau)Y`,

`gamma=(r-s^2/tau)/(2B)`,

`T'=T+gamma Y`,

and

`W=sqrt(c)X_i+T'`.

Then the quadratic form is exactly

`Q=2 B W Y + tau Z^2`.                                            (3.2)

The shear `(Y,Z0)->(Y,Z)` has determinant one. Therefore the partner theorem implies

`||p_(Y,Z)||_infinity <= e`.                                      (3.3)

No conditional density assertion is made.

## 4. A general endpoint L^p lemma for an original scalar pivot

### Theorem `QFORM-SCALAR-PIVOT-LP-ENDPOINT-v1`

Let `X` be independent of a residual sigma-field, with a probability density `f_X<=1`. Let `Y,R` be residual-measurable and suppose `Y` has a probability density bounded by `M`. For `a!=0`, set

`S=2aXY+R`.

Then for every `1<=p<infinity`,

`||p_S||_p <= p (M/|a|)^(1-1/p)`.                                (4.1)

### Proof

Put `alpha=1-1/p`. Conditional on the residual variables and on `Y=y!=0`, the density of `S` is a translate/dilate of `f_X`; hence

`||p_(S|res)||_p = (2|a y|)^(-alpha) ||f_X||_p <= (2|a y|)^(-alpha)`,

because `0<=f_X<=1` and `int f_X=1` imply `||f_X||_p<=1`. Minkowski gives

`||p_S||_p <= (2|a|)^(-alpha) E |Y|^(-alpha)`.                    (4.2)

For every probability density `g<=M`, the bathtub/rearrangement bound gives

`int |y|^(-alpha)g(y)dy
 <= M int_{-1/(2M)}^{1/(2M)} |y|^(-alpha)dy
 = 2^alpha M^alpha/(1-alpha)`.                                    (4.3)

Since `(1-alpha)^(-1)=p`, substituting (4.3) into (4.2) cancels the factor `2^alpha` and proves (4.1). The possible event `Y=0` has probability zero because `Y` has a density. QED.

### Application to (3.2)

Before the shear, `Y` is a normalized one-dimensional linear projection of independent residual coordinates. The one-dimensional part of the assigned partner theorem gives `M<=sqrt(e)`. In (3.2), regard

`S=2(B sqrt(c)) X_i Y + [2B T'Y+tau Z^2]`.

Thus, for every finite `p>=1`,

`||p_Q||_p <= p (sqrt(e)/(B sqrt(c)))^(1-1/p)
            <= sqrt(2e) p`.                                      (4.4)

This is not an `L^infinity` bound. It records the exact endpoint logarithmic loss left by a scalar hyperbolic pivot, while allowing completely arbitrary correlated leakage inside the bracketed residual term.

A useful corollary is an exponential tail for the **values of the density**. With `C0=sqrt(2e)`, Chebyshev and (4.4) give, for `u>=e C0`, choosing `p=u/(e C0)`,

`Leb{q: p_Q(q)>u} <= exp[-u/(e C0)]`.                              (4.5)

Thus any failure of a universal `L^infinity` bound in this state would have to occur on exponentially small output sets; (4.5) itself does not exclude such spikes.

## 5. A universal coarea kernel estimate in the residual plane

For `L>0`, define

`K_L(y,z)=1_{|z|<=L|y|}/|y|`.

### Lemma `QFORM-WEDGE-KERNEL-v1`

If `(Y,Z)` has a probability density bounded by `M`, then

`E K_L(Y,Z) <= 2 sqrt(2 M L)`.                                    (5.1)

### Proof

For `t>0`,

`{K_L>t}={|y|<1/t, |z|<=L|y|}`

has Lebesgue area

`int_{-1/t}^{1/t} 2L|y|dy = 2L/t^2`.

Therefore

`P(K_L>t)<=min(1,2ML/t^2)`.

Layer cake yields

`E K_L <= int_0^infinity min(1,2ML/t^2)dt=2sqrt(2ML)`. QED.

## 6. Uniform boundedness of the balanced heavy-isotropic sector

Define the balanced sector

`E_bal={|Z|<=B^2 c |Y|}`.                                         (6.1)

Let `mu_bal` be the subprobability law of `Q` restricted to `E_bal`, and let `p_bal` denote its density. Conditional on all residual variables, integrating the original coordinate `X_i` in (3.2) gives

`p_bal(q)
 <= [1/(2 B sqrt(c))]
    E[1_{E_bal}/|Y|]`.                                            (6.2)

Apply (5.1) with `M=e` from the partner theorem (3.3) and `L=B^2 c`. Then

`||p_bal||_infinity
 <= [1/(2B sqrt(c))] 2 sqrt(2e B^2 c)
 = sqrt(2e)`.                                                     (6.3)

This is a genuine, dimension-free pointwise density bound for a nontrivial part of the exact-rank-three heavy-isotropic coarea measure. It allows arbitrary fragmented input supports and arbitrary hidden linear leakage `T`; the only ingredients are one untouched original coordinate and the partner's aggregate pair theorem.

The complement is now geometrically rigid. On

`E_curv={|Z|>B^2 c |Y|}`,                                        (6.4)

(3.1) implies

`|tau Z| > |tau| B^2 c |Y| = |det M| c |Y| >= c |Y| > |Y|/2`.     (6.5)

Hence the only unpaid contribution is the **curvature-dominant sector** in which the `Z`-gradient is quantitatively larger than the hyperbolic `Y` scale. The former vague hidden-leakage obstruction is reduced to this precise sector.

## 7. Exact radial trace and why pair/X-ray bounds are one endpoint short

The preceding sector estimate can be recast in a form that exposes the remaining logarithm. Let `h(t,y,z)` be a joint density of `(T',Y,Z)`. Integrating `X_i` and then setting `z=ry` gives the exact nonnegative representation

`p_Q(q)=1/(2B sqrt(c))
        int_R int_R int_R
        h(t,y,ry)
        f_i( (q-2Bty-tau r^2 y^2)/(2B sqrt(c)y) )
        dt dy dr`,                                                (7.1)

with the null set `y=0` ignored. Equivalently, if `k(w,y,z)` is the joint density of `(W,Y,Z)`, then convolution in the untouched coordinate gives

`p_Q(q)=1/(2B)
        int_R int_R
        k((q-tau r^2 y^2)/(2By),y,ry)
        dy dr`.                                                   (7.2)

Formula (7.1), not a conditional supremum, is the correct product-provenance trace.

Write `kappa=s/tau`, so `Z=Z0+kappa Y`, where the residual coefficient vectors of `Y,Z0` are orthonormal. If in (7.1) one discards the translated factor `f_i` and retains only the pair marginal, then

`int h(t,y,ry)dt = p_(Y,Z)(y,ry)`.

Moreover

`int_R p_(Y,Z)(y,ry)dy
 = p_(Z-rY)(0)
 <= sqrt(e)/sqrt(1+(r-kappa)^2)`,                                 (7.3)

because `Z-rY=Z0+(kappa-r)Y` is a linear form whose coefficient-vector norm is `sqrt(1+(r-kappa)^2)`, and the normalized one-dimensional product projection has density at most `sqrt(e)` by the assigned partner theorem.

The right side of (7.3) has the exact nonintegrable endpoint tail `~1/|r|`. Thus pair-density or X-ray information alone loses a logarithm. This is consistent with the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` and hidden-leakage corrections; it does not refute the target.

The missing resource in (7.1) is now explicit: the translated original-coordinate factor must provide an **integrated radial gain** in the curvature-dominant region. Any source-valid estimate of the schematic form

`sup_q int_{|r-kappa|>R0} int int h(t,y,ry)
 f_i((q-2Bty-tau r^2y^2)/(2B sqrt(c)y)) dt dy dr <= C`            (7.4)

would close the heavy-isotropic state together with (6.3). It is enough, for example, to gain any integrable improvement over the endpoint X-ray tail, such as an averaged `O(|r|^{-1-epsilon})` bound; pointwise decay is not required.

## 8. Conditional end-to-end argument and first unpaid implication

Within the exact-rank-three heavy-isotropic branch, the argument is now:

1. Put the form in the exact normal form (3.2), with `B>=1`, `B^2|tau|>=1`, and preserve the original scalar `X_i`.
2. Apply fleet02/B05 `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1` to obtain (3.3).
3. Split the coarea trace by (6.1)/(6.4).
4. The balanced sector has universal density at most `sqrt(2e)` by (6.3).
5. The complement automatically satisfies the curvature dominance (6.5).
6. Therefore a uniform translated radial estimate (7.4) for the curvature-dominant sector would finish this heavy-isotropic branch without any conditional density supremum or reciprocal selected minor.

The first essential missing implication is therefore

`QFORM-HEAVY-ISOTROPIC-CURVATURE-TAIL-v1`:

> In the exact product-projection geometry above, exploit the simultaneous original-coordinate linear provenance of `(T,Y,Z0)` and the retained translated factor `f_i` to make the radial trace in (7.1) integrable on `|Z|>B^2 c|Y|`.

The exact missing factor is **one integrable radial gain beyond the universal `1/|r|` X-ray tail**. The balanced sector, all finite `L^p` norms, and the location of the endpoint loss are now paid quantitatively.

This supporting result does not prove the unrestricted exact-rank-three theorem, does not address arbitrary additional spectral directions, and does not prove continuity. Full QFORM remains open.

## 9. Source ledger

- Fresh controlling repository: `yspennstate/math-research-brain`, programme `QFORM-DENSITY-3EIG-20260922`; the owner control advanced during the run and was refreshed before publication.
- Assigned partner actually applied: fleet02/B05 `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1`, canonical commit `e74a5d8fabe1c914be1ca2d3689a2cd65ba58f5a`.
- Live corrections consumed: arbitrary-joint rank-three coarea false; positive conditional projection-height moments false; pointwise phase decay false; fiber-sup dimension loss; X-ray-only curved trace false; bounded pair density alone insufficient under arbitrary hidden leakage.
- No scheduler, notification, email, Drive, public-release, paid-model/API, remote-workflow, permission, or installation mutation was used.
