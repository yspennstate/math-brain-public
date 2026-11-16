# LO05: Section 2 (the reduction: finite rational tests force an integer zero) read line by line (12 Nov 2026)

Source: lit/openai_oct6/paper_c.txt, lines 225-719 (text extraction of paper.pdf in openai/math tree
0a112e434f6bf7f316e2999a63813ce58447e432). Each step below was re-derived by hand. The inputs it uses were
checked separately: Props 2.1, 2.2 (Section 5, LO05_SECTION5_CHECK.md), Theorem 2.4 (Section 4,
LO05_SECTION4_CHECK.md), Cor 2.6 (Section 6, LO05_SECTION6_CHECK.md), Prop 2.8 (Section 3, LO05_SECTION3_CHECK.md).

| Part | Content | Check | Result |
|---|---|---|---|
| 2.1, (2.2)-(2.5) | point data T_a in E(F_R), additive, in mE(F_R), finite with xy != 0 for a != 0; in the ambient extension T_a = eta(a)P | mE(F) = ZP transfers; eta additive with eta(1) = 1; eta(a) = 0 forces T_a = O, hence a = 0, so eta is injective | holds |
| Lemma 2.3 | local comparison at an ambient prime q > K+1 outside S_E | (2.6) on the conjugate points gives v_q(eta((h-4)a)/eta(j0)) >= K, and eta(j0) is a nonzero ambient integer, so v_q(eta((h-4)a)) >= K; V_a = eta(ha) = 4 eta(a) mod q^K and V_1 = 4 mod q^K, so V_a/V_1 = eta(a) mod q^K (q odd); (2.7) on the primary points (ratio now integral) and (i) give v_q(a - eta(a)) >= K and integrality of a | holds |
| Thm 2.4, Cor 2.5 | five-point height estimate h(s) <= H M_S(s)^c; enlarging S keeps c | contact orders independent of scaling; M_S <= (prod over S' \ S of q) M_S' | holds |
| Cor 2.6 | ordinary contact representations | proved in Section 6 | holds |
| 2.3, Lemma 2.7 | the recursive theory T and its model Z with T_a = aP | R[sqrt 2] = R[X]/(X^2 - 2) since sqrt 2 is not in Frac(R); the branches p+, p- are the two places above a split r; (2.15), (2.16) are exactly v_r >= K at that place; constants hardcoded, no search needed | holds |
| 2.4, Prop 2.8 use | Phi on every term value; product observation v_q(c) = v_q(ac) - v_q(a) even | proved in Section 3 | holds |
| 2.4, the tests | ground terms, constraints (a)-(d), each finite part an existential rational query | inequations g != 0 as gy = 1, disjunctive normal form, sum of squares; soundness: an integer zero extends the model of Lemma 2.7 with Skolem functions, all term values are integers and satisfy Phi | holds |
| Lemma 2.9 | compactness: an elementary extension, a model R of T with f(a) = 0 embedded in *Q, Phi on every element | each finite subset is realized in the ordinary structure by a successful test; R = term values; (b) makes functions well defined; (c) gives every universal Skolem axiom since every element is a term value | holds |
| 2.5, (2.18) | some listed factor r has odd v_q(r) at every ambient q counted by M_K(s_i) | at q outside S_K two contact forms have unit determinant, so the least of the five valuations is t = min(v_q(u_i), v_q(v)); an odd contact depth makes the five valuations not all of one parity; k is a q-unit | holds |
| Lemma 2.10 | a tested branch p and a place v* above q with D' in r^l (R_F)_p implying v*(D') >= l | every ring value in the convex subgroup J is even (Phi on b and ab with v_q(b) < -abs(v_q(a))); v_q(r) is odd, so outside J and positive; coarsening by J is nonnegative on R_F; its center contains r and R_F/rR_F is a product of two fields, so the center is p+ or p-; if J != 0 it contains Z and a positive class exceeds every ordinary integer | holds |
| Prop 2.11 | v_q(a - eta(a)) >= K for every a in R and every ambient q counted by M_K(s_i) | Lemma 2.10 turns (2.15), (2.16) into the hypotheses of Lemma 2.3; q outside S_K gives q outside S_E and q > K+1 | holds |
| Prop 2.12 | the height contradiction | v_q(delta) >= K from the congruences and integer coefficients; the internal universal premise gives M_K(s_i)^K divides delta; with K >= cD, M_K^c <= C_f^(c/K) B^(cD/K) << B; h(A) << B for every A in R; then h(x(eta(a_j)P)) << B against 2 h(P) B^2 + O(1), so B is ordinary, eta(a_j) = n_j ordinary, a_j = n_j by injectivity, and f(n) = 0 | holds |
| Thm 1.1 | rational decidability would decide integer solvability, against DPRM | run the test search and the enumeration of integer tuples in parallel; both answers sound | holds |

Remarks. The divisibility M_K(s_i)^K | delta is the transfer of an internal statement whose premise quantifies over
all ambient primes; the premise was proved for each such prime, with the coarsenings chosen outside the structure,
and only that universal assertion enters the transfer, as the paper says. Section 7 (Turing degree and a quartic
normal form) is a further result and is not used in Theorem 1.1; it was not read.

What this changes: with this, every section that Theorem 1.1 depends on (2, 3, 4, 5, 6) has had one independent
read with no gap found. LO05 stays REPORTED_SOLVED: the proofs of the two cited companion preprints ([48], [49])
are unread, the external citations were checked against the forms quoted rather than the sources, and a solved
mark needs a second independent audit.
