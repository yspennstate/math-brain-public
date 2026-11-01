# Exercised resets on a rare-core history

The first reference conversion has a positive debit for every n>=3. All subsequent data conversions have nonpositive signed reset. A single original child allocation pays the first debit and a prior quarter-bit charge, and keeps at least 3/20 bit at every data stopping frontier. This is a scoped C024/C019 result. Full FEI remains open.

## Family, source and transaction

All logarithms defining entropy are base two. Physical bits x,a,b,z_1,...,z_n are independent and fair. Let

    F=(-1)^a                         when x=0,
    F=1-2*1[b=1,z_1=...=z_n=0]      when x=1.

Take n>=2. The source reference is the FULL product of the actual root spectral marginals, Q_0=product Ber(Inf_j(F)); it is not the completed nonempty occupancy reference M used by A036 and earlier A037. Its initial KL resource is A=TC(F). Query a. Write m=n+2 and d=2^(1-m). The two actual children are a point defect p_m and -X p_m, where X=(-1)^x. The defect vertex has x=1,b=1,z=0; changing its location changes phases only. The two spectra differ by translation of their x mask.

After this query, actually replace both Bayes references by their actual full products. Then query any adaptive sequence of distinct z coordinates, with arbitrary stopping, replacing each reached reference by the actual product after each query. The bits x,b stay unqueried. All inactive branches and all terminal Fourier entropies and KLs are retained. An external prior debit omega=1/4 bit is genuinely booked against the same original allocation specified below. This is an accounting charge, not a proof that some particular upstream physical operation has exactly that cost.

For a common coherent physical kernel, the established finite KL chain is

    K_parent = E + O + mean K_predicted,
    sigma = mean TC_child - mean K_predicted.

Here E is the erased-coordinate conditional KL, O is physical-outcome KL, and sigma is the signed cost of an EXERCISED reset to the child products. Thus

    O + mean TC_child - K_parent = sigma-E.                 (1)

The kernel is k(y|T)=P_y(T)/(2q(T)), q=(P_0+P_1)/2, with a fair extension on source-zero fibers. This same kernel acts on actual and reference laws. Positive actual states have positive product reference mass. All sums are finite; only positive actual masses enter logarithms. No conditioning after the reset continues to use the old Bayes reference.

## Exact initial debit

The root has influences 1/2,1/2,d,...,d on x,a,b,z. At the a frontier, each child has marginal entropy m*h2(d); the x marginal of the twisted child is 1-d and all other child marginals are d. The residual parent and its product reference are invariant under toggling the x spectral mask; the two physical children swap under this toggle. Consequently the two reference outcome probabilities are exactly 1/2 and O_a=0.

Put H_m=H(p_m), H_1=0. The two disjoint a-bearing root Fourier atoms have mass 1/4 each; the remaining half of the root spectrum consists of two copies of the spectrum of p_(m-1), each scaled by 1/4. Therefore

    H(F)=2+H_(m-1)/2,
    H(children)=H_m,
    TC(F)=2+(m-1)h2(d)-2-H_(m-1)/2,
    mean TC_child=m*h2(d)-H_m.

The complete first-conversion excess is exactly

    D_m=O_a+mean TC_child-A
       =h2(d)+H_(m-1)/2-H_m.                              (2)

In particular (1) gives D_m=sigma_a-E_a. A positive D_m is a real uncovered debit after the initial erasure release, rather than a diagnostic component of an unexercised future conversion.

Since H_m-H_(m-1)/2=B_m+JS_m>=0, D_m<=h2(d). For m>=4, d<=1/8 and h2(d)<=h2(1/8)<3/5. The latter strict sign is independently certified by rational log intervals. Entropy monotonicity on [0,1/2] follows from h2'(t)=log2((1-t)/t)>=0.

For the positive sign, define g(t)=-2(1-t)^2 log2(1-t), with g(1)=0 by continuity. The exact point spectrum yields

    H_m=g(d)+2(2d-d^2)(m-1),
    H_m-H_(m-1)/2=g(d)-g(2d)/2+4d+(2m-6)d^2.              (3)

For m>=10, g(d)<3d (use -(1-d)ln(1-d)<=d and ln2>2/3), g(2d)>=0, and (2m-6)d<1. The last inequality holds at m=10 and decreases thereafter. Thus (3) is less than 8d. Meanwhile h2(d)>=(m-1)d, so D_m>(m-9)d>0. The remaining m=5,...,9 have strictly positive interval certificates. At m=4 the sign is NEGATIVE, which the first pilot exposed. Hence the positive-debit theorem is n>=3, not n>=2. The n=2 boundary remains covered by the budget with [D_m]_+=0.

## Every later product reset is nonpositive

Consider an active p_l or its x twist, querying one of the remaining private z bits. Put t=2^(1-l) and beta=2t(1-t). Toggling an unqueried x spectral mask conjugates the actual law, product reference, coherent kernel and reset, so it suffices to treat p_l. The inactive physical child is constant and the active child is p_(l-1). Let

    phi(u)=h2(u)-h2(2u)/2,
    q0=(1-t)^2+t^2,
    r=(1-t)^(l-1)/(2q0).

All source fibers are positive for l>=2. The inactive physical outcome has reference probability r: only its empty residual Fourier fiber can produce that outcome. Thus

    O_l=-log2(4r(1-r))/2,
    JS_l=phi(beta),
    Gamma_l=(l-1)phi(t),
    sigma_l=O_l+JS_l-Gamma_l.                             (4)

The last line is the product-reference reset identity; it also follows by directly expanding the finite KL likelihoods. For l=2, O=0 and JS=Gamma=1, so sigma_2=0 exactly. The three cases l=3,4,5 have strict negative rational interval certificates.

Here is a uniform proof for l>=6. The positive series for binary entropy gives

    u <= phi(u) <= u+u^2/((1-2u)ln2)       (0<=u<1/2).

Since t<=1/32 and beta<=1/16, ln2>2/3 gives

    JS_l <= beta+2beta^2 <= 2t+8t^2 <= (9/4)t,
    Gamma_l >=(l-1)t >=5t.                                (5)

Set alpha=2r-1. Both (1-t)^(l-1) and q0 lie in [1-(l-1)t,1], by Bernoulli's inequality and l>=3. Since q0>=1-2t>=15/16,

    |alpha| <= (16/15)(l-1)t <=1/6.

The sequence (l-1)t decreases for l>=3. Use -ln(1-u)<=u/(1-u), and ln2>56/81>24/35 (the first two positive terms of its atanh series) to obtain

    O_l <=(3/4)alpha^2
        <=(64/75)(l-1)^2 t^2 <=(2/3)t.                   (6)

The last inequality holds at l=6, where (l-1)^2 t=25/32, and this sequence decreases thereafter. Combining (4)-(6), sigma_l<=-25t/12<=-2t. This is an all-dimensional bound, not extrapolation of the scalar census. Inactive constant or x-character branches have deterministic spectra and zero conversion cost.

At every later active query (1) now gives

    O_l+mean TC_child-TC_parent=sigma_l-E_l<=0.             (7)

Summing (7) with actual physical reaches proves that no additional surplus withdrawal is needed after the first exercised conversion. Different adaptive queries and stopping times preserve this local conclusion. Nonpositive resets are retained in the same ledger, not booked as separate new influence or surplus resources.

## The original bank survives conditioning

For every point defect p_l, H_l<=4 I_l=4lt. Indeed g(t)<=2t/ln2 and the remaining term in H_l is at most 4(l-1)t; ln2>1/2 gives the claim. The l=1 character has zero entropy. A twisted active defect has

    I(X p_l)=1+(l-2)t,
    4I(X p_l)-H_l >=4-8t>=2     for l>=3.

For l=2 it has H=2,I=1 and surplus exactly 2. An inactive twisted branch is an x character with surplus 4. Because only z bits are queried, every descendant of the initial a=1 child is one of these cases with l>=2. Every descendant of the a=0 child is a point defect or constant and has nonnegative surplus.

At the INITIAL a frontier, reserve one bit globally from the a=1 child: its reach is 1/2 and its actual S4=4I-H is at least 2. Carry this very same allocation through all descendants. Book the prior global debit 1/4 by placing conditional debit 1/2 on each terminal of that lineage. Book the first actual excess [D_m]_+ by placing conditional debit 2[D_m]_+ there. Do not renew either debit after queries. At every terminal of that lineage,

    original carried debit =1/2+2[D_m]_+
                           <=1/2+2h2(d)<17/10,
    actual terminal S4 >=2.

The unused conditional allocation is at least 3/10 and the lineage still has total reach 1/2. Hence every stopping frontier retains at least 3/20 bit globally after both bookings. This is a pointwise descendant certificate for one original allocation; it does not rely on replacing the bank by each new mean terminal surplus. Equation (7) pays all later reset transactions without drawing from that allocation again.

The terminal entropy is always still present. If L is any allowed frontier and C_past denotes the later outcome KLs after the first reset, then weighted (7) gives

    C_past+E TC_L <= mean TC_at_first_frontier.

The actual complete terminal cost remains E[H_L+TC_L], with the original booked debit tracked separately. Nothing here removes H_L, pays an arbitrary source reference by influence, or certifies an unmentioned upstream charge. The construction shows that repeated exercised resets need not invalidate one precisely owned surplus payment.

## Checks, rung and remaining gap

Failure checks: initial sign at n=2, reset signs at l=2,...,5, the l=1 stopping boundary, outcome normalization, spectral/physical influence agreement, x-twist conjugacy, exact power-of-two logarithms, actual replacement of references, and individual terminal surplus after both bookings. The frozen raw domain is n=2,...,6; the scalar domain is l=2,...,20. Integer Walsh spectra and Fraction kernels are compared against the formulas. Every terminal entropy, influence, current reference KL and inherited debit is saved. Interval overlap is used only as a consistency check; the identities follow from the displayed finite algebra.

Rung: proof with exact finite base certificates, independent review pending. A separate core-Lean target concerns only a scaled integer allocation inequality; its result does not formalize the entropy or all-history argument. The full mathematical claim is not labelled Lean-checked.

First unsupported universal line: replace this hereditary point-defect/x-twist surplus certificate and nonpositive data-reset rule by an eligible rule for arbitrary unequal non-flat cores, while keeping the prescribed ORIGINAL occupancy reference or paying its actual conversion. In particular, this full-product source result does not inherit the earlier occupancy margin. No universal FEI constant improves.
