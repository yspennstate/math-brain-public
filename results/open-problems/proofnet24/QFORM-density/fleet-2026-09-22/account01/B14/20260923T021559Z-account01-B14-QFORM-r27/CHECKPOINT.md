# Early checkpoint — countable exact localization core

Run: `20260923T021559Z-account01-B14-QFORM-r27`.

Target remains the full QFORM conjecture. The new candidate lemma is an exact reduction of the *full universal density constant* to a countable class of compact finite-fragment product inputs and rational matrix/interval data.

Let `D_n` be all cap-one product laws. Let `R_n` be product laws with marginal densities `1_E`, where each `E` is a finite union of closed intervals with rational endpoints and total length one. Let `A_n^Q` be symmetric rational matrices with third singular value strictly larger than one. Define

`C_count = sup_{n>=3} sup_{A in A_n^Q} sup_{nu in R_n} sup_{r<s rational} nu{r<=x^T A x<=s}/(s-r)`.

Claim under proof:

`C_full = C_count`,

where `C_full` is the full target supremum over all real symmetric `A` with `s_3(A)>=1`, all cap-one product laws, and all real target intervals.

Mechanism:
1. apply account02/B14 r23 simultaneous convex-envelope localization with the parameter family equal to all target matrices, obtaining exact reduction to compact finite-fragment indicator products with zero constant loss;
2. only after this compact-law reduction, approximate a fixed real target matrix `A` by rational symmetric `A_m` with `s_3(A_m)>1`; uniform convergence of `x^T A_m x` on that fixed compact support and interval enlargement preserve the small-ball coefficient;
3. approximate each finite-fragment set in symmetric difference by a rational-endpoint finite union of exactly total measure one; total variation plus lower semicontinuity of the interval small-ball functional preserves the supremum;
4. restrict output intervals to rational endpoints by outer approximation.

The ordering is essential: matrix discretization before law localization is not justified uniformly over unbounded fragmented inputs because remote fragments can amplify tiny coefficient changes. The compact extreme-product step removes that obstruction law-by-law without imposing a universal support radius or fragment count.
