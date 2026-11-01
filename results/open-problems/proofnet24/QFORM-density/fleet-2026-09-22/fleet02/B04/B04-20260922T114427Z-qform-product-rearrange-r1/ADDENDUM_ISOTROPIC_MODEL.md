# B04 addendum — exact isotropic model via logarithmic product rearrangement

The non-isotropic large-row theorem degenerates when the distinguished row is `Lambda`-isotropic. The canonical three-dimensional isotropic quadratic is bilinear rather than a square. This addendum proves that the bilinear logarithmic singularity is exactly mild enough to be killed by the third square direction under the owner hypotheses.

## Theorem `QFORM-BILINEAR-PLUS-SQUARE-v1`

Let `X,Y,Z` be independent real random variables with probability densities bounded by one. Let `c,lambda` be nonzero real numbers and set

`Q = 2 c X Y + lambda Z^2`.                                                     (1)

Then `Q` has a bounded density satisfying

`||p_Q||_infinity
 <= |c|^(-1) + 2*24^(1/3)|c|^(-2/3)|lambda|^(-1/3).`                          (2)

In particular, if `|c|>=1` and `|lambda|>=1`, then

`||p_Q||_infinity <= 1+2*24^(1/3)`.                                            (3)

The symmetric matrix of (1) is

`[[0,c,0],[c,0,0],[0,0,lambda]]`,

whose eigenvalues are `(c,-c,lambda)`. Thus (3) is a genuine indefinite three-large-eigenvalue case of the owner target; it is not a diagonal physical-coordinate form.

### Proof

We first prove a universal product-density envelope.

### Lemma 1 — logarithmic product envelope

If `X,Y` are independent with densities `f,g<=1`, then for `U=XY`, at every nonzero Lebesgue point,

`p_U(u) <= 2 + 2 log_+(1/|u|)`.                                                (4)

For `0<|u|<=1`, use

`p_U(u)=int_R f(x)g(u/x) dx/|x|`.

Split the integral into three regions.

1. On `|x|<=|u|`, substitute `y=u/x`. Then `|y|>=1` and `|dx|/|x|=|dy|/|y|`, so this contribution is at most

`int_{|y|>=1} g(y)dy <=1`.

2. On `|u|<|x|<=1`, use `f,g<=1`; the contribution is at most

`int_{|u|<|x|<=1} dx/|x| = 2 log(1/|u|)`.

3. On `|x|>1`, use `1/|x|<=1` and `g<=1`; the contribution is at most

`int_{|x|>1}f(x)dx <=1`.

This proves (4) for `|u|<=1`. If `|u|>1`, the same split at `|x|=1` gives at most `1/|u|` from `|x|<=1` after the substitution and at most `1` from `|x|>1`, hence at most `2`; this is again (4).

Now put

`W=2cXY`.

Scaling (4) gives

`p_W(w)
 <= |c|^(-1)[1+log_+(2|c|/|w|)]
 = |c|^(-1) + ell_c(w)`,                                                       (5)

where

`ell_c(w)=|c|^(-1)log_+(2|c|/|w|)`.

A direct gamma-integral computation gives

`||ell_c||_3^3
 = |c|^(-3) int_{|w|<2|c|} log^3(2|c|/|w|)dw
 = 24 |c|^(-2)`,

so

`||ell_c||_3 = 24^(1/3)|c|^(-2/3)`.                                           (6)

For the third variable, the decreasing-rearrangement one-square estimate from the primary B04 report gives, for `V=lambda Z^2`,

`||p_V||_{3/2} <= 2 |lambda|^(-1/3)`.                                         (7)

Since `W` and `V` are independent,

`p_Q=p_W*p_V`.

The constant part in (5), convolved with the probability density `p_V`, contributes at most `|c|^(-1)`. Young's inequality with exponents `3` and `3/2` and (6)--(7) gives

`||ell_c*p_V||_infinity
 <= ||ell_c||_3 ||p_V||_{3/2}
 <= 2*24^(1/3)|c|^(-2/3)|lambda|^(-1/3)`.

This proves (2), and (3) follows immediately. QED.

## Interpretation for the large-row frontier

For signature `(2,1)` or `(1,2)`, an exactly `Lambda`-isotropic spectral direction is the natural limit `a=u^T Lambda u ->0` of the Schur-completion theorem. In a Witt basis, the quadratic form has a bilinear hyperbolic pair. The theorem above shows that, when that hyperbolic pair is carried by two independent physical product variables, its only singularity is logarithmic and the third square direction smooths it to a universal `L^infinity` density.

This gives a concrete replacement mechanism at the exact isotropic endpoint rather than trying to force the `|a|^(-1/4)` Schur estimate through `a=0`.

The remaining generic isotropic difficulty is dependence: after a large physical row is aligned with an isotropic spectral vector, its bilinear partner and the third direction are usually **projections of the same residual physical coordinates**, not independent variables. A next target-level lemma should therefore prove a two-dimensional product-projection analogue of Lemma 1 that preserves enough joint normalization to combine with the third direction. Any proof that merely diagonalizes the residual two-plane and multiplies marginal estimates would violate `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`.

No full-target claim is made.
