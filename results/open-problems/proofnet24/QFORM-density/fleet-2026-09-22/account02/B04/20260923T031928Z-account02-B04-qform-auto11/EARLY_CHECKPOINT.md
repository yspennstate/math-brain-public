SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T03:19:28Z.
attacking: near-coloop admissible-volume I-projection versus square-assisted ridge on the same physical cross block.

# Early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`; full target remains OPEN. Live corrections consumed: no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea bound, and no universally good single physical minor.

I changed the previous exact-coloop mechanism to a quantitative near-coloop. For `0<delta<1/2`, define the `6 x 3` tight frame `U_delta` by

- `u_1=(sqrt(1-delta),0,0)`;
- for `j=0,...,4`,
  `u_(j+2)=(sqrt(delta/5), sqrt(2/5) cos(2 pi j/5), sqrt(2/5) sin(2 pi j/5))`.

The fifth-root trigonometric identities give `U_delta^T U_delta=I_3`. With any orthogonal `V`, put

`M_(epsilon,delta)=U_delta diag(epsilon,2,2)V^T`.

For the squared-minor three-volume law on row triples, Cauchy--Binet and `|det V|=1` give

`P_*(S)=det(U_delta[S,:])^2`,

and the row marginals are exactly the projection diagonals

`alpha_1^*=1-delta`,
`alpha_2^*=...=alpha_6^*=(2+delta)/5`.

Let `E={1 in S}` and `p=P_*(E)=1-delta`. For any fractional-volume exponent `1<=q<3/2`, set `c=q/2`. Among *all* probability weights `w` on nonzero three-minors satisfying every row marginal `<=c`, the exact KL minimum is

`D_q^*=d_Bern(c||p)` when `c<p`, and `0` when `c>=p`.

Proof: data processing under `S -> 1_E` gives `KL(w||P_*)>=d_Bern(w(E)||p)`; when `c<p` this is minimized at `w(E)=c`. Equality is attained by the two-level tilt

`w_q = c P_*(.|E)+(1-c)P_*(.|E^c)`.

Cyclic symmetry of the five tail rows makes every tail marginal `(3-c)/5<=c` exactly because `c>=1/2`, so this tilt is feasible and attains the lower bound. Thus the entropy-adjusted volume is optimized exactly:

`G_q^*=16 epsilon^2 exp(-D_q^*)`.

Applying the arbitrary-weight form of the source-pinned sharp fractional three-volume theorem therefore gives the exact best certificate within this entire weighted-q family,

`C_vol(q) = [3e/((3-2q)sqrt(q))] [16 epsilon^2 exp(-D_q^*)]^(-1/6)`.

For `delta=1/100`, `p=.99`, strict convexity of `log C_vol(q)` on `[1,3/2)` and

`d/dq log C_vol(q)|_(q=1)=3/2+(1/12)log(delta/(1-delta))>0`

show that the global optimum is `q=1`. Then

`D_1^*=(1/2)log(1/[4 delta(1-delta)])=1.614463080360851...`,
`G_1^*=32 epsilon^2 sqrt(delta(1-delta))`,

and

`C_vol,opt = 6.723382313377931... epsilon^(-1/3)`.

At `epsilon=10^-6`, even the globally optimized admissible three-volume certificate is therefore `672.3382313377929...`.

Next in this same run: embed the block into `Q=Z^2+2X^T M Y`, verify the exact target spectrum, compare this optimized volume certificate to the square-assisted ridge certificate and to the latest completed account03/B04 physical-pair determinant theorem on the identical physical matrix, then preserve the resulting routing implication.
