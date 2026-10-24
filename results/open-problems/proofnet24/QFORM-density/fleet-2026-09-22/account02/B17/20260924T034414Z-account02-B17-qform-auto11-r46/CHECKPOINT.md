SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-24T03:44:14Z.
attacking: the generic zero-physical-pivot three-variable boundary: retain both unequal hub edges and arbitrary transverse quadratic curvature, then prove a global below-3sqrt2 barrier using the actual product law.

# Early substantive checkpoint

Let A be real symmetric 3x3 with A_22=0 and all three eigenvalue magnitudes >=1. Write
A=[[*,a,*],[a,0,b],[*,b,*]], L=sqrt(a^2+b^2). Since A^2 >= I, L>=1. Rotate only the (x,z) integration variables so u=(ax+bz)/L and v=(-bx+az)/L. The transformed (x,z) joint density remains pointwise <=1, and its u-marginal m obeys ||m||_infty<=sqrt(2) by direct one-dimensional convolution.

In these variables Q=r u^2+2d u v+kappa v^2+2Luy, with det A=-L^2 kappa, hence |kappa|>=L^-2. Resolving y gives
p_Q(s)=(2L)^-1 int I_s(u)/|u| du,
I_s(u)<=m(u),
I_s(u)<=2 sqrt(2L|u|/|kappa|).

Thus, with M=sqrt(2), C=2 sqrt(2L/|kappa|), z=I_s and q(u)=min(M,C sqrt|u|), one has z<=q and int z<=1. A weighted bathtub against |u|^-1 gives the exact piecewise envelope, K=|kappa|/L:

if K>=3/sqrt(2):  p_Q(s) <= (48/(L^2|kappa|))^(1/3);
if K<3/sqrt(2):   p_Q(s) <= (sqrt(2)/L)[2+log(sqrt(2)L/|kappa|+1/3)].

Using L>=1 and |kappa|>=L^-2, the first branch is <=2sqrt(2); the second is bounded by F(1)=sqrt(2)[2+log(sqrt(2)+1/3)]<3sqrt(2), because F(L)=sqrt(2)L^-1[2+log(sqrt(2)L^3+1/3)] is decreasing for L>=1.

This would rule out every target-valid 3-variable witness with at least one zero physical diagonal as a >3sqrt2 counterexample. Full verification, pinned-source application, latest account03/B17 application and exact witness checks follow in REPORT.md.
