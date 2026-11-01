SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-23T08:17:48Z.
attacking: high-leverage receiver escape via rank-two half-Riesz plus exact Schur-area identity.

# Early substantive checkpoint

Full QFORM remains OPEN. This checkpoint records a new calculation before the final report.

## Dependency actually used

1. fleet03/B01, commit `1a17dbbee81858c6cb1082c7cafaea345f07554b`, proves for an exact rank-two physical cross block K with singular values kappa_1,kappa_2 and arbitrary self phases on both original-coordinate banks:

`|phi_R(t)| <= min(1, 2*pi/(|t|*sqrt(kappa_1*kappa_2)))`.

2. designated partner fleet02/B01, commit `2276262ea756f8da3fc0b5252ec69537a5941257`, proves the grouped rank-two coefficient + transverse receiver Fresnel theorem under the augmented receiver leverage gate `ell_j<=1/2`.

## First new implication

Let `Delta=kappa_1*kappa_2`. From the rank-two cross characteristic envelope and the Fourier representation of `|x|^{-1/2}`,

`sup_s E|R-s|^{-1/2} <= 8 Delta^(-1/4)`.

Therefore if one independent physical coordinate X0 enters as

`Q=a(X0+h(Z))^2+R(Z)`, `a!=0`,

with the shift h allowed to depend arbitrarily on the residual variables, then

`||p_Q||_infinity <= 8 |a|^(-1/2) Delta^(-1/4)`.

This is a dependent-shift square lift: it does not require the square bank to be source-disjoint from the rank-two cross packet.

## Exact high-leverage receiver calculation

Take the partner geometry `K=U Sigma V^T`, `Delta=det Sigma`, and receiver self block `D+lambda w w^T`, with D diagonal and ||w||=1. For physical receiver coordinate j define

`v=V^T e_j`, `h=||v||^2`, `q=V^T w`, `t=w-Vq`, `Omega=||t||`, `tau=t_j`, `ell=h+tau^2/Omega^2`,

`a=d_j+lambda w_j^2`.

After completing the physical pivot j, the residual I x (J\{j}) cross block is

`M_j=U Sigma Z_j^T`, with rows `z_l=v_l-(lambda w_j/a) w_l v`, l!=j.

Direct 2x2 Gram expansion gives

`det(Z_j^T Z_j)=N_j/a^2`,

where

`N_j=lambda^2 w_j^2 ell Omega^2 + 2 lambda w_j d_j tau + (1-h)d_j^2 >=0`.

Hence, when `a!=0` and `N_j>0`, M_j has rank two and singular-value product

`Delta_j=Delta sqrt(N_j)/|a|`.

The dependent-shift square lift therefore gives

`||p_Q||_infinity <= 8 |a|^(-1/4) Delta^(-1/4) N_j^(-1/8)`.

This is the proposed high-leverage escape complement to the designated partner's low-leverage Fresnel theorem. It is uniform as a receiver direction overlaps the rank-two cross bank; no scalar pointwise quadratic-phase decay is used.

Remaining work for the final report: prove the two displayed identities carefully, apply the fleet02/B01 low-leverage theorem as the complementary branch, give a strict-N3 target-valid high-leverage family where its leverage gate fails but the new branch is uniform, refresh corrections, and save/check the final report.
