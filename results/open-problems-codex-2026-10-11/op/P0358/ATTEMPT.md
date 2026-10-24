# P0358 — attempt, 11–12 October 2026

**Latest result (second attempt, 12 October):** the complete moving-corridor and variable-time-reset proofs in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md) strengthen the bounds recorded below to

    2sqrt(m(alpha1-1)/t*) <= a1 <= 2sqrt(m(alpha2-1)/t*).

The canonical negative tilted moment index and raw existence-tail exponent also give the law-based bracket stated there. The original proof below is retained as the first-attempt record; its weaker bounds remain valid. The exact a1 is still not identified.

## Exact target and assumptions

Source: E. Aïdékon, Y. Hu and Z. Shi, *Boundedness of discounted tree sums*, arXiv:2409.01048v2 (6 June 2025; internal date 9 June 2025), Theorem 1.2, PDF pp. 2–3; Open question 2, p. 5. Local copies: source.pdf, source.txt. Crossref identifies the published version as Acta Mathematica Sinica, English Series 42, issue 6 (2026), 1639–1661, DOI 10.1007/s10114-026-4459-4 (metadata checked; journal theorem text not checked).

Let the offspring point process be N, with intensity measure mu, and mu(R)>1. Put phi(t)=log integral exp(-tx) mu(dx). There is a smallest positive zero t=t*, and

    integral x exp(-tx) mu(dx) = m > 0,    mu((-infinity,0)) > 0.

For some 1<p=alpha1<=q=alpha2,

    integral exp(-tx)|x|^p mu(dx) < infinity,
    theta(y):=P(N((-infinity,-y])>=1) >= exp(-ty)y^(-q)

for all sufficiently large y. Finally, with Sigma=sum_{|u|=1}exp(-tV(u)),

    E[Sigma log^+ Sigma] < infinity.

Under these assumptions the source proves, on survival, almost surely,

    Theta := inf_{infinite rays xi} limsup_n V(xi_n)/sqrt(n log n) = a1 in (0,infinity).

The target is the value of a1, not this existence theorem. Finite rays in the source boundary notation do not contribute an infinite-time limsup; the displayed target is interpreted over infinite rays as in the proof.

## Results obtained here

I do NOT identify a1. I prove the explicit bounds

    sqrt(m(p-1)/t) <= a1 <= 2 sqrt(m q/t).                 (B)

These sharpen the source's qualitative estimates by varying the block size and separating the excursion slope from the endpoint increment. They follow under exactly its hypotheses. No novelty claim is made. The lower proof below is self-contained apart from the many-to-one formula and the source's global-minimum divergence; the upper proof also uses the additive-martingale convergence theorem already invoked by the source.

### Inputs from the source

The tilted probability law nu(dx)=exp(-tx)mu(dx) defines i.i.d. random-walk increments X_j, S_n=sum X_j, with E X=m and E|X|^p<infinity. Its many-to-one formula (Fact 2.1, p. 5) gives

    E sum_{|u|=n} f(V(u_1),...,V(u_n))
      = E[exp(t S_n)f(S_1,...,S_n)].

Also min_{|u|=n}V(u)->infinity on survival (source p. 2 and Section 6), and hence inf_{u in T}V(u)>-infinity there. The additive martingale W_n=sum exp(-tV(u)) is uniformly integrable and converges in L1, with its limit positive on survival, by Biggins' theorem under m>0 and the stated LlogL assumption (source pp. 18–19). Only uniform integrability is needed in the new upper proof.

### Lemma 1: polynomial lower-deviation bound

For every h<m and every beta in (0,p-1), there is n_h such that

    P(S_n<=h n) <= n^(-beta),   n>=n_h.                    (L)

Proof. Let r=min(p,2)>1. There is a finite A_r for which

    exp(-z) <= 1-z+A_r |z|^r,   z>=-1.

Indeed the ratio (exp(-z)-1+z)/|z|^r is bounded on [-1,1] by Taylor's theorem (r<=2), and on [1,infinity) by exp(-z)-1+z<=z and r>1. Its value at zero is defined by continuity/bounded extension.

Choose delta in (0,1) so small that p(1-delta)-1>beta, and set y=n^(1-delta). Define Y_j=max(X_j,-y). Then E Y_j>=m and E|Y_j|^r<=E|X_j|^r. Consequently

    E exp(-Y_j/y) <= 1-m/y+A_r E|X|^r/y^r
                    <= exp(-m/y+A_r E|X|^r/y^r).

This uses 1+v<=exp(v); its left side is positive, so the intermediate bound is legitimate even if v is negative. Exponential Markov inequality and independence give

    P(sum Y_j <=h n) <= exp(-(m-h)n/y+A_r E|X|^r n/y^r)
                       <= exp(-(m-h)n^delta/2)

for sufficiently large n, since y^(1-r)->0. Outside the event {some X_j<-y}, S_n=sum Y_j. By the union bound and the p-moment Markov inequality,

    P(S_n<=h n) <= exp(-(m-h)n^delta/2)
                   +E|X|^p n^(1-p(1-delta)).

Both terms are o(n^(-beta)), proving (L). This works for all p>1, including p>2; it does not assume regular variation or a second moment. QED.

### Proposition 2: the lower bound in (B)

Fix 0<a<sqrt(m(p-1)/t). Choose beta with a^2 t/m<beta<p-1. Choose C in the nonempty interval

    a^2/(2m^2) < C < beta^2/(2a^2t^2).                  (I)

Put r_i=n0+floor(C i^2 log i), for i>=2, and H_i=a sqrt(r_i log r_i). Ignore finitely many indices so r_i is strictly increasing. Direct asymptotics give

    r_i-r_{i-1} ~ 2C i log i,
    H_i ~ a sqrt(2C) i log i,
    H_i/(r_i-r_{i-1}) -> a/sqrt(2C) < m.

The factor sqrt(2) is retained explicitly throughout this proof. Fix K>0 and choose h strictly between a/sqrt(2C) and m. For all large i, H_i+K <= h(r_i-r_{i-1}). If S_{r_{i-1}}>=-K and S_{r_i}<=H_i, then S_{r_i}-S_{r_{i-1}}<=H_i+K. The Markov property and (L) therefore yield

    P(-K<=S_{r_i}<=H_i for all sampled i<=L)
       <= product_{i=i0}^L (r_i-r_{i-1})^(-beta).

The constraints up to r_{i0-1} supply the starting lower bound for the first retained transition; their joint probability is bounded by one. By many-to-one, the probability that any generation-r_L particle satisfies all sampled constraints is at most

    exp(t H_L) product_{i=i0}^L (r_i-r_{i-1})^(-beta).

The logarithm divided by L log L tends to

    t a sqrt(2C) - beta < 0,

because sum_{i=i0}^L log(r_i-r_{i-1})/(L log L)->1. Thus this probability tends to zero.

Any infinite ray satisfying -K<=V(xi_n)<=a sqrt(n log n) for every n>=n0 supplies such a particle for every L. Its probability is therefore zero; no compactness or interchange of infimum and limit is required. Take the countable union over integers K,n0. On survival the global lower bound holds for some K. If Theta<a, the definition of infimum supplies a ray with limsup<a, so it satisfies the upper barrier eventually; this contradicts the preceding exclusion. Hence Theta>=a almost surely. Taking a countable sequence increasing to sqrt(m(p-1)/t) proves the lower bound. QED.

### Lemma 3: retaining positive tilted mass beneath a fixed slope

For every c>m,

    Q_c=P(S_k<=ck for every k>=1)>0.

Proof. Set Z_j=X_j-c, whose mean is negative. The strong law implies R=sup_{k>=0}sum_{j=1}^k Z_j is finite almost surely. There is delta>0 with P(Z_1<=-delta)>0, since a strictly negative mean rules out Z_1>=0 almost surely. Choose a finite integer N for which P(R<=N delta)>0. Demand Z_j<=-delta for j<=N and independently demand that the subsequent walk has supremum <=N delta. The first N partial sums are nonpositive; all subsequent ones are at most -N delta+N delta=0. These independent events have positive product probability. QED.

### Proposition 4: the upper bound in (B)

Fix c>m, d>q/t and lambda>0. Define r_i=floor(lambda i^2 log i) for sufficiently large i, and b_i=r_i-r_{i-1}-1, so b_i~2lambda i log i. Consider an independent fresh subtree started at zero. Define its candidate parents at generation b_i by

    A_i={w: |w|=b_i, V(w_k)<=ck for k<=b_i,
                   V(w)>=2d log i}.

Each w in A_i is a success if it has a child u with V(u)<=d log i (positions relative to the fresh subtree root). Let nu_i count successful parents, keeping one successful child per parent. It defines a reproduction law using one entire block. Its weighted parent mass is

    W'_i=sum_{w in A_i}exp(-tV(w)),    0<=W'_i<=W_{b_i}.

By many-to-one,

    E W'_i=P(S_k<=ck for all k<=b_i, S_{b_i}>=2d log i)->Q_c>0. (M)

The convergence follows because the path-constraint events decrease to the event in Lemma 3, while the probability of S_{b_i}<2d log i tends to zero by the strong law and m>0.

Uniform integrability of W_{b_i} and domination imply uniform integrability of W'_i. There are epsilon>0, M0<infinity, rho>0 for which

    P(W'_i>=epsilon)>=rho                                (P)

for every sufficiently large i. In detail, write Q=Q_c. For large i, E W'_i>=Q/2. Choose M0 with sup_i E[W_{b_i}1_{W_{b_i}>M0}]<Q/8, increasing it to cover finitely many indices if necessary, and epsilon=Q/8. Then

    Q/2<=epsilon+M0 P(W'_i>=epsilon)+Q/8,

which gives rho=Q/(4M0), after enlarging M0 if needed. In particular no passage c->infinity is necessary.

All parents lie between 2d log i and c b_i. Their number is finite almost surely: each has weight at least exp(-tc b_i), whereas W_{b_i}<infinity almost surely. Conditionally on the tree up to generation b_i, success indicators of distinct parents are independent Bernoulli variables. Their success probabilities are theta(V(w)-d log i). The lower-tail hypothesis applies for large i, as V(w)-d log i>=d log i. Also V(w)-d log i<=c b_i. Hence, with L_i the conditional mean of nu_i,

    L_i >= i^(td)(c b_i)^(-q) W'_i = F_i W'_i,
    Var(nu_i | F_{b_i})<=L_i,
    F_i -> infinity,

since td>q and b_i~2lambda i log i. For any fixed integer K0, on {W'_i>=epsilon} and for large i, L_i>=2K0. Conditional Chebyshev gives

    P(nu_i<K0, W'_i>=epsilon)<=4/(epsilon F_i)->0.

Using (P), eventually P(nu_i>=K0)>=rho/2. Choose K0 so large that K0 rho/2>1. Each sufficiently late block reproduction law stochastically dominates the fixed law which is K0 with probability rho/2 and zero otherwise. The homogeneous Galton–Watson process with this law is supercritical (its probability generating function has derivative >1 at 1), hence survives with positive probability. Independent quantile couplings at successive vertices show that the embedded, inhomogeneous process also survives with positive probability.

Start this process at any fixed sufficiently late block index. A generation-r_{I-1} vertex exists with positive probability, since the original supercritical tree survives with positive probability. Select one such vertex using only the tree up to that generation; its future subtree is independent. Thus the construction has positive probability in the original branching random walk. The retained children form a locally finite embedded tree, with at most one per successful parent; survival supplies an infinite ray by the elementary finitely branching tree lemma. Every block path along this ray has incremental position at most ck at its first b_i steps and endpoint position at most d log i. The latter also satisfies the slope bound at the final step for large i.

Write A for the finite initial position. At endpoints,

    V(xi_{r_j})<=A+d sum_{i=I}^j log i
               <= d j log j+o(j log j).

For r_j<=n<r_{j+1},

    V(xi_n)<=V(xi_{r_j})+c(n-r_j)
             <=(d+2c lambda+o(1)) j log j.

Uniformly in such n, sqrt(n log n)>=(sqrt(2lambda)+o(1))j log j. Therefore this ray satisfies

    limsup_n V(xi_n)/sqrt(n log n)
       <=(d+2c lambda)/sqrt(2lambda).                     (U)

This occurs with positive probability. The deterministic-on-survival conclusion of the source Theorem 1.2 consequently implies that a1 is bounded above by the right side of (U). This uses its existence conclusion, not an unproved upgrade from a finite-horizon path.

Set z=sqrt(2lambda)>0. The bound is d/z+c z, whose minimum is 2sqrt(cd), attained at lambda=d/(2c). Indeed its square minus 4cd is (d/z-cz)^2, and the sum is nonnegative. These real-algebra steps are the target of Bounds.lean. Let c decrease to m and d decrease to q/t along countable sequences. Continuity proves a1<=2sqrt(mq/t). QED.

## Scaling check (previous result, rechecked)

For a spatial dilation V_c=cV, c>0, the tilted parameter is t_c=t/c, its law is the pushforward of nu by x->cx, and m_c=cm. The moment and LlogL conditions are preserved. The tail lower bound becomes c^q exp(-t_c y)y^(-q); any sufficiently small increase q' > q absorbs its prefactor, retaining the theorem class and p<=q'. The minimal-zero property follows from phi_c(s)=phi(cs). Pathwise the ray functional is cTheta, so a1(cN)=ca1(N). Thus a distribution-free numerical a1 is impossible. This is a consistency restriction, not a counterexample to the source question, which allows dependence on the law. Both bounds (B) have the correct units.

## A concrete admissible family (verification)

Take t=1, p0>1, epsilon in (0,1), and b>0 large. Let the tilted law nu have mass 1-epsilon at b and mass epsilon at -Y, where Y has density p0 y^(-p0-1) on [1,infinity). Use a Poisson offspring point process with finite intensity mu(dx)=exp(x)nu(dx). Its mean total number is

    M=(1-epsilon)exp(b)+epsilon E exp(-Y)>1,
    m=(1-epsilon)b-epsilon p0/(p0-1)>0

when b is sufficiently large. At t=1 the Laplace integral is 1. For 0<s<1, Jensen gives integral exp(-sx)mu(dx)=E_nu exp((1-s)X)>=exp((1-s)m)>1. For s>1 it is infinite because of the Pareto negative tail. Thus 1 is the smallest positive zero, and negative intensity is positive.

The tilted moment of order alpha1 is finite whenever 1<alpha1<p0. If A(y)=mu((-infinity,-y]) then

    A(y)=epsilon p0 integral_y^infinity exp(-z)z^(-p0-1)dz
         ~epsilon p0 exp(-y)y^(-p0-1).

For the Poisson process theta(y)=1-exp(-A(y))~A(y), so the source lower bound holds with every alpha2>p0+1. The asymptotic follows by substituting z=y+w and dominated convergence.

To check LlogL, condition on the finite Poisson offspring count N. Write its positive weights w_i=exp(-X_i), with marks drawn from mu/M. Convexity of x log x gives, when N>=1,

    Sigma log^+Sigma <= sum_i w_i log^+w_i + Sigma log^+N.

For Sigma>=1, apply Jensen to the average Sigma/N; for Sigma<1 the left side is zero. Expectations of the first term equal integral exp(-x)log^+(exp(-x))mu(dx)=epsilon E Y<infinity. For the second term, E[w_i]=1/M and E[N log^+N]<infinity, so its expectation is finite. Every hypothesis is therefore verified.

Taking limits alpha1 up to p0 and alpha2 down to p0+1 in (B) gives for this family

    sqrt(m(p0-1)) <= a1 <= 2sqrt(m(p0+1)).

This remains a bound, not an exact special-case solution.

### Corollary 5: t* and tilted drift do not determine a1

This is stronger than the previous scaling-only restriction. In the family above fix epsilon=1/10 and t=1. Model A has p0=5/2, b=2. Model B has p0=16, b=29/15. Both have exactly

    m=(1-epsilon)b-epsilon p0/(p0-1)=49/30.

Their mean total offspring is greater than 1: M>=(9/10)exp(b)>=(9/10)(1+b)>1 for both positive b. All other assumptions were verified for the general family above. Model A's upper bound and Model B's lower bound give

    a1(A) <= 2sqrt((49/30)(7/2))=sqrt(14(49/30)),
    a1(B) >= sqrt((49/30)(16-1))=sqrt(15(49/30)).

Since m=49/30>0 and 15m>14m, strict monotonicity of square root gives a1(B)>a1(A). Thus no formula in t* and m alone can answer the source question. In particular t*a1 is not universal even after fixing t*, and a universal coefficient multiplying sqrt(m/t*) is impossible. This is not a counterexample to Theorem 1.2 or a solution of Open question 2: that question permits dependence on the whole law.

## Recorded checks

`numerical_checks.py` completed successfully; numerical_checks.json stores its output. It checked 1,000 seeded positive parameter choices for the lower-bound feasibility interval, and six lambda offsets per case for the optimized upper coefficient. It also checked the block normalization at i=100, 10^4, 10^6 and 10^8 for C=0.2,1,5; convergence is slow because log log i/log i is still visible. The Poisson example (p0=2.5, epsilon=0.1, b=2) has m=49/30, mean offspring approximately 6.67429, and bounds approximately 1.56525 and 4.78191. Factored 50-digit quadrature at y=10,100,1000 verifies the tail asymptotic ratios. The coefficient-one source tail lower bound with q=4 fails at y=10 but holds at these two larger sample points; the proof, not those samples, establishes eventual validity.

`lake env lean ~/brain_workers/TRIO_1011/op/P0358/Bounds.lean` was run from ~/lean_verify, via run_lean.py with a 3600-second timeout. Exit code 0. Both block_bound and block_equality report only axioms [propext, Classical.choice, Quot.sound]. There is no sorry, native_decide, or additional axiom. The real analysis import is Mathlib.Analysis.Real.Sqrt, with explicit tactic imports rather than import Mathlib. Output and runtime are in lean_check.txt. These are kernel-checked algebraic certificates; the probabilistic bounds remain conventional complete mathematical proofs.

## Referee audit and precise remaining gap

1. **Normalization:** sqrt(r_i log r_i)~sqrt(2C)i log i. No omission of sqrt(2) is allowed. Numerical checks test this slow asymptotic separately.
2. **Quantifiers:** exclusion is for every infinite ray, via expected counts at sampled generations and countable K,n0; it is not inferred from the minimum at a single generation.
3. **Moment range:** the deviation proof uses r=min(p,2), while the large-jump union bound uses p. No finite variance is silently assumed.
4. **Upper construction:** the endpoint budget d and within-block slope c are distinct. The positive-mass argument uses uniform integrability; mere E W_n=1 would not suffice.
5. **Independence:** Bernoulli success indicators are independent only conditional on the full parent generation. Descendants used in different block subtrees are disjoint.
6. **Finite branches:** candidate counts are finite because candidate positions have a deterministic upper bound and the weighted sum is finite. No unrestricted compactness assumption is needed.
7. **Positive-probability versus almost-sure:** the upper bound is promoted using the already proved deterministic a1 theorem, not by an unsupported assertion that every root succeeds.
8. **Scaling:** if c<1, the numerical coefficient in the raw-tail bound requires an arbitrarily larger exponent. It is not literally preserved with coefficient one and the same alpha2.
9. **Finite simulations:** experiments below inspect deterministic coefficient limits only. They do not simulate a truly infinite ray, and cannot establish a1.
10. **Formal scope:** Lean checks only the finite optimization algebra, not the random-walk, martingale, or branching arguments.

The first-attempt gap was the interval between the two constants in (B). The tilted p-moment controls a block lower-deviation probability, whereas the one-child reset construction uses the raw offspring tail exponent q and pays an accumulated endpoint budget. These bounds cannot be equated: p and q are merely admissible witnesses, not canonically equal tail parameters. Corollary 5 shows that drift and tilt alone cannot suffice; the tilted tail or other law data must enter.

## Current remaining gap after the second attempt

The complete new proofs are in SECOND_ATTEMPT.md. A moving-corridor bootstrap doubles the lower bound, and a variable-time stopping-line reset construction subtracts one from the upper exponent. Thus the current bracket is

    2sqrt(m(alpha1-1)/t*) <= a1 <= 2sqrt(m(alpha2-1)/t*).

Canonical law parameters replace alpha1 with the critical negative tilted moment index p_- and alpha2 with the eventual raw-tail exponent q_*, giving the corresponding bracket. A Tonelli argument proves q_*>=p_-+1, so merely optimizing witnesses cannot close it. In the fully checked Poisson-Pareto family the remaining squared-cost gap is p0-1 versus p0, and the exact a1 is unknown even there. The second approach supplies an exact Poisson finite-horizon survival recursion but no solved critical asymptotic. All lower/upper proofs and finite formal checks survived the recorded referee audit; none gives a full solution or an exact-value conjecture promoted to a theorem.
