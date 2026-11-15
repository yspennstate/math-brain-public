# Relative equidistribution on prescribed shrinking vertex sets

## Statement

Let B be a random real symmetric N by N matrix whose law is invariant under conjugation by permutation matrices. Assume that, outside an event of probability epsilon, every unit eigenvector, including every unit vector in each repeated eigenspace, satisfies

\[
 \|u\|_\infty\le L/\sqrt N,\qquad L\ge1.                 \tag{1}
\]

Fix a deterministic set S of k vertices, where 1 <= k < N, and put q=min(k,N-k). Then, for every r>0,

\[
 \mathbb P\left\{
 \sup_{Bu=\lambda u,\ \|u\|_2=1}
 \left|\frac{N}{k}\sum_{i\in S}|u_i|^2-1\right|>r\right\}
 \le \varepsilon+2N^2\exp\left(-\frac{k^2r^2}{8qL^8}\right).
                                                               \tag{2}
\]

In particular the exponent can be replaced by the weaker k r^2/(8L^8). For each D>0 the relative error is at most

\[
 r_{N,k}=\frac{L^4}{k}\sqrt{8q(D+2)\log N}                     \tag{3}
\]

except with probability epsilon+2N^(-D). When k=N, the error is identically zero. The zero-size set has no relative normalization and is excluded.

Thus if L=L_N and epsilon=epsilon_N, with epsilon_N tending to zero, relative equidistribution holds in probability for every prescribed sequence of sets satisfying

\[
 \frac{k_N}{L_N^8\log N}\longrightarrow\infty.                 \tag{4}
\]

The supremum is over all unit eigenvectors. It does not include a choice of S after seeing B.

## 1. Sampling a subset without replacement

Let w_1,...,w_N be fixed real numbers in [-b,b], b>0. Let J_1,...,J_q be uniformly sampled distinct indices, with 1 <= q < N. Define

\[
 T=\sum_{j=1}^q w_{J_j},\qquad
 \bar w=\frac1N\sum_{i=1}^Nw_i.
\]

Reveal the indices in their sampling order. Write F_j for the information after j reveals and M_j=E[T|F_j]. If mu_{j-1} is the mean of the N-j+1 unrevealed values before step j and x=w_{J_j}, then

\[
 \begin{aligned}
 M_{j-1}&=\sum_{\ell<j}w_{J_\ell}+(q-j+1)\mu_{j-1},\\
 M_j&=\sum_{\ell<j}w_{J_\ell}+x+
             (q-j)\frac{(N-j+1)\mu_{j-1}-x}{N-j}.
 \end{aligned}
\]

Subtracting and collecting x and mu separately gives

\[
 M_j-M_{j-1}=\frac{N-q}{N-j}(x-\mu_{j-1}).                    \tag{5}
\]

Since j<=q, the coefficient lies in [0,1]. Both x and mu lie in [-b,b], so each increment has absolute value at most 2b. Its conditional mean is zero because x is a uniform unrevealed value. Also M_0=q bar w and M_q=T.

If Y has conditional mean zero and |Y|<=c, the secant inequality for the exponential on [-c,c] gives

\[
 E[e^{\theta Y}\mid F]\le\cosh(\theta c)
                    \le e^{\theta^2c^2/2}.
\]

The last inequality follows by integrating tanh(t)<=t for t>=0 and using evenness. Apply this with c=2b to the q increments and iterate:

\[
 E e^{\theta(T-q\bar w)}\le e^{2qb^2\theta^2}.
\]

Markov's inequality with theta=t/(4qb^2) yields the upper tail exp(-t^2/(8qb^2)); applying the same argument to -T yields

\[
 \mathbb P\{|T-q\bar w|>t\}
 \le 2e^{-t^2/(8qb^2)}.                                      \tag{6}
\]

When b=0 the centered sum is zero. When q=N its centered sum is also zero, without using (5).

For a uniform subset R of size k, apply (6) directly if k<=N/2. Otherwise use its complement, since

\[
 \sum_{i\in R}w_i-k\bar w
   =-\left(\sum_{i\notin R}w_i-(N-k)\bar w\right).
\]

Consequently (6) holds for a k-subset with q=min(k,N-k) in the denominator.

## 2. Compression to a complete eigenspace

Fix a realization B satisfying (1). If V_lambda is an eigenspace of dimension m_lambda and Q_lambda its orthogonal projection, then

\[
 Q_\lambda(i,i)
  =\sup_{u\in V_\lambda,\ \|u\|_2=1}|u_i|^2\le L^2/N.
\]

Indeed u_i=<Q_lambda e_i,u>, and equality is attained by normalizing Q_lambda e_i when it is nonzero. Taking the trace gives m_lambda<=L^2. Choose any real orthonormal basis v_{lambda,1},...,v_{lambda,m_lambda} for each eigenspace, before sampling a permutation. Set

\[
 C_\lambda(R)_{\alpha\beta}
    =\sum_{i\in R}v_{\lambda,\alpha}(i)v_{\lambda,\beta}(i)
                           -\frac{k}{N}\delta_{\alpha\beta}.
\]

Each entry is a centered subset sum with

\[
 w_i=v_{\lambda,\alpha}(i)v_{\lambda,\beta}(i),\quad
 |w_i|\le L^2/N,\quad
 \bar w=\delta_{\alpha\beta}/N.
\]

The centering follows from orthonormality, including for off-diagonal entries. Equation (6) therefore gives

\[
 \mathbb P_R\{|C_\lambda(R)_{\alpha\beta}|>t\}
   \le2\exp\left(-\frac{N^2t^2}{8qL^4}\right).                \tag{7}
\]

There are sum_lambda m_lambda^2 <= (sum_lambda m_lambda)^2=N^2 such entries. A union bound controls them all at once with the same exponent and prefactor 2N^2. If every entry has absolute value at most t, every real or complex unit coefficient vector z satisfies

\[
 |z^*C_\lambda(R)z|
 \le t\left(\sum_\alpha|z_\alpha|\right)^2
 \le m_\lambda t\le L^2t.                                  \tag{8}
\]

Every unit eigenvector in V_lambda is a linear combination of this basis, so the expression on the left covers its deviation sum_{i in R}|u_i|^2-k/N. No simple-spectrum assumption is needed. With t=kr/(NL^2), (7)-(8) give conditional failure at most

\[
 2N^2\exp\left(-\frac{k^2r^2}{8qL^8}\right).                 \tag{9}
\]

## 3. Return to the prescribed set and random matrix

Let pi be an independent uniform permutation and P_pi e_i=e_{pi(i)}. For an eigenvector u of B, the corresponding eigenvector P_pi u of P_pi B P_pi^T has mass on the prescribed set S equal to

\[
 \sum_{j\in S}|(P_\pi u)_j|^2
       =\sum_{i\in\pi^{-1}(S)}|u_i|^2.
\]

Conditional on B, pi^{-1}(S) is a uniform k-subset. Thus (9) controls the conditional failure for every good B. On bad B use the bound 1. Average over B and use permutation invariance of its law to obtain (2). The good event defined by (1) is itself permutation invariant; no basis chosen as a function of labels has to be equivariant.

Substituting (3) makes the extra failure term exactly 2N^2 exp(-(D+2)log N)=2N^(-D). Since q<=k, (3) is at most L^4 sqrt(8(D+2)log N/k), which tends to zero under (4).

## 4. Application to fixed-degree random regular graphs

Jiaoyang Huang and Horng-Tzer Yau, *Spectrum of Random d-regular Graphs Up to the Edge*, [arXiv:2102.00963v3](https://arxiv.org/html/2102.00963v3), Theorem 1.4 and the paragraph following it, give (1) for every fixed d>=3 with L_N a fixed power of log N and epsilon_N tending to zero. The theorem is first stated on a locally tree-like graph event; its following paragraph gives the unconditional high-probability consequence. The all-eigenvector form also follows from their resolvent proof, which bounds every coordinate of any vector in an eigenspace. Adjacency normalization by sqrt(d-1) leaves eigenvectors unchanged. Uniform simple labelled regular graphs have permutation-invariant law.

It follows that, for some finite C depending on the delocalization bound and for each prescribed sequence S_N with |S_N|/(log N)^C tending to infinity,

\[
 \sup_{A_Nu=\lambda u,\ \|u\|_2=1}
 \left|\frac{N}{|S_N|}\sum_{i\in S_N}|u_i|^2-1\right|
                  \xrightarrow{\mathbb P}0.                  \tag{10}
\]

More explicitly one may take any C=8c+1 if L_N<=(log N)^c for all sufficiently large N. A fixed multiplicative constant in L_N can be absorbed by increasing c. No numerical value for the exponent hidden in Huang–Yau is asserted. In particular (10) holds on every prescribed set of size at least N^alpha for every fixed alpha>0. The assertion is for all eigenvectors, so in particular for every bulk eigenvector. The exceptional-graph term epsilon_N remains in (2); arbitrary unconditional polynomial success probabilities are not claimed.

## 5. Independent scale checks and obstructions

Let I_i indicate inclusion in a uniform q-subset. Direct counting gives E I_i=q/N and E I_i I_j=q(q-1)/(N(N-1)) for i!=j. Expanding the variance of sum_i I_i w_i gives

\[
 \operatorname{Var}T
  =\frac{q(N-q)}{N-1}
       \left(\frac1N\sum_iw_i^2-\bar w^2\right).              \tag{11}
\]

A second derivation uses ordered samples: the individual variance is sigma_w^2=(sum w_i^2)/N-bar w^2 and the covariance of distinct draws is -sigma_w^2/(N-1). Adding q variances and q(q-1) covariances gives (11). This also verifies the complement symmetry q <-> N-q. For an eigenspace-entry weight, sum_i |w_i|<=1 by Cauchy–Schwarz, hence (sum_i w_i^2)/N<=L^2/N^2. Its variance is at most q(N-q)L^2/((N-1)N^2). The bounded-increment estimate is deliberately weaker; no optimal logarithmic exponent is claimed.

The constants in (2) have two separate sources: q increments bounded by 2b give 2q(2b)^2=8qb^2; b=L^2/N and t=kr/(NL^2) give t^2/(8qb^2)=k^2r^2/(8qL^8). This also shows why substituting k for q only weakens the estimate.

The earlier bounded-test estimate applied directly to 1_S would give relative error of order L^4 sqrt(N log N)/k. The new estimate for k<=N/2 is of order L^4 sqrt(log N/k). Thus the new result treats polylogarithmic set sizes growing sufficiently fast, whereas that earlier bound alone requires k much larger than L^4 sqrt(N log N).

Small sets cannot be ignored in the abstract implication. Let N=2^h and let H be a real normalized Walsh matrix with entries +/-1/sqrt N. Define an orthogonal matrix U by, for each pair of rows of H, replacing them by their sum and difference divided by sqrt 2. Every column of U has exactly N/2 nonzero coordinates, each with squared modulus 2/N. For distinct real numbers lambda_1,...,lambda_N, set B_0=U diag(lambda_j)U^T, and randomize B_0 by uniform label permutation. This gives a permutation-invariant matrix ensemble with simple spectrum and all unit eigenvectors bounded by sqrt(2/N), so L=sqrt 2. For a prescribed singleton S, every eigenvector has relative mass either 0 or 2; its relative discrepancy is exactly 1. This is a full matrix-ensemble counterexample to singleton QUE from the hypotheses, not an example of a regular graph.

Nor is S allowed to depend on the matrix: in the same ensemble choose the support of a simple eigenvector using its distinct eigenvalue to identify it. This set has k=N/2 but carries its entire mass, again giving relative discrepancy 1. These examples rule out illicit uniformity over every set and arbitrary graph-dependent sets. They do not exclude stronger conclusions available from additional random-regular-graph structure. Graph balls centered at a vertex are graph-dependent and are not covered by (10).
