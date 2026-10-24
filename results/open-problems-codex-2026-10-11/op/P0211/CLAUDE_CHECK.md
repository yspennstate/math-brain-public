# P0211: third check (claude-322bc92e, 11 Oct 2026 23:1x)

Verdict: PASS on correctness. Novelty not verified.

Theorem: s/6 <= gamma_M <= 4s with s = beta + sqrt(beta) + 1/n, so relaxation is Theta(sqrt(n)) when beta_n ~ 1/n. This answers the order question in Aldous's coagulation-fragmentation problem (the gap between orders sqrt(n) and n at beta_n ~ b/n).

Checked by hand:
- Cycle representation. pi_B(S) proportional to (beta n)^k/(k-1)! is reversible: the ratio beta n/k against the removal rate k/n. Each adjacency is removed at rate (k-1)/n and a given pair of segments is adjacent with probability 2/(k-1) in uniform cyclic order, so the averaged pair-merge rate is 2/n, matching the polymer chain. Total merge rate k(k-1)/n on both sides. Equal variances and Dirichlet forms on lifted functions make gamma_M a constrained infimum over B.
- Upper bound (U). Count chain with lambda_k = beta(n-k), mu_k = k(k-1)/n. The derivative chain A_0 has killing beta + 2k/n. With h = 1/((k+a)(k+a+1)), I recomputed -A_0 h/h = 2 beta(n-k-1)/(k+a+2) + beta + 2ka/(n(k+a-1)) exactly, and it is at most beta + 4 max(sqrt beta, 1/n) <= 4s.
- Lower bound (L0). The degree-0 killing is at least beta + 2/n, degrees l >= 2 at least 2 beta + 2/n, and rotation invariance removes degree 1. I took the sector formula (H) on trust; the solver also matched full edge spectra n = 2..9 numerically.
- Lower bound (L1), for n >= 8 and 4/n^2 <= beta <= 1/16. The h = 1/(k+a) certificates give sqrt(beta)/5 in degree 0 and sqrt(beta)/5 or sqrt(beta)/3 in degrees l >= 1. I rechecked both case splits: n-k-l >= n/2 and k+a+1 <= 5a/2 when k <= a; (k-1)/(k+a-1) >= 1/3 when k >= a >= 2.
- Combination. All four cases of section 5 hold.
