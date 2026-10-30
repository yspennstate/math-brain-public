# Addendum: arbitrary Gaussian-location mixtures are globally bounded by the centered reflection

Run: `20260924T074031Z-fleet01-B17-QFORM-auto11`  
Status: stronger supporting theorem found after the initial run report. **FULL QFORM remains OPEN.** Continuity for the unrestricted target remains separate.

This addendum strictly strengthens Section 2 of `REPORT.md`: the majority-plane restriction on the Gaussian location is unnecessary.

## Theorem G — global arbitrary-location Gaussian reflection barrier

Let `s>0`, let `G~N(0,s I_3)`, let `M` be an arbitrary independent random vector in `R^3` (no moment, density, support, or regularity assumption), and let `B` be any real symmetric orthogonal reflection with spectrum `{1,1,-1}`. Then

`Q=(G+M)^T B(G+M)`

has an essentially bounded density satisfying

`||p_Q||_infinity <= 1/(2 sqrt(2) s)`.

At the cap-one minimum-variance scale `s=1/12`,

`||p_Q||_infinity <= 3 sqrt(2)`.

The constant is exact: equality is attained for `M=0`.

### Proof

Condition on `M=m`. Orthogonally diagonalize `B` to `J=diag(1,1,-1)`. This is performed only after conditioning inside an isotropic Gaussian law; no claim about independence of rotated finite physical inputs is involved. Write the rotated location as `(u,a)` with `u in R^2`, `a in R`, and define

`U=|G_+ + u|^2`, `V=(G_3+a)^2`.

Then `U,V` are independent and `Q=U-V`.

Set `theta=2s`. The standard noncentral-chi-square Poisson mixture gives independent Poisson variables

`K~Poisson(|u|^2/(2s))`, `L~Poisson(a^2/(2s))`

such that conditionally on `(K,L)=(k,l)`,

`U ~ Gamma(1+k, theta)`,

`V ~ Gamma(1/2+l, theta)`.

This representation follows directly from the noncentral chi-square generating function; it can also be verified by expanding the modified-Bessel density in its power series.

By gamma additivity, on an enlarged probability space one may write

`U=U0+Uk`, `V=V0+Vl`,

where all four terms are independent,

`U0~Gamma(1,theta)`, `V0~Gamma(1/2,theta)`,

`Uk~Gamma(k,theta)`, `Vl~Gamma(l,theta)`,

with `Gamma(0,theta)` interpreted as the point mass at zero. Hence

`U-V = Q0 + Wkl`,

where

`Q0=U0-V0`, `Wkl=Uk-Vl`

are independent. Therefore

`p_{U-V | k,l} = p_{Q0} * mu_{Wkl}`,

and convolution with a probability measure is an `L^infinity` contraction:

`||p_{U-V | k,l}||_infinity <= ||p_{Q0}||_infinity`.

It remains only to compute the centered base law. Since `U0` is exponential with scale `theta` and `V0~Gamma(1/2,theta)`, for `q>=0`,

`p_{Q0}(q)=exp(-q/theta) p_{Q0}(0)`,

while for `q=-r<0`, the density of `V0` is decreasing and therefore

`p_{Q0}(-r)=integral_0^infinity f_{U0}(u) f_{V0}(u+r) du <= p_{Q0}(0)`.

Finally

`p_{Q0}(0)=integral_0^infinity f_{U0}(u)f_{V0}(u)du = 1/(sqrt(2) theta)=1/(2 sqrt(2)s)`.

Thus every fixed `(k,l)` component has density norm at most `1/(2sqrt(2)s)`. Mixing first over the independent Poisson variables `(K,L)`, then over the arbitrary law of `M`, preserves the same bound. This proves Theorem G.

## Relation to the designated partner result

The latest completed `fleet02/B17` result (`math-open-problems@5b85a3d5f95ea478f2534589aaf8729a4e1a29d6`) proved the exact `1/(2sqrt(2)s)` bound on the majority-sign one-sheet `q>=0` for arbitrary Gaussian location mixtures, and identified the off-axis negative two-sheet branch as unpaid. Theorem G closes that branch globally by a different mechanism: noncentral chi-square Poissonization plus gamma-shape additivity and `L^infinity` contraction under convolution. It does not use the live-refuted generic two-sheet X-ray shortcut.

## Stronger exact rotated stress family: all physical marginals iid

Retain the exact dense frame from `REPORT.md`:

`R0=(1/2)*[[1,1,1],[1,-1,1],[1,1,-1],[1,-1,-1]]`,

`B=[[0,0,1],[0,1,0],[1,0,0]]`,

and `A_m=R_m B R_m^T`, where `R_m` stacks `m` copies of `R0/sqrt(m)`. Then every physical matrix entry is nonzero and

`spec_nonzero(A_m)={1,1,-1}`.

Now give **all `4m` physical coordinates the same cap-one three-interval law**

`f_m(x)=1_{[-ell_m/2,ell_m/2]}(x)`

`       +1_{[a sqrt(m)-lambda/(4m),a sqrt(m)+lambda/(4m)]}(x)`

`       +1_{[-a sqrt(m)-lambda/(4m),-a sqrt(m)+lambda/(4m)]}(x)`,

with `ell_m=1-lambda/m`. Thus the finite physical inputs are iid, not merely independent.

For the four rows `r_j` of `R0`, the latent limit is

`Y_m => G + M`,

`G~N(0,I_3/12)`,

`M=a sum_{j=1}^4 S_j r_j`,

where the `S_j` are independent Skellam variables with Poisson parameters `(lambda/2,lambda/2)`. The location `M` now spans all of `R^3`; it is not restricted to either spectral sign subspace.

Pinned Theorem F at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` still applies in the actual physical frame: every row leverage is `3/(4m)`, the Gram is `I_3`, and the residual is zero. Hence the complete output densities converge uniformly to that of

`(G+M)^T B(G+M)`.

Theorem G yields the global upper bound

`limsup ||p_m||_infinity <=3sqrt(2)`.

On the event `S_1=S_2=S_3=S_4=0`, which has probability

`w0=[e^(-lambda) I_0(lambda)]^4=e^(-4lambda) I_0(lambda)^4`,

the limit is the centered Gaussian reflection. Therefore

`3sqrt(2)e^(-4lambda)I_0(lambda)^4 <= lim_{m->infinity} ||p_m||_infinity <=3sqrt(2)`.

This is an iid, entrywise-dense, exact-spectrum source-valid lower-witness family.

## Fixed variance and fixed Lindeberg defect can coexist with near-sharpness

For one physical coordinate,

`Var(X_m) -> 1/12 + lambda a^2`.

The vector triangular-array Lindeberg contribution from all four row types tends

`lambda a^2 sum_{j=1}^4 ||r_j||^2 =3 lambda a^2`,

because `sum_j r_j r_j^T=I_3` and hence `sum_j ||r_j||^2=3`.

Fix any `D>0` and choose `a=sqrt(D/lambda)`. Then all physical marginals are iid with limiting variance `1/12+D`, the vector Lindeberg defect tends to the fixed value `3D`, but

`e^(-4lambda)I_0(lambda)^4 ->1`

as `lambda->0`. Hence their output-density norms can approach `3sqrt(2)` arbitrarily closely despite a fixed nonminimal variance and a fixed positive Lindeberg defect.

Concrete choice:

`lambda=10^(-4)`, `D=1`, `a=100`.

Then every physical marginal has limiting variance `13/12`, the vector Lindeberg defect tends to `3`, and

`4.240944012619882... <= lim ||p_m||_infinity <= 4.242640687119286...`.

The certified gap is below `0.001697`.

## Diverging-moment iid diagonal variant

Set

`lambda_m=m^(-1/4)`, `a_m=m^(1/4)=lambda_m^(-1)`

and use the same three-interval law for every one of the `4m` coordinates. The per-coordinate satellite mass is `m^(-5/4)` and the satellite centers are `+-m^(3/4)`. The probability that any satellite appears among all `4m` coordinates tends to zero, so the latent vector converges weakly to `N(0,I_3/12)`. Yet

`Var(X_m)-1/12 ~ m^(1/4)`,

and the vector Lindeberg sum is asymptotic to `3m^(1/4)`, both diverging.

The uniform Theorem-F `|t|^(-3/2)` envelope again upgrades weak quadratic-form convergence to uniform density convergence, giving

`||p_{X^T A_m X}||_infinity ->3sqrt(2)`.

Thus even with iid physical coordinates, entrywise-dense exact target matrices, and exploding second moments/Lindeberg defect, the known lower obstruction is still asymptotically saturated. A sharp proof cannot obtain a fixed improvement from any of those features alone.
