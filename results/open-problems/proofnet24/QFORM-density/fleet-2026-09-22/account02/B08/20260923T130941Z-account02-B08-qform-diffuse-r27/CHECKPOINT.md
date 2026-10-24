# B08 r27 early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`; full target OPEN.  This checkpoint is mathematics, not a completion claim.

Work in the current `k=1` actual spectral-gate state at scale `L`:

`c=(1/2)sqrt(3/5)`, `beta=(3/16)sqrt(3/5)`,

so each child has an actual `cL`-large eigendirection and the actual full physical cross block `B` has `s_2(B)>=beta L`.

Let `P_2` project onto the top two left singular vectors of `B`, and put

`T_2=sum_{nu>=3}s_nu(B)^2`, `gamma=beta/64`.

The completed tail-volume theorem at `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba` gives the following immediate exhaustive router.  If

`T_2>=gamma^2 L^2`, `max_i (P_2)_{ii}<=1/2`, and `T_2/s_3(B)^2>=225`,

then

`||p_Q||_infinity <= (9sqrt(3)e/2)[s_1^2 s_2^2 T_2]^(-1/6)
 <= (18 sqrt(3)e)/(beta L) < 584/L`.

If the first condition fails, Eckart--Young gives the strong collective tube

`dist_F(B, rank<=2)=sqrt(T_2)<(beta/64)L`.

If the third condition fails (and `s_3>0`), the singular-value tail has stable rank `<225`.  If the leverage condition fails, choose a physical row `i` with `(P_2)_{ii}>1/2`.  Then, writing `g=B^T e_i`,

`||g||^2 >= s_2(B)^2 (P_2)_{ii} > beta^2 L^2/2`.

Now let `s` be a unit `cL`-large child eigenvector on the opposite bank and write `g=<g,s>s+h`, `h perp s`, `tau=||h||`.  Exactly one of

`tau >= beta L/2`,

or

`|<g,s>|>beta L/2`

holds (the latter follows from `||g||^2>beta^2L^2/2` and `tau^2<beta^2L^2/4`).  Thus a heavy top-two cross row is either quantitatively child-aligned or has a quantitative transverse arm.

For the transverse arm, the newest completed designated-partner theorem account03/B08 r37 (`QFORM-MULTIHUB-TRANSVERSE-FRESNEL-v1`, source commit `58b2a0752f409dd48ae5e39851ac84f13be4470b`) gives, in the exact compatible subcase where the opposite child block is `D+lambda ss^T` with `D` diagonal and `|lambda|>=cL`, and where the augmented physical frame has leverage at most `1/2`,

`||p_Q||_infinity < 3*4^(2/3)c^(-1/3)(beta/2)^(-2/3)L^(-1) < 60/L`.

If that augmented leverage gate fails, an actual opposite-bank coordinate carries `>1/4` of either the child frame or the normalized transverse arm.  If the compatible diagonal-plus-child representation fails, the non-diagonal same-bank leakage is retained as the explicit unpaid obstruction; it is not discarded as a small quadratic perturbation.

This already joins the collective-tail diffuse exit to three explicit survivors: a very narrow Frobenius rank-two tube, tail stable rank `<225`, or a heavy physical cross row which is aligned/localized/non-diagonal-leakage.  The next step is to state this as a clean theorem, apply r37 to a target-valid actual `k=1` family, and stress it on the prior Hadamard `k=1` witness.
