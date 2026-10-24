VERDICT: PASS (correct and complete)

Independent audit of F0086, 2026-10-11

Claim and scope

The claimant claims a literature resolution, not a proof of Conjecture 40 as originally conjectured. ATTEMPT.md lines 18-31 and CLAIMS.jsonl lines 1-2 claim that the universal real-PSD positivity parameters are exactly

D_R = {0} union {-1/m : m >= 1} union {2/m : m >= 1},

and consequently every positive alpha outside {2/m : m >= 1} admits an admissible real kernel with no alpha-determinantal process. This includes alpha=3/2, so the asserted universal existence throughout [0,2] is false. Every alpha>2 is excluded, so the second assertion is true. This answers both quantifiers of the stated problem. SOLVED_IN_LITERATURE means the conjecture has been resolved by disproof of its first assertion, not that both original assertions are true.

Primary-source verification

I independently downloaded https://arxiv.org/pdf/1104.3531v2 and https://arxiv.org/pdf/math/0503110 using Python requests, extracted their text with pypdf, and read the relevant statements and proof. Copies are saved here as branden.pdf/branden.txt and source.pdf/source.txt. I did not rely on the claimant's downloaded sources.

Branden, Solutions to two problems on permanents, Theorem 2.3 on PDF page 4, states exactly the real classification above, with m+1 and nonnegative integer m in place of positive integer m. Problem 2.1 explicitly quantifies over all real symmetric positive semidefinite matrices, with no fixed dimension or entrywise-nonnegativity restriction. This is not merely a complex-matrix result or a fixed-size result. Its definition det_alpha(A)=alpha^n per_(1/alpha)(A) agrees with the problem's convention term by term: alpha^n alpha^(-c(sigma))=alpha^(n-c(sigma)). This conversion is valid for the positive alpha used to exclude parameters; zero is handled separately.

Crossref's DOI endpoint https://api.crossref.org/works/10.1016/j.laa.2011.06.022 independently confirms Petter Branden, the exact title, Linear Algebra and its Applications 436(1), 53-58, January 2012. The response is saved as crossref.txt.

The original source's PDF page 22 contains the stated Conjecture 40 and the same determinant convention. Immediately before it, the source explicitly records existence at alpha=2/m for real kernels. Its introductory setup assumes locally compact Polish spaces, Radon reference measures, and locally trace-class operators. Thus ATTEMPT.md lines 7-16 and 68-71 accurately represent the source and known positive cases.

Independent check of the kernel implication

ATTEMPT.md lines 34-35: Failure of universal positivity means there exists a finite real symmetric PSD A with strictly negative det_alpha(A). Theorem 2.3 supplies this for every positive excluded alpha; in particular 3/2 is excluded since 2/(3/2)=4/3 is not an integer. Every alpha>2 is excluded because 2/m <= 2.

Lines 36-43: For the unit cells I_i and the isometry J sending e_i to 1_(I_i), the block integral operator is J A J*. Consequently it is self-adjoint, nonnegative, bounded, and finite rank, with trace equal to tr(A). Equivalently its quadratic form is v* A v for v_i=integral_(I_i) f. Complex-valued test functions cause no problem: a real symmetric PSD matrix is also Hermitian PSD. Its compression to every compact subset is positive trace class. The space [0,n) is a G-delta subspace of R and hence Polish; it is locally compact in its relative topology, and restricted Lebesgue measure is Radon. The discontinuity of the block kernel at cell boundaries is not forbidden by Conjecture 40 or the ambient general setup. The source's continuous-kernel example is not an additional universal hypothesis.

Lines 44-50: The pairwise disjoint cells ensure all coordinates in I_1 x ... x I_n are distinct. This rectangle has measure one, and its kernel matrix is exactly A. The alleged intensity therefore integrates to det_alpha(A)<0 there. The source's own Definition 1 requires this integral to equal E[product_i X(I_i)], which is nonnegative. This direct contradiction verifies nonexistence without relying on pointwise values on null sets, atomic diagonal conventions, or simplicity. The block kernel also has the natural finite spectral representative, so the source's representative convention in Remark 5 introduces no loophole.

Published-proof checks and computations

ATTEMPT.md lines 53-64 correctly summarize Branden's proof on PDF pages 5-6. If beta=1/alpha is not a nonnegative half-integer, choose dimension d with beta<(d-1)/2. Rank-one PSD matrices spanning Sym_d exist: the outer products of e_i and e_i+e_j suffice. Their positive combination at the basepoint is positive definite. Failure of complete monotonicity, via the cited Scott-Sokal theorem, gives a negative signed mixed derivative and hence a negative Taylor coefficient of P(y-x)^(-beta). Whitening gives det(A)^(-beta) times det(I-X U^T U)^(-beta); the prefactor is positive. The generalized MacMahon identity identifies the sign with per_beta((U^T U)[r])/r!. Replication is R (U^T U) R^T and preserves PSD, and multiplication by positive alpha^|r| preserves the negative sign. These are the same steps as the claimant reports.

I checked exact algebra with SymPy and full permutation enumeration: parameter conversion on replicated PSD matrices of sizes 1 through 5; MacMahon coefficients for a 2x2 PSD matrix with replication multiplicities (1,1), (2,1), (1,2), (2,2); the replication identity; and the original 3x3 example, whose spectrum is {0,3,3} and determinant is 2(4-alpha)(alpha+1). The results are retained in exact_checks.txt. These computations check identities, not the universal classification by finite sampling.

I also ran fresh arXiv API queries using HTTP, saved in arxiv_search.txt and dependency_search.xml. The targeted dependency query identified Scott-Sokal, arXiv:1301.2449v3, whose abstract confirms the inverse-determinant/complete-monotonicity subject. I did not independently reprove the Scott-Sokal classification; the literature verdict rests on the verified published Branden theorem. No built-in web search was used.

Issues and limits

No substantive error or required fix was found in ATTEMPT.md. Lines 73-78 correctly disclose that no explicit numerical matrix at alpha=3/2 and no new proof of the classification are supplied. Neither is needed for this literature-based existential conclusion. Matrix positivity alone would not generally prove existence of a point process; the claimant uses it only as a necessary condition to prove nonexistence, and separately cites the already-known Gaussian-square cases for the allowed positive parameters. The alpha=0 Poisson statement requires the ambient local finiteness and canonical diagonal convention, as the claimant acknowledges at lines 68-69. The counterexamples satisfy stronger trace-class conditions and therefore also refute the literal, weaker conjecture sentence.

What is established: the universal interval assertion is false; for every alpha>2 an admissible real kernel with no corresponding process exists; and the exact universal positive parameter set, under the source's ambient kernel conventions, is {2/m : m >= 1}, together with alpha=0. Nothing here excludes existence for particular kernels at other positive alpha. The claimant's stated result is correct and complete.
