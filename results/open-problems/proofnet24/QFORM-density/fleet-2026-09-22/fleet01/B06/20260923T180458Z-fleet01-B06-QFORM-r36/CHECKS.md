# r36 exact checks

## Fourier constants

For Theorem 2.1:

- `||H||_infinity <= 4pi`.
- `int H <= (4pi)^2`.
- `int |t|^(-1/2)H(t)dt <=4 sqrt((4pi)(4pi)^2)=32 pi^(3/2)`.
- Fresnel prefactor `(4pi|c|)^(-1/2)` gives `int |phi_F| <=16pi/sqrt(|c|)`.
- Division by `2pi` gives `8/sqrt(|c|)`.

For Theorem 3.1:

- `||H||_infinity <=(4pi)^2`.
- `int H <=(4pi)^3`.
- weighted interpolation gives `128 pi^(5/2)`.
- Fresnel prefactor and `tau=beta t` give `64pi^2/sqrt(|lambda beta|)`.
- Division by `(2pi)^2` gives `16/sqrt(|lambda beta|)`.

For Theorem 4.1:

- two-frame Fourier volume `(4pi)^2` divided by `(2pi)^2` gives `||p_(L,V)||_infinity<=4`.
- two inverse quadratic branches, each derivative at least `2|lambda|r`, give `4/(|lambda|r)`.

## Walsh pair-minor count

Let the four sign classes have size `n/4`. For `c=cos(theta)`, `s=sin(theta)`, each unordered class-pair contributes `(n/4)^2` physical coordinate pairs. The six class-pair minor magnitudes are

`2|s|/n, 2|c|/n, 2|c+s|/n, 2|c-s|/n, 2|c|/n, 2|s|/n`.

Therefore

`sum_{i<j}|d_ij|
 = (n^2/16)(2/n)[2|s|+2|c|+|c+s|+|c-s|]
 = n/8[2|s|+2|c|+|c+s|+|c-s|]
 = n/4[|s|+|c|+max(|s|,|c|)]`.

On one octant take `0<=theta<=pi/4`. The bracket is `2cos(theta)+sin(theta)`, concave, so its minimum is at an endpoint: `min{2,3/sqrt(2)}=2`. Hence the sum is at least `n/2` for every theta.

Cauchy--Binet independently gives `sum d_ij^2=det Gram(w,n_theta)=1`.

All statements are exact; no Monte Carlo or asymptotic numerical inference is used.
