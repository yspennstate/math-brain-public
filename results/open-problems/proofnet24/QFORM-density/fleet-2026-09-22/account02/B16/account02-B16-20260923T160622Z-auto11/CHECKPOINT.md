# account02/B16 early checkpoint — hub-convolution cylinder and near-null log barrier

Programme `QFORM-DENSITY-3EIG-20260922`; owner revision `2026-09-22.15`. Full QFORM remains OPEN.

First unpaid implication attacked: retain the translating physical-hub source weight through the true-near-coloop shared-bank curved integral. A bounded two-dimensional transverse product marginal by itself is not enough after replacing that source weight by its height bound.

## Source-preserving cylinder domination

Write an exact-rank-three Parseval frame with a physical near-coloop row

`r_0=sqrt(c)e`, `0<c<=1`,

and residual rows `r_j=s_j e+w_j`, `w_j perpendicular e`. Parseval gives

`sum s_j^2=1-c`, `sum s_j w_j=0`, `sum w_j w_j^T=I_2`.

For independent cap-one inputs define

`S=sum s_j X_j`, `W=sum w_j X_j`, `Z=sqrt(c)X_0+S`.

For every nonnegative measurable `F`, conditioning on the residual product bank and changing variable `z=sqrt(c)x_0+S` gives

`E F(Z,W)
 =c^(-1/2) E_res int f_0((z-S)/sqrt(c)) F(z,W) dz
 <=c^(-1/2) int int F(z,w) p_W(w) dz dw`.

Thus, as measures,

`Law(Z,W) <= c^(-1/2) dz tensor Law(W)`.

Since the two columns `(w_j)` are orthonormal, the completed two-dimensional product-projection theorem in the pinned `e5f71d79...` package gives `||p_W||_infinity<=2`. No independence of the coordinates of `W` is inferred.

If in the spectral basis `(e,e^perp)`

`Lambda=[[a,b^T],[b,C]]`, `a!=0`,

then completing the scalar square and applying the domination above gives

`||p_Q||_infinity <= c^(-1/2)|a|^(-1/2) H_(1/2)(W^T(C-a^(-1)bb^T)W)`.

When `max_j ||w_j||^2<=1/2`, pinned Theorem F with rank two plus its fractional-potential Lemma 4.1 yields

`H_(1/2) <=8sqrt(2)|det(C-a^(-1)bb^T)|^(-1/4)`.

Using `det(C-a^(-1)bb^T)=det(Lambda)/a`,

`boxed: ||p_Q||_infinity <=8sqrt(2)c^(-1/2)|det Lambda|^(-1/4)|a|^(-1/4).`

This is a valid all-level bound on the non-null scalar branch, but it is deliberately not claimed uniform as `a->0`.

## Strict near-coloop shared-bank obstruction

Let `0<rho<1/64`, `c=1-rho`, let `m>=512` be divisible by four, and choose balanced sign pairs `(epsilon_j,tau_j)`. Put

`r_0=(sqrt(c),0,0)`,
`r_j=m^(-1/2)(sqrt(rho),epsilon_j,tau_j)`,

and for `eta>0`

`Lambda_eta=[[eta,sqrt(1+eta),0],[sqrt(1+eta),0,0],[0,0,1]].`

Then `R^T R=I_3` and the nonzero spectrum is exactly `{1+eta,-1,1}`. With

`L=m^(-1/2)sum X_j`, `U=m^(-1/2)sum epsilon_j X_j`, `T=m^(-1/2)sum tau_j X_j`,

`Q_eta=eta(sqrt(c)X_0+sqrt(rho)L)^2+2sqrt(1+eta)(sqrt(c)X_0+sqrt(rho)L)U+T^2.`

For small `eta` this lies inside the true near-coloop/superdiffuse physical regime: hub leverage `c>63/64`, transverse leaf leverage `2/m<1/64`, `A_00=c eta<1/64`, and `|A_0j|<1/16` for the displayed `m` scale.

The same cylinder domination followed by scalar square completion gives the translation-uniform envelope at level zero

`K_eta(0)=c^(-1/2) eta^(-1/2) E[(L_eta U^2-T^2)^(-1/2) 1_{L_eta U^2>T^2}]`,

where `L_eta=(1+eta)/eta`.

For iid `Unif[-1/2,1/2]` residual inputs, the genuine product-projection density `p_(U,T)` is continuous and bounded below by some `kappa_m>0` on a fixed square `|u|,|t|<=r_m`. With `y=sqrt(L_eta)u`, restrict to

`r_m/2<=t<=r_m`, `2r_m<=y<=(r_m/2)sqrt(L_eta)`.

There `1/sqrt(y^2-t^2)>=1/y`, so for all sufficiently small `eta`,

`K_eta(0)
 >= [kappa_m r_m/(2 sqrt(c) sqrt(1+eta))]
    log(sqrt(L_eta)/4)
 -> infinity.`

Thus even in a strict true-near-coloop target family, the operation

`exact hub convolution -> replace f_0 by height 1 -> two-dimensional transverse marginal -> scalar square coarea`

loses logarithmically. The obstruction is to that proof interface, not to QFORM.

The true density of the same family is uniformly bounded: regroup the four original sign banks exactly as in the completed account02/B16 source-plane/source-line compiler at `math-open-problems@612c5bfc1edc4c288cc52c5097db269910486ebd`. With the same coefficient matrix `P` (`det(P)^2=1/2`) and source-line vector `g=(sqrt(rho),1,-1)/2`,

`g^T Lambda_eta g=[1+eta rho+2sqrt(rho(1+eta))]/4>=1/4`,
`|det Lambda_eta|=1+eta>=1`.

The completed account03/B16 r27 dependence-preserving receiver therefore gives

`||p_(Q_eta)||_infinity <=2^(19/4)c^(-1/4)<27.015`,

uniformly in `eta>0`, `rho<1/64`, `m`, and all cap-one source laws. The pinned ruled theorem C additionally gives `p_Q(s)<=pi sqrt(2)` on its one-sheet side. Hence the logarithmic divergence is purely the cost of discarding the translating original-source factor.

Next unpaid implication: `QFORM-SUPERDIFFUSE-TRANSLATION-WEIGHT-TRANSDUCER-v1` — preserve `f_0((z-S)/sqrt(c))` (or an equivalent modulation) through the minority-sign curved integral and combine it with the dependent transverse two-dimensional product marginal, rather than normalizing/conditioning it away or replacing it by a height bound.
