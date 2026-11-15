# Relative mass on prescribed sets without a multiplicity cost

## Statement

Let B be a random real symmetric N by N matrix, N>=2, whose law is invariant under conjugation by permutation matrices. Suppose that, outside an event of probability epsilon, every unit vector in every eigenspace satisfies
\[
 \|u\|_\infty\le L/\sqrt N,\qquad L\ge1.                 \tag{1}
\]
For each deterministic set S of size 1<=k<N, put q=min(k,N-k). For every r>0,
\[
 \mathbb P\left\{
 \sup_{Bu=\lambda u,\ \|u\|_2=1}
 \left|\frac Nk\sum_{i\in S}|u_i|^2-1\right|>r\right\}
 \le \varepsilon+2N
 \exp\left[-\frac{k^2r^2}{2L^2(q+kr/3)}\right].           \tag{2}
\]
The supremum includes every vector in repeated eigenspaces and also complex unit eigenvectors. No multiplicity bound or simple-spectrum event is required. The right side can be capped at 1. For k=N the discrepancy is zero; k=0 has no relative normalization.

For D>0, set x=(D+1)log N and
\[
 r_* =\frac{\sqrt{2qL^2x}}k+\frac{2L^2x}{3k}.             \tag{3}
\]
The failure probability at r_* is at most epsilon+2N^(-D). In particular, if epsilon_N->0, then
\[
 \frac{k_N}{L_N^2\log N}\longrightarrow\infty            \tag{4}
\]
is sufficient for the supremum in (2) to tend to zero in probability. Each set is prescribed before sampling B; the assertion is not uniform over all choices of S.

This improves the round-5 sufficient condition k/[L^2(M+log N)]->infinity, where M bounds eigenspace dimensions, to (4). It also removes the 1/4-net's loss in the scalar tail constant. It is a consequence of standard matrix concentration methods, with no claim of novelty.

## 1. Convex comparison for sampling without replacement

Let X_1,...,X_N be fixed elements of a finite-dimensional real vector space, and let 1<=q<=N. Draw independent uniform indices J_1,...,J_q from {1,...,N}. Write T for their set of distinct values. Conditional on these indices, choose R uniformly among all q-subsets containing T. This is possible because |T|<=q. Let n_i count the occurrences of i among the J_j.

The construction is invariant under every permutation of the N labels. All q-subsets are therefore equally likely as R, so R is a uniform q-subset. Fix any possible value R=R_0. Its conditional law is invariant under every label permutation that preserves R_0. Thus E[n_i|R=R_0] has one common value for i in R_0. All counts outside R_0 vanish, and sum_i n_i=q holds identically. Since |R_0|=q, that common conditional expectation is 1. Consequently
\[
 \mathbb E\left[\sum_{j=1}^q X_{J_j}\,\middle|\,R\right]
       =\sum_{i\in R}X_i.                                \tag{5}
\]
This is an equality of vectors, with deterministic X_i; it requires no assumption that the X_i are distinct.

For every convex real function F on the vector space, conditional Jensen followed by expectation gives
\[
 \mathbb E_R F\left(\sum_{i\in R}X_i\right)
 \le \mathbb E_J F\left(\sum_{j=1}^q X_{J_j}\right).       \tag{6}
\]
This is the without-replacement comparison used below. David Gross and Vincent Nesme, *Note on sampling without replacing from a finite collection of matrices*, [arXiv:1001.2738v2](https://arxiv.org/pdf/1001.2738), Section C and Lemma 2, give the corresponding convex comparison and its trace-exponential application. Equations (5)–(6) provide the needed coupling argument directly.

For completeness, F(H)=tr exp(theta H) is convex on real symmetric matrices for every real theta. Here is a finite-dimensional verification. For symmetric H,K let g(t)=tr exp(H+tK). Differentiation of the absolutely convergent exponential series and cyclicity of trace give g'(t)=tr(K exp(H+tK)). The derivative of the exponential in direction K is
\[
 D\exp(H)[K]=\int_0^1 e^{(1-s)H}K e^{sH}\,ds.
\]
To obtain this identity directly, expand both exponentials inside the integral. The coefficient of H^a K H^b is
\(\int_0^1(1-s)^a s^b ds/(a!b!)=1/(a+b+1)!\), which is exactly its coefficient in the differentiated series. Hence
\[
 g''(t)=\int_0^1\operatorname{tr}
    \bigl(K e^{(1-s)(H+tK)}K e^{s(H+tK)}\bigr)\,ds\ge0.  \tag{7}
\]
Indeed, diagonalizing H+tK expresses the integrand as a sum of terms |K_ij|^2 exp((1-s)lambda_j+s lambda_i), each nonnegative. Replacing H,K by theta H,theta K proves the asserted convexity for either sign of theta. Only trace convexity is used; operator convexity of exp is not asserted.

## 2. A matrix Bernstein estimate

Let X_1,...,X_N now be symmetric m by m matrices satisfying
\[
 \frac1N\sum_iX_i=0,\quad \|X_i\|\le b,\quad
 \frac1N\sum_iX_i^2\preceq vI_m,\qquad b,v>0.           \tag{8}
\]
The order A preceq B means B-A is positive semidefinite. Let Y be one uniform draw from these matrices. For |theta|b<3, the scalar power series, applied to each eigenvalue z of Y, gives
\[
 e^{\theta z}\le1+\theta z+
       \frac{\theta^2 z^2}{2(1-b|\theta|/3)}.
\]
To check this bound, use |z|^j<=b^(j-2)z^2 for j>=2 and j!>=2*3^(j-2), and sum the resulting geometric series. Spectral calculus and (8) therefore give
\[
 \mathbb Ee^{\theta Y}
 \preceq\left(1+\frac{v\theta^2}{2(1-b|\theta|/3)}\right)I_m
 \preceq e^{h(\theta)}I_m,\qquad
 h(\theta)=\frac{v\theta^2}{2(1-b|\theta|/3)}.            \tag{9}
\]

Use the standard Golden–Thompson inequality
\[
 \operatorname{tr}e^{A+C}\le\operatorname{tr}(e^A e^C)
                                                               \tag{10}
\]
for two real symmetric matrices A,C. This established matrix-analysis theorem is the only trace inequality imported without proof; see Joel A. Tropp, *User-Friendly Tail Bounds for Sums of Random Matrices*, [author PDF](https://tropp.caltech.edu/papers/Tro11-User-Friendly-preprint.pdf), equation (2.6). It holds without commutativity.

Let Y_1,...,Y_q be independent draws and H_{j-1}=theta sum_{ell<j}Y_ell. Conditional on the first j-1 draws, (10), independence, and (9) imply
\[
 \begin{aligned}
 \mathbb E[\operatorname{tr}e^{H_{j-1}+\theta Y_j}
              \mid Y_1,\ldots,Y_{j-1}]
 &\le\operatorname{tr}\bigl(e^{H_{j-1}}\mathbb Ee^{\theta Y_j}\bigr)\\
 &\le e^{h(\theta)}\operatorname{tr}e^{H_{j-1}}.
 \end{aligned}                                             \tag{11}
\]
The second inequality follows because e^{H_{j-1}} is positive semidefinite: if C preceq cI then tr(PC)<=c tr(P) for P positive semidefinite, as tr(P^(1/2)(cI-C)P^(1/2))>=0. Iteration from tr(I_m)=m gives
\[
 \mathbb E\operatorname{tr}e^{\theta\sum_{j=1}^qY_j}
           \le m e^{q h(\theta)}.                         \tag{12}
\]
This iteration replaces the last conditional matrix mgf by a scalar multiple of the identity at each step. It does not assert a Golden–Thompson inequality for three or more factors or a product formula for noncommuting exponentials.

Apply (6) with the convex trace exponential to transfer (12) to a uniform q-subset R and Z=sum_{i in R}X_i. For theta>0, the event lambda_max(Z)>t implies tr exp(theta Z)>exp(theta t). Markov's inequality yields
\[
 \mathbb P\{\lambda_{\max}(Z)>t\}
        \le m\exp(-\theta t+q h(\theta)).
\]
Choose theta=t/(qv+bt/3). It satisfies theta b<3 since v>0. Substitution, using 1-b theta/3=qv/(qv+bt/3), gives exactly
\[
 -\theta t+q h(\theta)=-\frac{t^2}{2(qv+bt/3)}.
\]
Apply the same argument to -X_i and sum the two tails:
\[
 \mathbb P_R\left\{\left\|\sum_{i\in R}X_i\right\|>t\right\}
 \le2m\exp\left[-\frac{t^2}{2(qv+bt/3)}\right].           \tag{13}
\]
The estimate needs only upper bounds b,v, which may be positive even if the actual matrices or variance vanish.

## 3. Compressing the set observable to an entire eigenspace

Fix a realization satisfying (1) and an eigenspace V of dimension m. Let U have a real orthonormal basis of V as its columns, let a_i=U^T e_i, and set A_i=a_i a_i^T. Then
\[
 A_i\succeq0,\quad \sum_iA_i=I_m,\quad
 \|A_i\|=\|a_i\|_2^2=(UU^T)_{ii}\le L^2/N.              \tag{14}
\]
The last inequality uses the identity
\[
 (UU^T)_{ii}=\sup_{u\in V,\ \|u\|=1}|u_i|^2.
\]
Cauchy–Schwarz proves the upper bound in that identity; if U^T e_i is nonzero, its normalized coefficient vector attains it. In particular the hypothesis is on every vector in V, not merely on the chosen basis. Taking the trace in (14) also recovers m<=L^2, but this dimension estimate is unnecessary for (2).

Define X_i=A_i-I_m/N. Its mean is zero. Every eigenvalue of A_i lies in [0,L^2/N], so, since L>=1,
\[
 \|X_i\|\le L^2/N=:b.
\]
Since A_i has rank at most one, A_i^2=||a_i||^2 A_i preceq (L^2/N)A_i. Thus
\[
 \begin{aligned}
 \frac1N\sum_i X_i^2
 &=\frac1N\sum_i A_i^2-\frac1{N^2}I_m\\
 &\preceq\frac{L^2-1}{N^2}I_m
 \preceq\frac{L^2}{N^2}I_m=:vI_m.                         \tag{15}
 \end{aligned}
\]
In the first equality, expand the square, use sum_i A_i=I_m, and note that N copies of I_m/N^2 sum to I_m/N. Both b and v chosen here are strictly positive.

For a uniform k-subset R, its centered compression is
\[
 C_V(R)=U^T\operatorname{diag}(1_R)U-(k/N)I_m
       =\sum_{i\in R}X_i.
\]
If k>N/2 use its complementary q-subset, since sum_i X_i=0 and C_V(R)=-sum_{i notin R}X_i. Otherwise use q=k directly. Equation (13) with (15) gives
\[
 \mathbb P_R\{\|C_V(R)\|>t\}
 \le2m\exp\left[-\frac{N^2t^2}{2L^2(q+Nt/3)}\right].    \tag{16}
\]
For a unit real or complex coefficient vector z, the mass of u=Uz is z^*U^T diag(1_R)Uz. The spectral theorem gives sup_{||z||=1}|z^*C_V(R)z|=||C_V(R)||, also for complex z, since C_V(R) is real symmetric. Thus (16) controls all unit vectors in V at once.

Distinct eigenspaces form an orthogonal direct sum of R^N, so sum_V dim V=N. A union bound over them, with t=kr/N, gives
\[
 \mathbb P_R\left\{
 \sup_{Bu=\lambda u,\ \|u\|=1}
 \left|\frac Nk\sum_{i\in R}|u_i|^2-1\right|>r\right\}
 \le2N\exp\left[-\frac{k^2r^2}{2L^2(q+kr/3)}\right].     \tag{17}
\]
No net or entrywise-to-operator estimate enters (17).

## 4. Random labels and inversion

Let pi be an independent uniform permutation, with P_pi e_i=e_{pi(i)}. For every eigenvector u of B, P_pi u is an eigenvector of P_pi B P_pi^T. Its mass on the prescribed S is the mass of u on pi^(-1)(S), which is a uniform k-subset conditional on B. For each good B, (17) applies; bad B contribute at most epsilon. The distribution of P_pi B P_pi^T equals that of B. Averaging proves (2). The good event can be taken to be exactly (1), hence is label invariant. There is no requirement to choose an eigenbasis equivariantly.

To check (3), put A=kr_*, a=2qL^2x, b_0=2L^2x/3. Then A=sqrt(a)+b_0 and
\[
 A^2-b_0A-a=b_0\sqrt a\ge0.
\]
Therefore A^2>=2L^2x(q+A/3), so the exponent in (2) is at least x. The prefactor is 2N exp(-x)=2N^(-D). Since q<=k, (3) is at most sqrt(2L^2x/k)+2L^2x/(3k), proving (4).

## 5. Independent checks, application, and limits

There is a second derivation of the matrix variance scale, independent of expanding centered squares in (15). For symmetric X_i with sum_i X_i=0, expansion of the square of a subset sum gives
\[
 \mathbb E_R\left(\sum_{i\in R}X_i\right)^2
 =\frac{q(N-q)}{N(N-1)}\sum_iX_i^2.                      \tag{18}
\]
Indeed, each diagonal term has inclusion probability q/N and each ordered off-diagonal term has probability q(q-1)/(N(N-1)). The sum of all ordered off-diagonal products is -sum_i X_i^2, because (sum_i X_i)^2=0. This argument retains the order of the products and does not assume commutativity. For q independent uniform draws the corresponding second moment is (q/N)sum_i X_i^2. Thus (18) is smaller by the finite-population factor (N-q)/(N-1), in agreement with the safe direction of the convex comparison.

A separate scalar check fixes any real unit z, sets w_i=(a_i^T z)^2, and uses sum_i w_i=1, max_i w_i<=L^2/N. It gives N^(-1)sum_i(w_i-1/N)^2<=(L^2-1)/N^2, the round-5 variance scale. The matrix calculation (15) extends this scale to the complete eigenspace. For m=1, (16) is exactly the earlier scalar estimate, with no net constant. Substituting t=kr/N in (16) independently verifies both the 2 in the quadratic denominator and the kr/3 linear term of (2).

For uniform simple labelled random regular graphs, label invariance is exact. Jiaoyang Huang and Horng-Tzer Yau, *Spectrum of Random d-regular Graphs Up to the Edge*, [arXiv:2102.00963v3](https://arxiv.org/html/2102.00963v3), Theorem 1.4 and its following unconditional-event paragraph, supply (1) for every fixed d>=3 with L_N a fixed power of log N and epsilon_N->0. Their resolvent control bounds every vector in an eigenspace: by the spectral theorem, at any eigenvalue lambda, |u_i|^2<=eta Im G_ii(lambda+i eta) for every normalized u in its eigenspace. Scaling adjacency by a nonzero constant leaves eigenvectors unchanged. Therefore (2)–(4) apply. If L_N<=(log N)^c, it suffices that k_N/(log N)^(2c+1)->infinity. No value for the hidden published exponent c or stronger unconditional failure probability is asserted.

The earlier obstructions remain: neither singleton QUE nor graph-dependent sets follow from (1) and label symmetry. The round-5 block-Walsh ensemble has N=s^2, L^2=s, and a designated simple eigenvector flat on s coordinates. A prescribed set of size s misses that support with probability binom(s^2-s,s)/binom(s^2,s)->e^(-1); relative discrepancy is then 1. These are abstract symmetric-matrix examples, not regular graphs. Equation (4) is sufficient, not asserted necessary; this proof does not establish optimality of its logarithm or cover graph-dependent balls. It also does not validate the OpenAI bulk-universality proof.
