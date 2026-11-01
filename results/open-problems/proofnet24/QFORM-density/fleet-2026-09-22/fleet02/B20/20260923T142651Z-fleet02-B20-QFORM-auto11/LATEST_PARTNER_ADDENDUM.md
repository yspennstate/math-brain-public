# Publication-refresh addendum — newest fleet03/B20 strong-top4 splice

A later completed designated-partner handoff appeared during this run and supersedes r32 as the current global proof-graph position:

- fleet03/B20 run `20260923T141124Z-fleet03-B20-QFORM-auto11`;
- canonical report `yspennstate/math-open-problems@118afc3cd9eefcd8ee8282993e78e0e3a841e17a`;
- publication-refresh addendum `yspennstate/math-open-problems@1194a70fc1a8194b940e6ee1b1ad6193fe5e14ad`.

Its fresh global input is fleet04/B20 r10. In `N3(1/64)` it produces a literal original-coordinate cross cut `N=A[J,K]` with

`E:=||N||_F^2 > 11907/16384`,

and either pays continuously by `<116.502`, or leaves

`x_1+x_2+x_3+x_4 >(63/64)E`,

where `x_r=s_r(N)^2`. The designated partner then proves that every unpaid state is in one of two physical cross tubes:

**R1:** `s_2<=s_1/16` and `(sum_{r>=2}s_r^2)^(1/2)<s_1/6`;

**R2:** `sum_{r>=3}s_r^2<(3/64)E` and

`s_1s_2 > rho0:=726327/33554432 =0.0216462314...`.

The older r32 pair payment and augmented-volume results in `REPORT.md` remain valid subsidiary statements, but the global first edge is now this stronger r10/r33 strong-top4 survivor.

## New theorem — `QFORM-STRONGTOP4-ABSOLUTE-RANK2-TUBE-v1`

Every still-unpaid state in the newest designated-partner strong-top4 survivor satisfies

`boxed: s_3(N)<1/64`.                                                  (A.1)

More precisely:

1. In branch R1, if `s_3(N)>=1/64`, then also `s_2>=1/64` and `s_1>=16s_2>=1/4`. Therefore the physical rank-three singular product obeys

   `Delta_3(N)=s_1s_2s_3 >=1/16384`.

   Applying the completed grouped physical cross-rank-three receiver used by the designated partner,

   `||p_Q||_infinity <=3e Delta_3(N)^(-1/3)`,

   gives

   `||p_Q||_infinity <=3e*16384^(1/3)=207.120165...<207.121`.          (A.2)

   Hence an unpaid R1 state has `s_3(N)<1/64`.

2. In branch R2, if `s_3(N)>=1/64`, then the partner's exact product lower bound gives

   `Delta_3(N)>rho0/64`.

   The same full-ambient original-coordinate receiver yields

   `||p_Q||_infinity`
   ` <3e(rho0/64)^(-1/3)`
   ` =117.043769...<117.044`.                                         (A.3)

   Hence an unpaid R2 state also has `s_3(N)<1/64`.

Thus the newest global N3 obstruction is no longer merely "near rank one or near rank two" in a relative Frobenius sense: after all currently completed payments it is trapped in an **absolute operator-norm rank-two tube** around its best physical rank-two cross approximation,

`||N-N_2||_op=s_3(N)<1/64`.                                          (A.4)

The full random quadratic form is *not* replaced by the rank-two truncation; (A.4) is only deterministic coefficient geometry. The known correction forbidding deletion of a small random quadratic perturbation on arbitrary cap-one product inputs remains in force.

## Updated first unpaid implication

The current first full-target edge is sharpened to

`QFORM-N3-ABSOLUTE-RANK2-CROSS-TUBE-PAYMENT-v1`:

> Under the original independent cap-one product hypotheses, `A in N3(1/64)`, and the newest literal physical cut `J disjoint K`, assume `s_3(A)>=1`, `E=||A[J,K]||_F^2>11907/16384`, `s_3(A[J,K])<1/64`, and either R1 or R2 above. Prove one universal finite density bound while retaining arbitrary same-bank quadratic blocks and all extra spectrum, or reduce source-preservingly to a paid physical pair, grouped-square/hub, ridge, or volume receiver.

The r32 moderate-diagonal edge recorded in `REPORT.md` is therefore not the freshest global proof-graph edge; this addendum supersedes that ordering while preserving the r32 local results.

No post-rotation independence, pointwise decay, fiber supremum, one-good-minor selection, or random small-tail deletion is used. Full QFORM and global continuity remain OPEN.
