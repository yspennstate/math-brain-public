# Child certification is not an arbitrary-seed admission property

All entropies are in bits. For an actual finite uniform Boolean sign f, let n be its number of relevant coordinates, I its total influence, H its Fourier entropy, B=sum_i B_i its aggregate erasure, and D=H-B its dual total correlation. Fix C>=0 and put delta=H-CI. For each relevant coordinate define the AVERAGE child slack

    sigma_i = [C I(f_i+) - H(f_i+) + C I(f_i-) - H(f_i-)]/2.

This slack can be negative. One must not replace it by a reserve before checking its sign. Both individual children certified at C imply sigma_i>=0; the converse need not hold.

The exact physical influence identity and entropy restriction identity yield

    Delta_i H = C Inf_i + delta + sigma_i,
    B_i = C Inf_i + delta + sigma_i - JS_i,
    D + (n-1)delta + sum_i sigma_i = sum_i JS_i.                (1)

The final equality follows by summing the second line and using B=H-D=CI+delta-D. There are no independence or extremality hypotheses in (1). It is an exact conservation identity with SIGNED child slacks, including constants and dummy deletion.

Write a=2/ln2 and mu_i=sum_{T not containing i} min(p(T),p(T+i)). The already proved scalar restriction bound gives JS_i<=a mu_i and mu_i<=min(Inf_i,1-Inf_i). If delta>0 and all sigma_i>=0, then n>=2 and

    D + sum sigma_i + (n-1)delta <= a sum mu_i <= a I,
    0 < H/I-C <= a/(n-1).                                   (2)

Thus a sequence F_m with relevant dimension n_m->infinity, ratio H(F_m)/I(F_m)->R>C, and all average one-coordinate children certified at the SAME C cannot exist. Eventually (2) fails. Quantitatively n_m<=1+a/(R_m-C). If child allowance varies with m, it must satisfy

    C_m >= R_m - a/(n_m-1),

so liminf C_m>=R for a ratio-convergent sequence. Adding dummy variables does not count toward n_m. This is a precise obstruction to admission into the child-certified minimal-violator endpoint, and applies to every Boolean transformation with these output properties, not merely to ordinary activation. It does not prevent a different endpoint or a restriction extraction whose final ratio approaches C.

For any arbitrary seed f with delta_0=H(f)-CI(f)>0, tensor independence gives, on m disjoint copies,

    delta(f^tensor m)=m delta_0,
    sigma_(copy,i)(f^tensor m)=sigma_i(f)-(m-1)delta_0.         (3)

Every one-copy entropy decrement and JS payment remains unchanged, whereas the positive root deficit grows with m. Once (m-1)delta_0>max_i sigma_i, EVERY relevant averaged child is a violator, even if every seed child was certified. In particular preserving H/I by tensor amplification does not preserve child certification.

For a seed with ratio R and an arbitrary bounded-ratio tensor auxiliary h_m, ratio preservation also cannot restore certification if total relevant dimension tends to infinity and the limiting ratio remains R>C: this is already excluded by (2). No statement is made about auxiliaries whose influence overwhelms the seed and forces the ratio down to C.

Concrete seed f: +1 everywhere except -1 at one point of the three-cube. It has H=4-(9/8)log2(3), I=3/4, d_i=1/4, and one child is a two-bit point defect (H=2,I=1), while its other child is constant. At C=8/3,

    delta_0=2-(9/8)log2(3)>0,
    sigma_i=1/3,
    sigma_i(f^tensor2)=1/3-delta_0>0,
    sigma_i(f^tensor3)=1/3-2delta_0<0.

Thus the nine-variable ratio-preserving tensor fails AVERAGE certification at every coordinate. The six-variable tensor still has nonnegative average slack but already fails INDIVIDUAL certification: the constant branch of the restricted copy leaves an untouched violating seed copy. This is an exact distinction between the two endpoint hypotheses. A rational log interval separately certifies (R-C)>a/10. Therefore NO Boolean sign on n>=11 relevant variables with ratio at least this seed ratio can have all average children certified at C=8/3, regardless of its construction. This is a finite exact threshold derived from the all-dimensional inequality, not a finite-to-infinite conjecture.

The B01 lead's B01-MINIMAL-VIOLATOR-STRUCTURE@1 assumes the stronger hypothesis that every individual child satisfies H<=CI. Its statements follow from (1), sigma_i>=0, D>=0 and the scalar JS bound. In particular Delta_i>=C d_i+delta>R d_i since n>=2 implies d_i<I, hence B_i>(R-a)d_i. The bound B_i<=h2(d_i)<=d_i log2(e/d_i) then gives d_i<e^3 2^-R. Summing gives the lead's D/I<=a-(n-1)(R-C) and B/H>1-a/R. A least-relevant-dimension violator exists by well ordering whenever any C-violator exists; all its physical children have fewer relevant variables and are certified. This reconstructs the original claim without its blocked REPORT being used as a premise.

The endpoint remains logically sufficient at the SAME C: ruling out every actual C-violator whose children are certified rules out every C-violator by minimality. But an arbitrary seed of ratio R>C cannot be embedded in a diverging-dimension ratio-preserving family of such witnesses. These are different quantifiers. Full FEI is not an assumption in this argument.

First unsupported line: obtain a signed Boolean inequality excluding a C-violator with D+(n-1)delta+sum sigma_i=sum JS_i, sigma_i>=0, for some absolute C. Neither (1) nor the admission obstruction pays the surviving JS/erasure debt. A reduction that finds a minimal violating descendant may lose the original gap R-C; it preserves positivity, not a promised seed ratio. The exact proof required of a purported easier endpoint is either such an exclusion or an explicit transfer accounting for this gap loss and the entire terminal entropy.
