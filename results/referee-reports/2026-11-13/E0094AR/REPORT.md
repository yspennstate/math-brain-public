MINOR

The mathematical PARTIAL claim survives this audit under the submission's stated conventions. Theorem 2 really proves O(n log^3 n) for every odd n >= 5, including composite n. Its word construction, comparison constant 720 ceil(log_2 n)^2, and full-spectrum mixing argument are valid. The universal lower bound, weighted antipodal-chord theorem, single-edge obstruction, and ten-vertex counterexample also withstand checking. I found no false principal theorem or discrepant small-state mixing table. The optimal added generator and its exact asymptotic mixing order remain undetermined.

The main correction is to the literature discussion: a closely related O(n log^3 n) three-generator shuffle is already Theorem 7 of Diaconis–Saloff-Coste (1993), in the very paper cited by the submission. That theorem does not literally use the prescribed transposition and n-cycle. Consequently it does not by itself invalidate the fixed-pair adaptation here, but its omission materially overstates the distance between this report and the prior literature. The verdict concerns the correctness of this partial report; it is not a claim that its remaining novelty meets a particular journal's significance threshold.

Required corrections, with locations in the unchanged CLAIM.md:

1. **Omitted principal predecessor, lines 22–36 and 89–194.** The literature table describes Diaconis–Saloff-Coste only as the comparison source and an analysis of the slow base walk. Section 4, Theorem 7, pp. 2151–2152, already proves O(n log^3 n) mixing for two affine perfect shuffles and a transposition. Add that theorem explicitly, describe the different generators, and identify the contribution here as the construction for the prescribed pair. The proof strategy and the general few-generator mixing order are not new. Theorem 1's order-n-log-n counting obstruction is also recorded in the remark following that earlier theorem. [Original paper](https://pi.math.cornell.edu/~lsc/papers/comp-fg.pdf).

2. **Missing faster unrestricted constructions, literature table, lines 20–36.** Include Kassabov's explicit bounded-size expanding generating sets for symmetric groups. They give O(log(n!)) = O(n log n) half-lazy mixing for those sets. They do not say that one can retain this prescribed pair and add only one permutation. State this distinction; do not either present all explicit O(n log n) constructions as unknown or cite them as a solution of E0094. [Kassabov, Symmetric Groups and Expander Graphs](https://arxiv.org/abs/math/0505624).

3. **Unqualified parity in the summary, lines 5–10, 194 and 438.** The proved upper bound is for odd n, whereas the introductory infimum display has no parity restriction. Add “as n tends to infinity through odd integers” to the summary and corresponding optimal-exponent statements, or supply an even-n proof with its own constants. Doubling modulo an even n is not a permutation. Lines 353–354 correctly say that the even numerical rows are exploratory. This is a scope correction, not a failure to answer Diaconis's example: the original Question 3 explicitly specifies odd n. [Diaconis's original question](https://arxiv.org/abs/1309.7754).

4. **Reproduction paths in the delivered bundle, lines 36, 339, 369 and 414–432.** From the directory containing CLAIM.md, the displayed commands reference nonexistent code/ paths; the actual files are under claim_files/code/. Begin those instructions with `cd claim_files`, and qualify the other relative references accordingly. The bundle contains extracted source texts and the cycle TeX manuscript, but no source PDFs at the top level of claim_files/sources; correct the assertion that PDFs are included, or include them. This does not affect the proofs or the independently reproduced results.

These are the errors and presentation gaps I found. In particular, I do not list an absent log(n!) factor as an error: the submission explicitly proves the stronger spectral information needed to avoid that loss.

Theorem 2: detailed proof audit.

At lines 89–105, sigma(x) = 2x modulo n is invertible for every odd n. No primality or assumption about the multiplicative order of 2 is needed. For odd n >= 5 the five nonidentity moves are distinct: sigma fixes 0, c and c^{-1} do not; sigma moves 1 to 2, unlike tau; and sigma = sigma^{-1} would imply n divides 3. The probabilities are therefore exactly 1/2 for holding and 1/10 for each displayed move.

At lines 107–112, sigma c sigma^{-1} = c^2 has the asserted orientation. If i has k binary digits, starting with c and processing the remaining digits costs at most 1 + 3(k-1) = 3k-2 letters. Since 0 < i < n, k <= h; i = 0 has the empty word. Thus the stated power-word bound holds uniformly, including just above powers of two.

At lines 114–137, the binary partial sums lie in [0,d] with d < n and increase strictly. They therefore give distinct vertices even after reducing modulo n. Conjugation gives exactly

    A_l tau A_l^{-1} = (a_l, a_l + 2^{j_l}).

The palindrome of consecutive path-edge transpositions exchanges only 0 and d. The displayed expression B tau B^{-1} is correct for rightmost-first composition. Expanding B gives the particularly useful explicit word

    B = sigma^{j_1} tau c sigma^{j_2-j_1} tau c ... tau c sigma^{j_r-j_{r-1}},

with the evident interpretation B = sigma^{j_1} when r = 1. Indeed A_l^{-1} A_{l+1} = c sigma^{j_{l+1}-j_l}. Its length is j_r + 2(r-1), not a sum of separately constructed long powers of c. This telescoping is essential. Hence |B| <= 3h-3, and |B tau B^{-1}| <= 6h-5. Conjugating by the binary word for c^i gives length at most 12h-9. Every unordered pair is obtained by taking d = j-i with 0 <= i < j < n; the version with residues also works. This proves the result for every admissible odd n, not merely the tested sizes. The subsequent diameter upper bound follows from the usual cycle decomposition into at most n-1 transpositions.

At lines 139–157, both Dirichlet-form normalizations are correct. With D_s as defined there,

    E_P = (1/20) sum_{s in T} D_s,
    E_Q = (1/(4M)) sum_{u transposition} D_u,   M = n(n-1)/2.

For any word of length l <= L = 12h, translation of the uniform summation variable at each step and Cauchy–Schwarz give

    D_u <= l sum_s N_s(u) D_s <= L^2 sum_s D_s.

This already allows maximal congestion: N_s(u) <= L for each of the M words. Summing and dividing by M gives E_Q <= 5L^2 E_P. Equivalently, the standard comparison constant is bounded by

    max_s (5/M) sum_u |u| N_s(u) <= 5L^2 = 720h^2.

There is no omitted factor M, |S_n|, or additional congestion factor. The factor five and the holding factors have been included correctly. Comparison is in the correct direction: I-P >= (I-Q)/A as quadratic forms. Min–max compares all ordered eigenvalues; simultaneous diagonalization of these two operators is not needed.

At lines 159–191, the passage to mixing is valid and stronger than a spectral-gap bound. The transposition character ratio, regular-representation multiplicity d_lambda^2, and half-lazy eigenvalue mu_lambda = (1-r_lambda)/2 have the right normalizations. With j = n-lambda_1,

    mu_lambda >= j/[2(n-1)],
    sum_{lambda: n-lambda_1=j} d_lambda^2
        <= binom(n,j)^2 j! <= n^{2j}.

The tableau injection used for the dimension inequality is valid: choose the labels below the first row and their standard tableau; the first row is then forced. Some choices violate column restrictions, which only makes this an upper bound.

Both kernels have nonnegative spectrum. Reversibility and translation invariance give

    chi^2(P^t(e,.), U) = n! P^{2t}(e,e)-1 = trace(P^{2t})-1.

Thus, putting A = 720h^2,

    chi^2 <= sum_{j=1}^{n-1} [n^2 exp{-t/[A(n-1)]}]^j.

At the stated ceiling time, the bracket is at most q = 4 eps^2/(1+4 eps^2). The finite geometric sum is bounded by q/(1-q) = 4 eps^2, so TV <= sqrt(chi^2)/2 <= eps. Every inequality has the required direction.

This also answers the question about log|S_n|. Keeping only gap(P) >= 1/[A(n-1)] and applying the generic bound involving the minimum stationary probability 1/n! would give only O(n^2 log^3 n) at fixed error. That would be inadequate. The submitted proof retains the whole eigenvalue list and controls its multiplicities; n! is accounted for by the heat trace, rather than replaced by a single worst eigenvalue. Its final bound really is

    O(n log^2 n [log n + log(1/eps)]),

and therefore O(n log^3 n) at fixed error. This conclusion is for the symmetric half-lazy kernel defined in the report; the same numerical constants have not been established for a directed kernel or arbitrary nonlazy move weights.

Theorem 1 and the walk conventions.

The degree-five, inverse-reduced word count at lines 58–85 is valid even with coincident generators: coincidences can only reduce the ball. The inverse of tau is tau, so after the first letter there are at most four choices. At time t the support lies in B(t), including when holding is allowed. Testing this event in total variation proves the displayed finite-time bound, and the ball needed to cover n! states gives exactly the stated ceiling for diameter. A diameter lower bound has not been misused as a mixing upper bound.

The stronger coefficient for the half-lazy walk is also justified. With R = log_4(n!), t = floor((2-delta)R), and r = floor((1-delta/4)R), the mean number of active steps is at most (1-delta/2)R. Its variance is O(R), and the gap between r and that mean is order R. Chebyshev therefore gives probability 1-o(1) of lying in B(r), uniformly in sigma, whereas U(B(r)) is exponentially small in R. The TV distance tends to one. This proves the lower bound for each fixed eps < 1, with coefficient 2/log 4 in natural-log units after Stirling. That coefficient uses holding probability 1/2; it is not asserted for every supported walk. The weaker support bound, and hence order n log n, needs no such holding convention.

Independent computations.

I wrote independent_audit.py without importing, executing, or copying the submitted code. It constructs lexicographic permutation states, computes right-composition successors using independently implemented Lehmer ranks, and propagates the full probability vector. This is deterministic full-state arithmetic, rather than sampling. Numerical thresholds are distinguished below from rational certificates. Submitted data were read only to compare the independently generated outputs.

| n | base t(1/4) | doubling t(1/4) | base t(.01) | doubling t(.01) | best t(1/4), exhaustive over every sigma |
|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 2 | 10 | 6 | 2 |
| 4 | 11 | 6 | 42 | 22 | 5 |
| 5 | 29 | 13 | 92 | 44 | 9 |
| 6 | 58 | 17 | 170 | 46 | 14 |
| 7 | 103 | 42 | 281 | 113 | 20 |
| 8 | 168 | 49 | 433 | 126 | not searched exhaustively |
| 9 | 254 | 74 | 633 | 171 | not searched exhaustively |

For even n I used exactly the report's exploratory generator: doubling on 0,...,n-2 modulo n-1 and fixing n-1. For n=3,4 the move set has fewer than five distinct moves; duplicates and identity are removed before assigning uniform active-step probabilities. Every sigma, including identity and coincidences with base moves, was considered in each exhaustive search. There were 6+24+120+720+5040 = 5,910 candidates in total. The numbers of quarter-TV optimizers for n=4,5,6,7 were respectively 6,14,8,138. Thus doubling is explicitly not the best finite generator at these sizes. The submission does not claim otherwise.

Examples of optimal generators, written as image tuples (sigma(0),...,sigma(n-1)), are:

| n | an optimal image tuple | TV at time t_best-1 | TV at t_best |
|---:|---|---:|---:|
| 4 | (1,2,0,3) | .296000000 | .218380000 |
| 5 | (1,2,4,0,3) | .296773247 | .246796672 |
| 6 | (1,3,0,5,2,4) | .282849514 | .245430826 |
| 7 | (0,2,6,5,1,4,3) | .274196097 | .245688855 |

For these witnesses I separately propagated arbitrary-precision integer path counts, with weights m for holding and one for each of the m distinct moves, denominator (2m)^t. Their boundary TV values are exact rationals in independent_results/cross_checks.json. Exhaustiveness over all other candidates is numerical, not an exact rational certificate for every candidate. No global optimizer is asserted for n=8 or 9, nor for the .01 objective.

The five submitted rows n=5,...,9 agree at both thresholds. All ten full TV curves agree to maximum absolute discrepancy below 6.16e-12; my largest probability-mass error was below 1.61e-14. As another check, full matrices at n=5 give gaps .0484541067605 for the base and .0975943946092 for doubling. Theorem 2's actual quarter-TV upper bounds at n=5,7,9 are 125150,213889,553319; the observed times 13,42,74 are far below them. These very loose bounds and small sizes cannot establish the true asymptotic logarithmic power.

I independently evaluated 91,977 constructed transposition words at n=5,7,9,11,15,17,31,33,63,65,101,127,129,255,257. Evaluation checked the entire resulting permutation, not just its two intended endpoints. There were no failures. Maximum freely reduced word lengths include 9,15,19 at n=5,7,9, and 63,63,75,75 at n=127,129,255,257. The lengths agree with the submitted certificates wherever these sizes overlap. The all-odd-n conclusion comes from the proof above, not induction from these computations.

Proposition 7, the chord theorem, and Theorem 5.

For Proposition 7 I rebuilt the graph directly from its 15 listed edges. It is connected and cubic. Exact rational characteristic-polynomial calculations reproduce

    x(x-5)(x-2)(x^3-9x^2+24x-17)
      (x^4-14x^3+69x^2-141x+101).

Exact real-root isolation shows that the second root is simple and lies in (1.120,1.121). Polynomial reduction modulo z^3-3z-1 verifies every coordinate of Af=zf and also sum f=0. Isolating its root in (1.879,1.880) proves the displayed ordering of entries. The unique maximum is 0 and the two minima are 2 and 8, as claimed.

For every one of the 30 missing edges I independently formed D'^{-1}L' over the rationals, computed its characteristic polynomial, and isolated its smallest positive root. The exact polynomials for 02,08 and 24 reproduce the displayed F and H coefficient for coefficient. Independently computed Sturm variation counts are (9,9,8) at the submission's three rational test points in each row. In particular,

    gap(02) = gap(08) is in (.47694,.47695),
    gap(24) = gap(78) is in (.48117,.48118).

Disjoint rational isolating intervals separate every inferior candidate; polynomial gcds certify the tied top root. The global optimizers are precisely 24 and 78. The counterexample is valid for the ordinary-walk objective. It does not refute a theorem of Ghosh–Boyd: their rule was expressly a perturbation heuristic for the combinatorial Laplacian. [Ghosh–Boyd, Section III](https://web.stanford.edu/~boyd/papers/pdf/growing_fast_graphs.pdf).

Theorem 3's proof at lines 200–235 is correct for every even n >= 4 and every positive chord weight. The path Dirichlet constant is 2a. The half-turn decomposition is orthogonal for both the degree inner product and the energy. In the even subspace, subtracting the common endpoint value removes all extra endpoint degree contributions. In the odd subspace, cycle energy plus 4ws^2 dominates a times the new degree norm. The sine eigenfunction supplies equality for an antipodal chord. For the other chords, the equal-endpoint cosine test has energy na and weighted variance n[1+2w cos^2(pi k/n)/(n+w)], yielding exactly the stated strict upper bound.

I also checked all 950 cases consisting of even n=4,...,40, every chord distance, and weights .01,.5,1,5,1000 through symmetric normalization D^{-1/2}AD^{-1/2}. All agree. The analytic argument, rather than these numerical checks, establishes the all-n/all-weight theorem. A public read of the cited the author manuscript confirms that it contains the same theorem and proof; the attribution to that prior preprint is correct. [the author manuscript](https://github.com/yspennstate/one-chord-even-cycle-spectral-gap/blob/main/paper/main.tex).

This is the ordinary gap 1-lambda_2, as the report explicitly states, rather than the absolute gap or a TV optimizer. For example, when n=2 mod 4, an antipodal chord preserves bipartiteness, and the nonlazy walk does not mix in TV. Half-laziness removes this obstruction and halves the ordinary gap. The submission's convention prevents a contradiction, but this distinction must be preserved in any shortened account of the result.

Theorem 5 is correct: the repeated Fiedler eigenspace contains a nonzero vector with equal endpoint values, the added edge contributes zero energy, and the weighted variance increases by

    [2wnd/(nd+2w)] b^2.

The resulting quotient cannot exceed alpha/d and is strictly smaller if b is nonzero. Proposition 6's differentiated generalized eigenvalue formula likewise has the correct degree-perturbation term and normalization. These arguments concern ordinary-walk gaps after degree changes.

Theorem 4's invocation of Hermon–Sly–Sousi is also appropriate. Their Theorem 1.1 and Proposition 1.2 provide logarithmic mixing with cutoff and a constant absolute gap for bounded-degree base graphs whose components have at least three vertices. The submission's factorial-moment/Bonferroni calculation gives probability tending to exp(-d/2) of no overlap with a fixed d-regular base. Conditioning on that event preserves high-probability conclusions. This legitimately restricts the result to missing-edge matchings. [Hermon–Sly–Sousi](https://arxiv.org/abs/2008.08564).

Literature result and remaining novelty.

The closest predecessor is the omitted Diaconis–Saloff-Coste Theorem 7: for even deck size k, use Z/(k-1) plus a point infinity, affine maps x -> 2x and x -> 2x+1 fixing infinity, and (0,infinity). They prove mixing at order k log^3 k by short transposition words and spectral comparison. Their generators are not the submission's fixed tau and full n-cycle. The potential new ingredient here is the telescoping path construction retaining that exact pair for odd n, not the general mixing order or method. I did not find this exact formulation already proved in the sources searched. [1993 paper, pp. 2151–2152](https://pi.math.cornell.edu/~lsc/papers/comp-fg.pdf).

Babai–Kantor–Lubotzky already supply the binary affine short-word idea and O(n log n) diameter constructions with other generators. Wilson supplies the slow base-walk lower bound, rather than an optimal added generator. Hildebrand surveys randomly chosen driving sets; that is different from choosing one augmentation of the prescribed pair. Helfgott–Seress–Zuk give polynomial mixing estimates for random generating pairs, which are neither sharper here nor a theorem about this fixed pair. [BKL](https://pages.uoregon.edu/kantor/PAPERS/BKL.pdf), [Wilson](https://arxiv.org/abs/math/0210469), [Hildebrand](https://arxiv.org/abs/math/0401189), [Helfgott–Seress–Zuk](https://arxiv.org/abs/1311.6742).

Kassabov gives explicit O(n log n) mixing with other bounded-size generating sets, as noted in correction 2. General random-Cayley claims also cannot simply be transferred to this model. In particular, van Handel's 2026 strong-convergence survey still distinguishes expansion for tuple Schreier actions from the open nonvanishing-gap question for random Cayley graphs on the entire symmetric group. An expanding action on a few labels does not establish full-permutation mixing. [Kassabov](https://arxiv.org/abs/math/0505624), [van Handel, Section 4.1.2](https://epubs.siam.org/doi/10.1137/25M1807113).

Chatterjee–Diaconis permit deterministic bijections of the entire chain state space; right multiplication by sigma is a special, highly restricted class of bijections of S_n. Their result is therefore not a proved O(n log n) solution for the allowed augmentation. [Chatterjee–Diaconis](https://arxiv.org/abs/2004.11491).

For E0095 the optimal matching order is already the published Hermon–Sly–Sousi result, and the chord theorem is already in the cited the author preprint. The single-edge obstruction is an elementary variational consequence; the ten-vertex example is a useful exact finite certificate of failure of a heuristic, not a new general optimization theorem. No exact finite optimizer for general regular graphs is supplied. My targeted search through material dated 2026 located no better proved bound for the exact E0094 augmentation, but this is a bounded literature search, not a priority certificate or proof that no such paper exists.

Reproduction and limits of this audit.

Run `python3 independent_audit.py` from this directory. It writes independent_results/, including all curves, exhaustive-search outputs, word counts, exact graph polynomials and root intervals, rational mixing witnesses, and resource metadata. The complete run peaked at 304,840,704 bytes RSS (about 291 MiB), inherited nice level 20, and configured numerical-library threads to one before import. I used no subagents, no worker pool, and no publication or external writes. The submitted CLAIM.md and claim_files/ were left unchanged. Its audited SHA-256 is 19c2233c43c38e20d007a17fae32a50bdf2efbe0f82d6ccf11041741e98fb9bf.

I did not rerun the n=10,11 full-state walks, all 192 regular-graph census entries, or every certificate in that census. Those are outside the independent numerical verification claimed here. The requested main proofs, small-state walks, exhaustive small generator search, transposition words, exact ten-vertex example, chord result, and relevant literature were checked as described above.

Task: “Your job is to break it if it is wrong.” Received 2026-11-13 02:48 +04 (Asia/Tbilisi).
