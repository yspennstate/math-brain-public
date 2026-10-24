Author-written proofs, 2026-10-10. Independent referee: w425, review pending. These are general finite-event identities and a special-graph counterexample, not a proof of C0023. No novelty claim.

L1. Conditional bridge identity and exact reverse-parameter cost.

Let E be a finite set of edges, A a nonempty increasing event on {0,1}^E with P_p(A)>0 for 0<p<1, and f(p)=P_p(A) under independent Bernoulli(p) edges. An edge is pivotal when changing only that edge changes 1_A. Let N_A(omega) count OPEN pivotal edges. Define lambda_A(p)=E_p[N_A | A]. Then

    lambda_A(p) = p f'(p)/f(p),
    f(a)/f(b) = exp(-integral_a^b lambda_A(s)/s ds),  0<a<b<1.

Proof. Differentiate the finite product measure polynomial one coordinate at a time. The derivative is sum_e (P_p(A | omega_e=1)-P_p(A | omega_e=0)). Monotonicity makes each summand P_p(e pivotal); pivotality depends only on the other edges. An open pivotal edge entails A, so E_p[N_A 1_A]=E_p[N_A]=p sum_e P_p(e pivotal)=p f'(p). Divide by f(p). Integrate the derivative of log f on [a,b]. This uses no assumption of independence between different pivotal-edge indicators.

L2. A sufficient backward-interval criterion, with its missing hypothesis explicit.

For Bernoulli bond percolation on Z^d let B_n=[-n,n]^d intersect Z^d, A_n={0 connects to the vertex boundary of B_n using edges within B_n}, f_n(p)=P_p(A_n), and lambda_n(p)=E_p[N_{A_n}|A_n]. The events decrease to {0 connects to infinity}; hence f_n(p) decreases to theta(p). Suppose 0<a<p_c<1, theta(p_c)>0, and liminf_n integral_a^{p_c} lambda_n(s)/s ds < infinity. Then theta(a)>0, contradicting a<p_c. In particular an integrable g on [a,p_c] with lambda_n(s)/s<=g(s) for every n would suffice.

Proof. Choose M<infinity and a subsequence n_k tending to infinity on which the integral is at most M. L1 gives f_{n_k}(a)>=f_{n_k}(p_c)e^{-M}>=theta(p_c)e^{-M}>0. Pass to the decreasing-event limit. The definition p_c=inf{p:theta(p)>0} gives theta(a)=0 when a<p_c. The domination condition bounds every integral by integral g. The required domination is NOT proved for Z^d. The criterion is an analytic reformulation, not an independent geometric mechanism.

L3. Endpoint bridge control, even all exponential moments, does not imply backward continuity on general locally finite graphs.

Construct a countable simple graph Gamma with vertices a_0,a_1,... . For each integer n>=1, connect a_{n-1} to a_n by m_n=n^2 2^{n+1} internally vertex-disjoint paths of length ell_n=n+1. Internal vertices of different paths and blocks are distinct. Every degree is finite; terminal degrees are unbounded and the graph is not transitive. Put independent Bernoulli(p) bonds on Gamma. Let A_N={a_0 connects to a_N}, using its first N blocks. Then

    h_n(p)=1-(1-p^{ell_n})^{m_n},
    f_N(p)=product_{n=1}^N h_n(p),
    theta_Gamma(p)=product_{n>=1} h_n(p).

The product identities hold because blocks have disjoint edge sets and every a_0-a_N path must cross each successive block. Also A_N decrease to the event that the cluster of a_0 is infinite, since the union of any fixed finite number of blocks is finite.

At b=1/2, x_n=b^{ell_n}=2^{-n-1} and m_n x_n=n^2, so 1-h_n(b)=(1-x_n)^{m_n}<=e^{-n^2}. Therefore

    theta_Gamma(1/2) >= 1 - sum_{n>=1} e^{-n^2}
                       >= 1 - e^{-1} - e^{-4}/(1-e^{-5}) > 0.

The last series bound uses (n+1)^2-n^2>=5 for n>=2. For 0<=p<1/2, h_n(p)<=m_n p^{ell_n}=n^2(2p)^{n+1} tends to zero. Since theta_Gamma(p)<=h_n(p) for every n, theta_Gamma(p)=0. Thus p_c(Gamma)=1/2 and theta_Gamma(p_c)>0.

Here an open pivotal edge in a crossed block occurs exactly when that block has exactly one fully open path. In this case its ell_n path edges are precisely that block's open pivotal edges. Given A_N the crossed blocks remain independent, so

    N_{A_N} = sum_{n=1}^N ell_n I_n,
    P(I_n=1 | A_N) = r_n = m_n x_n(1-x_n)^{m_n-1}/h_n(b)
                           <= n^2 e^{-n^2+1/4}/(1-e^{-1}).

For any fixed t>=0,

    E_b[exp(t N_{A_N}) | A_N]
      = product_{n=1}^N (1+r_n(exp(t ell_n)-1))
      <= exp(sum_{n>=1} r_n(exp(t(n+1))-1)) < infinity,

uniformly in N, because a quadratic negative exponent dominates t(n+1). In particular sup_N lambda_N(b)<infinity. A concrete upper bound is

    sup_N lambda_N(b)
      <= 2 e^{-3/4}/((1-e^{-1})(1-6e^{-3})) < infinity.

To obtain this bound use ((n+2)(n+1)/n^2)e^{-(2n+1)}<=6e^{-3}<1 to sum (n+1)n^2e^{-n^2} geometrically.

Nevertheless, for every 0<a<b, L1 gives integral_a^b lambda_N(s)/s ds = log(f_N(b)/f_N(a)) tending to infinity. A bound only at b, even uniform exponential moments there, gives no domination over a fixed interval below b.

Moreover there is almost surely exactly one infinite cluster at b: block failures have summable probabilities, so only finitely many fail (first Borel-Cantelli); every later terminal belongs to a single infinite tail. Any infinite path must visit infinitely many terminals, since each block is finite, and must eventually join this tail. Thus uniqueness alone also does not repair the inference. This does not counterexample Z^d: transitivity and bounded degree are absent.

Hardest remaining gap for C0023: derive an integrable uniform bound on conditional bridge load over a nonzero interval [p_c-delta,p_c], from theta(p_c)>0 and the exact Z^d product geometry. Endpoint bounds, uniqueness, and finite-volume continuity do not provide this bound.

L4. Quenched fragility of a hypothetical infinite critical cluster.

Let Omega be independent Bernoulli(p_c) bond percolation on Z^d, where 0<p_c<1. For P_{p_c}-almost every Omega, independent Bernoulli(q) retention on the already open edges of Omega has no infinite component for every 0<=q<1. Consequently, any infinite component H of such an Omega has quenched bond-percolation threshold 1 (with the usual root-specific definition, which has the same threshold at each vertex of a connected graph).

Proof. For each rational q in [0,1), use independent retention coins on every lattice edge, keeping an edge iff Omega had it open and its retention coin succeeds. The resulting edge indicators are independent Bernoulli(p_c q). Since p_c q<p_c, no vertex has an infinite component with positive probability; a countable union over vertices shows that no infinite component exists almost surely in the retained graph. Fubini then says that for almost every Omega the conditional probability of any infinite retained component is zero. Intersect these full-measure statements over countably many rational q. For arbitrary real q<1 choose rational r with q<r<1 and use the monotone retention coupling. A retained infinite component inside any H would also be an infinite component of the entire retained Omega, so it has zero probability. At q=1 each vertex of an infinite H is connected to infinity with probability one. This proves the threshold claim. No uniqueness, independence between clusters, or statement about whether Omega actually has an infinite component was assumed.

The route's equivalent geometric bottleneck: from existence of an infinite critical lattice cluster, show that some such cluster would retain percolation for a q<1 on a set of Omega of positive P_{p_c} measure. L4 rules this out, yielding a contradiction if that resilience result were established. That resilience result is unproved; L3 illustrates why existence and uniqueness alone are insufficient in a broader graph class.
