VERDICT: PASS (correct and complete)

Audit of P0204, 11 October 2026

Claim checked

ATTEMPT.md lines 5?11 and 79?89, with the final claim at line 110, assert that there is a universal constant C such that, for every N >= 2 and every coordinatewise increasing V contained in {0,1}^N with |V| >= 2^(N-1), the induced-graph walk P(x,x)=1/2 and P(x,y)=1/(2d(x)) on edges satisfies worst-start total-variation mixing time t_mix(P,1/4) <= C N log N. Its stationary measure is pi(x)=d(x)/D, D=sum_x d(x). This is the question supplied for this audit, with the required quantifiers and stationary measure.

The claim is a literature resolution plus an original chain-convention transfer. The cited paper concerns Q(x,y)=1/(2N) on edges and Q(x,x)=1-d(x)/(2N), whose stationary measure is uniform on V. The claimant does not confuse these kernels or pass a typical-set result off as universal.

No substantive error or missing argument was found. No correction is required for the stated asymptotic result. The bound is explicitly stated for N >= 2; it does not assert the false literal inequality C N log N at N=1. The full one-dimensional cube mixes in one step, and its singleton has mixing time zero.

Independent literature verification

I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md in the claimant's directory. I independently fetched the following URLs with Python urllib, retaining responses in this audit directory rather than relying on the claimant's downloaded files:

- https://arxiv.org/abs/2609.16515v2
- https://arxiv.org/html/2609.16515v2
- https://export.arxiv.org/api/query?id_list=2609.16515
- https://arxiv.org/html/1108.0133v3
- https://arxiv.org/html/2505.02685v2
- https://www.yuval-peres-books.com/markov-chains-and-mixing-times/

All these requests succeeded with HTTP 200. The abstract and arXiv metadata identify Yiming Chen and Yuval Peres, Mixing time under monotone censoring, first submitted 15 September 2026 and revised 19 September 2026. The full text identifies the appendix by Peres. These facts support ATTEMPT.md line 11 and its qualification that this is a public preprint, without a verified journal publication.

Equation (1.1) in the fetched full text is precisely Q above. Equation (1.2) defines worst-start TV mixing at threshold 1/4. Theorem 1.2 applies to EVERY nonempty increasing subset of the cube and states t_mix(Q) <= K a^(-3) N log(eN), with an absolute K and a the ambient cube density. It also states a large-set hitting bound with coefficient 6148. Corollary 1.3 explicitly gives O_c(N log N) for every increasing set of density at least c, N >= 2. Thus ATTEMPT.md lines 11 and 85 cite the correct theorem, rather than a special case, spectral bound alone, or conjecture. Substituting a >= 1/2 makes the constant universal.

The fetched Peres?Sousi paper, Mixing times are hitting times of large sets, arXiv:1108.0133v3, defines t_L using (I+R)/2, and t_H(alpha) using hitting times of R itself. Theorem 1.1 bounds t_L <= c_alpha t_H(alpha) for finite irreducible reversible chains and fixed alpha < 1/2. Taking alpha=1/4 verifies exactly the version used in ATTEMPT.md line 79. It is also correctly quoted as Theorem 2.3 in the Chen paper. No hidden uniform-stationarity or aperiodicity assumption invalidates its application here.

The Peres webpage still presents the half-volume increasing-set problem and conjectures O(N log N), citing Ding?Mossel's O(N^3) result. Its outdated status does not refute the later preprint. The Fei?Ferreira Pinto full text confirms Theorem 1.6 and that its energy normalization is N times the standard Q Dirichlet form, as stated at ATTEMPT.md line 35.

I also ran independent bounded arXiv searches for the exact phrase "monotone censoring" and for hypercube AND (monotone OR censoring). The exact phrase returned Ding?Mossel, the June typical-set paper, and the September universal paper. The broader query returned the Fei?Ferreira Pinto paper among other results, but omitted the September title; it is not an exhaustive status test. An OpenAlex title/topic search returned HTTP 429. No conflicting source or counterexample was found in this bounded search. Responses are saved as search.txt and broad_search.txt; the OpenAlex failure was observed directly.

Independent mathematical checks, with ATTEMPT.md locations

1. Lines 17?19: The upward path from x to x OR y followed by the reverse upward path from y uses exactly the differing coordinates and stays in V. Connectivity and isometry follow. Detailed balance gives edge flow 1/(2D) for P and 1/(2Nm) for Q. Hence pi is degree weighted and generally differs from uniform. All states have positive degree under N >= 2 and the half-volume hypothesis.

2. Lines 23?31: Summing the directed edge contributions with the factor 1/2 in the Dirichlet definition gives E_P=S/(2D), E_Q=S/(2Nm). With c=Nm/D, pi <= c mu and E_P=c E_Q. Minimizing variance over its center yields Var_pi <= c Var_mu. The entropy variational formula uses the nonnegative integrand h log(h/b)-h+b, so the same domination is valid. Both the spectral and classical log-Sobolev transfers have the stated direction. These comparisons do not alone prove the sharp TV bound, and the claimant does not say they do.

3. Lines 35?45: The older spectral result gives gamma_Q >= (1-sqrt(1-a))/N. The transfer yields the same lower bound for gamma_P. Laziness puts the eigenvalues in [0,1]; the L2 initial norm is sqrt(1/pi(x)-1). Since pi(x) >= 1/D and D <= N 2^N, the displayed time makes the TV upper bound <= 1/4. This proves O(N^2), correctly identified as weaker than the target.

4. Lines 51?59: Counting edges from their lower endpoints gives D=2 sum_{x in V}(N-|x|). Cauchy?Schwarz gives Cov(W,1_V)/a <= sqrt(N(1-a)/a)/2. Thus the average degree is at least N-sqrt(N), hence at least N/2 for N >= 4. The separate connected-graph estimate handles N=2,3. Consequently pi <= 2 mu and pi(B) >= 1/4 implies mu(B) >= 1/8. The direction of this implication is correct and is essential to the transfer.

5. Line 63: The embedded neighbor-choice chain is identical for P and Q. At every visit, their waiting times are geometric with success probabilities 1/2 and d(x)/(2N), respectively. Conditional on the common embedded path, common independent uniforms order the waiting times, and their sum up to the first embedded entrance to B orders the hitting times. Therefore E_x^P tau_B <= E_x^Q tau_B. This does not assert that faster holding directly orders TV mixing.

6. Lines 67?75: The contraction coefficient for a zero-mass signed measure is bounded by the maximum pairwise TV distance, which is <=2d_Q(t). Therefore d_Q(2t0)<=1/8 and d_Q(3t0)<=1/16. A target of uniform mass >=1/8 has endpoint probability >=1/16 from every state after 3t0 steps. The Markov property iterates this into a geometric survival bound. Grouping the integer tail sum into blocks gives E tau_B <=48t0. There is no conditioning error: the endpoint estimate is uniform over the state at each surviving block boundary.

7. Lines 79?89: The nonlazy graph walk R is finite, irreducible and reversible with pi; P=(I+R)/2. Its independent geometric holds have mean two, so E^P tau_B=2E^R tau_B. Peres?Sousi applies with alpha=1/4. The claimant's looser constant 48 in line 83 is valid; retaining the factor two would merely improve it. Combining with t0 <=8K N log(eN) proves the displayed 384 C_(1/4) K bound. Finally log(eN) <= (1+1/log 2) log N for N >= 2, yielding the exact requested order with universal constants.

Independent computation

I wrote verify.py in this audit directory; I did not run or modify the claimant's scripts. It recursively enumerates all increasing subsets through N=5 and filters the half-volume condition. Counts are 4, 12, 96 and 4101 for N=2,3,4,5. Exact integer checks verified the upward-edge identity and D/m >= N/2 on every such set. Minimum average degrees were 1, 3/2, 5/2 and 25/8.

Fresh NumPy matrix calculations reproduced the claimant's maximum P mixing times 1, 4, 7 and 10. Stationarity and row-sum residuals were at most 1.12e-16, and no spectral comparison violation occurred. These are floating-point diagnostics, not an asymptotic proof.

For N=2,3, I additionally solved the Dirichlet hitting-time systems (I-P)h=1 and (I-Q)g=1 on each target complement using exact Fraction Gaussian elimination. Every nonempty target subset was included. Across 41 and 2352 start/target comparisons respectively, h <= g held exactly. Starts already in the target have zero hitting time for both walks. Results are retained in verification_results.json. These finite computations test the transfer; its universal justification is the coupling and algebra above.

Scope of the verdict

The literature theorem's existence, statement, kernel, quantifiers and mixing convention were independently verified, and the claimant's full transfer to the specified induced walk was independently re-derived. This is a PASS for SOLVED_IN_LITERATURE. It relies on the cited preprint theorem as an external mathematical result; this audit does not claim an independent proof of every internal lemma of that paper or a full Lean formalization. The claimant explicitly makes the same distinction at lines 97 and 110. Its numerical and limited Lean checks are not being treated as proofs of the asymptotic theorem.

All audit writes were confined to the assigned audit directory. The claimant's directory was read only. No built-in web search, image tools, repository changes, services, or background tasks were used.
