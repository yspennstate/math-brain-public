# fleet02/B14 — overlap hyperbolic third-curvature localization

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260924T055741Z-fleet02-B14-QFORM-auto11`.
Status: supporting localization theorem + exact active-fragment barrier; full unrestricted QFORM remains OPEN; continuity remains separate.

## First unpaid implication

`QFORM-ACTIVE-CURVATURE-AGGREGATE-BEFORE-ENTROPY-v1`.

Before arbitrary localization of any coordinate that supplies the third smoothing curvature, force one of:

1. the fleet03/B14 same-sign overlap compiler with both square carriers left whole;
2. the overlap-hyperbolic determinant compiler proved below, with the hyperbolic pair and third-curvature carrier left whole; or
3. an already-certified whole-law D'/D5/projected-crossing/ridge/hub/grouped-bank/physical-triple exit.

A translation-uniform cellwise estimate linear in the mass of the third hyperbolic curvature carrier is impossible: the exact target core `2UV+Y^2` has an `m log(1/m)` submeasure lower bound. Thus arbitrary active refinement cannot be paid after the logarithmic singularity has been exposed.

## Inputs and source matching

The newest designated fleet03/B14 input is `QFORM-OVERLAP-SAME-SIGN-SQUARE-COMPILER-v1` at `math-open-problems@7c982b2537be11bbe3f63123e2870171bfb27717`: for same-sign curvatures it allows the first square center to depend arbitrarily on the transverse coordinate and still gives `pi K_W K_U/sqrt(|ad|)`. Its addendum is authoritative about prior-source matches.

The uncoupled mass-sensitive hyperbolic-plus-square optimization is already present in fleet01/B14 at repository snapshot `9c7d5029a308cb0f4903065baab48638203c4206`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B14/20260924T001138Z-fleet01-B14-QFORM-auto11/REPORT.md`. I do not relabel that theorem as new. The new step here is the arbitrary same-bank overlap extension (`UY` and `VY` couplings), its determinant-only corollary, and the exact translated active-submeasure lower barrier.

The fixed required Claude source is `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`; `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` were read. A completed result from that source is applied in Section 6.

No moment, support, diameter, fragment-count, connectedness, log-concavity, post-rotation independence or bounded translation hypothesis is used.

## 1. Overlap completion

Let `U,V,Y` be independent. Allow positive subdensities `u,v,w`, each bounded by one, with masses

`int u=m`, `int v=n`, `int w=r`, where `0<m,n,r<=1`.

Fix real coefficients with `a!=0` and define

`Q = 2aUV + 2b UY + 2c VY + lambda Y^2 + alpha U + beta V + gamma Y + eta`.

Set the Schur residual

`delta = lambda - 2bc/a`.

Assume `delta!=0`. The exact identity

`Q = 2a (U + (c/a)Y + beta/(2a)) (V + (b/a)Y + alpha/(2a))
       + delta Y^2 + ell Y + eta0`

holds, where

`ell = gamma - (c alpha + b beta)/a`,
`eta0 = eta - alpha beta/(2a)`.

For each fixed `Y=y`, the two product variables have merely been translated. Their independence and density caps are unchanged. Thus every translation-uniform product estimate may be applied before integrating in `y`; the overlap terms `b,c` cost nothing except through the genuine residual curvature `delta`.

This is the hyperbolic counterpart of the partner's same-sign overlap observation.

## 2. Mass-sensitive product envelope

For completeness, the only product estimate needed is the already-proved two-threshold envelope. For subdensities `u,v` of masses `m,n`, the pushforward density `h` of `UV` obeys, for every `R,S>0`,

`h(z) <= m/R + n/S + 2 log_+(RS/|z|)`.

Optimizing at fixed `q^2=RS` gives

`h(z) <= 2 sqrt(mn)/q + 2 log_+(q^2/|z|)`.

Therefore the pushforward under `2aUV`, uniformly under arbitrary translations of both variables, satisfies

`p(x) <= sqrt(mn)/(|a| q) + |a|^{-1} log_+(2|a|q^2/|x|)`.

The location of either subdensity never appears.

## 3. Finite-mass logarithmic square potential

Let `w` be any subdensity bounded by one with mass `r`. For `A,d>0`, every `t` satisfies

`int w(y) log_+(A/|t-d y^2|) dy <= 2 psi_r(K)`,

where

`K=2 sqrt(2A/d)`,

and

`psi_r(K)=K` for `K<=r`,
`psi_r(K)=r(1+log(K/r))` for `K>=r`.

Proof: layer cake and the uniform level-set estimate

`|{y: |tau-y^2|<eps}| <= 2 sqrt(2eps)`

give

`int_0^infinity min(r, K e^{-s/2}) ds`,

which evaluates exactly to the displayed two branches. An arbitrary linear term in `y` is removed by completing the square; translating `w` preserves cap and mass.

## 4. Main theorem: overlap hyperbolic mass compiler

Define

`theta = 2 sqrt(|a| m n / |delta|) / r`.

Then the output submeasure of `Q` has an essentially bounded density and

`boxed: ||p_Q^(sub)||_infinity <= (2r/|a|) Phi(theta),`

where

`Phi(theta)=2 sqrt(theta)` for `0<theta<=1`,
`Phi(theta)=2+log(theta)` for `theta>=1`.

### Proof

Use the completion in Section 1. For fixed `y`, apply the translation-uniform product envelope of Section 2 to the shifted `U,V`. Integrating the constant part against `w` costs

`r sqrt(mn)/(|a|q)`.

For the logarithmic part, complete `delta y^2+ell y`, then apply Section 3 with

`A=2|a|q^2`, `d=|delta|`, hence `K=4q sqrt(|a|/|delta|)`.

Therefore

`|a| ||p_Q^(sub)||_infinity
 <= r sqrt(mn)/q + 2 psi_r(4q sqrt(|a|/|delta|)).`

Put

`x=4q sqrt(|a|/|delta|)/r`.

The right side becomes

`2r theta/x + 2r psi_1(x)`.

If `theta<=1`, the minimizer is `x=sqrt(theta)<=1`, giving `4r sqrt(theta)`. If `theta>=1`, the minimizer is `x=theta>=1`, giving `2r(2+log theta)`. Divide by `|a|`.

All affine coefficients are arbitrary. In particular, if an independent outside environment `Z` changes `alpha,beta,gamma,eta` measurably, condition on `Z`; the same estimate is uniform in `z`. A positive environment piece of mass `s` simply multiplies the bound by `s`, so arbitrary finite or countable outside localization is exactly mass-linear and zero-tax.

## 5. Determinant-only whole-law exit

For the physical block

`B = [[0,a,b],[a,0,c],[b,c,lambda]]`,

`det B = -a^2 delta`.

Take probability marginals (`m=n=r=1`) and write `D=|det B|`. Then

`theta = 2 |a|^(3/2) / sqrt(D)`.

Suppose only

`|a|>=1`, `D>=1`.

If `theta<=1`, the theorem gives

`||p_Q||_infinity <= 4 sqrt(theta)/|a| <= 4/|a| <= 4`.

If `theta>=1`, use `D>=1`:

`||p_Q||_infinity
 <= (2/|a|)[2+log theta]
 <= [4+2log2+3log|a|]/|a|`.

The last expression is decreasing for `|a|>=1`, hence

`boxed: ||p_Q||_infinity <= 4+2 log 2 = 5.38629436111989... .`

This requires neither a lower bound on `|delta|` nor a lower bound on the smallest eigenvalue of `B`; a tiny Schur residual is automatically compensated by the large hyperbolic coefficient when the determinant stays non-small.

If all three eigenvalues of this `3x3` block have modulus at least one, the two hypotheses above are automatic. Indeed the `2x2` principal block `[[0,a],[a,0]]` has eigenvalues `+-|a|`; Cauchy interlacing forces `|a|>=1`, while `D` is the product of the three eigenvalue magnitudes and is at least one.

The same conclusion holds inside any ambient quadratic form after conditioning on every outside original coordinate: all outside couplings become arbitrary affine coefficients already covered by the theorem. Outside supports may be fragmented, translated or unbounded.

### Near-singular overlap family

For `M>=1`, put

`B_M=[[0,1,M],[1,0,M],[M,M,2M^2+1]]`.

Then

`2UV+2M(U+V)Y+(2M^2+1)Y^2 = 2(U+MY)(V+MY)+Y^2`,

so `a=1`, `delta=1`, `det B_M=-1`, and the bound above is exactly `4+2log2`, uniformly in `M`.

The eigenvalues are

`-1`,
`lambda_-(M)=M^2+1-M sqrt(M^2+2)`,
`lambda_+(M)=M^2+1+M sqrt(M^2+2)`,

with `lambda_- lambda_+=1` and `lambda_-(M)~(2M^2)^{-1}`. Thus the active physical triple can become arbitrarily ill-conditioned even though the overlap completion remains uniformly bounded.

## 6. Fixed-source result applied to a real target inequality/obstruction

Add an independent cap-one variable `Z` and define

`Q_M = 2UV+2M(U+V)Y+(2M^2+1)Y^2+Z^2`.

Its matrix has spectrum

`{-1, lambda_-(M), lambda_+(M), 1}`,

so it lies in the exact owner target: `-1`, `1`, and `lambda_+(M)>1` are three eigenvalues of modulus at least one.

The new overlap theorem gives

`boxed: ||p_{Q_M}||_infinity <= 4+2log2 = 5.3862943611...`

because convolution with the independent `Z^2` cannot increase `L^infinity`.

Now apply a completed result from the required fixed source. `COUNTEREXAMPLE_SEARCH.md`, Theorem A, says that a three-dimensional physical block whose three eigenvalues have modulus at least `sigma` has density at most `6sqrt(pi)/sigma`, with arbitrary linear terms. Condition on `Y`; on the retained original coordinates `(U,V,Z)` the quadratic block is

`[[0,1,0],[1,0,0],[0,0,1]]`,

whose eigenvalues are `{-1,1,1}`. The conditioning-generated terms in `U,V` are affine, so Theorem A gives

`boxed: ||p_{Q_M}||_infinity <= 6sqrt(pi)=10.6347231054...`

uniformly in `M`.

By contrast, applying the same Theorem A to the ill-conditioned active block `B_M` itself with `sigma=lambda_-(M)` gives the valid but useless certificate

`6sqrt(pi)/lambda_-(M) ~ 12sqrt(pi) M^2`.

Thus the same exact-target family has a uniform source-valid whole-law certificate while reciprocal payment of the wrong physical triple's smallest eigenvalue diverges quadratically. The overlap completion removes precisely that artificial near-degeneracy loss.

The fixed source's Theorem B also gives the independent check `||p_{Q_M}||_infinity<=8sqrt(2pi)=20.0530261970...`, since the `4x4` matrix is invertible and its range projection is the identity.

## 7. Exact active-third-curvature mass barrier

The mass dependence in Section 4 cannot be improved to a translation-uniform linear bound `C r` on the third curvature carrier.

Take `a=delta=1`, `b=c=alpha=beta=gamma=eta=0`, let `U,V` be independent Uniform`[-1/2,1/2]`, and let the `Y` input be the positive subdensity

`w_m=1_[-m/2,m/2]`, `0<m<=1`.

The density of `2UV` is exactly

`p_{2UV}(z)=log(1/(2|z|))`, for `0<|z|<1/2`.

Hence the unnormalised output submeasure of `2UV+Y^2` has, at zero,

`p_m(0)
 = int_{-m/2}^{m/2} log(1/(2y^2)) dy
 = m[2log(1/m)+2+log2].`

Therefore

`boxed: p_m(0)/m = 2log(1/m)+2+log2 -> infinity.`

No universal bound `||p_m||_infinity<=C m` is possible. The leading `2m log(1/m)` agrees with the entropy scale of the upper compiler, so the logarithmic mass loss is not merely an artifact of its proof.

The obstruction is fully translation-uniform. For any remote center `R`, take `w_{m,R}=1_[R-m/2,R+m/2]` and the affine term that completes the third curvature as `(Y-R)^2`; the same identity holds. Thus distant fragments and conditioning-generated affine shifts can reproduce the endpoint at arbitrary locations.

For a decomposition into masses `r_j`, positive piecewise certificates necessarily carry an entropy-type cost; equal masses `1/N` produce a `log N` loss. This is a proof-interface obstruction, not a QFORM counterexample: with the whole `Y` law retained, the exact target core `2UV+Y^2` is uniformly bounded (and the fixed-source Theorem A gives `6sqrt(pi)`).

## 8. Consequence for localization order

The fleet03/B14 same-sign overlap theorem and the present hyperbolic overlap theorem now give a sign-complementary rule:

- same-sign: two whole square carriers form a terminal Beta core; arbitrary outside localization is mass-linear, but fragmenting a carrier before the Beta endpoint has no positive mass homogeneity;
- hyperbolic/opposite-sign: the two-variable product is logarithmically singular and requires genuine third curvature; arbitrary overlap `UY,VY` is harmless after completion, but fragmenting that third curvature before payment has an unavoidable `m log(1/m)` loss.

Thus translations, remote fragments and unbounded support are not the debt. The debt is **which variables are localized before the active curvature is aggregated**. A full proof must route the matrix into a completed whole-active certificate before taking positive fragment sums.
