SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-23T19:29:04Z.
attacking: the zero/near-zero physical square pivot when a genuine original-coordinate cross coupling can replace the missing square receiver, while retaining a C0 output density.

# account03/B15 auto26 — external-coupling rescue of a vanishing square pivot

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T192904Z-account03-B15-qform-auto26`  
Status: `NEW TARGET-VALID REGULARITY BRANCH / PARTNER APPLIED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope

Let the independent original coordinates contain four distinct variables `X,Y,Z,U`, each with a probability density bounded by one. Write the symmetric physical coefficient matrix in those coordinates and assume only

- `b=A_XY != 0`,
- `A_YY=0`,
- `A_XZ=A_YZ=0`,
- `gamma=A_ZZ` is arbitrary (possibly zero),
- `c=A_ZU != 0`.

Every other matrix entry is arbitrary: `A_XX`, `A_XU`, `A_YU`, `A_UU`, all couplings to every remaining original coordinate, all remaining self blocks, all signs and all additional spectrum are unrestricted.

Then `Q=X^TAX` has a density in `C_0(R)`. Quantitatively,

`||p_Q||_infinity <= 3 |b|^(-2/3) Psi(gamma,c)`,

where

`Psi(gamma,c)=2|gamma|^(-1/3)` if `|gamma|>=8|c|`, and

`Psi(gamma,c)=(3/2)|c|^(-1/3)-|gamma|^(2/3)/(8|c|)` if `0<=|gamma|<8|c|`.

The first branch is interpreted in the obvious limiting sense when `c=0`; the new content here is `c!=0`, especially the endpoint `gamma=0`. In that endpoint one also has the independent sharper family

`||p_Q||_infinity <= p q |b|^(-1+1/p)|c|^(-1/p),   q=p/(p-1), 1<p<infinity`,

and in particular

`boxed( ||p_Q||_infinity <= 4 / sqrt(|bc|) )`.

Thus a vanishing physical square pivot does not force a blow-up if the same original coordinate has a genuine cross coupling to one independent outside coordinate. This is a product-preserving statement; no rotation is used.

## 2. Completed partner input actually used

The designated partner `account04/B15` proved at

`yspennstate/math-open-problems@f8d97d9b706dc383144c98bec09a0af076e762da`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T151702Z-account04-B15-pivoted-convolution-r6/REPORT.md`,

that for independent cap-one `X,Y`, arbitrary real `a,u,v,k`, and `b!=0`,

`T=aX^2+2bXY+2uX+2vY+k`

has a density satisfying, for every `1<p<infinity`,

`||p_T||_p <= p |b|^(-1+1/p)`.

In particular,

`||p_T||_3 <= 3|b|^(-2/3)` and `||p_T||_2 <= 2|b|^(-1/2)`.

This theorem is used below at the actual conditional-output inequalities; it is not merely cited.

## 3. Rough quadratic-or-affine receiver

### Lemma 3.1

Let `Z` have a probability density `f_Z<=1`. For real `gamma,r`, not both zero, put

`S=gamma Z^2+2rZ`.

Then

`boxed( ||p_S||_(3/2) <= min( 2|gamma|^(-1/3), (2|r|)^(-1/3) ) ).`

The terms with zero denominator are read as `+infinity`.

### Proof

The affine estimate is exact scaling:

`||p_(2rZ)||_(3/2)=(2|r|)^(-1/3)||f_Z||_(3/2)<=(2|r|)^(-1/3)`.

For the quadratic estimate, complete the square. Translation of `Z` and of the output changes no norm, so it suffices to consider `gamma W^2`. Its density `h` obeys the pointwise envelope

`h(t)<=|gamma t|^(-1/2)` on its supporting half-line.

Therefore

`int h(t)^(3/2)dt = E[h(gamma W^2)^(1/2)]`
` <= |gamma|^(-1/2) E|W|^(-1/2)`.

For every cap-one probability density and every translation,

`E|W|^(-1/2)<=int_(-1/2)^(1/2)|x|^(-1/2)dx=2sqrt(2)`

by the elementary one-dimensional bathtub principle. Hence

`int h^(3/2)<=2sqrt(2)|gamma|^(-1/2)`,

and raising to power `2/3` gives

`||h||_(3/2)<=2|gamma|^(-1/3)`.

Taking the better of the two valid estimates proves the lemma. No support, moment, smoothness or connectedness assumption occurs.

## 4. Conditioning and the exact interpolation integral

Let `R` denote all original coordinates other than `X,Y,Z,U`. Condition first on `(R,U)=(r0,u)`. Because `A_XZ=A_YZ=0`, the remaining random part splits as

`Q = T_(r0,u)(X,Y) + S_(r0,u)(Z) + constant`,

where

`T_(r0,u)=aX^2+2bXY+2alpha(r0,u)X+2beta(r0,u)Y`

and

`S_(r0,u)=gamma Z^2+2(cu+d(r0))Z`.

The variables `(X,Y)` and `Z` are independent on this genuine original-coordinate fiber. The partner theorem and Lemma 3.1, followed by Young at exponents `3` and `3/2`, give for almost every `(r0,u)`

`||p_(Q|r0,u)||_infinity`
` <= 3|b|^(-2/3) min(2|gamma|^(-1/3),(2|cu+d(r0)|)^(-1/3)).`      (4.1)

The possible fiber `cu+d(r0)=0=gamma` is a single `u` and therefore null for the absolutely continuous law of `U`; it has no effect on disintegration.

Now average (4.1) over `U`. Since `f_U<=1` and has mass one, the radial decreasing kernel is maximized by placing the mass on the unit interval centered at `-d(r0)/c`. Put

`A=2|gamma|^(-1/3)`, `B=(2|c|)^(-1/3)`.

The required exact integral is

`J=2 int_0^(1/2) min(A,Bu^(-1/3))du`.

The switching point is

`u_*=(B/A)^3=|gamma|/(16|c|)`.

If `u_*>=1/2`, equivalently `|gamma|>=8|c|`, then `J=A=2|gamma|^(-1/3)`.

If `u_*<1/2`, then

`J=2Au_*+2B int_(u_*)^(1/2) u^(-1/3)du`
` =2Au_*+3B[(1/2)^(2/3)-u_*^(2/3)]`
` =(3/2)|c|^(-1/3)-|gamma|^(2/3)/(8|c|)`.

This is exactly `Psi(gamma,c)`. It is continuous at `|gamma|=8|c|`, where both formulas equal `|c|^(-1/3)`.

Averaging next over `R` does not change the bound. Thus

`boxed( ||p_Q||_infinity <=3|b|^(-2/3)Psi(gamma,c) ).`            (4.2)

In particular the estimate stays finite through the null pivot `gamma->0` whenever `c!=0`:

`||p_Q||_infinity <= (9/2)|b|^(-2/3)|c|^(-1/3)` at `gamma=0`.

## 5. Optimized null-pivot estimate

When `gamma=0`, one can use the full partner `L^p` family rather than fixing `p=3`. Let `q=p/(p-1)`. Conditional on `(R,U)`, the affine receiver obeys

`||p_(2(cu+d)Z)||_q <= (2|cu+d|)^(-1/p)`.

Young and the partner theorem therefore give

`||p_(Q|R,U)||_infinity`
` <= p |b|^(-1+1/p)(2|cU+d(R)|)^(-1/p)`.

The fractional bathtub integral is exact at the level needed here:

`E_U (2|cU+d|)^(-1/p) <= q |c|^(-1/p)`.

Indeed, after centering and scaling,

`int_(-1/2)^(1/2)(2|c||u|)^(-1/p)du=q|c|^(-1/p)`.

Hence, for every `1<p<infinity`,

`boxed( ||p_Q||_infinity <= p q |b|^(-1+1/p)|c|^(-1/p) ).`       (5.1)

Taking `p=q=2` yields

`boxed( ||p_Q||_infinity <=4|bc|^(-1/2) ).`                      (5.2)

This is homogeneous of degree `-1` under a common scaling of the quadratic form, as required.

## 6. Continuous density, not only an essential cap

For every nonexceptional conditional fiber, the partner factor belongs to `L^p` and the receiver belongs to `L^q`, with `1<p,q<infinity` conjugate. Therefore

`p_(Q|R,U)=p_T*p_S in C_0(R)`

because `L^p*L^q subset C_0`.

The conditional sup norms are dominated by the integrable envelopes computed in Sections 4 and 5. Dominated convergence in `U`, followed by dominated convergence in `R`, therefore shows that the unconditional density itself satisfies

`boxed( p_Q in C_0(R) ).`                                       (6.1)

Thus this branch proves the owner's stronger continuity conclusion as well as the quantitative essential-height bound, without any common Holder modulus or pointwise Fourier decay.

## 7. Matrix interpretation and target relevance

On the physical coordinates `(X,Y,Z,U)`, the relevant visible pattern is

`[[a,b,0,r],`
` [b,0,0,s],`
` [0,0,gamma,c],`
` [r,s,c,d]]`,

with `b c !=0`; the entries `a,r,s,d` are arbitrary, and every coupling to all other coordinates is arbitrary. At the exact null endpoint `gamma=0`, the determinant of this displayed `4x4` core is

`det = b^2 c^2`,

independent of `a,r,s,d`, and its inertia is `(2,2)` because eliminating the invertible hyperbolic `(X,Y)` block leaves another hyperbolic `[[0,c],[c,*]]` Schur block. The analytic estimate (5.2) may be written

`||p_Q||_infinity <=4 |det(core)|^(-1/4)`

for this null-pivot pattern.

A concrete owner-target control is `a=r=s=d=gamma=0`, `b=c=1`: the four eigenvalues of the core are `1,-1,1,-1`, so it certainly has at least three eigenvalues of modulus at least one, while (5.2) gives the actual rough-law bound

`p_Q in C_0,   ||p_Q||_infinity<=4`.

More importantly, (4.2) is stable as a square pivot tends to zero provided a transverse original-coordinate coupling `c` remains available. This is precisely the sort of regularity passage that a near-null physical-pivot reduction may use without treating a small matrix coefficient as a small random error.

## 8. What this does not prove

The unrestricted three-large-eigenvalue conjecture remains OPEN. The bare spectral hypothesis does not by itself force four original coordinates with `A_YY=0` and `A_XZ=A_YZ=0` and nonzero `A_XY,A_ZU`. Rotating coordinates to create this pattern would destroy input independence and is forbidden.

The remaining structural question is therefore whether an actual unresolved low-rank/high-leverage configuration can be reduced, in original coordinates and with uniform constants, either to this external-coupling-rescued null-pivot pattern or to another completed branch. If not, a grouped-coordinate version of the same `L^p*L^q` mechanism is still needed.

No Gaussianity, log-concavity, moments, compact support, connected support, diagonal-basis assumption, arbitrary-joint coarea bound, fiber supremum, pointwise van-der-Corput decay, or Monte Carlo inference is used.
