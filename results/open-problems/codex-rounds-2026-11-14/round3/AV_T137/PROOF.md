# Comparing the two Viana–Bray conventions

Let c >= 0, beta > 0, and let J have mean zero and E|J| < infinity. Suppose N is a positive integer with p = c/N <= 1. Define

\[
F_N^{\rm B}=\frac1N\mathbb E\log\sum_{\sigma\in\{-1,1\}^N}
\exp\left(\beta\sum_{i<j}B_{ij}J_{ij}\sigma_i\sigma_j\right),
\]

where the B_ij are independent Bernoulli(p) variables and the J_ij are independent copies of J, independent of the edges. Define F_N^P by replacing the Hamiltonian with

\[
\beta\sum_{a=1}^{M}J_a\sigma_{I_a}\sigma_{L_a},
\qquad M\sim\operatorname{Pois}(cN/2),
\]

where all endpoints are independent uniform elements of {1,...,N}, and all other disorder is independent. Then

\[
|F_N^{\rm P}-F_N^{\rm B}|
\leq \frac{\beta\mathbb E|J|}{N}\,N(N-1)
\left(\frac cN-1+e^{-c/N}\right)
\leq\frac{\beta\mathbb E|J|c^2(N-1)}{2N^2}.
\tag{1}
\]

In particular, the limiting expected pressures agree whenever one exists. The claim applies to both coupling laws in T137.

## Proof

Poisson thinning partitions the ordered endpoints of M into independent counts. Each unordered off-diagonal pair has probability 2/N^2 per clause, hence count X_ij with law Pois(c/N). Each diagonal pair has probability 1/N^2. The total number of loops is Pois(c/2).

A loop contributes beta J_a to the Hamiltonian, independently of the spin configuration. Thus its contribution to log Z is exactly beta J_a. Their sum has expectation zero because E J = 0, so deleting all loops leaves the expected pressure unchanged. This is an identity for expected pressure; no claim of equality of the random pressures is needed.

For one off-diagonal pair put q = 1 - exp(-p). Let X have law Pois(p). If X >= 1, set B = 1. If X = 0, set B = 1 with probability (p-q)/exp(-p), independently of the coupling marks. This is a valid probability: p-q >= 0 by exp(-p) >= 1-p, and p-q <= exp(-p) because p <= 1. The resulting marginal satisfies P(B=1) = q + (p-q) = p.

On X >= 1, reuse the first Poisson bond as the Bernoulli bond and delete X-1 bonds. On X = 0 and B = 1, insert one independently marked bond. Consequently

\[
\mathbb E|X-B|
=\mathbb E(X-1)_++\mathbb P(X=0,B=1)
=(p-q)+(p-q)=2(p-1+e^{-p}).
\tag{2}
\]

Choose this construction independently for all pairs. Coupling marks remain independent with law J in both marginal models, since the count construction does not depend on marks.

Adding a bond beta J sigma_i sigma_j multiplies every Gibbs weight by a number between exp(-beta|J|) and exp(beta|J|). Therefore it changes log Z by at most beta|J|. Applying this bound successively to all unmatched bonds and taking expectations gives

\[
|F_N^{\rm P}-F_N^{\rm B}|
\leq\frac{\beta\mathbb E|J|}{N}
\binom N2\,2(p-1+e^{-p}).
\]

This is the first inequality in (1). The identity

\[
p-1+e^{-p}=\int_0^p(1-e^{-t})\,dt
\leq\int_0^p t\,dt=\frac{p^2}{2}
\]

gives the second. All bounds are finite under E|J| < infinity.

## Independent audit of the edit cost and density

For any coupling of nonnegative integer X and B,

\[
\mathbb E|X-B|\geq\sum_{k=0}^{\infty}
\left|\mathbb P(X>k)-\mathbb P(B>k)\right|.
\]

Indeed, pointwise |X-B| is the number of thresholds k at which their indicators differ, and the expectation of each absolute indicator difference dominates the absolute difference of expectations. For these marginals the displayed lower bound is

\[
|q-p|+\sum_{k\geq1}\mathbb P(X>k)
=(p-q)+(\mathbb E X-\mathbb P(X>0))
=2(p-q).
\]

Thus the explicit construction attains the lower bound, independently checking (2) and its factor of two.

There is also a count check on lambda = c/2. The Poisson model has expected off-diagonal bond count c(N-1)/2 after removing c/2 expected loops. The Bernoulli model has exactly the same expected bond count, binom(N,2)c/N = c(N-1)/2. Taking lambda = c would double that count.

At c = 0 both pressures equal log 2. At N = 1, where c <= 1, there are no off-diagonal pairs and the expected loop contribution is zero, so both pressures again equal log 2 and (1) gives zero. At p = 1 the conditional insertion probability equals one and the coupling remains valid. The argument requires fixed c and beta in the thermodynamic limit; it does not assert a uniform vanishing bound when they grow with N.

Without the mean-zero hypothesis the same argument yields (1) with the additional term beta c |E J|/(2N), accounting for the expected loop shift.
