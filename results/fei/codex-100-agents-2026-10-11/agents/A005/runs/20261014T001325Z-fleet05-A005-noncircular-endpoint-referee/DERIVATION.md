# Full-support point surgery clamps the selectable price

SOURCE CORRECTION AFTER INTAKE: A061's PADDING_EDIT_PROOF.md Sections 1--4, run 20261013T215821Z-fleet05-A061-entropy-process, already proves the arbitrary-core local limits and the minimum clamp (5), as well as continuity of the old coordinates. Equations (1)--(5) below are an independent reconstruction, not a new theorem. The new stage target is the signed-child eligibility obstruction in the appended section.

All functions are finite uniform Boolean signs; entropy is in bits. Fix a nonconstant seed f on n relevant coordinates, with normalized coefficients a_S, H, I>0, coordinate influences d_i>0 and erasures B_i. Let E(f)=min_i B_i/d_i. Pad f with r=N-n dummy coordinates, N>=n+2, then reverse its value at the all-zero physical vertex (in the 0/1 representation). Call the resulting actual Boolean function F_N. Put alpha=2^(1-N), v=alpha^2, and eta=f(0).

For every Fourier index U,

    Fhat_N(U)=a_U-eta alpha     if U is contained in the n seed coordinates,
              -eta alpha       otherwise.                    (1)

Old nonzero Fourier coefficients have magnitude at least 2^-n. Since alpha<=2^(-n-1), none can cancel. Every old zero becomes a nonzero +/-alpha. Hence EVERY Fourier coefficient of F_N is nonzero. All added coordinates have influence alpha. An original coordinate changes influence by +alpha if f(0)=f(e_i), and by -alpha otherwise. In particular all seed coordinates stay relevant for large N, and

    |I(F_N)-I(f)|<=N alpha ->0.

The input disagreement probability is 2^-N. Parseval and Cauchy-Schwarz bound the total variation of squared Fourier spectra by 2sqrt(2^-N). For a normalized spectral law on 2^N points, the usual maximal-coupling bound is |H(P)-H(Q)|<=h2(t)+t log2(2^N-1). This tends to zero here. The seed law is padded deterministically, so H(F_N)->H(f) and H(F_N)/I(F_N)->H(f)/I(f). This is the previously established H/I admission, not a new universal bound.

For EVERY added coordinate j, partition erasure edges by their retained index. Exactly 2^n edges meet a seed-only Fourier index, while all other 2^(N-1)-2^n edges have both masses equal to v. Therefore

    B_j(F_N)=2v[2^(N-1)-2^n]
                 +sum_(S subset [n]) Phi((a_S-eta alpha)^2,v),
    B_j(F_N)/Inf_j(F_N)
          =2-2^(n+1)alpha
                 +(1/alpha)sum_S Phi((a_S-eta alpha)^2,alpha^2),       (2)

where Phi(x,y)=-x log2 x-y log2 y+(x+y)log2(x+y). The formula includes old zero coefficients and both exceptional empty atoms. It is uniform across all added coordinates because padding and the chosen vertex are symmetric under dummy-coordinate permutations.

For x,y>=0, Phi(x,y)<=y log2(e(1+x/y)). Indeed x log2(1+y/x)<=y log2 e, and the other term is y log2(1+x/y). Since |a_S-eta alpha|<=1+alpha, equation (2) gives

    2-2^(n+1)alpha <= B_j/Inf_j
      <=2-2^(n+1)alpha
         +2^n alpha log2(e[1+(1+alpha)^2/alpha^2]).              (3)

For fixed seed n the error is O_f(N 2^-N), and every dummy ratio tends to exactly TWO.

For a seed coordinate i, the exact corresponding formula is

    B_i(F_N)=2v[2^(N-1)-2^(n-1)]
      +sum_(T subset [n]\{i})
        Phi((a_T-eta alpha)^2,(a_(T+i)-eta alpha)^2).           (4)

This formula is independently validated below. Alternatively B_i=H(S)-H(S_-i), and the same spectral continuity bound, including marginal contraction of total variation, shows B_i(F_N)->B_i(f), uniformly over the finitely many seed coordinates. Since their influences converge to d_i>0, their ratios converge to the seed ratios. Combining this with (2)-(3) proves

    min_(i relevant) B_i(F_N)/Inf_i(F_N) -> min(E(f),2).        (5)

Thus full-support hardening preserves the arbitrary seed's H/I ratio while CLAMPING its selectable erasure price to at most two in this family. It preserves the price only when E(f)<=2. This is not a theorem that every full-support Boolean function has E<=2; small full-support point defects themselves have E>2.

For the original localized threshold T(f)=lambda H(f)/I(f)+K, the criterion on these images is asymptotically governed by min(E(f),2)<=T(f), not E(f)<=T(f). In particular whenever 2<T(f)<E(f), all sufficiently large images have an added-coordinate witness, and the seed fails that same-parameter pointwise rule. No claim is made at an exact equality boundary from a limit alone, and no claim is made that the UNIVERSALLY quantified localized endpoint is true or false at those constants.

Actual certificate: seed f is +1 except -1 at one point of the three-cube. It has I=3/4 and E(f)=4+(5/2)log2 5-(9/2)log2 3>5/2. Choose N=12, r=9. Alpha=1/2048; eta=-1. Each original influence is 1/4-alpha=511/2048; each dummy influence is alpha=1/2048; total influence is 3/4+6alpha=771/1024. Equations (2),(4) and rational logarithm intervals certify every original ratio >5/2 and every dummy ratio <5/2. All 4096 Fourier coefficients are nonzero; their three compressed classes are explicitly normalized. This gives a new full-support pointwise witness-transport obstruction at lambda=0,K=5/2. In fact F_12 has max influence<1/4 while the seed sits on that strict threshold boundary, so the image lies in the lead's strict weak-influence class tau=1/4.

The exact first unsupported line toward SAME-parameter universal localization remains: deduce a seed witness from a universally available witness on these admitted images, despite the new dummy witnesses in (2). The existing finite FEI consequence with its JS/threshold constants remains valid; neither this construction nor (5) improves that constant. Any proposed endpoint using full support plus weak influences must prove a data-only selection or a nonlocal payment, rather than assume that full support preserves the selected-coordinate price.

## Signed-child eligibility: the remaining universal endpoint gap

Fix a real C and a fixed nonconstant seed with delta(f)=H(f)-C I(f)>0. Define average child slack sigma_i(F)=E_b[C I(F|i=b)-H(F|i=b)]. Call a coordinate eligible if sigma_i>=0; this is weaker than requiring both children to satisfy FEI at C. For every dummy coordinate of F_N, the two physical children are exactly the padded clean seed and the one-point edited F_(N-1). Therefore

    sigma_j(F_N)=-(delta(f)+delta(F_(N-1)))/2 -> -delta(f)<0. (6)

Every newly relevant cheap direction is thus eventually ineligible, despite B_j/I_j ->2 and full Fourier support. Every old coordinate has child slack converging to its seed child slack: its two children are the corresponding clean seed restriction and a one-point edited restriction, so the same continuity estimate applies. If all seed average child slacks are strictly positive, then eventually the eligible coordinates are exactly the seed coordinates and

    min_(i:sigma_i>=0) B_i(F_N)/I_i(F_N) -> E(f).           (7)

If every individual seed child has strictly positive slack, this statement also holds with individual-child eligibility. Zero-slack seed children require a separate sign check; no uniform boundary claim is made. Constants in clean children are zero-slack, which the exact witness checks directly.

For a finite sufficient exclusion criterion, A061 gives D_j/I_j<=4+kappa(2N+7), kappa=|supp(fhat)| alpha, once r>=4. The exact restriction identity is

    sigma_j=-delta(F_N)+(D_j/I_j-C)alpha.

Thus delta(F_N)>alpha[4-C+kappa(2N+7)] guarantees ineligibility of every dummy. This is a signed child correction, not a universal terminal payment.

The fixed N=12 example at C=8/3 has delta(F_12)>0, all three original average child slacks positive and all nine dummy average child slacks negative. Each original B_i/I_i>5/2, while every dummy B_j/I_j<5/2. Hence there exists an actual full-support Boolean function with max_i I_i<1/4 for which a cheap root witness exists but NO cheap average-child-eligible witness exists at (C,K)=(8/3,5/2). This refutes that specific strengthened endpoint, not FEI at an arbitrary absolute constant, and not an implication restricted to genuine minimal violators (all coordinates child-certified). The root itself has uncertified dummy children and therefore cannot be used as a minimal-violator counterexample.

The first unsupported universal line is now precise: produce a selectable witness with both its erasure price and its negative descendant slack paid, or prove an admission into genuinely child-certified roots while preserving a fixed violating ratio. Root full-support/weak-influence admission alone supplies neither. Our stage-2 dimension obstruction already forbids a fixed-gap ratio-preserving admission into diverging relevant dimension with all average children certified; the present construction identifies the exact coordinates that fail certification.

## Corrected witness admission, without a seed-child positivity assumption

Define Q_C(f)=min_(i relevant) [B_i(f)+max(-sigma_i(f),0)]/I_i(f). For any fixed seed with delta(f)>0, each dummy direction has

    [B_j(F_N)+max(-sigma_j(F_N),0)]/alpha
                ~ delta(f)/alpha -> infinity.

Here B_j=O(alpha), sigma_j->-delta(f), and alpha=2^(1-N). Every original numerator and its positive denominator converge to the seed quantity, by continuity of B and of the two physical child deficits. There are only finitely many original coordinates, and all dummy coordinates have the same price. Thus, with no positivity hypothesis on seed child slacks,

    Q_C(F_N) -> Q_C(f).                                  (8)

This is an arbitrary violating-seed admission preserving the explicitly debt-corrected witness price. It is stronger than the data-only eligible minimum statement as a transport theorem, but supplies no universal bound on Q_C. The root identity delta+sigma_i=B_i+JS_i-C I_i explains the correction's necessity. A proof that pays this corrected price from independent structural resources would be useful; assuming a bound strong enough to force delta<=0 is not such a proof.
