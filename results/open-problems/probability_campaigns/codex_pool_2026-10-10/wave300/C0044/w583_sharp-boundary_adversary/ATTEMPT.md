# C0044 adversarial attempt

Author w583; 2026-10-10. No parent-problem proof or novelty claim.

## Exact mathematical target

For each fixed integer d >= 3, take nearest-neighbor RWRE on Z^d whose site transition vectors are iid with one common law supported on strictly positive vectors summing to one. For each fixed deterministic nonzero real direction ell, let A_ell = {X_n dot ell tends to +infinity}. With the annealed law P_0 = E[P_(0,omega)], determine whether P_0(A_ell) is always in {0,1}. Uniform ellipticity is a stronger subcase, not a hypothesis of the full strictly elliptic version. A simultaneous random-direction statement is not asserted.

Primary statement sources: Zerner, arXiv:0706.0745, introduction; Slonim, arXiv:2108.11424v3, introduction and Theorem 2.1 (the latter is a planar bounded-jump result). Slonim calls the d>=3 question open as of 2023. A September 2026 public preprint now claims a solution. Current openness: UNKNOWN until the actual manuscript and matching proof receipt are checked. The comparator statement containing `sorry` alone is not such a receipt; it does not refute a separate actual proof.

## Hardest remaining target step

Kalikow's union law is P_0(A_ell union A_-ell) in {0,1}. Since the two events are disjoint, the new step is excluding coexistence: P_0(A_ell)*P_0(A_-ell)=0. A harmonic or restart argument must supply an iid-specific reason for that conclusion. An environment-dependent positive escape probability at every individual site is not a uniform escape floor over sites.

## Independent obstruction and check

INDEPENDENT.md was saved before opening w582's proof. It constructs, for every 0<kappa<1/(2d), an explicitly uniformly elliptic outward-drift environment with P_0(A_+)=P_0(A_-)=1/2 and a nonconstant bounded harmonic h(k). The infima of h and 1-h are both zero. The counterexample is NOT stationary iid and thus only rules out a stronger auxiliary lemma omitting iid. The symmetric maximal-ellipticity endpoint kappa=1/(2d) gives recurrence of the projected coordinate and no directional escape.

check_boundary.py passed 1,296 exact rational harmonic equations and 688 values from an independently eliminated finite-interval linear system over 16 environments. This is algebraic verification, not independent mathematical review or a formal proof of C0044.

## Paired proof audit

Read w582/ATTEMPT.md after saving the independent derivation. L1 (global escape floor suffices) and L2 (irreducible positivity propagation and extreme infima in the mixed case) receive scoped KEEP in PAIRED_PROOF_AUDIT.md. They do not derive the floor from iid. My construction adds arbitrary kappa below 1/(2d), symmetry q(0)=1/2 and the maximal-ellipticity endpoint to the independently obtained asymmetric CE1 in w582's file.

The local intake source is Drewitz-Ramirez, Open question 3.2. C0044-A002 had already corrected A001's empty-intersection error. SOURCE_CORRECTION.md identifies a separate surviving erroneous reason for rejecting the quenched martingale: dependence on the whole environment does not prevent its path-filtration conditional-expectation identity. The actual missing step is excluding its zero limit.

NEXT: Freeze the reviewed arbitrary-kappa obstruction and the exact source correction as clearly labeled concept drafts; leave iid noncoexistence open in this packet.
