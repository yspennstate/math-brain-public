SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T10:23:21Z.
attacking: integrated Fourier estimate — apply account02/B02's incident-(3+2) cross-disjoint compiler, then replace its common-anchor E2 survivor by an anchored-star fractional-volume gate with a quantitative half-marginal threshold.

# Early substantive checkpoint

Status: SUPPORTING L1 FOURIER LEMMA DERIVED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN.

Let B=A[I,J] be an original-coordinate physical cross block with outer anchors x in I,y in J. Let J3>0 be the squared 3x3-minor mass containing x,y. Let N=B[I\{x},J\{y}], and fix residual physical anchors i,j. Define the positive anchored residual two-volume

H = sum_{r!=i,c!=j} det N[{i,r},{j,c}]^2.

Normalize the incident-J3 family and the anchored-H family separately. Denote their row marginals by a_k and b_k. For 0<theta<1 set alpha_k=theta a_k+(1-theta)b_k and d=2+theta. Exactly the same positive determinant-family interpolation used in the weighted mixed-(3+2) theorem works after restricting the order-two family to this anchored positive subfamily: if 1<=q<d/2 and alpha_k<=q/2 on one physical side (or the analogous column gate), then

||p_Q||_infinity <= C(theta,q) J3^{-theta/(2d)} H^{-(1-theta)/(2d)},

C(theta,q)= e d/[(d-2q)sqrt(q)] [theta^theta(1-theta)^(1-theta)]^{1/(2d)},

and phi_Q is in L1, so the density is continuous and vanishes at infinity.

New quantitative specialization: if every NON-OUTER incident-J3 row marginal obeys a_k<=1/2-gamma, 0<gamma<=1/2, choose

theta=(2-gamma)/3,   q=4/3-5gamma/12,   d=(8-gamma)/3.

Then d-2q=gamma/2 and q>=1. The outer anchor has mixed marginal theta, while every residual row has

alpha_k <= 1-theta(1/2+gamma).

Writing u=d/4, direct algebra gives

u-theta=gamma/4,

u-[1-theta(1/2+gamma)]=gamma(5-4gamma)/12 >= gamma/4,

q/2=u-gamma/8.

Hence all mixed marginals are strictly below q/2. Consequently

integral |phi_Q(t)| dt <= [32 pi e/(3 gamma)] J3^{-a_gamma} H^{-b_gamma},

||p_Q||_infinity <= [16 e/(3 gamma)] J3^{-a_gamma} H^{-b_gamma},

where

a_gamma=(2-gamma)/[2(8-gamma)],  b_gamma=(1+gamma)/[2(8-gamma)].

The homogeneity check is exact: 6 a_gamma+4 b_gamma=1.

Application queued to designated partner account02/B02: in its current two-sided D' failure/cross-disjoint failure branch at eta=1/16, J3>Z3/3 and H>7E2/32. Therefore the displayed L1 estimate applies immediately whenever the incident third-volume law on either physical orientation has residual marginal maximum <=1/2-gamma.

First remaining collar after this checkpoint: both incident row and incident column laws are at/above the half-marginal endpoint, or the aggregate scales J3,H themselves are too small to yield a universal constant from the bare spectral hypothesis.
