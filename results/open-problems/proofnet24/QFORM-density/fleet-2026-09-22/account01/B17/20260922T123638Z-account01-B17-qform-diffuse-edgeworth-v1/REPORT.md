# Diffuse periodic cube frames approach the Gaussian lower-bound ceiling from below

Programme: QFORM-DENSITY-3EIG-20260922
Worker: account01/B17
Run: 20260922T123638Z-account01-B17-qform-diffuse-edgeworth-v1
Classification: AUXILIARY_ONLY / SHARP_WITNESS_CONSTRAINT
Full conjecture: OPEN / NOT PROVED

## 1. Statement

Let `J=diag(1,1,-1)`. Fix vectors `v_1,...,v_r in R^3` spanning `R^3` and satisfying

`sum_{j=1}^r v_j v_j^T = I_3`.

For each integer `m>=1`, repeat this row pattern `m` times and define an `rm x 3` matrix `U_m` whose row indexed by `(g,j)` is `v_j/sqrt(m)`. Then `U_m^T U_m=I_3`, so

`A_m = U_m J U_m^T`

has eigenvalues `+1,+1,-1` and all remaining eigenvalues zero.

Let the physical coordinates be independent `X_{g,j} ~ Uniform[-1/2,1/2]`, and put

`Q_m = X^T A_m X`.

Write, for `v=(v_1,v_2,v_3)`,

`s(v)=v_1^2+v_2^2`, `t(v)=v_3^2`,

and

`E_J(v) = (57/32)s(v)^2 + (15/4)s(v)t(v) + (3/4)t(v)^2`.

Then, as `m -> infinity`, the density of `Q_m` exists near zero and

`p_{Q_m}(0) = 3 sqrt(2) [ 1 - (1/(20m)) sum_j E_J(v_j) + O(m^{-2}) ].`

In particular the first non-Gaussian correction is strictly negative for every fixed spanning pattern. Thus every fixed-pattern periodic diffuse cube-frame witness approaches the Gaussian value `3 sqrt(2)` from below.

Moreover

`E_J(v) >= (3/4)||v||_2^4`,

hence, since `sum_j ||v_j||_2^2 = 3`,

`sum_j E_J(v_j) >= 27/(4r)`

and therefore

`p_{Q_m}(0) <= 3 sqrt(2) [1 - 27/(80 r m) + O(m^{-2})]`.

Equivalently, with `n=rm`, the universal first-order relative deficit is at least `27/(80n)` inside this periodic family.

This does NOT prove a universal upper bound for arbitrary bounded-density product inputs. It rules out a broad diffuse finite-size mechanism for exceeding the already-proved lower-bound ceiling `3 sqrt(2)`.

## 2. Standardization

Set `xi=sqrt(12) X`, so `xi ~ Uniform[-sqrt(3),sqrt(3)]`,

`E xi=0`, `E xi^2=1`, `cum_4(xi)=-6/5`.

For one pattern block define

`W = sum_j v_j xi_j`.

Then `Cov(W)=sum_j v_j v_j^T=I_3`. With iid blocks `W_1,...,W_m`,

`Z_m = m^{-1/2} sum_{g=1}^m W_g`

satisfies

`Q_m = (1/12) Z_m^T J Z_m`.

The block law is compactly supported and nonlattice; because the fixed vectors span `R^3`, a standard multivariate density Edgeworth expansion applies. Symmetry kills all odd cumulants. To first order,

`f_m(z)=phi_3(z) [1 + (kappa_4/(24m)) sum_j H_{4,v_j}(z)] + O(m^{-2})`,

in a norm strong enough to integrate over the quadratic level surface, where `kappa_4=-6/5` and

`H_{4,v}(z)=(v.z)^4 - 6||v||^2(v.z)^2 + 3||v||^4`.

The remainder statement can also be obtained directly from the characteristic function product because the summands are bounded and the pattern is fixed: the sixth-cumulant and square-of-fourth-cumulant terms enter at order `m^{-2}`.

## 3. Exact cone calculation

Let `G~N(0,I_3)`, `T=G_1^2+G_2^2-G_3^2`. Its density at zero is

`p_T(0)=1/(2 sqrt(2))`.

Normalize the Gaussian cone measure

`dmu(z) = [delta(z_1^2+z_2^2-z_3^2) phi_3(z) dz] / p_T(0)`.

Parametrize the cone by

`z=(r cos theta, r sin theta, eps r)`,

with `theta` uniform on `[0,2pi)`, `eps` uniform on `{+1,-1}`, and radial density proportional to `exp(-r^2)` on `r>=0`. Hence

`E_mu r^2=1/2`, `E_mu r^4=3/4`.

For `v=(a,b,c)`, set `s=a^2+b^2`, `t=c^2`. Averaging over `theta,eps` gives

`E_mu (v.z)^2 = s/4 + t/2`,

`E_mu (v.z)^4 = 9 s^2/32 + 9 st/4 + 3 t^2/4`.

Therefore

`E_mu H_{4,v}(Z)`
`= E(v.z)^4 - 6(s+t)E(v.z)^2 + 3(s+t)^2`
`= 57 s^2/32 + 15 st/4 + 3 t^2/4`
`= E_J(v)`.

Since `kappa_4/24=(-6/5)/24=-1/20`, integrating the first Edgeworth correction over the cone yields

`p_{Z_m^T J Z_m}(0)`
`= (1/(2sqrt(2))) [1 - (1/(20m)) sum_j E_J(v_j) + O(m^{-2})]`.

Finally `Q_m=(1/12) Z_m^T J Z_m`, so density scaling multiplies the value at zero by 12 and gives

`p_{Q_m}(0)=3sqrt(2)[1-(1/(20m))sum_j E_J(v_j)+O(m^{-2})]`.

## 4. Positivity and universal orientation bound

Writing `h=s+t=||v||^2` and `x=t/h` for `h>0`,

`E_J(v)/h^2 = (57/32)(1-x)^2 + (15/4)x(1-x) + (3/4)x^2`.

This concave quadratic has its minimum on `[0,1]` at an endpoint, and the smaller endpoint value is `3/4`. Thus

`E_J(v) >= (3/4)||v||^4`.

Since `sum_j ||v_j||^2 = tr(sum_j v_j v_j^T)=3`, Cauchy gives

`sum_j ||v_j||^4 >= 9/r`,

hence

`sum_j E_J(v_j) >= 27/(4r)`.

The first correction is therefore negative for every pattern and quantitatively bounded away from zero at fixed `r`.

## 5. Two canonical families

### 5.1 Three disjoint averaging blocks

Take `r=3`, `v_1=e_1`, `v_2=e_2`, `v_3=e_3`. Then

`sum_j E_J(v_j)=2*(57/32)+3/4=69/16`,

so

`p_{Q_m}(0)=3sqrt(2)[1-69/(320m)+O(m^{-2})]`.

This matches direct numerical evaluation of the exact Irwin-Hall block-sum densities (for example the `m=10` prediction is already accurate at the fourth decimal place).

### 5.2 Four-row Hadamard pattern

Take

`v_1=(1,1,1)/2`, `v_2=(1,-1,1)/2`,
`v_3=(1,1,-1)/2`, `v_4=(1,-1,-1)/2`.

Then `sum_j v_jv_j^T=I_3`, and every row has `s=1/2`, `t=1/4`. Hence

`E_J(v_j)=123/128`, `sum_j E_J(v_j)=123/32`,

and for `n=4m`

`p_{Q_m}(0)=3sqrt(2)[1-123/(640m)+O(m^{-2})]`
`=3sqrt(2)[1-123/(160n)+O(n^{-2})]`.

Thus the Sylvester-Hadamard diffuse family also approaches `3sqrt(2)` from below.

## 6. Source-bound consequence

Earlier account02/B17 work proved the target-level lower bound `C>=3sqrt(2)` from disjoint uniform block averages, and the preceding account01/B17 run proved that `3sqrt(2)` is the exact ceiling for every Gaussian projection-limit mechanism under the density-one variance floor. The present theorem shows more: for every fixed periodic cube frame, the leading non-Gaussian finite-size correction has the WRONG sign for producing a larger witness.

Therefore a witness with density peak strictly above `3sqrt(2)` cannot arise as a small finite-size perturbation of a fixed periodic diffuse uniform-cube frame. A successful witness must use a genuinely mesoscopic/nonperiodic frame, non-uniform density-one supports, or another mechanism outside this Edgeworth neighborhood.

## 7. Remaining target gap

The universal arbitrary-law, arbitrary-dimension quadratic-form density conjecture remains open. This report supplies only a sharp witness-side exclusion theorem. It neither proves `C=3sqrt(2)` nor gives an upper bound for general rotated product measures.

Dependencies consumed:
- account02/B17 lower-bound report: `yspennstate/math-open-problems@4a3d4af77778f20a95855c6dfbf69540dcfa5fe4`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T114529Z-qform-sharp-witness/REPORT.md`.
- account01/B17 Gaussian ceiling: `yspennstate/math-open-problems@cd6ae6f74d77c7090e8ba08101e916dfd0d8df15`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260922T120821Z-account01-B17-qform-sharp-constant-v1/ADDENDUM_NONCENTRAL_GAUSSIAN.md`.
- live brain control source at invocation start: `yspennstate/math-research-brain@e4218a319d6a7a51d55098fa961eaee67f5fc19d`, revision `2026-09-22.5`.

External theorem used only for the standard asymptotic justification: a classical multivariate Edgeworth expansion under Cramer/nonlattice conditions for iid bounded vectors. The coefficient and cone integral above are derived explicitly here.
