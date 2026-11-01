# fleet02/B03 r12 — algebra/constants check

Analytic identities checked for the q=3/2 specialization.

With p=3, q=3/2 and T0=2|td|,

- physical-row factor:
  `||F||_3^3 <= 2 pi T0 L^2/|alpha|`;
- deletion-plane factor:
  `||P||_(3/2)^(3/2) <= (32 pi^2/3) det(G)^(-1/2)`;
- total time exponent:
  `1/2+1/q=7/6`.

The pointwise constant simplifies as

`(4pi)^(-1/2) 2^(-2/3) (2pi)^(1/3) (32pi^2/3)^(2/3)
 =4 pi^(7/6)/3^(2/3)`.

Since

`integral_R min(1,K|t|^(-7/6)) dt=14 K^(6/7)`,

Fourier inversion gives the exact front factor

`7*2^(12/7)*3^(-4/7)`.

For the one-sided packet,

`|a|^(3/7)|sigma|^(-4/7)|h_r|^(-2/7)m^(-4/7)
 =gamma^(-3/7)|sigma|^(-4/7)
  delta^(-2/7)y^(-4/7)`

with `delta=|h_r|/rho`.  The target-scale spectral step is exactly

`gamma^(3/7)|sigma|^(4/7)
 =(gamma|sigma|)^(2/7)(gamma sigma^2)^(1/7)>=s_3(A)`.

Using `L<=sqrt(2)` and `y>1/sqrt(2)` gives

`C_*=7*2^(16/7)*3^(-4/7)=18.2190565794241...`.

Matching `C_* [delta(1-eta_r)]^(-2/7)` to the existing envelope `128sqrt(15)` gives

`delta_*=(C_*/(128sqrt(15)))^(7/2)
 =9.5158151888273e-6`.

No numerical step is used as proof; these values only check the closed-form algebra in `REPORT.md`.
