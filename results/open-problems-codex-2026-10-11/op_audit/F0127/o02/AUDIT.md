VERDICT: PASS

# F0127 independent hostile-referee audit

Date: 2026-10-11. Claimant files examined read-only: STATUS.md, ATTEMPT.md, CLAIMS.jsonl, LITERATURE.md. Locations below are line numbers in ATTEMPT.md. All audit artifacts were written in this audit directory.

## Exact claim and scope

The principal claim (lines 19-29; CLAIMS.jsonl entry 1) is this: for a sequence of finite connected symmetric weighted chains on n vertices, with off-diagonal rates Q(i,j)=nu(i,j)/2 and sum_{j != i} nu(i,j)=1, rate-preserving transitivity and t_rel(Q)/tau_meet(Q) -> 0 imply E T_coal/tau_meet -> 2. The initial configuration has one walker at every vertex; tau_meet uses two independent uniform starting vertices, including coincident starts. The claimant also asserts L1 Wasserstein convergence to the Kingman full-coalescence law.

The subsidiary nontransitive sufficient condition (line 84; CLAIMS.jsonl entry 3) is t_mix=o(n/(log n)^5), in the same symmetric standardized half-speed setting.

These statements answer the literal request for further sufficient conditions assuming (5.2). They hold even without imposing (5.2), hence hold on the intersection with (5.2). No argument that the extra hypotheses are necessary is required by the quoted question. The claimant explicitly limits its verdict at lines 29 and 96-98 and labels the principal claims as special cases in CLAIMS.jsonl. It does not pass off transitivity as covering arbitrary geometries.

PASS is for this explicitly scoped literature answer. It does not certify a necessary-and-sufficient characterization, an unrestricted theorem from (5.2) alone, or a new proof of the published foundational theorems.

## Primary literature verification

I independently downloaded the full PDFs from https://arxiv.org/pdf/1309.6766, https://arxiv.org/pdf/1109.5684 and https://arxiv.org/pdf/1908.08525 and extracted their text into aldous.txt, oliveira.txt and hermon.txt in this directory. All three requests succeeded (HTTP 200).

1. Aldous, Section 5.5, PDF pages 15-16: the half-speed convention, (5.2), and Open Problem 2 agree with lines 9-15. The source says Stage 1 is likely, and that Stage 2 needs different assumptions. Thus the claimant is correct not to use the source's sketch as a proved general theorem. Section 2.5 states standardization (2.2) only for constant-row-sum geometries; line 15 correctly distinguishes the source's broader setting from the user's standardized setting.

2. Oliveira, Theorem 1.1, PDF pages 3-4: the theorem applies to finite irreducible reversible transitive generators, defines m(Q) by independent stationary meeting times, and controls the full coalescence time in L1 Wasserstein distance by O((rho log(1/rho))^(1/6)), rho=t_mix/m(Q). It explicitly also gives convergence of the mean to 2m(Q). The mixing convention is worst-start total variation at threshold 1/4 (Section 2.3). The full-occupancy initial configuration and early reduction phase are covered, not merely a fixed number of walkers. This verifies lines 68-78.

3. Hermon, Theorem 1, PDF page 3, equation (1.1): the bound is exactly t_mix^(infinity)(epsilon) <= t_rel max{1, log(max_x E_pi T_x/(epsilon t_rel))}. It applies to finite irreducible reversible chains and permits P with self-loops. Thus P=(I+nu)/2 has P-I=Q and introduces no speed conversion. The coalescence discussion on PDF page 5 explicitly invokes Oliveira and resolves the transitive Aldous-Fill spectral criterion. Its broader nontransitive extension is stated as a belief, not a theorem; the claimant does not rely on it. This verifies lines 56-66 and the historical distinction at line 29.

4. Oliveira, Theorem 1.2, PDF page 4: the general-chain bound uses alpha=(1+q_max t_mix)pi_max and error O((alpha log(1/alpha)(log |V|)^4)^(1/6)). It agrees with line 84. Here q_max=1/2, pi_max=1/n. Under the stated convenient condition alpha -> 0, eventually 1/n <= alpha < 1 and log(1/alpha) <= log n; consequently the error parameter is bounded by (1+t_mix/2)(log n)^5/n -> 0. No additional meeting-time condition is missing.

Crossref independently confirmed both theorem papers' titles, journal volumes, pages and publication dates: Oliveira September 2013 (DOI 10.1214/12-AOP813), Hermon August 2022 (DOI 10.1214/21-AIHP1208). Oliveira was already source reference [42]; presenting his theorem alone as a later solution would be misleading, but the claimant expressly avoids doing so.

## Independent mathematical checks

Lines 33-47: rate symmetry and transitivity make H_t(o,o) the trace divided by n. For a stationary single walk, decompose the event X_t=o at its first hitting time T_o, including the atom T_o=0. The strong Markov property yields the displayed renewal identity. Its Laplace transform is 1/(ns)=F(s)R(s). Substitution of the spectral expansion gives F(s)=[1+s sum_{r>=2}(s+a_r)^(-1)]^(-1), and differentiation at zero gives E_pi T_o=sum_{r>=2}a_r^(-1)=K. Finiteness follows from finite irreducibility. No sign, atom or normalization defect was found.

Lines 49-54: the stationary pair has diagonal probability 1/n. Starting from (o,o), its diagonal return probability is sum_z H_t(o,z)^2=H_{2t}(o,o), using symmetry. Rate transitivity makes this probability independent of the first meeting location. Applying the same renewal calculation doubles the eigenvalues, so E M=K/2. Using this identity without transitivity would be unjustified; the claimant confines it to the transitive derivation.

Lines 61-66: substitution into Hermon's bound gives t_mix^(infinity)(1/2)/m <= r max{1,log(4/r)}, with r=t_rel/m. This tends to zero if r -> 0. Relative density error at most 1/2 implies total variation at most 1/4 by summing against pi and dividing by two. Thus Oliveira's actual mixing convention is met.

Lines 73-78: independent Kingman holding times have means 1/binom(k,2). Their sum has expectation sum_{k>=2}2/[k(k-1)]=2 by telescoping and monotone convergence. The coupling inequality |EU-EV| <= E|U-V|, followed by the infimum over couplings, proves the needed convergence of means from L1 Wasserstein convergence. Weak convergence alone would not justify this step, but is not what is used.

Line 92: on the half-speed complete graph a distinct pair meets at rate 1/(n-1). Uniform independent starts are distinct with probability (n-1)/n, so tau_meet=(n-1)^2/n. The k-cluster merger rate is binom(k,2)/(n-1), yielding E T_coal=2(n-1)^2/n. I checked these identities with exact rational arithmetic for n=2,...,100.

For additional independent numerical checks, independent_checks.py builds the killed two-walker generator Q tensor I + I tensor Q and solves its backward equations, separately solves single-target hitting equations, and separately builds the coalescing occupancy generator on nonempty subsets. It covers complete graphs n=2,...,8, cycles n=3,...,8, and weighted symmetric circulants n=5,...,8. All meeting means agree with K/2 and all stationary target means with K to tolerance 1e-9. Matrix exponentiation verifies Hermon's density-error bound at the proposed bound time. Computed complete-graph coalescence ratios are 2. Weighted-circulant finite-size ratios differ slightly from 2, which is consistent with an asymptotic claim. Results are in independent_checks.txt. These finite computations test applicability and normalization; they are not a proof of an asymptotic theorem.

## Issues and remaining limits

No mathematical error or required repair was found in ATTEMPT.md under its explicit scope. No PASS_WITH_GAPS correction is necessary.

Scope caveat, lines 19-29 and 96-98: the SOLVED_IN_LITERATURE label must retain the supplied limitation to further sufficient conditions. Interpreting that label as settling (5.2) alone for all nontransitive geometries would not be supported. The actual text retains the limitation, so this is not a defect in the submitted claim.

Historical caveat, lines 27-29 and 82-84: Oliveira's conditions were known when Aldous posed the question. Hermon's later result supplies a distinct spectral sufficient criterion under transitivity. None of these facts establishes a complete resolution of every possible interpretation of the broader research program.

I performed a fresh bounded arXiv API search for coalescing random walks with mean-field or Kingman terms. It returned the cited papers and related Big Bang, torus, and directed-graph work. OpenAlex returned HTTP 429; this limitation is recorded in search_log.txt. The arXiv response and Crossref responses are preserved locally. This was not an exhaustive literature search, and the verdict rests on verified positive theorems rather than an absence of counterexamples in search results.

The unrestricted implication from (5.2) alone and the source's suggested general Stage 1 remain unproved by this submission. The stated transitive spectral and nontransitive fast-mixing sufficient conditions are proved by the cited literature with the applicability arguments checked above.
