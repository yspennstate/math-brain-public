# Referee report on P7, "The Fourier entropy of linear monotone DNFs on few variables" (an agent, 11 Nov 2026 02:2x)

Read: `fei_papers_agent/p7/main.tex` (520 lines), all of it, read-only. Checks written from the paper's statements, without
the census code or `p7/code/td_check.py`: `code/referee_p7_census_check.py`, `code/referee_p7_bias_check.py`,
`code/referee_p7_td_check.py`, `code/referee_p7_local_check.py` (outputs `*_out.txt`). The pre-draft checks of the census and
of BIAS are in `referee_p7_51f2.md`; this file is the report on the draft and will be merged into it.

## Verdict

The mathematics is correct: Lemma rel, Proposition mix with Lemmas m1-m3, Theorem local, Lemma bias and all four items of
Theorem td hold line by line, and every number in the paper that I recomputed reproduces. One sentence in the introduction
misdescribes how Theorem local relates to Proposition mix, one sentence in Section 3.2 does not match the enumeration of
Section 3.1, and one citation should be added. Fixes at the end, in order of weight.

## Line by line

**Lemma rel (172-193).** Correct. Phi(a,b) <= 2 sqrt(ab): the derivative argument is right (checked numerically too:
max_x Phi(x^2,1) - 2x = 0, at x = 1). Empty set: p = (Ef)^2, q = delta^2 uses Eh = delta, i.e. monotonicity. P = v - delta and
Q = delta - delta^2 are right by Parseval. The last step needs Q <= delta <= v; delta <= v holds for every Boolean f
(Inf_i <= 2 min(Pr[f=1], Pr[f=-1]) <= 4m(1-m) = v for m <= 1/2) but the paper does not say why. Half a clause.

**Width remark (195-197).** With Inf_i >= 2Pr[F=0]/(2^w-1) and v <= 4Pr[F=0], Lemma rel gives 2 + log2(2e(2^w-1)). Correct.

**Census (199-247).** Table: my own labeled enumeration (plain backtracking over subsets, no canonical forms) gives
9 / 97 / 2625 / 185521 functions for n = 3..6 and both maxima to 1e-13; the two n = 8 maximisers recompute to
3.889105419815 and 3.304701322451, and the C4+C4 value of H/I is 3.6125175459 as stated. "Grows at every step from n = 4"
is true for both columns (the min E/Inf column dips from n = 3 to n = 4).
- Lines 220-221: Section 3.1 adds a singleton term at every isolated vertex, which makes labeled linear hypergraphs on [n]
  (edges of size >= 2, isolated vertices allowed) correspond one to one with functions having exactly n relevant variables.
  Then the pair-recursion count IS the third column, and "counted by inclusion-exclusion over the isolated vertices" has
  nothing to do. Either the recursion counts something else (hypergraphs without isolated vertices?) and the sentence should
  say so, or the inclusion-exclusion clause should go. Please check against labeled_check.cpp and make the two sections agree.
- Line 96: "the first exhaustive computation of the FEI ratio on a class of this size" with "as far as we know" is fine.
  The Biswas-Sarkar statement (all functions on at most five variables, max min-entropy/influence 16/7) matches their
  paper (arXiv 2212.07713).

**Proposition mix and Lemmas m1-m3 (249-333).** Correct.
- Lemma m1: on A_t, N = R_t and not V_t; Harris for the two decreasing events; Pr[V_t] <= eta_t because a background term
  meets B_t in at most one variable (it cannot contain i, and it shares at most one variable with t). Bonferroni gives
  A b theta. Fine.
- Lemma m2: h_t = A_t (N restricted to B_t = 1) times the other (1 - A_u), which do not involve B_t; the expansion of A_t
  gives binom(L_t, r) a_t ||h_t||^2 on sets meeting B_t in r variables. Fine.
- Lemma m3: Q_j cannot contain another j' of J (a term through j and j' would meet t twice), so N = R_J prod(1 - x_j Q_j)
  and |D_J N| = 2^{-k} R_J prod Q_j; the s_j are distinct for the same reason; the union bound
  |union| >= sum - binom(k,2) and the lower bound on A are right. Matches P6 Lemma 5.
- Proof: eps = min(1, sum gamma) >= min(1, b) = b because b <= 1/4. Fine.
- Citations to P6 (Proposition 2, Lemma 4, Lemma 5, Theorem 6) match P6's numbering.

**Theorem local (337-367).** Correct, and the constants have room: the exact right side is 4.934 at L = 3, 3.909 at L = 4,
and decreasing after (largest over L = 3..80 is 4.934). Each displayed estimate holds: eps0 = 0.1563 < 0.157,
L eps0 = 0.4689 < 0.47, kappa0 = 0.00130 < 0.0014, second term 0.417 < 0.44, third term 1.584 < 1.79, fourth 0.934 < 0.95.
The split h = h_t + h', the bounds ||h'||^2 <= A u a (Harris for each s != t) and delta >= ||h_t||^2 >= A a theta0, and the
choice Omega = sets meeting B_t are all right.
- Lines 117-119 say Theorem local "is a special case of a finite certificate, Proposition mix". It is not: Proposition mix
  puts thresholds on every term through i, and its kappa then contains alpha_s for the other terms s through i, whose
  variables outside t have unbounded loads (alpha_s can be infinite or its denominator negative). The proof in Section 5
  uses a different Omega and splits off h'. Suggested: "Theorem local is proved by a variant of the argument for
  Proposition mix, which bounds ...".

**Lemma bias (374-390).** Correct; it is the sharper form, with the edge-isoperimetric inequality cited to Harper and Hart.
0 violations in my check (all f on n <= 4; random and structured f to n = 10; the ratio to the bound reaches 0.906 at n = 10).
Line 121's strict "< 2 + 2n/log2(1/m)" follows because log2 e < 2. The ingredients are classical; calling it a lemma rather than
a theorem, as the draft does, is right.

**Theorem td (393-452).** Correct.
- (2): theta = 1 - L ell - (Q-1)a/2 = 1 - O(1/k); the dichotomy (at least Q/2 thresholds >= 4, or at least Q/2 in {1,2,3})
  covers every choice; L^3/(48k^2) and the orders LQ, Q, Q/L are right (ell >= lambda/2 since ell = lambda(1 - 1/Q)).
- (3): E Z = 2^{2k-w} >= 2^k/(8k^2); covariance p^2 for intersecting terms and w(Q-1) neighbours give the Chebyshev bound;
  Harris gives the lower bound. Small point: the bias bound is "at least 2n/r" only once r >= (2 - log2 e)/2 = 0.28, i.e.
  once Pr[F=0] < 1/2 and m = Pr[F=0]; true eventually, worth saying.
- (4): Pr[F=0] = A - delta/2 and delta <= A lambda give Var f/delta -> infinity. Fine.
- Line 415 "w <= Q for k >= 7": true, and already for k >= 3 (k = 3: w = 8 = Q). Either is fine.
- Table 2, own construction (lines {(g, a + bg)}), exact transforms: TD(3,3) 3.085609 / 2.101500, TD(3,5) 3.879785 / 2.715095,
  TD(4,5) 3.902443 / 2.471331, TD(3,7) 4.134586 / 2.533512, and P[F=0] 0.4180, 0.1435, 0.3219, 0.0408: all match.
  TD(5,5) (n = 25): 3.879972 / 2.200337, P[F=0] 0.5332. All five rows match.

**Closing paragraph (446-452).** The class is closed under restrictions (setting x_j = 1 makes the terms through j disjoint,
and the minimal DNF of a linear family is linear), so the induction of [Shm1] applies as stated. "Covering them requires
either ..." claims more than is shown; "would need" or "seems to need" is safer.

## Literature

- Add Hod's lower bound on the FEI constant, C > 6.454784 (R. Hod, Improved lower bounds for the Fourier entropy/influence
  conjecture via lexicographic functions, arXiv:1711.00762; the value as quoted by Biswas-Sarkar - confirm it in Hod's text). Without it a reader may take 3.889 or
  4.135 as evidence about the constant; one sentence after line 103 placing them below the known lower bound for general f
  avoids that.
- Biswas-Sarkar: stated correctly (16/7 over all functions on at most five variables, arXiv 2212.07713; DAM 2025).

## Fixes, in order of weight

1. Lines 117-119: Theorem local is a variant of, not a special case of, Proposition mix.
2. Lines 220-221: make the count description agree with Section 3.1 (inclusion-exclusion vs the bijection).
3. Cite Hod's FEI lower bound next to the TD remark (line 100-103).
4. Lemma rel: say why delta <= v.
5. Theorem td (3): say m = Pr[F=0] once it is below 1/2.
6. Line 450: "requires" -> "would need".

Checked separately: the funding block is word for word P6's; the AI declaration is a short factual record; no sentence in
the body is about the paper's own history.

## Re-check of the revision (11 Nov 02:3x)

All six points are fixed in the 528-line text: line 120 now says Theorem local is proved by a variant of the argument for
Proposition mix; Section 3.2 states the bijection (a singleton at each isolated vertex) and drops the inclusion-exclusion
clause; Hod's bound C > 6.454784 (arXiv:1711.00762) is cited after the TD remark; Lemma rel gives delta <= 2 mu <= 4 mu (1 - mu) = v;
Theorem td (3) sets m = Pr[F=0] once it is below 1/2 and uses "exceeds 2(n-1)/log2(1/Pr[F=0])", which holds; line 455 reads
"would need". The one item left for the author is to confirm the digits 6.454784 in Hod's own text (I have them from
Biswas-Sarkar's citation of it). Nothing further from me.

Published 11 Nov: github.com/yspennstate/fei-linear-dnf-census (0479a01). The author confirmed 6.454784 in the abstract of arXiv:1711.00762 (third construction, monotone f), so the last open item is closed.
