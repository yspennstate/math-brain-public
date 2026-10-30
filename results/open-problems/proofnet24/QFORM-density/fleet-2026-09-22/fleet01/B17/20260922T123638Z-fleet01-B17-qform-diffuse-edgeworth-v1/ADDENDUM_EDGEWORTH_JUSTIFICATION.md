# Addendum: justification of the density Edgeworth expansion used in REPORT.md

This addendum supplies the analytic regularity point behind the first-order formula in the main report.

Let

`W = sum_{j=1}^r v_j xi_j`,

where the fixed vectors `v_j` span `R^3`, `xi_j` are independent `Uniform[-sqrt(3),sqrt(3)]`, and `sum_j v_j v_j^T=I_3`. Let `phi_W` be the characteristic function.

## 1. Cramer condition and Fourier integrability

The law of `W` is the pushforward of a bounded product density on `R^r` by a surjective linear map to `R^3`. Choosing any three linearly independent pattern vectors and conditioning on the remaining coordinates shows that `W` has a bounded compactly supported density `g`. Hence `g in L^1 cap L^2`, and by Plancherel `phi_W in L^2(R^3)`.

Also `g in L^1` implies `phi_W(t)->0` as `|t|->infinity` (Riemann-Lebesgue). Since the covariance is nonsingular, `|phi_W(t)|<1` for every nonzero `t`; by compactness, for every fixed `delta>0` there is `rho_delta<1` such that

`sup_{|t|>=delta} |phi_W(t)| <= rho_delta`

outside a sufficiently large compact set, and the same strict bound holds on compact annuli. Thus the ordinary Cramer condition holds.

The explicit product formula is

`phi_W(t)=prod_j sinc(sqrt(3) v_j.t)`.

## 2. Local logarithmic expansion

Because the inputs are symmetric and bounded, all odd cumulants vanish and the logarithm is analytic near zero. With standardized fourth cumulant `kappa_4=-6/5`,

`log phi_W(t) = -|t|^2/2 + (kappa_4/24) sum_j (v_j.t)^4 + O(|t|^6)`.

For `Z_m=m^{-1/2} sum_{g=1}^m W_g`,

`[phi_W(t/sqrt(m))]^m`
`= exp(-|t|^2/2) [1 + (kappa_4/(24m)) sum_j (v_j.t)^4 + O(m^-2 P(t))]`

uniformly on `|t|<=m^epsilon` for any fixed sufficiently small `epsilon>0`, with `P` a fixed polynomial times a Gaussian-dominated factor after shrinking the local radius.

Inverse Fourier transformation gives

`f_m(z)=phi_3(z)[1+(kappa_4/(24m)) sum_j H_{4,v_j}(z)] + R_m(z)`.

## 3. Remainder strong enough for cone integration

A standard Fourier split yields a polynomially weighted `O(m^-2)` remainder.

- On `|t|<=delta sqrt(m)`, the cumulant expansion above and the nonsingular covariance give Gaussian domination `exp(-c|t|^2)` after choosing fixed small `delta`.
- On `|t|>delta sqrt(m)`, change variables `t=sqrt(m) s`. Since `phi_W in L^2` and `sup_{|s|>=delta}|phi_W(s)|<=rho_delta<1`,

`int_{|t|>delta sqrt(m)} |phi_W(t/sqrt(m))|^m dt`
`<= m^(3/2) rho_delta^(m-2) ||phi_W||_2^2`,

which is exponentially small.
- Applying the same argument after differentiating the Fourier integrand gives weighted control of `R_m(z)`; bounded support gives cumulants of every order.

Consequently one may take, for some fixed integer `M>1`,

`sup_z (1+|z|)^M |R_m(z)| = O(m^-2)`.

This is more than enough for the quadratic-cone functional because

`int delta(z_1^2+z_2^2-z_3^2) (1+|z|)^(-M) dz < infinity`

for `M>1`: under `z=(r cos theta,r sin theta, +/-r)` the cone Jacobian reduces the integral to a constant multiple of `int_0^infinity (1+r)^(-M) dr`.

Therefore termwise integration over the zero level is justified and the main report's expansion

`p_{Q_m}(0)=3sqrt(2)[1-(1/(20m))sum_j E_J(v_j)+O(m^-2)]`

is a genuine asymptotic theorem for every fixed spanning periodic pattern, not merely a formal Edgeworth calculation.

No claim is made here for patterns changing with `m`; the constants in the remainder may depend on the fixed pattern. This distinction is exactly why genuinely mesoscopic/nonperiodic frames remain an open witness mechanism.
