# Exact linear-hub endpoint for two or more original coordinates

**Status:** proved sufficient theorem. It improves the constant of the recent two-hub zero-self-block branch; it does not apply when the hub-hub quadratic block is nonzero.

Let \(H_1,\ldots,H_k\) be independent ORIGINAL coordinates, each with probability density bounded by one, and let \(W\) be independent of them. Suppose the vector \(L(W)=(L_1(W),\ldots,L_k(W))\) has a joint density bounded by \(M<\infty\). Let \(R(W)\) be any real measurable function, \(\beta\in\mathbb R^k\), and
\[
 Q=2\sum_{i=1}^k H_i(L_i(W)+\beta_i)+R(W).
\]
For every integer \(k\ge2\), \(Q\) has a density in \(C_0(\mathbb R)\) and
\[
 \|p_Q\|_\infty\le \frac{k}{k-1}M^{1/k}. \tag{1}
\]
The case \(k=2\) gives \(2\sqrt M\). If \(L=TW\), where \(W\) is a cap-one product vector and the \(k\times n\) matrix \(T\) has singular values \(s_1,\ldots,s_k>0\), the Livshyts–Paouris–Pivovarov projection theorem gives
\[
 \|p_Q\|_\infty\le \frac{k\sqrt2}{k-1}(s_1\cdots s_k)^{-1/k}. \tag{2}
\]
In particular, two original hubs and a rank-two crossing \(T\) give \(2\sqrt2/\sqrt{s_1s_2}\), with an arbitrary dense quadratic or measurable remainder \(R(W)\).

**Proof.** Condition on \(W=w\), and put \(a_i=L_i(w)+\beta_i\). If \(a_i\ne0\), the conditional density of \(2a_iH_i\) is bounded by \(1/(2|a_i|)\). Convolution with the other independent scaled hubs cannot increase this bound. Therefore, whenever \(a\ne0\), the conditional density of \(Q\) is bounded by \(1/(2\|a\|_\infty)\). Since \(L\) has a joint density, \(a=0\) occurs with probability zero. Layer cake and the \(k\)-dimensional density cap yield
\[
 \begin{aligned}
 \mathbb E\frac1{2\|L+\beta\|_\infty}
 &=\int_0^\infty \mathbb P\!\left(\|L+\beta\|_\infty<\frac1{2t}\right)\,dt\\
 &\le\int_0^\infty\min(1,Mt^{-k})\,dt
 =\frac{k}{k-1}M^{1/k}.
 \end{aligned}
\]
This also dominates the output law by the right side of (1) times Lebesgue measure. Almost surely at least two \(a_i\)'s are nonzero. The conditional convolution of their scaled \(L^1\cap L^\infty\) densities belongs to \(C_0\); translation continuity in \(L^1\) proves this directly. The displayed integrable envelope permits dominated convergence as the output level varies or tends to infinity, so the averaged density belongs to \(C_0\). Formula (2) follows from \(\|p_{TW}\|_\infty\le 2^{k/2}/(s_1\cdots s_k)\). \(\square\)

For hub caps \(c_i\) instead of one, the same argument gives \((k/(k-1))(M\prod_i c_i)^{1/k}\) after rescaling the partners. No moment, support, or smoothness assumption is used.

**Scope and prior record:** the \(k>2\) Fourier result is in manuscript/hubs.tex, Theorem thm:hub-many. A recent exact two-original-hub result appears at proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T180936Z-account01-B01-qform-auto11/REPORT.md. The present proof makes the linear two-hub endpoint direct and improves its constant. A quadratic \(H^{\mathsf T}BH\), however small, is outside (1). The unrestricted \(s_3(A)\ge1\) theorem and the adapted one-hub leakage case remain open.
