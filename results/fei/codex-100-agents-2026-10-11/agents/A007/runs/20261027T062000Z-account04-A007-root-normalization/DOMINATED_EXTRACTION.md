# Finite positive-core extraction with the full normalization refund

All cubes are uniform, all costs are in bits. The universal paid source remains open.

## A sector lemma without common amplitude scaling

Let p and u be nonnegative weights on a finite alphabet E, with v=sum p>0, and suppose u(e)>=a p(e) for a>0. Let R be a subprobability reference on a larger finite alphabet, fixed before the target, covering every e with u(e)>0. Write Z=sum_E R(e), r(e)=R(e)/Z, and

    D=sum_E u(e) log2(1/R(e)),
    B=sum_E (u(e)-a p(e)) log2(1/R(e)).

Zero-weight terms have value zero; coverage makes all other terms finite. Since R has total mass at most one, each logarithm is nonnegative, B>=0 and 0<Z<=1. Direct expansion gives the EXACT identity

    C_p(r)=(D-B)/a + v log2 Z.                       (1)

Thus C_p(r)<=D/a+v log2 Z<=C_total(u;R)/a whenever the latter includes D with nonnegative other costs. This is a finite change-of-measure statement, not a new reference supplier. Both the signed normalization and the surplus B are retained before taking the inequality. The condition u>=a p is essential to the inequality, not to the algebraic identity.

For a rare-root sector R(e)=tau r(e), sum r=1, equation (1) becomes

    D-B=a C_p(r)+a v log2(1/tau).

The entire rarity av log2(1/tau) cancels with av log2 Z. Unequal scaling also puts (sum u-av) log2(1/tau) in B; omitting B would leave an artificial rarity bill. This cancellation holds for every 0<tau<=1, including arbitrarily rare sectors. A normalized whole-output law can assign the remaining mass outside E. No selected-witness entropy or unnormalized mass is substituted for actual output mass.

There are TWO different normalizers in a root-source application. Let Q be the original raw successful output law, theta=Pr(initial root set nonempty)>0, with sum Q<=theta, and R=Q/theta its conditioned output law. Put Q_E=sum_E Q, so Z=Q_E/theta. With D_Q and B_Q defined using raw Q instead of R, exact substitution gives

    D_R=D_Q+(sum_E u)log2 theta,
    B_R=B_Q+(sum_E u-av)log2 theta,
    C_p(r)=(D_Q-B_Q)/a+v log2 Q_E.                  (1a)

The original root normalizer cancels algebraically against the sector normalizer; it was not dropped as negative. This holds for every theta with 0<Q_E<=theta<=1, with the SAME raw generator. It refunds one nested conditioning event and does not pay repeated roots, labels or attachments. For independent root activities x_l=lambda_l*pi_l, theta=1-prod_l(1+x_l)^-1; no product-root hypothesis is needed for(1a). The actual hard task is still bounding D_Q-B_Q+av log2 Q_E under the spectral law.

## Application to A015's overlapping positive anchors

Fix a nonconstant monotone sign function g on s>=1 bits, and any fixed finite positive CNF G=(1+g)/2=AND_j C_j with nonempty clauses. Repeated or redundant anchors are allowed. Make L copies of each anchor, each with its own positive private bit, exactly as in A015-POSITIVE-ANCHOR-MONOTONE-UNIVERSALITY@1. Set epsilon=2^-L, b(z)=number of false anchors, q=Pr[g=-1], m(z)=2 epsilon^b(z)-1. Then m=g+d, where d is nonnegative, supported on false cores and E d<=2qepsilon. Hence for EVERY core Fourier set S,

    |Fhat_L(S,empty)-ghat(S)|<=2qepsilon.             (2)

For a nonempty S, any nonzero Boolean Walsh coefficient has magnitude at least 2^(1-s): its integer numerator is an even, nonzero sum of 2^s signs. Set rho=2^s qepsilon and require rho<1. Then

    Fhat_L(S,empty)^2 >= (1-rho)^2 ghat(S)^2.         (3)

At a zero coefficient of g this remains true. E is ALL nonempty core sets, chosen from the fixed representation before a Fourier target. Thus (1) applies with p=ghat^2, u=Fhat_core^2, a=(1-rho)^2 and v=Var(g), for ANY supplied subprobability nonempty reference covering F_L. In particular, u has no common scaling requirement. All original labels, local choices, signed fusion, attachment and output ambiguity must already be included in R. No new free label or adaptive reset is asserted.

## Explicit finite (1+delta) transfer

First orient the monotone core by choosing h=g or h(z)=-g(-z) so that q=Pr[h=-1]<=1/2. This duality preserves monotonicity, squared spectrum, variance and influence. Under the coordinate negation the coefficients acquire signs only, so the extracted reference also prices g.

For 0<delta<=1 let A be the least integer with 2^A>=16/delta, and choose

    L=2s+2A, epsilon=2^-L, rho=2^s qepsilon,
    a=(1-rho)^2, d0=(s+L)epsilon.

A015's physical bound and Poincare give I(F_L)<=I(h)+2q(s+L)epsilon<=(1+d0)I(g). Here I(g)>=Var(g)=4q(1-q)>=2q; nonconstancy guarantees every denominator is positive.

For s>=1, s/4^s<=1/4 and 4^-s<=1/4. Also A<=16/delta: on each dyadic interval ceil(log2 x)<=x for x>=2. Consequently

    rho<=4^-A/4<=delta^2/1024<=delta/1024,
    d0=(3s+2A)4^-s4^-A
       <=(3/4+A/2)delta^2/256
       <=3delta^2/1024+delta/32 < delta/16.

In particular rho<1. Since a>=1-2rho>=1-delta/512, and

    (1+delta)(1-delta/512)-(1+delta/16)
       =delta(479-delta)/512 >0,

we have (1+d0)/a<=1+delta. Thus ANY fixed supplied nonempty source satisfying C_total(F_L;R)<=K I(F_L), K>=0, yields the FINITE normalized core reference

    C_g(r)<= (1+delta) K I(g).                       (4)

Equation (1), with its negative Var(g)log2 Z and surplus B, is the exact extraction underlying this upper bound. This closes the finite arbitrary-reference transfer left open by A015's entropy-limit reduction. It does not recover a false common-scaling identity, improve A008's signed-point multiplicity, pay a universal source or identify monotone FEI with full FEI. The extra O(s) private multiplicity comes from Boolean coefficient granularity, not an asserted optimality bound. The full empty/nonempty entropy wrapper remains separate.

## Checks that could fail

The physical nesting used by A015 needs positive anchors; equal-probability incomparable signed groups violate it. Dominance requires rho<1 and Boolean granularity; arbitrary real targets can have arbitrarily small nonzero coefficients. A reference of mass greater than one can give negative code lengths, invalidating B>=0. A finite source covering F_L need not dominate g at small L without the displayed rho hypothesis. All these conditions are checked where used. Small physical positive lifts, redundant anchors, the AND2 unequal-scaling control, exactly normalized rare-sector laws and the no-domination countercontrol are in code/check.py. The mathematical rung is an analytic proof with exact finite checks; independent acceptance is pending.

The first unsupported universal line is still a core-sensitive ORIGINAL source R with complete C_total(F_L;R)<=K I(F_L), from the same unused physical influence account. No calculation here supplies it.
