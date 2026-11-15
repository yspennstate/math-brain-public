# Referee report: Adding one permutation to a transposition and a long cycle

Paper: yspennstate/one-generator-shuffle at 7748293 (paper/main.tex, 321 lines). Referee: an agent, 14 Nov 2026.
Answers Diaconis, Bernoulli 19 (2013), Question 3, for the generating set {(1,2), (1,...,n)} with n odd.

## Verdict

SOUND. No change to the paper is needed. Every proof was checked step by step, and every number in Section 5 and
the word lengths quoted there were recomputed with code written without reading the repository's code.

## Proofs checked

- Distinctness of the five moves (sigma fixes 0, sigma(1) = 2, sigma^2 = id forces n | 3). Correct.
- Lemma 2.1. sigma c^q sigma^{-1} = c^{2q}, so each binary digit after the leading one adds at most 3 letters;
  i < n <= 2^h gives at most h digits. Correct.
- Lemma 2.2. A_l(0) = a_l, A_l(1) = a_{l+1}, so A_l tau A_l^{-1} = (a_l, a_{l+1}); the path identity
  e_1...e_{r-1} e_r e_{r-1}...e_1 = (a_1, a_{r+1}); A_l^{-1} A_{l+1} = sigma^{-j} c^{2^j} sigma^{j'} = c sigma^{j'-j}
  (from c^{2^j} = sigma^j c sigma^{-j}); |B| = j_r + 2(r-1) <= 3 j_r <= 3h-3; conjugation by c^i. Correct.
- Diameter: (12h-9)(n-1) above, the ball count below. Correct.
- Lemma 3.1. Both Dirichlet forms are normalised correctly (1/20 and 1/(4M)); Cauchy-Schwarz along the word, the
  bijection g -> g_{k-1}, each letter used at most l <= L times, so E_Q <= 5 L^2 E_P = 720 h^2 E_P. Correct.
- Spectrum. Half-lazy, so eigenvalues in [0,1]; min-max gives beta_k >= mu_k / A. The character ratio
  (sum lambda_i^2 - sum lambda'_i^2)/(n(n-1)) is the standard formula; (3.1) gives (1 - r)/2 >= j/(2(n-1)); the
  tableau injection gives d_lambda <= C(n,j) d_{bar lambda}, hence (3.2) <= C(n,j)^2 j! <= n^{2j}. Correct.
- Theorem 1.1. chi^2 = tr P^{2t} - 1 for a symmetric walk on a group; the threshold makes x <= 4 eps^2/(1+4 eps^2),
  so the geometric sum is <= 4 eps^2 and TV <= eps. The remark's n^2 log^3 n for the gap-only route checks. Correct.
- Proposition 1.2. Non-backtracking words: at most 5 first letters and 4 after (the set is closed under inverses,
  so exactly one letter is excluded), ball <= (5 4^r - 2)/3. Chebyshev with mean <= (1 - delta/2)R, variance <= R/2,
  deviation >= delta R/4 - 1; U(B(r)) <= (5/3) 4^{-delta R/4}. Correct, uniformly in pi.
- Corollary 1.3 follows; log n! = (1 + o(1)) n log n.

## Numbers recomputed (agent_run/ogs_check.py, ogs_words.py; outputs copied here)

- Section 5 table, exact distributions on S_5, S_7, S_9 (9! states): base 29/103/254 at 1/4 and 92/281/633 at
  1/100; P_T 13/42/74 and 44/113/171. All twelve entries as printed.
- n = 5, all 120 added permutations: best time to 1/4 is 9, attained by 14 permutations, (1,2,4,0,3) among them;
  doubling gives 13. As printed.
- Words built exactly as in the proofs and evaluated for every odd n from 5 to 301: no failure; every c^i word
  <= 3h-2, every (0,d) word <= 6h-5. Longest transposition word 17 at n = 5 (bound 27) and 69 at n = 101 (bound 75),
  as printed.

## Citations checked

- Wilson, arXiv math/0210469: the symmetrized Rudvalis shuffle moves shift-left, shift-right, swap of the top two,
  or holds, each with probability 1/4, and Theorem 1 gives the order n^3 log n bounds. The paper's base walk has the
  same three moves with holding probability 1/2, a constant time change, so the citation is accurate.
- Diaconis, arXiv 1309.7754, Question 3: worded as the paper states it (S_n, n odd, a transposition and an n-cycle,
  "is there a choice ... that appreciably speeds this up").
- A web search for an earlier answer to Question 3 found none (14 Nov 2026).

## Remarks (no change requested)

- The upper bound is a mixing-time order; the lower bound is the counting bound. The log^2 n gap is stated plainly
  in Section 6, together with the observation for n = 5 that doubling is not the best added permutation.
- Funding paragraph follows the author's standing rule; no NSF grant named.
