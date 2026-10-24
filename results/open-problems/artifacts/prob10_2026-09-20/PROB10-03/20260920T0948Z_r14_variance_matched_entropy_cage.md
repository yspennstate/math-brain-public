# PROB10-03 / R14 — variance-matched entropy cage for the third-full c-sector

Status: **PROVED ANALYTICAL REDUCTION / NO SOURCE ENDPOINT PROMOTED**.  
Frozen model: `kappa=-1`, `M=floor(alpha N)`, `g_a iid N(0,I_N)`, `||sigma||_2=sqrt(N)` exactly, and `<g_a,sigma> >= -sqrt(N)` for all `a<=M`.  
Probability convention: a lower endpoint means SAT probability tends to one; an upper endpoint means SAT probability tends to zero as `N->infinity` at fixed `alpha`.

This note is written **before** the checker. It responds to the named third-full obstruction in the current R14/NM13 chain: the two nested Gaussian KL terms in the `c2,c3` stationarity equations are still the difficult part of an outward interval certificate near the numerical third-full capacity point.

## 1. Consumed state and motivation

The current projective third-full chart uses

`w0=1-p2`, `w1=p2-p3`, `w2=p3`,

`x=r0 r2/r1^2 > 1`, `y=r1/r2 > 1`,

`Z=x y^2 w0+y w1+w2`,

and gives

`q3=w2/Z`, `q2=(y w1+w2)/Z`,

`A_c3 = w1/(2Z) [w2+w1 k(y)]`,

`A_c2 = w0/2 [1-(x y^2 w0/Z) h(x)]`,

where

`k(y)=y(y log y-y+1)/(y-1)^2`,

`h(x)=x(x-1-log x)/(x-1)^2`.

The companion transport/LSI cage gives, at every full stationary point,

`w1 q3/2 <= A_c3 <= w1 q2/2`,

`w0 q2/2 <= A_c2 <= w0/2`.

The first task of this note is to test the negation: does that cage actually remove any point of the strict projective overlap cone?

## 2. Obstruction theorem: the old algebraic transport cage is automatic

### Theorem R14-T03-PROJECTIVE-CAGE-TAUTOLOGY

For every `x>1`, `y>1`, and every `w0,w1,w2>0` with `w0+w1+w2=1`, the projective c-sector formulas automatically satisfy

`w1 q3/2 < A_c3 < w1 q2/2`,

`w0 q2/2 < A_c2 < w0/2`.

Hence the purely algebraic inequalities obtained from the first Gaussian transport/LSI cage do **not** prune the strict projective cone at all. Their value is consistency checking, not root isolation.

### Proof

For `y>1`, convexity of `t log t-t+1` and `log y<y-1` give

`0 < y log y-y+1 < (y-1)^2`.

Therefore

`0<k(y)<y`.

Using `q3=w2/Z` and `q2=(y w1+w2)/Z`,

`A_c3-w1 q3/2 = w1^2 k(y)/(2Z) > 0`,

`w1 q2/2-A_c3 = w1^2 [y-k(y)]/(2Z) > 0`.

For `x>1`, `log x<x-1` gives `h(x)>0`. Also

`h(x)<1`

is equivalent to

`x(x-1-log x)<(x-1)^2`,

or `x log x-x+1>0`, again true for `x>1`. Thus `0<h(x)<1`. Put

`a=xy^2 w0/Z = 1-q2`, so `0<a<1`. Then

`A_c2-w0 q2/2 = (w0 a/2)[1-h(x)]>0`,

`w0/2-A_c2 = (w0 a/2)h(x)>0`.

This proves the theorem. QED.

**Consequence.** Repeating the old transport/LSI pruning on smaller boxes cannot be the next method. A genuinely stronger information-theoretic inequality must retain more than the mean/Fisher information used by the coarse cage.

## 3. New general lemma: match the Gaussian mean and variance first

Let `gamma=N(0,1)`. Let `nu` be an absolutely continuous probability on `R` with finite second moment and finite relative Fisher information

`I(nu|gamma)=E_nu[(d/dx log(dnu/dgamma))^2]`.

Write

`mu=E_nu X`, `v=Var_nu(X)>0`,

and define the Gaussian moment cost

`G(mu,v)=1/2 [mu^2+v-1-log v]`.

### Theorem R14-T03-VARIANCE-MATCHED-KL-FISHER

With

`J = I(nu|gamma)-mu^2-(v-1)^2/v`,

one has `J>=0` and the two-sided bound

`boxed:  G(mu,v) <= KL(nu||gamma) <= G(mu,v)+(v/2) J`.      (3.1)

The lower and upper bounds coincide when `nu` itself is Gaussian.

### Proof

Let `gamma_{mu,v}=N(mu,v)`. The log-density ratio between `gamma_{mu,v}` and `gamma` is affine-quadratic, and matching the first two moments gives the exact Pythagorean decomposition

`KL(nu||gamma)=KL(nu||gamma_{mu,v})+KL(gamma_{mu,v}||gamma)`

`              =KL(nu||gamma_{mu,v})+G(mu,v)`.              (3.2)

This immediately proves the lower bound.

For Fisher information, write

`r=d/dx log(dnu/dgamma_{mu,v})`,

`ell=d/dx log(dgamma_{mu,v}/dgamma)`.

The function `ell` is affine. Because `gamma_{mu,v}` matches the mean and variance of `nu`, integration by parts gives

`E_nu r=0`, `E_nu[(X-mu) r]=0`.

Hence `r` is orthogonal in `L^2(nu)` to the affine function `ell`, so

`I(nu|gamma)=I(nu|gamma_{mu,v})+E_nu ell^2`

`             =I(nu|gamma_{mu,v})+mu^2+(v-1)^2/v`.          (3.3)

Thus `J=I(nu|gamma_{mu,v})>=0`.

Apply the one-dimensional Gaussian log-Sobolev inequality with reference measure `gamma_{mu,v}`:

`KL(nu||gamma_{mu,v}) <= (v/2) I(nu|gamma_{mu,v})=(v/2)J`.

Combine this with (3.2). QED.

Compared with the ordinary Gaussian LSI bound `KL<=I/2`, (3.1) uses the exact mean and variance first and applies LSI only to the non-Gaussian remainder. For the present tilted laws the variance is substantially below one on the active region, so this is a materially stronger cage.

## 4. Exact variance identities for the two perceptron tilts

Use the strict complete-third notation

`m=c3/c2 in (0,1)`, `B=c2/(4 gamma_sq)`,

`s^2=1-p2`, `d^2=p2-p3`,

`X=d U+sqrt(p3)V-1`,

`f(x)=E_H exp[-B(x+sH)_+^2]`, `u(x)=log f(x)`.

For fixed `V=v`, let `nu_v` be the tilted `U` law with density proportional to `exp[m u(X)]`. For fixed `x`, let `rho_x` be the tilted `H` law with density proportional to `exp[-B(x+sH)_+^2]`.

### Lemma R14-T03-INNER-MOMENTS

For `rho_x`, exactly

`mu_H(x)=E_rho H = s u_x(x)`,

`v_H(x)=Var_rho(H)=1+s^2 u_xx(x)`,

`I_H(x)=I(rho_x|gamma_H)=-4 B^2 s^2 u_B(x)`.

Moreover, with `A=1+2Bs^2`, the already-proved kernel curvature bound

`-2B/A <= u_xx <= 0`

implies

`1/A <= v_H(x) <= 1`.                                       (4.1)

#### Proof

The relative score is `-2Bs(x+sH)_+`. Gaussian integration by parts gives

`E_rho H=s u_x`.

A second integration by parts gives the general exponential-tilt identity

`Var_rho(H)=1+E_rho k_HH+Var_rho(k_H)`

for `k(H)=-B(x+sH)_+^2`. Equivalently, differentiating `E_rho H=s u_x` with respect to a linear Gaussian shift yields

`Var_rho(H)=1+s^2 u_xx`.

Finally the square of the relative score is

`4B^2 s^2 E_rho[(x+sH)_+^2] = -4B^2s^2 u_B`.

The variance bounds follow from the kernel curvature theorem. QED.

### Lemma R14-T03-OUTER-MOMENTS

For fixed `v`, abbreviate tilted expectation under `nu_v` by `<.>_v`. Then exactly

`mu_U(v)=m d <u_x>_v`,

`v_U(v)=1+m d^2 <u_xx>_v + m^2 d^2 Var_v(u_x)`,

`I_U(v)=m^2 d^2 <u_x^2>_v`.                                 (4.2)

Furthermore `0<v_U(v)<=1`. If `L=2B/(1+2Bs^2)`, then

`v_U(v) >= 1/(1+m d^2 L)`.                                  (4.3)

#### Proof

The relative log-density is `h(U)=m u(dU+sqrt(p3)v-1)-log Z_v`; its score is `h'=m d u_x`. Gaussian integration by parts yields `E U=E h'=m d<u_x>`. Applying the same identity a second time,

`Var(U)=1+E h''+Var(h')`

`      =1+m d^2<u_xx>+m^2d^2 Var(u_x)`.

The Fisher identity is immediate from `I=E(h')^2`.

Since `u` is concave, `h` is concave and the tilted potential `U^2/2-h(U)` is 1-strongly convex; Brascamp--Lieb gives `v_U<=1`. Positivity is automatic because it is a variance. For the quantitative lower bound, the kernel semiconvexity gives `-L<=u_xx<=0`, hence the tilted potential has second derivative at most `1+m d^2L`. In one dimension, if a normalized density is `e^{-V}` and `V''<=C`, then `Var(X)>=1/C`: integration by parts gives `Cov(X,V')=1`, Cauchy--Schwarz gives `Var(X) E(V')^2>=1`, and another integration by parts gives `E(V')^2=E V''<=C`. This proves (4.3). QED.

## 5. New c-sector cage with no direct KL evaluation

Define, pointwise,

`G_U(v)=G(mu_U(v),v_U(v))`,

`J_U(v)=I_U(v)-mu_U(v)^2-(v_U(v)-1)^2/v_U(v)`,

and

`G_H(x)=G(mu_H(x),v_H(x))`,

`J_H(x)=I_H(x)-mu_H(x)^2-(v_H(x)-1)^2/v_H(x)`.

Then `J_U,J_H>=0`, and Theorem (3.1) gives

`boxed:`

`E_V G_U(V) <= D_U <= E_V [G_U(V)+(v_U(V)/2)J_U(V)]`,        (5.1)

`boxed:`

`m E_V <G_H(X)>_V <= D_H`

` <= m E_V <G_H(X)+(v_H(X)/2)J_H(X)>_V`.                    (5.2)

At a full stationary point these become the c-sector residual cages

`alpha/c3^2 * (left side of 5.1) <= A_c3 <= alpha/c3^2 * (right side of 5.1)`,

`alpha/(c2 c3) * (left side of 5.2) <= A_c2 <= alpha/(c2 c3) * (right side of 5.2)`.

Unlike the old algebraic cage, these bounds are **not** tautologies in `(w0,w1,w2,x,y)`: they retain the variance deficit of the actual tilted Gaussian laws. They also avoid direct KL/log-partition subtraction. The required quantities are the already-available one-step moments `u_x,u_xx,u_B` and the outer first/second score moments.

This is the proposed certification route for the next third-full interval box: use (5.1)--(5.2) first to prune and sign c-sector faces; evaluate the exact entropy only if the refined cage still straddles zero on the final surviving box.

## 6. Numerical-only falsification scout at the supported third-full point

For the NM13-03 GH240 supported point near `alpha=12.2872223`, the previously reported exact-KL numerical values are

`D_U ~= 0.04498795676177`,

`D_H ~= 0.03519830974786`.

A separate Gauss--Hermite scout using the closed one-step kernel gives, at order 120,

old transport/LSI cage:

`0.0283072730 <= D_U <= 0.0790229969`,

`0.0301469922 <= D_H <= 0.0472200078`;

new variance-matched cage:

`0.0408919618 <= D_U <= 0.0555555182`,

`0.0346054428 <= D_H <= 0.0367728964`.

Thus the new cage contains the independently computed KL values while shrinking the numerical cage width by about `71.1%` for `D_U` and `87.3%` for `D_H`. This is **NUMERICAL ONLY** and is not a source endpoint or an outward interval certificate. Its role is to falsify gross sign/algebra mistakes and quantify whether the new theorem addresses the actual bottleneck.

## 7. Source-level status and remaining gap

No source endpoint is promoted by this note. The current repository-supported bracket entering this iteration is

`alpha_L=6.30297437506`,

`alpha_U=12.3196348278`,

width `6.01666045274`,

where the upper endpoint is inherited from the newest NM13-07 complete-second directed continuation and is not attributed to R14.

The supported third-full capacity zero near `12.28722222...` remains conditional. To move the source upper endpoint materially, the remaining full-scope obligation is an outward interval/Krawczyk (or equivalent) certificate for a strict complete-third stationary point with positive comparison value. The new theorem replaces the direct nested KL bottleneck by variance/Fisher moments with explicit positive variance domains, but it does not itself prove the root exists.

The exact target remains **OPEN / PARTIAL** until the full proof and repository-required independent validation are complete.
