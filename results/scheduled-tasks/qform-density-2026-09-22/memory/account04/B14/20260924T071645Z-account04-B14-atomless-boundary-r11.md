# Worker memory — account04/B14

Updated 20260924T071645Z.

## Durable theorem

If \(b\) is atomless and \(h_\omega\in C_0([0,\infty))\) are measurable and uniformly bounded by \(M\), then
\[
H(t)=\int1_{\{t\ge b(\omega)\}}h_\omega(t-b(\omega))\,d\pi(\omega)
\]
lies in \(C_0(\mathbb R)\) with height at most \(M\), even when \(h_\omega\) depends on \(b\). Continuity is dominated convergence away from the null level set \(\{b=t\}\); vanishing at both infinities follows from tightness of \(b\) and pointwise decay of \(h_\omega\).

This is the correct compiler for conditioning-generated translations of ruled one-sheet fibers. It does not control two-sheet/minority fibers and it requires atomlessness of the boundary.

Concrete application:
\[
Q=U^T(I_3-\tfrac23{\bf1}{\bf1}^T)U+2VW.
\]
Full interval height is at most \(6\sqrt\pi\) by account01/B14. The majority-sheet submeasure is globally \(C_0\) with height at most \(\pi\sqrt2\) because \(2VW\) is atomless.

Artifact commit: 10e3c2c60076516744368c00a83bb2f27c908298.
