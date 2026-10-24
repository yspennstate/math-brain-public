# P0104: typical-scale to variance bridge

2026-10-10, w369. All proofs below are author proofs awaiting w371's independent review. P0104 is not solved. The statement-only challenge was saved before the proof. After recovering an absent peer registry row and a transient mesh lock, the statement was delivered to w370 (msg-eb11695c9b), then the complete proof packet to w371 (msg-9ccf802796). Receipts are in COMMUNICATION_RECEIPTS.json.

Target and source scope are in STATEMENT_FOR_ADVERSARY.md. The recovered earlier attempt establishes the logarithmic barrier, not a polynomial saving. Owner scars also record a solved directed width-three time constant and an unresolved sharp multiscale variance recursion. This lane uses neither computation. The perceptron proof-gap scar requires identifying the missing mathematical input even when mechanical checks pass.

The single hardest attempted bridge gap is a uniform bound on the standardized fourth moment of planar iid Exp(1) passage times. Nondegenerate n^(1/3) typical scaling is also unproved and remains an independent prerequisite for the target. Nothing here supplies either input for lattice FPP.

## L0. Quantitative anti-concentration does lower-bound variance

The read-only math probe returned card `claim_3ccc6fc493b4e17b5c29966949004f575c51205c8a4f0ba3bc516d0b752ebea4`. Its body says: "It does not by itself lower-bound the variance" about an anti-concentration statement. As a categorical separation this is incorrect. This correction concerns that inference, not a claim that the cited paper's theorem is wrong.

Let X be real and square-integrable. If L>0, epsilon in (0,1], and every closed interval of length L has probability at most 1-epsilon, then

    Var(X) >= epsilon L^2/4.

Proof. Apply the interval hypothesis to [E X-L/2,E X+L/2]. Its complement has mass at least epsilon, and on that complement |X-E X|>L/2. Integrating the squared deviation gives the bound. Conversely a variance lower bound alone does not ensure anti-concentration, as L4's rare-tail construction demonstrates. The repair must preserve this directionality and the uniform interval quantifier.

## L1. Sharp two-quantile variance lower bound

Let X be a real square-integrable random variable. Suppose a < b, p,q > 0, P(X <= a) >= p, and P(X >= b) >= q. Necessarily p+q <= 1. Then

    Var(X) >= [pq/(p+q)] (b-a)^2.

Proof. Write mu=E X. If mu lies in [a,b], the two disjoint events give
Var(X) >= p(mu-a)^2 + q(b-mu)^2. Completing the square gives the claimed lower bound. If mu<a, the right event alone gives Var(X) >= q(b-mu)^2 >= q(b-a)^2, which is at least the claimed expression. The case mu>b is symmetric. Equality is attained by masses p at a, q at b, and 1-p-q at (pa+qb)/(p+q). The mean of this three-atom law is that middle location, so the computed variance is exactly the lower bound. This proves sharpness. No claim about independence of lattice events is used.

Consequence. If (X_n-m_n)/a_n converges in law to a nondegenerate Z, choose continuity points u<v for which P(Z<=u)>0 and P(Z>=v)>0. Convergence supplies fixed positive lower bounds p,q on the corresponding probabilities for large n. Thus Var(X_n)>=c a_n^2. This direction needs no fourth-moment bound.

Checked primary-source consequence. Damron--Hanson--Houdre--Xu, arXiv:1810.08270v2, Theorem 1, is stated on Z^2. Write I=inf supp F. Its distribution hypotheses are F(0)<p_c=1/2 and, if I>0, F(I)<the oriented-bond threshold. It gives deterministic A_x,B_x with two strictly positive probability liminfs at T(0,x)<=A_x and T(0,x)>=B_x and a strictly positive liminf of (B_x-A_x)/sqrt(log ||x||). If additionally T(0,x) is square-integrable (for example iid Exp(1)), L1 gives Var(T(0,x))>=c log ||x|| for sufficiently large ||x||. This is a deduction of an already known lower bound, not a new exponent. The paper's Remark 2 says the method gives only a constant lower bound for d>2. The retrieved legacy card must preserve both the implication direction and this dimension restriction.

## L2. Quantitative interval-width comparison

Let 0<sigma^2=Var(X)<infinity and E|X-E X|^4 <= K sigma^4, with K finite. Jensen gives K>=1. For p in (0,1/(32K)], define W_p(X) as the infimum of the lengths of closed intervals having mass at least 1-p. Then

    sigma <= W_p(X) <= 2 sigma/sqrt(p).

Proof. Chebyshev gives the upper bound using the interval centered at mu=E X with radius sigma/sqrt(p). For the lower bound, let X' be an independent copy constructed on a product probability space and put D=X-X'. Its second moment is 2 sigma^2. The inequality |r-s|^4 <= 8(|r|^4+|s|^4) gives E D^4 <= 16K sigma^4. Take any interval I of length ell and mass at least 1-p. Outside the event {X and X' both belong to I}, the union bound gives probability at most 2p. Inside that event, |D|<=ell. Cauchy--Schwarz therefore gives

    2 sigma^2 <= ell^2 + (E D^4)^(1/2) sqrt(2p)
                 <= ell^2 + 4 sqrt(2Kp) sigma^2.

For the stated p, the last coefficient is at most 1. Hence ell^2>=sigma^2. Taking the infimum over all such intervals proves the claim; no attaining interval is required. X' is solely a proof device. There is no independence assumption across n or between selected geodesic blocks.

## L3. Distributional scaling transfers to variance under uniform kurtosis

Let X_n be real random variables with finite positive variances sigma_n^2. Suppose E|X_n-E X_n|^4 <= K sigma_n^4 with one finite K for all n. Let m_n be deterministic, a_n>0, and Y_n=(X_n-m_n)/a_n converge in distribution to a nondegenerate real Z. Then Z has finite fourth moment, its variance is positive, and

    Var(X_n)/a_n^2 -> Var(Z) in (0,infinity).

Proof. Fix p=1/(32K). Weak convergence implies tightness, so there is M<infinity such that P(|Y_n|<=M)>=1-p for all sufficiently large n. The interval [m_n-M a_n,m_n+M a_n] has width 2M a_n. L2 implies sigma_n<=2M a_n. Write mu_n=E X_n. If |mu_n-m_n|>M a_n, every point of that interval lies at distance at least |mu_n-m_n|-M a_n from mu_n. Its mass is at least 1-p, so its contribution to variance yields

    |mu_n-m_n| <= M a_n + sigma_n/sqrt(1-p).

This bound also holds if the mean is inside the interval. Both sigma_n/a_n and (mu_n-m_n)/a_n are uniformly bounded eventually. Applying |r+s|^4<=8(|r|^4+|s|^4) now shows sup_n E|Y_n|^4<infinity for all sufficiently large n. Adding the finite number of initial terms preserves finiteness. Consequently Y_n and Y_n^2 are uniformly integrable. Truncating to bounded continuous functions, taking the distributional limit, then removing the truncation gives E Y_n -> E Z and E Y_n^2 -> E Z^2. Fatou via bounded truncations also gives E|Z|^4<infinity. Thus Var(Y_n)->Var(Z). A nondegenerate square-integrable law has strictly positive variance. This proves the theorem.

Application boundary. With a_n=n^(1/3), L3 would yield the stronger positive limiting variance constant, hence the target exponent. Its two lattice inputs have not been proved. More weakly, L2 shows that W_p(T_n)=n^(1/3+o(1)) with uniform kurtosis would suffice for the exponent, without identifying a limiting law.

## L4. Rare-tail counterexample to the weaker route

For every real parameter n>=3 (in particular every integer n>=3) let p_n=n^(-1/6), a_n=n^(1/3), s_n=sqrt(n/log n), and b_n=s_n log n=sqrt(n log n). Let R_n have masses (1-p_n)/2 at each of +/-a_n and p_n/2 at each of +/-b_n. Set X_n=n+R_n. Each X_n is positive, has mean n and finite moments of every order, and |X_n/n-1|<=sqrt(log n/n)->0 for every realization.

The distribution of (X_n-n)/n^(1/3) converges to a symmetric sign Z. Its total variation distance to Z is exactly p_n and its Kolmogorov distance is p_n/2. Nevertheless,

    Var(X_n) = (1-p_n)n^(2/3) + n^(5/6) log n,
    log Var(X_n)/(2 log n) -> 5/12,
    Var(X_n)/n^(2/3) -> infinity.

It even has the known-form concentration bound at the larger subdiffusive scale:

    P(|X_n-E X_n| >= lambda sqrt(n/log n))
        <= exp(1/3) exp(-lambda/6)   for all lambda>=0 and n>=3.

Proof of the tail assertion. Let t=log n. The normalized ordinary atom has size r=sqrt(t)exp(-t/6)<=sqrt(3/e)<2 (maximize t exp(-t/3)); the rare atom has size t and t>=r for n>=3. For 0<=lambda<=r, the left side is at most 1 and the stated right side is at least 1. For r<lambda<=t, the left side is p_n=exp(-t/6), bounded by exp(-lambda/6). For lambda>t it vanishes. Endpoint atoms satisfy the displayed weak inequality. The variance formula follows directly from the four masses; its leading term has log exponent 5/6. Also

    E R_n^4 / Var(R_n)^2 ~ n^(1/6) -> infinity.

Thus the very uniform kurtosis input in L3 fails. This is a counterexample to an abstract implication, not a construction of iid lattice edge weights and not a counterexample to KPZ. It rules out deducing the variance exponent from weak n^(1/3) scaling plus the numerical content of a sqrt(n/log n) exponential concentration estimate alone. Lattice structure could still provide additional information.

## L5. Exact fourth-moment martingale identity and a nonzero cubic term

Let (M_k,F_k) be a finite real martingale with M_0=0 and finite fourth moments, and let D_k=M_k-M_{k-1}. Expanding the fourth power and using E[D_k|F_{k-1}]=0 gives exactly

    E M_N^4 = sum_{k=1}^N [6 E M_{k-1}^2 D_k^2
                           +4 E M_{k-1} D_k^3 + E D_k^4].

The removed linear term is 4 E M_{k-1}^3 D_k=0. The cubic term generally remains. For an explicit example, take M_1 to be a symmetric sign. Conditional on M_1=1, let D_2=-1 with probability 2/3 and D_2=2 with probability 1/3. Conditional on M_1=-1, reverse both signs. This is a martingale, but E[M_1 D_2^3]=2. Its M_2 has masses 2/3 at 0 and 1/6 at each of +/-3. Thus E M_2^4=27; discarding the cubic contribution would give 19, a strict underestimate.

For lattice FPP, enumerate the edges and take the finite Doob martingale M_k=E[T_n|F_k]-E T_n. The exact identity is valid at every finite k because T_n has finite fourth moment under Exp(1) weights (it is bounded above by the straight path's gamma-distributed weight). Closing G would require controlling the displayed total relative to Var(T_n)^2 uniformly in n and in the truncation of the edge enumeration, followed by convergence in the L^4 norm of conditional expectations. Merely orthogonalizing the second moments or multiplying conditional row estimates does not supply that bound.

## Hardest gap and next proof step

Attempt to discharge G with the known lattice theorem. Damron--Hanson--Sosoe Theorem 1.1 assumes iid nonnegative weights, d>=2, F(0)<p_c(d), and an exponential moment for the two-tail bound. If P(|T_n-E T_n|>=lambda s_n)<=A exp(-B lambda) with s_n=sqrt(n/log n), tail integration yields E|T_n-E T_n|^4 <=24 A B^(-4) s_n^4. Even granting the needed typical-scale variance lower bound c n^(2/3), this only bounds standardized fourth moments by C n^(2/3)/(log n)^2, which is unbounded as a bound. This does not prove the actual standardized moments diverge; it shows the available argument does not supply G.

By contrast, a stretched-exponential bound P(|X_n-c_n|>=t sigma_n)<=A exp(-B t^eta) at the actual standard deviation, with fixed A,B,eta>0, gives E|X_n-c_n|^4<=A B^(-4/eta) Gamma(1+4/eta) sigma_n^4. Jensen and |u+v|^4<=8(|u|^4+|v|^4) then give a uniform standardized centered-fourth-moment bound even if c_n differs from E X_n. This is exactly the scale-sensitive missing input. The checked Riemannian model has such a bound; its rotational and kernel hypotheses are not hypotheses of lattice Exp(1) FPP.

G: prove or refute sup_n E|T_n-E T_n|^4 / Var(T_n)^2 < infinity for actual iid Exp(1) undirected planar FPP. The Riemannian standard-deviation concentration theorem has extra model hypotheses and cannot discharge G. Nondegenerate n^(1/3) weak scaling is separately missing. The next concrete proof step is to bound the cross and cubic sums in L5 relative to Var(T_n)^2 uniformly over finite Doob truncations. Unconditional per-edge estimates at n/log n do not close it.
