# account03/B01 early substantive checkpoint — rank-two cross + definite two-dimensional kernel

Programme: `QFORM-DENSITY-3EIG-20260922`. Run: `account03-B01-20260923T083025Z-auto11`. Full conjecture remains OPEN.

Take four ORIGINAL coordinates `I`, a disjoint ORIGINAL-coordinate bank `J`, and condition every other coordinate. Write

`Q_w = X_I^T B X_I + 2 X_I^T K X_J + l_w^T X_I + G_w(X_J)`

with `rank K=2`. Let `V` be an orthonormal basis of `ker(K^T)` (dimension two), put

`Delta = sigma_1(K) sigma_2(K)`,  `H = V^T B V`,  `d2=|det H|`.

If `H` is positive or negative definite, the following calculation gives a candidate complete supporting theorem:

`||p_Q||_infinity <= 3 (pi/2)^(1/3) Delta^(-1/3) d2^(-1/6) < 3.488 Delta^(-1/3)d2^(-1/6)`.

Proof skeleton. Rotate only the four-dimensional center algebraically so `(u,z)` has `u in range(K)` and `z in ker(K^T)`. The rotated joint density `rho(u,z)` remains pointwise <=1; no independence is asserted. For fixed `u`, the definite translated quadratic in `z in R^2` pushes the subprobability slice `rho(u,z)dz` to a one-dimensional density bounded by `pi/sqrt(d2)`. If its slice mass is `m(u)`, Plancherel gives

`int_R |h_t(u)|^2 dt <= 2 pi^2 d2^(-1/2) m(u)`.

Therefore, with `A(t)=||h_t||_{L^2(du)}`,

`||A||_2 <= sqrt(2) pi d2^(-1/4)`.

The untouched original-product `J` bank supplies the rank-two physical gradient. The two-dimensional product-projection theorem gives `||p_{2 M X_J}||_infinity <= 1/(2 Delta)` after the center rotation, and two-dimensional Plancherel yields

`|phi_Q(t)| <= sqrt(2) pi Delta^(-1/2) |t|^(-1) A(t)`.

Hence for every `T>0`,

`int |phi_Q(t)|dt <= 2T + 2 sqrt(2) pi^2 Delta^(-1/2)d2^(-1/4) T^(-1/2)`.

The exact minimizer is `T=(B/4)^(2/3)` for `B=2sqrt(2)pi^2 Delta^(-1/2)d2^(-1/4)`, and Fourier inversion simplifies the constant to `3(pi/2)^(1/3)`. This also gives a continuous `C_0` density.

This mechanism is distinct from the previous source-disjoint-square L3 argument: the two smoothing directions may be arbitrary rotations inside the SAME four-coordinate center bank. What remains to check before publication is the block-determinant invariant, constants, source/correction refresh, and exact signed-Fejer transfer using the designated account04/B01 theorem.
