VERDICT: PASS (correct and complete)

# Independent audit of F0127

Audit performed 11–12 October 2026. The verdict applies to the claimant's expressly limited answer giving further sufficient conditions. It does not certify a solution under (5.2) alone or a necessary-and-sufficient characterization.

## Exact claim and fit to the question

ATTEMPT.md lines 9–29 claims the following: for a sequence of finite connected symmetric standardized weighted chains, with each walker having off-diagonal rates Q(i,j)=nu(i,j)/2, if the rate-preserving automorphism group is transitive and t_rel(Q)/tau_meet tends to zero, then the full coalescence time from one walker per vertex satisfies E[T_coal]/tau_meet -> 2. Indeed, its normalized law converges in L1 Wasserstein distance to the sum of independent exponentials with rates k(k-1)/2, k>=2. Here tau_meet includes independent uniform starts that coincide, and the corresponding meeting time is zero.

ATTEMPT.md lines 82–84 additionally claims sufficient conditions without transitivity: Oliveira's alpha=(1+q_max t_mix) pi_max tends to zero and alpha log(1/alpha)(log n)^4 tends to zero. In the specified standardized symmetric half-speed setting, t_mix=o(n/(log n)^5) suffices.

Aldous asks, verbatim, “Assuming (5.2), under what further conditions can one prove” the expected-time asymptotic. Thus supplying these additional sufficient conditions answers the literal question. They imply the conclusion even without separately assuming (5.2), which makes the implication with (5.2) valid. This is a family-level theorem, not a lone example represented as a general solution. CLAIMS.jsonl correctly labels the sufficient-condition results “proved_special_case,” and ATTEMPT.md lines 96–98 expressly limits the verdict. An unrestricted interpretation of the label SOLVED_IN_LITERATURE would be unjustified; the accompanying statement prevents that interpretation.

## Primary sources fetched independently

I downloaded the following PDFs directly from arXiv using Python urllib, all with HTTP 200, and extracted their text locally using PyMuPDF. These are independent downloads, not the claimant's saved copies.

- Aldous, arXiv:1309.6766, saved as aldous.pdf and aldous.txt. PDF pages 15–16 contain (5.2), Open Problem 2, (5.3), and the two-stage discussion. PDF page 12 explicitly specifies rates nu_ij/2 and full initial occupancy. Sections 2 and 5 confirm symmetry, connected support, and uniform stationarity. The distinction in ATTEMPT.md line 15 between a standardization convention and the source's broader geometries causes no restriction error for this user's specified subclass.
- Oliveira, arXiv:1109.5684v3, saved as oliveira.pdf and oliveira.txt. Theorem 1.1 on PDF pages 3–4 is for finite irreducible reversible rate-transitive generators, stationary independent starts for the mean meeting time, and full coalescence. It gives exactly the stated Wasserstein error O([rho log(1/rho)]^(1/6)) and explicitly gives the expectation asymptotic. Theorem 1.2 on page 4 gives the stated general-chain alpha bound with the factor (log |V|)^4. These verify ATTEMPT.md lines 68–84.
- Hermon, arXiv:1908.08525v4, saved as hermon.pdf and hermon.txt. Theorem 1, equation (1.1), on PDF page 3 states t_mix^infinity(epsilon) <= t_rel max{1, log(max_x E_pi[T_x]/(epsilon t_rel))}. The continuous-time rate-one convention is on page 2. Page 5 expressly explains the transitive coalescence consequence using Oliveira. Its proposed nontransitive extension is a belief, not a theorem. ATTEMPT.md does not use that proposed extension.

Oliveira already appears in Aldous's references; it is not a later solution. Hermon's bound supplies the later spectral criterion. ATTEMPT.md lines 27–29 correctly distinguishes these facts. The sufficient-condition verdict does not depend on claiming novelty.

## Independent mathematical checks

No failed step or substantive gap was found. The following potential failure points were checked against the actual assumptions.

1. **Stationary hitting and meeting identities (ATTEMPT.md lines 33–54).** Transitivity makes H_t(o,o) constant in o and hence equal to Tr(H_t)/n. For stationary starts, the hitting-time renewal equation includes the atom at zero and gives F(s)=1/[1+s sum_{r>=2}(s+a_r)^(-1)]. Differentiating at zero gives E_pi[T_o]=sum_{r>=2} a_r^(-1)=K. For the independent pair, symmetry gives sum_z H_t(o,z)^2=H_{2t}(o,o). Transitivity makes this return probability independent of the random meeting vertex. Applying strong Markov at the first diagonal hit gives G(s)=1/[1+s sum_{r>=2}(s+2a_r)^(-1)] and tau_meet=K/2. Finite irreducibility ensures integrability. There is no unwarranted assumption that a relative-displacement chain exists for every transitive geometry.

2. **Generator and mixing conversion (lines 56–66).** Taking P=(I+nu)/2 gives P-I=Q exactly, so Hermon's theorem uses the same physical time. Substitution yields t_mix^infinity(1/2)/tau_meet <= r max{1,log(4/r)}, with r=t_rel/tau_meet. This tends to zero. Relative-density error at most 1/2 implies TV distance at most 1/4 by summing against pi and dividing by two. Consequently the mixing hypothesis needed by Oliveira holds. No missing factor of two occurs.

3. **Full occupancy and expectations (lines 68–78).** Oliveira's theorem covers the initial n walkers, not just fixed m walkers. Its full-coalescence proof in Section 6 explicitly handles the early reduction stage. Thus there is no inserted unproved Stage 2. The limiting exponential sum has expectation sum_{k>=2} 2/[k(k-1)]=2, and L1 Wasserstein convergence bounds the difference of means. Weak convergence alone is not being used to justify convergence of expectations.

4. **General-chain condition (line 84).** Here q_max=1/2 and pi_max=1/n, so alpha=(1+t_mix/2)/n. The proposed stronger condition implies alpha(log n)^5 -> 0, and eventually 1/n<=alpha<1. Therefore alpha log(1/alpha)(log n)^4 <= alpha(log n)^5 -> 0, and alpha -> 0 as separately required. Oliveira's Theorem 1.2 applies without transitivity.

5. **Exact computations (line 92 and CLAIMS.jsonl).** I wrote independent_checks.py, using SymPy rational arithmetic to solve killed pair-chain Poisson equations, single-target hitting equations, and full coalescence equations on occupied subsets. Complete graphs n=2,...,6, cycles n=4,5,6, and a six-state weighted circulant all satisfy E_pi[T_o]=K and tau_meet=K/2 exactly. For each example the claimed meeting-time Laplace transform was checked directly against the killed pair-generator resolvent at s=1/7 and s=3/2. Complete-graph coalescence equations agree with E[T_coal]=2(n-1)^2/n. Separate rational holding-time checks pass for n=2,...,50. Results are in independent_checks.txt. The weighted circulant gives E[T_coal]/tau_meet=5726/2865 rather than exactly 2, consistent with an asymptotic theorem, and guards against treating the complete-graph identity as universal. These finite computations validate identities and normalization, not the asymptotic published theorems themselves.

## Fresh bounded literature search and limits

I repeated an arXiv API search for coalescing random walks with mean-field or Kingman terms, sorted by submission date, and queried OpenAlex and Crossref using Python HTTP requests. Raw responses and query/status/abstract records are retained in arxiv_search.response, crossref_oliveira.response, and literature_search.json. The arXiv search succeeded and returned both cited papers, the Big Bang paper, torus convergence work, directed-graph work, and a 2026 broadcast-voter-model paper. I read the relevant returned abstracts: they concern early density, special geometries, or modified particle dynamics, and do not replace the verified application of the two cited theorems. OpenAlex and the Hermon Crossref lookup returned HTTP 429; Oliveira's Crossref record succeeded. No exhaustive search or proof that no broader solution exists is claimed.

## Issues requiring correction

None in the actual mathematical claim or its stated applicability. No fixes are needed for PASS. The limitation at ATTEMPT.md lines 96–98 is essential: this audit establishes literature-backed sufficient conditions, and does not establish that (5.2) alone suffices on arbitrary nontransitive weighted graphs. No independent reproof of the complete published Hermon or Oliveira theorems is claimed.

All writes for this audit were confined to the assigned audit folder; the claimant's four requested records were read only.
