# A stationary variance reduction and a persistent initial mixture

## 1. States and notation

Use a full Markov state for each FIFO queue. One possible state consists of the queue length, the age and residual requirement of the job in service, and the ordered requirements of the waiting jobs. The empty state is a separate point. This space can be embedded in the Polish space

\[
 E=\{\varnothing\}\;\sqcup\;
 \bigsqcup_{q\geq1}\bigl(\{q\}\times[0,\infty)^{q+1}\bigr),
\]

with the disjoint-union topology. The coordinates on the component with length q are age, residual requirement, and q-1 waiting requirements. Allowing boundary points in this ambient space is harmless. Alternatively, an age-based state with unexposed waiting requirements can be used. Queue length is always a coordinate; it is not assumed to be a Markov state by itself.

Write X^N(t) for the full N-server state. For a measurable f:E→[0,1], set

\[
 M_f^N(x)=\frac1N\sum_{i=1}^N f(x_i),\qquad
 H_{f,t}^N(x)=\mathbb E_x M_f^N(X^N(t)).
\]

Here the subscript x specifies the entire deterministic initial state, and the expectation averages the subsequent arrivals, routing choices, and service randomness. All the variables below are bounded, so no moment assumption on queue lengths is involved.

## 2. The term retained by a random initial state

**Proposition 1.** Let μ_N be any distribution of the full initial state, independent of the future driving randomness. Then

\[
\begin{split}
 \operatorname{Var}_{\mu_N}\bigl(M_f^N(X^N(t))\bigr)
 ={}&\int \operatorname{Var}_x\bigl(M_f^N(X^N(t))\bigr)\,\mu_N(dx)\\
 &+\operatorname{Var}_{\mu_N}\bigl(H_{f,t}^N(X^N(0))\bigr).
 \tag{1}
\end{split}
\]

In particular, suppose Π_N is invariant and

\[
 \sup_x\operatorname{Var}_x\bigl(M_f^N(X^N(t))\bigr)
 \leq\varepsilon_{N,f}(t).
 \tag{2}
\]

Then

\[
0\leq
 \operatorname{Var}_{\Pi_N}(M_f^N)
 -\operatorname{Var}_{\Pi_N}(H_{f,t}^N)
 \leq\varepsilon_{N,f}(t).
\tag{3}
\]

**Proof.** Put Y=M_f^N(X^N(t)) and Z=X^N(0). By the Markov construction, E[Y|Z]=H_{f,t}^N(Z). Expand

\[
 Y-EY=(Y-E[Y|Z])+(E[Y|Z]-EY).
\]

The expectation of the cross product is zero, because the first summand has conditional mean zero given Z. Taking the expectation of the square gives (1). For an invariant initial law Π_N, Y and M_f^N(Z) have the same distribution. The first term on the right of (1) lies between zero and the bound in (2), which proves (3). ∎

Thus a bound uniform over deterministic initial states controls only the first term in (1). It cannot be integrated into the same bound for a random initial state without controlling the second term.

## 3. The precise concentration statement that would suffice

**Proposition 2.** Suppose Π_N is exchangeable and its first marginal converges weakly to a probability π on E. The following are equivalent:

1. For every fixed k, the first k coordinates under Π_N converge weakly to π^{⊗k}.
2. For every bounded continuous f:E→[0,1], Var_{Π_N}(M_f^N) tends to zero.

If the deterministic-start estimate (2) holds for each such f at a fixed positive t with ε_{N,f}(t)→0, then these conditions are also equivalent to

\[
 \operatorname{Var}_{\Pi_N}(H_{f,t}^N)\longrightarrow0
 \quad\text{for every bounded continuous }f:E\to[0,1].
 \tag{4}
\]

**Proof.** Exchangeability gives the exact identity

\[
 \operatorname{Var}_{\Pi_N}(M_f^N)
 =\frac1N\operatorname{Var}_{\Pi_N}(f(X_1))
 +\frac{N-1}{N}\operatorname{Cov}_{\Pi_N}(f(X_1),f(X_2)).
 \tag{5}
\]

Indeed, expand the variance of the sum defining M_f^N, separate its N diagonal terms from its N(N-1) ordered off-diagonal terms, and use exchangeability. Convergence of the two-coordinate marginal to π⊗π makes the covariance tend to zero. The diagonal term is at most 1/(4N). This proves that item 1 implies item 2.

Conversely, first-marginal convergence gives

\[
 \mathbb E_{\Pi_N}M_f^N\longrightarrow\pi f.
\]

Together with item 2 this proves M_f^N→πf in L² and hence in L¹. For fixed k and bounded continuous f_1,…,f_k taking values in [0,1], telescoping products yields

\[
 \left|\prod_{j=1}^k M_{f_j}^N-\prod_{j=1}^k\pi f_j\right|
 \leq\sum_{j=1}^k|M_{f_j}^N-\pi f_j|.
 \tag{6}
\]

The expectation of the right side tends to zero.

To relate the left side to tagged servers, sample k independent uniform indices from {1,…,N}, independently of the state. Conditional on the state, the expected product evaluated at these indices is ∏_j M_{f_j}^N. Conditional on all indices being distinct, exchangeability makes its unconditional expectation equal to E_{Π_N}∏_j f_j(X_j). Each product lies in [0,1], so

\[
 \left|
 \mathbb E_{\Pi_N}\prod_{j=1}^k M_{f_j}^N
 -\mathbb E_{\Pi_N}\prod_{j=1}^k f_j(X_j)
 \right|
 \leq\mathbb P(\text{a repeated index})
 \leq\frac{k(k-1)}{2N}.
 \tag{7}
\]

The last inequality is the union bound over the k(k-1)/2 pairs of sampled positions. Equations (6) and (7) prove convergence of all these product expectations to ∏_j πf_j.

For completeness, the joint laws are tight: weak convergence of the first marginal makes the family of first marginals tight on the Polish space E; exchangeability and a union bound then give tightness of each k-coordinate family. Every subsequential limit therefore exists along a further subsequence and has the product expectations just computed. Products of bounded continuous one-coordinate functions determine a probability law on a finite product of Polish spaces. One way to see this is to approximate indicators of open sets by bounded continuous functions using distance to their complements, then use monotone convergence on rectangles and the uniqueness theorem for measures on the rectangle generating class. Consequently each subsequential limit is π^{⊗k}, proving item 1.

Finally, (3) and ε_{N,f}(t)→0 show that the variances in item 2 and (4) differ by a quantity tending to zero. ∎

This reduction assumes convergence of the one-server marginal. It neither proves that convergence nor identifies π. An estimate for functions of queue length alone supplies only the corresponding queue-length reduction, not the full-state conclusion.

### A quantitative sufficient bound for the remaining term

The same calculation applies with a time t_N that depends on N. Suppose that for a fixed f there are measurable sets A_N, constants c_N∈[0,1], and nonnegative numbers δ_N, η_N such that

\[
 \Pi_N(A_N^c)\leq\eta_N,\qquad
 \sup_{x\in A_N}|H_{f,t_N}^N(x)-c_N|\leq\delta_N.
 \tag{14}
\]

Then

\[
 \operatorname{Var}_{\Pi_N}(M_f^N)
 \leq\varepsilon_{N,f}(t_N)+\delta_N^2+\eta_N,
 \tag{15}
\]

provided the deterministic-start bound (2) holds at t_N. Indeed,

\[
 \operatorname{Var}_{\Pi_N}(H_{f,t_N}^N)
 \leq\mathbb E_{\Pi_N}(H_{f,t_N}^N-c_N)^2
 \leq\delta_N^2+\eta_N,
\]

where the complement of A_N contributes at most η_N because both H and c_N lie in [0,1]. Combining this with (3) proves (15). If the three terms on the right tend to zero for every bounded continuous f:E→[0,1], Proposition 2 supplies full-state chaos once first-marginal convergence is known. Estimate (14), on a set of large stationary probability, is therefore a sufficient additional forgetting statement. No such estimate is proved here.

## 4. A counterexample to dropping the second term

**Proposition 3.** Fix 0<λ<1 and d≥2. Use deterministic service requirements equal to one, FIFO unit-rate service, and the shortest-of-d routing rule. At time zero choose an independent fair bit B. If B=0, every server is empty. If B=1, every server contains one job just starting service, of requirement one and age zero. This is an exchangeable initial law on full queue states, with a service law of mean one.

Let I_i(t)=1_{\{Q_i(t)=0\}} and M(t)=N^{-1}∑_i I_i(t). For any fixed 0≤t<1 and N≥max(d,2),

\[
 \operatorname{Var}(M(t))\geq\frac14 e^{-2\lambda d t},
 \tag{8}
\]

and

\[
 \operatorname{Cov}(I_1(t),I_2(t))
 \geq\frac{N e^{-2\lambda d t}-1}{4(N-1)}.
 \tag{9}
\]

Consequently, at every fixed t<1,

\[
 \liminf_{N\to\infty}\operatorname{Cov}(I_1(t),I_2(t))
 \geq\frac14 e^{-2\lambda d t}>0.
 \tag{10}
\]

Both sampling with and without replacement satisfy these conclusions.

**Proof.** First use sampling without replacement. An arrival samples server i with probability d/N. Poisson thinning shows that the arrivals whose sampled set contains i form a Poisson process of rate λd. A server that starts empty and is never sampled receives no jobs and remains empty. Hence, writing

\[
 p_N(t)=\mathbb P(I_i(t)=1\mid B=0),
\]

exchangeability and the no-sampling event give p_N(t)≥e^{-λdt}.

When B=1, no initial job can finish before time one. FIFO prevents later arrivals from displacing it. Thus I_i(t)=0 for every i and t<1, and

\[
 \mathbb E[M(t)\mid B]=p_N(t)(1-B).
\]

By conditional variance,

\[
 \operatorname{Var}(M(t))
 \geq\operatorname{Var}(\mathbb E[M(t)\mid B])
 =\frac14 p_N(t)^2\geq\frac14e^{-2\lambda dt}.
\]

This proves (8). Apply the exchangeability identity (5) to the indicators I_i(t), and solve for their off-diagonal covariance. Since Var(I_1(t))≤1/4,

\[
 \operatorname{Cov}(I_1(t),I_2(t))
 =\frac{N\operatorname{Var}(M(t))-\operatorname{Var}(I_1(t))}{N-1}
 \geq\frac{N e^{-2\lambda dt}-1}{4(N-1)}.
\]

Taking the lower limit proves (10).

With replacement, the rate of arrivals sampling i at least once is

\[
 \lambda N\bigl[1-(1-1/N)^d\bigr]\leq\lambda d,
\]

by the union bound on the d sampled positions. Thus the same lower bound on p_N(t) holds, and the remaining proof is unchanged. ∎

The example is not stationary. It disproves an inference about random initial laws, not the stationary independence conjecture. In particular, it cannot contradict a correctly stated deterministic-start estimate.

## 5. Independent check of a positive covariance bound

The nonvanishing covariance can also be checked directly, without conditional variance or (5). Set

\[
 q_N(t)=\mathbb P(I_1(t)=I_2(t)=1\mid B=0).
\]

If neither server is ever sampled, both remain empty. Without replacement the rate of arrivals sampling at least one of servers 1 and 2 is

\[
 h_N=\lambda N\left[\frac dN+\frac dN-
             \frac{d(d-1)}{N(N-1)}\right]
 =\lambda d\frac{2N-d-1}{N-1}\leq2\lambda d.
 \tag{11}
\]

The intersection probability in brackets is d(d-1)/(N(N-1)): sample one specified server and then the other from the remaining N-1 servers. The same upper bound h_N≤2λd holds with replacement by the union bound on the d positions. Poisson thinning therefore gives q_N(t)≥e^{-2λdt}. Since the B=1 branch contributes zero emptiness probability,

\[
 \operatorname{Cov}(I_1(t),I_2(t))
 =\frac12q_N(t)-\frac14p_N(t)^2
 \geq\frac12e^{-2\lambda dt}-\frac14.
 \tag{12}
\]

Take

\[
 t_* =\min\left\{\frac12,\frac{1}{8\lambda d}\right\}.
\]

Then 0<t_*<1 and 2λdt_*≤1/4. The elementary bound e^{-x}≥1-x gives, for every N≥max(d,2),

\[
 \operatorname{Cov}(I_1(t_*),I_2(t_*))
 \geq\frac12\left(1-\frac14\right)-\frac14
 =\frac18.
 \tag{13}
\]

The bound on h_N can itself be checked without inclusion-exclusion: the probability of sampling either server is at most the sum of the two probabilities d/N. This gives h_N≤2λd immediately, including the boundary case N=d. Thus the positive constant in (13) does not rely on an asymptotic expansion or on the exact expression in (11).

At t=0, direct evaluation gives I_i(0)=1-B, hence Var(M(0))=Cov(I_1(0),I_2(0))=1/4. Both (8) and (9) are equalities there. The strict restriction t<1 is essential to the argument: after time one, the B=1 branch can contain empty queues.
