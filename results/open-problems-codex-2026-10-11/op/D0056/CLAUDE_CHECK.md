# D0056: third check (claude-322bc92e, 11 Oct 2026 22:5x)

Verdict: PASS. The counterexample refutes Conjecture 1 of Chen, Derrida, Hu, Lifshits and Shi (arXiv:1705.04787v2) as stated. The problem is resolved as posed, in the negative. This is a modest result: the conjecture's literal hypothesis is weaker than what the heuristics need.

What I checked, each independently of the attempt and of the two Codex audits:

1. Hypothesis. The paper's condition (4), read in the fetched source.txt lines 101-104, is only criticality with finiteness: (m-1)E(X0 m^X0) = E(m^X0) < infinity. Conjecture 1 (line 115) assumes only (4). The introduction also assumes X0 is not almost surely constant.
2. The law. p0 = cB, p1 = 0, pk = c 2^-k k^-3 for k >= 2, with m = 2 and B = zeta(2) - zeta(3). I recomputed to 30 digits with mpmath: E[2^X] = E[X 2^X] = 1.343359759358150859638306682, so the law is exactly critical. It is nonconstant and satisfies (4). E[X^2 2^X] and E[X^3 2^X] are infinite, so the law sits outside any third-moment repair. The attempt says the same.
3. Recurrence. For m = 2, G_{n+1}(2) = G_n(2)^2/2 + (1-q_n)^2/2, because 2^{(S-1)^+} equals 2^{S-1} on S >= 1 and 1 on S = 0. This gives e_{n+1} = e_n + e_n^2/2 - q_n + q_n^2/2 exactly.
4. Barrier lemma, line by line. If q_n ~ 4/n^2, then q_n - q_n^2/2 >= 3/n^2 eventually. Wherever e_n <= 3/(2n), d_{n+1} <= d_n - 3/(8n^2), so a first d_j <= 0 forces e_k < 0 eventually, which is impossible. Hence e_n > 3/(2n) for all n >= N. Correct.
5. Product. Q_n = prod (1 + e_i) >= K n^{3/2}, using log(1+x) >= x - x^2/2. Correct.
6. The borrowed theorem. Chen and Shi, arXiv:2006.06140v1, Theorem 1.1 (stable.txt line 120): for a critical law with P(Y0 = k) ~ c0 m^-k k^-alpha and 2 < alpha < 4, the product of E(m^Y_i)^{m-1} over i < n lies between c1 n^{alpha-2} and c2 n^{alpha-2}. Here alpha = 3, so Q_n <= c2 n, which contradicts step 5.

Novelty and literature. Chen, Hu and Shi (arXiv:2108.05610, PTRF 2022) prove P(Y_n > 0) = n^{-2+o(1)} only under E(t^Y0) < infinity for some t > m, which this law fails. Chen and Shi (2020) write that their Theorem 1.1 might play a role in the survival asymptotics of the stable system, so they did not derive them. I found no printed statement of this refutation in the files fetched here. The solver's search coverage was incomplete (OpenAlex and Semantic Scholar rate-limited), so the right record is "proved here from a published theorem, no novelty claim". The source authors themselves warned that stronger integrability may be needed.

Not checked here: the Lean file Barrier.lean, and a full literature search beyond the solver's.
