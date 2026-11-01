# Exact rank three in every fixed physical dimension

**Status:** Complete, dimension-dependent theorem from the checked three-original-coordinate result. For four physical originals the constant is universal. This does not solve the dimension-uniform full conjecture.

Let \(A\) be a real symmetric \(n\times n\) matrix of **exact rank three**, with \(s_3(A)\ge1\), and let \(X_1,\ldots,X_n\) be independent original-coordinate real variables with probability densities at most one. Let \(C_3\) denote the universal density constant from the complete theorem for three independent original coordinates, including arbitrary affine terms. Then
\[
 \|p_{X^\top AX}\|_\infty\le {n\choose3}C_3.
 \tag{1}
\]
In particular, for \(n=4\), \(\|p\|_\infty\le4C_3\), uniformly in every signed rank-three \(4\times4\) matrix and every admissible product law.

**Proof.** Take an orthonormal eigenbasis \(U\in\mathbb R^{n\times3}\) for the range and write \(A=U\Lambda U^\top\), where \(\Lambda\) is invertible and \(\|\Lambda^{-1}\|\le1\). Cauchy–Binet gives
\[
 \sum_{S\subset[n],\ |S|=3}\det(U_S)^2
 =\det(U^\top U)=1.
\]
Thus some triple \(S\) has \(|\det U_S|^2\ge{n\choose3}^{-1}\). Since \(\|U_S\|\le1\), the least singular value obeys \(s_3(U_S)\ge|\det U_S|\). The physical principal compression \(B=A_{S,S}=U_S\Lambda U_S^\top\) is invertible and
\[
 \|B^{-1}\|\le\|U_S^{-1}\|^2\|\Lambda^{-1}\|
 \le|\det U_S|^{-2},\qquad
 s_3(B)\ge{n\choose3}^{-1}.
\]
Condition on the original inputs \((X_i)_{i\notin S}\). The conditional polynomial in the three independent originals \((X_i)_{i\in S}\) has quadratic matrix \(B\) and arbitrary affine and constant terms. Scale by \({n\choose3}\) and apply the complete signed three-original-coordinate theorem. Its uniform conditional density bound is \({n\choose3}C_3\); averaging over the conditioned inputs proves (1). This avoids any independence assumption after an eigenbasis rotation.

For \(n=4\), an equivalent direct proof chooses a unit null vector \(w\) and a coordinate \(j\) with \(|w_j|\ge1/2\). The complementary principal block has least singular value at least \(w_j^2s_3(A)\ge1/4\), using the least angle from the physical three-plane \(\{x_j=0\}\) to \(w^\perp\) on both sides of \(A\).

The three-original-coordinate theorem is archived at `proofnet24/QFORM-density/interactive/20260923T212800Z-complete-three-original-coordinate-theorem/REPORT.md`. Its affine-uniform form is essential: conditioning on the other physical inputs introduces a random affine term.
