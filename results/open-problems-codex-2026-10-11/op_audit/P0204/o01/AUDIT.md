VERDICT: PASS (correct and complete)

# Exact claim and scope

The claimant asserts SOLVED_IN_LITERATURE: there is a universal constant C such that, for every N>=2 and every coordinatewise increasing V contained in {0,1}^N with |V|>=2^(N-1), the induced graph walk P(x,x)=1/2 and P(x,y)=1/(2d(x)) on edges has worst-start total-variation mixing time at threshold 1/4 at most C N log N. Its stationary measure is pi(x)=d(x)/D, where D=sum_x d(x). The singleton convention handles N=1 separately. This is exactly the question posed in this audit, with the correct quantifiers and stationary law.

The September preprint proves the bound for a different kernel, Q(x,y)=1/(2N) on edges and Q(x,x)=1-d(x)/(2N), stationary under the uniform measure mu on V. The claimant supplies a valid transfer to P. Thus this is a literature solution plus a proved chain-convention transfer, rather than an unqualified direct application of the preprint to P.

# Independent source verification

On 11 October 2026 I retrieved the following directly with Python urllib, independently of the claimant's saved responses. All returned HTTP 200; the raw responses are saved in this audit folder.

- https://arxiv.org/abs/2609.16515v2 (chen_abs.html): title Mixing time under monotone censoring; metadata lists Yiming Chen and Yuval Peres; submitted 15 September 2026, revised 19 September 2026. The manuscript credits Chen with an appendix by Peres. The abstract explicitly asserts a universal bound K a^(-3) N log(eN) for every nonempty increasing set, where a is its full-cube density.
- https://arxiv.org/html/2609.16515v2 (chen_html.html; readable mathematical extraction chen_tex.txt): equation (1.1) is precisely Q above; equation (1.2) uses worst-start total variation at 1/4; Theorem 1.2 states the universal mixing bound and a large-set hitting bound. Corollary 1.3 states O_c(N log N) for every increasing set of density at least c. There is no typical-set or extra geometric hypothesis. Section 2.2, Theorem 2.3, also states the required hitting-to-lazy-mixing theorem.
- https://arxiv.org/html/1108.0133v3 (sousi_html.html): Peres and Sousi, Mixing times are hitting times of large sets. Its definitions distinguish the original kernel from its lazy version. Theorem 1.1 gives t_L <= c_alpha t_H(alpha) for finite irreducible reversible chains and fixed alpha<1/2, with t_H measured for the original chain. This is the precise form used in ATTEMPT.md lines 79-83.
- https://www.yuval-peres-books.com/markov-chains-and-mixing-times/ (source.html): Related open problems, Question 1, has the stated increasing/half-volume hypotheses, lazy simple random walk wording, O(N^3) attribution, and O(N log N) conjecture. Its continued presentation as open does not contradict the later fetched preprint.
- https://export.arxiv.org/api/query?search_query=all:%22monotone%20censoring%22&max_results=20 (search.html): the bounded fresh search returned three entries: Ding-Mossel (2013), Oliveira Santos-Tripathi-Youssef (June 2026), and Chen-Peres (September 2026). The June abstract explicitly gives a typical-set result and says its log-Sobolev conclusion is not universal. The September entry explicitly claims the universal mixing result. This search is not an exhaustive priority certification.

The decisive result is a publicly posted arXiv preprint. I verified its statement, kernel, hypotheses, and threshold in full text; I did not independently re-prove its entire internal argument or verify journal publication. That is the appropriate external-theorem boundary for this SOLVED_IN_LITERATURE audit.

# Proof transfer checked independently

1. ATTEMPT.md lines 17-19: The coordinatewise join x OR y supplies an induced path of Hamming length; all its points remain in V. This proves connectedness and positive degrees under the volume hypothesis for N>=2. Detailed balance gives pi(x)P(x,y)=1/(2D). The nonuniformity example (cube minus zero, N>=3) is correct.

2. Lines 23-31: For unordered-edge sum S(f), direct substitution gives E_P=S/(2D), E_Q=S/(2Nm), hence E_P=c E_Q with c=Nm/D. The variance comparison follows by evaluating the minimizing-center formula at the uniform mean. The entropy comparison uses the nonnegative function h log(h/b)-h+b and its minimizing b. These prove the claimed spectral-gap and classical log-Sobolev comparisons, but alone do not prove the sharp total-variation bound. The claimant correctly makes that distinction.

3. Lines 35-45: Conditional on the stated earlier Poincare theorem, the spectral calculation is correct: laziness makes the spectrum nonnegative, initial squared L2 density norm is 1/pi(x)-1, and TV is bounded by half the L2 norm. The estimate pi(x)>=1/D and D<=N2^N produces only O(N^2). This weaker bound is not passed off as the solution. I did not need to certify the earlier paper separately to establish the final verdict.

4. Lines 51-59: Count each induced edge from its lower endpoint to obtain D=2 sum_{x in V}(N-|x|). With full-cube uniform X and W=|X|, Cov(W,1_V)/a=E[W|V]-N/2. Cauchy-Schwarz and Var(W)=N/4 give a shift at most sqrt(N)/2 for a>=1/2. Therefore average degree >=N-sqrt(N)>=N/2 for N>=4. The connected-graph bound D>=2(m-1) gives the needed N=2,3 exceptions. Consequently pi<=2mu, and pi(B)>=1/4 entails mu(B)>=1/8. The direction of this implication is correct.

5. Line 63: Both walks have the same embedded neighbor-uniform jump chain. Their holding times at a visit to x are geometric with parameters 1/2 and d(x)/(2N), respectively. Coupling by inverse CDF makes each P holding time at most its Q counterpart. The first embedded visit to B has the same index. Summing holdings gives tau_B(P)<=tau_B(Q) pathwise. This proves a hitting-time comparison, without asserting a generally unjustified pointwise TV comparison.

6. Lines 67-75: Dobrushin contraction gives d_Q(s+t)<=d_Q(s) bard_Q(t), and bard_Q(t0)<=2d_Q(t0)<=1/2. Hence d_Q(3t0)<=1/16. Every B of mu-mass >=1/8 has endpoint probability at least 1/16 after 3t0 from every starting state. Endpoint membership implies a prior hit. Conditional block iteration bounds survival by (15/16)^j. The integer tail-sum formula then gives E tau_B(Q)<=48t0, and thus t_H^P(1/4)<=48t0. The block bound does not require B to be increasing.

7. Lines 79-89: Let R be the nonlazy induced walk. It is finite, irreducible and reversible, with pi stationary, and (I+R)/2=P. Mean-two independent geometric holding gives t_H^P(alpha)=2t_H^R(alpha). The verified Peres-Sousi theorem yields t_mix(P,1/4)<=C_(1/4)t_H^R(1/4)<=48C_(1/4)t0. Using the factor two would sharpen 48 to 24, but the deliberately loose inequality is valid. The fetched Theorem 1.2 gives t0<=8K N log(eN), so the displayed 384C_(1/4)K bound follows. For N>=2, log(eN)<= (1+1/log 2)log N, yielding the claimed universal O(N log N).

# Independent computations

I wrote and ran independent_checks.py in this folder, without executing the claimant's scripts. Results are in independent_checks.json.

- Recursively enumerated all half-volume increasing subsets for N=2,3,4: 4,12,96 sets.
- Checked the edge-count identity and average-degree bound with integers for every set. Minimum average degrees were 1, 1.5, 2.5, respectively.
- Constructed P,Q and checked stationarity, pi<=2mu, the Dirichlet-matrix identity, and gap(P)>=gap(Q) numerically with tolerance 1e-12. Minimum observed gap difference was zero in each dimension.
- Independently obtained maximal induced-walk mixing times 1,4,7 at threshold 1/4 using floating-point matrix iteration. These agree with the claimant's corresponding reported values; they are diagnostics, not asymptotic proof or exact certified mixing times.
- For N=2,3, checked every nontrivial target of pi-mass at least 1/4 using exact rational arithmetic: 24 and 661 set-target pairs. Verified mu(B)>=1/8 by integer comparison, solved the killed-chain equations, and confirmed h_Q>=2h_R=h_P componentwise. This directly checks the hitting comparison rather than relying on simulation. No N=5 replication was needed for the proof.

The first run of my checker reached its final output-writing step but lacked a pathlib import; I added the import and reran it successfully. This was an audit-script error, not an issue in the claimant's work.

# Issues found and verdict limits

No substantive mathematical issue was found in ATTEMPT.md. In particular, the stationary-law mismatch at lines 7 and 11 is explicitly acknowledged and completely addressed in section 4; it is not a remaining gap. The nonlazy/lazy distinction at lines 79-83 is handled correctly. The unused factor two at lines 83-85 is harmless slack, not a correction required for validity.

The Lean checks described at line 97 are explicitly limited; I do not treat them as verification of the full theorem or transfer and did not rerun them. Likewise, the finite computations in lines 93-95 are not a proof of the asymptotic bound. Neither limitation undermines the independently checked analytic transfer and the verified external literature theorem.

What stands: assuming the cited preprint theorem as the literature result it is claimed to be, every increasing half-volume subset satisfies the requested universal O(N log N) worst-start total-variation mixing bound for the degree-weighted lazy induced walk. The claim answers the exact problem. No small fixes are necessary, so PASS rather than PASS_WITH_GAPS is warranted.
