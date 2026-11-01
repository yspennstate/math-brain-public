# P0347: joint finite-n laws and an exact one-split correction

2026-10-10. Label: proof of finite-n recurrences, awaiting w346 KEEP. The asymptotic joint distribution remains unresolved; novelty is unverified.

Use the critical beta=-1 Markov branching model: q_n(i)=n/(2 H_{n-1} i(n-i)), 1<=i<n, and conditional on I=i the two daughter trees are independent copies of sizes i and n-i. Let S be external path length and C the Colless sum, both zero for one leaf. Then S_n=n+S_i+S_{n-i} and C_n=|n-2i|+C_i+C_{n-i}. Consequently their joint probability polynomial is exactly

    G_1(u,v)=1,
    G_n(u,v)=sum_{i=1}^{n-1} q_n(i) u^n v^{|n-2i|} G_i(u,v)G_{n-i}(u,v).

This gives an exact algorithm for every fixed n and the full joint law, including all dependence between the indices. It does not identify a limiting normalization or limiting law.

For the one-split minimum M=min(I,n-I), pairing i with n-i gives

    E M = n/H_{n-1} * (H_{n-1}-H_floor(n/2) + 1_{n even}/n).

Thus the exact Colless root toll is n-2 E M. The center term when n is even must occur once, not twice. This sharpens the recorded bound E M<=n/H_{n-1}. It also confirms the earlier quadratic root identity E(n-2I)^2=n^2-2n(n-1)/H_{n-1}.

For any additive index with deterministic root toll t_n(i), define d_n(i)=t_n(i)+mu_i+mu_{n-i}-mu_n. Conditional independence and total variance give

    mu_n=sum_i q_n(i)(t_n(i)+mu_i+mu_{n-i}),
    V_n=sum_i q_n(i)(V_i+V_{n-i}+d_n(i)^2).

For two indices A,B the corresponding covariance is sum_i q_n(i)(K_i+K_{n-i}+d_n^A(i)d_n^B(i)). These recurrences require no unproved occupation ansatz. Initial means, variances and covariance at n=1 are zero.

Independent failure checks: q sums to one; exact joint probabilities normalize; direct one-split sums agree with the harmonic formula for odd/even n; the joint law has S>=C and S-C even; its moments agree with the total-variance recurrences. Conditional subtree independence is a model assumption, not inferred merely from the split probabilities.

Sources read: P0347-A001 in the existing campaign ledger and the corresponding store attempt card. The cached Aldous-Janson paper supplies q and Markov branching. Its distributional request remains open in the local corpus; a negative literature search is not a current global status certificate.
