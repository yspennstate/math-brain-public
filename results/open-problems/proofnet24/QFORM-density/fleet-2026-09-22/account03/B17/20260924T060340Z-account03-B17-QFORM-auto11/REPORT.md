# QFORM minority-axis noncentral rigidity and diffuse-bank transfer

Run: `20260924T060340Z-account03-B17-QFORM-auto11`  
Worker: `account03/B17`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: supporting theorem; FULL QFORM remains OPEN.

## Exact target context

The unrestricted target is: for independent real `X_i` with probability densities `0<=f_i<=1` and real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal bound on the essential supremum of the density of `X^T A X`, or give a counterexample. No rotation of the input coordinates is allowed to manufacture independence. The present report does **not** solve that target. It closes a concrete negative-two-sheet/off-tip witness mechanism and gives a source-valid finite cap-one transfer.

The live corrections consumed here include the failure of law-uniform pointwise quadratic van der Corput decay, the failure of arbitrary-joint rank-three coarea as a universal interface, the failure of positive conditional projection-density moments, and the dimension loss of naive fiber-sup integration. None of those statements is used below.

## Theorem 1: exact noncentral Gaussian minority-axis bound

Let `s>0`, `c>0`, let

`G_1,G_2 ~ N(0,s)`, `G_3 ~ N(a,s)`

be independent, and put

`Q = G_1^2 + G_2^2 - c G_3^2`.

Set

`alpha = 1+c`, `b = a/sqrt(2 s alpha)`.

Then `Q` has a continuous density. For `q>=0`,

`p_Q(q) = [1/(2 s sqrt(alpha))] exp[-q/(2s)-c b^2]`.

For `q=-r<0`, define

`y = sqrt(alpha r/(2 c s))`.

Then

`p_Q(-r) = [1/(2 s sqrt(alpha))] R_c(y,b)`,

where

`R_c(y,b) = (1/2) exp[(c/alpha)y^2-c b^2] [erfc(y-b)+erfc(y+b)]`.

For every `y,b>=0`,

`R_c(y,b) <= 1`.

Consequently

`||p_Q||_infinity <= 1/(2 s sqrt(1+c))`,

and equality is attained when `a=0` at `q=0`. If `a!=0`, the inequality is strict.

This proves that moving the Gaussian mean along the minority-sign eigendirection cannot create a negative two-sheet off-tip peak above the centered cone-tip value.

### Proof

Let `U=G_1^2+G_2^2`. Since two centered equal-variance Gaussian squares form a scaled chi-square with two degrees of freedom,

`f_U(u)=(2s)^(-1) exp[-u/(2s)] 1_{u>=0}`.

For `q>=0`, conditioning on `G_3` gives

`p_Q(q)=(2s)^(-1) exp[-q/(2s)] E exp[-c G_3^2/(2s)]`.

Completing the square in the Gaussian expectation yields

`E exp[-c G_3^2/(2s)] = alpha^(-1/2) exp[-c a^2/(2s alpha)] = alpha^(-1/2) exp[-c b^2]`,

which is the first formula.

For `q=-r<0`,

`p_Q(-r)=(2s)^(-1) exp[r/(2s)] E[exp(-cG_3^2/(2s)); cG_3^2>=r]`.

Combining the Gaussian density with the extra exponential gives

`c x^2+(x-a)^2 = alpha (x-a/alpha)^2 + c a^2/alpha`.

With

`u=sqrt(alpha/(2s))(x-a/alpha)`,

and `y,b` as above, the two tails `x>=sqrt(r/c)` and `x<=-sqrt(r/c)` become `u>=y-b` and `u<=-y-b`. The stated `erfc` formula follows.

It remains to prove the uniform bound. First,

`erfc(y-b)+erfc(y+b) <= 2`

for `y,b>=0`: equivalently `erf(y-b)+erf(y+b)>=0`, which follows from oddness and monotonicity of `erf`.

If `y<=sqrt(alpha)b`, then

`(c/alpha)y^2-cb^2 <=0`,

so directly `R_c(y,b)<=1`.

If `y>sqrt(alpha)b`, then `y>b`. Use the elementary bound `erfc(x)<=exp(-x^2)` for `x>=0`. The two exponential terms become exactly

`exp[(c/alpha)y^2-cb^2-(y-b)^2] = exp[-(y/sqrt(alpha)-sqrt(alpha)b)^2]`,

`exp[(c/alpha)y^2-cb^2-(y+b)^2] = exp[-(y/sqrt(alpha)+sqrt(alpha)b)^2]`.

Each is at most one, hence `R_c(y,b)<=1`. For `b>0`, equality cannot occur in either region, so the global bound is strict.

## Quantitative strictness envelope

The preceding proof gives an explicit loss for `b>0`. Define

`H_c(b)=sup_{y>=0} R_c(y,b)`.

For `alpha=1+c`,

`H_c(b) <= max{ A_1,A_2,A_3 }`,

where

`A_1 = exp[-c^2 b^2/alpha]`,

`A_2 = exp[-(sqrt(alpha)-1)^2 b^2]`,

`A_3 = (1/2)[1+exp(-(1+sqrt(alpha))^2 b^2)]`.

Indeed:

* on `0<=y<=b`, use the `erfc` sum <=2 and maximize the exponent;
* on `b<=y<=sqrt(alpha)b`, both `erfc` arguments are nonnegative, use `erfc(x)<=e^{-x^2}` and the first completed square;
* on `y>=sqrt(alpha)b`, put `z=y/sqrt(alpha)>=b`; the first completed-square exponential is <=1 and the second is <=`exp[-(1+sqrt(alpha))^2b^2]`.

The `q>=0` branch is already covered because its ratio to the centered peak is `exp(-cb^2)<=A_1`.

For the concrete sharp-scale choice `c=1`, `a=sqrt(s)`, one has `b=1/2`. Then the largest of these three bounds is

`A_2 = exp[-(3-2sqrt(2))/4]`,

so

`||p_Q||_infinity <= [1/(2sqrt(2)s)] exp[-(3-2sqrt(2))/4]`.

At `s=1/12`, this is

`||p_Q||_infinity <= 3sqrt(2) exp[-(3-2sqrt(2))/4] = 4.064507827950592...`.

The point is not the decimal but the strict analytic factor.

## Theorem 2: exact source-valid diffuse-bank transfer

Let `s=1/12` and `a=sqrt(s)=1/sqrt(12)`. For every integer `m>=2`, let all `3m` physical inputs be independent, with

`X_{1k},X_{2k} ~ Unif[-1/2,1/2]`,

`X_{3k} ~ Unif[a/sqrt(m)-1/2, a/sqrt(m)+1/2]`.

Every marginal density is exactly one on an interval of length one. Define normalized bank sums

`Y_{j,m}=m^(-1/2) sum_{k=1}^m X_{jk}`

and `c_m=1+1/m`. Set

`Q_m=Y_{1,m}^2+Y_{2,m}^2-c_m Y_{3,m}^2`.

Equivalently, with `J_m` the all-ones `m x m` matrix,

`A_m = diag(J_m/m, J_m/m, -c_m J_m/m)`.

Thus the exact nonzero spectrum of the physical `3m x 3m` matrix is

`{1,1,-(1+1/m)}`,

so every finite member satisfies the owner's three-large-eigenvalue hypothesis. For `m>=2` this is genuinely non-diagonal in the original independent coordinates: each bank contains all pairwise cross terms.

Then `Q_m` has a continuous density `p_m`, and

`p_m -> p_infinity` uniformly on the whole real line,

where `p_infinity` is the density from Theorem 1 with `c=1`, `s=1/12`, `a=1/sqrt(12)`. In particular,

`limsup_{m->infinity} ||p_m||_infinity <= 3sqrt(2) exp[-(3-2sqrt(2))/4] = 4.064507827950592... < 3sqrt(2)`.

Hence a fixed minority-axis noncentral drift does **not** generate a sharper source-valid witness in the diffuse three-bank regime; it creates a strict asymptotic deficit.

### Proof of uniform density convergence

Write

`Z_m=m^(-1/2) sum_{k=1}^m U_k`, `U_k~Unif[-1/2,1/2]`.

Its density `g_m` is symmetric, log-concave and therefore unimodal. There is an absolute bound on `||g_m||_infinity` for all `m>=2`. A self-contained crude bound suffices. Since

`E exp(itZ_m)=sinc(t/(2sqrt(m)))^m`,

Fourier inversion and `|sinc u|<=exp(-u^2/6)` for `|u|<=1`, `|sinc u|<=|u|^(-1)` for `|u|>1`, give

`||g_m||_infinity=g_m(0)`

`<= sqrt(m)/pi * integral_R |sinc u|^m du`

`<= sqrt(6/pi) + 2sqrt(m)/(pi(m-1)) < 2.3`.

Now use the following interval-layer lemma. If `h` is any nonnegative unimodal probability density with `||h||_infinity<=M`, then for `t!=0`,

`| integral exp(itx^2)h(x)dx | <= 4M |t|^(-1/2)`.

Indeed, the layer-cake superlevel sets of `h` are intervals. For every interval `I`, scaling followed by one integration by parts outside `[-1,1]` gives

`|integral_I exp(itx^2)dx| <= 4|t|^(-1/2)`.

Integrate this estimate over the layer parameter from zero to `||h||_infinity`. Translation of `h` does not affect the argument because its superlevel sets remain intervals.

Let

`F_m(t)=E exp(it Z_m^2)`,

`G_m(t)=E exp(-it c_m(a+Z_m)^2)`.

The characteristic function of `Q_m` is `Phi_m(t)=F_m(t)^2G_m(t)`. With one common `M<2.3`, the interval-layer lemma and `c_m>=1` yield the integrable, `m`-independent envelope

`|Phi_m(t)| <= min{1,(4M)^3 |t|^(-3/2)}`.

By the ordinary CLT, `Z_m` converges in distribution to `N(0,1/12)`, while `c_m->1`; hence `Phi_m(t)` converges pointwise to the characteristic function `Phi_infinity(t)` of the Gaussian limit in Theorem 1. Dominated convergence therefore gives

`||Phi_m-Phi_infinity||_{L^1(R)} ->0`.

Fourier inversion now gives bounded continuous densities and

`||p_m-p_infinity||_infinity <= (2pi)^(-1)||Phi_m-Phi_infinity||_1 ->0`.

Taking suprema proves the claim.

This is an integrated-Fourier argument for a specific smooth bank family; it does not assert the refuted law-uniform pointwise quadratic decay for arbitrary cap-one laws.

## Exact fully dense Gaussian stress family (secondary control)

Theorem 1 itself also gives an exact finite, fully dense target family with original-coordinate independence. Let

`n=(1,2,3)/sqrt(14)`, `B_c=I-(1+c)nn^T`,

so `spec(B_c)={1,1,-c}` and, for `c` near one, every matrix entry is nonzero. Let `X~N(an,sI_3)`. Its physical coordinates are independent. If `s>=1/(2pi)`, every marginal Gaussian density is <=1. Since the mean lies exactly along the negative eigenvector,

`||p_{X^T B_c X}||_infinity <= 1/(2s sqrt(1+c))`,

with the stricter `H_c(b)` factor when `a!=0`. Thus noncentrality in the dangerous two-sheet direction is not a source of blow-up even in an exact entrywise-dense original-coordinate family.

This control is not sharp for the universal constant because the density-one Gaussian constraint forces `s>=1/(2pi)>1/12`; the diffuse-bank transfer above is what reaches the sharp variance scale allowed by cap-one laws.

## Application of completed partner account04/B17 result

The completed partner result `QFORM-MACROFRAGMENTED-STRICTSLACK-DENSE-WITNESS-v1` is recorded at

`yspennstate/math-open-problems@4be63022324b82f254f1d7a4353a3e883f08d10a`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260924T011922Z-account04-B17-QFORM-r6/REPORT.md`.

It constructs an entrywise-dense exact-target family with the **same exact spectrum**

`{1,1,-(1+1/m)}`

and, for every admissible `theta`,

`liminf ||p_Q||_infinity >= 3sqrt(2) exp(-3theta)`.

Take `theta=1/100`. Then the partner theorem gives

`liminf ||p_Q^(partner)||_infinity >= 3sqrt(2)e^(-3/100)=4.117251705266084...`.

Our axial-drift diffuse-bank family gives

`limsup ||p_Q^(axial)||_infinity <= 3sqrt(2)e^{-(3-2sqrt(2))/4}=4.064507827950592...`.

The comparison is analytically strict because

`(3-2sqrt(2))/4 > 3/100`.

Indeed this is equivalent to `72>50sqrt(2)`, and squaring the positive sides gives `1296>1250`.

Therefore

`liminf ||p_Q^(partner)||_infinity > limsup ||p_Q^(axial)||_infinity`,

with certified numerical separation about `0.0527438773`.

This is a concrete mechanism comparison at identical three-eigenvalue spectra: remote fragmented non-Gaussian structure can retain a peak that a fixed minority-axis noncentral drift in a diffuse-bank CLT architecture provably cannot match. It does not imply that the partner family exceeds `3sqrt(2)`; it does not.

## What this constrains

The result removes one plausible negative-two-sheet witness route. In the sharp rank-three `(+,+,-)` diffuse regime, merely translating the limiting mass along the minority-sign direction cannot create an off-tip peak above the centered `3sqrt(2)` obstruction. The exact Gaussian density formula shows how the two-sheet tail is suppressed, and the finite cap-one bank theorem shows the conclusion is not an artifact of inserting Gaussian physical inputs.

A witness above `3sqrt(2)`, if one exists, must therefore use a mechanism not captured by this fixed axial noncentral diffuse limit: for example a genuinely surviving non-Gaussian component, non-collinear macroscopic shared rows, an off-axis translation coupled to anisotropy, or additional active spectrum.

## Status and continuity

* FULL QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
* Universal lower obstruction remains `C_*>=3sqrt(2)` from previously completed source-valid diffuse witnesses; this run does not raise it.
* Theorem 1 gives a continuous density.
* The finite bank family in Theorem 2 has a bounded continuous density for every `m>=2` by the `L^1` characteristic-function argument.
* Full-target continuity remains OPEN.
* No Monte Carlo histogram or interval-extremality assumption is used.
* No independence after a general rotation is assumed.
