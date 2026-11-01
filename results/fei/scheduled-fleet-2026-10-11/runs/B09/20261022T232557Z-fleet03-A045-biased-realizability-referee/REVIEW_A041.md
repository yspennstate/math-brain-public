# Scoped reconstruction of the new quadratic coherence clauses

Source: A041-SHARP-QUADRATIC-COHERENCE-CHARGE@1, exact statement SHA256 c958945c4cc6ab13b72c1d24659df0a678cd4ec0ae40067aaa88ef81b62df150, run20261021T190738Z-fleet03-A041-weighted-threshold-fei. No source checker is copied or executed. The canonical squared-tail reference and supplied all-bias symmetric-threshold baseline remain declared dependencies. A045 contributed the earlier canonical-reference dependency, so this is independent reconstruction of A041's NEW coherence, sharpness, overlap and tax clauses, not a claim of a wholly independent reconstruction of the complete earlier dependency chain.

## Signed amplitudes before selecting the direction

For the B-frequency label T, integrate its actual physical coefficient on the B complement, obtaining the signed normalized count profile h_T(k). Write its canonical jumps as alpha_j=(h_T(j)-h_T(j-1))/2. For nonempty A label U the constant part disappears, so the full normalized coefficient is sum_j alpha_j c_j(U), with c_j the normalized product Fourier coefficient of the physical count tail on A. Squaring only after this sum gives P(U,T)=v_(U,T)(sum alpha_j c_j)^2. The diagonal reference is K_A=v_(U,T)sum alpha_j^2 c_j^2. Finite Cauchy gives P<=r_A K_A, with r_A the number of nonzero canonical jumps. Reverse the groups to obtain P<=r_B K_B. If r_A<=r_B then P<=r_A K_A<=r_A max(K_A,K_B), and conversely. Thus P<=min(r_A,r_B)K_star. On occupied support every divisor and jump count is positive.

It follows directly that C_star-E_mix=sum P ln(P/K_star)<=sum P ln min(r_A,r_B). This is a logarithmic coherence debit, not a proof that the debit is bounded by an absolute mixed-deficit price. No selected part of K is assumed to be Boolean or an integer mixed-difference profile.

## Complete normalizer and ordinary KL

Physical count tails have disjoint one-coordinate derivative supports. Applying Parseval to that derivative identity gives sum|U|K_A=sum|U|P and the reverse identity for B. Since |U|,|T|>=1, Z_star<=Z_A+Z_B<=D+M. The same physical proof works at unequal biases; no spectral conditional-input independence is inserted. With R=P/M, Q=K_star/Z_star on the complete mixed label space, including off-support atoms,

    E_mix=C_star+M ln(Z_star/M)-M KL(R||Q).

For M>0 let x=M/D<=1. Then tax<=D x ln(1+1/x)<=D ln2. The final inequality follows from the positive derivative ln(1+1/x)-1/(1+x). The logarithm lower bound ln(1+y)>y/(1+y), y>0, follows by integrating 1/(1+t) on [0,y]. The positive part has the same bound. For M=0 no conditional law is formed. Ordinary KL and the original mass M are essential; no degree-tilted replacement is made.

## Independent sharpness calculation

For the actual count threshold F=2*1{at most one zero}-1 split into a,b>=2 inputs, the all-B physical coefficient is zero before A-count a-1, then 2^(1-b) and (1-b)2^(1-b). The only canonical jumps are 2^(-b) and -b2^(-b). The full-A coefficients of the last two count tails are (1-a)2^(1-a) and 2^(1-a). Thus direct alternating sums give

    P(top)/v=(a+b-1)^2/4^(a+b-1),
    K_A(top)/v=((a-1)^2+b^2)/4^(a+b-1),
    K_B(top)/v=(a^2+(b-1)^2)/4^(a+b-1).

At a=b=m their ratio is 2-1/(m^2+(m-1)^2), so every uniform factor below2 fails and factor2 holds throughout this two-jump class by Cauchy. A real two-weight representation uses 1<w<2, total score aw+b and allowed missing score w. One missing input loses at most w, whereas any two missing inputs lose at least2>w, proving the representation for all assignments.

At fair a=b=2 an independent direct spectrum/reference computation gives M=17/64, D=39/64, Z_star=29/64 and overlap13/64<M. Summing both directional energy identities gives exactly D-Z_star=R_A+R_B+overlap-M. The overlap failure alone cannot refute Z_star<=D, which remains unproved and is not claimed by the source.

Every normalized Boolean coefficient has absolute value at most1: it is the average of a signed 2^|S|-term alternating sum divided by2^|S|. Hence corrected entropy summands are nonnegative. The supplied symmetric-threshold bound E_total<=c Delta, c=460+80ln2, therefore gives C_star<=E_mix+Mln2<=(c+ln2)Delta on the sharp family. This is a consequence conditional on that declared established baseline, not a new universal threshold result.

Verdict: the new source clauses hold at their exact scope without repair, relative to their declared canonical-reference and symmetric-baseline dependencies. Neither free atom domination, Boolean admission of selected spectral fragments, a universal jump-count payment nor a new FEI constant is accepted. Exact independent finite validation is saved in out/CHECKS.json and out/REFERENCE_CASES.json. Review scope excludes re-certifying A045's own earlier reference construction as independent work.
