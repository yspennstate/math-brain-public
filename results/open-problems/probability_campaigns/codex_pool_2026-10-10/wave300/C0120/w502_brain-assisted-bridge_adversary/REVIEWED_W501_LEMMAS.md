# C0120: saved proofs, all awaiting w503's independent review

Setup for L1-L3: n>=2; independent N(0,1) weights on the finite triangle Lambda_n={(i,j):i,j>=0,i+j<=n-1}. Paths have n vertices starting at (0,0), each next step right/up, and endpoint free. M_n is the maximum path sum, P_n its almost surely unique maximizer. Distinct path incidence vectors differ, so their Gaussian weight difference has nonzero variance and ties have probability zero. Set g^t=e^(-t)g+sqrt(1-e^(-2t))g', with g' independent; h_n(t)=E|P_n(g) intersect P_n(g^t)|.

L1 (known source bridge, stated with exact rate): h_n is nonnegative and nonincreasing, and
Var(M_n)=integral_0^infinity e^(-t) h_n(t) dt.
For every tau>0,
(1-e^(-tau)) h_n(tau)<=Var(M_n)<=n(1-e^(-tau))+e^(-tau)h_n(tau).
Thus h_n(n^(-alpha))<=C n^(1-delta), with constants C,alpha,delta>0 independent of n, implies Var(M_n)<=(1+C)n^(1-min(alpha,delta)). Conversely, Var(M_n)<=C n^(1-epsilon) implies h_n(n^(-alpha))<=2C n^(1-epsilon+alpha) for 0<alpha<epsilon, since 1-e^(-tau)>=tau/2 when 0<tau<=1.

Proof: M_n is Lipschitz with almost everywhere gradient (1_{v in P_n})_v, whose squared norm is n. The Gaussian covariance identity (Chatterjee Lemma 3.3) applies, giving the integral. If P_t is the stationary Gaussian OU semigroup, each summand E[f_v(g)f_v(g^t)] is ||P_(t/2) f_v||_2^2 and is nonincreasing by the L2 contraction and semigroup properties; f_v=1_{v in P_n} is bounded and square integrable. Sum the finitely many terms. Split the integral at tau, use h_n(t)<=n before tau and monotonicity after tau for the upper inequality; integrate the lower bound h_n(t)>=h_n(tau) on [0,tau] for the lower inequality. Substitute the indicated powers. These are source consequences, not new novelty claims.

L2 (hypercontractivity envelope): define q_v=P(v in P_n) and a(t)=tanh(t/2). The standard Gaussian hypercontractive inequality ||P_s f||_2<=||f||_(1+e^(-2s)) gives
h_n(t)<=B_n(t):=sum_{v in Lambda_n} q_v^(1+a(t)).
Proof: with s=t/2 and f_v an indicator, its Lp norm squared is q_v^(2/p), and 2/(1+e^(-t))=1+tanh(t/2). Sum. At t=0 interpret p=2. This bound uses no independence of path-site indicators.

L3 (proved obstruction to this envelope supplying a power improvement): for ANY nonnegative q_v with sum_{v:i+j=k}q_v=1 on each k=0,...,n-1,
B_n(t)>=sum_{k=1}^n k^(-a(t))>=n^(1-a(t)).
Consequently, for every fixed alpha>0,
B_n(n^(-alpha))/n>=exp[-(log n)n^(-alpha)/2] -> 1,
and the integrated certificate satisfies
J_n(q):=integral_0^infinity e^(-t)B_n(t)dt >= (n-1)/log n.
In particular J_n(q) is not O(n^(1-epsilon)) for any fixed epsilon>0. Knowing all exact one-site marginals cannot make this unweighted per-site hypercontractivity certificate prove the target.

Proof: the layer k-1 has k sites. For a in [0,1], Jensen gives sum_layer q_v^(1+a)>=k*(1/k)^(1+a)=k^(-a), including a=0. Summing yields B_n(t)>=n*n^(-a(t)). Since tanh(t/2)<=t/2, the small-time lower bound follows; also B_n(t)<=sum_v q_v=n because 0<=q_v<=1, so the normalized envelope tends to 1 by squeezing. In the integrated bound, set u=e^(-t). Then a(t)=(1-u)/(1+u)<=1-u, so J_n(q)>=n*integral_0^1 exp[-(log n)(1-u)]du=(n-1)/log n. Finally ((n-1)/log n)/n^(1-epsilon) diverges. THIS IS A LOWER BOUND ON THE HYPERCONTRACTIVE UPPER-BOUND CERTIFICATE, NOT ON h_n(t) OR Var(M_n). It refutes only using this certificate as the missing bridge. BKS shifts, other semigroup estimates, or joint path geometry require separate arguments.

L4 (conditional correction to prior attempt): if Var(F_n)=n^(2chi+o(1)) and chi=2xi-1 are assumed, then a bound Var(F_n)<=C n^(1-epsilon) requires xi<=3/4-epsilon/4. Conversely xi<3/4 under those two assumptions yields a power upper bound with some smaller positive epsilon for all sufficiently large n. Proof: 2chi=4xi-2; compare to 1-epsilon. xi=4/5 gives variance exponent 6/5 despite xi<1. No claim establishes the KPZ relation itself for the current model.

Remaining single hardest gap: prove polynomially small OU-time loss of coupled path overlap by information stronger than the above per-site hypercontractive envelope. No such loss is proved here. C0120 is NOT solved.

Primary support: https://arxiv.org/html/0810.4221 , Lemma 3.3, Lemma 3.5, Theorem 3.2, Lemma 4.1, Section 8. Own deductions: L3 and the explicit rate bookkeeping in L1/L4.
