# account01/B04 r34 addendum — fresh account02/B04 r22 same-matrix comparison

This addendum records the newest designated partner result consumed after the main r34 report was committed.

Partner source: `yspennstate/math-open-problems@2311fa678098f3ac7b96e5eb3795d9def07cc2fd`, account02/B04 r22, theorem `QFORM-ZEROPIVOT-J1-WEIGHTED-MIXED-HUB-v1`.

Let `A_J1=[[0,a^T],[a,vv^T]]` be the partner's pure localized-J1 carrier with 144 residual coordinates, `v_i=1/12` for every `i`, and `a_i=+1/12` on 72 coordinates and `a_i=-1/12` on 72 coordinates. Then `||a||_2=||v||_2=1`, `a.v=0`, and the nonzero spectrum is exactly `{1,1,-1}`. The partner's globally optimized disjoint-pair law has `G_*=1`, hence

`||p_(X^T A_J1 X)||_infinity <= 3*2^(4/3) = 7.559526299369239...`,

with a continuous `C_0` density in that branch.

Now adjoin an independent original-coordinate hyperbolic pair

`B0=[[0,1],[1,0]]`

and set `Ahat=B0 direct_sum A_J1`. Convolution with the independent `B0` contribution does not increase a density supremum, so the partner certificate remains

`||p_(X^T Ahat X)||_infinity <= 3*2^(4/3)`.

Apply the new r34 exact-optimizer route to the same `Ahat`, using `B0` as the outer indefinite physical pair. Then

`D=|det B0|=1`, `kappa=sigma_min(B0)=1`.

The residual zero-self hub is the anchor of `A_J1`; its slope is `2 a^T X`. The sharp one-dimensional product-projection bound gives

`H <= sqrt(2)/||2a||_2 = 1/sqrt(2)`.

Hence the r34 dimensionless parameter is

`rho=8 sqrt(D H/kappa)=8*2^(-1/4)=6.727171322029716... >2`.

The exact high-rho optimizer therefore gives

`||p_(X^T Ahat X)||_infinity <= 4+2 log(rho/2) = 6.426015131959808...`.

Thus, on the same target-valid matrix, the new exact optimizer improves the fresh partner r22 displayed certificate by the factor

`7.559526299369239... / 6.426015131959808... = 1.17639410180843...`.

This comparison is only between two valid sufficient receivers on this matrix; neither theorem globally subsumes the other. The unrestricted three-large-eigenvalue conjecture remains open. The r34 branch proves essential boundedness; continuity is not claimed for the exact-optimizer theorem itself.
