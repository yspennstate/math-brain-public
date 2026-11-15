# A necessary loss for independent-set amplification

Write alpha(G) for the largest independent-set size. All logarithms are natural. This result concerns amplification at arbitrary targets, including targets near the random optimum. It does not establish a computational obstruction at the large-degree overlap barrier.

## 1. Quantitative feasibility bound

Fix d>0 and let G_n have law G(n,d/n). Put

    mu_d = (2/3)d^3 exp(-4d),
    c_* = exp(-320)/16,
    C_d = 40/mu_d.

Let k_n be any integer sequence such that, eventually,

    P(alpha(G_n) < k_n) >= 1/3.                              (1)

For every sequence of nonnegative integers r_n=o(n), eventually

    P(alpha(G_n) < k_n-r_n)
        >= c_* exp(-C_d r_n^2/n).                           (2)

There is no computability hypothesis on k_n in this statement. In particular, (2) bounds the failure of every algorithm, even one with unlimited running time, that must return k_n-r_n independent vertices. If such failure is at most n^(-L), for a fixed L>0, then

    r_n >= sqrt((L/(2 C_d)) n log n)                         (3)

eventually, provided r_n=o(n). A loss r_n=o(sqrt(n log n)) cannot suffice.

The representation by four-vertex tree components below is the mechanism in Section 5, Theorem 12 and Lemma 13, of Tom Bohman and Jakob Hofstad, *Two-Point Concentration of the Independence Number of the Random Graph*, Forum of Mathematics, Sigma 12 (2024), e24, https://doi.org/10.1017/fms.2024.6 . It is reproduced with its elementary counting proof. The quantitative lower-tail estimate and its implication for amplification are the application needed here; no novelty claim is made for the component mechanism.

### 1.1. Many four-vertex tree components

Let T count connected components that are trees on four vertices. For each four-set S, let W_S indicate that S is such a component. Write p=d/n. There are sixteen labelled trees on S, each with three edges and three absent internal pairs. All 4(n-4) external pairs must also be absent. Thus

    a_n := E W_S = 16 p^3(1-p)^(4n-13),
    E T = binom(n,4) a_n = (mu_d+o(1)) n.                   (4)

The sixteen trees can be counted without invoking a general tree formula: there are four stars, one for each centre, and twelve paths, one for each ordering of the four vertices modulo reversal.

Distinct intersecting four-sets cannot both be vertex sets of components, so their indicators have nonpositive covariance. If S and U are disjoint, multiplying the two individual event probabilities counts the sixteen pairs joining S to U twice. The joint event counts them once. All other constraints are disjoint, giving

    E(W_S W_U) = a_n^2(1-p)^(-16).

Consequently

    Var(T) <= E T + (E T)^2 ((1-p)^(-16)-1) = O_d(n),       (5)

because (1-d/n)^(-16)-1=O_d(1/n). For example the mean value theorem applied to (1-x)^(-16) on 0<=x<=1/2 proves this bound. Equation (4) implies E T>=3 mu_d n/4 eventually. Chebyshev's inequality and (5) therefore show

    P(T < mu_d n/2) = O_d(1/n).                            (6)

Always T<=n/4.

### 1.2. Exposing everything except the tree shapes

Expose the unordered collection of vertex sets of all four-vertex tree components and the entire graph H on the remaining vertices. Call this information F. For each possible value of F, all ways of inserting one labelled tree on each exposed four-set have equal probability: they have the same total numbers of present and absent pairs. Every insertion has exactly the exposed components and remainder, so this describes the full conditional fibre.

The shapes are therefore conditionally independent uniform choices from sixteen trees. A star has independence number three; a path has independence number two. If t=T and Z=alpha(H)+2t, then

    alpha(G_n) = Z+B,      (B | F) ~ Bin(t,1/4).            (7)

Both t and Z are determined by F. Computing F or alpha(H) is not required by this argument.

### 1.3. A binomial lower-tail lemma

Let B~Bin(t,1/4), with t>=1 an integer. Suppose h is an integer and

    P(B<=h) >= 1/6.

If r>=0 is an integer satisfying

    Delta := (r+4 sqrt(t))/t <= 1/8,                        (8)

then

    P(B<=h-r) >= (3/4) exp(-320-20r^2/t).                  (9)

First, E B=t/4 and Var(B)=3t/16. If h<t/4-2 sqrt(t), Chebyshev gives P(B<=h)<=3/64<1/6. Therefore

    h >= t/4-2 sqrt(t).                                    (10)

Set q=1/4 and q'=q-Delta. By (8), 1/8<=q'<q. Under the auxiliary law Q=Bin(t,q'), let

    E = {b integer: |b-tq'|<sqrt(t)}.

Chebyshev and Var_Q(B)<=t/4 give Q(E)>=3/4. Every b in E satisfies

    b < tq'+sqrt(t)=t/4-r-3 sqrt(t) <= h-r.                (11)

The exact likelihood ratio between P=Bin(t,q) and Q at b is

    log(P(b)/Q(b))
       = -t D(q'||q)+(b-tq') theta,
    theta = log(q(1-q')/(q'(1-q))),

where D(x||y)=x log(x/y)+(1-x)log((1-x)/(1-y)). The elementary bound log u<=u-1 gives

    D(q'||q) <= (q'-q)^2/(q(1-q)) <= 6 Delta^2.            (12)

For completeness, the first inequality follows by replacing both logarithms in D: the resulting sum is (q'-q)^2/[q(1-q)]. Also

    theta = integral from q' to q of 1/(x(1-x)) dx
           <= 16 Delta,                                  (13)

since x(1-x)>=7/64>1/16 on [1/8,1/4]. For b in E, (12)--(13) imply

    log(P(b)/Q(b)) >= -6t Delta^2-16 sqrt(t)Delta.

Write u=r/sqrt(t), so sqrt(t)Delta=u+4. As u>=0,

    6(u+4)^2+16(u+4)
       <= 10(u+4)^2 <= 20u^2+320.                         (14)

The first inequality uses u+4>=4; the second is (u+4)^2<=2u^2+32. Summing P(b)>=exp(-320-20r^2/t)Q(b) over E, and using (11), proves (9). The window is strictly defined so that its Chebyshev complement includes equality; no rounding of its endpoints is needed.

### 1.4. Integrating the conditional estimate

Set f(F)=P(alpha(G_n)<k_n | F). Equation (1) gives E f>=1/3. Since 0<=f<=1,

    P(f>=1/6) >= 1/6.                                     (15)

Indeed E f<=1/6+P(f>=1/6). Combining (6) and (15), the event

    A = {f>=1/6, T>=mu_d n/2}

has probability at least 1/12 for all sufficiently large n. On A put t=T, Z as in (7), and h=k_n-1-Z. Then f=P(B<=h | F)>=1/6.

Put a=mu_d/2>0. On A, a n<=t<=n/4. Uniformly in this range,

    (r_n+4 sqrt(t))/t <= r_n/(a n)+4/sqrt(a n) -> 0.

Thus (8) holds eventually for all histories in A. By (9),

    P(alpha(G_n)<k_n-r_n | F)
        >= (3/4)exp(-320-20r_n^2/t)
        >= (3/4)exp(-320-(40/mu_d)r_n^2/n)

on A. Multiplication by P(A)>=1/12 proves (2) with c_*=exp(-320)/16. No additive O(1/n) error is subtracted from this possibly very small tail: a fixed positive mass of good histories is selected first.

Finally, if the left side of (2) is at most n^(-L), taking logarithms gives

    C_d r_n^2/n >= L log n+log c_*.

For sufficiently large n the right side is at least (L/2)log n, proving (3).

## 2. A polynomial-time example showing the loss is necessary

Fix d=1/2. There is a polynomial-time computable integer target k_n and a deterministic algorithm A of polynomial worst-case time such that

    P(A(G_n) finds at least k_n independent vertices) -> 1/2,
    P(alpha(G_n)<k_n) -> 1/2.                              (16)

For this same target, every algorithm returning at least k_n-r_n vertices with failure at most n^(-L), where L>0 is fixed and r_n=o(n), must have r_n=Omega_L(sqrt(n log n)). This follows immediately from Section 1 and the second limit in (16). It rules out an improvement to o(sqrt(n log n)) for a theorem covering all fixed rational d>0 and all computable targets, even with constant starting success.

### 2.1. The imported subcritical central limit theorem

Boris Pittel, *On tree census and the giant component in sparse random graphs*, Random Structures & Algorithms 1 (1990), 311--342, https://doi.org/10.1002/rsa.3240010306 , proves the following subcritical central limit theorem. For 0<d<1, let beta>0 solve beta exp(beta)=d and put

    a_d = (beta+beta^2/2)/d,
    sigma_d^2 = a_d-(d+1)beta^2/d^2.

Then

    (alpha(G_n)-a_d n)/(sigma_d sqrt(n))
        converges in distribution to N(0,1).               (17)

This is a published input. The publisher's abstract, opened for this work, states the Gaussian limit and these exact mean and variance formulas; the full paper's proof was not accessible through that page. No theorem number or quantitative moderate-deviation estimate is attributed to it.

The variance is strictly positive in the range used here. Substituting d=beta exp(beta) gives

    sigma_d^2 = exp(-2 beta)[exp(beta)(1-beta/2)-1].         (18)

For 0<d<1, 0<beta<1. The bracket vanishes at beta=0 and has derivative exp(beta)(1-beta)/2>0 on (0,1), proving positivity. Also a_d=exp(-beta)(1+beta/2) lies strictly between zero and one: its derivative is -exp(-beta)(1+beta)/2<0 and its value at zero is one.

### 2.2. Computing the target

Take d=1/2 and write a=a_(1/2). Compute a rational lower approximation a_n with 0<=a-a_n<=n^(-2). Set k_n=max{1,floor(n a_n)}, modifying finitely many initial terms to keep k_n<=n. Then k_n-a n=O(1), so (17), including its continuity at zero, yields

    P(alpha(G_n)<k_n) -> 1/2,
    P(alpha(G_n)>=k_n) -> 1/2.                              (19)

Here is an explicit polynomial-time method for the approximation. Let g(x)=x exp(x)-1/2 on [0,1]. It is increasing, g'(x)>=1, and its root beta is in (0,1). Compute g(x) to error at most eta at each rational bisection point, using the exponential series. If the resulting interval excludes zero, retain the indicated half interval. If it contains zero, |g(x)|<=2 eta and the mean value theorem locates beta within 2 eta of x; intersect that interval with the previous bracket and stop. Taking eta=n^(-2)/100, O(log n) bisections either reach width at most 4 eta or take this early stopping branch. For x in [0,1], the tail of sum_(j=0)^J x^j/j! is at most 2/(J+1)!; J=O(log n) suffices. All rational operations have polynomial bit cost. Since a=2 beta+beta^2 and this map has derivative at most four on [0,1], the lower endpoint of the final beta bracket yields the required a_n (with more accuracy than needed).

### 2.3. A solver with polynomial worst-case time

Let b_n=64 ceil(log_2 n) for n>=2. Find all connected components of the input graph. If some component has more than b_n vertices, return the empty set. Otherwise enumerate all vertex subsets of each component, retain a largest independent subset, and return their union. This is a maximum independent set whenever the cutoff does not trigger. On every input the time is bounded by a polynomial: 2^(b_n)<=2^64 n^64, and component and independence checks add polynomial factors.

To bound the cutoff probability, explore the component of a fixed vertex. At each processed vertex the number of newly discovered neighbours is conditionally a binomial variable with at most n trials and probability 1/(2n). By adding independent dummy trials, and using fresh trials at each step, these numbers can be coupled below independent Bin(n,1/(2n)) variables. Padding after exploration has ended does not affect this domination.

If the component contains at least m vertices, the first m-1 processed vertices must discover at least m-1 vertices in total. Their dominating total Y has law Bin(n(m-1),1/(2n)). Its exponential moment satisfies

    E 2^Y = (1+1/(2n))^(n(m-1)) <= exp((m-1)/2).

Thus Markov's inequality gives

    P(component size >=m)
        <= exp(-(log 2-1/2)(m-1)).                         (20)

The event of a component of more than b_n vertices uses m=b_n+1. A union bound over starting vertices bounds it by

    n exp(-(log 2-1/2)b_n)=o(1).                           (21)

For an elementary check of the exponent, log 2>=2/3 follows from the first term of its atanh series at 1/3, while log 2<=1. Hence log 2-1/2>=1/6 and b_n>=64 log n. The right side of (21) is at most n^(1-64/6), which tends to zero. The solver therefore finds the maximum independent set with probability 1-o(1). Combining with (19) proves (16).

## 3. Scope at the overlap barrier

The general tail bound in Section 1 holds for every fixed d>0, including large d. Its hypothesis is a constant probability that the target is infeasible. It does not apply automatically to a density such as (1+epsilon)log(d)/d, which may lie a linear distance below the typical optimum.

The explicit algorithmic example uses d=1/2 and a target near the optimum; it is outside the large-d regime in T284. It establishes that the round-4 amplification theorem's O(sqrt(n log n)) order cannot be improved uniformly over the full parameter and target class that theorem covers. Exact-target amplification is false in that class for feasibility reasons. Improving the loss at a fixed density below the optimum remains possible. No overlap-gap-to-hardness implication, named average-case reduction, or algorithm crossing the large-d barrier is proved.
