# Correction to the early checkpoint

The checkpoint's equations (C3)--(C5) are **not valid as written**. The common hyperbolic pointwise envelope

  G_B(s)=D^(-1/2)[5.2+log_+(16 sqrt(D)/|s|)]

has a nonzero constant tail, so G_B is not in L^{3/2}(R). The partner's uniform conditional L^{3/2} bound does not come from the L^{3/2} norm of this common envelope; it uses probability normalization of each individual conditional density on the tail. Therefore one may not apply Young/Hölder to G_B*p_R and obtain the checkpoint constant 32.531.

The valid dependence-safe decomposition is instead

  p_Q(t)
  <= 5.2 D^(-1/2)
     +D^(-1/2) E log_+(16 sqrt(D)/|t-R|).

The logarithmic kernel alone is in L^{3/2}. If p_R is in L^3, then

  sup_t E log_+(K/|t-R|)
  <= [2K Gamma(5/2)]^(2/3) ||p_R||_3,

with K=16 sqrt(D). Hence

  ||p_Q||_infinity
  <= 5.2 D^(-1/2)
     +[32 Gamma(5/2)]^(2/3) D^(-1/6)||p_R||_3.

In the partner's paid Schur-E2 branch, under |d|,|e|<|a|/2, D>=3a^2/4 and ||p_R||_3<12.257 |a|^(1/3) Z^(-1/6), this becomes

  ||p_Q||_infinity
  < 6.004443 |a|^(-1)+156.698472 Z^(-1/6).

Thus the common-singularity argument closes the branch only when |a| is quantitatively comparable to Z^(1/6); it does not remove the small-edge obstruction. The final report develops this corrected theorem and records the resulting sharper survivor.
