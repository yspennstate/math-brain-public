# Checks for fleet01/B19 20260923T204757Z

The proof is exact; these are regression/bookkeeping checks only.

## Constants

- `S0 = 1/(480*sqrt(7626)) = 2.3856699607287348e-5`.
- `C_E3 = 3*2^(4/3)*e^(1/3) = 10.550168831164775`.
- `C_E3*(256/27)^(1/6) = 15.348718100234715`.
- At `W=2^-20`, the compiled physical third volume is at least
  `(27/256)*S0^2*2^-20 = 5.724592930120713e-17`.
- Fourier inversion then gives `5374.053363485854 < 5375`.
- If `W<2^-20` and `ell_i<=3/4`, then
  `sum r_i^2 < 4*2^-20 = 2^-18`, hence the aggregate row residual is `<2^-9=1/512`.
- With `mu>=1/4`, the deterministic stability bound is
  `3 eps + 3 eps/mu <= 15 eps < 15/512 = 0.029296875`.

## Algebra regression

For random real symmetric leaf blocks and random full-rank `2 x n` hub frames, whitening to `VV^T=I` was used only as a coefficient transformation. The identity

`A0 V0 - V0^T A0^T = R^T-R`

and the reconstruction

`D0 = Delta + A0 V0 + R`

were evaluated numerically. In all trials the derived Frobenius estimate

`||D0-Delta-V0^T K V0||F <= 3 eps + 3 eps/mu`

held with positive slack. No numerical experiment is used as proof.
