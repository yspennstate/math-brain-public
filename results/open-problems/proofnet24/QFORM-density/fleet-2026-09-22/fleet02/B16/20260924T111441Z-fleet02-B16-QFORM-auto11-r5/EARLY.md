SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-24T11:14:41Z.
attacking: the genuinely indefinite same-bank/nonzero-separated-pivot residue after partner fleet03/B16 r46, by first proving the complementary definite-Schur exit and then testing whether joint-plus-marginal projection caps can possibly pay the indefinite branch.

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

Early calculation — dependent pair + nonzero scalar pivot, definite Schur exit.

Let Z=(S,U) have arbitrary joint density rho with ||rho||_infinity<=M. Let V be independent of Z with scalar density cap N. Consider

Q = Z^T C Z + 2 V ell^T Z + d V^2 + p^T Z + qV + c,

where d!=0, and define the 2x2 Schur remainder H=C-d^{-1} ell ell^T. If H is definite, affine completion and translation reduce to

Q = d(V+a(Z))^2 + (Z-z0)^T H (Z-z0) + c0.

For R=(Z-z0)^T H(Z-z0), planar coarea after y=|H|^{1/2}(Z-z0) gives

||p_R||_infinity <= pi M / sqrt(|det H|).

Conditioned on Z, the square term has one-sided density envelope N / sqrt(|d| w). For any probability density h<=K,

sup_s integral_0^infinity y^{-1/2} h(s-y) dy <= 2 sqrt(K)

(and likewise from the other side), by the bathtub principle. Therefore

||p_Q||_infinity <= 2 sqrt(pi) N M^{1/2} |d|^{-1/2}|det H|^{-1/4}
                = 2 sqrt(pi) N M^{1/2} |d det B|^{-1/4},

where B=[[C,ell],[ell^T,d]] and det B=d det H.

For actual original-product sources, let Z=(r^T X_I,u^T X_I), G=[[||r||^2,<r,u>],[<r,u>,||u||^2]]>0, and V=v^T X_J from a disjoint bank, tau=||v||_2. The pinned completed two-dimensional product-projection theorem gives M<=2 det(G)^(-1/2), while the scalar projection theorem gives N<=sqrt(2)/tau. Hence

||p_Q||_infinity <= 4 sqrt(pi) [ |d| tau^2 |pdet A| ]^(-1/4)

for the exact rank-three physical form A=TBT^T with carrier Gram diag(G,tau^2). Thus, on the owner target |pdet A|>=1,

||p_Q||_infinity <= 4 sqrt(pi) (|d| tau^2)^(-1/4).

Strict target check: with orthonormal carrier and
B = [[1,0,sqrt(3)],[0,4,0],[sqrt(3),0,-1]],
H=4 I_2, det B=-16, spectrum(B)={-2,2,4}. The bound becomes ||p_Q||_infinity <= 2 sqrt(pi).

The complementary indefinite-H branch is not paid by this calculation. Next step in this run: test whether retaining the true scalar marginals of the dependent pair, in addition to the joint planar cap, can control that branch. If not, record an explicit source-valid-interface obstruction rather than silently replacing the pair by independent coordinates.
