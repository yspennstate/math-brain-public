# P0110 boundary lemma: sharp forced-straight scale

Author w378, 2026-10-10. Status: proved special case by the author; independent mathematical review pending with w380. This is a boundary lemma, not a solution or refutation of P0110.

Let d >= 2, a > 0, b > a, n >= 1 an integer. Assign each undirected nearest-neighbor edge of Z^d a weight in [a,b]. Let P_n be the n-edge axial path from 0 to n e_1. If n(b-a) < 2a, P_n is the unique geodesic.

Proof. Positive edge weights make every minimizing path simple. Any path from 0 to n e_1 has length n+2k for some integer k >= 0: count positive and negative coordinate steps. A path of length n must take only positive e_1 steps, so is P_n. Every different simple path therefore costs at least (n+2)a, whereas P_n costs at most nb. The strict hypothesis says nb < (n+2)a. It also proves that the infimum is attained by P_n. This proof uses no independence.

For iid nondegenerate weights in [a,b] with mean mu and variance sigma^2, the same hypothesis gives exactly T(0,n e_1)=sum_{i=1}^n tau_i, E T=n mu, Var T=n sigma^2, and every geodesic has zero transverse displacement from the segment [0,n e_1].

The scale is sharp as a statement uniform over assignments with this support. A parallel detour in the e_2 direction consists of the step 0 -> e_2, n positive e_1 steps, and the step n e_1+e_2 -> n e_1; it has n+2 edges and shares no edge with P_n. Assign weight b to P_n and weight a to the detour. If n(b-a)>2a the detour is strictly cheaper. If n(b-a)=2a both are geodesics: every other path has either n edges (P_n) or at least n+2, hence costs at least (n+2)a. For the iid two-point law with P(tau=b)=p in (0,1), this edge assignment occurs with probability p^n(1-p)^(n+2)>0. No weights on other edges need to be specified.

Continuous variant. If weights are iid Uniform[1,1+epsilon], epsilon>0, then for n epsilon<2, Var T(0,n e_1)=n epsilon^2/12 exactly. For n epsilon>2, an open neighborhood of the detour assignment has positive probability and makes P_n strictly suboptimal. At equality, P_n is almost surely uniquely optimal since its cost is strictly less than n(1+epsilon) almost surely.

Sharp fixed-law classification. For each fixed epsilon>0 and each integer n>=1, P_n is the unique geodesic almost surely if and only if n epsilon<=2. The preceding comparison proves the sufficient direction, including equality. To prove necessity, suppose n epsilon>2, put delta=(n epsilon-2)/(4n+4), require all n axial weights to lie in [1+epsilon-delta,1+epsilon], and require all n+2 parallel-detour weights to lie in [1,1+delta]. Since 0<delta<epsilon/4, the two route costs differ by at least n epsilon-2-(2n+2)delta=(n epsilon-2)/2>0 in favor of the detour. The routes share no edges; the event probability is exactly (delta/epsilon)^(2n+2)>0. This proves failure of almost-sure axial optimality, rather than failure on every configuration. Positive weights ensure a global minimizing path exists, because comparison with the straight route bounds its length and leaves finitely many candidate paths. The exact variance formula also holds at equality, since T is still the iid axial sum almost surely.

In particular, for the one fixed law Uniform[1,5/4], the cutoff is n=8. At n=9 the above event has delta=1/160, probability 40^(-20), and decreases the competitor cost by at least 1/8. This is a finite-scale classification, not an asymptotic exponent theorem.

Consequent obstruction. Fix integers M>=2 and n>=1 and choose 0<epsilon<min(1,2/(Mn)). For the nondegenerate continuous iid law Uniform[1,1+epsilon],

Var T(0,Mn e_1) = M Var T(0,n e_1) > 0.

Therefore no rho<1 can give Var T(0,Mn e_1) <= rho M Var T(0,n e_1) at all n>=N with the same N for every nondegenerate continuous iid law supported in [1,2]. Choose n>=N and epsilon as above. The counterexample concerns uniformity in the law of a proposed variance-contraction bridge. It says nothing against eventual contraction at a threshold N(F) depending on a fixed law F, and nothing against the original existential KPZ problem.

Hardest remaining gap for P0110: for a fixed admissible iid law, establish compatible large-scale lower and upper fluctuation/wandering exponents (or another sufficient set of exact exponent hypotheses), rather than a finite-scale variance identity. The epsilon used in the counterexample depends on n; it cannot be varied with n to prove any assertion about a single law's asymptotic exponent.
