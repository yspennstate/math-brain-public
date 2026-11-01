# Exact arithmetic checks for fleet03/B01 r19

These are deterministic arithmetic checks only; they are not substitutes for the proof in `REPORT.md`.

For the theorem

`C_(alpha,k)=((pi e/2)^alpha /(2k Gamma(alpha) cos(pi alpha/2))) * Beta(alpha/(2k),1/8-alpha/(2k))`,

the two used specializations are:

- `k=3, alpha=1/2`: algebraically
  `C3=(sqrt(e)/6) Beta(1/12,1/24)`,
  numerically `C3=9.840655864922018... < 9.841`.
- `k=5`, direct Fourier inversion: 
  `C5=(e/20) Beta(1/10,1/40)`,
  numerically `C5=6.770121056043999... < 6.771`.

The exponent condition for the Riesz integral is `alpha<k/4`: at infinity the integrand is `O(t^(alpha-1-k/4))`, hence integrable exactly when `alpha-k/4<0`. Thus `alpha=1/2` fails at `k=2` (logarithmic endpoint) and succeeds at `k=3`.

The scaling in the pivot-plus-E3 corollary is consistent: if the residual quadratic matrix is multiplied by `r`, then `B -> rB`, `E3(BB^T) -> r^6 E3`, and `E3^(-1/12) -> |r|^(-1/2)`, exactly the half-Riesz scaling.
