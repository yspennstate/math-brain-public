# Referee report on P4, "Four equivalent forms of the FEI conjecture" (an agent, 10 Nov 23:5x)

Text read: fei_papers_agent/repo_p4/main.tex as of 23:41 (281 lines). Every proof re-derived by hand; numbers
re-computed with my own code, code/referee_p4_check.py (written without reading the paper's code): 60 random functions
n = 3..7 at biases 1/2, 0.15, 0.03, plus majority.

## Verdict
The mathematics is correct. No errors in Lemma 1, Theorem 1 (a)-(d), the equivalences, Proposition 2 or the constant
predictor bound. Three things need fixing before it is a finished paper (items 1-3); the rest are small.

## Checked, correct
- Lemma 1: the sum of 2^|T| signs is even, so d_T f lies in 2^{1-|T|} Z; (d_T f)^2 >= 2^{1-|T|}|d_T f|;
  E d_T f = fhat(T). Max ratio mu/(4^{|T|-1} gamma^2) = 1.000 numerically, attained.
- (a): log2(1/gamma) <= |S|-1 + log2(1/mu)/2 and sum_{S nonempty} mu = Var give A <= I - Var + H/2. Holds, slack >= 0.
- (b): nu_t is the law of U thinned with keep-probability 1-t, sums to 1; Gibbs gives the upper bound, gamma_t >= mu
  the lower. The Gibbs step is right. Holds at t = .25, .5, .75, .9.
- (c): d/ds ln gamma_s = m_s/s; s m_s' = variance of the tilted law, so m_s is nondecreasing; m_s = O(s) needs T in the
  support (stated). B integral formula holds to 1.8e-10 (80-point Gauss-Legendre). The constant: H/2 <= I - Var +
  (1/ln2) int_{1/2}^1 M_s ds/s + I log2 2, so H <= 4I - 2Var + (2/ln2) int ..., and int_{1/2}^1 M_s ds/s <= M_1 ln 2
  gives 2M. The constant 4I - 2Var + 2M is right. Both inequalities hold numerically (min slack 0.22 and 0).
- Equivalence for (c): ds/s <= 2 ds on [1/2,1] one way, int_{1/2}^1 M_s ds <= B ln2 <= H ln2 the other. Right.
- (d): pair contribution p log((p+q)/p) + q log((p+q)/q); second term sums to I L; first in [0, q/ln2]; sum q = I.
  Holds numerically. Combined with Shm1 Cor 5: L <= C gives H <= (C + 3/ln2) I. Right.
- Proposition 2: R sums to 1 with K_p as normalised in the text (the K_p normalisation is right); equality at the
  posterior predictor with K_p = 1. Constant predictor: K = n/(2I), L <= log2(n/I). Holds numerically.
- Remark (centring): S -> S xor R maps {T, T+i} pairs to pairs; E_i invariant, Inf_i -> 1 - Inf_i for i in R.
- Majority: sum E_i = L = 0 exactly (odd support). H/I for majority on 9 = 2.1375 (paper: 2.137).

## Must fix
1. Prior work on the erasure entropies. Intro lines 49-53 credit the E_i form only to [Shm1]. The decomposition of the
   one-coordinate entropy drop into E_i plus a term J_i is eq. (32) of Gonzalez, MacManus, Pereyra, "Further evidence
   towards the Fourier entropy-influence conjecture", arXiv:2606.00246 (June 2026), and the inductive one-coordinate
   route is Han [Han], Remarks 3.1-3.2 (memory fei_one_coordinate_step_is_in_gonzalez_macmanus_pereyra_2606_00246).
   Add GMP to the bibliography and one neutral present-tense clause where E_i is introduced.
2. Remark (centring), the W_1 form. "FEI is equivalent to sum E_i <= C (I - W_1)" needs a step the text does not
   give: Inf_i - fhat({i})^2 >= Inf_i (1 - Inf_i). Proof: D_i f takes values in {-1, 0, 1}, Inf_i = Pr[D_i f != 0] and
   fhat({i}) = E D_i f, so fhat({i})^2 <= Inf_i^2. Hence I - W_1 >= sum_i Inf_i (1 - Inf_i) >= (1/2) sum_i
   min(Inf_i, 1 - Inf_i), and the W_1 form follows from the min form with C replaced by 2C. Checked numerically
   (min over all coordinates of Inf - fhat^2 - Inf(1-Inf) is 0, never negative). Also: the min form for sum E_i follows
   from the E_i invariance alone; Lemma 2.2 of [Shm2] is needed only for the same statement about H. Say which.
3. Theorem 1, "Consequently ... L(f) <= C": that equivalence (and the one for sum E_i) uses [Shm1, Corollary 5],
   which is outside the theorem. Put "(with [Shm1, Corollary 5])" in the statement, or move the L equivalence to the
   corollary after the proof of (d).

## Small
4. Line 143: "A <= H(f)/2 + I(f) by part (a)": write I(f) - Var(f), as proved.
5. Section 6: the slack figures (0.022, 0.0055, 0.16) depend on the sample; characters (H = 0) have zero slack in (a)
   and (b). Say "on these functions" or drop the minima. My sample had zero slack on characters, as expected.
6. Abstract, "The second gives": the second of the three further forms is (c); since the theorem labels it (c), "Form
   (c) gives" reads better.
7. Funding block cites the Google education credit by number; check that the author wants that line (not a math issue).

No sentence about the writing process in the body; the AI declaration is factual. Voice is fine.
