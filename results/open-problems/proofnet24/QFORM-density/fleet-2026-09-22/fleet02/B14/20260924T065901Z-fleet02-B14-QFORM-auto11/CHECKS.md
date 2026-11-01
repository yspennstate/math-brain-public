# Checks — cap-weighted active-mixture localization

Run `20260924T065901Z-fleet02-B14-QFORM-auto11`.

## 1. Coordinate scaling

If a normalized one-dimensional cell density has essential cap `k>0` and `Z=kY`, then

`p_Z(z)=k^{-1}p_Y(z/k)`, hence `||p_Z||_infinity=1`.

For a three-variable quadratic form `Y^T B Y+ell^T Y+c` with `K=diag(k_1,k_2,k_3)` and `Z=KY`,

`Y^T B Y = Z^T K^{-1}BK^{-1}Z`,
`ell^T Y=(K^{-1}ell)^T Z`.

Thus the source three-dimensional theorem sees exactly the cap-weighted Hessian `K^{-1}BK^{-1}`.

## 2. Zero-tax congruence identity

If `K<=M` coordinatewise and `H_0=M^{-1}BM^{-1}`, then with `R=K^{-1}M>=I`,

`R H_0 R = K^{-1}BK^{-1}`.

Therefore fleet03/B14's signed threshold monotonicity applies directly. In dimension three, if `sigma_0=min|eig(H_0)|`, the positive and negative threshold counts at `sigma_0` sum to three, so every eigenvalue of `R H_0 R` has modulus at least `sigma_0`.

## 3. Recovery of the earlier disjoint-bank constant

For bank coefficient norms `rho_r`, Ball--Rogozin gives `k_r<=sqrt(2)/rho_r`. Put

`R_0=diag(rho_1,rho_2,rho_3)`,
`M=sqrt(2)R_0^{-1}`.

Then

`M^{-1}BM^{-1}=(1/2)R_0BR_0`.

Hence the cap-weighted theorem gives

`6sqrt(pi)/(sigma_min(R_0BR_0)/2)=12sqrt(pi)/sigma_min(R_0BR_0)`,

exactly matching `QFORM-DISJOINT-BANK-SCHUR-LOCALIZATION-v1`.

## 4. Tiny-cube lower bound

For the subdensity `1_{[-m/2,m/2]^3}` and `Q=|x|^2`, if `0<s<m^2/4` the ball of radius `sqrt(s)` is contained in the cube. Therefore

`mu(Q<=s)=(4pi/3)s^(3/2)`,

and the pushforward density is

`p_m(s)=2pi sqrt(s)`.

At `s=m^2/16`,

`p_m(s)=pi m/2`.

The total cell mass is `m^3`, so a mass-linear cell certificate would require `pi m/2 <= C m^3`, impossible uniformly as `m->0`.

The normalized cell cap is `k=1/m`; its cap-weighted Hessian for `B=I_3` is `m^2 I_3`. The fixed-source Theorem A upper bound, restored to submeasure mass, is

`m^3 * 6sqrt(pi)/m^2 = 6sqrt(pi)m`,

which has the same `m` exponent as the exact lower bound.

## 5. N-cell bookkeeping obstruction

Split each uniform marginal on `[-1/2,1/2]` into `N` equal interval subdensities. Each piece has mass `1/N`, unnormalised cap `1`, and normalized cap `N`. For every product cell,

`m_cell=N^{-3}`,
`K=NI_3`,
`sigma_min(K^{-1}I_3K^{-1})=N^{-2}`.

Thus the fixed-source Theorem A gives submeasure height at most

`N^{-3} * 6sqrt(pi) * N^2 = 6sqrt(pi)/N`.

There are `N^3` cells, so summing cell suprema gives `6sqrt(pi)N^2`. Applying the same theorem once to the whole cap-one law gives `6sqrt(pi)`.

## 6. Countable-comb divergence

Let `m_j=6/(pi^2 j^2)` and use cap-one indicator teeth of these lengths. For `B=I_3`, cell `(j,1,1)` has

`m_cell=m_j m_1^2`,
`sigma=m_j^2`,

so its term in the compiler is `m_1^2/m_j=(pi^2/6)j^2`. Hence the fragment-first sum diverges, while the whole law remains bounded by the fixed-source Theorem A.
