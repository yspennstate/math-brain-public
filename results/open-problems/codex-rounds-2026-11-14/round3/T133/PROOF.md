# Local continuation of the disordered Fredholm formulas

The definitions below are the disordered formulas in Alexey Bufetov,
[*Limit shape for domain-wall six-vertex model*, arXiv:2609.20576v1](https://arxiv.org/html/2609.20576v1),
equations (2.1)–(2.4), (2.13), and (4.3), continued by definition to
all $0<\gamma<\pi$. The results here concern these analytic formulas.
They do not establish convergence of a six-vertex measure.

## Definitions and result

Fix $0<\gamma<\pi$, put $\delta=\pi-\gamma$, and choose

\[
0<u<\delta,\qquad T=\delta-u,\qquad |\theta|<T.
\]

The omitted physical interval $1/2<\Delta<1$ corresponds to

\[
\Delta=\cos\gamma,\qquad 0<\gamma<\pi/3.
\]

For real $z$, let

\[
k(z)=\frac{\sin(2\gamma)}{2\pi(\cosh z-\cos(2\gamma))},
\quad \gamma\ne\pi/2;
\qquad k(z)=0,\quad\gamma=\pi/2.
\]

On $I_B=[-B,B]$, $B>0$, define

\[
(K_Bg)(s)=\int_{-B}^B k(s-t)g(t)\,dt,
\qquad (U_fg)(s)=\int_{-B}^B f(t)g(t)\,dt.
\]

The last integral is complex linear, with no conjugation of $f$. Set

\[
\mathcal D_B[f]=\frac{\det(I-K_B+U_f)}{\det(I-K_B)}-1.
\]

Define meromorphic functions, using removable continuation where necessary,

\[
A(z)=\frac{\sin\gamma}{2\pi(\cosh z+\cos\gamma)},
\]

\[
L(z)=\frac{\sin T}{2\pi(\cosh z-\cos T)}
-\frac{\sin(\pi T/\delta)}
 {2\delta(\cosh(\pi z/\delta)-\cos(\pi T/\delta))}.
\]

For real $x,y$, write

\[
F(z;x,y,\theta)=xA(z+i(\theta-u))
+yA(z+i(\theta+u))-L(z+i\theta),
\quad \Phi(B;x,y,\theta)=\mathcal D_B[F(\cdot;x,y,\theta)].
\]

The strict inequalities on $\theta$ keep all these functions holomorphic
in a neighborhood of the real integration segment. In particular, the first
possible poles of $A$ have imaginary part $\pm\delta$, and the two
terms defining $L$ have no poles in $|\operatorname{Im}z|<T$.

**Proposition.** For every fixed $0<\gamma<\pi$:

1. For every $B>0$, $K_B$ is trace class and
   \[
   \|K_B\|_{2\to2}\le q_\gamma:=|1-2\gamma/\pi|<1.
   \]
   Consequently $\det(I-K_B)>0$. If
   $\rho_B=(I-K_B)^{-1}1$, then
   \[
   \mathcal D_B[f]=\int_{-B}^B f(s)\rho_B(s)\,ds.
   \tag{1}
   \]
   The function $\rho_B$ is real and even. For $\gamma<\pi/2$,
   \[
   1\le\rho_B(s)\le\frac{\pi}{2\gamma}.
   \]

2. Let
   \[
   a(\theta)=A(i(\theta-u)),\quad b(\theta)=A(i(\theta+u)),
   \quad e(\theta)=L(i\theta),\quad W=ab'-a'b.
   \]
   Then $W>0$ for every $|\theta|<T$. Put
   \[
   x_0=\frac{eb'-e'b}{W},\qquad
   y_0=\frac{ae'-a'e}{W}.
   \tag{2}
   \]
   For each such $\theta$, and all sufficiently small $B>0$, there is
   a unique real pair $(x(B,\theta),y(B,\theta))$ satisfying
   \[
   \partial_B\Phi=\partial_\theta\Phi=0.
   \tag{3}
   \]
   The pair extends real analytically to $B=0$, with value $(x_0,y_0)$.
   The allowed size of $B$ can be chosen uniformly on compact subintervals
   of $(-T,T)$, with $\gamma,u$ fixed.

3. Define, with the values $x_0,y_0$ held fixed inside each expression,
   \[
   C=x_0a''+y_0b''-e'',\qquad
   D=x_0a'''+y_0b'''-e'''.
   \]
   Then
   \[
   \begin{split}
   x(B,\theta)&=x_0+B^2\frac{3Cb'-Db}{6W}+O(B^3),\\
   y(B,\theta)&=y_0+B^2\frac{aD-3a'C}{6W}+O(B^3).
   \end{split}
   \tag{4}
   \]
   Thus the quadratic displacement is independent of the integral kernel
   when $A,L$ are held fixed. If $C\ne0$, the critical point is a
   nondegenerate saddle for sufficiently small $B>0$:
   \[
   \det\operatorname{Hess}_{B,\theta}\Phi
   =-4C^2 B^2+O(B^3)<0.
   \tag{5}
   \]

Uniqueness in part 2 refers to the pair $(x,y)$ for fixed $B,\theta$.
It does not assert uniqueness of $(B,\theta)$ for prescribed $x,y$,
nor that the pairs lie in the physical liquid region.

## Proof of the operator statements

First suppose $0<\gamma<\pi/2$. The substitution $t=\tanh(z/2)$
gives

\[
\begin{split}
\int_{\mathbb R}k(z)\,dz
&=\frac{\sin(2\gamma)}{2\pi}
  \int_{-1}^{1}\frac{dt}{\sin^2\gamma+\cos^2\gamma\,t^2}\\
&=\frac2\pi\arctan(\cot\gamma)
=1-\frac{2\gamma}{\pi}.
\end{split}
\tag{6}
\]

For $\pi/2<\gamma<\pi$, put $\beta=\pi-\gamma$. Directly from
the formula, $k_\gamma=-k_\beta$, so the signed integral is again

\[
\int_{\mathbb R}k(z)\,dz=1-2\gamma/\pi.
\]

The kernel has constant sign. Hence $\int_{\mathbb R}|k|=q_\gamma$.
The result also holds at $\gamma=\pi/2$, where both sides are zero.
Every row and column integral of $|k(s-t)|$ over $I_B$ is at most

\[
q_\gamma<1.
\]

Schur's inequality proves the $L^2$ bound. The same row integral gives
the $L^\infty$ bound. Therefore the Neumann series for $I-K_B$
converges on both spaces, and

\[
\|(I-K_B)^{-1}\|\le (1-q_\gamma)^{-1}.
\tag{7}
\]

Here is a trace-class justification independent of any positivity assertion
about the kernel. On a larger square $[-R,R]^2$, $R>B$, multiply

\[
k(s-t)
\]

by smooth cutoffs in $s,t$, equal to one on $I_B$ and supported away
from the boundary of the larger square. Periodic extension gives a smooth
two-variable function. Integrating its Fourier coefficients twice in each
variable bounds them by

\[
\frac{M}{(1+m^2)(1+n^2)}.
\]

Their absolute sum is finite. Restricted to $I_B^2$, each Fourier term
defines a rank-one operator of trace norm $2B$ times its coefficient's
absolute value. Thus the series converges in trace norm to $K_B$.
The original kernel is real and symmetric, so $K_B$ is self-adjoint.
Its real eigenvalues $\lambda_j$ satisfy $|\lambda_j|\le q_\gamma<1$
and $\sum_j|\lambda_j|<\infty$. Consequently

\[
\det(I-K_B)=\prod_j(1-\lambda_j)>0.
\]

For $f\in L^2(I_B)$, write $U_f=1\otimes\lambda_f$, where

\[
\lambda_f(g)=\int_{I_B}f(t)g(t)\,dt.
\]

Factoring the invertible operator $I-K_B$ in the determinant quotient
reduces it to the determinant of

\[
I+\rho_B\otimes\lambda_f.
\]

A rank-one determinant is $1+\lambda_f(\rho_B)$. This proves (1),
including complex linearity in $f$. Reflection and complex conjugation
commute with $K_B$; uniqueness of the resolvent equation makes
\$\rho_B\$ even and real. Its Neumann series also converges in the
uniform norm and gives a continuous representative. If $\gamma<\pi/2$,
the kernel is nonnegative, so every term in that series is nonnegative and

\[
1\le\rho_B\le\sum_{j\ge0}q_\gamma^j
=\frac1{1-q_\gamma}=\frac\pi{2\gamma}.
\]

For any $f$ satisfying $f(-s)=\overline{f(s)}$, (1) is real.
The functions defining $\Phi$ have this property for real $x,y,\theta$.

## Nonvanishing of the envelope determinant

Set $c=\cos\gamma$ and $c_0=\sin\gamma/(2\pi)>0$. On

\[
-\delta<t<\delta
\]

one has $\cos t+c>0$. The function

\[
g(t)=\frac{\sin t}{\cos t+c}
\]

satisfies

\[
g'(t)=\frac{1+c\cos t}{(\cos t+c)^2}>0,
\tag{8}
\]

since $|c|<1$. Both $\theta-u$ and $\theta+u$ belong to this
interval. Differentiating $a=c_0/(\cos(\theta-u)+c)$ and the analogous
formula for $b$,

\[
\frac{a'}a=g(\theta-u),\qquad \frac{b'}b=g(\theta+u).
\]

Since $u>0$, strict monotonicity gives

\[
W=ab\bigl(g(\theta+u)-g(\theta-u)\bigr)>0.
\tag{9}
\]

In particular (2) is the unique solution of

\[
ax_0+by_0=e,\qquad a'x_0+b'y_0=e'.
\tag{10}
\]

## Expansion and the local critical branch

Rescale the interval to $[-1,1]$. Its kernel becomes

\[
(\widetilde K_Bh)(r)=B\int_{-1}^1 k(B(r-t))h(t)\,dt.
\]

This is an analytic operator-valued function of $B$ near zero, on the
space of continuous functions, and its norm is $O(|B|)$. Its Neumann
series converges there for sufficiently small complex $B$. This defines
an analytic extension of the rescaled resolvent density and of

\[
\Phi(B)=B\int_{-1}^1 F(Br;x,y,\theta)\,
 (I-\widetilde K_B)^{-1}1(r)\,dr.
\tag{11}
\]

The same assertion holds with derivatives in $x,y,\theta$, locally
uniformly in the strict parameter domain. Negative $B$ in this analytic
extension is an auxiliary parameter, not an interval with reversed limits.

Let $k_0=k(0)$. Evenness of $k$ gives, in the uniform operator norm,

\[
\widetilde K_B=B k_0 J+O(B^3),\qquad
(Jh)(r)=\int_{-1}^1h(t)\,dt.
\]

As $J1=2$ and $J^21=4$, the rescaled density is

\[
(I-\widetilde K_B)^{-1}1
=1+2k_0B+4k_0^2B^2+O(B^3).
\tag{12}
\]

It is exactly even in $r$. Taylor expansion of $F(Br)$ in (11)
therefore yields, with $F_j=\partial_z^jF(0;x,y,\theta)$,

\[
\Phi=2BF_0+4k_0B^2F_0
+B^3\left(8k_0^2F_0+\frac{F_2}{3}\right)+O(B^4).
\tag{13}
\]

Analyticity justifies differentiating the remainder. Thus

\[
\frac{\partial_B\Phi}{2}
=F_0+4k_0BF_0+B^2\left(12k_0^2F_0+\frac{F_2}{2}\right)+O(B^3),
\tag{14}
\]

\[
\frac{\partial_\theta\Phi}{2B}
=\partial_\theta F_0+2k_0B\partial_\theta F_0
+B^2\left(4k_0^2\partial_\theta F_0
+\frac{\partial_\theta F_2}{6}\right)+O(B^3).
\tag{15}
\]

The quotient in (15) extends analytically to $B=0$. Each equation is
affine in $x,y$, and its coefficient matrix at zero is

\[
\begin{pmatrix}a&b\\a'&b'\end{pmatrix},
\]

of determinant $W>0$. Analytic inversion of this two-by-two matrix
proves existence, uniqueness and analyticity of the pair in part 2.
Compactness gives a common sufficiently small neighborhood for $\theta$
in any fixed compact subinterval.

For (4), substitute

\[
x=x_0+Bx_1+B^2x_2+O(B^3),\quad
y=y_0+By_1+B^2y_2+O(B^3)
\]

into (14)–(15). The constant terms vanish by (10). At first order the
matrix above sends $(x_1,y_1)$ to zero, so $x_1=y_1=0$.
All arguments of $A,L$ vary with $z+i\theta$; hence, at fixed $x,y$,

\[
\partial_z^2F=-\partial_\theta^2F,
\qquad \partial_\theta\partial_z^2F=-\partial_\theta^3F.
\]

At $(x_0,y_0)$ these identities give $F_2=-C$ and

\[
\partial_\theta F_2=-D.
\]

The second-order equations are therefore

\[
ax_2+by_2=C/2,\qquad a'x_2+b'y_2=D/6.
\tag{16}
\]

Cramer's rule gives exactly (4).

Finally evaluate second derivatives of (13) at this critical pair, taking
the derivatives at fixed $x,y$. Since $F_0=O(B^2)$ and

\[
\partial_\theta F_0=O(B^2),
\]

one obtains

\[
\Phi_{BB}=-2BC+O(B^2),\quad
\Phi_{\theta\theta}=2BC+O(B^2),\quad
\Phi_{B\theta}=O(B^2).
\]

Their determinant is (5). This completes the proof.

## A second derivation of the two quadratic constants

Define even moments

\[
M_j(B)=\int_{-B}^B s^j\rho_B(s)\,ds.
\]

Rescaling and (12) give

\[
M_0=2B+O(B^2),\quad M_2=2B^3/3+O(B^4),\quad M_4=O(B^5).
\]

Evenness and Taylor expansion in (1) give

\[
\Phi=M_0F_0+\tfrac12M_2F_2+O(B^5).
\]

These are analytic expansions, so they can be differentiated. Dividing the

\[
\partial_B\Phi=0
\]

equation by $M_0'$, and the $\partial_\theta\Phi=0$ equation by

\[
M_0,
\]

gives coefficients

\[
\frac{M_2'}{2M_0'}=\frac{B^2}{2}+O(B^3),\qquad
\frac{M_2}{2M_0}=\frac{B^2}{6}+O(B^3).
\]

These independently recover the constants $1/2$ and $1/6$ in (16).

## Exact free-fermion check

At $\gamma=\pi/2$, $u=T=\pi/4$, and $\theta=0$, the kernel vanishes.
Reflection interchanges the two $A$ terms, and the $\theta$-derivative
equation vanishes when $x=y$. If $c=\cosh B$ and $q=1/\sqrt2$, direct
simplification gives

\[
A(B-iu)+A(B+iu)=\frac{\sqrt2 c}{\pi(2c^2-1)},
\]

\[
L(B)=\frac{q}{2\pi(c-q)}-\frac1{\pi(2c^2-1)}
=\frac{qc-1/2}{\pi(2c^2-1)}.
\]

Since $\Phi$ is now an ordinary integral and its integrand is even for
$x=y$, its $B$-derivative is twice the integrand at $B$. Thus

\[
x(B)=y(B)=\frac{L(B)}{A(B-iu)+A(B+iu)}
=\frac12-\frac1{2\sqrt2\cosh B}
=\frac12-\frac1{2\sqrt2}+\frac{B^2}{4\sqrt2}+O(B^4).
\]

This verifies both the envelope point on the known circle and the
quadratic displacement without the general perturbation argument.

## Scope and excluded limits

The bounds concern each fixed $0<\gamma<\pi$; the resolvent estimate
deteriorates as $\gamma\to0$ or $\gamma\to\pi$. The branch theorem
is local in $B$ and excludes $\theta=\pm T$, where coefficients have
poles before taking endpoint limits. It also excludes $u=0,\delta$.
The saddle conclusion is conditional on $C\ne0$; no assertion about
all possible zeros of $C$ is needed for existence of the branch.
No probabilistic input, global critical-point classification, physical
admissibility of the branch, or frozen-boundary convergence follows from
this proposition.
