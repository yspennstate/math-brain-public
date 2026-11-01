# The separate remainder R need not be nonnegative

19 September 2026. This corrects one suggested stronger target in Section 7
of ../2026-09-19-sidorenko-mixed-spectrum/MIXED_SPECTRUM.md. It does not
invalidate its local theorem, positive-part identity, or structured results.

The proposed assertion R(U)>=0 is false already for an exactly regular,
strictly positive two-block kernel lying inside the proved local neighborhood.
The full Sidorenko inequality is not refuted.

## Exact example

Take block probabilities p=(1/3,2/3) and

    W = [[4/5, 11/10], [11/10, 19/20]].

Its weighted row sums equal one, and ||W-1||_infinity=1/5. Set
f=(2,-1)/sqrt(2). Then E f=0, E f^2=1, (E f^3)^2=1/2, and

    W=1+lambda f tensor f,        lambda=-1/10.

Put z=(E f^3)^2. On rank two, each selected graph with e edges and 2k
cubic vertices contributes lambda^e z^k. The residual defined by actual
edge subsets in the mixed-spectrum note is therefore exactly

    R = 50z lambda^9 + 15z^2 lambda^10
        +(90z+60z^2)lambda^11 +(145z^2+10z^3)lambda^12
        +75z^3 lambda^13 +15z^4 lambda^14 +z^5 lambda^15.

At the stated rational parameters this is

    R = -806029701 / 32000000000000000 < 0.

A separate direct five-variable contraction, which does not use that
residual polynomial, gives

    t_H(W) = 32016482386770299 / 32000000000000000 > 1,
    P_+(U) = 203991 / 40000000000 > 0,
    P_+(U)+R(U) = 162386770299 / 32000000000000000 > 0.

The checker verifies all equalities with exact integers and fractions.
It also verifies the kernel normalization and the claimed eigenfunction
without taking irrational square roots.

## Why this failure is structural

For any fixed z>0 coming from a bounded nonconstant skewed two-point
law, W=1-r f tensor f is nonnegative for all sufficiently small r>0.
The residual polynomial then has

    R = -50z r^9 + O_z(r^10) < 0

for sufficiently small r. Thus the failure is not a rounding issue or a
large-amplitude exception. The first negative ninth-order interactions can
be outweighed by the positive sixth- and eighth-order terms, as the
local theorem already proves, but they cannot be declared nonnegative
on their own.

The stronger combined target

    P_+(U)+R(U)>=0

is not disproved by this example and remains unproved in general. The exact
bound needed merely for Sidorenko is weaker still:

    R(U)>=-5Tr(U^4)-10Tr(U^6)-P_+(U).

The balanced-moment certificate in BALANCED_MOMENTS.md estimates the whole
fifth trace, so it does not make the invalid separate-remainder assertion.

Run python check_residual.py to regenerate residual_checks.json. These
are same-assistant exact checks, not an independent audit. No publication
novelty is asserted for the observation.
