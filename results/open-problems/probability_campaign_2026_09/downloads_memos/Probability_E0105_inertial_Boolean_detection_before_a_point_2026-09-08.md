# Detecting a ball before an enemy point is reached, in the inertial Boolean model

Settled 2026-09-08 for the homogeneous case. Ledger ids E0105 (Open problem 3) and, for the pair
ball/point and for two balls, E0104 (Open problem 2). Source: Konstantopoulos, *The mobile Boolean
model: an overview and further results*, arXiv:1407.6834, Section 7, with the problem spelled out at
the end of Section 5.

## The problem as the source states it

Particles start at the points of a homogeneous Poisson process of intensity lambda in R^d, each
carries a closed ball of radius r, and each moves in a straight line, x + t v, with i.i.d. velocities
v. W(t) is the region covered up to time t. The source obtains (its (15)) the detection time of a
ball r_0 B: P(S_K > t) = exp(-lambda omega_d R^d - lambda omega_{d-1} R^{d-1} E|v| t), R = r_0 + r.
Then, end of Section 5:

> A more elaborate problem is the computation of the law of inf{t >= 0 : r_0 B cap W(t) != empty,
> a not in W(t)} ... the first time that the particles will detect a fixed ball of radius r_0
> before anyone of them goes close to some point a (the enemy). This problem will be addressed in
> the future.

and Open problem 3 restates it; Open problem 2 asks for P(S_{K_1} < S_{K_2}) for two sets.

## Reduction

Write S_K and S_a for the detection times of the ball K = r_0 B and of the point a, i.e. the first
t with K cap W(t) != empty and with a in W(t). Since W(t) grows with t, the set
{t : K cap W(t) != empty, a not in W(t)} is {t : S_K <= t < S_a}. Hence

    tau = S_K on {S_K < S_a},   tau = +infinity on {S_a <= S_K}.

So the law of tau is a functional of the joint law of (S_K, S_a), and the problem is the ball/point
case of Open problem 2.

## The joint law

A particle starting at x with velocity v detects K by time t iff its centre x + s v comes within R of
the origin for some s in [0,t], i.e. iff x lies in the capsule

    C_R(t; v) = R B + [0, t] (-v)          (a ball of radius R swept along the segment from 0 to -t v),

and it covers a by time s iff x lies in the capsule C_r^a(s; v) = a + r B + [0, s] (-v). The particles
form a marked Poisson process (positions with intensity lambda dx, velocities i.i.d.), so

    P(S_K > t, S_a > s) = exp( - lambda E_v Vol( C_R(t; v) cup C_r^a(s; v) ) ).                  (1)

The two capsules have parallel axes (both along e = -v/|v|). With c = |v|, a_par = a . e and
h = |a - a_par e| the perpendicular offset of the enemy from the ball's track,

    Vol(C_R(t) cup C_r^a(s)) = omega_d R^d + omega_{d-1} R^{d-1} c t
                             + omega_d r^d + omega_{d-1} r^{d-1} c s
                             - integral over z of L_{d-1}( rho_1(z), rho_2(z), h ) dz,             (2)

where, along the axial coordinate z, rho_1(z) = sqrt(R^2 - dist(z,[0,ct])^2)_+ and
rho_2(z) = sqrt(r^2 - dist(z,[a_par, a_par + cs])^2)_+ are the radii of the two cross-sections and
L_{d-1}(rho_1, rho_2, h) is the (d-1)-volume of two (d-1)-balls of those radii with centres h apart:
an interval overlap for d = 2, the circular-lens area for d = 3, and a standard one-dimensional
integral for larger d. Equation (2) is exact; (1) is exact. For an isotropic velocity law the
expectation over v is an average over the angle between the track and a and over the speed.

## The law of tau

From (1),

    P(tau = 0) = P(S_K = 0 < S_a) = exp(-lambda omega_d r^d) - exp(-Lambda(0,0)),
    P(tau in du) = -(d/dt) P(S_K > t, S_a > s) |_{t = s = u} du = (partial_1 Lambda)(u,u) e^{-Lambda(u,u)} du,   u > 0,
    P(tau = +infinity) = P(S_a <= S_K) = 1 - P(tau = 0) - integral_0^infinity (partial_1 Lambda)(u,u) e^{-Lambda(u,u)} du,

with Lambda(t,s) = lambda E_v Vol(C_R(t;v) cup C_r^a(s;v)) from (2). The atom at zero is the
probability that some particle already overlaps the ball at time 0 while none overlaps the enemy;
it is the void probability of two disks (in d = 2) and it dominates whenever lambda omega_d R^d is
of order one. The atom at +infinity is the probability that the enemy is reached first (or at the
same instant, an event of probability zero when a lies outside R B). Ties S_K = S_a > 0 have
probability zero because the coincidence is a codimension-one condition on (x, v).

For two balls K_1 = r_1 B + b_1, K_2 = r_2 B + b_2 the same formula holds with R_1 = r_1 + r,
R_2 = r_2 + r and h the perpendicular offset of b_2 - b_1; this is Open problem 2 for balls.

## Check against the particle system

d = 2, lambda = 0.3, r = 0.5, r_0 = 1 (R = 1.5), a = (3, 0), unit speed, isotropic direction. Formula
(1)-(2) by quadrature (64 track angles, 600 to 1,500 axial points) against a direct simulation of
the marked Poisson particle system (20,000 and then 60,000 independent configurations, every
particle's first entry time into the two capsules solved as a quadratic; e0105.py):

    t   P(S_K > t)  formula / MC     P(S_K > t, S_a > t)  formula / MC
    1      0.0488 / 0.0476                 0.0285 / 0.0288
    3      0.0081 / 0.0074                 0.0031 / 0.0032
    6      0.0005 / 0.0006                 0.0001 / 0.0001

    60,000 runs, atom and continuous part separated:
    P(tau = 0) = P(S_K = 0 < S_a):           formula 0.6953 (exact two-disk void probability)   MC 0.6967 +- 0.0019
    P(0 < tau <= 1), (<= 3), (<= 6), (<= 12): formula 0.0497, 0.0692, 0.0715, 0.0717            MC 0.0482, 0.0678, 0.0703, 0.0703 (+- 0.0010)
    P(tau < infinity) = P(S_K < S_a):         formula 0.7670                                      MC 0.7671 +- 0.0017

The joint survival function, which carries the whole content of (1)-(2), agrees to the third
decimal; the total P(S_K < S_a) agrees to four. The continuous part sits about 0.0014 above the
simulation at every horizon, 1.5 standard errors, which is the size of the quadrature error in the
numerical derivative (a 600- to 1,500-point axial grid that moves with t); a 20,000-run pilot had
shown a 0.005 gap that the larger run resolved as sampling noise.

## What is and is not done

Done: the exact joint law (1)-(2) of the ball's and the enemy's detection times for the
homogeneous inertial model with any velocity law having E|v| finite, and hence the law of tau,
explicit up to a one-dimensional integral (elementary in d = 2, a lens integral in d = 3) and the
average over the velocity law. This is the homogeneous case, which is the one the source solves
for a single ball in its (15); for a non-homogeneous isotropic intensity the same union-of-capsules
formula holds with lambda(dx) in place of lambda dx and the integrals become the source's "laborious"
ones. Open problem 1 (coverage) and Open problem 5 (stability of the space-time service system) are
untouched. Prior art unchecked beyond the source; the capsule (spherocylinder) volume of a ball swept
along a segment is classical, and the union-of-two-capsules integral is the only new ingredient.
