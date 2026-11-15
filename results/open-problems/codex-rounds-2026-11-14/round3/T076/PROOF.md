# The centered return propagator for the two-dimensional block profile

Let \(M\geq3\) be an integer, and let \(\mathbb T_M=(\mathbb Z/M\mathbb Z)^2\).
Define the stochastic matrix
\[
B_{ab}=\frac15\bigl(\mathbf1_{a=b}+\mathbf1_{a\sim b}\bigr),
\qquad a,b\in\mathbb T_M,
\]
where each vertex has four distinct nearest neighbors. Let \(P\) be the
orthogonal projection onto constant functions on \(\mathbb T_M\), so that
\(P_{ab}=M^{-2}\). For \(0<\mu\leq1/2\), put \(t=1-\mu\) and
\[
G_\mu=(I-tB)^{-1},\qquad
R_M(\mu)=(G_\mu-\mu^{-1}P)_{00}.
\]
All logarithms are natural. An \(O(1)\) below has an absolute constant,
independent of \(M\) and \(\mu\).

## Proposition

Uniformly for \(M\geq3\) and \(0<\mu\leq1/2\),
\[
\boxed{\displaystyle
R_M(\mu)=\frac5{4\pi}\log\frac1{\mu+M^{-2}}+O(1).}
\tag{1}
\]
In particular the zero-mass limit on the orthogonal complement of constants
exists, and
\[
R_M(0):=\lim_{\mu\downarrow0}R_M(\mu)
       =\frac5{2\pi}\log M+O(1).
\tag{2}
\]

For an integer \(W\geq1\), give each block \(W^2\) sites and set
\(N=W^2M^2\). The normalized block propagator \(K_\mu=W^{-2}G_\mu\)
satisfies
\[
(K_\mu)_{00}
=\frac1{\mu N}+\frac5{4\pi W^2}\log\frac1{\mu+M^{-2}}
 +O(W^{-2}).
\tag{3}
\]
If \(S=B\otimes J\), where \(J\) is the \(W^2\)-by-\(W^2\) matrix
with every entry \(W^{-2}\), then, for every physical site \(x\),
\[
\bigl[tS(I-tS)^{-1}\bigr]_{xx}-\frac{t}{\mu N}
=\frac5{4\pi W^2}\log\frac1{\mu+M^{-2}}+O(W^{-2}).
\tag{4}
\]

## Proof of (1)

### Fourier representation

Choose representatives
\[
I_M=\{-\lfloor M/2\rfloor,\ldots,\lceil M/2\rceil-1\},
\qquad \Lambda_M=I_M^2.
\]
For \(k\in\Lambda_M\), put \(q_k=2\pi k/M\). The normalized characters
\(a\mapsto M^{-1}\exp(iq_k\cdot a)\) form an orthonormal basis and
diagonalize \(B\), with eigenvalues
\[
b(q)=\frac{1+2\cos q_1+2\cos q_2}{5}.
\]
Thus \(-3/5\leq b(q)\leq1\), and \(b(q_k)=1\) only for \(k=0\).
All eigenvalues of \(I-tB\) are positive. The constant character contributes
exactly \((\mu M^2)^{-1}\) to \((G_\mu)_{00}\). Consequently
\[
R_M(\mu)=\frac1{M^2}\sum_{k\in\Lambda_M\setminus\{0\}}
 \frac1{\mu+t a(q_k)},
\qquad
a(q)=1-b(q)=\frac25\sum_{j=1}^2(1-\cos q_j).
\tag{5}
\]

### Uniform replacement by the quadratic symbol

For \(|u|\leq\pi\), the elementary sine bounds and Taylor remainder give
\[
\frac{2u^2}{\pi^2}\leq1-\cos u\leq\frac{u^2}{2},
\qquad
\left|1-\cos u-\frac{u^2}{2}\right|\leq\frac{u^4}{24}.
\]
For the lower bound, use \(1-\cos u=2\sin^2(|u|/2)\) and
\(\sin v\geq2v/\pi\) on \([0,\pi/2]\), which follows from
concavity of sine. The upper bound follows from \(|\sin v|\leq|v|\).
The displayed remainder is Taylor's theorem applied to cosine through
degree three, whose fourth derivative has absolute value at most one.
It follows that, on \([-\pi,\pi]^2\),
\[
\frac4{5\pi^2}|q|^2\leq a(q)\leq\frac15|q|^2,
\qquad
\left|a(q)-\frac15|q|^2\right|\leq C|q|^4.
\tag{6}
\]
Since \(t\geq1/2\), both \(\mu+t a(q)\) and
\(\mu+|q|^2/5\) are bounded below by \(c(\mu+|q|^2)\).
Moreover
\[
\left|t a(q)-\frac15|q|^2\right|
\leq C\bigl(|q|^4+\mu|q|^2\bigr).
\]
Taking the difference of reciprocals therefore gives
\[
\left|\frac1{\mu+t a(q)}-\frac1{\mu+|q|^2/5}\right|
\leq C\frac{|q|^4+\mu|q|^2}{(\mu+|q|^2)^2}\leq C.
\tag{7}
\]
At \(q=0\) the difference is zero. There are fewer than \(M^2\) terms
in (5), and its prefactor is \(M^{-2}\). Hence, with
\(h=\mu M^2\) and \(\alpha=4\pi^2/5\),
\[
R_M(\mu)
=\sum_{k\in\Lambda_M\setminus\{0\}}
       \frac1{h+\alpha|k|^2}+O(1).
\tag{8}
\]
In particular replacing \(t\) by 1 in the quadratic coefficient costs
only a bounded error even when \(\mu\) and \(M^{-2}\) are comparable.

### Comparison with an integral

For \(k\in\mathbb Z^2\), let \(Q_k=k+[-1/2,1/2]^2\), and write
\(f_h(x)=(h+\alpha|x|^2)^{-1}\). If \(k\ne0\) and \(x\in Q_k\),
\[
|x|\geq |k|-\sqrt2/2\geq(1-\sqrt2/2)|k|.
\]
The same bound holds on the segment from \(k\) to \(x\). Also
\[
|\nabla f_h(x)|
=\frac{2\alpha|x|}{(h+\alpha|x|^2)^2}
\leq\frac2{\alpha|x|^3}.
\]
The mean value theorem and \(\operatorname{area}(Q_k)=1\) give
\[
\left|f_h(k)-\int_{Q_k}f_h(x)\,dx\right|\leq C|k|^{-3}.
\tag{9}
\]
These errors are summable independently of \(h\) and \(M\): the shell
\(\{k:\|k\|_\infty=n\}\) has \(8n\) points and \(|k|\geq n\), so
\(\sum_{k\ne0}|k|^{-3}\leq8\sum_{n\geq1}n^{-2}<\infty\).

Let
\[
\mathcal R_M=\bigcup_{k\in\Lambda_M}Q_k,
\qquad E_M=\mathcal R_M\setminus Q_0.
\]
Boundary overlaps have measure zero. Summing (9) proves
\[
\sum_{k\in\Lambda_M\setminus\{0\}}f_h(k)
=\int_{E_M}f_h(x)\,dx+O(1).
\tag{10}
\]

The rectangle \(\mathcal R_M\) contains the disk of radius \(M/4\)
and is contained in the disk of radius \(M\), for both even and odd
\(M\geq3\). Indeed its nearest side is at distance at least
\((M-1)/2\geq M/4\), and every corner has norm at most
\((M+1)/\sqrt2\leq M\). Further, \(Q_0\) contains the disk of radius
\(1/2\) and is contained in the disk of radius \(\sqrt2/2\).
Let \(A_M=\{x:1\leq|x|\leq M\}\). Up to boundaries,
\[
E_M\setminus A_M\subset\{1/2\leq|x|\leq1\},
\qquad
A_M\setminus E_M\subset\{M/4\leq|x|\leq M\}.
\]
Since \(f_h(x)\leq(\alpha|x|^2)^{-1}\), the integrals over these
two differences are at most \((2\pi/\alpha)\log2\) and
\((2\pi/\alpha)\log4\), respectively. Thus
\[
\int_{E_M}f_h(x)\,dx
=\int_{A_M}f_h(x)\,dx+O(1)
=\frac\pi\alpha\log\frac{h+\alpha M^2}{h+\alpha}+O(1).
\tag{11}
\]
The last equality follows by integrating
\(2\pi\int_1^M r(h+\alpha r^2)^{-1}\,dr\).

Substitution of \(h=\mu M^2\) yields
\[
\log\frac{h+\alpha M^2}{h+\alpha}
=\log\frac{\mu+\alpha}{\mu+\alpha M^{-2}}
=\log\frac1{\mu+M^{-2}}+O(1).
\tag{12}
\]
To see uniformity of the final error, its exact value is
\(\log(\mu+\alpha)+\log[(\mu+M^{-2})/(\mu+\alpha M^{-2})]\).
The first term is bounded for \(0<\mu\leq1/2\); the ratio in the
second lies between \(1/\alpha\) and 1, since \(\alpha>1\).
Combining (8), (10), (11), and (12), and using
\(\pi/\alpha=5/(4\pi)\), proves (1).

## Zero mass and physical normalization

For fixed \(M\), each nonzero summand in (5) has a positive limit as
\(\mu\downarrow0\). This proves existence of \(R_M(0)\). The error in
(1) is uniform in \(\mu\), and \(\log(1/M^{-2})=2\log M\), proving
(2). Equation (3) follows by multiplying
\((G_\mu)_{00}=(\mu M^2)^{-1}+R_M(\mu)\) by \(W^{-2}\).

For (4), \(J^2=J\). Since \(t<1\), the Neumann series converges in
operator norm and gives
\[
tS(I-tS)^{-1}=\sum_{n\geq1}t^n B^n\otimes J
             =(G_\mu-I)\otimes J.
\]
Every diagonal entry of \(J\) is \(W^{-2}\). The constant Fourier
mode in \(G_\mu-I\) is \((\mu^{-1}-1)P=(t/\mu)P\).
Consequently the left side of (4) is exactly
\[
W^{-2}\bigl(R_M(\mu)-1+M^{-2}\bigr).
\tag{13}
\]
Equations (1) and (13) prove (4).

## Consequence at exponentially large side lengths

If \(0<\mu\leq M^{-2}\), then
\[
\log\frac1{\mu+M^{-2}}
=2\log M-\log(1+\mu M^2)=2\log M+O(1).
\]
Hence, uniformly in this range,
\[
(K_\mu)_{00}-\frac1{\mu N}
=\frac5{2\pi}\frac{\log M}{W^2}+O(W^{-2}).
\tag{14}
\]
Along any sequence \(W\to\infty\), \(M\geq3\), and
\(0<\mu\leq M^{-2}\), this centered quantity tends to zero if and
only if \(\log M=o(W^2)\). More generally, if
\(\log M/W^2\to\gamma\in[0,\infty]\), it tends to
\(5\gamma/(2\pi)\), with divergence to infinity when \(\gamma=\infty\).
For finite \(\gamma>0\), the physical side length \(WM\) has the same
limit \(\log(WM)/W^2\to\gamma\), since \(\log W/W^2\to0\).

The full diagonal in (3) includes the additional nonnegative term
\((\mu N)^{-1}\). Its behavior cannot be deduced from (14) without
an assumption on \(\mu N\).

## Independent check of the coefficient

Consider the same walk on \(\mathbb Z^2\). Write \(p_n(0)\) for its
return probability after \(n\) steps. Fourier inversion gives
\[
p_n(0)=\frac1{(2\pi)^2}\int_{[-\pi,\pi]^2}b(q)^n\,dq.
\tag{15}
\]
The only point of this square with \(|b(q)|=1\) is \(q=0\).
Indeed \(b(q)\geq-3/5\), and equality \(b(q)=1\) requires
\(\cos q_1=\cos q_2=1\). Outside any fixed sufficiently small disk
about zero, continuity gives \(|b(q)|\leq\rho<1\).
Inside that disk,
\[
b(q)=1-|q|^2/5+O(|q|^4),\qquad
0<b(q)\leq e^{-c|q|^2}.
\]
Set \(q=u/\sqrt n\) in its contribution to (15). For fixed \(u\),
\(b(u/\sqrt n)^n\to e^{-|u|^2/5}\); after extension by zero outside
the rescaled disk the integrand is bounded by \(e^{-c|u|^2}\).
Dominated convergence applies, and the complementary contribution
multiplied by \(n\) is bounded by \(n\rho^n\to0\). Therefore
\[
\lim_{n\to\infty}n p_n(0)
=\frac1{(2\pi)^2}\int_{\mathbb R^2}e^{-|u|^2/5}\,du
=\frac{5\pi}{4\pi^2}=\frac5{4\pi}.
\tag{16}
\]
The Gaussian integral is \(2\pi\int_0^\infty r e^{-r^2/5}\,dr=5\pi\).
This also checks the normalization from the one-step covariance:
each coordinate has variance \(2/5\), so the limiting diffusion
coefficient is \(1/5\) in each direction.

For completeness, (16) gives a second derivation of the logarithmic
coefficient without using the lattice-to-integral comparison above.
Let \(c_0=5/(4\pi)\). For every \(\epsilon>0\), choose \(n_0\)
such that \(|p_n(0)-c_0/n|\leq\epsilon/n\) for \(n\geq n_0\).
For \(0<t<1\), the initial finitely many terms have bounded sum, while
\[
\left|\sum_{n\geq n_0}t^n\left(p_n(0)-\frac{c_0}{n}\right)\right|
\leq\epsilon\sum_{n\geq1}\frac{t^n}{n}
=\epsilon\log\frac1{1-t}.
\]
The identity on the right follows by integrating the geometric series
from 0 to \(t\). Divide by \(\log(1/(1-t))\), let \(t\uparrow1\),
and then \(\epsilon\downarrow0\). It follows that
\[
\sum_{n\geq0}t^n p_n(0)
\sim\frac5{4\pi}\log\frac1{1-t}.
\tag{17}
\]
This independent check gives the same coefficient as (1); the uniform
bounded error and finite-size cutoff are supplied by the first proof.

## Small-volume and constant-mode checks

For \(M=3\), the Fourier eigenvalues are 1 with multiplicity one,
\(2/5\) with multiplicity four, and \(-1/5\) with multiplicity four.
Indeed \(\cos(2\pi/3)=\cos(-2\pi/3)=-1/2\); one nonzero coordinate
gives \(b=(1+2-1)/5=2/5\), and two give
\(b=(1-1-1)/5=-1/5\). Thus the exact centered diagonal is
\[
R_3(\mu)=\frac49\left(\frac1{1-2t/5}+\frac1{1+t/5}\right),
\qquad R_3(0)=\frac49\left(\frac53+\frac56\right)=\frac{10}{9}.
\tag{18}
\]
At \(\mu=1/2\) this gives
\(R_3(1/2)=(4/9)(5/4+10/11)=95/99\).
This includes negative eigenvalues and both ends of the mass range without
any singular nonconstant mode. For even \(M\), the mode
\(q=(-\pi,-\pi)\) has eigenvalue \(-3/5\), with denominator
\(1+3t/5\geq1\). It creates no additional low-mass divergence.
The geometric integral comparison above explicitly handles either parity.
For \(M=1,2\) the distinct-neighbor convention changes, so those tori
are outside the proposition.

As a separate test of (3), take \(W\to\infty\),
\(M=\lfloor e^W\rfloor\), and \(\mu=N^{-1}\). Then
\(\mu\leq M^{-2}\), and (14) gives a centered diagonal tending to
zero. Nevertheless \((\mu N)^{-1}=1\), so
\((K_\mu)_{00}\to1\). Thus the smallness of the centered propagator
cannot be substituted for smallness of the full propagator.

## Relation to the random-matrix question

The matrix \(B\) is precisely the block variance profile in equation
(1.5) of Xujie Lai and Fan Yang,
*Localization Lengths for Two-Dimensional Random Band Matrices: Exponential
Lower Bounds*, [arXiv:2609.24426v4](https://arxiv.org/abs/2609.24426v4).
Their equation (2.31) defines the same propagator, and Lemma 2.7 gives
upper bounds with a logarithmic spatial factor. Formula (1) identifies
its diagonal coefficient and separates the constant mode uniformly down
to zero mass.

These are statements about the deterministic variance kernel. They do
not bound the difference between a random resolvent observable and its
deterministic approximation. In particular (14) supplies neither a
localization-length theorem nor a criterion for Wigner–Dyson statistics.
The number \(5/(2\pi)\) is a return-kernel coefficient for this profile;
it is not a proved constant in an eigenvector localization length.
