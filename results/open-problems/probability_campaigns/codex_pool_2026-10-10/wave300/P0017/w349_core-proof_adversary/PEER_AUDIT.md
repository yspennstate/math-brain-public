# w349 adversarial audit of w348 ATTEMPT.md

Audited 2026-10-10. Independent work was saved in INDEPENDENT.md and
WEIGHTED_GAP.md before opening the paired proof, and the L1 equality
witness in PEER_L1_INDEPENDENT.md was saved after reading the challenge
but before opening ATTEMPT.md. The full-target analytic input remains
unproved in both packets.

L1: KEEP the bound and sharpness. With N=p+q, the coefficient on the
left side of incidence identity (I), for an ordered pair F,G of
p-subsets with |F intersection G|=r, is binom(q-p+r,p). The right
coefficient is sum_s binom(r,s)binom(q-p,p-s), equal by Vandermonde.
The s=p term has coefficient 1 and is the sum of individual squared
norms. All terms are nonnegative because q>=p. The numbers of p- and
q-subsets of N agree, so cancellation yields exactly binom(q,p),
without a hidden factorial or dimension factor. The construction of
T_F requires both separate block symmetries; the sum over F within a
q-subset is precisely a permuted binom(q,p) P_q T. I independently
derived the sharpness witness using a different arrangement-count
formula; see PEER_L1_INDEPENDENT.md. p=q, p=1, zero tensor, nonzero W,
and an embedding from dimension 2 to larger dimensions cause no gap.
For dim H=1 the stated sharpness claim is deliberately not made.

L2: KEEP the stability bound binom(q,p)||P_qT||+(binom(q,p)+1)delta.
The two original block projections commute, but P_q and Q need not
commute. The proof uses contraction and a triangle inequality, so it
does not require that false commutation. The missing-symmetry example
has squared norm 2 and P_2T=0. No optimality of the error coefficient
is asserted.

L3: KEEP the all-degree centered-exponential-product special case.
The shifted exponential's normalized tilt kernel is exactly
(1-z)exp(zy); the centering factors cancel. Dividing the ordered
derivative tensor by d! contributes alpha!/d! after summing the
d!/alpha! repeated coordinates. Distinct coordinate supports are
orthogonal by the explicitly stated product independence and the
zero means of P_j. Within a support the frame need not be orthogonal;
the trace bound is valid for its positive frame operator. Taking the
direct sum across supports uses the maximum of their norms and adds
no number-of-supports factor. For a support of size s, the exact
composition-count bound is (d-s+1)/(d(s-1)!)<=1. The support of size
one attains B(d-1). At d=1 it gives 1, and the all-degree optimal base
is 2 by the central-binomial limit. This does not cover all
log-concave laws or directly remove the regularity assumption from
the cited analytic criterion.

L4: FIX the scope of the Taylor-derivative terminology, while keeping
the algebraic operator-norm identity. The displayed statement says:

> For a general centered isotropic probability mu with finite fourth moments, the degree-two tensor is

Finite fourth moments alone do not imply that exponential tilts are
defined on any neighborhood of zero. Let R have density 5 r^(-6) on
r>=1, let S be an independent fair sign, and set X=sqrt(3/5) S R.
Then E X=0, E X^2=(3/5)(5/3)=1, and
E X^4=(9/25)5=9/5<infinity. However E exp(zX)=infinity for every real
z!=0: the tail with the matching sign has positive exponential
growth and only polynomial decay. Thus F_f as previously defined is
not a well-defined tilted average there. This is a counterexample
to the stated general derivative domain, not to the log-concave
target or to the displayed quadratic-form duality identity.

Minimal repair: require the Laplace transform of mu to be finite on
an open neighborhood of zero (then shrink the neighborhood for all
L2 f), or define the displayed T_2 algebraically and explicitly say
that it equals (1/2)D^2F_f(0) whenever those tilts exist. Under the
original finite-fourth-moment assumptions the algebraic map
f -> (1/2)E[f(XX^T-I)] is bounded, and its norm equals half the
supremum of the standard deviations of centered quadratic forms.
Regular log-concave laws already satisfy the needed extra premise.

Full-target verdict: the selected unresolved input is still the
universal all-degree Hilbert-Schmidt bound for all L2 tilt averages.
The four checked component claims, including the scope repair, do
not prove KLS. Recent primary preprints claim proofs; current
openness and complete independent proof validity remain UNKNOWN.

NEXT: w348 apply the one-line L4 domain repair; w350 independently
checks the new results and the variance-weighted counterexample.

Follow-up 2026-10-10T05:04:44.462564+00:00: w348 applied the exact L4 repair. The current source defines U_2 as a quadratic-moment operator, with U_2=T_2 only under neighborhood exponential moments. Verdict w349-A006 KEEP closes the scope correction; A004 is retained as history.
