# Rigor check — account02/B15 20260924T063601Z

## 1. Multi-marginal constant

For one coordinate, the prior ruled submass theorem gives `20 sqrt(2) sqrt(m)`. If `delta=||f-g||_1` for two probability densities, the positive and negative parts of `f-g` each have mass `delta/2` and cap at most one. Hence each sign contributes

`20 sqrt(2) sqrt(delta/2)=20 sqrt(delta)`

and their difference contributes at most `40 sqrt(delta)`. Telescoping the product law therefore gives exactly

`40 sum_j sqrt(delta_j)`.

No hidden factor `sqrt(2)` remains.

## 2. Continuity at the cone vertex

For compact-smooth product input, the projected 3D density is compact-smooth. In the ruled formula

`r(s)=1/2 int_theta int_t rho(sqrt(s)e_theta+t(e_theta^perp+e_3)) dt dtheta`,

`sqrt(s)` is continuous on the closed half-line. On a compact `s`-neighborhood, compact support of `rho` bounds the relevant `t` uniformly. Dominated convergence therefore applies also at `s=0`. This proves one-sided continuity at the cone vertex without using an output height estimate.

## 3. Uniform C0 closure

Cap-preserving compact-smooth approximants converge in each marginal in `L1`; hence they are Cauchy in `L1`. The multi-marginal estimate makes their majority-sheet densities uniformly Cauchy on `[0,infinity)`. Every approximant is in `C_0([0,infinity))` because the source input is compactly supported, and `C_0` is closed in the uniform norm. Thus the limit is in `C_0([0,infinity))`.

Identification with the rough pushforward uses product `L1` convergence plus contraction of total variation under restriction and deterministic pushforward. Continuity is therefore downstream from the measure-level limit.

## 4. Gaussian smoothing facts in the blow-up extraction

For a finite union `E` of bounded intervals and `sigma>0`,

`f_sigma=1_E * gamma_sigma`

has mass one, is strictly positive, real analytic, Schwartz, and satisfies `0<f_sigma<=1` because convolution with a probability kernel preserves the `L-infinity` cap. Also `f_sigma->1_E` in `L1`.

The account03/B15 fixed-matrix stability theorem applies because the rational generic skeleton matrix has rank at least three. Therefore simultaneous smoothing of finitely many marginals converges uniformly at the output-density level. A rational `sigma` can be chosen inside any sufficiently small admissible interval.

## 5. Physical-triple degeneration inequality

For a rational generic matrix `A`, every physical `3x3` principal block is invertible. Define

`kappa_3(A)=max_|S|=3 min_{lambda in spec(A_SS)} |lambda| >0`.

Choose a maximizing triple. The newest account03/B15 localized theorem gives

`||p_Q||_infinity <= C_loc/kappa_3(A)`, `C_loc=128*2^(1/4)<153`.

Thus any witness with `p_Q(y)>N` obeys

`kappa_3(A)<C_loc/N`.

The direction of the inequality is correct: large output height forces small best-triple conditioning.

## 6. Status

These checks do not prove `C_*<infinity`; they validate only the stated ruled stability/regularity results and the conditional regular blow-up extraction. Full QFORM remains open.
