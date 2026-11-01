VERDICT: PASS

Independent audit of P0211, 2026-10-11. I read the claimant's STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md read-only. Line references below refer to ATTEMPT.md as read during this audit. All audit downloads, scripts and results are in this audit directory. I used neither claimant verification code nor claimant numerical results as evidence.

## What is claimed, and whether it answers the question

ATTEMPT.md lines 7-16 claim, for the continuous-time integer-partition chain with total mass n, merger rate 2/n per unordered pair of distinct clusters, and fragmentation rate beta per internal polymer link, that for every integer n >= 2 and every beta > 0,

    (beta + sqrt(beta) + 1/n)/6 <= gamma_M <= 4(beta + sqrt(beta) + 1/n),

where gamma_M is the smallest positive eigenvalue of minus its generator. Thus relaxation time tau_2 = 1/gamma_M is uniformly of order 1/(beta + sqrt(beta) + 1/n). In particular, if 0 < b_- <= n beta_n <= b_+ < infinity eventually, tau_2 = Theta(sqrt(n)), with constants allowed to depend on b_-, b_+.

I independently downloaded the source page and coag_frag_mix.pdf. PDF page 1 specifies exactly these rates and stationary law. Its Proposition 1 gives the fixed-beta asymptotic lower bound (beta^2 + 4 beta)^(-1/2) on relaxation time and the upper bound beta^(-1). PDF page 4 explicitly asks to close the order-sqrt(n) versus order-n gap at beta_n ~ b/n. The claimed theorem answers that precise relaxation-order question, with stronger uniform quantifiers. It is not merely a fixed-beta result or a special choice beta_n = 1/n. The exclusion of n = 1 is appropriate because that chain has a single state.

This verdict concerns the specified linear-polymer chain, not every coagulation-fragmentation model mentioned on Aldous's broader webpage. The theorem does not claim a sharp asymptotic constant, an exact spectral gap, a total-variation mixing-time order, or a full formalization. None of those is proved here.

## Issues found

No mathematical failure, missing hypothesis, unsupported limiting interchange, or necessary repair was found in the theorem's proof. The delicate locations and their checks are detailed below. The claimant's statements about earlier hostile audits, extensive numerical grids, and a queued Lean job (lines 218-230 and 278-282) are self-reports; I did not adopt them as independent evidence. The proof does not rely on them, and it explicitly disclaims a completed Lean check.

The only external limitation is literature coverage: the fresh OpenAlex request returned HTTP 429. This is not evidence that no earlier solution exists. The bounded successful searches below did not identify an earlier theorem settling this exact question. Priority remains unestablished; it is not needed for mathematical correctness of the submitted order theorem.

## Independent proof review

### 1. Edge representation and stationary projection (lines 20-46)

The auxiliary chain must exclude the empty subset; otherwise the purported death rate is negative there and its stationary formula is undefined. The submission excludes it and gives singleton removals rate zero. For a k-subset the ratio of per-subset stationary masses after one addition is beta n/k, exactly birth rate divided by reverse death rate. Connectivity through unions proves irreducibility.

I re-counted cut sets by marking one cut and ordering the k segment lengths. This gives k N(m) = n k! / product_j m_j!, including the repeated-length cases and the endpoints k = 1,n. Multiplying N(m) by the per-subset weight gives the stated polymer stationary law.

Conditional on a mass partition, a distinguished cut gives a uniformly ordered multiset of segment lengths. There are, on average, 2 m_i m_j/(k-1) boundaries between unequal sizes and m_i(m_i-1)/(k-1) between equal sizes. Multiplication by (k-1)/n yields precisely the merger rates. With k = 2 the two cycle boundaries must both be counted; they are. Internal absent edges produce the fragmentation rates with the correct central-split factor.

Therefore the stationary conditional generator identity is valid. Multiplying it by f and integrating establishes equality of Dirichlet forms, and the pushforward establishes equality of variances. The variational direction is gamma_M >= gamma_B. A Poincare inequality on rotation-invariant edge functions also transfers, because every polymer lift is rotation invariant. No pathwise Markov projection or strong lumpability is assumed. This distinction is essential and is handled correctly.

Independent exact enumeration verified subset multiplicities and every averaged off-diagonal rate for n = 2,...,9 at beta = 1/n and 3/7: 190 partition/parameter cases, using rational arithmetic. In particular this checked equal-size mergers and singleton boundaries.

### 2. Positive comparison, count gradient and upper bound (lines 50-94)

The killed-semigroup argument follows from positivity of exp(tA). For irreducible Metzler A, its positive principal eigenvector and the minimizing/maximizing coordinates of v/h give min(-Ah/h) <= lambda <= max(-Ah/h). All applications here are irreducible birth-death matrices or one-state matrices, with real spectra; there is no problem applying the comparison at an endpoint.

Summing polymer jump rates gives births beta(n-k) and deaths k(k-1)/n for the count chain. Count observables restrict the variational test space, so gamma_M <= gamma_Q, the opposite direction to the edge comparison.

I independently expanded Qg(k+1)-Qg(k). Its derivative generator has birth beta(n-k-1), death k(k-1)/n and killing beta+2k/n on 1,...,n-1. The derivative has only constants in its kernel and is onto that (n-1)-dimensional space, so it identifies all nonzero count eigenvalues, not just a subset. I checked DQ = A_0 D exactly in 87 rational matrix cases, n = 2,...,30 and three positive beta choices. Testing h = 1 gives gamma_Q >= beta+2/n.

For h(k) = 1/[(k+a)(k+a+1)] I independently substituted both neighbor ratios. Symbolic simplification verifies the exact certificate on lines 86-87. The bound follows from k/(k+a-1) <= 1 and n-k-1 <= n for a >= 1. With a = max(1,n sqrt(beta)), its upper bound is beta+4 max(sqrt(beta),1/n). Both choices of the maximum are valid, including beta extremely small or large. No concentration or central limit statement enters this step.

### 3. Completeness and removal of the slow labelled modes (lines 100-169)

I re-derived DU-UD = (n-2j)I by counting extensions/deletions and exchanges. Its inner-product identity proves U injective below the middle layer and D surjective at the required next layer. This gives dim H_l = binom(n,l)-binom(n,l-1), including even-n middle layers. The induction coefficient j(n-2l-j+1) is correct: adding n-2(l+j-1) to (j-1)(n-2l-j+2) gives it exactly.

The norm recurrence proves injectivity of the lifts up to layer n-l and vanishing beyond that layer. For distinct harmonic degrees, moving adjoint maps across the inner product leaves an inner product with Db = 0. Thus the lifts are orthogonal. Summing their dimensions telescopes to binom(n,k) on every layer. This supplies a complete decomposition; there is no omitted sector that could invalidate a spectral lower bound. Removing the empty state changes only the degree-zero radial domain to 1,...,n. I also checked the commutator by exact integer incidence matrices on 42 layers for n = 2,...,8.

The deletion and addition sums for F_a are (k-l)F_a and (n-k-l)F_a. In the latter, harmonicity contributes the negative l F_a term. Substitution into the edge generator gives exactly the killed A_l in lines 145-147; its endpoints have zero outward coefficients. Each harmonic basis vector produces a copy of this radial operator, and the complete decomposition and reversibility justify using its spectra to bound all edge observables.

For l >= 2, killing is at least l beta + l(l-1)/n >= 2 beta+2/n. Degree zero has nonconstant eigenvalues at least beta+2/n. Degree one could be slower, so it must actually be excluded. The zero-sum coefficient representation is injective on every supported layer; a vector fixed by the cyclic rotation has equal coordinates and hence is zero. Sector projection commutes with that rotation because the sector and its orthogonal complement are invariant. Consequently a rotation-invariant observable has no degree-one part, even with arbitrary radial dependence. The claimed polymer lower bound gamma_M >= beta+2/n follows. This is not incorrectly asserted for all labelled edge observables.

Independent full nonempty-subset spectra for n = 2,...,8 at five beta values agree with the count spectrum plus all killed-sector spectra, with harmonic multiplicities; maximum eigenvalue discrepancy was 1.94e-12.

### 4. The sqrt(beta) certificate (lines 173-205)

Under n >= 8 and 4/n^2 <= beta <= 1/16, a = n sqrt(beta) lies in [2,n/4]. Substitution of h = 1/(k+a) into the count-gradient matrix gives lines 177-179; the negative death term is bounded in magnitude by k/n. If k <= a, n-k-1 >= n/2 and k+a+1 <= 5a/2. If k >= a, k/n >= sqrt(beta). These exhaust every count-gradient state.

For l >= 1, I independently combined the death contribution with the killing contribution, obtaining exactly

    beta(n-k-l)/(k+a+1) + l beta
      + (k-1)[(l-1)k+l a]/[n(k+a-1)].

Symbolic simplification confirms this identity. All summands are nonnegative on l <= k <= n-l. If k <= a, l <= k gives n-k-l >= n-2a >= n/2. If k >= a, the bracket is at least a and (k-1)/(k+a-1) >= 1/3, because 2k-a-2 >= a-2 >= 0. Thus each sector's principal eigenvalue is at least sqrt(beta)/5. Its other eigenvalues are no smaller, and completeness gives the full edge-gap bound and hence the polymer bound.

The junction k = a, the single-state middle sectors, and n = 8, beta = 1/16 all satisfy these inequalities. A separate grid checked 39,819 count/sector certificates for n = 8,9,12,16,32,100; the smallest sector-certificate/sqrt(beta) was 0.51, above the required 0.2. This numerical grid corroborates, but does not replace, the pointwise argument.

### 5. Combining regimes (lines 209-216)

The four cases cover all n >= 2, beta > 0. For beta >= 1/16, sqrt(beta) <= 4 beta. For beta <= 4/n^2, sqrt(beta) <= 2/n. For n < 8 and beta < 1/16, sqrt(beta) < 1/4 <= 2/n. In the remaining regime, gamma_M >= sqrt(beta)/5 and gamma_M >= beta+2/n imply s <= 6 gamma_M. Boundary cases are covered with weak inequalities. Inverting positive bounds gives exactly the stated relaxation-time bounds, uniformly in both parameters.

The beta_n comparable to 1/n corollary follows because s is then comparable to n^(-1/2). The other advertised regime orders also follow from the same formula. No asymptotic interchange is used.

### 6. Appendix coupling (lines 238-275)

I separately checked this alternative proof rather than treating it as a premise of the sector proof. Stage I has correct marginal removals: each common occupied edge has rate (k-1)/n in X and k/n in Y. Removal of a common edge from Y alone enters Stage II; removal of the differing edge from Y or its addition to X couples. Thus the total Stage I exit rate is beta+2k/n and the internal killed count generator is A_0.

Stage II simultaneous union/intersection moves each have one clock, giving absorption beta+r/n, not twice that rate. Common-edge deaths have total r^2/n. When r = 0 intersection removal has zero rate, so the empty state is never entered. Exact rational enumeration of both marginal generators passed for 651 eligible pairs at n = 2,...,6. I also symbolically verified the Stage II reciprocal certificate.

The two killed stages have exponential tails at rate c = sqrt(beta)/5. Passing to exponential moments for every theta < c permits concatenation through the strong Markov property without incorrectly asserting a pure e^(-ct) bound for a sum of stages. Triangle inequalities along paths of nonempty subsets extend the bound to all starts. Testing a nonconstant eigenfunction then forces every positive eigenvalue to be at least theta, and letting theta increase to c proves the claimed edge-gap lower bound. Finite prefactors may depend on n,beta because the exponential-rate conclusion is taken for each finite chain. This causes no uniform-gap loophole.

## Additional computational evidence and reproducibility

check_independent.py constructs polymer generators directly from individual pair mergers and individual internal-link splits. At n = 2,...,16 and beta in {10^(-8),1/n^2,1/n,1,100}, all 75 reversible-generator spectra obeyed the theorem, gamma_M >= beta+2/n, and gamma_M <= gamma_Q. Stationary symmetrization was checked before diagonalization. The n = 2 model also gives the exact gap beta+1, consistent with the boundaries.

check_count.py checks the exact gradient intertwining, 545,664 upper pointwise certificates for n up to 10,000 and beta from 10^(-16) to 10^8, and the combination inequality at 441 parameter pairs. All passed. Results are recorded in independent_results.json and count_results.json. The three reciprocal identities were checked symbolically with SymPy. These are independent finite checks; the uniform theorem rests on the reviewed algebra and inequalities, not on extrapolation from computed spectra.

## Fresh bounded literature check

I fetched the Aldous webpage and linked notes directly using Python urllib and extracted the PDF text with PyMuPDF. Stored files: source.html, source.pdf, source.pdf.txt. The original source's unfinished coupling factors were not imported into this proof; the submitted Appendix uses separately valid marginals.

Fresh arXiv API searches covered coagulation with spectral gap/relaxation/mixing time, and fragmentation with Aldous/linear polymers/relaxation time. Raw results are arxiv.xml and arxiv_target.xml. Crossref was queried for coagulation-fragmentation spectral gap/relaxation/Aldous and is stored in crossref.json. The query URLs and successful/error outcomes are in fetch_results.json and target_fetch_results.json. OpenAlex returned HTTP 429 for the new request and was not counted as a negative result.

The potentially relevant finite-particle paper by Hoze and Holcman, arXiv:1611.06493, was downloaded and its abstract and text checked. It derives stationary laws, moments and tagged-particle meeting/separation times, which do not provide the required spectral-gap order. The source-linked Hingant-Yvinec survey, arXiv:1609.00697, was also downloaded; its stochastic model in section 3.1 has monomer attachment/removal transitions, not the all-pair merger and all-link fragmentation chain here. Returned spectral-gap work on spatial coagulation/decoagulation and double-coset chains has different transitions. No checked result gave an earlier solution or a counterexample to the exact theorem. This bounded check establishes neither exhaustive coverage nor originality.

The submitted written proof is correct and complete for the relaxation-order claim as stated. No fix is required for that result.
