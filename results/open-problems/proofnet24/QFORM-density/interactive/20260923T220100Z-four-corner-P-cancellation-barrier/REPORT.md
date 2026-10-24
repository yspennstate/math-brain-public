# Four-corner cancellation of P and the dyadic exponent loss

**Status:** Exact identity and explicit obstruction to a naive box-norm proof, not a counterexample to the RMT/QFORM conjecture. The example uses admissible independent original-coordinate inputs in the already-solved zero-leakage case.

For the canonical quadratic \(Q=2HL+\beta L^2+V^2+2\varepsilon LP\), at a target level \(s\) and \(L\ne0\), integrating the independent hub makes the lookup argument
\[
 g_s(X)={s\over2L}-{\beta L\over2}-{V^2\over2L}-\varepsilon P.
\]
Let \(F_s(l,v)=s/(2l)-\beta l/2-v^2/(2l)\). For any two original-coordinate resamplings \(X_i=x_i,x_i'\) and \(X_j=x_j,x_j'\), the alternating four-corner difference of \(g_s\) equals that of \(F_s(L,V)\): the entire term \(-\varepsilon P\) cancels, since \(P\) is a sum of one-coordinate contributions. Its continuous Hessian, in \((l,v)\), is
\[
 D^2F_s(l,v)=
 \begin{pmatrix}
  (s-v^2)/l^3 & v/l^2\\
  v/l^2 & -1/l
 \end{pmatrix},
 \qquad \det D^2F_s(l,v)=-s/l^4.
\]
At negative targets \(s=-\gamma<0\), this Hessian is definite on each half-plane \(l>0\) and \(l<0\), with opposite signs; the linear \(P\) tail does not appear in this curvature.

The ordinary two-coordinate Cauchy–Schwarz box bound nevertheless discards too much dyadic mass. Fix small \(r>0\), take independent \(L,V\) uniform on \([0,1]\) and a hub density equal to the indicator of \([-1,0]\), set \(\beta=\varepsilon=0\), and target \(s=-r\). On
\[
 R_r=\{r\le L\le2r,\quad0\le V\le\sqrt r\},
\]
the lookup value \(g_s=-(r+V^2)/(2L)\) lies in \([-1,-1/4]\), so \(f_H(g_s)=1\). The event mass \(\mathbb E[\mathbf1_{R_r} f_H(g_s)]\) is at least \(r^{3/2}\), and its dyadic density contribution after division by \(2L\) is of order \(\sqrt r\), as expected from the sharp restricted weak-L² target.

If one applies Cauchy–Schwarz first in the original \(L\) source and then in the independent \(V\) source, the resulting four-corner expectation contains two independent \(L\)'s and two independent \(V\)'s. All four corners lie in \(R_r\) with probability \(r^3\), and on that event the four lookup indicators equal one. Thus the fourth-root box upper bound can be no smaller than \(r^{3/4}\), far larger than the required \(r^{3/2}\) mass. This proves that *bare* four-corner cancellation, followed by a fourth root, cannot establish the desired dyadic estimate even for this easy \(\varepsilon=0\) input. Any successful four-corner proof must retain the \(1/|L|\) weight and the square-root preimage geometry in a sharper multilinear estimate.

Similarly, the fixed-target dyadic hub level density
\[
 T_{0,r}(h)=\int_{r\le L\le2r} f_L(l)\int f_V(v)\delta(2hl+v^2)\,dv\,dl
\]
for the same independent uniform \(L,V\) obeys \(T_{0,r}(h)\asymp\sqrt{r/|h|}\) as \(h\uparrow0\) through negative values. It belongs to weak \(L^2(dh)\) at the correct scale but not strong \(L^2\). A Plancherel bound for \(\|T_{s,r}\|_2\) therefore cannot uniformly replace the required restricted weak-L² estimate as \(s\uparrow0\).

The positive restricted weak-L² dyadic statement and why it suffices for the canonical density appear in `proofnet24/QFORM-density/interactive/20260923T205500Z-dyadic-rw2-hub-target/REPORT.md`.
