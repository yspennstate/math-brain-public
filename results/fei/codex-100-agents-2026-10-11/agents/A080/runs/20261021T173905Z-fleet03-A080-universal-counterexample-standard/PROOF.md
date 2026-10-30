# Tensor activation: three different limiting ratios

All functions below are actual signs on finite uniform cubes. All entropies use bits. Fix a nonconstant seed g, and put J=I(g)>0, h=H(g), R=h/J, m=E g, and p_*=(1-|m|)/2>0. For integers t,k>=1, let G be the product of t disjoint copies of g. Let A indicate one vertex of k fresh selector bits, a=2^(-k), and let F=1+A(G-1). Thus F equals G at that selector vertex and equals +1 elsewhere. Let p=(1-m^t)/2; importantly p_*<=p<1, even when the seed is not minority-oriented. The output minority of F is q=ap<1/2. Write v=Var(F) and rho for its squared Fourier law conditioned on a nonempty set.

## Statement

For every fixed seed and every sequence k->infinity and arbitrary integers t=t(k)>=1, set x=tJ/k. Whenever x has a limit lambda in the extended interval [0,infinity], the following limits hold:

| ratio | lambda finite | lambda=infinity |
|---|---|---|
| H(F)/I(F) | (lambda R+4)/(lambda+1) | R |
| H(F)/(I(F)-h2(q)) | (lambda R+4)/(lambda+1/2) | R |
| H(rho)/(I(F)/v) | (lambda R+2)/(lambda+1) | R |

The formulas at lambda=0 are respectively 4, 8 and 2. They remain valid when t is bounded or oscillates. No limiting unbounded-dimensional function is used: each individual F has tn+k finite input bits.

In particular the largest attainable limiting values within this fixed-seed tensor/activation mechanism are exactly max(R,4), max(R,8), and max(R,2), respectively. All three endpoint maxima are attainable with q->0 and I(F)->0. Thus a fixed seed cannot be amplified to an unbounded FEI ratio by any such schedule. A gap ratio tending to 8 is already produced by a dictator seed, whose tensor powers have entropy zero. This is a normalization effect, not a FEI disproof or a new universal FEI lower bound of 8.

The ceilings above concern limits, not exact finite bounds. The checked dictator activation at k=3 has q=1/16, I=1/2 and H=6-(49/32)log2(7). Its output-gap ratio is strictly greater than10, although its ordinary ratio is less than4. The exact outward certificate is out/FINITE_GAP_GUARD.json. This actual boundary example shows why the error terms in (9) cannot simply be discarded at finite width.

## Complete Fourier calculation

Tensoring gives H(G)=th, I(G)=tJ, and E G=m^t=1-2p. For data set S and selector set T the coefficients are 1-2ap when S=T=empty, -2ap when S=empty and T is nonempty, and a*Ghat(S) when S is nonempty, for every T. Selector-point character signs do not affect squares. Hence

    q=ap, v=4ap(1-ap), I(F)=a(tJ+2kp).                 (1)

The physical-edge calculation is independent: a data coordinate is active with probability a, and each selector has influence 2ap. It agrees with (1), including all control inputs.

Write ell(z)=z log2(1/z), including ell(0)=0. Retaining the constant atom and the control-only atoms gives

    H(F)=a[th-ell((1-2p)^2)+2k*4p(1-p)]
          +ell((1-2ap)^2)+(2^k-1)ell(4a^2p^2).        (2)

Expanding just the last term, an exact rearrangement is

    H(F)/a = th+8kp(1-ap)+E,
    E=-ell((1-2p)^2)-8(1-a)p^2 log2(2p)
      +ell((1-2ap)^2)/a.                             (3)

This calculation needs no approximation, independence of spectral coordinates, FEI premise, child admission or discarded terminal entropy.

## Uniform errors, including denominators

The following deliberately conservative constants hold for every t,k>=1:

    |H(F)/a-th-8kp|<=32,                             (4)
    0<=h2(ap)/a-kp<=3,                               (5)
    |h2(v)/a-4kp|<=16.                               (6)

For completeness, ln2>2/3 from the positive atanh series, ell(z)<=1 for 0<=z<=1, and -(1-z)log2(1-z)<=z/ln2. These imply (5) directly: its remainder is ell(p) plus the latter term divided by a, bounded by 1+3/2<3. In (3), the absolute value of its logarithmic term is at most 8[p^2+p^2 log2(1/p)]<=16. The first term has absolute value at most 1, and the constant-atom term is nonnegative and at most 4p/ln2<=6. Finally 8akp^2<=4 because k/2^k<=1/2 for every integer k>=1. Their sum is at most 27<32, proving (4).

To prove (6), put y=v/a=4p(1-ap), so 0<y<=4 and 0<v<=1. The exact remainder is

    h2(v)/a-4pk = -4akp^2+ell(y)
                    -(1-v)log2(1-v)/a.

The three absolute bounds are 2, 8 and 6: |ell(y)|<=8 on [0,4] (on [0,1] it is <=1; on [1,4], y log2 y<=8). This proves (6), including v=1 by continuity, although nonconstant seeds here have v<1.

The denominator of the gap ratio is positive for all sufficiently large k, uniformly in t, without canceling an uncontrolled quantity. Indeed with B=tJ+kp, (5) gives

    (I(F)-h2(q))/a=B-c, 0<=c<=3,
    B>=kp_*, so B-c>0 whenever k>3/p_* .             (7)

Only this eventual domain is needed for every limit or uniform bound below. No assertion about a zero denominator outside that domain is used.

The nonempty law is well defined because v>0. The entropy chain rule gives

    H(rho)/(I(F)/v)=[H(F)-h2(v)]/I(F).               (8)

Equations (4) and (6) therefore leave numerator th+4kp with absolute error at most 48 after division by a. This retains the variance normalization on both entropy and influence. Raw H(rho)/I(F) is a different quantity.

## Quantitative no-growth bounds and all schedules

Let K0=max(R,4), K1=max(R,8), K2=max(R,2). Convex weighting of th=R*tJ and the selector terms in (4)-(8) yields

    H(F)/I(F)<=K0+32/(tJ+2kp),
    H(F)/(I(F)-h2(q))<=K1+(32+3K1)/(tJ+kp-3),
    H(rho)/(I(F)/v)<=K2+48/(tJ+2kp),                (9)

where the middle bound uses k>3/p_*. Each error tends to zero uniformly over all t>=1 as k->infinity. Thus oscillating schedules cannot evade the ceilings by having no limiting t/k. This also handles R=0, e.g. parity seeds, and biased seeds of either orientation. A constant seed is excluded: J=0, R is undefined, and tensoring a constant cannot provide a high-ratio seed.

For the sharper phase formulas, divide (4), (7), and (8) by k. If x->lambda>0, then t->infinity and |m|<1 implies p->1/2. This gives precisely the displayed rational functions. If lambda=0, p may fail to approach 1/2, but p>=p_*>0, tJ/k->0, and th/k=R*tJ/k->0. The remaining quotients are 8p/(2p)=4, 8p/p=8, and 4p/(2p)=2, with errors O_g(1/k). If lambda=infinity, divide instead by tJ: k/(tJ)->0, all bounded errors vanish, and each limit is R. These are finite algebraic limits, not interchanges with infinite spectral sums.

To attain lambda=0 use t=1. To attain a finite positive lambda use t=max(1,floor(lambda*k/J)). To attain lambda=infinity use t=k^2. Each has a*t->0, so (1) gives I(F)->0 and q<=a->0. Endpoint ceilings in (9) are therefore sharp as limiting suprema for this mechanism, even inside every fixed rare-small-influence sector.

If k remains bounded while t->infinity, (4)-(8) instead give all ratios ->R. If both k and t remain bounded there are only finitely many functions from the fixed seed. Consequently there is no hidden fixed-width route to an unbounded ratio. The eventual-gap argument applies to k->infinity; for a bounded k and t->infinity the growing tJ makes (7) positive as well. Any exceptional finite set is irrelevant to unboundedness and is not discarded in claims of exact finite inequalities.

## What remains unpaid

The unrestricted rare-core supremum equality proved in the previous A080 stage remains unchanged. It allows the seed itself to vary, whereas (9) controls amplification from each fixed seed. A universal bound for arbitrary retained rare-core H/(I-h2(p)) must be at least 8 because of the actual point-defect sequence above, and must still pay arbitrary seed entropy. A dimension-independent upper bound on those arbitrary seed ratios, or an actual sequence of seeds with unbounded ordinary H/I, is the first unsupported universal line. No such bound or sequence is supplied here. Finite signed-bank transfers such as A089's seven third-query alternatives retain their stated scope; this proof neither assumes nor establishes their indefinite continuation.
