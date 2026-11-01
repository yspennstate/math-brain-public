# F0127: third check (claude-322bc92e, 12 Oct 2026 02:1x)

Verdict: PASS on correctness, but the scope is narrower than the attempt's SOLVED_IN_LITERATURE. Record it as partially resolved in the literature.

The question. Aldous (Bernoulli 2013, Section 5.5, Open Problem 2) asks: assuming (5.2), under what further conditions can one prove E T_coal ~ 2 m_n? His own text around it, read in op/F0127/aldous_source.txt (lines 715-740), matters for the scope:
- he says (5.2) already gives t_mix = o(m_n) by old mixing-time results;
- Stage 2 (n walkers down to m(n) clusters) "requires some different assumptions", and he points to Oliveira [42] for "the current best results".

The attempt's answer:
- transitive with t_rel = o(m_n), from Hermon (AIHP 2022, Theorem 1) plus Oliveira (AoP 2013, Theorem 1.1);
- nontransitive with t_mix = o(n/(log n)^5), from Oliveira's Theorem 1.2.

The derivation is right. I checked:
- m_n = K/2 for symmetric transitive chains. The renewal identities for T_o and for the pair's diagonal give E_pi T_o = K = sum 1/a_r and E M = K/2, using H_t(o,o) = Tr H_t / n and sum_z H_t(o,z)^2 = H_2t(o,o).
- Hermon's bound with max_x E_pi T_x = 2 m_n gives t_mix^(inf)(1/2)/m_n <= r log(4/r) -> 0 for r = t_rel/m_n.
- Oliveira's Wasserstein bound controls the mean, and E S = sum 2/(k(k-1)) = 2.
- The complete-graph normalisation (m_n = (n-1)^2/n, E C_n = 2(n-1)^2/n) is exact.

Why this is not a resolution of the problem as posed. Oliveira [42] is the paper Aldous already cited as the state of the art. And by Aldous's remark, (5.2) already gives t_mix = o(m_n), so for transitive chains Oliveira's Theorem 1.1 applied directly when the question was asked. Hermon's result restates that transitive condition in spectral form (t_rel = o(m_n)), which under (5.2) adds nothing. The question asks for conditions beyond those results, in particular for general nontransitive geometries, ideally (5.2) alone. That part stays open, as the attempt itself says under "Precise limitation".

The audits: o03 and o05 both PASS. Both judged the literal question.
