# A variance-sensitive bound for prescribed vertex sets

## Statement

Let B be a random real symmetric N by N matrix, N>=2, whose law is invariant under conjugation by permutation matrices. Suppose that, outside an event of probability epsilon, every unit eigenvector, including every unit vector in every repeated eigenspace, satisfies
\[
 \|u\|_\infty\le L/\sqrt N,\qquad L\ge1.                 \tag{1}
\]
Suppose also that each eigenspace has dimension at most a deterministic integer M on this event. One may always take M=min(N,floor(L^2)). Fix a deterministic vertex set S of size 1<=k<N, put q=min(k,N-k), and let r>0. Then
\[
 \mathbb P\left\{
 \sup_{Bu=\lambda u,\ \|u\|_2=1}
 \left|\frac Nk\sum_{i\in S}|u_i|^2-1\right|>r\right\}
 \le \varepsilon+2N9^M
 \exp\left[-\frac{k^2r^2}{8L^2(q+kr/6)}\right].          \tag{2}
\]
The right side may of course be replaced by its minimum with 1. The case k=N has identically zero error; relative error is undefined when k=0. The supremum includes complex unit eigenvectors if desired.

For D>0 set
\[
 x=M\log9+(D+1)\log N,\qquad
 r_* =\frac{\sqrt{8qL^2x}}k+\frac{4L^2x}{3k}.             \tag{3}
\]
The probability of relative discrepancy greater than r_* is at most epsilon+2N^(-D). Consequently, for sequences with epsilon_N tending to zero, it suffices that
\[
 \frac{k_N}{L_N^2(M_N+\log N)}\longrightarrow\infty.       \tag{4}
\]
Without an additional multiplicity bound, the sufficient condition is k_N/[L_N^2(L_N^2+log N)] tending to infinity. This improves the round-4 sufficient condition k_N/(L_N^8 log N) tending to infinity. Each set is prescribed before B is sampled.

## 1. Exponential moments for sampling without replacement

For nonnegative numbers a_1,...,a_N, let e_q(a) be their elementary symmetric polynomial of degree q. For 1<=q<=N,
\[
 \frac{e_q(a)}{\binom Nq}\le
       \left(\frac1N\sum_i a_i\right)^q.                 \tag{5}
\]
Here is a proof. Fix the sum A. If A=0 there is nothing to show; q=1 is equality. For q>=2, maximize e_q on the compact nonnegative simplex of sum A. The maximum is positive, since the equal tuple has positive e_q, so a maximizing tuple has at least q positive entries. Holding all other entries fixed, write
\[
 e_q(a)=a_i a_j e_{q-2}(a_{\widehat{i,j}})
       +(a_i+a_j)e_{q-1}(a_{\widehat{i,j}})
       +e_q(a_{\widehat{i,j}}).
\]
If a_i!=a_j, replacing both by (a_i+a_j)/2 strictly increases their product. There are at least q-2 positive remaining entries, so e_{q-2}>0 (with e_0=1). This contradicts maximality. Thus the maximum occurs at the equal tuple, proving (5).

Let z_1,...,z_N have mean zero, |z_i|<=b, and mean square v=N^(-1)sum_i z_i^2. Let R be a uniform q-subset. Substitution a_i=exp(theta z_i) in (5), for either sign of theta, gives
\[
 \mathbb E_R\exp\left(\theta\sum_{i\in R}z_i\right)
 \le \left(\frac1N\sum_i e^{\theta z_i}\right)^q.         \tag{6}
\]
Thus no independence of the sampled coordinates is assumed.

For |theta|b<3, expand the scalar exponential and use the mean-zero property:
\[
 \frac1N\sum_i e^{\theta z_i}
 \le 1+v\sum_{j=2}^\infty
          \frac{|\theta|^j b^{j-2}}{j!}
 \le 1+\frac{v\theta^2}{2(1-b|\theta|/3)}
 \le \exp\left(\frac{v\theta^2}{2(1-b|\theta|/3)}\right).
                                                               \tag{7}
\]
The factorial inequality j!>=2*3^(j-2) follows by induction from j=2, since the next multiplier is at least 3. The first inequality in (7) follows from |z_i|^j<=b^(j-2)z_i^2, so it applies even when an odd moment has the opposite sign.

For v>0 choose theta=t/(qv+bt/3) in exponential Markov, with t>0. This satisfies theta b<3. Equations (6)-(7) yield an upper tail exp[-t^2/(2(qv+bt/3))]. Apply the same argument to -z for the lower tail:
\[
 \mathbb P_R\left\{\left|\sum_{i\in R}z_i\right|>t\right\}
 \le 2\exp\left[-\frac{t^2}{2(qv+bt/3)}\right].          \tag{8}
\]
If v=0 all z_i vanish and the probability is zero. The formula with positive upper bounds on b and v remains valid.

## 2. Variance of eigenvector mass

Fix a realization satisfying (1), and fix any real unit vector u in one of its eigenspaces, before selecting R. Put w_i=u_i^2, so 0<=w_i<=L^2/N and sum_i w_i=1. For z_i=w_i-1/N,
\[
 |z_i|\le L^2/N,\qquad
 v=\frac1N\sum_i w_i^2-\frac1{N^2}
 \le\frac{L^2-1}{N^2}\le\frac{L^2}{N^2}.                \tag{9}
\]
The key bound is sum_i w_i^2<=max_i w_i sum_i w_i<=L^2/N. Unlike a bound using only |w_i|, it retains the normalization sum_i w_i=1.

For a uniform k-subset R, use (8) directly if k<=N/2 and use its complement otherwise. The two centered masses are negatives of one another, since sum_i z_i=0. With q=min(k,N-k) this gives
\[
 \mathbb P_R\left\{
 \left|\sum_{i\in R}u_i^2-\frac kN\right|>t\right\}
 \le 2\exp\left[-\frac{N^2t^2}
                         {2L^2(q+Nt/3)}\right].        \tag{10}
\]
This step uses the all-unit-eigenvector assumption for the chosen direction, not just a single basis in each eigenspace.

## 3. A net in each eigenspace

For an eigenspace V of dimension m, choose an orthonormal real basis and write U for the N by m matrix of its columns. Define the symmetric compression
\[
 C_V(R)=U^T\operatorname{diag}(1_R)U-(k/N)I_m.
\]
For a real unit coefficient vector y, its quadratic form is the centered mass of the unit eigenvector Uy, so (10) applies to y^T C_V(R)y.

There is a 1/4-net T of the real unit sphere with |T|<=9^m. To see this, take a maximal set of sphere points at mutual distance greater than 1/4. Their open balls of radius 1/8 are disjoint and lie inside the ball of radius 9/8. Volume comparison bounds the number by 9^m. A greedy selection must terminate within that bound, and maximality gives the covering property. The net is selected before R.

For a real symmetric m by m matrix C, let z be a real unit eigenvector whose eigenvalue has modulus ||C||. Choose y in T with ||z-y||<=1/4. Then
\[
 |z^TCz-y^TCy|
 \le |(z-y)^TCz|+|y^TC(z-y)|
 \le\tfrac12\|C\|.
\]
It follows that
\[
 \|C\|\le 2\max_{y\in T}|y^TCy|.                        \tag{11}
\]
The same operator norm controls complex quadratic forms: a real symmetric matrix has a real orthogonal diagonalization, and a complex unit vector's quadratic form is a convex combination of its real eigenvalues.

Take t=kr/(2N) in (10). If every net quadratic form has modulus at most t, (11) bounds all relative discrepancies in V by r. There are at most N distinct eigenspaces, each of dimension at most M. A union bound therefore gives conditional failure probability at most
\[
 2\sum_V9^{\dim V}
 \exp\left[-\frac{k^2r^2}{8L^2(q+kr/6)}\right]
 \le 2N9^M\exp\left[-\frac{k^2r^2}{8L^2(q+kr/6)}\right]. \tag{12}
\]

For completeness, (1) implies the asserted multiplicity bound. If Q_V is the orthogonal projection onto V, then
\[
 Q_V(i,i)=\sup_{u\in V,\ \|u\|=1}|u_i|^2\le L^2/N.
\]
This identity follows from u_i=<Q_V e_i,u>, with equality attained by normalizing Q_V e_i when it is nonzero. Summing over i gives dim V=tr Q_V<=L^2.

## 4. Restore the random labels and derive the error scale

Let pi be an independent uniform permutation and P_pi e_i=e_{pi(i)}. The mass of P_pi u on the prescribed set S equals the mass of u on pi^(-1)(S), a uniform k-subset conditional on B. Thus (12) controls the probability for P_pi B P_pi^T on each good realization B. On the exceptional event use the bound 1. Permutation invariance of the matrix law proves (2). No equivariant choice of eigenbasis or net is required, since the bound holds conditional on each B for any such choices.

To verify (3), write a=8qL^2x and b=(4/3)L^2x. For A=kr_*=sqrt(a)+b,
\[
 A^2-bA-a=b\sqrt a\ge0.
\]
Therefore A^2>=8L^2x(q+A/6), so the exponent in (2) is at least x. The remaining factor is
\[
 2N9^M e^{-x}=2N^{-D}.
\]
Since q<=k, (3) is at most sqrt(8L^2x/k)+4L^2x/(3k), which tends to zero under (4).

If the spectrum is simple on the good event, no net is needed: one real unit eigenvector per eigenvalue covers every unit vector up to a scalar phase. Taking t=kr/N directly in (10) yields the stronger bound
\[
 \varepsilon+2N
 \exp\left[-\frac{k^2r^2}{2L^2(q+kr/3)}\right].          \tag{13}
\]
Thus k/(L^2 log N) tending to infinity suffices in that additional case. No simple-spectrum assertion for random regular graphs is being imported here.

## 5. Independent checks and limits

There are two separate ways to check the variance scale. First, (9) follows directly from positivity and normalization. Second, if I_i indicates membership in a uniform q-subset, direct counting gives E I_i=q/N and E I_i I_j=q(q-1)/(N(N-1)) for i!=j. Expanding the square gives
\[
 \operatorname{Var}\sum_{i\in R}z_i
       =\frac{q(N-q)}{N-1}\,v.                           \tag{14}
\]
The covariances of two distinct ordered draws also equal -v/(N-1); summing q variances and q(q-1) covariances reproduces (14). The qv in (8) is an upper bound on (14), so losing the finite-population correction is in the safe direction. Complementing the set restores q=min(k,N-k) in both approaches.

The constants in (2) can be checked directly without (3): substitute t=kr/(2N) into N^2t^2/[2L^2(q+Nt/3)]. This gives k^2r^2/[8L^2(q+kr/6)]. The factor 2 in the denominator of t comes only from the 1/4-net estimate. Equation (13) checks that removing that factor changes both the quadratic constant and the linear term as expected.

A lower-scale obstruction is explicit. For any integer h>=1 set s=2^h and N=s^2. Take a block-diagonal orthogonal matrix with s copies of a normalized s by s Walsh matrix, assign distinct eigenvalues to all its columns, and conjugate the resulting real symmetric matrix by a uniform label permutation. Its spectrum is simple; each eigenvector is flat on one block of s coordinates, so L^2=s. Let k=s and prescribe any k-subset. The event that S misses the support of the eigenvector with the least eigenvalue has probability
\[
 p_s=\frac{\binom{s^2-s}{s}}{\binom{s^2}{s}}
     =\prod_{j=0}^{s-1}\left(1-\frac{s}{s^2-j}\right)
     \longrightarrow e^{-1}.                            \tag{15}
\]
Indeed the maximum of the subtracted fractions tends to zero, their sum tends to 1 by bounding each between 1/s and s/(s^2-s+1), and the sum of their squares tends to zero. The Taylor estimate log(1-x)=-x+O(x^2), uniform for x<=1/2, proves the limit. On this event the relative discrepancy is 1. Thus even with simple spectrum, bounded k/L^2 does not suffice in general. This is a counterexample ensemble for the abstract hypotheses, not a regular graph.

For fixed L=sqrt(2), the round-4 Walsh construction also gives discrepancy 1 on every singleton. Choosing a set after observing an eigenvector's support gives discrepancy 1 on a set of size N/2. Nothing in (2) permits graph-dependent sets, a simultaneous supremum over every set, or singleton equidistribution.

For uniform simple labelled random regular graphs, permutation invariance is exact. Jiaoyang Huang and Horng-Tzer Yau, *Spectrum of Random d-regular Graphs Up to the Edge*, [arXiv:2102.00963v3](https://arxiv.org/html/2102.00963v3), Theorem 1.4 and its following unconditional-event discussion, supply (1) for every fixed d>=3 with L_N a fixed power of log N and epsilon_N tending to zero. Their resolvent proof bounds every vector in each eigenspace; a scalar normalization of adjacency leaves its eigenvectors unchanged. Hence (4) applies with M_N<=L_N^2. If L_N<=(log N)^c, a sufficient condition is
\[
 k_N/\bigl((\log N)^{4c}+(\log N)^{2c+1}\bigr)
       \longrightarrow\infty.                          \tag{16}
\]
This replaces the earlier exponent 8c+1 by max(4c,2c+1), with no numerical value assigned to the published hidden exponent c. The exceptional-graph probability epsilon_N is retained. This is a quantitative consequence of existing inputs; no novelty or validation of the OpenAI universality proof is asserted.
