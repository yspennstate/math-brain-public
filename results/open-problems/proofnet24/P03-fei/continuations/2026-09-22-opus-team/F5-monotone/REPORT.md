# The Fourier entropy-influence inequality for linear threshold functions

Group F5, 22-23 September 2026.

Status of each claim:

- Proved: every linear threshold function f satisfies H(f) <= 14.22 I(f) (Theorem 1). The same proof gives the inequality with constant O(log k) for every Boolean function of k threshold functions whose weight vectors induce a common order (Corollary 2). The proofs are analytic and complete. They use the Erdős-Littlewood-Offord inequality, the level-entropy lemma of O'Donnell, Wright and Zhou (which rests on the edge-isoperimetric inequality) and elementary estimates. `code/constants_thm1.py` evaluates the constant to 20 digits.
- Numerical: the supremum of H/I over linear threshold functions appears to be 4 and is not attained. AND_n gives 4(1 - 1/n) + o(1). AND/OR chains (lexicographic threshold functions) approach 4 from below faster (3.99225 at n = 22). Annealing over integer weights at n = 10 and 12, and every integer weight vector with entries <= 6 (n <= 6) or <= 5 (n = 7), find no threshold function above the best chain of the same length.
- Conjectural: the sharp constant of the class is 4.
- Tested: every lemma was also tested numerically, including searches built to violate it. The largest ratios of left side to bound are 0.77 (Lemma 2, exact pointwise enumeration), 0.33 (Lemma 3), 0.12 (Lemma 4) and 0.84 (Lemma 5).
- Not proved: the sharp constant, and a bound for the restriction step at the heaviest coordinate (observed <= 4.8723, Section 4.3), which the proof does not use.

## 0. Notation

f: {-1,1}^n -> {-1,1}, f = sum_S fhat(S) chi_S. The spectral sample is the random set S with Pr[S = A] = fhat(A)^2, so that H(f) = H(S) (Shannon entropy in bits), I(f) = E|S| and Pr[i in S] = Inf_i(f). Here log = log2 and ln is the natural logarithm.

A linear threshold function (LTF) is f(x) = sgn(w.x - theta) with w in R^n and theta in R, where sgn(t) = 1 for t > 0 and -1 for t <= 0 (every threshold function has such a representation). D_i f(x) = (f(x^{i->1}) - f(x^{i->-1}))/2 is a function of x_{-i} with values in {0, 1, -1}. Its Fourier coefficients are fhat(T+i) for T not containing i, and E(D_i f)^2 = E|D_i f| = Inf_i(f).

Order the coordinates by decreasing |w_j|, with ties broken arbitrarily, and let r(i) be the position of i. For each i put

    U_i = { j != i : |w_j| >= |w_i| },      N_i = |U_i| + 1.

Every j with r(j) < r(i) lies in U_i, so N_i >= r(i).

## 1. Results

Theorem 1. For every linear threshold function f,

    H(f) <= C I(f),    C = 3 + min_{a>1} [1 + ln(a/(a-1)) + a L1] / ln 2 = 14.2141880860...,

where L1 = 2 ln B + 2 = 4.1511069801... and B = 3 sqrt(3/pi) = 2.9316150714... . The minimum is attained at a = (1 + sqrt(1 + 4/L1))/2 = 1.2006422748... .

Corollary 2. Let f_l = sgn(w^(l).x - theta_l), l = 1..k, be threshold functions whose weight vectors are co-monotone: one ordering of [n] makes |w^(l)_j| nonincreasing for every l. Then for every F: {-1,1}^k -> {-1,1}, the function f = F(f_1, ..., f_k) satisfies H(f) <= C_k I(f), with

    C_k = 3 + min_{a>1} [1 + ln(a/(a-1)) + a (L1 + 2 ln k)] / ln 2.

Numerically C_1 = 14.214, C_2 = 16.567, C_3 = 17.909, C_4 = 18.850, C_16 = 23.287 and C_100 = 29.003. In particular, f = G(w.x) with G changing sign at most k times satisfies H(f) <= C_k I(f).

AND_n is a threshold function with H/I -> 4, so the best constant for the class lies in [4, 14.22].

## 2. Proofs

Lemma 1 (Erdős 1945). Let b_1, ..., b_m be reals with |b_j| >= beta > 0, and let eps be uniform on {-1,1}^m. For every half-open interval J of length 2 beta,

    Pr[ sum_j b_j eps_j in J ] <= C(m, floor(m/2)) 2^{-m} <= sqrt(2/(pi m))     (m >= 1).

Proof. Replacing eps_j by sgn(b_j) eps_j, we may assume every b_j > 0. If eps <= eps' coordinatewise and eps != eps', the two sums differ by at least 2 beta, while two points of J differ by less than 2 beta. So the sign vectors whose sum lies in J form an antichain, and Sperner's theorem bounds their number by C(m, floor(m/2)). For the second inequality, the even case is Wallis' bound C(2r,r) 4^{-r} <= (pi r)^{-1/2}. For m = 2r+1 >= 3, C(2r+1,r) 2^{-2r-1} = C(2r,r) 4^{-r} (2r+1)/(2r+2), so the claim reduces to (2r+1)^3 <= 2r(2r+2)^2, that is, 4r^2 + 2r - 1 >= 0. The case m = 1 reads 1/2 <= sqrt(2/pi). []

Lemma 2 (partial noise sensitivity of a derivative). Let f = sgn(w.x - theta) with w_i != 0, g = D_i f, U = U_i and N = N_i >= 2. For 0 < c <= N and rho = 1 - c/N,

    Stab^U_rho[g] := sum_T ghat(T)^2 rho^{|T cap U|} <= (2/sqrt(pi)) c^{-1/2} Inf_i(f).

Proof. Let x be uniform, and obtain y from x by flipping each coordinate of U independently with probability (1-rho)/2 = c/(2N), leaving the other coordinates unchanged. Then E[chi_T(x) chi_T'(y)] = [T = T'] rho^{|T cap U|}, so Stab^U_rho[g] = E[g(x) g(y)] <= E[|g(x)| Pr[g(y) != 0 | x]], and E|g| = Inf_i(f). It is enough to show Pr[g(y) != 0 | x] <= (2/sqrt(pi)) c^{-1/2} for every x.

Write L(z) = sum_{j != i} w_j z_j. Then g(y) != 0 exactly when L(y) lies in J = (theta - |w_i|, theta + |w_i|], of length 2|w_i|. Realise the flip indicators as xi_j = eta_j (1 + eps_j)/2, where eta_j ~ Bernoulli(c/N) and eps_j is uniform on {-1,1}, all independent of each other and of x (this needs c <= N). Given x and R = {j in U : eta_j = 1}, with m = |R|,

    L(y) = [ L(x) - sum_{j in R} w_j x_j ] - sum_{j in R} w_j x_j eps_j.

This is a constant minus a Rademacher sum whose coefficients satisfy |w_j x_j| = |w_j| >= |w_i|. Lemma 1 with beta = |w_i| gives Pr[L(y) in J | x, R] <= min(1, sqrt(2/(pi m))) <= (2/sqrt(pi)) (m+1)^{-1/2}. For m >= 1 the last step is 2(m+1) <= 4m; for m = 0 it is 1 <= 2/sqrt(pi). The size m is Binomial(N-1, c/N), independent of x, with E[1/(m+1)] = (1 - (1 - c/N)^N)/c <= 1/c. Jensen's inequality gives E[(m+1)^{-1/2}] <= c^{-1/2}. []

Lemma 3. For every i with Inf_i(f) > 0,

    sum_{T not containing i} fhat(T+i)^2 ln( N_i / (|T cap U_i| + 1) ) <= L1 Inf_i(f).

Proof. If N_i = 1, every term is 0. Otherwise let nu(T) = fhat(T+i)^2 / Inf_i(f), k(T) = |T cap U_i| in [0, N-1], and N = N_i. For real K >= 1, Lemma 2 with c = N/(3K) (so rho = 1 - 1/(3K)) gives

    nu(k <= K) <= rho^{-K} sum_T nu(T) rho^{k(T)} <= (1 - 1/(3K))^{-K} (2/sqrt(pi)) (3K/N)^{1/2} <= B (K/N)^{1/2}.

The last step holds because -K ln(1 - 1/(3K)) = sum_{m>=1} 3^{-m} K^{1-m}/m is nonincreasing in K and equals ln(3/2) at K = 1. Since ln(N/(k+1)) >= 0,

    E_nu ln(N/(k+1)) = int_0^{ln N} nu(k + 1 < N e^{-u}) du <= int_0^inf min(1, B e^{-u/2}) du = 2 ln B + 2,

using K = N e^{-u} >= 1 on the range of integration and B >= 1. []

Lemma 4 (rank bound). Sigma(f) := E_S[ sum_{i in S} ln+( r(i)/|S| ) ] <= L1 I(f), where ln+ = max(ln, 0).

Proof. Let i be in S and T = S \ {i}. Then |T cap U_i| + 1 <= |S| and N_i >= r(i), so ln(N_i/(|T cap U_i| + 1)) >= ln+(r(i)/|S|); the left side is nonnegative. Summing over pairs (i, S) with weights fhat(S)^2 and applying Lemma 3 to each i gives Sigma(f) <= L1 sum_i Inf_i(f) = L1 I(f). []

Lemma 5 (O'Donnell, Wright and Zhou 2011, Theorem 5). For every Boolean f, H(|S|) <= 3 I(f).

Proof (as in the source). Let eps = 1 - fhat(empty)^2. Then H(|S|) = (1-eps) log(1/(1-eps)) + eps log(1/eps) + eps H(|S| given |S| >= 1). A variable K on {1, 2, ...} has H(K) <= E K (the divergence from Geometric(1/2) is nonnegative), so the last term is at most I. Also (1-eps) log(1/(1-eps)) <= 2 eps. Finally, the edge-isoperimetric inequality gives I >= (1 - sqrt(1-eps)) log(2/(1 - sqrt(1-eps))) >= (1/2) eps log(1/eps) + eps on (0,1]; the last step is an elementary inequality, checked on a grid of 220,000 points in `code/scalar_checks.py`. []

Lemma 6 (rank-weighted entropy). For every random set S in [n], every bijection r: [n] -> {1..n} and every a > 1,

    H(S given |S|) <= (1/ln 2) [ ln(e a/(a-1)) E|S| + a E sum_{i in S} ln+( r(i)/|S| ) ].

Proof. For k >= 1 put q_k(s) = min(1, (k/s)^a), and on k-sets let pi_k(A) = prod_{i in A} q_k(r(i)) / Z_k, where Z_k = e_k(q_k(1), ..., q_k(n)). By Gibbs' inequality, H(S given |S| = k) <= E[ln(1/pi_k(S)) given |S| = k] / ln 2, and ln(1/pi_k(S)) = ln Z_k + a sum_{i in S} ln+(r(i)/k). Now Z_k <= (sum_s q_k(s))^k / k!, sum_s q_k(s) <= k + k^a int_k^inf s^{-a} ds = k a/(a-1), and k! >= (k/e)^k, so ln Z_k <= k ln(e a/(a-1)). Averaging over k proves the claim. []

Proof of Theorem 1. By the chain rule, then Lemmas 5, 6 and 4,

    H(f) = H(|S|) + H(S given |S|) <= 3 I + (1/ln 2)[ ln(e a/(a-1)) I + a Sigma(f) ] <= [3 + (1 + ln(a/(a-1)) + a L1)/ln 2] I.

The bracket is smallest at a(a-1) = 1/L1, where it equals 14.2141880860... . []

Proof of Corollary 2. Only Lemma 2 changes. Take U_i = {j != i : |w^(l)_j| >= |w^(l)_i| for every l}; it contains every coordinate that precedes i in the common order. If D_i f(y) != 0, then some D_i f_l(y) != 0, so L^(l)(y) lies in a half-open interval of length 2|w^(l)_i|, with Littlewood-Offord coefficients |w^(l)_j| >= |w^(l)_i| on U_i. The union bound gives the conditional probability <= min(1, k sqrt(2/(pi m))) <= k (2/sqrt(pi)) (m+1)^{-1/2}. So B becomes kB and L1 becomes L1 + 2 ln k. For G(w.x) with k sign changes, take w^(l) = w for every l. []

## 3. Remarks

1. What the proof uses. Suppose some ordering of the coordinates and some kappa >= 1 have the following property. For every i there is a set U_i, containing all coordinates before i, such that for every assignment z to the coordinates outside U_i and i, the set {y in {-1,1}^{U_i} : D_i f(z,y) != 0} is a union of at most kappa antichains (each for some orientation of the coordinates). Then H(f) <= C_kappa I(f). Restricting a union of kappa antichains to a subcube leaves a union of kappa antichains, which is all that Lemma 2 needs. Threshold functions have the property with kappa = 1, using U_i as above and the orientation sgn(w_j).

2. Lemmas 5 and 6 hold for every Boolean f and every ordering r. So H(f) <= 3I + [(1 + ln(a/(a-1))) I + a Sigma_r(f)]/ln 2 in general, and FEI holds on any class whose functions admit orderings with Sigma_r = O(I). Ordering by influence recovers the bound by the entropy of the influence distribution.

   The criterion is not necessary. Recursive ternary majority of depth d (n = 3^d) satisfies FEI, and its automorphism group is transitive on the leaves, so Sigma_r = (I/n) sum_{s=1}^n E_sb[ln+(s/|S|)] for every ordering, where E_sb is the size-biased law of |S|. The spectral sample is a Galton-Watson tree with offspring 1 (probability 3/4) or 3 (probability 1/4), so E_sb|S| <= 2(3/2)^d. By Jensen's inequality and (n!)^{1/n} >= n/e, Sigma_r/I >= d ln 2 - 1 - ln 2 -> infinity. The argument therefore gives nothing for general functions.

3. The constant breaks down as 3 from Lemma 5, about 4.0 from normalising the reference measure, and 7.2 from a L1/ln 2. A reference measure that follows the rank order of S's elements lowers the constant to about 13.3 in numerical estimates of its partition function; this was not made rigorous.

4. The proof never restricts or composes. It is independent of the read-once gate potentials and bears on neither the lower bound 6.52 nor full FEI.

## 4. Numerics of the class

### 4.1 Largest H/I

| family | n | H/I |
|---|---|---|
| majority | 17 / 23 | 2.3989 / 2.4876 |
| symmetric thresholds, best over k (k = 1 is AND) | 100 / 200 / 400 | 3.96 / 3.98 / 3.99 |
| AND_n | 10 / 16 / 22 | 3.88418 / 3.93027 / 3.94933 |
| best AND/OR chain | 10 / 12 / 16 / 22 | 3.93519 / 3.96225 / 3.98474 / 3.99225 |
| weights i^{-1/2}, theta = 0 | 12 / 24 | 2.3176 / 2.5296 |
| annealing over integer weights and all thresholds | 10 / 12 | 3.93519 / 3.96225 (the best chain) |
| every integer weight vector, entries <= 6 (n <= 6) or <= 5 (n = 7) | 3..7 | the best chain (AND_n for n <= 7) |

For symmetric thresholds at fixed k/n, H/I decreases in n (k/n = 0.1: 3.524, 3.497, 3.478 at n = 100, 200, 400). Majority increases slowly (2.758, 2.797, 2.824 at the same n). Exact values for symmetric thresholds come from a Krawtchouk formula checked against the Walsh transform (`code/symthresh.py`). Chains use the exact AND-composition formulas, checked against the Walsh transform at n = 6 (`code/chains.py`).

Conjecture. sup{ H/I : f a linear threshold function } = 4, the supremum is not attained, and for each n the maximum is attained by an AND/OR chain.

### 4.2 Why nothing here exceeds 4

For a rare event of density p, H = 4p(1-p)[log(1/(4p(1-p))) + H(q)] and I = 4p(1-p) E_q|S|, where q is the normalised nonempty spectrum. Edge isoperimetry gives log(1/p) <= 2(1-p) E_q|S|. So H/I > 4 roughly requires H(q) > 2 E_q|S|. The constructions that achieve this, Hod's biased compositions of lexicographic functions, are compositions that are not threshold functions.

### 4.3 Restriction step at the heaviest coordinate

At the coordinate of largest |w|, Delta_1 H = H(f) - (H(f_{1->1}) + H(f_{1->-1}))/2 stayed <= 4.8723 Inf_1 in every search (annealing at n = 12). The value is attained near AND_3, where it is 4.8677. For f = sgn(w.x) with w.x never 0, Delta_1 H = 0 exactly. The lightest coordinate can have much larger ratios (8.59 in a Gaussian-weight example at n = 16).

A structural fact found along the way: with M the slab where x_1 decides f, s = E_{x_1} f and D = D_1 f = 1_M, one has |D_j s| = |D_j D| pointwise for every j != 1, because no edge joins the two sides of the slab. Hence I(s) = I(D), H(f) = Ent(shat^2) + Ent(Dhat^2) and I(f) = 2 I(D) + Pr[M]. The identity I(s) = I(D) was checked numerically; the largest difference found was 0.0.

## 5. Tests of the proof

Ratios are left side divided by bound; each must be at most 1.

| test | worst ratio | log |
|---|---|---|
| Lemma 2, 400 random LTFs, n <= 15 | 0.696 | check_rank_final.log |
| Lemma 2, pointwise over every x, exact enumeration, 160 LTFs, n <= 8 | 0.768 | pointwise_lemma2.log |
| Lemma 2, annealing | 0.696 | adv_p1_final.log |
| Lemma 3, random / annealing | 0.218 / 0.230 | check_rank_final.log, adv_p2_final.log |
| Lemma 3, symmetric thresholds, exact, n <= 4001 | 0.328 | lemma3_symmetric_large_n.log |
| Lemma 4, random / annealing | 0.121 / 0.124 | check_rank_final.log, adv_sig_final.log |
| Lemma 5; Lemma 6 bound on H(S given abs S); Theorem 1 | 0.826; 0.375; 0.272 | check_rank_final.log |
| integer weights, exhaustive, n <= 7 (Lemmas 2, 3, 4, Theorem 1) | 0.696 / 0.200 / 0.110 / 0.268 | exhaust_small_final.log |
| structured LTFs, n = 18-22 (majority, AND, chains, power laws, heavy-light, Fibonacci, Gaussian) | Lemma 2 <= 0.677, Lemma 3 <= 0.256, Lemma 4 <= 0.147, Lemma 5 <= 0.766, Theorem 1 <= 0.277 | large_n_lemmas.log |
| Corollary 2, G(w.x) with 2 or 3 sign changes | 0.332 / 0.169 / 0.083 | check_corollary2.log |
| Corollary 2, AND, parity or majority of 2-3 co-monotone LTFs | 0.406 / 0.158 / 0.084 | check_corollary3.log |

## 6. Literature

Chakraborty, Kulkarni, Lokam and Saurabh (TCS 2016, ECCC TR13-052) prove H(f) = O(sqrt n) for every LTF. Chakraborty, Karmalkar, Kundu, Lokam and Saurabh (LATIN 2018, arXiv:1903.11635) prove FEI with high probability for LTFs with Gaussian or uniform weights, and for tau-regular LTFs with tau <= c/sqrt(n), the threshold included in the normalisation. They note that the min-entropy version for LTFs follows from KKL, list general LTFs as open, and ask for an entropy bound adapted to the skewness of the weights; Lemma 4 is such a bound. O'Donnell, Wright and Zhou (ICALP 2011) prove FEI for symmetric functions (C = 12.04), for d-part-symmetric functions (C = 12.04 + log2 d, which covers LTFs with d distinct weights) and for read-once decision trees (C = 4.88). Lemma 5 is their Theorem 5, and Lemma 3 adapts their derivative noise-sensitivity method, with Littlewood-Offord replacing unimodality of the Hamming weight. Erdős, Bull. AMS 51 (1945). The edge-isoperimetric inequality is due to Harper, Bernstein and Hart.

## 7. Files

- `code/ltf_core.py`: truth tables, Walsh transform, H, I and restriction steps.
- `code/constants_thm1.py`: the constants and the scalar facts (mpmath, 50 digits).
- `code/scalar_checks.py`: elementary inequalities checked on grids.
- `code/check_rank.py`: all lemmas on random LTFs.
- `code/adversarial_rank.py`: annealing searches against the lemmas.
- `code/exhaust_small.py`: exhaustive integer weights up to n = 7.
- `code/pointwise_lemma2.py`: exact pointwise check of Lemma 2.
- `code/lemma3_symmetric_large_n.py`: exact Lemma 3 for symmetric thresholds.
- `code/large_n_lemmas.py`: structured families, n = 18-22.
- `code/check_corollary2.py`, `code/check_corollary3.py`: tests of Corollary 2.
- `code/symthresh.py`, `code/chains.py`, `code/local_search.py`, `code/step_search.py`, `code/step_analysis.py`, `code/run_steps.py`, `code/powerlaw.py`, `code/seq_partition.py`: the numerics of Sections 3 and 4.
- `code/check_thmA.py`: an earlier dyadic-class variant of the argument (H <= (12.68 + log2 d) I), superseded by Theorem 1.
- `logs/`: all outputs. `logs/check_rank_random.log` and `logs/adv_p1.log` / `logs/adv_p2.log` come from a first variant (U_i with |w_j| >= |w_i|/2) and are superseded by the `*_final` logs.
