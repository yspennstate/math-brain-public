# Polynomial activations for the projected spherical kernel

Let the columns of $X\in\mathbb R^{d\times N}$ be independent and
uniform on the sphere of radius $\sqrt d$. Independently, let
$W\in\mathbb R^{m\times d}$ have independent standard real Gaussian
entries. Assume

\[
 N/d\longrightarrow\alpha\in(0,\infty),\qquad
 b_N=m/N\longrightarrow b\in(0,\infty)\setminus\{1\}.
\]

Let $\sigma$ be a fixed real polynomial of degree $k\geq2$, satisfying

\[
 \mathbb E\sigma(Z)=\mathbb E[Z\sigma(Z)]=0,\qquad
 v=\mathbb E\sigma(Z)^2>0,\qquad Z\sim N(0,1).
\]

Put $Y_{ij}=\sigma(w_i^Tx_j/\sqrt d)$,
$e=N^{-1/2}(1,\ldots,1)^T$, and $P=I_N-ee^T$.

**Theorem.** For $K_P=YPY^T/N$,

\[
 \frac{b_N^{1/6}}{v(1+\sqrt{b_N})^{4/3}}N^{2/3}
 \left[\lambda_{\max}(K_P)-v(1+\sqrt{b_N})^2\right]
 \ \Longrightarrow\ \mathrm{TW}_1.                         \tag{1}
\]

Consequently $\lambda_{\max}(K_P)\to v(1+\sqrt b)^2$ in probability.
The degree and coefficients of $\sigma$ do not vary with dimension.
There is no restriction on its quadratic Hermite coefficient.

The main estimate is the polynomial quadratic-form bound in Section 2.
The covariance and edge argument below also records why projection and
finite-dimensional centering suffice.

## 1. Two Gaussian inequalities

For a real polynomial $H$ of total degree at most $l$ in any number
of independent standard Gaussian variables, Gaussian hypercontractivity
gives

\[
 \|H\|_p\leq(p-1)^{l/2}\|H\|_2,\qquad p\geq2.             \tag{2}
\]

The classical semigroup inequality used here is equation (1.1) of
Yuu Hariya, *A unification of the hypercontractivity and its exponential
variant of the Ornstein-Uhlenbeck semigroup*,
[arXiv:1707.03163v2](https://arxiv.org/html/1707.03163):
$\|Q_tH\|_p\leq\|H\|_2$ for $e^{2t}=p-1$.
To obtain (2) for an inhomogeneous polynomial, write
$H=\sum_{j=0}^l H_j$ in orthogonal Hermite degrees, and put
$G=\sum_{j=0}^l e^{tj}H_j$. The Hermite generating function shows
$Q_tH_j=e^{-tj}H_j$, so $Q_tG=H$. Orthogonality gives
$\|G\|_2^2=\sum_j e^{2tj}\|H_j\|_2^2
\leq e^{2tl}\|H\|_2^2$. Semigroup contraction now proves (2).
This explains both the constant and its independence of dimension.

We also use Gaussian Poincare for polynomials,

\[
 \operatorname{Var}H(g)\leq\mathbb E\|\nabla H(g)\|^2.       \tag{3}
\]

Indeed expand $H=\sum_\nu c_\nu h_\nu$ in the orthonormal product
Hermite basis. The derivative identity
$\partial_jh_\nu=\sqrt{\nu_j}h_{\nu-e_j}$ gives
$\mathbb E\|\nabla H\|^2=\sum_\nu |\nu|c_\nu^2$, whereas
$\operatorname{Var}H=\sum_{|\nu|\geq1}c_\nu^2$. This proves (3).
All these sums are finite.

## 2. Quadratic forms of projected polynomial features

Fix a deterministic $d\times N$ matrix $U$ with unit columns and
$\|U\|_{\rm op}\leq C_U$. Let $Q$ be any deterministic $N\times M$
matrix with $Q^TQ=I_M$. For standard Gaussian $g\in\mathbb R^d$, set

\[
 p(g)=\sigma(U^Tg),\qquad z(g)=Q^Tp(g),\qquad
 T=\mathbb E zz^T.
\]

Here it suffices to assume $\mathbb E\sigma(Z)=0$; no Hermite-rank
condition is needed for this section. Unit columns imply
$\mathbb Ep=0$ and hence $\mathbb Ez=0$. Assume
$\|T\|_{\rm op}\leq C_T$. Define the finite scalar constant

\[
 D_4=\left(\mathbb E|\sigma'(Z)|^4\right)^{1/4}.
\]

For every real symmetric $A\in\mathbb R^{M\times M}$ and $p\geq2$,

\[
 \|z^TAz-\operatorname{Tr}(AT)\|_p
 \leq 2 C_U D_4\,3^{k/2}\sqrt{C_T}\,(p-1)^k\|A\|_F.       \tag{4}
\]

To prove this, put $F(g)=z(g)^TAz(g)$ and
$L_j(g)=(QAz(g))_j$. Differentiation gives the exact identity

\[
 \nabla F=2U\operatorname{diag}(\sigma'(U^Tg))QAz.
\]

Apply (3), the operator bound on $U$, and Cauchy–Schwarz to obtain

\[
 \begin{split}
 \operatorname{Var}F
 &\leq4C_U^2\sum_{j=1}^N
     \mathbb E[\sigma'(u_j^Tg)^2L_j(g)^2]\\
 &\leq4C_U^2D_4^2\sum_{j=1}^N\|L_j\|_4^2.
 \end{split}                                                   \tag{5}
\]

Each $L_j$ is a polynomial of degree at most $k$ in the independent
coordinates of $g$. Equation (2), with $p=4$, gives
$\|L_j\|_4^2\leq3^k\mathbb E L_j^2$. Moreover

\[
 \sum_j\mathbb EL_j^2
 =\mathbb E\|QAz\|^2
 =\operatorname{Tr}(A^2T)
 \leq C_T\|A\|_F^2.                                        \tag{6}
\]

Combining (5) and (6) bounds the variance of $F$. The centered polynomial
$F-\mathbb EF$ has degree at most $2k$, so another application of (2)
gives
$\|F-\mathbb EF\|_p\leq(p-1)^k\sqrt{\operatorname{Var}F}$.
Since $\mathbb EF=\operatorname{Tr}(AT)$, this is (4).
For complex symmetric $A$, apply the real bound to its real and
imaginary parts and use the triangle inequality; an additional factor
$\sqrt2$ suffices. Thus (4) verifies the dimension-uniform moment
condition for every deterministic complex symmetric quadratic form.

Neither independence of the coordinates of $z$ nor independence between
$\sigma'(u_j^Tg)$ and $L_j(g)$ was used. In particular the estimate
survives projection even if the ambient covariance has a large eigenvalue.

## 3. Conditional covariance and projection

Write $u_j=x_j/\sqrt d$, $U=(u_1,\ldots,u_N)$, and
$\rho_{jl}=u_j^Tu_l$. Let
$h_j=\mathrm{He}_j/\sqrt{j!}$ and
$\sigma=\sum_{j=2}^k a_jh_j$. Set $q=a_2^2$; then
$v=\sum_{j=2}^k a_j^2$.

Given $U$, the rows of $Y$, considered as column vectors $p_i$, are
independent and centered. The joint Gaussian generating identity
$\mathbb E e^{sG-s^2/2}e^{tH-t^2/2}=e^{\rho st}$ implies
$\mathbb Eh_j(G)h_l(H)=\mathbf1_{j=l}\rho^j$. Therefore their
conditional covariance is exactly

\[
 \Sigma_{jl}=\sum_{s=2}^k a_s^2\rho_{jl}^s,\qquad
 \Sigma_{jj}=v.                                             \tag{7}
\]

Let $B,R$ be zero-diagonal symmetric matrices with

\[
 B_{jl}=\rho_{jl}^2-1/d,\qquad
 R_{jl}=\sum_{s=3}^k a_s^2\rho_{jl}^s\quad(j\ne l).
\]

Empty sums are zero. Then

\[
 \Sigma=(v-q/d)I_N+(q/d)\mathbf1\mathbf1^T+qB+R.             \tag{8}
\]

For two independent unit spherical vectors, radial Gaussian moments give

\[
 \mathbb E\rho^{2s}=
 \frac{1\cdot3\cdots(2s-1)}{d(d+2)\cdots(d+2s-2)}.          \tag{9}
\]

Indeed a standard Gaussian vector is its independent uniform direction
times its length; divide the moment of its first coordinate by the
corresponding moment of its length. Since
$|R_{jl}|\leq v|\rho_{jl}|^3$, (9) gives

\[
 \mathbb E\|R\|_F^2\leq
 \frac{15v^2N(N-1)}{d(d+2)(d+4)}=O(N^{-1}).                 \tag{10}
\]

With $D=\Sigma-vI_N$, (7) also yields

\[
 \operatorname{Tr}D=0,\qquad
 \mathbb E\operatorname{Tr}D^2\leq
 \frac{3v^2N(N-1)}{d(d+2)}=O(1).                            \tag{11}
\]

For clarity the needed operator bound for $B$ follows from its fourth
trace. Put $c=1-1/d$, $\tau=2/[d(d+2)]$, and
$\mu_4=\mathbb E(\rho^2-1/d)^4$. In the space of traceless symmetric
$d\times d$ matrices, $z(u)=uu^T-I_d/d$ has mean zero, squared norm
$c$, and covariance $\tau I$. The last assertion follows by contracting

\[
 \mathbb E u_a u_b u_c u_f=
 \frac{\delta_{ab}\delta_{cf}+\delta_{ac}\delta_{bf}
                         +\delta_{af}\delta_{bc}}{d(d+2)}
\]

against two traceless symmetric matrices. Sign and rotational symmetry
give this fourth-moment identity, and summing
$\mathbb E(\sum_a u_a^2)^2=1$ fixes its constant.
Off the diagonal $B_{jl}=\langle z(u_j),z(u_l)\rangle$.
The closed-walk expansion of $\operatorname{Tr}B^4$ has two, three
or four distinct vertices. Alternating two-vertex walks number $(N)_2$
and have expectation $\mu_4$. The two three-vertex patterns each number
$(N)_3$ and have expectation $(c\tau)^2$, by conditioning on the
repeated vertex. Four-vertex walks number $(N)_4$ and have expectation
$c\tau^3$, by integrating two opposite vertices first. Thus

\[
 \mathbb E\operatorname{Tr}B^4
   =(N)_2\mu_4+2(N)_3(c\tau)^2+(N)_4c\tau^3.                \tag{12}
\]

Expansion using (9) gives

\[
 \begin{split}
 \mu_4={}&\frac{105}{d(d+2)(d+4)(d+6)}
 -\frac{60}{d^2(d+2)(d+4)}+\frac{18}{d^3(d+2)}-\frac3{d^4}\\
 ={}&\frac{12(d-1)(5d^2-13d+12)}{d^4(d+2)(d+4)(d+6)}
 \leq\frac{60}{d^4}\quad(d\geq2).
 \end{split}
\]

Since $c\leq1$ and $\tau\leq2/d^2$, (12) is bounded by
$60N^2/d^4+8N^3/d^4+8N^4/d^6=O(N^{-1})$.
As $\|B\|_{\rm op}^4\leq\operatorname{Tr}B^4$,
$\|B\|_{\rm op}=O_p(N^{-1/4})=o_p(1)$.

Choose deterministic $Q\in\mathbb R^{N\times M}$ with
$M=N-1$, $Q^TQ=I_M$, and $QQ^T=P$. Then $Q^T\mathbf1=0$.
The projected conditional covariance is

\[
 T=Q^T\Sigma Q=(v-q/d)I_M+qQ^TBQ+Q^TRQ.
\]

Consequently $\|T-vI_M\|_{\rm op}=o_p(1)$. Also, with $A_0=T-vI_M$,

\[
 \operatorname{Tr}A_0=-e^TDe=-q(N-1)/d+o_p(1),\qquad
 \|A_0\|_F^2\leq\|D\|_F^2=O_p(1).                         \tag{13}
\]

The trace identity uses $QQ^T=P$ and $\operatorname{Tr}D=0$;
the asymptotic formula uses (8), $\|B\|_{\rm op}=o_p(1)$ and (10).
The Frobenius inequality follows from contraction by $Q,Q^T$.
Projection therefore removes the constant covariance spike while leaving
a bounded, generally nonzero, trace defect.

## 4. Covariance-edge displacement

Let $t_1,\ldots,t_M$ be positive numbers,
$r=M/m$ in a fixed positive compact interval, and
$\epsilon=\max_j|t_j-v|\to0$. Put

\[
 \mu=M^{-1}\sum_j(t_j-v),\quad s_2=M^{-1}\sum_j(t_j-v)^2,
 \quad f(u)=-1/u+m^{-1}\sum_j\frac{t_j}{1+t_ju}.
\]

There is a unique $u_+\in(-1/t_{\max},0)$ with $f'(u_+)=0$.
Set $E_T=f(u_+)$, $\gamma_T=(2/f''(u_+))^{1/3}$ and

\[
 u_0=-\frac1{v(1+\sqrt r)},\quad E_0=v(1+\sqrt r)^2,
 \quad\gamma_0=\frac{r^{1/6}}{v(1+\sqrt r)^{4/3}}.
\]

Uniformly for sufficiently small $\epsilon$,

\[
 |u_+-u_0|+|E_T-E_0|+|\gamma_T-\gamma_0|
 \leq C(|\mu|+s_2),\qquad 1+t_{\max}u_+\geq c_0>0.         \tag{14}
\]

Here is a direct proof. For $f_0(u)=-1/u+rv/(1+vu)$,
$f_0'(u_0)=0$ and $f_0''(u_0)=2v^3(1+\sqrt r)^4/\sqrt r>0$.
Choose a fixed small interval $J$ about $u_0$ so $u<0$, all
$1+t_ju$ have a uniform positive lower bound, $f_0''$ is bounded below,
and $f_0'$ has opposite signs at its endpoints. The choices can be
uniform over the compact range of $r$ and sufficiently small $\epsilon$.
For $\delta=t-v$ the exact identity is

\[
 \frac{t}{1+tu}-\frac{v}{1+vu}
 =\frac{\delta}{(1+vu)^2}
  -\frac{u\delta^2}{(1+vu)^2(1+tu)}.                       \tag{15}
\]

The last term and its first two $u$-derivatives on $J$ are bounded by
$C\delta^2$. Averaging yields
$\sup_J|f^{(l)}-f_0^{(l)}|\leq C(|\mu|+s_2)$ for $l=0,1,2$.
Thus $f'$ has a zero in $J$, with $f''$ bounded below there.
On the whole pole interval,
$f''(u)=-2/u^3+(2/m)\sum_jt_j^3/(1+t_ju)^3>0$;
$f'$ tends to $-\infty$ at the left endpoint and $+\infty$ at zero.
The zero in $J$ is therefore unique. The mean value theorem bounds
$|u_+-u_0|$ by $C(|\mu|+s_2)$. Evaluation of $f$ bounds the edge
displacement by the same quantity. The bound on its second derivative
at $u_+$ follows from bounded $f_0'''$ on $J$; applying the smooth
function $x\mapsto(2/x)^{1/3}$ proves the scale bound. The pole margin
follows from $t_{\max}\to v$ and $u_+\to u_0$. This proves (14).

For the covariance in (13), $\mu=O_p(N^{-1})$ and
$s_2=O_p(N^{-1})$. Hence

\[
 E_T-v(1+\sqrt{M/m})^2=O_p(N^{-1}),\qquad
 \gamma_T-\gamma_0=O_p(N^{-1}).                             \tag{16}
\]

## 5. Uniform design event and conditional universality

First $\|U\|_{\rm op}\leq C_U$ with probability tending to one for a
fixed constant. Represent the unit columns as $u_j=g_j/\|g_j\|$ with
independent standard Gaussian $g_j$. Markov's inequality applied to
$e^{-\|g_j\|^2/2}$ gives
$\mathbb P(\|g_j\|^2<d/2)\leq e^{-d[(\log2)/2-1/4]}$.
A union bound controls their minimum. For $G=(g_1,\ldots,g_N)$,
take $1/4$-nets of the two unit spheres, of sizes at most $9^d,9^N$.
Each net bilinear form is standard Gaussian. A tail bound and a union
bound give maximum absolute value at most $4\sqrt{d+N}$ except with
probability at most $2e^{-(8-\log9)(d+N)}$. Approximating both vectors
by the nets gives $\|G\|_{\rm op}\leq8\sqrt{d+N}$.
Thus $\|U\|_{\rm op}\leq\|G\|_{\rm op}/\min_j\|g_j\|=O(1)$.

Define the event

\[
 \mathcal G_N=\{\|U\|_{\rm op}\leq C_U,\quad
 \|B\|_{\rm op}\leq N^{-1/8},\quad
 \|R\|_F\leq N^{-1/8},\quad
 \operatorname{Tr}D^2\leq N^{1/6}\}.
\]

Equations (10)–(12) and Markov's inequality bound the last three
failure probabilities respectively by $O(N^{-1/2})$, $O(N^{-3/4})$,
and $O(N^{-1/6})$. Thus $\mathbb P(\mathcal G_N)\to1$.
Uniformly on this event, $\|T-vI\|_{\rm op}\to0$ and
$\|D\|_{\rm op}\leq C$ by (8). Equations (13)–(14) then imply

\[
 |\mu|\leq C/M,\quad s_2\leq N^{1/6}/M,
 \quad m^{2/3}|E_T-E_0|=O(N^{-1/6})\to0,
 \quad\gamma_T-\gamma_0\to0.                               \tag{17}
\]

In particular $T$ is uniformly positive, bounded, and has a uniform
right-edge pole margin. Section 2 proves uniform fixed-$p$ moment
bounds on this same event despite the unbounded derivative of $\sigma$.

Apply Corollary 1.4 of Guangchen Chen and Xing Lyu,
*Tracy–Widom law for sample covariance matrices under quadratic form
concentration*, [arXiv:2610.41416v2](https://arxiv.org/html/2610.41416v2),
conditionally on $U$, to

\[
 H_P=m^{-1}Q^TY^TYQ=m^{-1}\sum_{i=1}^m z_i z_i^T.
\]

Its assumptions are independent centered real vectors, common positive
covariance, dimension-uniform fixed-moment quadratic-form bounds,
aspect limit in $(0,\infty)\setminus\{1\}$, and a regular right
covariance edge. These have just been verified with dimension $M=N-1$
and sample count $m$. It gives

\[
 \gamma_Tm^{2/3}[\lambda_{\max}(H_P)-E_T]
       \Longrightarrow\mathrm{TW}_1.                      \tag{18}
\]

The corollary is an external input, not reproved here. It applies to
every deterministic sequence of designs in $\mathcal G_N$, with uniform
constants. The conditional convergence of distribution functions in
(18) is uniform on $\mathcal G_N$: otherwise a violating design could
be chosen on a subsequence, contradicting the corollary for that
deterministic sequence. The event is nonempty eventually because its
probability tends to one. The same argument gives uniform tightness.
Equation (17) therefore permits replacing $E_T,\gamma_T$ by
$E_0,\gamma_0$ uniformly in the conditional limit. Integrating over
$U$ and discarding an event of probability tending to zero yields

\[
 \gamma_0m^{2/3}[\lambda_{\max}(H_P)-v(1+\sqrt{M/m})^2]
       \Longrightarrow\mathrm{TW}_1.                      \tag{19}
\]

## 6. Normalization and scope

The nonzero eigenvalues of $(YQ)^T(YQ)$ and $(YQ)(YQ)^T=YPY^T$
coincide. Hence $\lambda_{\max}(H_P)=(N/m)\lambda_{\max}(K_P)$.
Writing $c_N=M/N=1-1/N$, (19) becomes

\[
 \widetilde g_N N^{2/3}
 [\lambda_{\max}(K_P)-\widetilde E_N]\Longrightarrow\mathrm{TW}_1,
\]
\[
 \widetilde E_N=v(\sqrt{b_N}+\sqrt{c_N})^2,\qquad
 \widetilde g_N=
 \frac{b_N^{1/6}c_N^{1/6}}{v(\sqrt{b_N}+\sqrt{c_N})^{4/3}}.
\]

These formulas follow by substituting $M/m=c_N/b_N$ in (19).
Since $c_N=1-1/N$ and $b_N$ stays in a positive compact interval,
$\widetilde E_N-v(1+\sqrt{b_N})^2=O(N^{-1})$ and the ratio of
$\widetilde g_N$ to the coefficient in (1) tends to one. The center
error is negligible after multiplication by $N^{2/3}$, proving (1).
Its tightness and $b_N\to b$ give the probability limit.

The theorem covers every fixed centered Hermite polynomial of degree
at least two, and their fixed finite sums with no degree-one term.
The constants in (4) grow with the degree; no growing-degree statement
is made. Occasional large entries at moderate dimensions are compatible
with the theorem's asymptotic conclusion. As a separate consistency
check, every entry has the fixed distribution $\sigma(Z)$, so for any
$p>12$, a union bound and Markov give

\[
 \mathbb P\!\left(\max_{i,j}|Y_{ij}|>N^{1/6}\right)
 \leq mN\,\mathbb E|\sigma(Z)|^pN^{-p/6}\longrightarrow0.
\]

Thus even the squared maximum entry divided by $N$ is
$o_p(N^{-2/3})$: the same estimate holds with the threshold multiplied by
any fixed positive constant. This observation alone proves no spectral
comparison.

For $K=YY^T/N$, the exact relation $K=K_P+aa^T$ with
$a=Ye/\sqrt N$ supplies interlacing, but no eigenvalue sticking at
the fluctuation scale. No conclusion for the largest eigenvalue below
an unprojected supercritical spike is asserted. Linear Hermite terms,
random column norms and $b=1$ remain outside (1). Replacing $b_N$ by
its limit in the center requires an additional convergence rate.
