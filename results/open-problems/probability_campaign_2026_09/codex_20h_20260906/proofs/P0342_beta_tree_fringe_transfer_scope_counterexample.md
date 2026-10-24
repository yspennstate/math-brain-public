# P0342: A global finite-tree perturbation obstructs an unrestricted fringe CLT transfer

Status: author-checked scope counterexample and partial answer to Aldous-Janson Open Problem 12. The example has a zero-variance Gaussian limit on the infinite fringe process. If the intended meaning of CLT requires strictly positive limiting variance or restricts functionals to a fixed finite neighborhood, that narrower question is not settled by this example. No independent review or novelty claim.

Source: Aldous-Janson, arXiv:2303.02529v3, PDF pages 44-45, with split law on PDF page 4. https://arxiv.org/abs/2303.02529v3. The source asks whether a CLT for a given functional along the stationary infinite fringe process necessarily transfers to the corresponding sum over leaves of the finite tree. Its preceding text mentions suitable functionals but imposes no quantitative locality or uniform error condition in the numbered question.

## Explicit bounded functional

For a finite full binary tree with n leaves, its original root is the unique degree-two vertex when n is at least two. Thus the original root split is recoverable after choosing a leaf as the distinguished root. Let $R_n$ be the smaller of the two original root-clade sizes, let $r_n=\lfloor\sqrt n\rfloor$, and for n at least nine put

$$B_n=\mathbf1_{\{R_n\le r_n\}},\qquad p_n=\mathbb P(B_n=1).$$

Define a single deterministic functional on finite or infinite leaf-rooted binary trees by

$$\Phi(T)=n^{-1/4}(B_n(T)-p_n)\quad\hbox{if T is finite with n at least nine leaves},$$

and $\Phi(T)=0$ for infinite T or smaller finite trees. This does not use external randomness. It is the same function at every n; n is a measurable statistic of its input tree. It is bounded by one.

In the usual local topology on these bounded-degree rooted trees, this functional is continuous. Every finite tree is isolated after a large enough rooted ball is specified, including the degrees of its boundary leaves. If finite trees converge locally to an infinite tree, their leaf counts must tend to infinity: a full binary tree with n leaves has exactly $2n-1$ vertices. Consequently $|\Phi(T)|\le n^{-1/4}\to0$ along every such sequence. The global split indicator need not itself be continuous at infinity because its prefactor tends uniformly to zero.

## The two sums behave differently

The stationary fringe tree and all its leaf rerootings are infinite. Thus $\Phi(T_i)=0$ almost surely for all i. Every centered normalized fringe sum is exactly zero, a degenerate Gaussian limit.

For the finite tree, rerooting at a different leaf leaves n and its unique degree-two original root unchanged. Hence every leaf has the same functional value and

$$\frac1{\sqrt n}\sum_{i=1}^n\Phi(T_i^{(n)})
=n^{1/4}(B_n-p_n). \tag{1}$$

Each summand has expectation zero already, so both centering by the infinite-fringe mean and centering by the finite-tree expectation give exactly (1).

For n at least nine the small-left and small-right split events are disjoint. The exact split law yields

$$p_n=\frac1{H_{n-1}}\left(H_{r_n}+\sum_{i=1}^{r_n}\frac1{n-i}\right)\longrightarrow\frac12.$$

Indeed $H_{r_n}/H_{n-1}\to1/2$, and the second numerator sum is at most $r_n/(n-r_n)=O(n^{-1/2})$. Eventually both $p_n$ and $1-p_n$ exceed one third. Therefore the absolute value in (1) is at least $n^{1/4}/3$ with probability one for all sufficiently large n. The finite normalized sums are not tight. Nevertheless their unnormalized empirical averages have magnitude at most $n^{-1/4}$ and tend to zero deterministically, so this does not contradict first-order fringe convergence.

## Positive-variance interpretation and remaining obstruction

If a nondegenerate Gaussian limit is mandatory, the construction by itself is not a full counterexample. It still gives the following precise structural implication. Let a class of admissible functionals contain some $\Psi$ with a nondegenerate fringe CLT and be closed under addition of the bounded continuous perturbation $\Phi$ above. A universal finite-tree transfer theorem cannot hold for every member of that class. The infinite fringe sums for $\Psi$ and $\Psi+\Phi$ are identical. If both centered finite-tree normalized sums were tight, their difference would be tight; the difference is (1), which is not tight. Thus at least one fails, conditional on the existence and admissibility of such $\Psi$.

The useful unresolved question is a transfer theorem with quantitative locality, stabilization, mixing, or a finite/infinite approximation error that is negligible after summing at square-root scale. Mere bounded continuity and first-order convergence are insufficient. These scope limits are retained in the problem ledger; this packet is not counted as a full solution of all intended versions of Open Problem 12.
