# Self-covariance concentration for a cubic activation

Let \(d,k\geq1\), let the rows \(w_1,\ldots,w_k\) of \(W\) be independent \(N(0,I_d)\), and independently let \(X\sim N(0,I_d)\). Set

\[
 \varphi(z)=\frac{z^3-3z}{\sqrt6},\qquad
 F_W(X)=\frac1{\sqrt k}\sum_{i=1}^k\varphi(w_i\cdot X/\sqrt d).
\]

In the convention \(\mu_\ell=\mathbb E[\varphi(Z)\operatorname{He}_\ell(Z)]\), this activation has \(\mu_0=\mu_1=\mu_2=0\), \(\mu_3=\sqrt6\), and kernel \(g(q)=q^3\). Introduce

\[
 u_i=w_i/\sqrt d,\quad r_i=\|u_i\|^2,\quad q_{ij}=u_i\cdot u_j,\qquad
 C(W)=\frac1k\sum_{i,j}q_{ij}^3,
 \quad V(W)=\operatorname{Var}_X(F_W(X)\mid W).
\]

For integers \(p\geq0\) write

\[
 M_p=\prod_{a=0}^{p-1}\left(1+\frac{2a}{d}\right),\qquad M_0=1,
\]

and define

\[
 b=M_3-2M_2+M_1=\frac2d+\frac8{d^2},
 \qquad h=M_6-4M_5+6M_4-4M_3+M_2.
\]

**Proposition.** The following are exact finite-dimensional identities:

\[
\begin{split}
 V(W)&=C(W)+B(W),\\
 B(W)&=\frac{3}{2k}\left\|\sum_i(r_i-1)u_i\right\|^2\geq0,\\
 \mathbb EC&=M_3=1+\frac6d+\frac8{d^2},\\
 A_{d,k}:=\mathbb E(C-1)^2
  &=(M_3-1)^2+\frac{M_6-M_3^2}{k}
      +\frac{30(k-1)}{k d^3}M_3,\\
 \mathbb EB&=\frac32 b=\frac3d+\frac{12}{d^2},\\
 D_{d,k}:=\mathbb EB^2
  &=\frac94\left[\frac hk+
       \frac{k-1}{k}\left(1+\frac2d\right)b^2\right].
\end{split}
\]

Consequently

\[
 \mathbb EV=1+\frac9d+\frac{20}{d^2},\qquad
 \mathbb E(V-1)^2\leq(\sqrt{A_{d,k}}+\sqrt{D_{d,k}})^2.
\]

If \(k/d\to\gamma\in(0,\infty)\), both \(\mathbb E(C-1)^2\) and \(\mathbb E(V-1)^2\) are \(O(d^{-2})\). More explicitly,

\[
 d^2 A_{d,k}\longrightarrow36+18/\gamma,
 \qquad d^2 D_{d,k}\longrightarrow9,
\]

so

\[
 d^2\mathbb E(V-1)^2\longrightarrow81+18/\gamma.
\]

## Proof

For fixed \(W\), each \(u_i\cdot X\) is symmetric, so \(\mathbb E_XF_W=0\). If \((A_1,A_2)\) is a centered Gaussian pair with variances \(r,s\) and covariance \(q\), pairing its factors gives

\[
 \mathbb EA_1^3A_2^3=9rsq+6q^3,\qquad
 \mathbb EA_1^3A_2=3rq,\qquad
 \mathbb EA_1A_2^3=3sq.
\]

There are six pairings having three cross pairs and nine having one cross pair in the first identity. In the second and third identities the single variable can pair with any of three factors. Expanding the two cubic polynomials therefore yields

\[
 \mathbb E[\varphi(A_1)\varphi(A_2)]
 =q^3+\frac32(r-1)(s-1)q.
\]

Apply this to \((u_i\cdot X,u_j\cdot X)\) and sum over \(i,j\). The second term is a Gram quadratic form, giving \(V=C+B\) as stated. The term \(B\) is absent if the row norms are exactly \(\sqrt d\), but not for Gaussian rows.

The moment generating function of \(dr_i=\sum_{a=1}^d w_{ia}^2\) is \((1-2t)^{-d/2}\) for \(t<1/2\), obtained by multiplying the one-coordinate Gaussian integrals. Differentiating \(p\) times at zero shows that \(\mathbb Er_i^p=M_p\).

Split

\[
 C=C_{\rm diag}+C_{\rm off},\qquad
 C_{\rm diag}=\frac1k\sum_i r_i^3,\quad
 C_{\rm off}=\frac2k\sum_{i<j}q_{ij}^3.
\]

Negating either row in \(q_{ij}^3\) changes its sign and preserves the row distribution. Thus \(\mathbb E q_{ij}^3=0\), and every diagonal term is uncorrelated with every off-diagonal term. Two distinct off-diagonal unordered pairs are also uncorrelated: if they are disjoint use independence, and if they share a row, negate a row occurring in only one of the pairs. Independence of the diagonal terms now gives

\[
 \mathbb EC=M_3,\qquad
 \operatorname{Var}(C)=\frac{M_6-M_3^2}{k}
      +\frac4{k^2}\binom k2\mathbb E q_{12}^6.
\]

Conditional on \(u_1\), the variable \(q_{12}\) is normal with variance \(r_1/d\). Its sixth moment is \(15(r_1/d)^3\), hence

\[
 \mathbb E q_{12}^6=\frac{15}{d^3}M_3.
\]

Adding the squared bias proves the identity for \(A_{d,k}\).

For the correction term put \(v_i=(r_i-1)u_i\). These vectors are independent, centered, and rotationally invariant. Directly,

\[
 \mathbb E\|v_i\|^2=\mathbb E(r_i-1)^2r_i=b,
 \qquad \mathbb E\|v_i\|^4=\mathbb E(r_i-1)^4r_i^2=h.
\]

Rotational invariance and the trace determine \(\mathbb Ev_iv_i^\top=(b/d)I_d\), so for \(i\ne j\),

\[
 \mathbb E(v_i\cdot v_j)^2
 =\operatorname{Tr}[(bI_d/d)^2]=b^2/d.
\]

Let \(S=\sum_i v_i\), and expand

\[
 \|S\|^2=\sum_i\|v_i\|^2+2\sum_{i<j}v_i\cdot v_j.
\]

The mixed terms in its square have expectation zero by centering or row sign symmetry. Distinct unordered dot-product pairs likewise have zero expectation. Thus

\[
\begin{split}
 \mathbb E\|S\|^2&=kb,\\
 \mathbb E\|S\|^4
 &=kh+k(k-1)b^2+4\binom k2 b^2/d\\
 &=kh+k(k-1)(1+2/d)b^2.
\end{split}
\]

Multiplication by \(3/(2k)\), or its square, proves both identities for \(B\). Minkowski's inequality in \(L^2\) applied to \(V-1=(C-1)+B\) gives the asserted bound.

For clarity, the polynomials needed for the rates are

\[
\begin{split}
 M_6-M_3^2&=18/d+288/d^2+1704/d^3+4320/d^4+3840/d^5,\\
 h&=12/d^2+488/d^3+2848/d^4+3840/d^5.
\end{split}
\]

These follow by expanding the products defining \(M_p\). It follows that \((M_6-M_3^2)/k\sim18/(\gamma d^2)\), the squared bias is asymptotic to \(36/d^2\), and the off-diagonal variance is \(O(d^{-3})\). In \(D_{d,k}\), the term \(h/k\) is \(O(d^{-3})\), whereas \((9/4)(1+2/d)b^2\sim9/d^2\).

For the sharp constant for \(V\), subtract the squared mean of \(B\) from its second moment:

\[
 \operatorname{Var}(B)=\frac94\left[
    \frac{h-b^2}{k}+\frac{2(k-1)}{kd}b^2\right]=O(d^{-3}).
\]

On the other hand \(d^2\operatorname{Var}(C)\to18/\gamma\). Cauchy–Schwarz gives
\( |\operatorname{Cov}(C,B)|\leq\sqrt{\operatorname{Var}(C)\operatorname{Var}(B)}=O(d^{-5/2})\).
Hence \(d^2\operatorname{Var}(V)\to18/\gamma\). Since \(d(\mathbb EV-1)\to9\), adding the squared bias proves \(d^2\mathbb E(V-1)^2\to81+18/\gamma\).

## Interpretation for the interpolation

The self-covariance concentration condition (165) in Appendix B.6 of Jean Barbier, Francesco Camilli, Minh-Toan Nguyen, Mauro Pastore and Rudy Skerk, [*Statistical physics of deep learning: Optimal learning of a multi-layer perceptron near interpolation*, arXiv:2510.24616v5](https://arxiv.org/html/2510.24616v5#A2.SS6), concerns \(C_{**}\). For the cubic activation its displayed kernel equals \(C(W^*)\); the proposition proves that condition for Gaussian teacher weights, with rate \(O(d^{-2})\). It also proves concentration of the actual conditional variance \(V(W^*)\), including the norm correction.

At every deterministic interpolation parameter the teacher marginal remains the prior, because integrating its conditional observation distribution gives one. Therefore the expectations just bounded do not depend on that parameter, and the bounds are uniform. They also apply to a single matched posterior draw: for integrable \(H\), the tower property gives \(\mathbb E\langle H(W)\rangle=\mathbb EH(W^*)\). This does not assert concentration of a joint teacher–replica covariance.

The result is independent of sample size, hence applies in particular when \(n/d^2\to\alpha\). It neither establishes a Gaussian replacement inside the likelihood nor proves the distinct teacher–replica condition (166), the interpolation remainder estimate, a Bayes-error formula, or a gradient-descent theorem.
