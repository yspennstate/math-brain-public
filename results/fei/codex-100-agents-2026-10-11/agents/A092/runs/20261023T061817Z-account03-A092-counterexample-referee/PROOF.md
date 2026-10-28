# Independent referee proof: the zero-phase obstruction

All logarithms are base two. This review accepts only
A096-ZERO-PHASE-QUERY-REFUND-OBSTRUCTION@1. The companion phase-funded
transaction theorem is read for context and is NOT independently accepted here.

## 1. Original Boolean definition, with no producer checker

The controller table indexed by the integer whose least significant bit is the
first coordinate is

    a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1).

Put b=1-a^2 and F(x,y)=a(x)+sigma*b(x)*chi_[k](y), for sigma in {-1,1}.
Every value is in {-1,1}: on b=0 it is a, and on b=1 it is sigma*chi_[k].
For the claimed witness k=3. The same argument works for every k>=3 and
every physical controller restriction. Let A_U=ahat(U), B_U=bhat(U), and
beta=sum B_U^2=E b. The original controller has beta=3/8.

The complete true squared Fourier law, supplied as the incoming reference,
is exactly

    P(U,0)=A_U^2,
    P(U,[k])=B_U^2,
    P(U,T)=0 at every other seed frequency.

This follows directly by Fourier expansion on disjoint physical cubes. In
particular the alleged counterexample is an actual Boolean function, rather
than a free probability law or an approximate Boolean vector.

## 2. The actual query and every refund

Choose any seed coordinate j. The seed h has Inf_j(h)=1 and singleton
coefficient E(h*y_j)=0. The FULL wrapper has Inf_j(F)=beta, which is 3/8
for the displayed controller. Thus the phrase "influence is one" in the
producer's statement refers to its parity seed, not to the full wrapper.
The local obstruction only requires positive wrapper influence, which holds.

Let M_j erase frequency coordinate j. No two occupied parent frequencies
have the same erased frequency with opposite j-membership. This is because
the only seed frequencies are empty and [k], and k>=3. Consequently
H(P)-H(M_j P)=0: the spectral erasure charge B_j is EXACTLY zero.

On the two physical outcomes the seed is respectively chi_[k]\{j} and
-chi_[k]\{j}. Their squared spectra coincide. The complete child laws
are both M_j P, including every controller atom. The supplied incoming
Q=P also has M_j Q=M_j P. Conditional occupancy KL compares identical
conditional laws on every positive fiber, so it is exactly zero. Each full
child's signed vacuum/controller blocks and its tail mass already match
their inherited reference. Both block-calibration KL refunds are exactly
zero. No estimate, neglected normalizer, or unused positive term is involved.

## 3. The prescribed nonempty change and its rigorous sign

The remaining seed pair K=[k]\{j} has at least two coordinates. Select any
remaining singleton L, so L is nonempty and L!=K. The prescribed conditional
nonempty law changes from delta_K to

    (63/64)*delta_K+(1/64)*delta_L.

Keep every vacuum atom A_U^2 fixed. On the tail, multiply this law by B_U^2
for each U. This is a COMPLETE normalized child reference; its new ghost
atoms are included and it is positive at all actual occupied atoms. Every
occupied tail probability is decreased by exactly 63/64, while every
occupied vacuum probability stays fixed. Therefore each full child has

    CE(P_child,Q_new)-CE(P_child,Q_old)
        = beta*log2(64/63).

Both fair physical children have the SAME increment, so their mean has this
increment too, rather than twice it. The entire query-plus-reset transaction
has this same positive increment because all preceding query refunds vanish.
For the original controller it is (3/8)*log2(64/63)>3/512: indeed
ln(1+t)>t/(1+t) at t>0, so ln(64/63)>1/64, and ln(2)<1.
This provides a sign certificate independent of numerical log evaluation.
The rational interval checker separately encloses the full CE difference.

The plain three-bit parity function with controller a=0,b=1 gives the even
smaller witness log2(64/63)>0. Two remaining seed bits are necessary for
this particular distinct-nonempty-point replacement; this is not a claim
of minimality among all conceivable reference counterexamples.

## 4. Exact target refuted, and the remaining account

The false proposed supplier is: at every relevant physical query, its current
erasure/conditional-occupancy/coherent-calibration refunds suffice to pay
every prescribed fixed positive nonempty-profile mixture. Here the total
current refund is zero and the complete required increase is strictly
positive. Equivalently relevance does not imply a positive uniform lower
bound on this current refund proportional to Inf_j(F). A positive controller
Gram constant does not help when d=0: Gamma=9/3584 but Gamma*d^2=0.

The phase-adaptive theorem explicitly selects zero strength at d=0 and is
NOT refuted. Nor does this example forbid payment from an unused original
bank. If the reached node has weight w, any pre-existing booked amount O
and every untouched full sibling remain booked, and the same reserve U
becomes exactly U-w*beta*log2(64/63). A successful original-bank payment
requires that amount of ACTUAL unused reserve. This proof neither invents
that reserve nor declares it absent. The first unsupported universal line
is a dimension-independent influence-paid source/surplus that funds a
necessary zero-singleton nonempty transport, with all old bookings retained.

## 5. Why this is not an FEI counterfamily

There are at most 2^(r+1) nonzero Fourier atoms for r controller bits,
independently of k. Thus

    H(F)=H((A_U^2)_U,(B_U^2)_U)<=r+1,
    I(F)=sum_U |U|*(A_U^2+B_U^2)+k*beta.

These are exact identities from the actual spectrum. For any fixed
controller with beta>0, H(F)/I(F) tends to zero as k grows. For the
displayed controller r=4, H(F)<=5 and I(F)>=3k/8. This family therefore
cannot disprove FEI. Entropy remains unchanged by the query even though
its FULL wrapper influence is positive; that distinction is the obstruction.

## 6. Validation independence and scope

The new checker constructs every original truth-table value, applies its own
integer butterfly transform, computes physical edge influences, restricts
the truth table on both actual outcomes, and charges both complete terminal
references. At the source seven-bit witness it also compares all coefficients
against direct character sums. It imports only A092's already checked exact
arithmetic primitives, not A096's implementation. Its finite controller/
parity domain does not prove generality; Sections 1--5 provide that proof.
No formal proof assistant certificate or broad phase-funded claim acceptance
is asserted.
