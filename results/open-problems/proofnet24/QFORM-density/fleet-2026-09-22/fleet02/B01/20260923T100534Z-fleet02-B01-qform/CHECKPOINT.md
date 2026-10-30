SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T10:05:34Z.
attacking: the indefinite two-dimensional cross-kernel left by fleet03/B01, using product-preserving L^4 square-phase control rather than an arbitrary-joint planar shell bound.

# Early mathematical checkpoint

Provisional result: if four ORIGINAL center coordinates split as P={p1,p2} and Z={z1,z2}, J is a disjoint original-coordinate bank, A[Z,J]=0, A[Z,Z]=diag(a,c) with ac!=0, and K=A[P,J] has rank two with Delta=sigma1(K)sigma2(K), then the full ambient form should satisfy

||p_Q||_infinity <= (9/2) Delta^(-1/3)|ac|^(-1/6),

with arbitrary P-P, P-Z, J-J, outside couplings and affine terms retained. The key new estimate is the product-preserving scalar-square bound

int_R |E exp(it(aX^2+lX))|^4 dt <= 27 pi/(2|a|)

for every cap-one density, uniformly in l. For two independent original kernel coordinates this gives an L^2_t bound for the indefinite/separable kernel even though the analogous arbitrary-joint cap-one planar statement is false.

Concrete obstruction to the arbitrary-joint extension: for q(x,y)=xy, R>e, delta=1/log R, rho=1_{1<=x<=R, 0<=y<=delta/x}. Then rho<=1 has mass one, but q has density g(s)=log R on 0<s<delta, hence ||g||_2^2=log R -> infinity. This is not a QFORM counterexample; it shows why original product provenance is essential in the indefinite cross-kernel branch.

Next: complete constants by combining this L^2_t kernel estimate with the same rank-two J-bank projection/Plancherel step as fleet03/B01, apply the newest Theorem H/D/D5 package to a concrete comparison packet, and test a strict-N3 diffuse family.
