SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T22:47:30Z.
attacking: route rough clean-bank curvature by conditioning a physical quadratic vertex cover, then apply the completed account02/B04 top-two rearrangement to the surviving grouped clean bank and prove C0 regularity.

# Early calculation — curvature-cover splice

Let

Q=F(X)+2 X^T M Y+Y^T C Y+b^T Y+c

for disjoint original-coordinate product banks X,Y with scalar densities <=1. If R is a set of Y coordinates and L=J\R satisfies C[L,L]=0, then after conditioning Y_R=r,

Q=F_r(X)+2X^T M_L Y_L+beta_r^T Y_L+c_r.

Therefore the completed account02/B04 clean-bank theorem applies to M_L. If s1(M_L)>=s2(M_L)>0,

||p_(Q|Y_R=r)||_infinity <= 2 sqrt(pi) [s1(M_L)s2(M_L)]^(-1/2),

uniformly in r. Hence the same bound holds unconditionally.

A useful structural identity is

M_L M_L^T=M M^T-M_RM_R^T,

so

s2(M_L)^2 >= s2(M)^2-||M_R||_op^2.

Thus rough Y-curvature is harmless whenever its physical support admits a vertex cover R whose crossing columns do not consume all of the second crossing singular direction.

Regularity upgrade to prove in the full report: for a.e. X=x the conditional linear form in Y_L has at least two nonzero coefficients because rank(M_L)>=2; its density is a convolution of two L1 densities and hence C0. The partner reciprocal-norm majorant is integrable, so dominated convergence should give p_Q in C0 after averaging first over X and then over Y_R.

Stress family to check: X has two physical coordinates, Y={h,z_1,...,z_m} with m even. Let u=(1,1)/sqrt2, v=(1,-1)/sqrt2, alpha=2sqrt(2/m), take m/2 columns alpha u and m/2 columns alpha v, plus a nonzero hub column. Then M_L M_L^T=4I_2 although every nonzero leaf-leaf 2x2 minor is only 8/m. Put all Y-Y curvature on the star centered at h. Conditioning h kills the rough curvature while retaining s1=s2=2. The partner theorem gives sqrt(pi); because the constrained X-bank is exactly two physical coordinates, the exact projection cap is one and the refined constant is sqrt(pi/2).