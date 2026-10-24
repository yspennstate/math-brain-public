SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T23:10:57Z.
attacking: the principal-minimal base-subcritical threshold-transfer gate by sign-resolved Schur inertia and a threshold-normalized physical carrier.

# Early checkpoint — threshold-normalized carrier

Let a real symmetric coefficient matrix be split in ORIGINAL coordinates as

A = [[B,C],[C^T,D]],

with nonempty hub bank H and base bank L. For sigma in {+1,-1}, let

p_sigma(M) = #{lambda(sigma M) >= 1}.

Suppose p_sigma(A) > p_sigma(D). Fix gamma in (0,1]. If

lambda_max(sigma B) <= 1-gamma,

then the sign-sigma subthreshold spectral carrier obeys

|| C P_{sigma D<1} (I-sigma D)^(-1/2) ||_op^2 >= gamma,

where the inverse square root is taken only on the spectral subspace {sigma D<1}.

Proof sketch. For t=1-epsilon with epsilon>0 small enough that the counts above t equal the counts at threshold 1 for both sigma A and sigma D, Haynsworth inertia for D_sigma-tI gives a Schur complement with a positive eigenvalue. Since sigma B-tI <= -(gamma-epsilon)I,

lambda_max(C(tI-sigma D)^(-1)C^T) > gamma-epsilon.

Split the resolvent into its positive piece over eigenvalues mu<t and its negative piece over mu>t. Dropping the negative piece only increases the top eigenvalue. Let epsilon down to zero. This yields the displayed inequality, including exact threshold eigenvalues without any continuity-in-law argument.

Consequently, if c=||C||_op and the hub alternative fails, then the nearest sign-sigma base eigenvalue below threshold satisfies

min_{mu in spec(sigma D), mu<1} (1-mu) <= c^2/gamma.

Indeed the weighted carrier is bounded above by c^2/delta if every subthreshold gap is at least delta. Thus a vanishing physical carrier forces a base mode to approach the same signed threshold at QUADRATIC scale. This is exactly the scale of the previously constructed principal-minimal model with carrier sqrt(delta): there the weighted carrier equals 1 identically.

In a principal-minimal target with N_A(1)>=3 and N_D(1)<=2, at least one sign sigma has p_sigma(A)>p_sigma(D). Taking gamma=1/2 gives the unconditional deterministic dichotomy

lambda_max(sigma B) >= 1/2

or

|| C P_{sigma D<1}(I-sigma D)^(-1/2)||_op >= 1/sqrt(2),

and in the second branch

1-mu_* <= 2 ||C||_op^2

for some mu_*<1 in spec(sigma D).

This attacks the first base-subcritical transfer gap without requiring a fixed base gap, fixed carrier norm, local pivot, source rotation, or deletion of a coefficient tail. The remaining analytic receiver must spend this normalized near-threshold carrier while retaining arbitrary same-bank curvature and rough cap-one product laws.
