# Independent square bank may be fully shared by V and P

This addendum extends the [all-target conditional-hub square receiver](https://github.com/yspennstate/math-open-problems/blob/1a79f3525d40fef2baf7a1d19d2614f2b786bc49/proofnet24/QFORM-density/interactive/20260923T203741Z-independent-v-square-product-band/GLOBAL_LEVEL_ADDENDUM.md). Its original requirement \(p_T=0\) can be replaced by **collinearity** with \(v_T\).

Let \(H\) be independent physical cap-one, and let \(L=\ell\cdot X\), \(V=v\cdot X\), \(P=p\cdot X\) be orthonormal linear forms of independent cap-one original leaves. Suppose a nonempty literal original-coordinate bank \(T\) has
\[
\ell_T=0,\qquad p_T=c\,v_T,\qquad
\rho=\|v_T\|_2>0
\]
for some arbitrary real \(c\). In particular, a **single coordinate** \(i\) with \(\ell_i=0,v_i\ne0\) qualifies, regardless of \(p_i\): set \(c=p_i/v_i\).

Define \(Z=v_T\cdot X_T\), \(V_0=v_{T^c}\cdot X_{T^c}\), \(P_0=p_{T^c}\cdot X_{T^c}\). Then \(L\), \(V_0\), \(P_0\), \(H\) are independent of \(Z\); on the full probability space,
\[
V=V_0+Z,\qquad P=P_0+cZ.
\]
For arbitrary real \(\beta,\epsilon\), direct expansion and completion give the **exact identity**
\[
\boxed{
2HL+\beta L^2+V^2+2\epsilon LP
=(Z+V_0+\epsilon c L)^2
+2L\left[
H+\epsilon P_0-\epsilon c V_0
+\frac{\beta-\epsilon^2 c^2}{2}L
\right].}
\tag{1}
\]
Call the bracket \(U\), and put \(W=V_0+\epsilon cL\). The independent physical hub ensures \(p_{U\mid L}(u\mid l)\le1\), regardless of the real values of \(c,\beta,\epsilon\), because \(U=H+\text{a function of the non-hub leaves}\). More precisely \(g_{L,U}(l,u)\le p_L(l)\le\sqrt2\). The independent scalar \(Z\) has density \(p_Z\le\sqrt2/\rho\) by the sharp product-marginal theorem. Applying Theorem (A2) in the linked global addendum to \(2LU+(W+Z)^2\) yields
\[
\boxed{
\|p_Q\|_\infty
\le\frac{8+\frac32\sqrt2}{\rho}<\frac{10.13}{\rho}.}
\tag{2}
\]
No moment, support, sign, target-level, or \(L/P\)-overlap hypothesis is added; \(P\) and \(V\) may coincide throughout bank \(T\).

The exact-rank-three fully overlapping situation with **no** bank having \(\ell_T=0\) and \(p_T\parallel v_T\) remains outside this receiver. The original QFORM conjecture is not settled by (2).
