# Referee pass: G0002, "A counterexample to a conjecture of Cerf on second-order pivots"

Paper: yspennstate/second-order-pivots-cerf-conjecture, paper/main.tex (240 lines, dated 5 Nov 2026), read 16 Nov 2026
by agent A. Independent of the author's own check; nobody else has refereed this pass.

Verdict: ACCEPT, minor. Every step of the proof was re-derived by hand; no error found. The stored output of
code/checks.py was reproduced exactly (rerun 16 Nov, python -I, stdlib only; only the run time differs, 2.8 s vs 2.1 s).

## Steps checked

1. Lemma 2.1 (pair witness): with I = {j}, eta = omega minus j, eta^i = eta in A since i in eta, and eta_i = omega minus
   {i,j} not in A. Correct under both readings of (49.1).
2. Lemma 3.1 (band bound): levels |omega| >= d+3 contribute nothing (after one switch-off and one test at 0 at least d+1
   ones remain). Five levels d-2..d+2, each at most C(2d,d) elements times n. Induction b_d <= (d+1)^(-1/2):
   (2d+1)^2(d+2) = 4d^3+12d^2+9d+2 and 4(d+1)^3 = 4d^3+12d^2+12d+4, difference 3d+2 as stated. n <= 4(d+1) gives 10 sqrt n.
3. Section 4 powers: |2z-1| <= 2/h; (2z)^a <= (1-2r/h)^(-1) = 5/4; (2z)^(r-2) >= 1-1/5; r(2/h+2/n) = 1/5 + 1/(50r) < 1/4
   gives 4/3. n/3 <= s-1 needs h^2/6 >= h+1, true for h >= 30.
4. P(omega in A_Y) >= e^(-2Mq0) >= e^(-5/2) in fact; the paper uses e^(-4) > 1/81, valid but loose.
5. Lemma 5.1 (clause graph): an endpoint i outside V has a good edge {i,j}; neither endpoint is in S = P_1^+; the
   clause's positive part is {i,j}, so omega minus {i,j} is not in A. |C minus V| >= |C| - 2B.
6. Coverage: a_i = r(r-1)(s-1) z^(r-2)/n^2 (ordered choice of the i-position and the partner position) is right;
   M a_i >= (8/15) r^2/n is right. The stated upper bound M t_i <= (32/3) r^2/n holds; (20/3) r^2/n already follows
   (2 * 4 * (2/3) * (5/4)). Bonferroni step and E|C| >= r^2/12 correct.
7. Bad edges: singleton probability (z+1/n)^r - z^r <= (r/n)(z+1/n)^(r-1); MQ_S <= (32/9) r; q_E formula and
   MQ_E <= (20/9) r^2 < 4r^2; union bound over (edge clause, endpoint, other clause) with independence of distinct
   clauses under P_omega and symmetry over the coordinates of omega gives E B <= 144 r^3/n. Correct.
8. Conclusion: r^2/12 - 288 r^3/n >= r^2/24 iff r >= 69.12, i.e. n >= 6912 r. Chebyshev 3/4; 3/(4*81*24) = 1/2592;
   r^2/2592 = n/259200; n/259200 > 10 sqrt n iff h > 2,592,000. All checked; checks.py confirms the rational
   margins at h = 10^7 and h = 2,592,010 and the failure at h = 2,592,000.
9. Logic of the refutation: phi_2 >= phi_{2\1}, so a maximizer of either functional exceeds 10 sqrt n 2^n, which no
   set in the band reaches. Correct.

## Citations
- Cerf, arXiv:2608.23661 exists under the title "theta(p_c, Z^d) = 0?" (search 16 Nov 2026).
- Cerf, "The pivotal set of a Boolean function", arXiv:2405.19541 exists (May 2024). The journal reference
  Amer. Math. Monthly 132 (2025) 414-429 was NOT confirmed by search; check the arXiv journal-ref or the Monthly
  before any resubmission.
- Talagrand, Combinatorica 16 (1996) 243-258 and Russo, Z. Wahrsch. 56 (1981) 229-237 match the standard records.

## Suggestions to the author (not applied to the posted paper)
1. Tighten the two loose constants (20/3 in place of 32/3; e^(-5/2) in place of e^(-4)): the threshold dimension drops,
   though it stays astronomically large. The Remark already says the constants are not optimized.
2. The abstract says "a first and second moment count"; the proof uses a first moment plus a Bonferroni (second-order
   inclusion-exclusion) bound for one clause family. "First moment and inclusion-exclusion" is more exact.
3. The introduction does not say what the AI system contributed; only the acknowledgements and the AI declaration do.
