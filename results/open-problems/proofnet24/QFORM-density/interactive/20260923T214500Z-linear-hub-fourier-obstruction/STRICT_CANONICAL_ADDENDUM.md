# The Fourier power-decay obstruction already occurs at the strict canonical point

The preceding report used a positive \(L^2\) coefficient and two diffuse planar light banks. A simpler example shows that a universal pointwise bound \(|\phi_Q(t)|\le C|t|^{-1-\eta}\) fails even for the strict canonical form \(\beta=\varepsilon=0\), with genuine original product coordinates and \(s_3(A)=1\). This remains a Fourier-method obstruction only; the density is bounded by direct coarea.

Let \(H,L\) be independent uniforms on \([-1/2,1/2]\). For each sufficiently large prescribed \(t>0\), choose a measurable set \(E_t\subset[-4,4]\) of measure one on which \(\cos(tv^2)\ge1/\sqrt2\), and let \(V\) have density \(1_{E_t}\), independently of \(H,L\). Such an \(E_t\) exists because
\[
\big|\{v\in[-4,4]:\cos(tv^2)\ge1/\sqrt2\}\big|\longrightarrow2.
\]
All three original-coordinate densities are bounded by one.

For
\[
Q=2HL+V^2,\qquad
A=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},
\]
the eigenvalues are \(1,1,-1\), so \(s_3(A)=1\) exactly. Independence gives
\[
\phi_Q(t)
 =\mathbb E e^{2itHL}\,\mathbb E e^{itV^2}
 =\frac{2}{t}\operatorname{Si}(t/2)\,\mathbb E e^{itV^2},
\quad
\operatorname{Si}(x)=\int_0^x\frac{\sin u}{u}\,du.
\]
Indeed conditioning on \(L=\ell\) gives \(\mathbb E_H e^{2itH\ell}=\sin(t\ell)/(t\ell)\). Since \(\operatorname{Si}(t/2)\to\pi/2\) and \(\Re\mathbb E e^{itV^2}\ge1/\sqrt2\),
\[
|\phi_Q(t)|\ge \frac{c}{t}
\]
for an absolute \(c>0\) and every sufficiently large prescribed \(t\).

The example has a physical hub \(H\), but \(V\) is concentrated in one original coordinate rather than split between two diffuse light banks. Thus it does not disprove a stronger pointwise Fourier bound under an additional two-bank planar diffuseness assumption, nor any bounded-density claim.
