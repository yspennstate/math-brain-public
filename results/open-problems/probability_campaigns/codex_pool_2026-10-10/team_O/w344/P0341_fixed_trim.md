# P0341: fixed-width trimming does not repair the divergent-test ansatz

Label: proof (worker checked); primary transition formula confirmed in Aldous-Janson equation (2), cached text lines 577-589. Independent audit: pending w346. This is a refuted repair of Ansatz 20, not a solution of the uniform occupation-bound problem.

The earlier campaign proof uses a(n,n)=1. Consider the proposed repair that, for a fixed integer L>=0, sums only over 2<=j<=n-L-1. Let the harmonic descent chain have transitions q(n,j)=1/((n-j)H_(n-1)) for 1<=j<n, and let a(n,j) be its probability of visiting j. The first jump gives a(n,j)>=q(n,j).

Set g(j)=j when j=2^r for some integer r>=1, and g(j)=0 otherwise. This is nonnegative and g(j)<=j. For N=2^K and n=N+L+1, the retained term j=N alone gives

    sum_(j=2)^(n-L-1) a(n,j)g(j) >= N/((L+1)H_(N+L)).

The comparison series uses a(j)=6H_(j-1)/(pi^2(j-1)). For large K, n<2N, so its nonzero terms are precisely j=2,4,...,2^K. Since 1<=j/(j-1)<=2 and H_(2^r-1) is of order r, their sum is of order K^2. Meanwhile H_(N+L) is of order K for fixed L. The ratio is at least a positive L-dependent constant times 2^K/K^3, which tends to infinity. The conclusion holds whether the comparison series stops at n or at n-L-1, since the support sets coincide along these n.

Checks that can fail: transition normalization and the first-jump formula; indexing of the retained cutoff; accidental inclusion of 2^(K+1); confusion between hitting probability and expected repeated visits; treating a fixed L as a growing L; replacing the original open problem by its displayed ansatz. The chain strictly descends, so hitting and occupation probabilities coincide. The theorem here quantifies only over fixed L.

Sources: ~/Downloads/Probability_1000_20h_20260906/proofs/P0341_beta_tree_sparse_occupation_counterexample_candidate.md; Aldous-Janson, arXiv:2303.02529v3, 17 April 2025, equation (2), occupation definition (49), and Ansatz 20, PDF pp.9,28-30,39-40. Primary transition and occupation definitions were checked in the cached text; see source_followup.json.
