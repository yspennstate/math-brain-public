VERDICT: PASS (correct and complete)

# Independent audit of F0127

The verdict applies to the claimant's explicitly scoped answer: further **sufficient** conditions for Aldous's displayed asymptotic. It does not certify a theorem under (5.2) alone or a necessary-and-sufficient characterization.

## What is claimed, and whether it answers the question

ATTEMPT.md lines 9–29 claims the following. For a sequence of finite connected symmetric standardized rate matrices, let the walkers have off-diagonal rates nu_ij/2 and diagonal rates -1/2. If rate-preserving permutations act transitively and t_rel/tau_meet tends to zero, then the full coalescence time C, starting with one walker at every vertex, satisfies E C/tau_meet -> 2. Moreover, C/tau_meet converges in L1 Wasserstein distance to the sum of independent exponential variables with rates binom(k,2), k >= 2.

This is a sufficient-condition answer to the actual wording “Assuming (5.2), under what further conditions can one prove” (5.3). The conclusion holds under the stated extra conditions even without imposing (5.2), hence certainly holds for sequences also satisfying (5.2). No implication from (5.2) to transitivity is needed or claimed. The restriction is explicit in ATTEMPT.md lines 29 and 96–98 and in CLAIMS.jsonl. A special case is therefore not being presented as an unrestricted theorem. A verdict claiming that (5.2) alone had been settled would fail this audit; that is not the recorded claim.

The additional nontransitive sufficient condition at line 84, t_mix = o(n/(log n)^5), is also valid in the standardized symmetric setting.

## Issues found

No substantive mathematical error, missing hypothesis, or necessary repair was found in ATTEMPT.md. The following scope and convention points were checked because each could otherwise invalidate the argument:

- **Lines 7–15: exact source and normalization.** Aldous's PDF pages 15–16 contain (5.2) and Open Problem 2 exactly as quoted. Page 12 identifies the coalescing walkers' rates as nu_ij/2. Pages 2 and 7 establish symmetry, connectivity and uniform stationarity. Page 5 makes clear that (2.2) is a standardization for constant-row-sum geometries, not a requirement for every geometry in the original article. The claimant explicitly acknowledges this and answers the standardized subclass specified in the audit request.
- **Lines 21–29 and 68–78: sufficient conditions versus full resolution.** Rate transitivity is required, not merely transitivity of the support graph. Oliveira's theorem controls the fully occupied system and first moments, not only finitely many walkers or convergence in distribution. Those requirements are present. The claimant correctly leaves the general problem under (5.2) alone unresolved.
- **Lines 37–54 and 92: stationary starts can coincide.** The diagonal mass 1/n must not be discarded. It is retained in both renewal arguments and in the complete-graph computation. This is essential for the asserted exact finite-n identities.
- **Lines 56–66: generator and mixing conventions.** Hermon's rate-one representation accommodates the claimant's generator through P=(I+nu)/2, so no factor of two is lost. Oliveira Section 2.3.2 uses the opposite sign for its operator called Q; its stochastic transition rates are the same q(x,y), so this is purely a notation convention. His Section 2.3.3 defines t_mix at TV error 1/4, exactly the threshold implied by relative-density error 1/2.
- **Lines 80–84: nontransitive result and chronology.** Theorem 1.2 has the claimed alpha log(1/alpha)(log n)^4 error parameter. Oliveira is already Aldous reference [42]; these mixing conditions are not a newly discovered post-2013 resolution. The claimant correctly says so. Hermon's later result supplies the stronger transitive spectral criterion.

## Primary literature fetched independently

I downloaded the following PDFs directly from arXiv using Python urllib, rather than relying on the claimant's extracts. Copies and page-labelled UTF-8 extracts are in this audit folder.

1. Aldous, *Interacting particle systems as stochastic social dynamics*, https://arxiv.org/pdf/1309.6766. Checked Sections 2, 5.1 and 5.5 and reference [42]. The Stage 1 discussion is explicitly tentative; the claimant does not treat it as a proof.
2. Oliveira, *Mean field conditions for coalescing random walks*, https://arxiv.org/pdf/1109.5684, v3. Theorem 1.1, PDF pages 3–4, explicitly concerns irreducible reversible transitive chains, stationary independent mean meeting time m(Q), and full coalescence. It gives the stated Wasserstein error O((rho log(1/rho))^(1/6)) and explicitly E C=(2+O((rho log(1/rho))^(1/6)))m(Q). Theorem 1.2, page 4, gives the general-chain alpha bound. The introduction starts with one walker at every vertex; Section 6.1 treats the reduction from full occupancy, so Stage 2 is not an unproved addition by the claimant.
3. Hermon, *Some inequalities for reversible Markov chains and branching random walks via spectral optimization*, https://arxiv.org/pdf/1908.08525, v4. Theorem 1, PDF page 3, gives exactly

       t_mix^infinity(epsilon) <= t_rel max{1, log(max_x E_pi T_x/(epsilon t_rel))}.

   Page 5 explicitly describes the combination with Oliveira as resolving the transitive Aldous–Fill spectral conjecture. Its broader nontransitive extension is described as a belief, not a theorem. No such extension is used in ATTEMPT.md.

A fresh bounded arXiv API query for coalescing random walks and mean field/Kingman terms succeeded and is saved as literature_query.xml. It returned both main cited papers, the Big Bang regime paper, the torus-to-Kingman paper, and directed-graph results. This corroborates the literature leads; it is not an exhaustive search or evidence that the unrestricted (5.2)-only problem is solved.

## Independent mathematical checks

I re-derived the applicability argument rather than accepting the claimant's calculations:

For H_t=exp(tQ), symmetry and transitivity imply H_t(o,o)=Tr(H_t)/n. Starting from uniform stationarity, the first-hit renewal equation for o yields F(s)=1/[1+s sum_r 1/(s+a_r)]. Differentiation at zero gives E_pi T_o=K=sum_r 1/a_r. For the independent pair chain, the diagonal return probability from (o,o) is sum_z H_t(o,z)^2=H_2t(o,o). Transitivity makes this independent of the first meeting location, so the same renewal calculation gives G(s)=1/[1+s sum_r 1/(s+2a_r)] and tau_meet=K/2. Both arguments include first-hit mass at zero.

At epsilon=1/2, Hermon's bound therefore becomes t_mix^infinity/tau_meet <= r max{1,log(4/r)}, with r=t_rel/tau_meet. This tends to zero as r->0. TV mixing is bounded by this uniform mixing time. Oliveira Theorem 1.1 consequently applies. The limiting sum has mean sum_{k>=2} 2/[k(k-1)]=2; L1 Wasserstein convergence implies convergence of expectations by |E U-E V| <= d_W(Law(U),Law(V)). All quantifiers are along arbitrary sequences satisfying the stated hypotheses.

For line 84, q_max=1/2 and pi_max=1/n give alpha=(1+t_mix/2)/n. Under the stated sufficient condition, alpha->0 and, eventually, 1/n<=alpha<1. Thus alpha log(1/alpha)(log n)^4 <= alpha(log n)^5 ->0. This verifies the general-chain application.

The runnable independent script check_identities.py and its output independent_checks.txt provide additional falsification checks. Direct killed-generator linear systems for an unweighted 7-cycle, a weighted 9-cycle, and the 8-vertex complete graph agree with E_pi T_o=K and tau_meet=K/2. Direct pair-chain Laplace transforms agree with the renewal formula at s=0.03, 0.4 and 2.0. Numerically computed uniform mixing times satisfy the quoted Hermon bound. Exact rational complete-graph checks for every n=2,...,50 give tau_meet=(n-1)^2/n and E C=2(n-1)^2/n. These finite checks test normalization and identities; they are not proofs of the asymptotic theorem.

The established result is a valid literature-based sufficient-condition answer, with a correct derivation of applicability. The full published proofs of Hermon and Oliveira are relied on as literature results; this audit does not claim to replace them with new proofs. No repair is required.
