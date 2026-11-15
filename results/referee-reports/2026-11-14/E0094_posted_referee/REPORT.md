VERDICT: ACCEPT (no correction needed)

Independent post-posting referee pass on "Adding one permutation to a transposition and a long cycle"
(E0094, Diaconis 2013 Question 3), https://github.com/yspennstate/one-generator-shuffle (main.tex at 7748293,
cloned 14 Nov 2026 02:3x laptop time; Zenodo 24200518). Referee: an agent (Claude Opus 5.5), not the
writer of the proofs; the pre-posting reports are referee_reports/2026-11-13/E0094A and E0094AR. Lane:
T-20261112-017, independent referee passes on posted papers.

Checked by hand, line by line:
- Setup: for n >= 5 the five elements tau, c, c^{-1}, sigma, sigma^{-1} are distinct and non-identity
  (sigma fixes 0, sigma(1) = 2, sigma = sigma^{-1} forces n | 3). Correct.
- Lemma 2.1 (powers of c): sigma c^q sigma^{-1} = c^{2q}, so c^{2q+b} = sigma c^q sigma^{-1} c^b; reading the
  binary digits of i gives a word of length at most 3k - 2 for i < 2^k, hence at most 3h - 2. Correct.
- Lemma 2.2 (the transposition (0, d)): with d = sum of 2^{j_l}, A_l = c^{a_l} sigma^{j_l} and
  A_l^{-1} A_{l+1} = c sigma^{j_{l+1} - j_l} after the tau insertions; |B| <= j_r + 2(r - 1) <= 3h - 3, so
  (0, d) has length at most 6h - 5. Conjugating by c^i adds 2(3h - 2), giving 12h - 9 for every
  transposition. Correct.
- Lemma 3.1 (comparison): Dir_P = (1/20) sum_s D_s over the five moves with holding 1/2, Dir_Q = (1/(4M)) sum_u
  D_u over the M transpositions; each D_u <= l^2 sum_s D_s by Cauchy-Schwarz along a word of length l <= 12h,
  with each generator used at most l times per word; this gives Dir_Q <= A Dir_P with A = 5 L^2 = 720 h^2.
  Correct (the constant is not sharp, nothing depends on that).
- Eigenvalues: the half-lazy random transposition walk has eigenvalues 1/2 + r_lambda/2 with r_lambda the
  character ratio; the bound (1 - r_lambda)/2 >= j/(2(n - 1)) for lambda_1 = n - j and the multiplicity bound
  C(n, j)^2 j! <= n^{2j} both check. Min-max gives beta_k >= mu_k / A. The chi-square sum and the
  Cauchy-Schwarz passage to total variation give the stated t_mix(eps) <= ceil(720 h^2 (n - 1)[2 log n +
  log(1 + 1/(4 eps^2))]). Correct.
- Diameter of order n log n: upper bound from 12h - 9 times the n - 1 transpositions needed; lower bound from
  the ball count. Correct.
- Proposition 1.2 (lower bound, every added pi): the ball of radius r in the Cayley graph with at most five
  generators (inverse-closed, so each step has at most four non-backtracking continuations) has at most
  (5 * 4^r - 2)/3 elements; with R = log_4(n!), t = floor((2 - delta) R) and K_t ~ Bin(t, 1/2), Chebyshev gives
  P(K_t > r) -> 0 for r = floor((1 - delta/4) R), and the ball is o(n!), so TV -> 1. Uniform in pi. Correct.
- Corollary 1.3 follows from the two bounds.

Computer claims, reproduced by a script written from the paper's text only (e94check.py / e94check.out in
this folder, not the repo's code):
- Words (Lemmas 2.1-2.2): for every odd n from 5 to 301, every c^i word has length at most 3h - 2 and evaluates
  to c^i, and every (i, i + d) word has length at most 12h - 9; the transposition words were evaluated as
  permutations for all i when n <= 61 and for six values of i per n above that, all correct. Longest
  transposition word: 17 (n = 5, bound 27), 27 (n = 9, bound 39), 69 (n = 101, bound 75), 87 (n = 301, bound 99).
- Small-deck table (exact distributions, half-lazy, right multiplication): n = 5: base 29 / 92, P_T 13 / 44;
  n = 7: 103 / 281, 42 / 113; n = 9: 254 / 633, 74 / 171 (TV <= 1/4 / TV <= 1/100). Identical to the table.
- n = 5, all 120 added permutations: smallest time to TV <= 1/4 is 9, attained by 14 permutations, including
  (1,2,4,0,3); the doubling map gives 13. Identical to the text.

Remark (no change required): the paper says plainly that the order h^2 n log n is probably not sharp and that
the best added permutation for large n is unknown; both are fair statements of what is open.
