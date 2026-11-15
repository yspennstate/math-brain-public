# Edge fluctuations after removing the constant input direction

Let the columns of $X\in\mathbb R^{d\times N}$ be independent and uniform
on the sphere of radius $\sqrt d$. Let $W\in\mathbb R^{m\times d}$ have
independent standard real Gaussian entries, independently of $X$. Assume

\[
 N/d\longrightarrow\alpha\in(0,\infty),\qquad
 b_N=m/N\longrightarrow b\in(0,\infty)\setminus\{1\}.
\]

Let $\sigma:\mathbb R\to\mathbb R$ be a fixed Lipschitz function, with
orthonormal Gaussian Hermite coefficients $a_k$, such that

\[
 a_0=a_1=0,\qquad v=\mathbb E\sigma(Z)^2>0,\qquad q=a_2^2.
\]

Put $Y_{ij}=\sigma(w_i^Tx_j/\sqrt d)$, $e=N^{-1/2}(1,\ldots,1)^T$,

\[
 P=I_N-ee^T,\qquad K_P=YPY^T/N.
\]

**Theorem.** Without any subcriticality condition on $q$,

\[
 \frac{b_N^{1/6}}{v(1+\sqrt{b_N})^{4/3}}N^{2/3}
 \left[\lambda_{\max}(K_P)-v(1+\sqrt{b_N})^2\right]
 \ \Longrightarrow\ \mathrm{TW}_1.                                      \tag{1}
\]

Consequently $\lambda_{\max}(K_P)\to v(1+\sqrt b)^2$ in probability.
In particular (1) also holds when $q\alpha\sqrt b\geq v$.

The external input is Corollary 1.4 of Guangchen Chen and Xing Lyu,
*Tracy–Widom law for sample covariance matrices under quadratic form
concentration*, [arXiv:2610.41416v2](https://arxiv.org/html/2610.41416v2).
For independent centered real vectors $z_i\in\mathbb R^M$, $1\leq i\leq m$,
with common positive covariance $T$, it gives the following conclusion.
Suppose $M/m$ has a positive limit different from one, $T$ is uniformly
bounded and uniformly positive, all deterministic symmetric quadratic
forms satisfy

\[
 \|z_i^TAz_i-\operatorname{Tr}(TA)\|_p\leq C_p\|A\|_F,
 \qquad p\geq2,
                                                                    \tag{2}
\]

with constants independent of dimension, and the right covariance edge is
uniformly regular. If $t_j$ are the eigenvalues of $T$, define

\[
 f(u)=-\frac1u+\frac1m\sum_{j=1}^M\frac{t_j}{1+t_ju},\quad
 f'(u_+)=0,\quad -1/t_{\max}<u_+<0,
\]
\[
 E_T=f(u_+),\qquad \gamma_T=(2/f''(u_+))^{1/3}.
\]

The regularity condition is a dimension-independent positive lower bound
on $1+t_{\max}u_+$. The cited corollary states

\[
 \gamma_Tm^{2/3}
 \left[\lambda_{\max}\left(m^{-1}\sum_i z_i z_i^T\right)-E_T\right]
 \Longrightarrow\mathrm{TW}_1.                                      \tag{3}
\]

The proof below verifies these hypotheses conditionally on $X$ and
controls $E_T$ at the required scale. The external corollary is used as
stated; its proof is not reproduced.

## 1. Conditional covariance

Write $u_j=x_j/\sqrt d$, $U=(u_1,\ldots,u_N)$, and
$\rho_{jk}=u_j^Tu_k$. Given $U$, the feature rows, viewed as column
vectors $p_i=\sigma(U^Tw_i)\in\mathbb R^N$, are independent and identically
distributed. Each preactivation coordinate is standard Gaussian, so
$\mathbb E[p_i\mid U]=0$.

With $h_k=\mathrm{He}_k/\sqrt{k!}$, the Gaussian generating function gives

\[
 \mathbb E[h_k(G)h_l(H)]=\mathbf1_{k=l}\rho^k
\]

when $G,H$ are standard Gaussian with correlation $\rho$. Indeed,
the joint expectation of their Hermite generating functions is
$\exp(\rho st)$, and equality of coefficients gives the identity.
Passing from partial sums of the Hermite expansion to $\sigma$ is valid
by Cauchy–Schwarz in the two Gaussian marginals. Thus the conditional
covariance $\Sigma=\mathbb E[p_ip_i^T\mid U]$ is

\[
 \Sigma_{jk}=\sum_{l\geq2}a_l^2\rho_{jk}^l,\qquad \Sigma_{jj}=v.
                                                                    \tag{4}
\]

Define zero-diagonal symmetric matrices $B,R$ by

\[
 B_{jk}=\rho_{jk}^2-1/d,\qquad
 R_{jk}=\sum_{l\geq3}a_l^2\rho_{jk}^l\quad(j\ne k).
\]

Then, exactly,

\[
 \Sigma=(v-q/d)I_N+(q/d)\mathbf1\mathbf1^T+qB+R.                       \tag{5}
\]

For two independent uniform unit vectors, their inner product has moments

\[
 \mathbb E\rho^{2s}=
 \frac{1\cdot3\cdots(2s-1)}{d(d+2)\cdots(d+2s-2)}.                    \tag{6}
\]

To obtain (6), write a standard Gaussian vector as its independent length
times its uniform direction. Divide the $2s$-th moment of its first
coordinate by the $2s$-th moment of its length. These moments are the
numerator and denominator displayed in (6).

Since $|R_{jk}|\leq v|\rho_{jk}|^3$,

\[
 \mathbb E\|R\|_F^2\leq
 \frac{15v^2N(N-1)}{d(d+2)(d+4)}=O(d^{-1}).                            \tag{7}
\]

Set $D=\Sigma-vI_N$. Equation (4) gives $\operatorname{Tr}D=0$ and
$|D_{jk}|\leq v\rho_{jk}^2$ for $j\ne k$, hence

\[
 \mathbb E\operatorname{Tr}D^2\leq
 \frac{3v^2N(N-1)}{d(d+2)}=O(1).                                     \tag{8}
\]

## 2. Operator bound for the quadratic remainder

For completeness, the fourth-trace estimate from round 4 is proved here.
Put

\[
 c=1-1/d,\quad \tau=\frac{2}{d(d+2)},\quad
 \mu_4=\frac{12(d-1)(5d^2-13d+12)}{d^4(d+2)(d+4)(d+6)}.
\]

For $d\geq2$,

\[
 \mathbb E\operatorname{Tr}B^4
  =(N)_2\mu_4+2(N)_3(c\tau)^2+(N)_4c\tau^3,                           \tag{9}
\]

where $(N)_k=N(N-1)\cdots(N-k+1)$.

To prove this, in the Hilbert space of traceless symmetric $d\times d$
matrices set $z(u)=uu^T-I_d/d$. Directly $\mathbb Ez=0$ and
$\|z\|_F^2=c$. The spherical fourth-coordinate identity

\[
 \mathbb Eu_a u_b u_c u_l
 =\frac{\delta_{ab}\delta_{cl}+\delta_{ac}\delta_{bl}
                    +\delta_{al}\delta_{bc}}{d(d+2)}
\]

follows from sign symmetry and rotational invariance; its constant is
fixed by summing $\mathbb E(\sum_a u_a^2)^2=1$. Contracting it against
two traceless symmetric matrices $A,C$ gives

\[
 \mathbb E\langle z,A\rangle\langle z,C\rangle
       =\tau\langle A,C\rangle.                                    \tag{10}
\]

Also $B_{jk}=\langle z(u_j),z(u_k)\rangle$ off the diagonal. In the
closed-walk expansion of $\operatorname{Tr}B^4$, adjacent vertices must
be different. Walks with two vertices alternate; there are $(N)_2$,
and each has expectation $\mu_4=\mathbb E(\rho^2-1/d)^4$. Expanding
this power with (6) gives

\[
 \mu_4=\frac{105}{d(d+2)(d+4)(d+6)}
 -\frac{60}{d^2(d+2)(d+4)}+\frac{18}{d^3(d+2)}-\frac3{d^4},
\]

which equals the expression above. With three vertices, either the first
and third or the second and fourth vertices coincide. The two disjoint
classes each contain $(N)_3$ walks. Conditional on the repeated vertex,
each adjacent squared inner product has expectation $c\tau$, by (10),
and the two remaining vertices are independent. This gives $(c\tau)^2$.
With four different vertices, integrate the first and third vertices
using (10). The result is $\tau^2$ times the squared inner product of
the two remaining vectors, whose expectation is $c\tau$. There are
$(N)_4$ such walks. This proves (9).

The bounds $\mu_4\leq60/d^4$, $c\leq1$, $\tau\leq2/d^2$ show

\[
 \mathbb E\operatorname{Tr}B^4
 \leq60N^2/d^4+8N^3/d^4+8N^4/d^6=O(d^{-1}).
\]

Because $B$ is symmetric, $\|B\|_{\rm op}^4\leq\operatorname{Tr}B^4$.
Markov's inequality therefore yields

\[
 \|B\|_{\rm op}=O_p(d^{-1/4})=o_p(1).                                \tag{11}
\]

## 3. Projection and the trace defect

Choose a deterministic $N\times M$ matrix $Q$, $M=N-1$, whose
columns are an orthonormal basis of $e^\perp$. Thus $Q^TQ=I_M$,
$QQ^T=P$, and $Q^T\mathbf1=0$. The projected feature vectors
$z_i=Q^Tp_i$ are conditionally independent and centered with covariance

\[
 T=Q^T\Sigma Q
   =(v-q/d)I_M+qQ^TBQ+Q^TRQ.                                        \tag{12}
\]

In particular, by (7), (11),

\[
 \|T-vI_M\|_{\rm op}
 \leq q/d+q\|B\|_{\rm op}+\|R\|_F=o_p(1).                            \tag{13}
\]

This removes the quadratic covariance spike for every value of $q$.
The ambient projected covariance $P\Sigma P$ has a zero eigenvalue;
the positive covariance $T$ on $e^\perp$, rather than that singular
ambient matrix, is used in (3).

Let $A=T-vI_M=Q^TDQ$. Cyclicity of trace and (8) give

\[
 \operatorname{Tr}A=\operatorname{Tr}(DP)=-e^TDe,\qquad
 \|A\|_F^2\leq\|D\|_F^2=\operatorname{Tr}D^2.                        \tag{14}
\]

The norm inequality follows twice from
$\|CL\|_F\leq\|C\|_F\|L\|_{\rm op}$ and the same inequality for left
multiplication. The exact decomposition (5) also gives

\[
 e^TDe=q(N-1)/d+qe^TBe+e^TRe=q(N-1)/d+o_p(1).                        \tag{15}
\]

In particular the trace defect is bounded in probability, although it
does not generally vanish. If $t_1,\ldots,t_M$ are the eigenvalues of
$T$, equations (8), (14), (15) imply

\[
 \mu:=M^{-1}\sum_j(t_j-v)=O_p(N^{-1}),\qquad
 s_2:=M^{-1}\sum_j(t_j-v)^2=O_p(N^{-1}).                              \tag{16}
\]

Only the bounded trace defect is needed; replacing it by zero would be
incorrect when $q>0$.

## 4. A covariance-edge estimate with nonzero trace defect

Here $r=M/m$ stays in a compact subset of $(0,\infty)$. Suppose
$\epsilon=\max_j|t_j-v|$ is sufficiently small and define
$f,E_T,\gamma_T$ as above. Put

\[
 u_0=-\frac1{v(1+\sqrt r)},\quad
 E_0=v(1+\sqrt r)^2,\quad
 \gamma_0=\frac{r^{1/6}}{v(1+\sqrt r)^{4/3}}.
\]

Uniformly over these data,

\[
 |u_+-u_0|+|E_T-E_0|+|\gamma_T-\gamma_0|
       \leq C(|\mu|+s_2),\qquad 1+t_{\max}u_+\geq c_0>0.              \tag{17}
\]

To prove this, let $f_0(u)=-1/u+rv/(1+vu)$. Direct differentiation
gives

\[
 f_0'(u_0)=0,\quad
 f_0''(u_0)=\frac{2v^3(1+\sqrt r)^4}{\sqrt r}>0,\quad
 1+vu_0=\frac{\sqrt r}{1+\sqrt r}>0.
\]

There is a fixed-radius interval $J$ about $u_0$, uniform in $r$,
on which $u<0$, all $1+tu$ for $|t-v|\leq\epsilon$ are bounded
below by a positive constant, $f_0''$ has a positive lower bound, and
the endpoint signs of $f_0'$ are opposite. For $\delta=t-v$,

\[
 \frac{t}{1+tu}-\frac{v}{1+vu}
 =\frac{\delta}{(1+vu)^2}
   -\frac{u\delta^2}{(1+vu)^2(1+tu)}.                               \tag{18}
\]

This is checked by a common denominator. The last term and its first
two $u$-derivatives are bounded by $C\delta^2$ on $J$. Averaging
(18), and retaining the linear term $r\mu/(1+vu)^2$, proves

\[
 \sup_J|f^{(k)}-f_0^{(k)}|\leq C(|\mu|+s_2),\qquad k=0,1,2.            \tag{19}
\]

For small $\epsilon$, the right side is small, since
$|\mu|\leq\epsilon$ and $s_2\leq\epsilon^2$. The endpoint signs
therefore give a root of $f'$ in $J$, and $f''$ is positive there.
On the whole interval $(-1/t_{\max},0)$,

\[
 f''(u)=-2/u^3+(2/m)\sum_j t_j^3/(1+t_ju)^3>0.
\]

Also $f'\to-\infty$ at its left endpoint and $f'\to+\infty$ at
zero. Thus the root in $J$ is the unique $u_+$. The mean value
theorem, $f_0'(u_0)=0$, and (19) give the bound on $u_+-u_0$.
Evaluating $f$ at $u_+$ and using (19) gives the edge bound. Using
the bounded derivative $f_0'''$ on $J$ gives the bound on the second
derivative at $u_+$; the smooth function $x\mapsto(2/x)^{1/3}$ on a
fixed positive compact interval gives the scale bound. The pole margin
follows from $t_{\max}\to v$ and $u_+\to u_0$, uniformly. This proves
(17).

Equations (13), (16), (17) imply for the random conditional covariance

\[
 E_T-v(1+\sqrt{M/m})^2=O_p(N^{-1}),\qquad
 \gamma_T-\frac{(M/m)^{1/6}}{v(1+\sqrt{M/m})^{4/3}}=O_p(N^{-1}).        \tag{20}
\]

In particular $m^{2/3}(E_T-E_0)\to0$ in probability. The sign of the
edge defect is not asserted: the projected trace defect in (15) is
negative, while the second-order term in (18) is positive.

## 5. Uniform input norm and quadratic-form concentration

There is a fixed constant $C_U$ with
$\mathbb P(\|U\|_{\rm op}\leq C_U)\to1$. Here is an elementary proof.
Write $u_j=g_j/\|g_j\|$ with
independent standard Gaussian vectors and put $G=(g_1,\ldots,g_N)$.
Markov's inequality applied to $\exp(-\|g_j\|^2/2)$ gives

\[
 \mathbb P(\|g_j\|^2<d/2)
 \leq\exp\{-d[(\log2)/2-1/4]\}.
\]

A union bound controls the minimum column norm. Choose $1/4$-nets
of the unit spheres in dimensions $d,N$, of cardinalities at most
$9^d,9^N$. Each bilinear form of $G$ on one pair of net points
is standard Gaussian. A Gaussian tail bound and union bound show that
the maximum absolute bilinear form on the nets is at most
$4\sqrt{d+N}$, except with probability at most
$2\exp\{-(8-\log9)(d+N)\}$. Approximation of both unit vectors by
net points gives $\|G\|_{\rm op}\leq8\sqrt{d+N}$. Hence

\[
 \|U\|_{\rm op}\leq\|G\|_{\rm op}/\min_j\|g_j\|=O(1)
\]

with probability tending to one.

Fix a deterministic $U$ with this bound and with $T$ uniformly
bounded. The map $g\mapsto z(g)=Q^T\sigma(U^Tg)$ is $L$-Lipschitz,
where $L\leq\operatorname{Lip}(\sigma)C_U$. For a real symmetric $A$,
put $F(g)=z(g)^TAz(g)$. Its weak gradient satisfies

\[
 \|\nabla F\|\leq2L\|Az(g)\|.                                      \tag{21}
\]

For a locally Lipschitz Gaussian function $F$ of polynomial growth,

\[
 \|F-\mathbb EF\|_p\leq\frac\pi2\|Z\|_p
                      \|\,\|\nabla F\|\,\|_p.                       \tag{22}
\]

Indeed let $g'$ be an independent Gaussian and rotate
$g_\theta=g\cos\theta+g'\sin\theta$,
$h_\theta=-g\sin\theta+g'\cos\theta$. Conditional Jensen bounds
the left side by $\|F(g)-F(g')\|_p$. Integrate the derivative along
$0\leq\theta\leq\pi/2$ and apply Minkowski. For each $\theta$,
$g_\theta,h_\theta$ are independent standard Gaussians; integration
over $h_\theta$ supplies $\|Z\|_p$ times the $L^p$ norm of the
gradient length. Approximation by smooth functions extends the argument
to locally Lipschitz functions used here. Their moments are finite:
$z(g)$ has at most linear growth and $F(g)$ at most quadratic growth.

The function $h(g)=\|Az(g)\|$ is $L\|A\|_{\rm op}$-Lipschitz.
Equation (22) and Cauchy–Schwarz give

\[
 \|h\|_p\leq\mathbb Eh+C_pL\|A\|_{\rm op},\qquad
 \mathbb Eh\leq(\operatorname{Tr}(A^TA T))^{1/2}
                  \leq\sqrt{\|T\|_{\rm op}}\|A\|_F.
\]

Combining this with (21), (22), $\|A\|_{\rm op}\leq\|A\|_F$, and
$\mathbb EF=\operatorname{Tr}(TA)$ proves (2). Real and imaginary
parts give it for complex symmetric $A$ as well. All constants are
uniform over the indicated deterministic designs and dimensions.

## 6. Conditional theorem and deterministic centering

To make the conditioning argument uniform, restrict to the design event

\[
 \mathcal G_N=\{\|U\|_{\rm op}\leq C_U,\quad
 \|B\|_{\rm op}\leq N^{-1/8},\quad \|R\|_F\leq N^{-1/8},\quad
 \operatorname{Tr}D^2\leq N^{1/6}\}.                                \tag{23}
\]

Its probability tends to one. For the second condition, (9) and Markov
bound the failure probability by $O(N^{-1/2})$; for the third, (7)
gives $O(N^{-3/4})$; for the fourth, (8) gives $O(N^{-1/6})$.
The first condition was proved in Section 5. Here $N,d,m$ are
proportional, so the bounds can be expressed in $N$.

Uniformly on $\mathcal G_N$, (12) yields $\|T-vI_M\|_{\rm op}\to0$.
Equation (5) gives $\|D\|_{\rm op}\leq C$, so (14) gives

\[
 |\mu|\leq C/M,\qquad s_2\leq N^{1/6}/M=O(N^{-5/6}).
\]

The edge lemma therefore gives, uniformly,

\[
 m^{2/3}|E_T-E_0|=O(N^{-1/6})\to0,\qquad
 |\gamma_T-\gamma_0|\to0.                                           \tag{24}
\]

It also gives uniform positive covariance bounds and pole separation.
The aspect ratio $M/m\to1/b\ne1$, and Section 5 gives uniform
quadratic-form constants. Thus all hypotheses of (3) hold, conditional
on every deterministic sequence of designs in $\mathcal G_N$, for

\[
 H_P=Q^TY^TYQ/m=m^{-1}\sum_{i=1}^m z_i z_i^T.
\]

Convergence of the conditional distribution functions is uniform over
$\mathcal G_N$ at each fixed continuity point. Otherwise one could
choose a subsequence and one violating deterministic design at each
dimension, contradicting (3) for that deterministic sequence with its
uniform hypotheses. This also gives uniform tightness. Equation (24)
therefore permits replacing $E_T,\gamma_T$ by $E_0,\gamma_0$ in
the conditional limit. Integrating the conditional distributions and
using $\mathbb P(\mathcal G_N)\to1$ proves

\[
 \gamma_0m^{2/3}[\lambda_{\max}(H_P)-v(1+\sqrt{M/m})^2]
       \Longrightarrow\mathrm{TW}_1.                                \tag{25}
\]

Set $c_N=M/N=1-1/N$. Since $YQ(YQ)^T=YPY^T$, equality of the
nonzero singular-value squares gives
$\lambda_{\max}(H_P)=(N/m)\lambda_{\max}(K_P)$. Hence (25) is
equivalently

\[
 \widetilde g_NN^{2/3}
 [\lambda_{\max}(K_P)-\widetilde E_N]\Longrightarrow\mathrm{TW}_1,
\]
\[
 \widetilde E_N=v(\sqrt{b_N}+\sqrt{c_N})^2,\qquad
 \widetilde g_N=
 \frac{b_N^{1/6}c_N^{1/6}}{v(\sqrt{b_N}+\sqrt{c_N})^{4/3}}.            \tag{26}
\]

These identities follow by substituting $r=M/m=c_N/b_N$ in (25).
As $b_N$ stays in a positive compact interval and $c_N=1-1/N$,

\[
 \widetilde E_N-v(1+\sqrt{b_N})^2=O(N^{-1}),\qquad
 \frac{\widetilde g_N}{b_N^{1/6}/[v(1+\sqrt{b_N})^{4/3}]}
       =1+O(N^{-1}).
\]

The center difference is $o(N^{-2/3})$, so (26) implies (1).
Tightness of (1) and $b_N\to b$ give the asserted probability limit.

## 7. Scope and the unprojected matrix

For $K=YY^T/N$, let $a=Ye/\sqrt N$. The exact identity

\[
 K=K_P+aa^T
\]

and the variational principle imply

\[
 \lambda_1(K)\geq\lambda_1(K_P)\geq\lambda_2(K).
\]

This does not give a TW limit for $\lambda_2(K)$. A transfer at the
fluctuation scale would require an additional comparison, for example
$\lambda_1(K_P)-\lambda_2(K)=o_p(N^{-2/3})$ in a separated-outlier
regime. No such comparison is proved here. The theorem concerns the
explicit projected kernel, including all values of the quadratic
coefficient; it leaves linear Hermite components, random-norm inputs,
non-Lipschitz polynomial activations, and $b=1$ untreated. It uses
the exact finite-size aspect ratio in its deterministic centering;
replacing it by its limit requires an additional rate assumption.
