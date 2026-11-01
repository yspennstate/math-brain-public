# Exact rank three with finitely many physical row directions

**Status:** A dimension-independent, all-signature original-product density theorem for exact rank three with at most a fixed number of physical eigenframe directions. Arbitrary independent cap-one laws, unbounded tails, and mixed signs are included. The constant depends on the number of distinct directions, so the unrestricted case remains open.

Let \(A\in\mathbb R^{n\times n}\) be real symmetric of exact rank three, \(s_3(A)\ge1\), and write \(A=U\Lambda U^\top\), \(U^\top U=I_3\), with \(\Lambda\) invertible. Assume the nonzero row vectors \(U_{i,*}\in\mathbb R^3\) lie in the union of at most \(K\) one-dimensional subspaces through the origin. Then for independent real original-coordinate inputs \(X_i\) with densities bounded by one,
\[
 \|p_{X^\top AX}\|_\infty\le2{K\choose3}C_3,
 \tag{1}
\]
where \(C_3\) is the universal constant for all signed invertible quadratic forms in three independent cap-one originals with arbitrary affine terms. In particular, a four-direction frame obeys \(\|p_Q\|_\infty\le8C_3\), uniformly in the ambient dimension \(n\).

**Proof.** Partition the nonzero physical rows into disjoint groups \(G_1,\ldots,G_k\), \(3\le k\le K\), by their projective direction. Choose a unit direction \(r_g\in\mathbb R^3\) for each group, and write \(U_{i,*}=a_i r_g^\top\) for \(i\in G_g\), allowing either sign of \(a_i\). Set \(c_g=(\sum_{i\in G_g}a_i^2)^{1/2}\) and
\[
 Y_g={1\over c_g}\sum_{i\in G_g}a_iX_i,
 \qquad R_{g,*}=c_gr_g^\top.
\]
The variables \(Y_g\) are independent because their groups consist of disjoint original coordinates, and each \(Y_g\) is a normalized one-dimensional projection of independent cap-one originals, so \(\|f_{Y_g}\|_\infty\le\sqrt2\). In matrix notation \(U^\top X=R^\top Y\), and \(R^\top R=U^\top U=I_3\). Thus
\[
 X^\top AX=Y^\top(R\Lambda R^\top)Y.
\]
The \(k\times k\) matrix \(B=R\Lambda R^\top\) has exactly the same three nonzero eigenvalues as \(A\), including their signs. Put \(Z_g=\sqrt2Y_g\). Each independent \(Z_g\) has density bounded by one and
\[
 X^\top AX=Z^\top(B/2)Z,
 \qquad s_3(B/2)\ge1/2.
\]
Apply the exact-rank-three fixed-\(k\)-dimension theorem \(\|p_{Z^\top C Z}\|_\infty\le {k\choose3}C_3/s_3(C)\) to obtain \(2{k\choose3}C_3\le2{K\choose3}C_3\). Zero rows of \(U\) do not enter the quadratic and may be ignored.

This is a genuine-product result: physical originals are grouped only along **exactly collinear** frame rows, producing independent aggregated scalars. Approximate row collinearity alone does not allow this reduction for arbitrary unbounded original laws, because a small coefficient mismatch can multiply an arbitrarily large input.

The fixed-dimension lemma was proved in `proofnet24/QFORM-density/interactive/20260923T220500Z-exact-rank3-fixed-dimension/REPORT.md`; it uses the complete signed three-original-coordinate theorem and a Cauchy–Binet selection of one physical triple.
