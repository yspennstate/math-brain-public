# Arithmetic checks for r36

All formulas below are deterministic consequences of REPORT.md; decimals are only readability checks.

Constants:

- `E0=11907/16384 = 0.72674560546875`.
- `delta=2^-19 = 1/524288`.
- `tau=2^-12 = 1/4096`.
- `c=1/64`.

Parametric E3 floor:

`Z_delta=((1-delta)delta^2/2) E0^3`.

Numerically `Z_delta = 6.981947578553594e-13` and

`10.345084 Z_delta^(-1/6) < 1098.343`,

`2*pi*10.345084 Z_delta^(-1/6) < 6901.092`.

The account04/B20 D5 coefficient

`5 sqrt(2e) 120^(1/10) delta^(-2/5) E0^(-1/2)`

is `<4282.399`.

Relative-second-scale Pluecker branch:

`rho <= delta/[c(1-delta-c)] = 0.0001240081768...`,

`sqrt(rho)+rho/2 = 0.01119789996... < 1/64`.

The lower E2 floor is

`c(1-delta-c) E0^2 = 0.00812352625...`,

so the B07 macro-minor alternative gives

`|det| >= sqrt((15/64)*0.00812352625...) = 0.04363429...`.

The B07 half-Riesz alternative simplifies as

`39.379 [c(1-delta-c)]^(-35/253) E^(-1/4)`

and is `<75.99` for `E>E0`.

Absolute-second-scale / relative-near-rank-one branch:

`Z_tau=(1-c-delta)tau/4 = 6.00813655...e-5`,

so the account02/B02 E3 theorem gives density coefficient `<52.273` and Fourier-L1 `<328.441`.

If `T2<tau/E`, then because `E>16`,

`rho < tau/[4(1-c-delta)] = 6.20040884...e-5`,

`sqrt(rho)+rho/2 = 0.00790526953... <1/64`.

Also

`Omega>4(1-c-delta)=3.93749237...`,

so the macro-minor alternative gives

`|det|>sqrt((15/64)*3.93749237...)=0.96065070...`,

and the half-Riesz alternative is

`39.379 [(1-c-delta)/4]^(-35/253) 16^(-113/1012)
 <35.08`.

Physicalized same-bank curvature:

`(1/4)(31/64)^2 = 961/16384 = 0.05865478515625`.
