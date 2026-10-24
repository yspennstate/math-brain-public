# Second reading of F5's proof that threshold functions satisfy FEI (24 September, 18:5x)

Object: proofnet24/P03-fei/continuations/2026-09-22-opus-team/F5-monotone/REPORT.md, Theorem 1:
every f = sgn(w.x - theta) has H(f) <= 14.2141880860 I(f). The W2-A referee had checked every lemma numerically
(all ratios below 1) but was stopped before a written reading. This is a written reading, done independently of W2-A
and of F5's code. Verdict: the proof is correct as written; no gap found. Details per step:

- Lemma 1 (Erdos-Littlewood-Offord). Comparable sign vectors give sums at least 2 beta apart; two points of a
  half-open interval of length 2 beta are less than 2 beta apart; Sperner. The estimate
  C(m, floor(m/2)) 2^-m <= sqrt(2/(pi m)) reduces for odd m = 2r+1 to 4r^2 + 2r - 1 >= 0 (checked).
- Lemma 2. The slab: for w_i > 0, f(y^{i->1}) != f(y^{i->-1}) iff theta - w_i < L(y) <= theta + w_i with the
  convention sgn(0) = -1; the same interval for w_i < 0. The flip realisation xi_j = eta_j (1 + eps_j)/2 has
  Pr[xi_j = 1] = c/(2N) and gives y_j = -x_j eps_j on R, so L(y) is a constant minus a Rademacher sum with
  coefficients |w_j| >= |w_i| (j in U_i). min(1, sqrt(2/(pi m))) <= (2/sqrt pi)(m+1)^{-1/2} for all m >= 0.
  m ~ Bin(N-1, c/N) and E[1/(m+1)] = (1 - (1 - c/N)^N)/c <= 1/c; Jensen for the square root. Correct.
- Lemma 3. c = N/(3K) needs K >= 1/3; (1 - 1/(3K))^{-K} <= 3/2 for K >= 1 because -K ln(1 - 1/(3K)) =
  sum_m 3^-m K^{1-m}/m is nonincreasing; (3/2)(2/sqrt pi) sqrt 3 = 3 sqrt(3/pi) = B. Layer cake on [0, ln N] with
  K = N e^-u >= 1; the integral of min(1, B e^{-u/2}) is 2 ln B + 2 = L1 = 4.15111. Correct.
- Lemma 4. |T cap U_i| + 1 <= |S| and N_i >= r(i); the log is nonnegative since |T cap U_i| <= N_i - 1. Correct.
- Lemma 5 (OWZ). The decomposition of H(|S|), H(K) <= E K on {1,2,...} (cross-entropy with Geometric(1/2)),
  (1 - eps) log(1/(1 - eps)) <= eps log2 e <= 2 eps, and the scalar inequality
  (1 - sqrt(1 - eps)) log2(2/(1 - sqrt(1 - eps))) >= (1/2) eps log2(1/eps) + eps. With u = 1 - sqrt(1 - eps) the
  difference of the two sides divided by u is (u/2) log2(1/u) - 1 + u + (1 - u/2) log2(2 - u): it is 0 at u = 0 and
  u = 1, about (u/2)(log2(1/u) - 0.443) near 0, about 0.443 (1 - u) near 1, and positive in between (0.031, 0.146,
  0.189, 0.044, 0.0044 at u = 0.01, 0.1, 0.5, 0.9, 0.99). W2-B reports a two-line concavity proof. Correct.
- Lemma 6. pi_k is a probability on k-sets; Gibbs; e_k(q) <= (sum q)^k/k!; sum_s q_k(s) <= k a/(a - 1);
  k! >= (k/e)^k. Correct for every random set S and every ordering.
- Theorem 1. Chain rule H = H(|S|) + H(S given |S|); optimum a(a - 1) = 1/L1, a = 1.20064, value 14.2142 (recomputed).

What it gives for the monotone problem: every monotone threshold function (weighted majority with nonnegative
weights and any threshold) satisfies FEI with 14.22; with W2-B, every Boolean function of k halfspaces with O(log k).
These have unbounded width and unbounded read, so they are not covered by the width theorem, and the clique property
is not covered by them (for the clique property no ordering has Sigma_r = O(I): the spectral sample is spread over a
random clique). Its mechanism (derivatives localised on the heavier coordinates, then a rank-weighted reference
measure) and the vertex coding (a hierarchy on the vertices, then an arbitrary edge set inside) are two instances of
one scheme: a reference measure adapted to where the spectral sample lives.

Context found afterwards: the regular-function theorem of continuation 2026-09-23-readk-dnf (constant 15.1) already
covers every threshold function, since a threshold function is regular (its coordinates are totally preordered by
desirability, through |w|). F5's argument is a second, independent proof with a slightly better constant.
