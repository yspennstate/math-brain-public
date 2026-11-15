# A uniform weak bound from integrated residual curvature

## Result and scope

Consider the Euclidean, population-data gradient flow with fixed second-layer coefficients, as in Section 2 of Margalit Glasgow and Joan Bruna, *Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks*, [arXiv:2605.22010v3](https://arxiv.org/html/2605.22010v3). The flow uses half the gradient of the squared loss. The conclusions below concern the output norm, not a distance between parameter measures.

Write \(\mathcal H=L^2(P_X)\), \(g(x)=\mathbb E[Y\mid X=x]\), and \(\phi(w)(x)=\sigma(w^\top x)\). More generally, the proof applies to any twice continuously differentiable map \(\phi:\mathbb R^d\to\mathcal H\) satisfying

\[
 \sup_w\|\phi(w)\|\le A,\qquad
 \sup_w\|D\phi(w)\|_{\mathrm{op}}\le B,\qquad
 \sup_w\|D^2\phi(w)\|_{\mathrm{bil}}\le M.                 \tag{1}
\]

Here the last norm means \(\|D^2\phi(w)[u,v]\|\le M|u||v|\). Constants \(A,B,M\) are finite and nonnegative, and \(g\in\mathcal H\).

Let \(f_t=\int\phi(w)\rho_t(dw)\), \(r_t=f_t-g\), and \(L_t=\|r_t\|^2\). The mean-field characteristics satisfy

\[
 \dot v_t=-D\phi(v_t)^*r_t.
\]

The finite system is

\[
 f_t^m=\frac1m\sum_{i=1}^m\phi(w_i(t)),\qquad
 \dot w_i=-D\phi(w_i)^*(f_t^m-g).                         \tag{2}
\]

The initial \(w_i(0)\) are iid with law \(\rho_0\). Couple \(v_i(0)=w_i(0)\), with each \(v_i\) following the mean-field characteristic. Assume these flows exist globally. Under (1), bounded velocities and locally Lipschitz vector fields give the usual global characteristic construction; alternatively existence is already part of the source setting.

Define the nonnegative residual-curvature bound

\[
 h(t)=\sup_{w\in\mathbb R^d}\max\left\{0,
  \sup_{|u|=1}-\langle r_t,D^2\phi(w)[u,u]\rangle\right\},
 \qquad H(T)=\int_0^T h(t)\,dt.                           \tag{3}
\]

It obeys \(0\le h(t)\le M\sqrt{L_t}\). Suprema can be taken over countable dense sets, so \(h\) is measurable. Set

\[
 K=\big[2A^2+2A^2B^4+16A^4(1+B)^2\big]
       \exp\big(2M(1+B)\big).                            \tag{4}
\]

**Theorem.** For every deterministic \(T\ge1\),

\[
 \boxed{\quad
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le \frac{4K(1+T)^4e^{2H(T)}}m+6L_T.
 \quad}                                                 \tag{5}
\]

The expectation is over initialization. The supremum is outside the expectation.

Two consequences follow.

1. If \(L_t\le C(1+t)^{-c}\), \(0<c<2\), then for fixed \(A,B,M,C,c\),
   \[
    \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
      =O_{A,B,M,C,c}\big((\log m)^{-2c/(2-c)}\big).
                                                               \tag{6}
   \]
2. If, in addition to that loss decay, there are \(h_0,\kappa\ge0\) with
   \[
       H(T)\le h_0+\kappa\log(1+T)\qquad(T\ge1),          \tag{7}
   \]
   then, for \(m\ge2^{c+4+2\kappa}\),
   \[
    \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
    \le (4Ke^{2h_0}+6C)\,m^{-c/(c+4+2\kappa)}.           \tag{8}
   \]
   This is one sufficient stability hypothesis. It is not asserted to be necessary, and the exponent is not asserted to be sharp. This consequence also holds for any \(c>0\).

In particular, (6) is weaker than the polynomial rate asked for in T224. It establishes a quantitative uniform bound for a substantive subclass without asserting that the original question is settled.

## Proof of the theorem

### 1. The iid sampling error

Put

\[
 \bar f_t^m=\frac1m\sum_i\phi(v_i(t)),\qquad
 \zeta_t=\bar f_t^m-f_t,\qquad \eta_t=\|\zeta_t\|,
 \qquad Z_T=\int_0^T\eta_s\,ds.
\]

The mean-field characteristic map is deterministic. Therefore the \(v_i(t)\) are iid with law \(\rho_t\), for every fixed \(t\). Centering the Hilbert-valued random variables and expanding the squared norm gives

\[
 \mathbb E\eta_t^2
 =\frac1m\left(\mathbb E\|\phi(v_1(t))\|^2-\|f_t\|^2\right)
 \le\frac{A^2}{m}.                                      \tag{9}
\]

All off-diagonal terms vanish by independence and zero mean. Cauchy--Schwarz in time followed by Tonelli gives

\[
 \mathbb E Z_T^2
 \le T\int_0^T\mathbb E\eta_s^2\,ds
 \le\frac{A^2T^2}{m}.                                   \tag{10}
\]

Neither statement requires independence between different times.

### 2. The empirical-risk Hessian

Equip \((\mathbb R^d)^m\) with the normalized inner product

\[
 \langle U,V\rangle_m=\frac1m\sum_i u_i\cdot v_i,
 \qquad \|U\|_m^2=\frac1m\sum_i|u_i|^2.
\]

For \(U=(u_i)_i\), let \(f_U=m^{-1}\sum_i\phi(u_i)\) and
\(F(U)=\frac12\|f_U-g\|^2\). Its gradient in this inner product has components
\(G_i(U)=D\phi(u_i)^*(f_U-g)\). Direct differentiation gives, for any direction \(E=(e_i)_i\),

\[
 \begin{split}
 \langle E,DG(U)E\rangle_m
 &=\left\|\frac1m\sum_iD\phi(u_i)e_i\right\|^2\\
 &\quad+\frac1m\sum_i
       \langle f_U-g,D^2\phi(u_i)[e_i,e_i]\rangle.
 \end{split}                                             \tag{11}
\]

The first term is nonnegative. Let \(W=(w_i)_i\), \(V=(v_i)_i\), \(E=W-V\), and \(q=\|E\|_m\), all at time \(t\). Along \(U_\theta=V+\theta E\), \(0\le\theta\le1\), the Lipschitz bound in (1) implies

\[
 \|f_{U_\theta}-f_V\|
 \le\frac Bm\sum_i\theta|e_i|\le Bq.
\]

As \(f_V-g=r_t+\zeta_t\), it follows that

\[
 \|f_{U_\theta}-g-r_t\|\le\eta_t+Bq.
\]

The definition of \(h(t)\), the last bound in (1), and (11) now give

\[
 \langle E,DG(U_\theta)E\rangle_m
 \ge-\big[h(t)+M\eta_t+MBq\big]q^2.                     \tag{12}
\]

Integrating (12) in \(\theta\) yields

\[
 \langle E,G(W)-G(V)\rangle_m
 \ge-\big[h(t)+M\eta_t+MBq\big]q^2.                     \tag{13}
\]

### 3. Coupling and the stopping argument

The finite flow is \(\dot W=-G(W)\). The iid mean-field system obeys

\[
 \dot v_i=-G_i(V)+D\phi(v_i)^*\zeta_t.
\]

Subtract these identities and use (13). Since
\(\|(D\phi(v_i)^*\zeta_t)_i\|_m\le B\eta_t\),

\[
 \frac12\frac d{dt}q^2
 \le [h(t)+M\eta_t+MBq]q^2+B\eta_tq.
\]

Equivalently, where \(q>0\),

\[
 q'\le[h(t)+M\eta_t+MBq]q+B\eta_t.                       \tag{14}
\]

The norm is absolutely continuous; the same scalar comparison at its zeros follows by using \((q^2+\varepsilon^2)^{1/2}\) and letting \(\varepsilon\downarrow0\). Initially \(q(0)=0\).

Fix \(T\ge1\), and define

\[
 z_T=\frac{1}{2(1+B)T\exp(H(T)+M(1+B))},\qquad
 \mathcal G_T=\{Z_T\le z_T\}.                            \tag{15}
\]

Notice \(z_T\le1\). Up to a first time \(q\) reaches \(1/T\), (14) and the integrating-factor inequality imply, for \(s\le T\),

\[
 \begin{split}
 q(s)
 &\le B\int_0^s\eta_u
       \exp\left(\int_u^s[h(v)+M\eta_v+MB/T]dv\right)du\\
 &\le B Z_T\exp(H(T)+M Z_T+MB).
 \end{split}                                             \tag{16}
\]

On \(\mathcal G_T\), its right side is at most

\[
 Bz_Te^{H(T)+M+MB}=\frac{B}{2(1+B)T}<\frac1{2T}.           \tag{17}
\]

This contradicts a first hitting time of \(1/T\). Consequently (16) holds throughout \([0,T]\) on \(\mathcal G_T\), and in particular

\[
 q(s)\le B e^{H(T)+M(1+B)}Z_T\qquad(0\le s\le T).        \tag{18}
\]

### 4. Expectation up to the horizon

For each \(s\le T\),

\[
 \|f_s^m-f_s\|\le Bq(s)+\eta_s.
\]

On the event \(\mathcal G_T\), (18) gives

\[
 \mathbb E[\mathbf1_{\mathcal G_T}\|f_s^m-f_s\|^2]
 \le 2B^4e^{2H(T)+2M(1+B)}\mathbb E Z_T^2
       +2\mathbb E\eta_s^2.                              \tag{19}
\]

Both outputs have norm at most \(A\). Thus the complementary event contributes at most

\[
 \begin{split}
 4A^2\mathbb P(Z_T>z_T)
 &\le 4A^2\frac{\mathbb E Z_T^2}{z_T^2}\\
 &\le\frac{16A^4(1+B)^2T^4
                    e^{2H(T)+2M(1+B)}}m.                \tag{20}
 \end{split}
\]

Combine (9), (10), (19), and (20), and use \(T^2,T^4,1\le(1+T)^4\). The constant (4) then gives

\[
 \sup_{0\le s\le T}\mathbb E\|f_s^m-f_s\|^2
 \le D_T:=\frac{K(1+T)^4e^{2H(T)}}m.                     \tag{21}
\]

### 5. All later times

Write \(L_t^m=\|f_t^m-g\|^2\). Differentiation along (2) gives the exact dissipation identity

\[
 \frac d{dt}L_t^m
 =-\frac2m\sum_i|D\phi(w_i)^*(f_t^m-g)|^2\le0.           \tag{22}
\]

The mean-field loss also decreases, since

\[
 L_t'=-2\int|D\phi(w)^*r_t|^2\rho_t(dw)\le0.             \tag{23}
\]

For every \(t\ge T\), the squared triangle inequality gives

\[
 \begin{split}
 \mathbb E\|f_t^m-f_t\|^2
 &\le2\mathbb E L_t^m+2L_t\\
 &\le2\mathbb E L_T^m+2L_T\\
 &\le4\mathbb E\|f_T^m-f_T\|^2+6L_T\\
 &\le4D_T+6L_T.
 \end{split}                                             \tag{24}
\]

Together with (21), this proves (5).

## Consequences of the horizon bound

### Slow loss decay alone

Suppose \(0<c<2\), and put \(p=1-c/2\in(0,1)\). From (3),

\[
 H(T)\le M\sqrt C\int_0^T(1+s)^{-c/2}ds
 =\frac{M\sqrt C}{p}\big((1+T)^p-1\big).                 \tag{25}
\]

Let \(D=1+M\sqrt C/p\), and, for \(\log m\ge4D\,2^p\), choose

\[
 1+T=\left(\frac{\log m}{4D}\right)^{1/p}.
\]

Then \(T\ge1\), \(2H(T)\le\frac12\log m\), and (5) implies the explicit estimate

\[
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le4K m^{-1/2}\left(\frac{\log m}{4D}\right)^{4/p}
       +6C\left(\frac{\log m}{4D}\right)^{-c/p}.          \tag{26}
\]

The first term is of smaller order than the second logarithmic scale, since
\(m^{-1/2}(\log m)^{(4+c)/p}\to0\). Finally
\(c/p=2c/(2-c)\), proving (6). If \(C=0\), (26) still holds and its first term alone suffices for (6).

### An additional curvature condition

Under (7), (5) gives

\[
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le\frac{4Ke^{2h_0}(1+T)^{4+2\kappa}}m
       +6C(1+T)^{-c}.                                   \tag{27}
\]

Choose \(1+T=m^{1/(c+4+2\kappa)}\). For the stated lower bound on \(m\), this has \(T\ge1\). Both powers on the right of (27) become \(m^{-c/(c+4+2\kappa)}\), proving (8).

## Relation to the neural-network assumptions

For a bounded smooth activation with bounded first two derivatives, define

\[
 S_j=\|\sigma^{(j)}\|_\infty\quad(j=0,1,2),\qquad
 Q_j=\sup_{|u|=1}(\mathbb E|u^\top X|^j)^{1/j}
       \quad(j=2,4).
\]

Then (1) holds with

\[
 A=S_0,\qquad B=S_1Q_2,\qquad M=S_2Q_4^2.                 \tag{28}
\]

Indeed, \(D\phi(w)[u]=\sigma'(w^\top X)u^\top X\), while
\(D^2\phi(w)[u,v]=\sigma''(w^\top X)(u^\top X)(v^\top X)\).
Cauchy--Schwarz bounds the second derivative norm by
\(S_2(\mathbb E|u^\top X|^4\mathbb E|v^\top X|^4)^{1/4}\).
Under a dimension-uniform directional subgaussian bound on \(X\), \(Q_2,Q_4\) are bounded independently of \(d\). Thus all constants above are dimension independent when the activation and loss-decay constants are. The source's Euclidean bounded-total-variation assumptions on \(\sigma,\sigma',\sigma''\), together with their values at zero, imply finite \(S_0,S_1,S_2\). Requiring the source's remaining smoothness assumptions gives an admissible subclass. The population-data relaxation allowing unbounded \(\sigma\) is not included here.

The positive term in (11) is essential. Replacing it by an absolute-value bound produces an amplification exponential in \(T\), losing the improvement from \(\log m\) to \((\log m)^{1/p}\) in the horizon.

## What is not established

No lower bound or counterexample is proved. In particular, failure to bound \(H(T)\) logarithmically from the loss envelope does not prove that a polynomial weak rate is false. Cancellation specific to outputs could yield a stronger conclusion. The result does not cover unbounded activations, sphere-constrained dynamics, trainable second-layer coefficients, empirical-data error, or time discretization. The polynomial exponent in (8) depends on \(\kappa\), not only on \(c\).

The endpoint \(c=2\) is already treated in Remark 6 of Glasgow and Bruna's source paper, by a finite-horizon modification. It is not a new result here. The unresolved part of T224 remains whether the slow loss envelope alone yields any polynomial weak rate for the full stated class, and what its sharp exponent is.
