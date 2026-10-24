# B08 peer-consumption addendum — pi upgrade and a rotation-information no-go

**Live target:** owner revision `2026-09-22.4`, full bounded-density quadratic-form conjecture.  
**Full target:** **OPEN / NOT PROVED**.

## 1. Named OTHER-account result consumed and applied

I consumed account03/B17 run `account03-B17-20260922T112131Z`, exact source

`yspennstate/math-open-problems@c64fcff680b0a252a3c92002c60eedba02bbb9ec`

at

`qform/fleet-2026-09-22/account03/B17/account03-B17-20260922T112131Z/REPORT.md`.

That report independently proves the same pointwise-Fresnel no-go and, more strongly than B08's preliminary `L^3` diagonal constant `8`, proves the exact source lemma:

> if `X_1,X_2` are independent with densities `<=1` and `lambda_1,lambda_2` have the same sign with `|lambda_i|>=1`, then `lambda_1 X_1^2+lambda_2 X_2^2` has density at most `pi/sqrt(|lambda_1 lambda_2|)`.

By pigeonhole, it obtains the whole coordinate-diagonal three-large-eigenvalue branch with `C=pi`.

The next theorem applies that result to a non-diagonal ambient form.

## 2. Conditional same-sign coordinate-pair theorem

### Theorem — `QFORM-CONDITIONAL-SAMESIGN-PAIR-PI-v1`

Let `X_1,...,X_n` be independent real random variables with densities bounded by `1`, and write

`Q(x)=x^T A x`

in the original independent-coordinate basis. Suppose there exist two distinct coordinates `i,j` such that

`A_ij=0`,

`A_ii A_jj>0`,

and

`|A_ii|, |A_jj| >=1`.

Then `Q(X)` is absolutely continuous with

`boxed( ||p_Q||_infinity <= pi/sqrt(|A_ii A_jj|) <= pi ).`

### Proof

Condition on all coordinates except `X_i,X_j`. For every fixed outside vector `w`, the conditional quadratic polynomial is

`Q_w(X_i,X_j)
 = A_ii X_i^2 + beta_i(w) X_i
 + A_jj X_j^2 + beta_j(w) X_j + c(w)`,

because `A_ij=0`. The two retained variables remain independent under this conditioning.

Complete the two squares:

`A_ii X_i^2+beta_i X_i
 = A_ii (X_i+beta_i/(2A_ii))^2 - beta_i^2/(4A_ii)`,

and similarly for `j`. Translation preserves the density bound `<=1`. Since `A_ii,A_jj` have the same sign, account03/B17's same-sign pair lemma therefore gives, uniformly in `w`,

`||p_{Q_w}||_infinity
 <= pi/sqrt(|A_ii A_jj|)`.

The unconditional law is the mixture of these conditional laws. For every Borel interval `I`,

`P(Q in I)
 = E_w P(Q_w in I)
 <= [pi/sqrt(|A_ii A_jj|)] |I|`.

Hence the unconditional law has a density with the same `L^infinity` bound. `QED`.

This strictly extends the globally coordinate-diagonal branch: arbitrary couplings to every *other* coordinate are permitted; only the cross coefficient inside the selected same-sign pair must vanish.

## 3. Rotating and retaining only a joint L-infinity density bound cannot solve the indefinite case

The full problem cannot be reduced to: rotate to three eigencoordinates, note that their joint density is bounded by a universal constant, and then apply only that bound. There is a concrete geometric obstruction.

### Proposition — `QFORM-ROTATED-LINF-ONLY-NOGO-v1`

For the signature `(2,1)` quadratic form

`q(x,y,z)=x^2+y^2-z^2`,

the following holds. For every `delta>0` there is a compactly supported probability density `h` on `R^3` with `0<=h<=1` such that

`P_h(|q|<=delta)=1`.

Consequently the density of `q(Y)`, whenever represented by a bounded density, must have supremum at least `1/(2 delta)`. Thus no universal output-density bound is possible for arbitrary joint input densities merely satisfying `||h||_infinity<=1`.

### Proof

Use cylindrical coordinates `(r,theta,z)` and then

`u=r-z`, `v=r+z`.

Then

`q=r^2-z^2=uv`,

`r=(u+v)/2`,

and the Euclidean volume element is

`dx dy dz = r dr dtheta dz = (u+v)/4 du dv dtheta`.

Fix `R>0` so large that the region below has `r>0`, and define

`D_{delta,R}={0<=theta<2pi, R<=v<=2R, |u|<=delta/v}`.

Every point of this region satisfies `|q|=|uv|<=delta`. Its volume is exactly

`|D_{delta,R}|
 = integral_0^{2pi} integral_R^{2R} integral_{-delta/v}^{delta/v} (u+v)/4 du dv dtheta
 = pi delta R`.

Choose `R=2/(pi delta)`, so the volume is `2`, and choose a measurable compact subset `E` of volume `1`. Put `h=1_E`. Then `h` is a probability density bounded by `1` and `|q|<=delta` almost surely. If `q(Y)` had density bounded by `C`,

`1=P(|q(Y)|<=delta)<=2 delta C`,

so `C>=1/(2delta)`. Since `delta` is arbitrary, no universal `C` exists for the class of arbitrary joint densities bounded by `1`. `QED`.

### Meaning for the owner target

This is **not a counterexample** to the conjecture, because after rotating an original product measure the resulting joint density is a very special orthogonal image of a product density, not an arbitrary `h<=1`. The proposition proves that any successful rotation-based proof must retain quantitative information about that product origin; a generic projection-density bound alone necessarily discards too much.

## 4. Updated first essential implication

The surviving target-level implication is therefore more specific than a generic rotated-density estimate:

`QFORM-PRODUCT-STRUCTURE-OSCILLATORY-L1-v2`:

> prove a dimension-free `L^1_t` bound for `E exp(it X^T A X)` under the original product measure, using three spectral directions `|lambda|>=1`, in a way that survives delocalized eigenvectors and explicitly retains product structure after rotation/conditioning.

Two pieces are now source-valid inputs:

1. account03/B17's same-sign pair coarea lemma with constant `pi`;
2. B08's `L^3` square-characteristic bound and its uniformity under arbitrary linear terms.

A proof that replaces the rotated product density by only an `L^infinity` bound is ruled out by the null-cone construction above.
