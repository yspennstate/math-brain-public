# Two-variable product half-Riesz potential for an invertible quadratic

**Status:** A proved finite-dimensional receiver. This does not solve the general rank-three density conjecture. It covers a 3-original-coordinate matrix when one physical diagonal is bounded away from zero.

## Theorem

Let \(Y_1,Y_2\) be independent real random variables, each with a probability density bounded by one. Let \(S\in\mathbb R^{2\times2}\) be symmetric with \(s_2(S)\ge1\). Then an absolute constant \(C\) satisfies, uniformly in every \(s\in\mathbb R\) and affine form \(\ell\),
\[
 \mathbb E\left|s-Y^\top S Y-\ell(Y)\right|^{-1/2}\le C.\tag{1}
\]
We give both a diagonal-dominant small-ball argument and a mixed-derivative argument. Arbitrary fragmented one-dimensional densities are allowed; no single-interval extremizer assumption is used.

## A diagonal entry of magnitude at least \(1/4\)

Translate \(Y_1,Y_2\) separately to remove \(\ell\), using invertibility of \(S\). These translations preserve product structure and density caps. Write \(S=\begin{pmatrix}a&b\\b&d\end{pmatrix}\) and suppose \(|a|\ge1/4\). Complete the first square:
\[
 Y^\top S Y=a(Y_1+(b/a)Y_2)^2+\Delta Y_2^2,
 \qquad \Delta=d-b^2/a=\det(S)/a.
\]
For any \(0<\delta<1\) and any \(u\in\mathbb R\), the one-variable quadratic sublevel set has length
\[
 \big|\{x:|a x^2-u|\le\delta\}\big|
 \le C_0\frac{\delta}{\sqrt{|a|}\sqrt{|u|+\delta}}.\tag{2}
\]
The bound follows by subtracting the square roots of the two interval endpoints; when the interval meets the quadratic vertex, both sides are of order \(\sqrt{\delta/|a|}\). Independence and the density cap let us apply (2) for each fixed \(Y_2=y\), regardless of the center \(-(b/a)y\).

For any scalar \(W\) with density at most one, the sublevel estimate \(\mathbb P(|s-\Delta W^2|\le u)\le C_1\min\{1,\sqrt{u/|\Delta|}\}\) follows by the same interval geometry. Layer cake gives
\[
 \mathbb E (|s-\Delta W^2|+\delta)^{-1/2}
 \le C_2\min\left\{\delta^{-1/2},\ |\Delta|^{-1/2}[1+\log_+(|\Delta|/\delta)]\right\}.\tag{3}
\]
Since \(|a\Delta|=|\det S|\ge1\), equations (2)–(3) imply the uniform bound
\[
 \mathbb P(|Y^\top S Y-s|\le\delta)
 \le C_3\delta[1+\log(1/\delta)].\tag{4}
\]
To check the coefficient regimes explicitly: if \(|\Delta|\le\delta\), use the first term of (3), so \(\sqrt{\delta/|a|}\le\delta\) because \(|a|\ge1/|\Delta|\ge1/\delta\). If \(\delta<|\Delta|\le1\), use \(1/\sqrt{|a\Delta|}\le1\) and \(\log(|\Delta|/\delta)\le\log(1/\delta)\). If \(|\Delta|>1\), the extra \(\log|\Delta|/\sqrt{|a\Delta|}\) is uniformly bounded because \(|a|\ge1/4\), while \(1/\sqrt{|a\Delta|}\le1\). Equation (4) integrates against the \(t^{-3/2}\) layer-cake kernel and implies (1) in this case. The same reasoning applies when \(|d|\ge1/4\) after exchanging coordinates.

## Both diagonal entries smaller than \(1/4\)

Again translate to remove affine terms. Since \(s_2(S)\ge1\), Weyl's inequality between \(S\) and \(\begin{pmatrix}0&b\\b&0\end{pmatrix}\) gives \(|b|\ge1-\max(|a|,|d|)>3/4\). Consequently \(|ad|/b^2<1/9\).

Split the \((x,y)\) plane into
\[
 E_1=\{|dy|\le|bx|/2\},\qquad E_2=E_1^c.
\]
On \(E_1\), for each fixed \(x\ne0\), the map \(y\mapsto q(x,y)=a x^2+2bxy+d y^2\) has derivative magnitude \(|2bx+2dy|\ge|bx|\) and constant derivative sign on its allowed interval. Pushforward of the restricted cap-one \(Y_2\)-law therefore has density at most \((|b x|)^{-1}\) and mass at most one. The cap-and-mass rearrangement for the kernel \(|s-u|^{-1/2}\) gives
\[
 \mathbb E[\boldsymbol1_{E_1}|s-q(Y_1,Y_2)|^{-1/2}\mid Y_1=x]
 \le C_4(|b x|)^{-1/2}.\tag{5}
\]
On \(E_2\), \(|x|<2|dy|/|b|\) and therefore \(|a x|< (2/9)|b y|\). For each fixed \(y\ne0\), the map \(x\mapsto q(x,y)\) has derivative magnitude \(|2ax+2by|\ge(14/9)|b y|\) with constant sign on its allowed interval. The analogous bound is \(C_5(|b y|)^{-1/2}\). Finally, any cap-one scalar probability density satisfies \(\mathbb E|Y_j|^{-1/2}\le\int_{-1/2}^{1/2}|u|^{-1/2}\,du=2\sqrt2\) by rearrangement. Summing the bounds for \(E_1,E_2\), using \(|b|>3/4\), proves (1).

## Three original coordinates with a substantial diagonal

Let \(A\) be a symmetric **3 by 3** matrix with \(s_3(A)\ge1\), and suppose \(|A_{hh}|\ge1/4\) for some physical coordinate \(h\). Set \(a=A_{hh}\) and write the Schur complement \(S=A_{-h,-h}-A_{-h,h}A_{h,-h}/a\). The inverse block identity gives \(S^{-1}=(A^{-1})_{-h,-h}\), whence \(\|S^{-1}\|\le\|A^{-1}\|\le1\) and \(s_2(S)\ge1\). Completing the hub square and using its density cap gives, conditionally on the other two original coordinates,
\[
 p_{X^\top A X}(s)
 \le |a|^{-1/2}\,
 \mathbb E\left|s-X_{-h}^\top S X_{-h}\right|^{-1/2}
 \le 2C.\tag{6}
\]
All steps apply to arbitrary independent cap-one original densities. If all physical diagonals have magnitude less than \(1/4\), this note makes no claim; the remaining triangle interaction needs a separate receiver.
