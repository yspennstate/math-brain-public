# Relative QUE on deterministic vertex sets from complete delocalization

Let H be a random real symmetric N by N matrix, N >= 2. Suppose its law is invariant under simultaneous permutation of rows and columns. Fix a deterministic real number L with 1 <= L <= N. Write D_L for the event

\[
 \|u\|_\infty^2\leq L/N
 \quad\text{for every real unit eigenvector }u\text{ of }H.
 \tag{1}
\]

The quantifier in (1) includes every unit vector in every eigenspace, not just one selected eigenbasis. Suppose P(D_L^c) <= q.

Let S_1,...,S_M be nonempty deterministic subsets of {1,...,N}, put s_m = |S_m|, and suppose s_m >= s >= 1. The sets are chosen independently of H. Define

\[
 Q(H)=\max_{1\leq m\leq M}\ 
 \sup_{\substack{Hu=\lambda u\\u\in\mathbb R^N,\ \|u\|_2=1}}
 \left|\frac{N}{s_m}\sum_{x\in S_m}u(x)^2-1\right|.
\]

**Theorem.** For 0 < epsilon <= 1,

\[
 \mathbb P\{Q(H)>\epsilon\}
 \leq q+2MN(N+1)9^{\lfloor L\rfloor}
       \exp\left(-\frac{\epsilon^2s}{10L}\right).
 \tag{2}
\]

The right side may be replaced by its minimum with 1. No simplicity assumption on the spectrum is needed.

**Proof.** The proof has four parts.

First, fix nonnegative weights w_1,...,w_N with sum 1 and max w_i <= delta. If T is a uniformly sampled subset of size h, set p = h/N. For 1 <= h < N and a > 0, we claim

\[
 \mathbb P\left\{\left|\sum_{i\in T}w_i-p\right|>a\right\}
 \leq 2(N+1)\exp\left(-\frac{a^2}{2(p\delta+\delta a/3)}\right).
 \tag{3}
\]

To prove this, let xi_i be independent Bernoulli(p) variables and let X_i = (xi_i-p)w_i. They have mean zero, |X_i| <= delta, and

\[
 V:=\sum_i\mathbb E X_i^2
   =p(1-p)\sum_iw_i^2\leq p\delta.
\]

For a mean-zero variable X with |X| <= delta, and 0 <= t < 3/delta, expansion of the exponential gives

\[
 \mathbb E e^{tX}
 \leq 1+\mathbb E X^2\sum_{k\geq2}\frac{t^k\delta^{k-2}}{k!}
 \leq\exp\left(\frac{t^2\mathbb E X^2}{2(1-t\delta/3)}\right).
 \tag{4}
\]

Here |E X^k| <= delta^{k-2} E X^2, and k! >= 2*3^{k-2} for k >= 2. The latter inequality follows by induction, starting at k = 2 and multiplying by k+1 >= 3. Independence, (4), and Markov's inequality, with

\[
 t=\frac{a}{p\delta+\delta a/3},
\]

give

\[
 \mathbb P\left\{\left|\sum_iX_i\right|>a\right\}
 \leq2\exp\left(-\frac{a^2}{2(p\delta+\delta a/3)}\right).
 \tag{5}
\]

The same moment estimate applies to -X_i for the lower tail.

Conditioned on sum_i xi_i = h, the selected coordinates form a uniform h-subset. Moreover, h is a mode of the binomial distribution with parameters N and p = h/N. Indeed, the ratio of the mass at h to that at h-1 is (N-h+1)/(N-h) > 1, the ratio at h+1 to that at h is h/(h+1) < 1, and successive ratios decrease with the index. Thus

\[
 \mathbb P\left\{\sum_i\xi_i=h\right\}\geq\frac1{N+1}.
\]

Dividing (5) by this probability proves (3). When h = N, the subset mass equals 1 exactly, so no estimate is required.

Second, consider a fixed eigenspace E of a matrix satisfying D_L. Let P_E be its orthogonal projection and m = dim E. For every coordinate i,

\[
 (P_E)_{ii}=\sup_{\substack{u\in E\\\|u\|_2=1}}u(i)^2\leq L/N.
 \tag{6}
\]

The equality follows from u(i) = <P_E e_i,u> and Cauchy--Schwarz, with equality at the normalized projection when it is nonzero. Summing (6) gives

\[
 m=\operatorname{Tr}P_E\leq L.
 \tag{7}
\]

Choose a 1/4-net V_E of the unit sphere of E, in Euclidean distance, with at most 9^m points. For completeness, a maximal 1/4-separated family is a net. The open balls of radius 1/8 about its points are disjoint and lie in the ball of radius 9/8 in E. Comparison of m-dimensional volumes bounds its cardinality by 9^m; this also shows a finite maximal family exists.

For any symmetric operator B on E,

\[
 \|B\|\leq2\max_{v\in V_E}|\langle v,Bv\rangle|.
 \tag{8}
\]

In fact choose a unit u with |<u,Bu>| = ||B|| and a net point v with ||u-v|| <= 1/4. Then

\[
 |\langle u,Bu\rangle-\langle v,Bv\rangle|
 \leq |\langle u-v,Bu\rangle|+|\langle v,B(u-v)\rangle|
 \leq\tfrac12\|B\|,
\]

which proves (8).

Third, fix a uniform subset T of size h, put p = h/N, and let D_T be the diagonal projection onto T. On E consider

\[
 B=(P_E D_T P_E)|_E-pI_E.
\]

For any net vector v, the weights w_i = v(i)^2 sum to 1 and satisfy w_i <= delta = L/N by (1). Apply (3) with a = epsilon p/2. Its exponent is

\[
 \frac{a^2}{2(p\delta+\delta a/3)}
 =\frac{\epsilon^2p}{8\delta(1+\epsilon/6)}
 \geq\frac{\epsilon^2p}{10\delta}
 =\frac{\epsilon^2h}{10L},
 \tag{9}
\]

because 8(1+epsilon/6) <= 28/3 < 10. A union bound over the net and (8) now give

\[
 \mathbb P_T\left\{
  \sup_{\substack{u\in E\\\|u\|_2=1}}
   \left|\sum_{i\in T}u(i)^2-p\right|>\epsilon p
 \right\}
 \leq2(N+1)9^m\exp\left(-\frac{\epsilon^2h}{10L}\right).
 \tag{10}
\]

For h = N the left side is zero. The estimate therefore covers all permitted set sizes.

Finally, sample H and an independent uniform permutation pi, and write H' = P_pi H P_pi^T. By invariance H' has the law of H. Condition on any H in D_L. Its eigenspaces and their nets are now fixed. A unit eigenvector u of H becomes P_pi u for H', and its mass on S_m is the mass of u on pi^{-1}(S_m). Each inverse image is a uniform s_m-subset. Independence among these inverse images is unnecessary. There are at most N distinct eigenspaces, each of dimension at most floor L by (7). Apply (10) and take a union bound over eigenspaces and sets. This bounds the conditional failure probability by the second term of (2). The matrices outside D_L contribute at most q. Since H' and H have the same law, (2) follows. All nets were selected after conditioning on H, so no equivariant choice of eigenbasis was used. This completes the proof.

**Rate.** For r > 0 put

\[
 A=\lfloor L\rfloor\log9+\log(2MN(N+1))+r\log N,
 \qquad \epsilon_N=\sqrt{\frac{10LA}{s}}.
 \tag{11}
\]

Whenever epsilon_N <= 1, substituting (11) into (2) gives

\[
 \mathbb P\{Q(H)>\epsilon_N\}\leq q+N^{-r}.
 \tag{12}
\]

In particular relative QUE follows if q -> 0 and

\[
 \frac{s}{L(L+\log(MN))}\longrightarrow\infty.
 \tag{13}
\]

This is a sufficient scale from an elementary net argument; no optimality is asserted.

**Application to random regular graphs.** Fix d >= 3 and let H = A/sqrt(d-1), where A is the adjacency matrix of a uniform simple labelled d-regular graph. Its law is permutation invariant and its eigenvectors are those of A. Theorem 1.4 of Jiaoyang Huang and Horng-Tzer Yau, *Spectrum of Random d-regular Graphs Up to the Edge*, [arXiv:2102.00963v3](https://arxiv.org/html/2102.00963v3#S1.SS3), supplies (1) with L = (log N)^{C_d}, after increasing a fixed exponent C_d, and q = o(1). More precisely, fix the paper's parameter c in (0,1); the unconditional exceptional probability is O(N^{-(1-c) omega_d}) for its positive integer omega_d, after including the conditional error. No arbitrarily high polynomial probability is claimed unconditionally.

Consequently, for fixed alpha in (0,1], fixed K >= 0, and any deterministic family of at most N^K vertex sets with sizes at least N^alpha,

\[
 \max_m\sup_{\substack{Au=\lambda u\\\|u\|_2=1}}
 \left|\frac{N}{|S_m|}\sum_{x\in S_m}|u(x)|^2-1\right|
 \xrightarrow{\mathbb P}0.
 \tag{14}
\]

For each fixed r, the explicit error in (11) is

\[
 O_{d,K,r}\!\left(
 N^{-\alpha/2}
 \big((\log N)^{C_d}+(\log N)^{(C_d+1)/2}\big)
 \right),
 \tag{15}
\]

with failure probability at most q + N^{-r}. The unknown numerical value of the fixed exponent C_d is retained; it is not replaced by an invented constant. The assertion covers all eigenvalues, and therefore every compact bulk interval. It also covers complex eigenvectors: each eigenspace is the complexification of a real eigenspace, and the real symmetric compression B has the same operator norm on either field.

Equation (14) is a deterministic-observable QUE formulation that follows from existing delocalization. The work here is the explicit reduction and its quantifiers, not a new random-graph estimate or a claim of priority for (14).

**Why the deterministic-set condition cannot be dropped from the reduction.** Let n = 2^k and N = 2n. Let W be the real orthogonal Walsh matrix indexed by x,y in {0,1}^k, with W(x,y) = (-1)^{x dot y}/sqrt(n). Orthogonality follows by summing the character (-1)^{x dot (y-z)} over x. Put U = diag(W,W), choose N distinct real numbers lambda_j, and form H_0 = U diag(lambda_j) U^T. All its unit eigenvectors have coordinate squares at most 2/N, because each eigenspace is one-dimensional. Uniformly permute its coordinates to obtain a permutation-invariant random matrix H satisfying D_2 surely. The support of any eigenvector has size N/2 and contains its entire mass. Choosing that support after seeing H gives relative error 1, rather than a quantity tending to zero. This is a counterexample to extending the abstract reduction to adaptive sets; it is not a counterexample for uniform random regular graphs.
