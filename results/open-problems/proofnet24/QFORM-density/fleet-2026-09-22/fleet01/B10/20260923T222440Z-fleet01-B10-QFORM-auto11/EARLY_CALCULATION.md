SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B10, 2026-09-23T22:24:40Z.
attacking: the shared-hub near-coloop receiver by first making the fleet02/B10 pure-longitudinal recombination completely rough-law stable and identifying the exact three-bank inequality it satisfies.

# Early calculation — three-bank hyperbolic-square receiver

Let Z,Y,W be mutually independent real random variables with probability densities bounded by K_Z,K_Y,K_W. Let s,d be nonzero reals and b,c arbitrary. Put

Q = 2 s ZY + bY^2 + 2cYW + dW^2.

Complete the W-square:

Q = d(W+(c/d)Y)^2 + 2sZY + kappa Y^2,

where kappa=b-c^2/d. Conditional on (Y,Z), the translate W+(c/d)Y still has density bounded by K_W. Therefore the conditional density of d(W+(c/d)Y)^2 is bounded by

K_W / (sqrt(|d|) sqrt(|u|))

on the appropriate one-sided support, hence for a.e. q

p_Q(q) <= K_W |d|^(-1/2) E |q-(2sZY+kappa Y^2)|^(-1/2).      (E1)

For any probability density f<=K,

sup_a int f(x)|x-a|^(-1/2) dx <= 2 sqrt(2K),                   (E2)

by the bathtub/rearrangement bound (the extremizer is K on the centered interval of length 1/K).

Conditioning next on Y=y and using

2s y Z+kappa y^2 = 2s y (Z + kappa y/(2s)),

(E2) gives

E_Z |q-(2s y Z+kappa y^2)|^(-1/2)
 <= 2 sqrt(K_Z/|s|) |y|^(-1/2).

A second use of (E2) for Y yields

sup_q E |q-(2sZY+kappa Y^2)|^(-1/2)
 <= 4 sqrt(2) sqrt(K_Z K_Y/|s|).

Substituting in (E1):

||p_Q||_infinity <= 4 sqrt(2) K_W sqrt(K_Z K_Y) / sqrt(|s d|).  (E3)

No smoothness, moments, connected support, compact support, Gaussianity, or post-rotation independence is used. This establishes an L-infinity density; continuity has not yet been proved.

Application target: fleet02/B10's exact fragmented-hub family has Q_rho=2 ZY+W^2 with Z,Y,W normalized linear projections of three disjoint ORIGINAL-coordinate banks. The orthonormal-projection density theorem gives K_Z,K_Y,K_W<=sqrt(2) for arbitrary cap-one source laws, not only the uniform non-hub specialization used in the partner report. Hence (E3) gives ||p_Q||_infinity<=8 sqrt(2)<11.314 for that entire exact family, uniformly in rho including rho=0 and with arbitrarily fragmented hub density.

Next in this run: place (E3) in the exact rank-three null-axis geometry, where det M=-s^2 d and |det M|>=||M||>=s, to obtain a universal <=8sqrt(2) bound for every three-disjoint-bank null-axis form; then isolate precisely why generic mixed transverse rows are still outside this receiver.
