# Referee pass: Mixing of the Aldous-Fill crossover chain via random switching networks

Paper: github.com/yspennstate/crossover-chain-mixing (commit 2af7ef8), Zenodo doi:10.5281/zenodo.24257131.
Problem: P0251 = Aldous-Fill Open Problem 12.5. Referee: agent A, 16 Nov 2026.

## Verdict
The argument is correct as far as I can check it line by line. One citation detail needs the full Czumaj paper
before anyone relies on the theorem numbers. No change to the statements is needed.

## Checked step by step (each re-derived, not read)
- (1.x) conj identity P_M Q_sigma = Q_sigma P_{sigma(M)}, and its use as Q_theta P_N = P_{theta^{-1}N} Q_theta:
  correct; theta_k = sigma_k o theta_{k-1} matches Q_{sigma_1}Q_{sigma_2} = Q_{sigma_2 o sigma_1}.
- Lemma 2.1: M_k = theta_{k-1}^{-1}(N_k) is uniform and independent of pi_1..pi_{k-1}, so the M_k are i.i.d.
  uniform; columns independent given the permutations; product TV <= sum TV. Correct, both versions.
- Section 2.2: TV(delta P_{M'} ..., u) handled by u P = u; the product of block Dobrushin coefficients; the
  expectation of the product factors by block independence, separately for each l (s = m_l fixed per l), so
  d(t) <= L rho^{floor(t/T)}. Correct.
- Lemma 2.2(b): any omega reaches omega* by at most min(s, K-s) <= K-1 transpositions, one per round of the
  1-factorization; positive probability; rows overlap. Correct (K=2 gives depth 1, fine).
- Proof of Theorem 1.1, small K: needs t >= T for (2.4); t >= C(log K + log(L/eps)) >= C log 2 covers it once C
  is large. Correct.
- Theorem 1.2(a): E_U(L'-N) <= C(L',2)/K <= L'/2 needs L' <= K, which holds; Markov gives 4/7; 3/7 > 1/e. Correct.
- Theorem 1.2(b): |p - q| >= 1/(C(K,2) 2^{tK/2}) because a*C(K,2) - 2^{tK/2} is a nonzero integer (K-1 odd >= 3);
  Chebyshev both sides; 2/(L Delta^2) = K^2(K-1)^2 2^{tK}/(2L). The constant matches the statement. Correct.
- Remark 2.3: right; the annealed law of one 1 in one column is near uniform after O(1) steps (stay w.p. 1/2, else
  a uniform other position), while the 2^t support bound in (a) is quenched and needs many shared columns.

## Points for the author
1. Citation numbers in Czumaj STOC 2015 (doi 10.1145/2746539.2746629). Checked 16 Nov from a seminar deck of the
   paper (kam.mff.cuni.cz/~dsemweb/1516/Random-Permutations-using-Switching-Networks.pdf): Proposition 2.3 ("all
   but a 1/n^2 fraction ... of logarithmic depth are good") and Theorem 3.4 (good network, depth >= c log n,
   k-partial n-permutations almost uniform) match the paper's use. NOT CONFIRMED: Theorem 3.7 (the deck lists 3.6
   as an explicit network for (1-eps)n elements and 3.8 as an explicit O(log^2 n) construction; 3.7 is not shown),
   Theorem 3.5, and footnotes 2 and 3 (polynomial rates for every fixed exponent). The proof does not depend on
   3.7, because fact (ii) is also derived from 3.4 in the next paragraph; but 3.4's hypothesis k >= alpha n and the
   "every fixed exponent" claim should be read off the full paper (WRAP 69874 holds the accepted version). If 3.7
   is not the 0-1 statement, cite (ii) to 3.4 alone.
2. Depth in fact (i). Lemma 2.2(a) needs the same depth T_K = ceil(c_0 log K) to be both "logarithmic" for
   Proposition 2.3 and >= c log n for (ii). One sentence saying that Proposition 2.3 holds at every depth
   c' log n with c' at least Czumaj's constant (or for the chosen c_0) closes this.
3. Optional strengthening for L = 1. A lower bound of order log K at L = 1 is within reach: start with s = K/2 ones
   in positions A = {1..K/2}; the mean of Z = #ones in A minus K/4 contracts by lambda = (K-2)/(2(K-1)) per step
   (E omega'_i = omega_i/2 + (s - omega_i)/(2(K-1))), while its standard deviation under u_s is about sqrt(K)/4, so
   a Wilson-type second-moment argument should give (1/2)log_2 K - O(1). That would make the bound tight at L = 1
   for every K, which Remark 2.3 now leaves open. Not needed for the paper's claims.
4. Small text items: the DS81 sentence appears twice in the introduction (end of paragraph 3 and end of the
   paragraph after Theorem 1.2); keep one. Nothing in the body narrates the writing process.

## Not checked
The full text of Czumaj's paper (only the abstract on WRAP and the seminar deck were read). No numerics run;
none are needed for these proofs.

## Prior art
One web search on 16 Nov (crossover / random pairing / uniform crossover / Aldous-Fill) found no earlier answer to Open Problem 12.5; it surfaced the answer to 4.17 (arXiv:1508.04836, a different problem) and GA mixing studies (Rabani-Rabinovich-Sinclair line, already cited). Aldous's own open-problems page (stat.berkeley.edu/~aldous/Research/OP/) was not read.

## Addendum (16 Nov 00:4x): the L = 1 remark and a lower bound in K for every L >= 2
Read against paper/main.tex at the clone of 16 Nov (definition in par. 1, Remark after Theorem 1.1, Theorem 1.2).

5. Remark 2.3 should separate the two versions. In the original chain the new words get the labels 2i-1, 2i of the
   pair {pi(2i-1), pi(2i)}, so for L = 1 one step maps the column x to x o pi o tau, where tau is the product of the
   coin transpositions (2i-1 2i). pi o tau is a uniform permutation, so the column has law u_s after ONE step, for
   every K and s: there is no lower bound of order log K at L = 1 for this version. For the labeled variant the column
   is x P_{N_1} ... P_{N_t} with i.i.d. uniform matchings, and order log K is the truth (point 6).

6. Proposition (suggested). Let K >= 8 be even (smaller K only change the constant). (a) Labeled variant, any L >= 1, and (b) original chain, any L >= 2:
   tau(eps) >= (1/2) log_2 K - C(eps), with C(eps) = (1/2) log_2(C/eps) for an absolute C.
   Proof sketch. lambda = (K-2)/(2(K-1)).
   (a) Start column 1 with ones on A = {1..K/2}; Z = (#ones of column 1 in A) - K/4. For a uniform matching and fair
   coins, E[omega'_i | omega] = omega_i/2 + (s - omega_i)/(2(K-1)), and summing over A with s = K/2 gives
   E[Z' | omega] = lambda Z exactly, so E Z_t = lambda^t K/4.
   (b) Start columns 1 and 2 both with ones on A. W = #{k : x^k_1 = x^k_2 = 1} is invariant under the relabeling
   Q_theta, so it evolves as in the labeled variant with the two columns sharing matchings and having independent
   coins. Per pair {i,j}: E[a'_i b'_i + a'_j b'_j] = (a_i b_i + a_j b_j)/2 + (a_i b_j + a_j b_i)/2, and averaging over the
   matching gives E[W' | x] = W/2 + (s_1 s_2 - W)/(2(K-1)); with Y = W - s_1 s_2/K this is E[Y' | x] = lambda Y, and
   Y_0 = K/4.
   Variance (both cases). Given the matching, pairs are independent with contributions bounded by 2, so
   E[Var(. | M)] <= K/2. The conditional mean is the old value times 1/2 plus (1/2) sum_k f_k g(m(k)) with f, g in
   [0,1] and m the partner map; for a uniform perfect matching Cov(g(m(k)), g(m(k'))) = O(1/K) for k != k' (condition
   on whether k and k' are matched to each other), so Var_M = O(K). Hence Var(Z_{t+1}) <= lambda^2 Var(Z_t) + cK, so
   Var(Z_t) <= 2cK for all t, and the same for Y. Under the stationary law both statistics are centred hypergeometric
   (overlap of two uniform K/2-sets) with variance about K/16.
   Chebyshev at a = lambda^t K/8 on both laws gives TV >= 1 - C/(lambda^{2t} K). Since 2 lambda = 1 - 1/(K-1), for
   2t <= log_2 K <= (K-1)/2 (true for K >= 8) one has lambda^{2t} K >= 4^{-t} K/2, so t = (1/2)log_2 K - m gives TV >= 1 - C' 4^{-m}.
   Consequence: with Theorem 1.1 and Theorem 1.2(a), tau = Theta(log K + log L) whenever 2 <= L <= K (both versions),
   and Theta(log K) at L = 1 in the labeled variant. Theorem 1.2(a) gives log_2 min(K,L) - 3, which is O(1) for fixed L;
   this closes that case in K. For L > K the log L part remains as in 1.2(b) (fixed K only).
   Numerical check (K = 1024, 2000 runs, scripts p0251_l1_check.py / p0251_l2_check.py in this folder):
   labeled L=1: mean Z 128.2, 64.2, 31.9, 16.4, 8.2 at t=1..5 against lambda^t K/4 = 127.9, 63.9, 31.9, 15.9, 8.0;
   Var Z 96 -> 62 (K/16 = 64); TV of the A-count >= 0.95, 0.68, 0.39 at t = 3, 4, 5 ((1/2)log_2 K = 5).
   original L=1: TV at the sampling-noise floor (0.05-0.06) from t = 1, as point 5 says.
   original L=2, identical columns: mean Y 127.9, 64.0, 32.2, 15.9, 7.8 at t = 1..5 (same predictions); Var Y 101 -> 61;
   TV of W >= 0.95, 0.67, 0.38 at t = 3, 4, 5.
   Status: second audit 16 Nov 00:5x supplies the constant below.

7. The covariance constant (second audit). For a uniform perfect matching with partner map m, g in [0,1]^K, k != k',
   G = sum g, H = G - g_k - g_k', Q = sum over a not in {k,k'} of g_a^2:
   E g(m(k)) = (G - g_k)/(K-1),  E[g(m(k)) g(m(k'))] = g_k g_k'/(K-1) + (H^2 - Q)/((K-1)(K-3)).
   (Formula equals brute force over all 105 matchings at K = 8: -0.0137778 both.) Expanding,
   Cov = 2H^2/((K-1)^2(K-3)) - Q/((K-1)(K-3)) - H(g_k+g_k')/(K-1)^2 + g_k g_k'(K-2)/(K-1)^2.
   Upper: Q >= H^2/(K-2) gives the first two terms <= H^2/((K-1)^2(K-2)) < 1/(K-1); so Cov < 2/(K-1).
   Lower: Q <= H gives Cov >= -(K-2)/((K-1)(K-3)) - 2(K-2)/(K-1)^2 >= -3/(K-3). So |Cov| <= 3/(K-3).
   Numerically the worst case over 0/1 vectors and 2000 random vectors is (0.61 .. 0.9985)/(K-3) for K = 8 .. 2048
   (p0251_cov_check.py). Both statistics are of the form const + (1/2) sum_k f_k g(m(k)) with f, g 0/1-valued
   (for Z write 1[m(i) in B] = 1 - 1[m(i) in A] for i in A, so g = 1_A for every term; for W, f = a, g = b).
   Hence Var_M <= (1/4)(K/4 + 3K(K-1)/(K-3)) <= 1.12 K for K >= 8, and with the pair term (K/8 for Z, K/2 for W)
   the one-step conditional variance is <= 1.25 K (Z) and <= 1.62 K (W). Since lambda <= 1/2,
   Var Z_t <= (4/3)(1.25 K) <= 1.67 K and Var Y_t <= 2.16 K; the stationary hypergeometric variances are <= K/14.
   Chebyshev at half the mean: TV >= 1 - 64(2.23 K)/(lambda^{2t} K^2) >= 1 - 286 * 4^{-m} at t = (1/2)log_2 K - m.
   So t_mix(1/4) >= (1/2) log_2 K - 5 for every even K >= 8, in both cases of point 6. The simulated variances
   (60-100 at K = 1024) sit far inside these bounds.
