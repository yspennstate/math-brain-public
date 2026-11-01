# C0120 independent attempt: a bounded-degree obstruction

2026-10-10. Source-faithful target and model: STATEMENT.md. Author proof only; independent review pending. This is an obstruction to an abstract proof route, not a counterexample to the lattice conjecture or a novelty claim.

The older C0120-A001 invokes a quantitative chaos estimate without proving one and draws an analogy with FPP. This attempt instead tests the proposed reduction to small first Gaussian chaos and bounded-degree directed geometry. No current core-lane proof was read before this choice. The recalled FPP scar warns that unconditional occupation information can leave a conditional-variance residual; the conditional-product scar rules out multiplying bounds for correlated prefixes. Our prefix estimates use a union bound, and our variance comparison uses the L2 triangle inequality.

## L1: explicit logarithmic variance scale for independent Gaussian maxima

Let Z_1,...,Z_m be independent N(0,1), W_m=max_i Z_i, and m>=16. There is an explicit constant

    a=(2/5) exp(-3/2), c=(1-exp(-a))/8 > 0

such that

    c/log m <= Var(W_m) <= 2/log m.

Lower bound. Write Q(t)=P(Z_1>t), and take the unique t>0 with Q(t)=1/m. The Gaussian Mills bounds, valid for x>0, are

    x phi(x)/(1+x^2) <= Q(x) <= phi(x)/x.

They follow by integrating the density derivative: the upper bound uses u>=x in the Gaussian integral; integration by parts gives Q(x)=phi(x)/x-integral_x^infinity phi(u)/u^2 du >=phi(x)/x-Q(x)/x^2. Since Q(1)>=phi(1)/2>1/12>1/16, t>=1. Put s=t+1/t. The Mills bounds give

    Q(s)/Q(t) >= [ts/(1+s^2)] exp(-(s^2-t^2)/2)
                >= (2/5) exp(-3/2)=a.

Here ts=t^2+1, 1+s^2=t^2+3+t^-2<=t^2+4, and (t^2+1)/(t^2+4)>=2/5. Thus P(W_m<=t)=(1-1/m)^m>=1/4, and P(W_m>=s)>=1-exp(-a). The first inequality holds for all m>=2: x log(1-1/x) is increasing for x>1, since its derivative is log(1-1/x)+1/(x-1)>=0. For an independent copy W'_m,

    Var(W_m)=(1/2) E[(W_m-W'_m)^2]
              >=P(W_m<=t) P(W_m>=s) (s-t)^2.

Also Q(t)<=phi(t)/t<=exp(-t^2/2), so t^2<=2 log m. This proves the lower bound with the stated c.

Upper bound. We reuse the standard finite-dimensional Gaussian Ornstein-Uhlenbeck covariance identity and hypercontractivity with their exact hypotheses (Chatterjee 2008, Lemmas 3.3 and 4.1). W_m is Lipschitz and has weak derivative 1_{i=argmax Z}; ties have probability zero. For h_i=1_{i=argmax Z}, E h_i=1/m, and

    E[h_i(Z) h_i(Z^t)]=||P_(t/2) h_i||_2^2
       <=||h_i||_(1+exp(-t))^2=m^(-2/(1+exp(-t))).

The identity therefore yields, after u=exp(-t),

    Var(W_m) <= integral_0^1 m^(-(1-u)/(1+u)) du
                <= integral_0^1 exp(-(log m)(1-u)/2) du
                <=2/log m.

No asymptotic extreme-value law or unproved decorrelation rate is used.

## L2: a common-root directed graph with an explicit prefix error

Fix r>=1, m=2^r, and n=m. Take a complete binary tree with internal levels 0,...,r-1. At each of its m leaf positions attach a private chain of n vertices; the first chain vertex occupies level r. Orient every edge away from the root. Put independent N(0,1) weights at all vertices. There are m root-to-terminal paths, each containing L=n+r vertices. Every vertex has indegree at most 1 and outdegree at most 2. The graph is planar as an abstract graph, but is not the fixed east/north lattice of C0120.

Let U_i be the r internal-prefix weights on path i, S_i its n private-chain weights, A=max_i S_i, and M=max_i(U_i+S_i). The S_i are independent N(0,n), and independent of all prefix weights. The U_i are generally correlated. Pointwise

    |M-A| <=R=max_i |U_i|.

Since each U_i~N(0,r), the union bound gives P(R^2>x)<=min(1,2m exp(-x/(2r))). Integration, split at 2r log(2m), gives

    E[(M-A)^2] <=E[R^2] <=B=2r(log(2m)+1).

The correlation among the U_i is irrelevant to this valid union bound.

## L3: small first Gaussian chaos, exactly

For the above M, the first Gaussian chaos is the orthogonal projection

    Pi_1 M=sum_v E[M g_v] g_v.

Gaussian integration by parts for a finite Lipschitz maximum gives E[M g_v]=E[partial_v M]=P(v belongs to the unique maximizing path). The tree automorphism group acts transitively on the m chains, preserves the independent Gaussian law, and permutes maximizing paths equivariantly. Therefore every chain is selected with probability 1/m. Each internal vertex at level k belongs to m/2^k chains and has occupation probability 2^-k. Consequently

    Var(Pi_1 M)=sum_(k=0)^(r-1) 2^k(2^-k)^2+mn/m^2
                  =2-2/m+n/m=3-2/m.

Moreover partial_v M is 0 or 1 almost surely, and sum_v(partial_v M)^2=L. Thus total Gaussian derivative energy is L while the first-chaos contribution stays below 3.

## L4: first-chaos and bounded-degree information cannot force a power gain

L1 gives c n/log m<=Var(A)<=2n/log m. The triangle inequality for centered L2 random variables gives

    |sqrt(Var(M))-sqrt(Var(A))| <=sqrt(Var(M-A))<=sqrt(B).

For any r satisfying B<=c n/(4 log m), this implies

    c n/(4 log m) <=Var(M)<6n/log m.

Such r include all sufficiently large integers because B=O(r^2) and n/log m=2^r/(r log 2). Since L=n+r is comparable to n and log L is comparable to log m, Var(M)=Theta(L/log L). For every fixed epsilon>0, this is not O(L^(1-epsilon)). L3 shows at the same time that the first Gaussian chaos is O(1), every derivative is bounded by 1, all paths have the same length, the root is fixed, and all outdegrees are at most 2.

Conclusion proved for this special graph family: those properties do not imply a polynomial variance gain. This does not contradict C0120 because the graph changes with r and is not the fixed oriented lattice.

## L5: fixed positive-temperature extension (separate from the source target)

For any fixed beta>0 define

    F_beta=(1/beta) log[(1/m) sum_i exp(beta(U_i+S_i))].

Pointwise M-(log m)/beta<=F_beta<=M, so

    E[(F_beta-A)^2] <=2B+2((log m)/beta)^2=:B_beta.

For B_beta<=c n/(4 log m), the same centered L2 argument gives c n/(4 log m)<=Var(F_beta)<6n/log m. This holds for all sufficiently large r for each fixed beta. Gaussian integration by parts gives E[F_beta g_v]=E[partial_v F_beta]; transitivity gives expected Gibbs chain mass 1/m. Hence the first-chaos variance is again 3-2/m. Since each occupation mass is between 0 and 1 and the path length is L, total gradient energy is at most L. This finite-temperature example has a normalized log partition function; log Z itself differs by a factor beta and a deterministic normalization.

## Single hardest remaining gap

To prove the actual C0120 target one must use a quantitative property of the fixed east/north lattice that excludes this logarithmic extremal mechanism. The tree has m=2^r distinct sites already at layer r, whereas the source lattice has only r+1 sites there and permits paths to reconverge. Neither small first Gaussian chaos nor bounded outdegree controls the higher Gaussian chaoses that retain variance of order L/log L in this example. An explicit polynomial bound on their combined variance, or an equivalent polynomial noise-overlap estimate proved using lattice geometry, remains absent. C0120 is UNSOLVED BY THIS PACKET.

NEXT: Independent referee checks L1-L5 and the source correction; a continuation must attack a lattice-specific higher-chaos or overlap estimate rather than infer it from first-chaos smallness.
