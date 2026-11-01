SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T14:56:28Z.
attacking: a heat-scale Dini/Cauchy criterion that separates bounded height from continuity and passes new Fourier/volume estimates through rough weak limits.

# Early substantive checkpoint

Let `gamma_r(u)=(2*pi)^(-1/2) r^(-1) exp(-u^2/(2r^2))`, `H_r(y)=(mu*gamma_r)(y)`, and

`A_r(y)=int ((z-y)^2/r^2) gamma_r(z-y) dmu(z)`.

Direct differentiation gives the exact scale equation

`r d_r H_r = A_r-H_r`.

Therefore, writing `D_mu(r)=||A_r-H_r||_infinity`, for `0<s<r`,

`||H_r-H_s||_infinity <= int_s^r D_mu(u) du/u`.

Hence the Dini condition `int_0^{r0} D_mu(u) du/u<infinity` forces `H_r` to converge uniformly as `r downarrow 0`. The limit is in `C_0`; testing against compactly supported continuous functions identifies `mu=p dx`, and

`||p-H_r||_infinity <= int_0^r D_mu(u) du/u`.

This is a continuity criterion genuinely stronger than the central bounded-height condition. It is tailored to weak-law limits because for every fixed `r`, both `H_r` and `A_r-H_r` are convolutions with `C_0` kernels.

For any characteristic-function envelope `|phi(t)|<=K|t|^{-b}`, `1<b<3`, Fourier inversion of the heat defect gives

`D_mu(r) <= c_b K r^(b-1)`,

`c_b = 2^((1-b)/2) Gamma((3-b)/2)/pi`,

so

`||p-H_r||_infinity <= [c_b/(b-1)] K r^(b-1)`.

The current volume-stability theorem at q=4/3 has `b=9/8`; this will yield an explicit `r^(1/8)` uniform heat-to-density rate and a zero-loss continuity trace under weak limits. Full details/constants and the fleet04/B15 heat-height application follow in REPORT.md.
