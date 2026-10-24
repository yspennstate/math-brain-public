# account02/B05 r22 checkpoint — rough one-sheet interval and two-sheet reciprocal shear

Status: substantive checkpoint; full QFORM OPEN.

Control/source pins: brain main observed at `242a09dd205070fbf820b4d950daeb89f1af4b8a`, owner revision `2026-09-22.15`; required Claude/math package `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` (`COUNTEREXAMPLE_SEARCH.md`, Theorem C); designated partner account03/B05 r20 handoff pins canonical math `yspennstate/math-open-problems@929322485c85c8a08367589be2b8e2e73839c65f`.

## Paid early implication: rough-input one-sheet interval theorem

Let `X` have arbitrary independent coordinate densities bounded by one. Let `r1,r2,r3` be orthonormal and

`Q=lambda1 <r1,X>^2 + lambda2 <r2,X>^2 - mu <r3,X>^2`,  `lambda1,lambda2,mu >=1`.

For every interval `I=[a,a+h]` with `a>=0`,

`P(Q in I) <= h (lambda1 lambda2 mu)^(-1/2) integral_0^{2pi} [sin^2(theta)/lambda1 + cos^2(theta)/lambda2 + 1/mu]^(-1/2) dtheta <= pi sqrt(2) h`.

This is an interval statement and does not assume continuity. Proof uses the ruled coordinates for `z1^2+z2^2-z3^2=s`:

`F(s,theta,t)=sqrt(s)e_theta+t(e_theta^perp+e3)`, with `|det dF/d(s,theta,t)|=1/2` for `s>0`.

For fixed `(s,theta)`, the `t`-curve is a complete affine line. After undoing the coefficient scaling, its parameter-direction norm is

`sqrt(sin^2(theta)/lambda1 + cos^2(theta)/lambda2 + 1/mu)`.

The line integral is therefore at most `2` divided by that norm, by the cap-two theorem for every two-dimensional orthogonal marginal of the original product law. Tonelli over `s in I` gives the displayed interval bound. The endpoint `a=0` follows by monotone limiting from `s>0`. This directly applies the pinned Theorem C geometry to rough inputs rather than inferring continuity.

## First unpaid implication: two-sheet reciprocal-shear Carleson estimate

Already for the unit signature `q(y)=y1^2+y2^2-y3^2`, the negative interval side has a different exact geometry. On the upper sheet define

`a=(y3+r)/sqrt(2)`, `b=(y3-r)/sqrt(2)`, `r=sqrt(y1^2+y2^2)`, `theta=arg(y1+iy2)`.

Then `q=-2ab`, `a>=b>=0`, and the volume Jacobian is `(a-b)/sqrt(2)`. Thus for any projected density `g` and `u,h>=0`, the upper-branch contribution to `P(q in [-u-h,-u])` equals

`(1/(2sqrt(2))) integral_{s=u}^{u+h} integral_0^{2pi} integral_{a>=sqrt(s/2)} (1-s/(2a^2)) g(a n_+(theta) + (s/(2a)) n_-(theta)) da dtheta ds`,

where `n_+=(e_theta+e3)/sqrt(2)` and `n_-=(-e_theta+e3)/sqrt(2)`. The lower branch has the analogous sign-reversed formula.

Equivalently, for any fixed `theta0`, in the orthonormal null coordinates `(A,B,W)` one has the exact identity

`q = W^2 - 2AB`.

Hence one branch of the negative interval event is, line-by-line in the null direction `A`,

`A in [(W^2+u)/(2B), (W^2+u+h)/(2B)]`, `B>0`.

The complete-line marginal `m(B,W)=integral G(A,B,W)dA` is bounded by `2`, but this controls only the whole null line. The required linear-in-`h` estimate is a weighted *local segment* (Carleson) estimate at length `h/(2B)`. Replacing that local segment by the unrestricted full-line supremum loses the `h` factor and is exactly the invalid move ruled out by the existing `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction.

The precise missing factor is therefore not ordinary X-ray control: it is product-provenance control of reciprocal-shear null-line segment mass, uniformly after integrating over `(B,W)`. This is the next target.

## Partner application

Apply account03/B05 r20 `QFORM-HS-LINEAR-SMALLBALL-v1` to the two transverse null coordinates `(B,W)`, which form a `2 x n` orthonormal linear image of the original product vector. Since its Hilbert--Schmidt norm is `sqrt(2)`, the partner theorem gives

`sup_z P(||(B,W)-z||_2 <= rho) <= min(1, C_HS rho/sqrt(2))`.

The pinned two-dimensional marginal-density theorem actually gives the stronger small-radius estimate `<=2 pi rho^2`. Thus transverse small-ball control is already paid; the unresolved loss is genuinely longitudinal localization along `A` at the reciprocal length `h/(2|B|)`, not a missing coarse small-ball estimate.
