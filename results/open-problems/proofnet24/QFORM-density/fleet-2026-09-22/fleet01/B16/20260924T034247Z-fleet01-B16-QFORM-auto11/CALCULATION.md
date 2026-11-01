# Early substantive calculation — conditional pair-log plus shared-square smoothing

Run `20260924T034247Z-fleet01-B16-QFORM-auto11`. Full QFORM remains open.

Let three original source blocks be mutually independent: a fresh scalar `H` with density cap `L_H`, a scalar receiver `U` with density cap `K_U`, and a block producing a possibly dependent pair `(S,V)` whose `V`-marginal has density cap `K_V`. Put

`Y = gamma H + S`, `gamma != 0`.

For almost every `v`, if `mu_v` is the conditional law of `S|V=v`, then

`p_(Y|V=v)(y) = int |gamma|^-1 f_H((y-s)/gamma) mu_v(ds) <= A`,

where `A=L_H/|gamma|`. This is a genuine fresh-source convolution statement; it does not infer a conditional projection cap from a marginal cap. Also `U` remains independent of `Y` conditional on `V` because the entire `U` source block is disjoint.

Consider

`Q = aY^2 + 2 beta YU + rY+sU + lambda V^2+dV+c`,

with `beta lambda !=0`. Set `B=K_U` and scale `x=A Y`, `z=B U`. Conditional on `V=v`, `x,z` are independent and each has density cap one. The pair quadratic matrix is

`M0 = [[a/A^2, beta/(A B)], [beta/(A B),0]]`.

It is invertible indefinite. Write

`kappa0 = sigma_min(M0)
 = (sqrt((a/A^2)^2+4(beta/(AB))^2)-|a|/A^2)/2 >0`.

The completed physical-pair logarithmic envelope gives, for every cutoff `R>0`, a conditional density representative

`p_(pair|V=v)(t)
 <= 2 sqrt(2)/R
    +(AB/|beta|) log_+(2R^2/(kappa0 |t-t0|))`,

where `t0` depends only on the fixed affine pair coefficients, not on `v`.

For any scalar density `p_V<=K_V`, any `lambda!=0`, and any `rho>0`,

`Leb{x: |lambda x^2+dx+e-q|<rho} <= 2 sqrt(2 rho/|lambda|)`.

Hence, with `W=lambda V^2+dV+e`,

`P(|W-q|<rho) <= min(1,2 sqrt(2) K_V sqrt(rho/|lambda|))`.

Layer cake gives, for `C>0`,

`E log_+(C/|W-q|)
 <= J(2 sqrt(2)K_V sqrt(C/|lambda|))`,

where `J(z)=2z` for `z<=1` and `J(z)=2+2log z` for `z>=1`.

Take `C=2R^2/kappa0` and choose

`R = sqrt(kappa0 |lambda|)/(4K_V)`.

Then the argument of `J` is exactly one, so `J=2`. Therefore

`||p_Q||_infinity
 <= 8 sqrt(2) K_V / sqrt(kappa0 |lambda|)
    + 2 A B/|beta|.`

This remains finite as the literal physical-hub pivot `a` tends to zero: then `kappa0 -> |beta|/(AB)`. It therefore gives a source-preserving bridge through the hyperbolic literal-hub discriminant whenever a genuine third square survives, even if `S` and `V` are dependent projections of the same original source bank.

For the authentic fleet03/B16 r38 family

`Q_a=aY^2+4YU+V^2`, `Y=sqrt(c)X_0+S`, `c=127/128`, `0<a<2^-14`,

use `A=c^-1/2`, `B=K_V=sqrt(2)`, `beta=2`, `lambda=1`. Then

`kappa0 >= 1.40864817...`

throughout the collar and the preceding estimate gives

`||p_(Q_a)||_infinity < 14.901`.

Thus the logarithmically divergent positive hub-first trace in that source-valid family is provably a lossy interface: regrouping the same sources as the indefinite `(Y,U)` pair and averaging its logarithmic singularity against the genuine `V^2` smoother gives a uniform all-level density bound.
