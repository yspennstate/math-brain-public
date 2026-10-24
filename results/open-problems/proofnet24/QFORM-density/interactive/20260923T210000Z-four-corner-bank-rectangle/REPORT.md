# A quantitative four-corner obstruction for product light banks

**Status.** This is a proved inverse-geometry lemma for the unresolved exact-hub canonical form. It excludes concentration on a complete Cartesian rectangle of independent bank values. It does **not** bound the full near-level edge graph and does **not** prove the QFORM density conjecture or the dyadic weak-\(L^2\) target.

## The lemma

Let \(A,B\in\mathbb R^3\) be independent random vectors. Suppose the density of every one-dimensional orthogonal projection of \(A\) is at most \(M_A\), and likewise every one-dimensional projection of \(B\) is at most \(M_B\). Let \(C=C^T\) be any \(3\times3\) real matrix. Fix any affine function \(\ell\), constant \(c\), and interval \(I\) of length \(\delta\). Let \(S_A,S_B\) be bank events with probabilities \(\alpha,\theta>0\). If

\[
 (a+b)^TC(a+b)+\ell(a+b)+c\in I
 \quad\text{for almost every }(a,b)\in S_A\times S_B,
\]

then

\[
 \alpha\theta\le \frac{24M_A M_B}{\|C\|_F}\,\delta. \tag{1}
\]

The assertion is vacuous for \(C=0\). It requires neither moments nor support bounds.

For the canonical light form
\[
 q_h(l,v,p)=2hl+\beta l^2+v^2+2\varepsilon lp,
 \qquad
 C=\begin{pmatrix}\beta&0&\varepsilon\\0&1&0\\\varepsilon&0&0\end{pmatrix},
\]
we have \(\|C\|_F=\sqrt{1+\beta^2+2\varepsilon^2}\ge1\). Hence \(\alpha\theta\le24M_AM_B\delta\), uniformly in the hub value, leakage, and \(\beta\). The spectral condition \(|\beta|\le\varepsilon^2\) is not needed for this lemma.

## Proof

We use the elementary variance fact: a probability density on \(\mathbb R\) bounded by \(K\) has variance at least \(1/(12K^2)\). Translate to the mean and use the bathtub principle: among densities bounded by \(K\) with mass one, the centered second moment is minimized by \(K\mathbf1_{[-1/(2K),1/(2K)]}\). This also proves the claim if the original variance is infinite.

Condition \(A\) on \(S_A\) and then restrict to a bounded subset of that conditional event having conditional mass at least \(1/2\). Write \(A'\) for the resulting normalized bounded law. Every unit-direction marginal of \(A'\) has density at most \(2M_A/\alpha\), since restriction can only lower the unnormalized marginal. Therefore
\[
 \operatorname{Cov}(A')\succeq \frac{\alpha^2}{48M_A^2}I_3.
\]
The same construction gives a bounded \(B'\) with
\[
 \operatorname{Cov}(B')\succeq \frac{\theta^2}{48M_B^2}I_3.
\]
The stipulated near-level property persists on these restricted events.

Take independent copies \(a_1,a_2\) of \(A'\) and \(b_1,b_2\) of \(B'\). The four-corner difference is
\[
 D=q(a_1+b_1)+q(a_2+b_2)-q(a_1+b_2)-q(a_2+b_1)
   =2(a_1-a_2)^TC(b_1-b_2).
\]
Each of the four \(q\)-values lies in \(I\), so \(|D|\le2\delta\) almost surely. Independence and centering of the differences give
\[
 \begin{aligned}
 \mathbb E D^2
 &=16\operatorname{tr}\!\left(
      C\operatorname{Cov}(B')C^T\operatorname{Cov}(A')\right)\\
 &\ge \frac{\alpha^2\theta^2}{144M_A^2M_B^2}\|C\|_F^2.
 \end{aligned}
\]
Combining with \(\mathbb E D^2\le4\delta^2\) proves (1).

## Application and remaining gap

For an orthonormal physical light frame, split the independent original coordinates into banks \(A,B\). If each bank frame Gram matrix is at least \(\lambda I_3\), the one-dimensional product projection inequality gives \(M_A,M_B\le\sqrt{2/\lambda}\). In particular, a balanced split with \(\lambda\ge1/4\) gives \(\alpha\theta\le192\delta\). This bound stays uniform even when each physical row is diffuse and no single three-row minor is large.

The dependent-light curved shell counterexample can track the level set across many \(L\)-scales, but independent banks cannot place positive product mass on an entire thin-shell rectangle without paying (1). A general near-level event is a **bipartite edge set**, however: only selected \((a,b)\) pairs may land in the shell. An edge set of substantial measure need not contain a complete rectangle of comparable product measure. Turning (1) into an edge-density or dyadic weak-\(L^2\) estimate is the missing inverse step. In particular, this report does not rule out a genuine-product counterexample to the stronger dyadic target, and none is presently known.

See the [precise open dyadic target](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T205500Z-dyadic-rw2-hub-target/REPORT.md) and the [dependent-light fake](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T203400Z-negative-target-projection-fake/REPORT.md).
