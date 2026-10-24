SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-24T00:51:27Z.
attacking: convert the designated partner's high-E4 double-anchor packet into a continuous density bound by aggregate fixed-pair product Fourier, then test it on a dense rank-four indefinite family where every local four-row determinant vanishes with dimension.

# Early calculation: canonical E4 pair mass is already a fixed-pair Fourier currency

Let I,J be disjoint original-coordinate banks and M=A[I,J]. Put

E4 = e_4(M M^T) = sum_{R subset I, |R|=4} sum_{T subset J, |T|=4} det A[R,T]^2.

For a fixed original-coordinate pair H={i,j} subset I define the canonical pair mass

H_ij = sum_{R subset I, |R|=4, H subset R} sum_{T subset J, |T|=4} det A[R,T]^2.

The completed fixed-pair theorem of account01/B09 uses

U_H = sum_{S subset H^c, |S|=2} sum_{T subset H^c\S, |T|=4} det A[H union S,T]^2.

Every summand of H_ij is a summand of U_H because S subset I\H, T subset J, and I cap J is empty. Hence U_H >= H_ij. Therefore account01/B09's source-pinned estimate gives immediately

||p_Q||_infinity <= C4 H_ij^(-1/8),
C4 = 2 sqrt(2) e^(1/4) 3^(3/4) = 8.278650626819047...,

with a continuous C_0 density.

If eta=H_ij/E4 is the canonical fourth-volume pair probability, this is

||p_Q||_infinity <= C4 (eta E4)^(-1/8).

The designated partner account04/B04 r2 proves that in its high-carrier branch rho_i>1/25, failure of the anchored third-volume entropy gate at beta_*>2/3 yields some j with eta=rho_i beta_j>2/75. Therefore that entire double-anchor branch is paid by

||p_Q||_infinity < C4 (75/(2 E4))^(1/8)
                 = 13.023072655226386... E4^(-1/8),

again with continuous C_0 density.

Sources to re-read in the final report:
- partner: math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57, account04/B04 r2 REPORT.md;
- fixed-pair theorem: math-open-problems@2a53120a6f9206721f98811b05cd8c80002aab68, account01/B09 REPORT.md.

Full QFORM remains open: this converts one quantitative cross-block branch to a density estimate but does not force such a high-E4 carrier from the bare three-large-eigenvalue hypothesis.
