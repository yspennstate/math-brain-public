# Small-leakage Fourier obstruction for abstract full-3D banks

This addendum tests the strict coefficient relation \(\beta=0\), \(\varepsilon>0\) while retaining two independent full-dimensional light banks. It shows that full-3D bank density caps, even together with caps on the displayed \((L,V)\) bank marginals, do not yield a Fourier power-decay bound uniform as \(\varepsilon\downarrow0\). The construction is **not** a genuine orthonormal projection of capped original coordinates; that distinction is explicit below. It does not challenge the density conjecture.

Fix a large frequency \(t\) and let \(\varepsilon=t^{-3}\). In each independent bank \(j=A,B\), let
\[
L_j\sim{\rm Unif}[-8,8],\qquad
V_j,E_j\sim{\rm Unif}[-1/2,1/2]
\]
be independent, and define \(P_j=L_j/\varepsilon+E_j\). The map \((L_j,V_j,E_j)\mapsto(L_j,V_j,P_j)\) has determinant one, so each bank's full-3D density is bounded by \(1/16\). The \((L_j,V_j)\) marginal also has cap \(1/16\).

Let \(L=L_A+L_B\), \(V=V_A+V_B\), \(P=P_A+P_B\), and take an independent cap-one hub \(H\). The pure canonical quadratic expression is
\[
Q_\varepsilon=2HL+V^2+2\varepsilon LP
=Q_0+2\varepsilon L(E_A+E_B),
\qquad
Q_0=2HL+2L^2+V^2.
\]
Choose \(H\) with density \(1_{E_t}\), where \(E_t\subset[-4,4]\) has measure one and \(\cos(t h^2/2)\ge1/\sqrt2\) on \(E_t\). Such a set exists for large \(t\) by the periodic-mean argument in the main report.

Set \(S=L_A+L_B\), \(T=V_A+V_B\). Since
\[
Q_0=2(S+H/2)^2-H^2/2+T^2,
\]
the same uniform Fresnel calculation gives
\[
\mathbb E e^{itQ_0}
=i\,\frac{\pi}{\sqrt2\,t}
\int_{E_t}g_S(-h/2)e^{-ith^2/2}\,dh+o(t^{-1}).
\]
Here \(g_S(s)=(16-|s|)_+/256\), hence \(g_S(-h/2)\ge14/256\) for \(|h|\le4\). Therefore \(|\mathbb E e^{itQ_0}|\ge c/t\) for an absolute \(c>0\). As \(|L|\le16\) and \(|E_A+E_B|\le1\),
\[
\left|\mathbb E e^{itQ_\varepsilon}-\mathbb E e^{itQ_0}\right|
\le 2t\varepsilon\,\mathbb E|L(E_A+E_B)|
\le32t\varepsilon=32t^{-2}.
\]
Thus \(|\mathbb E e^{itQ_\varepsilon}|\ge c'/t\) for every sufficiently large prescribed \(t\), with \(\varepsilon=t^{-3}>0\).

**Why this does not transfer to the original-product frame.** These banks satisfy \(P_j-L_j/\varepsilon=E_j\); equivalently \(\varepsilon P-L=\varepsilon(E_A+E_B)\), so
\[
\Pr\{|\varepsilon P-L|\le\varepsilon\}=1.
\]
In a genuine orthonormal light frame, the coefficient vectors of \(L\) and \(P\) are orthogonal unit vectors in the original-coordinate space. Standard one-dimensional product projection caps then give, for independent cap-one originals,
\[
\Pr\{|\varepsilon P-L|\le r\}\le
\frac{2\sqrt2\,r}{\sqrt{1+\varepsilon^2}},
\]
which is incompatible with the displayed concentration when \(r=\varepsilon\) is small. The abstract bank law therefore loses exactly the oblique projection control supplied by the original product provenance.
