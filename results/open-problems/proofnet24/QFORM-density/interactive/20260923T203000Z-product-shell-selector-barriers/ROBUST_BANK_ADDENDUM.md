# Robust-bank version of the shell selector barrier

This extends the [single-original selector result](REPORT.md) to any physical selector bank whose removal leaves a quantitatively full three-dimensional light frame. It still does not address collective selectors that nearly exhaust a frame direction.

Let \(U\) be an orthonormal \(n\times3\) frame, \(Z=U^\top X=(L,V,P)\), and let the original \(X_i\) be independent with density caps \(1\). Choose a subset \(S\) of original coordinates such that
\[
G_S=\sum_{i\in S}u_i u_i^\top\preceq(1-c)I_3,
\qquad 0<c\le1.
\]
After conditioning all \(X_S\), the unconditioned complement is a translate of a three-dimensional projection whose frame Gram is
\(C_S=I_3-G_S\succeq cI_3\). Normalizing this frame and applying the dimension-three Livshyts--Paouris--Pivovarov cap gives
\[
\|p_{Z\mid X_S=x_S}\|_\infty
\le \frac{2^{3/2}}{\sqrt{\det C_S}}
\le 2^{3/2}c^{-3/2}=:M_c,
\]
uniformly in the conditioned values.

Let \(B_k\) be disjoint events measurable with respect to the selector bank \(X_S\), and put \(b_k=\Pr(B_k)\), so \(\sum b_k\le1\). Let \(E_k\) be the graph shells
\[
E_k=\{a_k\le l\le1,\ 0\le v\le1,\
|p+c_k+(1+v^2)/(2l)|\le a_k/2\},
\qquad 0<a_k<1.
\]
The subdensity of \(Z\) associated with \(B_k\) is bounded by \(M_cb_k\). For an independent cap-one hub \(H\), the contribution of \(B_k\) and \(Z\in E_k\) to the density of \(Q=2HL+V^2+2LP\) at any target is therefore at most
\[
\int_{E_k}\frac{M_cb_k}{2l}\,dl\,dv\,dp
=\frac{M_c}{2}b_k a_k\log(1/a_k).
\]
Using \(a\log(1/a)\le1/e\) and summing disjoint bank events gives the uniform bound
\[
\sum_k p_{Q;\,B_k,\,E_k}(s)\le\frac{M_c}{2e}
\quad\text{for every target }s.
\]

For a single original coordinate under the max-row-leverage-\(1/2\) gate, \(C_S=I-u_i u_i^\top\) has determinant at least \(1/2\), giving the sharper numerical cap \(M_c\le4\) in the main report. The bank statement shows exactly where a readable-shell-label construction could escape this argument: its selector bank must have \(\lambda_{\max}(G_S)\to1\), exhausting a light-frame direction so the conditional complement loses its uniform three-dimensional density cap.
