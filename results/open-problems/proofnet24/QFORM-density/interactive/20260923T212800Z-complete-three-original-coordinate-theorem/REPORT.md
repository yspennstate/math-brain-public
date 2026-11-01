# Complete three-original-coordinate density theorem

**Status:** Complete proof for \(n=3\), any signs and any independent cap-one original-coordinate laws. This does **not** prove a bound independent of \(n\) for arbitrary dimension. The high-dimensional overlapping small-leakage problem remains open.

## Theorem

Let \(X_1,X_2,X_3\) be independent real random variables whose probability densities are each bounded by one. For every symmetric \(3\times3\) real matrix \(A\) with \(s_3(A)\ge1\), \(Q=X^\top A X\) has a probability density obeying
\[
 \|p_Q\|_\infty\le C
\]
for an absolute constant \(C\), independent of \(A\), the signs of its eigenvalues, all three laws, and the density target. The argument also tolerates any affine term in \(Q\), by translating the three original independent variables through \(A^{-1}\).

## Case 1: some physical diagonal is substantial

If \(|A_{hh}|\ge1/4\) for some \(h\), complete the square in \(X_h\). The two-variable Schur complement \(S=A_{-h,-h}-A_{-h,h}A_{h,-h}/A_{hh}\) satisfies \(S^{-1}=(A^{-1})_{-h,-h}\), hence \(\|S^{-1}\|\le1\) because \(s_3(A)\ge1\). The proved two-variable product half-Riesz estimate gives, for independent cap-one \(X_{-h}\),
\[
 \sup_s\mathbb E|s-X_{-h}^\top S X_{-h}|^{-1/2}\le C_0.
\]
The conditional density of the completed hub square is at most \(|A_{hh}|^{-1/2}|s-X_{-h}^\top S X_{-h}|^{-1/2}\). Thus \(\|p_Q\|_\infty\le2C_0\). A detailed proof of the half-Riesz estimate, including arbitrary fragmented product densities and the saddle case, is in the companion *Two-variable product half-Riesz potential for an invertible quadratic* report.

## Case 2: every physical diagonal is small

Suppose \(|A_{ii}|<1/4\) for \(i=1,2,3\). Label the first two original variables \(X,Y\), and the third \(Z\), and write the leading block
\[
 B=\begin{pmatrix}a&b\\b&d\end{pmatrix},
 \qquad |a|,|d|<1/4.
\]
Every off-diagonal edge has magnitude at least \(3/4\). Indeed, remove from \(A\) both its diagonal and an arbitrarily selected symmetric edge \(b(e_i e_j^\top+e_j e_i^\top)\). In three dimensions, the two remaining off-diagonal edges form a star whose symmetric adjacency matrix has rank at most two. The removed matrix has operator norm at most \(\max_i|A_{ii}|+|b|<1/4+|b|\). The rank-two perturbation inequality therefore gives
\[
 1\le s_3(A)\le\max_i|A_{ii}|+|b|<1/4+|b|,
\]
so \(|b|>3/4\). In particular the displayed \(B\) is invertible because \(|ad|<1/16<|b|^2\).

## Strong-edge saddle lemma

Assume \(|a|,|d|<1/4\) and \(|b|\ge3/4\). For independent cap-one \(X,Y\), write \(q_B(x,y)=a x^2+2bxy+d y^2\). At every nonzero target \(t\),
\[
 p_{q_B}(t)\le \frac{C_1}{|b|}\bigl[1+\log_+(|b|/|t|)\bigr].\tag{1}
\]
For \(r=\sqrt{|t|/(4|b|)}\), any point on \(q_B=t\) has \(\max(|x|,|y|)\ge r\): if both are smaller, \(|q_B|\le (|a|+2|b|+|d|)r^2<|t|\), as \(|b|\ge3/4\).

Partition the plane into \(E_1=\{|dy|\le|bx|/2\}\) and \(E_2=E_1^c\). On \(E_1\), \(|\partial_y q_B|=|2bx+2dy|\ge|bx|\); for fixed \(x\), the map is monotone on its allowed interval, so cap-one \(Y\) contributes density at most \((|bx|)^{-1}\). If \(|x|<r\) at a point on \(q_B=t\), then \(|y|\ge r\), \(|a x|\le|b y|/3\), and \(|\partial_x q_B|\ge(4/3)|b y|\). The restricted map in \(x\) is monotone on \(|x|<r\), so cap-one \(X\) contributes at most \(C/(|b y|)\).

On \(E_2\), \(|x|<2|dy|/|b|\) and \(|ad|/b^2<1/9\), whence \(|\partial_x q_B|\ge(14/9)|b y|\). If \(|y|<r\) on the level set, then \(|x|\ge r\) and \(|\partial_y q_B|\ge(4/3)|b x|\). The two analogous monotone-section bounds apply. Altogether all four pieces of the density at \(t\) are bounded by
\[
 \frac{C_2}{|b|}\left(
   \int_{|x|\ge r}\frac{f_X(x)}{|x|}\,dx
   +\int_{|y|\ge r}\frac{f_Y(y)}{|y|}\,dy\right)
 \le\frac{C_3}{|b|}[1+\log_+(1/r)],
\]
which implies (1) after changing absolute constants. The estimates remain valid when the independent densities are translated separately, uniformly over both translation amounts.

For the present symmetric invertible \(3\times3\) matrix \(A\), complete the square in the \((X,Y)\) block:
\[
 Q=( (X,Y)^\top+B^{-1}uZ)^\top B((X,Y)^\top+B^{-1}uZ)
   +\kappa Z^2,
 \qquad \kappa=A_{33}-u^\top B^{-1}u.
\]
The inverse-block identity yields \((A^{-1})_{33}=1/\kappa\); \(s_3(A)\ge1\) therefore gives \(|\kappa|\ge1\). Conditionally on \(Z=z\), the translated \(X,Y\) retain their independent density caps, so (1) gives
\[
 p_Q(s)\le\frac{C_1}{|b|}\left[1+
 \mathbb E\log_+\frac{|b|}{|s-\kappa Z^2|}\right].
\]
The one-variable quadratic sublevel bound \(\mathbb P(|s-\kappa Z^2|\le u)\le C_4\min\{1,\sqrt{u/|\kappa|}\}\) implies, by layer cake,
\[
 \mathbb E\log_+\frac{|b|}{|s-\kappa Z^2|}
 \le C_5[1+\log_+(|b|/|\kappa|)]
 \le C_5[1+\log_+|b|].
\]
Finally \([1+\log_+|b|]/|b|\) is bounded for \(|b|\ge3/4\), proving a universal density bound under the stated strong-edge hypothesis.

## An ambient principal-block corollary

Suppose a larger symmetric \(A\) has a three-original-coordinate principal submatrix \(A_{J,J}\) with \(s_3(A_{J,J})\ge1\). Condition on all original variables outside \(J\): the remaining conditional polynomial in the three original coordinates has the same Hessian \(A_{J,J}\) and only gains an affine term and constant. The theorem's uniform affine version therefore gives \(\|p_{X^\top A X}\|_\infty\le C\), independently of ambient dimension and all cross terms touching the conditioned coordinates. No claim is made that \(s_3(A)\ge1\) alone guarantees such a principal triple; diffuse rank-three matrices generally have individual principal triples of tiny scale.
