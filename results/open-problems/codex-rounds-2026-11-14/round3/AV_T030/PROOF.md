# Reciprocal inertia under a bounded positive resolvent

This note verifies the bounded-kernel quadrature step in Section 5 of OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains* (September 24, 2026). It also gives an explicit error estimate for that step. It does not address the subsequent singular Green limit, boundary kernels, eigenfunction argument or nonsmooth-domain extension.

For a real symmetric finite matrix, property (P) means at most one positive eigenvalue, counted with multiplicity. All reciprocals of kernel matrices below are entrywise.

## 1. Independent recheck of the scalar correction

Put
\[
 L(h)=\frac1{\log(1+1/h)}\quad(h>0),\qquad L(0)=0,
 \qquad f(h)=h+\frac12-L(h).
\]
The earlier regularization check can be put in the explicit form
\[
 \boxed{\displaystyle
 f(h)=\int_0^1
 \frac{dr}{(h+r)\{\log^2((1-r)/r)+\pi^2\}} }\qquad(h\ge0).       \tag{1}
\]

Here is the normalization and derivation. For \(0<\alpha<1\),
\[
 I_\alpha=\int_0^\infty\frac{v^{\alpha-1}}{1+v}\,dv
 =\frac{\pi}{\sin(\pi\alpha)}.
\]
For completeness, integrate \(z^{\alpha-1}/(1+z)\) around a keyhole contour cut along the positive real axis, with argument in \((0,2\pi)\). The upper and lower straight segments have limiting sum \((1-e^{2\pi i\alpha})I_\alpha\). The residue at \(-1\) is \(e^{i\pi(\alpha-1)}\), so this sum equals \(2\pi i e^{i\pi(\alpha-1)}\). Dividing gives the stated real integral. The outer and inner arc contributions vanish with bounds of order \(R^{\alpha-1}\) and \(\varepsilon^\alpha\).

Let \(v\) have probability density \(I_\alpha^{-1}v^{\alpha-1}/(1+v)\), and put \(r=(1+v)^{-1}\). Change of variables gives its density on \((0,1)\):
\[
 \frac{\sin(\pi\alpha)}{\pi}
 r^{-\alpha}(1-r)^{\alpha-1}.
\]
Integration by parts in \(v\) gives
\[
 {\mathbb E}_\alpha(1-r)
 =I_\alpha^{-1}\int_0^\infty\frac{v^\alpha}{(1+v)^2}\,dv
 =\alpha.
\]
The boundary term \(v^\alpha/(1+v)\) vanishes at both ends. Scaling \(v=(h+1)t/h\) gives, for \(h>0\),
\[
 \begin{aligned}
 {\mathbb E}_\alpha\frac{h(h+1)}{h+r}
 &=I_\alpha^{-1}\int_0^\infty
   \frac{h(h+1)v^{\alpha-1}}{h+1+hv}\,dv\\
 &=h^{1-\alpha}(h+1)^\alpha.
 \end{aligned}
\]
Polynomial division gives
\[
 \frac{h(h+1)}{h+r}=h+(1-r)-\frac{r(1-r)}{h+r}.
\]
Also, direct integration of an exponential in \(\alpha\) gives
\[
 \int_0^1 h^{1-\alpha}(h+1)^\alpha\,d\alpha=L(h).
\]
Integrating the preceding identities over \(\alpha\) yields
\[
 f(h)=\int_0^1\int_0^1
 \frac{\sin(\pi\alpha)}{\pi}
 \frac{r^{1-\alpha}(1-r)^\alpha}{h+r}\,dr\,d\alpha.
\]
All integrands here are nonnegative; Tonelli therefore permits switching the two integrals. With \(t=\log((1-r)/r)\), the numerator integrated over \(\alpha\) is
\[
 \frac r\pi\int_0^1e^{\alpha t}\sin(\pi\alpha)\,d\alpha
 =\frac{r(1+e^t)}{t^2+\pi^2}
 =\frac1{t^2+\pi^2}.
\]
This proves (1) for \(h>0\).

To check the endpoint independently, use \(r=(1+e^t)^{-1}\). The integral in (1) at \(h=0\) becomes
\[
 \int_{\mathbb R}
 \frac{e^t}{1+e^t}\frac{dt}{t^2+\pi^2}
 =\frac12\int_{\mathbb R}\frac{dt}{t^2+\pi^2}
 =\frac12.                                                     \tag{2}
\]
The first equality with the factor \(1/2\) follows by replacing \(t\) with \(-t\) and adding; the final integral is 1 by the arctangent antiderivative. Monotone convergence as \(h\downarrow0\) proves (1) at zero and agrees with the definition of \(f(0)\). In particular \(0\le f(h)\le1/2\).

For disk points put
\[
 h(x,y)=\frac{|x-y|^2}{(1-|x|^2)(1-|y|^2)},\qquad
 k(x,y)=\frac1{1+h(x,y)}
 =\frac{(1-|x|^2)(1-|y|^2)}{|1-x\overline y|^2}.
\]
The power series of \(1/(1-x\overline y)\), its conjugate, and positive factors show that \(k\) is a Gram kernel. For \(0<r<1\),
\[
 \frac1{h+r}=\sum_{n=0}^\infty(1-r)^n k^{\,n+1}.
\]
This series converges even when \(x=y\). Entrywise products of Gram kernels are Gram kernels, by taking tensor products of their vectors. Formula (1), whose diagonal integral is finite by (2), therefore proves that \(f(h(x,y))\) is positive semidefinite on every finite set.

Multiplication of \(h+1/2\) by the positive row and column factors \(1-|x|^2\) and \(1-|y|^2\) gives
\[
 \tfrac12(1+|x|^2)(1+|y|^2)-2x\cdot y.
\]
This is a positive rank-one form minus a Gram form, and so has (P). Subtracting \((1-\epsilon)f\), for \(0<\epsilon\le1\), preserves (P). Thus
\[
 \frac1{C_\epsilon}=4\pi(L+\epsilon f)
\]
has (P), while
\[
 L+\epsilon f=\epsilon(h+1/2)+(1-\epsilon)L\ge\epsilon/2.
\]
Consequently \(C_\epsilon\le1/(2\pi\epsilon)\), with equality on the diagonal. Its increase to \(G=(4\pi)^{-1}\log(1+1/h)\), including the infinite diagonal, follows from \(f\ge0\). The earlier regularization result survives this independent normalization check.

## 2. The finite update

Let \(M\) be real symmetric with strictly positive entries and suppose its reciprocal has (P). Fix a column \(z\). Then, for every \(c\ge0\),
\[
 \widetilde M=M+cM_{:z}M_{z:}                                   \tag{3}
\]
has strictly positive entries and its reciprocal has (P).

Indeed, use the positive diagonal matrix with entries \(M_{iz}\) to transform the reciprocal into
\[
 H_{ij}=\frac{M_{iz}M_{zj}}{M_{ij}},\qquad a=M_{zz}.
\]
Its \(z\)-row and column are \(a\). Subtracting that row and column from the others is an invertible congruence, giving the blocks
\(H_0-a\mathbf1\mathbf1^T\) and \(a>0\). Property (P) forces the first block to be nonpositive. Thus
\[
 U=a\mathbf1\mathbf1^T-H\succeq0
\]
with zero \(z\)-row and column. Since \(H_{ii}>0\), \(0\le U_{ii}<a\). Cauchy--Schwarz for a positive semidefinite matrix gives \(|U_{ij}|<a\).

The same diagonal congruence applied to \(1/\widetilde M\) gives entries \(H_{ij}/(1+cH_{ij})\). If \(c>0\), then
\[
 \frac a{1+ca}-\frac{H_{ij}}{1+cH_{ij}}
 =\sum_{n=0}^\infty
   \frac{c^n U_{ij}^{n+1}}{(1+ca)^{n+2}}.                        \tag{4}
\]
To check the equality, sum the geometric series to
\(U_{ij}/[(1+ca)(1+ca-cU_{ij})]\) and use \(H_{ij}=a-U_{ij}\).
The series converges absolutely because \(c|U_{ij}|<ca<1+ca\).
Every coefficient is nonnegative, and every entrywise power of \(U\)
is positive semidefinite. The matrix on the right is therefore positive
semidefinite. The transformed reciprocal is a positive rank-one matrix
minus that matrix, proving (P). At \(c=0\), the left difference is
\(a-H_{ij}=U_{ij}\), giving the same conclusion without a series.

## 3. Finite resolvent: a Schur-complement proof

Let \(M\) be as in Section 2 on a finite index set \(I\). Let
\(Z\subset I\) carry weights \(w_z\ge0\), and let \(W=\operatorname{diag}(w_z)\).
Suppose
\[
 B=W^{1/2}M_{ZZ}W^{1/2},\qquad \|B\|_2<1.
\]
For all indices, including endpoints in \(Z\), define
\[
 F=M+M_{:Z}W^{1/2}(I-B)^{-1}W^{1/2}M_{Z:}.                     \tag{5}
\]
Then \(F\) has positive entries and its entrywise reciprocal has (P).
Zero weights can be discarded. No distinctness requirement on physical
node locations is needed: different indices may have identical rows.

For a subset \(A\subset Z\), put
\[
 Q_A=I-W_A^{1/2}M_{AA}W_A^{1/2},\qquad
 H^A=M+M_{:A}W_A^{1/2}Q_A^{-1}W_A^{1/2}M_{A:},
\]
where \(H^\varnothing=M\) and \(\det Q_\varnothing=1\).
The full \(Q_Z=I-B\) is positive definite since \(\|B\|_2<1\);
every \(Q_A\), being a principal submatrix, is positive definite too.

For \(z\notin A\), the block matrix \(Q_{A\cup\{z\}}\) is
\[
 \begin{pmatrix}
 Q_A&-\sqrt{w_z}W_A^{1/2}M_{Az}\\
 -\sqrt{w_z}M_{zA}W_A^{1/2}&1-w_zM_{zz}
 \end{pmatrix}.
\]
Its Schur complement in the \(z\)-coordinate equals
\[
 s_z^A=1-w_z\bigl(M_{zz}
       +M_{zA}W_A^{1/2}Q_A^{-1}W_A^{1/2}M_{Az}\bigr)
       =1-w_zH^A_{zz}>0.                                      \tag{6}
\]
Positivity follows also by evaluating the positive quadratic form at
the vector \((Q_A^{-1}\sqrt{w_z}W_A^{1/2}M_{Az},1)\).
Block triangular elimination gives a second formula for the same number:
\[
 s_z^A=\frac{\det Q_{A\cup\{z\}}}{\det Q_A}.                    \tag{7}
\]
Thus no denominator is justified merely by a formal series.

For an explicit inverse calculation, set
\(b=-\sqrt{w_z}W_A^{1/2}M_{Az}\) and \(s=s_z^A\).
Multiplication verifies
\[
 \begin{pmatrix}Q_A&b\\b^T&1-w_zM_{zz}\end{pmatrix}^{-1}
 =
 \begin{pmatrix}
 Q_A^{-1}+Q_A^{-1}bs^{-1}b^TQ_A^{-1}&-Q_A^{-1}bs^{-1}\\
 -s^{-1}b^TQ_A^{-1}&s^{-1}
 \end{pmatrix}.
\]
Substitution in the definition of \(H^{A\cup\{z\}}\), and collection
of the four terms containing \(s^{-1}\), gives
\[
 H^{A\cup\{z\}}
 =H^A+\frac{w_z}{1-w_zH^A_{zz}}H^A_{:z}H^A_{z:}.               \tag{8}
\]
For example its \(i,j\) correction is \(s^{-1}\) times the product
\[
 \sqrt{w_z}
 \bigl(M_{iz}+M_{iA}W_A^{1/2}Q_A^{-1}W_A^{1/2}M_{Az}\bigr)
\]
and the analogous expression with \(j\). This also checks (8) for
\(i=z\) or \(j=z\).

Start with \(A=\varnothing\). Equations (6) and (8) show that each
step has a nonnegative coefficient in (3), preserves strictly
positive entries, and preserves reciprocal property (P). Induction
ends at \(H^Z=F\). This proves (5) independently of the manuscript's
counting of chains. Equation (5) also proves independence of the order
of elimination.

As a separate interpretation, \((I-B)^{-1}=\sum_{n\ge0}B^n\)
converges in norm. Its entries are nonnegative. Each monomial is the
weight of a chain of intermediate nodes, which recovers the
manuscript's description and checks that endpoints receive no extra
quadrature weight. If two physical nodes coincide, summing their
weights combines identical chain terms. Alternatively, (6)--(8)
already work with the two copies as distinct indices.

## 4. A quantitative quadrature passage

Let \(\rho\) be a finite nonnegative measure supported in a compact set
\(X\), and put \(m=\rho(X)\). Let \(C\) be a continuous symmetric
strictly positive kernel on \(X\cup E\), where \(E\) is any fixed
finite set of evaluation points. Assume all its finite reciprocal
matrices have (P). Write \(T\) for the integral operator with kernel
\(C\) on \(L^2(\rho)\), and suppose \(\|T\|\le d<1\).
Set \(\alpha=1-d\).

For a finite measurable partition of \(X\), choose representatives
in its positive-mass cells and let \(\pi\) map each cell to its
representative. Ignore null cells. Define
\[
 T_\pi f(s)=\int_X C(\pi(s),\pi(t))f(t)\,d\rho(t),\quad
 g_x(t)=C(x,t),\quad g_x^\pi(t)=C(x,\pi(t)).
\]
Suppose
\[
 \eta=\sup_{s,t\in X}|C(\pi(s),\pi(t))-C(s,t)|,\quad
 e=m\eta<\alpha,\quad \beta=\alpha-e>0.
\]
Suprema can be taken off the null cells. For every \(f\),
\[
 |(T_\pi-T)f(s)|\le\eta\int_X|f|\,d\rho
 \le\eta\sqrt m\,\|f\|_2.
\]
Integration in \(s\) therefore gives \(\|T_\pi-T\|\le m\eta=e\).
Consequently \(\|T_\pi\|\le d+e<1\). With
\(R=(I-T)^{-1}\) and \(R_\pi=(I-T_\pi)^{-1}\),
the norm-convergent geometric series imply
\[
 \|R\|\le\alpha^{-1},\quad
 \|R_\pi\|\le\beta^{-1},\quad
 R_\pi-R=R_\pi(T_\pi-T)R,\quad
 \|R_\pi-R\|\le\frac e{\alpha\beta}.                            \tag{9}
\]

Set \(b_x=\|g_x\|_2\), \(\delta_x=\|g_x^\pi-g_x\|_2\), and define
\[
 F(x,y)=C(x,y)+\langle g_x,Rg_y\rangle,\quad
 F_\pi(x,y)=C(x,y)+\langle g_x^\pi,R_\pi g_y^\pi\rangle.
\]
Adding and subtracting terms gives precisely
\[
 \begin{aligned}
 F_\pi-F={}&
 \langle g_x^\pi-g_x,R_\pi g_y^\pi\rangle
 +\langle g_x,R_\pi(g_y^\pi-g_y)\rangle\\
 &+\langle g_x,(R_\pi-R)g_y\rangle.
 \end{aligned}
\]
Thus (9) gives the explicit estimate
\[
 \boxed{\displaystyle
 |F_\pi(x,y)-F(x,y)|
 \le \frac{\delta_x(b_y+\delta_y)+b_x\delta_y}{\beta}
       +\frac{b_xb_y e}{\alpha\beta}.}                          \tag{10}
\]
Also
\(\delta_x\le\sqrt m\sup_{t\in X}|C(x,\pi(t))-C(x,t)|\).
Uniform continuity on the compact sets makes \(\eta\) and all these
source errors tend to zero with the maximum cell diameter. Formula
(10) proves convergence at every fixed pair of evaluation points.
The case \(m=0\) gives \(F_\pi=F=C\) directly.

On the span of normalized cell indicators, \(T_\pi\) is the finite
matrix \(W^{1/2}C_{ZZ}W^{1/2}\), and it vanishes on the orthogonal
complement. The source vectors lie in that span. Thus \(F_\pi\)
is exactly (5). Section 3 proves (P) for each of its finite reciprocal
matrices, including coincident evaluation and integration points.

The geometric series for \(R\) and \(R_\pi\), and positivity of \(C\),
give \(F,F_\pi\ge C>0\) entrywise. Hence
\[
 \left|\frac1{F_\pi(x,y)}-\frac1{F(x,y)}\right|
 \le\frac{|F_\pi(x,y)-F(x,y)|}{C(x,y)^2}.                        \tag{11}
\]
The reciprocal matrices therefore converge entrywise in each fixed
finite dimension. Property (P) is closed under this convergence:
if the limiting form were positive on a two-dimensional subspace,
its minimum on the unit circle of that subspace would be strictly
positive, and uniform convergence of the forms there would make
the approximating forms positive on that subspace as well. This
contradicts (P). Thus the continuum resolvent \(F\) has (P).

This proves the bounded continuous compact-support quadrature step.
It uses neither point evaluation of a singular Green kernel at its
integration nodes nor a boundary \(L^2\) assertion.

## 5. Attempts to break the conclusion

The restriction \(c\ge0\) in (3) is essential. Take
\[
 M=\begin{pmatrix}
 1&1&1\\1&4/3&4/5\\1&4/5&4/3
 \end{pmatrix},\qquad z=1,\qquad c=-1/2.
\]
Its reciprocal is \(\mathbf1\mathbf1^T-vv^T\), with
\(v=(0,1/2,-1/2)^T\), and so has (P). All entries of
\(\widetilde M=M-\tfrac12\mathbf1\mathbf1^T\) remain positive.
But its reciprocal is
\[
 \begin{pmatrix}
 2&2&2\\2&6/5&10/3\\2&10/3&6/5
 \end{pmatrix}.
\]
Taking the Schur complement of its first entry gives
\[
 \begin{pmatrix}-4/5&4/3\\4/3&-4/5\end{pmatrix},
\]
with eigenvalues \(8/15\) and \(-32/15\).
Together with the first positive pivot 2, the reciprocal has two
positive eigenvalues. Allowing negative updates would invalidate
the result even while every kernel entry stays positive.

The strict spectral threshold is also needed. For the one-node
matrix \(M=(1)\), weight \(w=1\) gives \(B=(1)\); \(I-B\) is singular
and the denominator in (6) is zero. At \(0\le w<1\), (5) instead
gives \(F=(1/(1-w))\) and the denominator is exactly \(1-w\).

The exact rational checks in audit_resolvent.py compare direct
inversion of (5) with (8), and compare (6) with the determinant
ratio (7), for every ordering of four nodes, zero weights,
coincident nodes and coincident evaluation points. They are
finite algebraic checks, not discretized evidence for the full
hot-spots statement.

