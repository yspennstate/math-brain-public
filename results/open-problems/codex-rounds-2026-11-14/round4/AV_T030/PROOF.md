# Removing the bounded regularization in the interior Green resolvent

This note checks the passage \(\epsilon\downarrow0\) in the proposition labelled `prop:interior-reciprocal` in OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains* (September 24, 2026). The result below concerns that interior kernel proposition, not the hot-spots conjecture.

Write \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). All kernel reciprocals are entrywise. Property (P) means that a real symmetric finite matrix has at most one positive eigenvalue, counted with multiplicity.

## 1. Recheck of the preceding finite resolvent step

Let \(M\) be a real symmetric matrix with positive entries, let \(Z\) be a finite set of integration indices, and let \(W=\operatorname{diag}(w_z)\), with \(w_z\ge0\). Suppose
\[
 B=W^{1/2}M_{ZZ}W^{1/2},\qquad \|B\|<1.
\]
For \(A\subset Z\), define
\[
 Q_A=I-W_A^{1/2}M_{AA}W_A^{1/2},\qquad
 H^A=M+M_{:A}W_A^{1/2}Q_A^{-1}W_A^{1/2}M_{A:}.
\]
The empty-set expression is \(H^\varnothing=M\). Every \(Q_A\) is positive definite as a principal submatrix of \(I-B\).

Here is a direct factorization for adding an index \(z\notin A\). Set
\[
 b=-\sqrt{w_z}W_A^{1/2}M_{Az},\quad t=1-w_zM_{zz},\quad
 s=t-b^TQ_A^{-1}b=1-w_zH^A_{zz}.
\]
Multiplication gives
\[
 \begin{pmatrix}Q_A&b\\b^T&t\end{pmatrix}
 =
 \begin{pmatrix}I&0\\b^TQ_A^{-1}&1\end{pmatrix}
 \begin{pmatrix}Q_A&0\\0&s\end{pmatrix}
 \begin{pmatrix}I&Q_A^{-1}b\\0&1\end{pmatrix}.                 \tag{1}
\]
Positive definiteness forces \(s>0\), and determinants give
\(s=\det Q_{A\cup\{z\}}/\det Q_A\). Inverting the three factors in (1), in reverse order, and substituting in the definition of \(H\) yields
\[
 H^{A\cup\{z\}}=H^A+
 \frac{w_z}{1-w_zH^A_{zz}}H^A_{:z}H^A_{z:}.                   \tag{2}
\]
Indeed, the correction to the \(i,j\) entry is the product of
\[
 \sqrt{w_z}\bigl(M_{iz}+M_{iA}W_A^{1/2}Q_A^{-1}
 W_A^{1/2}M_{Az}\bigr)=\sqrt{w_z}H^A_{iz}
\]
and the analogous expression for \(j\), divided by \(s\). This remains true when either endpoint equals an integration index. If \(w_z=0\), the update vanishes and \(s=1\). Coincident physical node locations do not affect (1).

Thus the earlier finite-resolvent formula and its positive denominators hold. Combined with the previously checked positive-column-update lemma, (2) preserves (P) for reciprocals. The previous script also passes again: 34 elimination orders and 18 exact scalar perturbation checks.

The earlier quadrature perturbation estimate is checked independently by the identity
\[
 \langle g_x^\pi,R_\pi g_y^\pi\rangle-\langle g_x,Rg_y\rangle
 =\langle g_x^\pi-g_x,R_\pi g_y^\pi\rangle
 +\langle g_x,R_\pi(g_y^\pi-g_y)\rangle
 +\langle g_x,(R_\pi-R)g_y\rangle.
\]
If \(\|T\|\le d<1\), \(\|T_\pi-T\|\le e<1-d\), \(R=(I-T)^{-1}\), and \(R_\pi=(I-T_\pi)^{-1}\), the inverse identity gives
\[
 \|R_\pi-R\|\le\frac{e}{(1-d)(1-d-e)}.
\]
Cauchy--Schwarz applied to the three displayed terms gives exactly the earlier bound, with no missing factor. The finite and quadrature rechecks do not require a new assumption about positive semidefiniteness of the kernels themselves.

## 2. Statement for the singular passage

Let \(d\rho=b(y)\,dy\) on \(\mathbb D\), where \(0\le b\le A<\infty\), and put \(m=\rho(\mathbb D)\). In the application \(\rho\) is compactly supported and \(0\le\rho\le q\). Suppose the Green operator
\[
 Tf(x)=\int_{\mathbb D}G(x,y)f(y)\,d\rho(y)
\]
satisfies \(\|T\|_{L^2(\rho)\to L^2(\rho)}\le d<1\). Here
\[
 G(x,y)=\frac{1}{2\pi}\log\left|\frac{1-x\overline y}{x-y}\right|,
 \quad x\ne y,\qquad G(x,x)=+\infty.
\]
The norm hypothesis is exactly the conclusion of the manuscript's preceding Green-operator lemma. It also follows directly from its form assumption: if
\(\|\psi\|_\rho^2\le d\int|\nabla\psi|^2\) on \(H^1_0(\mathbb D)\), the weak Dirichlet solution \(\psi=Tv\) satisfies
\[
 \|\psi\|_\rho^2\le d\int|\nabla\psi|^2
 =d\langle\psi,v\rangle_\rho
 \le d\|\psi\|_\rho\|v\|_\rho.
\]
Division, with the zero case treated separately, gives \(\|Tv\|_\rho\le d\|v\|_\rho\). The source \(bv\) is in ordinary \(L^2\), because \(\int|bv|^2\le A\|v\|_\rho^2\), so the usual weak Dirichlet solution and its explicit disk Green representation apply. The weighted form assumption for \(\rho\le q\) follows by domination from the one for \(q\).

Let \(C_\epsilon\), \(0<\epsilon\le1\), be the bounded regularizations from the manuscript, so
\[
 C_\epsilon(x,y)^{-1}=4\pi\{L(h)+\epsilon f(h)\},\qquad
 h=\frac{|x-y|^2}{(1-|x|^2)(1-|y|^2)},
\]
where \(L(h)=1/\log(1+1/h)\) for \(h>0\), \(L(0)=0\), and
\(f(h)=h+1/2-L(h)\). The previously checked regularization lemma gives
\[
 0\le f(h)\le\tfrac12,\quad
 0<C_\epsilon\le G,\quad
 C_\epsilon\uparrow G,\quad
 C_\epsilon(x,x)=\frac{1}{2\pi\epsilon}.                       \tag{3}
\]
Let \(T_\epsilon\) have kernel \(C_\epsilon\) on \(L^2(\rho)\), and set
\[
 g_x=G(x,\cdot),\quad g_x^\epsilon=C_\epsilon(x,\cdot),\quad
 R=(I-T)^{-1},\quad R_\epsilon=(I-T_\epsilon)^{-1}.
\]
Values at a single point are immaterial in these \(L^2\) classes, because \(\rho\) has a density. Define the finite correction terms
\[
 Q(x,y)=\langle g_x,Rg_y\rangle_\rho,\qquad
 Q_\epsilon(x,y)=\langle g_x^\epsilon,R_\epsilon g_y^\epsilon\rangle_\rho,
\]
and
\[
 M(x,y)=G(x,y)+Q(x,y),\qquad
 F_\epsilon(x,y)=C_\epsilon(x,y)+Q_\epsilon(x,y).
\]

**Proposition.** These definitions are legitimate for every interior \(x,y\), except that \(M(x,x)=+\infty\). Put
\[
 \alpha=1-d,\qquad B=\sqrt{\frac{A}{2\pi}},\qquad
 H=\sqrt{\frac{3A}{2\pi}}.
\]
Then
\[
 \sup_x\|g_x\|_\rho\le B,\qquad
 \sup_x\|g_x-g_x^\epsilon\|_\rho\le H\epsilon,\qquad
 \|T-T_\epsilon\|\le H\sqrt m\,\epsilon,                       \tag{4}
\]
and
\[
 \sup_{x,y}|Q(x,y)-Q_\epsilon(x,y)|
 \le\epsilon\left(\frac{2BH}{\alpha}
                  +\frac{B^2H\sqrt m}{\alpha^2}\right).        \tag{5}
\]
Off the diagonal, \(F_\epsilon(x,y)\to M(x,y)\). On the diagonal,
\[
 \frac{2\pi\epsilon}{1+2\pi\epsilon B^2/\alpha}
 \le\frac1{F_\epsilon(x,x)}\le2\pi\epsilon.                    \tag{6}
\]
Consequently, if every finite reciprocal matrix of \(F_\epsilon\) has (P), the reciprocal matrix of \(M\), with diagonal zero, has (P) on every finite set of distinct interior points.

## 3. Uniform logarithmic moments

For \(x,y\in\mathbb D\), \(x\ne y\), positivity follows from
\[
 |1-x\overline y|^2-|x-y|^2=(1-|x|^2)(1-|y|^2)>0.
\]
Since \(|1-x\overline y|\le2\) and \(|x-y|<2\),
\[
 0<G(x,y)\le k_x(y):=\frac1{2\pi}\log\frac2{|x-y|}.
\]
For each positive integer \(p\), extend the integral to the disk \(B(x,2)\) and integrate in polar coordinates about \(x\):
\[
 \begin{aligned}
 \int_{\mathbb D}G(x,y)^p\,dy
 &\le\frac{2\pi}{(2\pi)^p}\int_0^2
        r\log^p(2/r)\,dr\\
 &=\frac{8\pi}{(2\pi)^p}\int_0^\infty t^p e^{-2t}\,dt
 =\frac{p!}{(4\pi)^{p-1}}.                                   \tag{7}
 \end{aligned}
\]
The substitution is \(r=2e^{-t}\). Repeated integration by parts gives
\(\int_0^\infty t^p e^{-2t}dt=p!/2^{p+1}\), with zero boundary terms. In particular,
\[
 \int_{\mathbb D}G(x,y)^2dy\le\frac1{2\pi},\qquad
 \int_{\mathbb D}G(x,y)^4dy\le\frac3{8\pi^3}.                  \tag{8}
\]
Multiplying by the density bound \(A\) proves \(\|g_x\|_\rho\le B\) uniformly, including when \(x\) lies in \(\operatorname{supp}\rho\). This also gives
\[
 \iint G(x,y)^2\,d\rho(x)d\rho(y)\le mB^2<\infty.
\]
The Green operator is therefore Hilbert--Schmidt as well as bounded.

Here is a second derivation of the constants in (7), using level sets rather than radial integration. For \(t\ge0\),
\[
 |\{y\in\mathbb D:k_x(y)>t\}|\le4\pi e^{-4\pi t}.
\]
Writing \(k^p=\int_0^k pt^{p-1}dt\) and using Tonelli gives
\[
 \int_{\mathbb D}k_x^pdy
 \le4\pi p\int_0^\infty t^{p-1}e^{-4\pi t}dt
 =\frac{p!}{(4\pi)^{p-1}}.
\]
Thus the two constants in (8) have independent normalizations. These are convenient upper bounds, not claims of sharp constants for the actual Green kernel.

## 4. Source and operator convergence

For \(x\ne y\), the reciprocal definition and (3) give the exact identity
\[
 G(x,y)-C_\epsilon(x,y)
 =4\pi\epsilon f(h)G(x,y)C_\epsilon(x,y).
\]
It follows that
\[
 0\le G-C_\epsilon\le2\pi\epsilon G^2                       \tag{9}
\]
away from the diagonal. For each fixed \(x\), the exceptional point \(y=x\) has zero \(\rho\)-mass. Squaring (9) and using the fourth moment in (8) gives
\[
 \|g_x-g_x^\epsilon\|_\rho^2
 \le4\pi^2\epsilon^2 A\frac3{8\pi^3}
 =\frac{3A}{2\pi}\epsilon^2=H^2\epsilon^2.
\]
This proves the source assertion in (4) uniformly in \(x\). Integrating this inequality in \(x\) against \(\rho\) gives
\[
 \|T-T_\epsilon\|^2
 \le\|G-C_\epsilon\|_{L^2(\rho\times\rho)}^2
 \le mH^2\epsilon^2,
\]
which proves the operator assertion in (4). The first inequality is Cauchy--Schwarz in the integration variable followed by integration in the evaluation variable.

For every \(v\in L^2(\rho)\), kernel positivity gives
\[
 |T_\epsilon v|\le T|v|,\qquad
 \|T_\epsilon v\|_\rho\le d\|v\|_\rho.
\]
Thus both inverses exist by their norm-convergent geometric series, with
\[
 \|R\|,\|R_\epsilon\|\le\alpha^{-1},\qquad
 R-R_\epsilon=R(T-T_\epsilon)R_\epsilon,
\]
and hence
\[
 \|R-R_\epsilon\|\le\frac{H\sqrt m}{\alpha^2}\epsilon.         \tag{10}
\]
This argument uses positivity of kernel entries. It does not infer positivity of a quadratic form from positive entries.

## 5. Evaluations, the infinite diagonal, and reciprocal inertia

By (4), the correction terms are defined at all interior pairs, and
\[
 |Q(x,y)|,|Q_\epsilon(x,y)|\le\frac{B^2}{\alpha}.               \tag{11}
\]
Add and subtract terms to obtain
\[
 \begin{aligned}
 Q-Q_\epsilon={}&
 \langle g_x-g_x^\epsilon,Rg_y\rangle_\rho
 +\langle g_x^\epsilon,R(g_y-g_y^\epsilon)\rangle_\rho\\
 &+\langle g_x^\epsilon,(R-R_\epsilon)g_y^\epsilon\rangle_\rho.
 \end{aligned}
\]
Use (4), (10), and \(\|g_x^\epsilon\|_\rho\le B\) in the three terms. Their bounds are \(HB\epsilon/\alpha\), \(BH\epsilon/\alpha\), and \(B^2H\sqrt m\,\epsilon/\alpha^2\), proving (5). Together with (9), this proves, at every fixed distinct pair,
\[
 |M(x,y)-F_\epsilon(x,y)|
 \le\epsilon\left(2\pi G(x,y)^2+
       \frac{2BH}{\alpha}+\frac{B^2H\sqrt m}{\alpha^2}\right).  \tag{12}
\]

For nonnegative sources all terms in each geometric-series pairing are nonnegative. Therefore \(Q,Q_\epsilon\ge0\). On the diagonal,
\[
 F_\epsilon(x,x)=\frac1{2\pi\epsilon}+Q_\epsilon(x,x),
 \qquad 0\le Q_\epsilon(x,x)\le B^2/\alpha,
\]
which gives (6). In particular, the infinite direct diagonal is retained; its reciprocal tends to zero. The correction itself has a finite diagonal limit by (5).

For a fixed distinct pair \(x,y\), \(G(x,y)>0\), and
\(F_\epsilon(x,y)\ge C_\epsilon(x,y)\ge C_1(x,y)>0\). Also \(M(x,y)\ge G(x,y)\ge C_1(x,y)\). Thus
\[
 \left|\frac1{F_\epsilon(x,y)}-\frac1{M(x,y)}\right|
 \le\frac{|F_\epsilon(x,y)-M(x,y)|}{C_1(x,y)^2}\longrightarrow0.
\]
For any finite set of distinct points, all reciprocal entries now converge, including the diagonal entries. To prove closure of (P), suppose the limiting symmetric matrix were positive definite on a two-dimensional subspace. Its quadratic form would have a positive minimum on the unit circle of that subspace. Entrywise convergence in finite dimension gives uniform convergence of the quadratic forms on this circle. The approximating matrix would then be positive definite on the same two-dimensional subspace, contradicting (P). This proves the proposition.

## 6. Independent check by nonnegative chain integrals

For fixed \(x,y\), the Green correction has the expansion
\[
 Q(x,y)=\sum_{n=0}^\infty\langle g_x,T^n g_y\rangle_\rho.
\]
The \(n\)-th term is nonnegative and bounded by \(B^2d^n\). Its integral expression is the product of \(n+2\) Green factors along a chain with \(n+1\) integration variables. Tonelli justifies this expression for the nonnegative integrand; the norm bound proves that its value is finite.

For fixed \(n\), replacing every factor by \(C_\epsilon\) gives an increasing chain integral as \(\epsilon\downarrow0\), with limit the Green chain integral by monotone convergence. The same theorem on the product of the integration spaces with counting measure on \(n\) gives
\[
 Q_\epsilon(x,y)\uparrow Q(x,y).
\]
The uniform bound \(B^2/(1-d)\) rules out an infinite correction, even at \(x=y\). This identifies the same limit as the source/operator-norm argument. The direct diagonal term, which is not part of an integration chain, still diverges by (3).

## 7. Hypotheses and excluded cases

If \(\rho=0\), the correction terms vanish, and all convergence and diagonal assertions follow directly from (3). The constants in (4)--(5) can be taken to be zero when the density is zero. When \(m>0\), all preceding integrals are with a nonatomic measure. Repeated evaluation locations, if used in a finite family, give identical reciprocal rows with zero entries between the copies; combining coefficients reduces to the distinct-point case.

The density condition cannot be replaced by an arbitrary finite measure. For \(\rho=w\delta_x\), \(w>0\), the section \(G(x,\cdot)\) is not in \(L^2(\rho)\), and the finite Green operator at that atom is not defined by this kernel. Such a measure is excluded by \(\rho\le q=a\,dx\), \(a\in L^\infty\).

The strict spectral margin is also necessary. On the one-dimensional Hilbert space, \(T=(d)\) has inverse resolvent \((1-d)^{-1}\), which diverges as \(d\uparrow1\) and is undefined at \(d=1\). No uniform bound in the critical parameter is asserted here.

The estimates in (12) concern a fixed distinct pair. The factor \(G(x,y)^2\) diverges as \(y\to x\), so (12) does not assert uniform convergence of the direct kernels across the diagonal. The separate reciprocal diagonal estimate (6) is what the finite-matrix limit needs.

No radial boundary limit, removal of compact support, boundary Poisson-kernel estimate, vector variational identity, or eigenfunction argument is proved here. In particular, this proposition adds no boundary class to the stated hot-spots theorem.
