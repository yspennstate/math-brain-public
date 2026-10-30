# A100 independent review of the full-support reset obstruction

Verdict: **HOLDS at the complete original A085-ABSOLUTE-TV-RESET-OBSTRUCTION@1 scope**, with an analytic proof and independent exact finite certificates. This accepts a reference-cost obstruction. Full FEI remains open, and the assembled A099 proof chain does not receive blanket acceptance.

The source is A085's 20261021T174013Z run, PROOF.md sections 1–5 and its exact original CLAIMS.json statement. The reconstruction below uses direct character sums, coordinatewise physical edge counts and exact probability transfers. No A085 helper is imported or executed.

For n≥2 put t=2^(-n), and take the sign on n+1 bits negative just at integer vertices 0,1,3. Coordinate j is the least significant bit. Its j and y1 directional influences each equal t; each of the other n−1 influences equals 3t. Thus I=(3n−1)t and Inf_j=t. The queried children have respectively one and two negative vertices, and both are nonconstant. For every nonzero Fourier mask s, direct summation gives coefficient −t[1+(−1)^sj+(−1)^(sj+sy1)]. Its bracket is odd, so no nonempty coefficient vanishes. The empty coefficient is 1−3t>0. The matching root Q=P therefore has full support.

After deleting the spectral membership coordinate j, its complete marginal q is the mean of the two actual child spectra. In the one-point child P_g, the empty mass is p0=(1−2t)^2 and every other mass is 4t². At mask a={y1}, the other child's mass is zero, so qa=2t². The empty marginal is q0=((1−2t)^2+(1−4t)^2)/2=1−6t+10t². In particular q0≥p0/2>0. Matching root conditional laws give refund R=0 exactly; all reference-only child atoms stay in q.

Let M=2^(2n−2). Move d=qa(1−2^(−M)) from atom a to the empty atom in the g-child reference alone. The resulting reference is normalized and strictly positive. Its total variation distance is exactly d<2t². Since 4t²M=1, the actual complete expected reset bill, including the unchanged other child with weight 1/2, is

    Z = [1 − p0 log2(1+d/q0)]/2.

For n=2 the logarithm's argument is 31/16<2 and p0=1/4, yielding Z>3/8. For n≥3, ln(1+x)≤x, ln 2>1/2, p0/q0≤2, and d<qa imply p0 log2(1+d/q0)<4qa≤1/8. Hence Z>7/16. These estimates also give Z→1/2 while TV→0, and Z/Inf_j>(3/8)2^n→∞. All denominators and support conditions used above have been checked before cancellation. No interchange of infinite sums is needed.

The nonempty root mass is 6t−9t² and each such atom is at least t². Its entropy is therefore at most 12nt. For the empty atom z=(1−3t)^2, −z ln z≤1−z and ln 2>1/2 give entropy ≤12t. Thus H≤12(n+1)t≤8(3n−1)t for n≥2. The root begins with a matching influence-priced reference; this is not an expensive unpaid source. At any fixed quota K I the whole new cost eventually exceeds the quota, because I→0 and Z>3/8. This family has bounded H/I and does not disprove FEI.

Minimality also holds at the exact stated additional conditions. In dimension two, both nonconstant children must be signed one-bit dictators. Their parent is the remaining variable times a one-bit sign, hence a monomial, with a one-atom spectrum. It cannot have full root support. The finite verifier checks all sixteen labeled two-bit signs and both queried coordinates. Dimension one has only constant children.

For the synthesis, let A be the original quota, d the spent debit, T the entire current terminal bill, and U=A−d−T. A further conservative finite history gives T=b+r+T'. Replacing its terminal references adds the signed true-law log-likelihood bill Z. Substitution gives the exact remaining balance U+r−Z. Thus the specified erasure/terminal account admits the reset iff Z≤U+r. Any extra channel or label charge L changes this to Z+L≤U+r. With leafwise relative bounds Qnew≥(1−η_leaf)Qold on every occupied atom, 0≤η_leaf<1, a sufficient certificate is

    sum_leaf w_leaf [−log2(1−η_leaf)] + L ≤ U+r.

This uses physical reach weights, complete normalized references and the same original balance. Reference mass at zero-true atoms may alter the normalizer and is never deleted. Absolute TV alone supplies none of these relative bounds; the reviewed family makes this failure quantitative. A useful prescribed reset satisfying this admission, or an influence-priced initial reference for arbitrary Boolean sources, remains the first unsupported universal step.

The source proof uses every structural assumption where needed: Booleanity fixes actual physical children, matching Q sets the refund to zero, two nonconstant children exclude a trivial constant-only witness, and full support excludes an undefined logarithm. Dropping these assumptions does not strengthen an accepted downstream theorem. No claim is made that a useful reset must choose this adverse reference.

Validation: out/INDEPENDENT_RESET_REVIEW.json records the fixed finite domain, rational logarithm intervals and assertion count. Its pilot is a subset and is not added to the full count. The atanh tail is bounded by 2z^81/[81(1−z²)] after reduction to 1≤x≤2; signed powers of two are added after division by the positive ln 2 interval. The all-n result follows from the proof above, not from the finite samples. The separate Lean receipt covers at most the integer endpoint 31<32; it does not certify the Fourier, entropy, or all-n argument. Independent-review status and any formal-check status remain distinct.
