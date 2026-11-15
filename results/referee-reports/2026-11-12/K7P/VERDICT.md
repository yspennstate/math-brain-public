# K7P verdict (an agent, 12 Nov 2026)

Question: lumping a reversible chain with r = 2 merges, is the mixing-time ratio at most 3? Settles K(7) in {3,4}.

Verdict: SOUND as a partial result. K(7) stays open, 3 <= K(7) <= 4.

Checked independently (indep_check_agent.py, my own sympy hitting solves, exact rationals):
- Section 2 family (a,b,u,v): T = N/W exactly and a_a = t^2(t^4+1)^2/W exactly at t = 2, 3, 10; a_a/T at t = 10 is 891.27 (= 5001000050/5611071). Since a_a/T = t^2(t^4+1)^2/N ~ t^3, no bound a_i <= C T or C(t_i+T) exists. This closes the diagonal / Cauchy-Schwarz route for good.
- Section 3 sequential example: both exact fractions reproduced; intermediate row sums exceed t_a+t_b+T, while the final entry stays at 1.637 T.
Read, not separately computed: the cloning and padding arguments of Section 2 (short, look right); the boxed orthogonal-minimum inequality of Section 4 (proof read step by step, holds; its sufficient mean bound is refuted by the run's own exact witnesses).
Search evidence: about 836,000 exact rank-two evaluations at n = 6, 7, 8 (389,193 optimizer + 447,028 prequotient partitions); best pairs ratio 3 - 6e-12 (the R3 family of K6P), triple 2 - 2e-12. Evidence, not proof.

For the lumping paper: state the factor-3 question for two merges as open; the a_i ~ t^3 family can be cited as the reason projection-cost bounds cannot work.
