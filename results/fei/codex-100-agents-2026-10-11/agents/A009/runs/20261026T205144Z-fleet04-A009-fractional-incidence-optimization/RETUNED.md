# Incidence-feasible retuning repairs the two-core test

For every integer r>=4 take precisely A010's physical Boolean function

    f_r=2 product_j OR(z0,z1,X_j1,X_j2)
            product_j OR(z1,z2,Y_j1,Y_j2)-1,

with all 2r private pairs disjoint. Entropy and costs are bits. Give each of its 2r width-four supports activation alpha=1/(2r). Choose an anchor uniformly from the 2r supports, force its mask uniform among its 15 nonempty subsets, and independently draw every other support empty with probability p=1-alpha or each particular nonempty mask with probability c=alpha/15. Decode the physical union. This is a fixed public reference, before the Fourier set is observed. No core dictionary, mixture branch or Fourier probabilities define it.

**Claim.** The resulting complete nonempty output cost C_Q(f_r) is less than 34 I(f_r), uniformly in r. This is a feasible certificate, not a claim of optimality or a universal FEI bound. The sampler changes the width-determined activation in A010's obstruction; it does not refute that obstruction at its stated hypotheses.

## All incidence rows and all actual runs

The z1 row sums to 2r alpha=1; z0 and z2 rows sum to r alpha=1/2; each private row is alpha<=1. Thus every physical coordinate incidence constraint holds with one global weight vector.

For a local-mask tuple u put K(u)=number of nonempty entries and mu(u)=product of its local probabilities. Summing actual (anchor,tuple) probabilities gives

    Q(A)=sum_{union u=A} K(u) mu(u),

because rho=sum alpha=1. Normalization follows from E_mu K=1, and empty output has zero probability. Anchors are distinct actual draws, not shuffled descriptions. Every compatible tuple is retained. The optimal posterior over these exact runs has cost -log2 Q(A); arbitrary posterior costs are this value plus a nonnegative KL divergence. Hence no selector, anchor or allocation charge is omitted.

Put N=2r. The finite binomial expansion yields

    p^(-(N-1))=(1+1/(N-1))^(N-1)
       <=sum_{k=0}^{N-1}1/k! <3,

where k!>=2^(k-1) for k>=2 and the finite geometric sum is <1. Therefore p^(N-1)>1/3 and p^(N-2)>1/3 for every N>=2.

For a nonempty pure-core output A contained in K1 or K2, choose one fixed such group. The r tuples having exactly one active clause in that group with mask A have total actual mass r c p^(N-1)>1/90. For A={z0,z2}, choose one clause in each group with masks {z0},{z2}. For A={z0,z1,z2}, use masks {z0,z1},{z2}. Each construction gives r^2 distinct tuples with K=2, so

    Q(A)>=2r^2 c^2 p^(N-2)>1/1350>2^-11.

These cases exhaust all seven nonempty subsets of the three-bit core. All their costs are <11, using the SAME globally feasible reference; a selected event lower-bounds full mass.

For ANY nonempty physical A, assign each coordinate in A to one support containing it and use these disjoint assigned masks. This is one compatible real tuple with K>=1. All local probabilities are >=c=1/(30r), so

    Q(A)>=c^(2r),   -log2 Q(A)<=2r log2(30r)<2r(5+r).

This assignment is only an analysis witness and does not choose or modify the sampler after seeing A.

## One original physical influence account

Writing a=(3/4)^r and s=(1+a)/2, the exact physical conditioning identities are

    I(f_r)=5/4-a/2-3a^2/4+(r/3)a(1+a)>5/4,
    M_private=a(1-a)+(a^2/2)(1-a^2)<7a/6.

For completeness, the Boolean expression is z1 OR [(z0 OR A_X)(z2 OR A_Y)], where A_X,A_Y are independent products of r private OR pairs. The middle bit contributes 1-s^2. Each private/outer group contributes s/2 times its sign influence 1-a+(2r/3)a; their sum gives the displayed I. Holding all three core bits fixed leaves two assignments of probability 1/8 with private conditional variance 4a(1-a), and one with variance 4a^2(1-a^2), giving M_private by Parseval. Thus these are physical rather than cloned influences.

For r>=4, a<=81/256<1/3 and ra<=81/64: its successive ratio is 3(r+1)/(4r)<=15/16. Also r^2 a<7. Check r=4,5,6,7 exactly; beyond 7 its successive ratio 3(r+1)^2/(4r^2)<=1, since r^2-6r-3>=0 for r>=7. Finally log2(30r)<5+r since 30<32 and r<=2^r. Consequently

    C_Q <11+2r(5+r) M_private
        <11+(7/3)(5ra+r^2 a)
        <11+(7/3)(405/64+7)=8083/192,
    C_Q/I <8083/240<34.

The pure-core bill is bounded by 11 times at most unit spectral mass, and the private bill uses its actual mass. Both are charged once to the same I>5/4. No entropy upper bound funds the reference.

## Scope and unpaid universal line

A010's fixed-t=1/16 entire individual-core-mixture lower bound and its joint-dictionary <24I repair remain valid. The broadened representation class that also permits global incidence-feasible activation retuning already has cost <34I on this same family, with no added dictionary. Thus the two-core obstruction does not force a joint dictionary once activation retuning is permitted. In contrast A009's preceding all-activation width-growing common-anchor obstruction is untouched: it explicitly allowed retuning, and its widths grow.

The useful next universal test must combine growing core/width geometry with optimized incidence weights. The first unsupported line is bounding the physical spectral mass outside low-cost core outputs for arbitrary overlapping supports; here it is exponentially small, M_private<7(3/4)^r/6. The proof supplies no such bound for an arbitrary Boolean core. This certificate is a mechanism separation on an existing test family, not a new FEI class or a resolution of full FEI.
