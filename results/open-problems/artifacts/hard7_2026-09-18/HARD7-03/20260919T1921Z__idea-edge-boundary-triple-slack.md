Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# HARD7-03 idea-before-code — recover the structural zero-gap edge stratum of the four-step triple slack

Active claim remains `D0025`, Seppäläinen 1999 Problem 4, frozen case `K=2`, `Q=(delta_{1/2}+delta_1)/2`. The carry-in certified source metric is

`L = 3125000/36511391 = 0.085589727326466... <= Delta_2(Q)`.

The preceding run (B3/B5/B20) made all three adjacent-pair classes exact and reoptimized the Chernoff parameter, leaving the upstream triple/higher-overlap envelope as the next bottleneck. This run uses **B4 / B13 / B30**, different from the preceding triple.

## New route

The global triple-slack lower bound and the later mixed-sign corrections still leave a positive-measure *structural boundary stratum* untreated. At the right edge of the sliding-window geometry, on the local-minimum event

`Y_2 > Y_1`,

we have

`S_2=Y_2`, `S_3=Y_2`, `S_1=max(Y_0,Y_1,Y_2)`.

Thus one predecessor gap is identically zero. On the strict subevent

`Y_0 > Y_2 > Y_1`,

write `u=Y_0-Y_2>0`; the two-gap fresh-layer slack is exactly `Phi_theta(u,0)`. The existing local-minimum term uses only `Phi_theta(0,0)=kappa(theta)`, while the existing mixed-sign correction lives on the disjoint event `Y_0>Y_1>Y_2`. Hence this boundary subevent has a genuine positive correction not yet used.

For `a=1-theta`, `b=2-theta`, `c=3-theta`, direct splitting of the defining integral at `u` gives

`Phi_theta(u,0) = theta/(a b) (1-e^{-a u}) + theta/(b c)e^{-b u}`,

so

`Phi_theta(u,0)-kappa(theta) = theta/(a b)(1-e^{-a u}) - kappa(theta)(1-e^{-b u}) > 0` for `u>0`,

where `kappa(theta)=theta/(b c)`.

The resulting one-edge correction is

`C_edge^0 = theta/(a b)(T_0-T_a) - kappa(theta)(T_0-T_b)`,

with

`T_r = E[ exp(theta Y_2-r(Y_0-Y_2)); Y_0>Y_2>Y_1 ]`, `r in {0,a,b}`.

The deterministic first-layer shifts satisfy

`s_0=max(A_-1,A_0,A_1) >= s_1=max(A_0,A_1) >= s_2=A_1`,

so the three `T_r` can be integrated exactly by splitting the `Y_2` integral once at `s_0`. On each of the six first-layer order cones the answer is a finite sum of exponential monomials and at most one gap factor `s_0-s_1`; therefore exact rational cone integration applies at rational `theta`.

### B4 — prove something weaker, completely

Prove this single omitted edge-boundary triple class exactly before touching near-edge/center strata.

### B13 — find what only increases

View the triple correction as a monotone hierarchy: global separable envelope < mixed-sign refinements + local-minimum baseline < those terms plus exact structural zero-gap boundary refinements. Every added stratum is a nonnegative subtraction from the four-step moment envelope, so no previous theorem is weakened.

### B30 — one scale / one direction at a time

Freeze only the two reflected edge strata `Y_0>Y_2>Y_1` and its mirror. Do not enumerate all remaining higher overlaps in this run. If this moves the source metric, checkpoint it and leave the near-edge/central zero-gap strata for the next recurrence.

Before code, the required safety check is disjointness: the new edge boundary stratum lies inside the local-minimum event `Y_2>Y_1`; the prior exact mixed-sign edge correction lies in `Y_1>Y_2`; the pair-minimum correction is a separate term in the deterministic three-variable max/min identity. Therefore the proposed subtraction is not double counted.
