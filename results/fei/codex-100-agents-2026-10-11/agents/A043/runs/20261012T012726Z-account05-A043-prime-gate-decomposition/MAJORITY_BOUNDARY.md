# A nonbinary prime approaches the binary endpoint constant

Let g(y)=2 1[y1+y2+y3>=2]-1 on independent bits. This is an essential prime: for each two-coordinate block, the three cofactor rows, according to block Hamming weight zero, one or two, are (-1,-1), (-1,+1), and (+1,+1). Thus no block can be compressed to one Boolean wire.

Take 0<q<1/2, r=q^3, and physical probabilities (1-r,q,q). All inputs are interior. Put sigma_i^2=4p_i(1-p_i), d_S=g_hat_mu(S)/product_{i in S} sigma_i. Direct differences of the majority truth table give

    d1=2q(1-q),
    d2=d3=1-r-q+2rq,
    d12=d13=(1-2q)/2,
    d23=(2r-1)/2,
    d123=-1/2.

Every nonempty squared mass is sigma_S^2 d_S^2. Consequently

    P1=P123=16r(1-r)q^2(1-q)^2,
    P2=P3=4q(1-q)(1-r-q+2rq)^2,
    P12=P13=4r(1-r)q(1-q)(1-2q)^2,
    P23=4q^2(1-q)^2(1-2r)^2.

The deficit is exactly delta=2P12+P23+2P123. Corrected entropy is sum_{S nonempty} P_S log2(1/d_S^2); terms with zero d_S are zero by continuity.

As q decreases to zero, r=q^3 gives delta=4q^2+O(q^3). The pair {2,3} contributes 8q^2+O(q^3) to corrected entropy. Each of the singleton terms {2},{3} contributes 8q^2/ln(2)+O(q^3): d2^2=1-2q+O(q^2), and t log2(1/t)=(1-t)/ln(2)+O((1-t)^2) at t=1. The two mixed pairs have masses O(q^4) and bounded corrected logarithms. The {1} term is O(q^5 log(1/q)), and the triple term is O(q^5). Therefore

    Hplus_mu(g)=(8+16/ln(2))q^2+O(q^3),
    lim_{q->0} Hplus_mu(g)/delta_mu(g)=2+4/ln(2).

This is a fixed three-input prime, rather than a decomposable binary gate with dummy inputs. Hence any corrected product-biased constant proposed even just for three-input primes must be at least 2+4/ln(2). This transports the already known binary lower constant into the nonbinary prime class; it does not recompute the one-bit uncertainty tax, prove an upper bound on this curve, or produce a divergent ratio.

All remainder statements are ordinary finite rational-function Taylor expansions at q=0, with the one logarithmic term explicitly bounded. The denominator has leading coefficient 4, so division is legitimate for all sufficiently small positive q. The exact independent eight-assignment Fourier reconstruction and twelve dyadic checks are in code/certify_boundary.py and out/boundary_certificate.json. These finite checks corroborate the formulas; the displayed expansion proves the limit.

The finite grid {1/4,1/2,3/4} misses this endpoint path. In particular a moderate-bias grid maximum below seven cannot justify the same bound over all interior biases.
