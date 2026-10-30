# fleet01/B05 r13 audit and improvement

Run: 20260924T182517Z-fleet01-B05-fixedmult-r13.

Source pins:
- historical baseline commit 7c0d6e60946b19423e6400a12d34b473cf0591e2, manuscript blob 183ccd294763214e6a707e8d4749ff9a8cf7006d, 790 lines;
- current nine-value paper commit eeb752c8943536541b34b42b8bf48e924f4d3d2f, blob 19fb119877426b640b2c0dae19ec2f78a399fe11, 955 lines.

Verdict: both literal sources have a local GAP in lem:hyperbola. The positive tail chooses a physical coordinate large for u; the negative tail must independently choose a physical coordinate large for w. With i_+ and i_- selected separately, the same cutoff bound and all constants are unchanged. Product-projection, deterministic orthogonal changes, grouped mollified-L2, density-version and exceptional-slice/Tonelli interfaces otherwise PASS. No FALSE item found.

New theorem (shared-bank two-hub coarea receiver): for source-disjoint literal hubs U=(U1,U2), a product bank V, and any conditioned outside bank, if
Q = 2 U^T (B V + beta) + G(V),
rank(B)=2, and all scalar densities are <=K, then
||p_Q||_infinity <= e sqrt(2 pi) K^2 det(B B^T)^(-1/4).
Proof: conditional on V, scalar product projection in U gives cap sqrt(e)K/(2|R|), R=BV+beta. Product projection in dimension two gives ||p_R||_infinity <= e K^2/sqrt(det(BB^T)). For any planar density p<=M,
E 1/|R| <= 2 sqrt(2 pi M).
Interval domination and Tonelli yield the bound. No independence of projected multiplier coordinates is assumed.

Thus pure bipartite four-direction blocks A=[[0,B],[B^T,0]] with s4(A)>=s obey ||p_Q||_infinity <= e sqrt(2pi) K^2/s. This is a genuine s4 subclass, not the full s4 theorem.

The advertised five-value final source main.tex remains absent from its results directory; s5 is therefore UNCHECKED at source-line level in this B05 run. s4/s3 bounded density remain open.
