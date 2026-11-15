# Concentration improves the conditional uniform output rate

## Setting and assertions

Let \(\mathcal H\) be a real separable Hilbert space, \(g\in\mathcal H\), and \(\phi:\mathbb R^d\to\mathcal H\) be \(C^2\), with

\[
 \sup_w\|\phi(w)\|\le A,\qquad
 \sup_w\|D\phi(w)\|_{\rm op}\le B,\qquad
 \|D^2\phi(w)[u,v]\|\le M|u||v|.                         \tag{1}
\]

The constants are finite and nonnegative. Consider the population flows

\[
 f_t=\int\phi(v)\rho_t(dv),\quad r_t=f_t-g,\quad
 \dot v=-D\phi(v)^*r_t,
\]
\[
 f_t^m=\frac1m\sum_{i=1}^m\phi(w_i(t)),\qquad
 \dot w_i=-D\phi(w_i)^*(f_t^m-g).                         \tag{2}
\]

The \(w_i(0)\) are iid with law \(\rho_0\). Both flows use the gradient of half the squared loss. Bounded residuals and (1) give bounded velocities and globally Lipschitz parameter vector fields on each bounded time interval; equivalently these may be the globally defined flows in the source setting. Set

\[
 L_t=\|r_t\|^2,\qquad
 h(t)=\sup_{w,\ |u|=1}
       [-\langle r_t,D^2\phi(w)[u,u]\rangle]_+,
 \quad H(t)=\int_0^t h(s)\,ds,
\]
\[
 S_T=\int_0^T e^{2H(s)}\,ds.                             \tag{3}
\]

The supremum in (3) is measurable by continuity and separability. In particular \(0\le h(t)\le M\sqrt{L_t}\), and \(S_T\le T e^{2H(T)}\).

**Theorem 1.** Suppose \(A M>0\), \(T\ge1\) is deterministic, and

\[
                 m\ge2M^2A^2 T S_T.                     \tag{4}
\]

Then

\[
\begin{split}
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le {}&\frac{8A^2+16A^2B^2 T e^{2H(T)}}m+6L_T\\
       &+16A^2\exp\!\left(-\frac{m}{4M^2A^2 T S_T}\right).
\end{split}                                               \tag{5}
\]

If \(A M=0\), (5) holds with the exponential term omitted and no condition (4). All suprema over time in this document are outside expectation.

Here are two consequences under the additional stability assumption

\[
 L_t\le C(1+t)^{-c},\qquad
 H(T)\le h_0+\kappa\log(1+T),\quad T\ge1,                \tag{6}
\]

where \(c>0\), \(h_0,\kappa\ge0\). In particular these cover \(0<c\le2\).

**Corollary 2.** Define

\[
 b=2+2\kappa,\quad q=b+(c-1)_+,\quad a=\frac c q,
 \quad Q=4M^2A^2e^{2h_0},\quad R=\max\{1,Q\},
\]
\[
 K=24A^2+16A^2B^2e^{2h_0}+6C.                            \tag{7}
\]

For every integer \(m\) satisfying \(m\ge2^q R\log(em)\),

\[
 \boxed{\displaystyle
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
       \le K\left(\frac{R\log(em)}m\right)^{c/q}.}        \tag{8}
\]

Thus the improved exponent, up to a logarithmic factor, is

\[
 a=\begin{cases}
      c/(2+2\kappa),&0<c\le1,\\
      c/(c+1+2\kappa),&c>1.
    \end{cases}                                          \tag{9}
\]

For any fixed \(a'<a\), (8) also implies a pure power bound \(O(m^{-a'})\). No sharpness is asserted, including for the logarithm at \(c=1\).

**Corollary 3.** If \(c>1\), put

\[
 q=c+1+2\kappa,\quad a=c/q,\quad
 \beta=(c-1)/q,\quad r=c/(c-1),
\]
\[
 K_>=8A^2+16A^2B^2e^{2h_0}+6C
                +16A^2(rQ/e)^r.                         \tag{10}
\]

For \(m\ge2^q\) and \(m^\beta\ge Q/2\),

\[
 \boxed{\displaystyle
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
                   \le K_>m^{-c/(c+1+2\kappa)}.}         \tag{11}
\]

The last summand in (10) is zero for \(Q=0\). For fixed \(c>1\) and dimension-independent \(\kappa\), the prefactor and width threshold in (11) are polynomial in \(d\) if \(A,B,M,C\) are polynomial in \(d\) and \(h_0=O(\log d)\). The corresponding statement for (8) includes its displayed logarithmic factor. Constants are not uniform as \(c\downarrow1\) in (11).

The preceding round's exponent was \(c/(c+2+2\kappa)\). Each exponent in (9) is strictly larger. At \(\kappa=0\), the examples \(c=1/2,1,3/2,2\) change respectively from \(1/5,1/3,3/7,1/2\) to \(1/4,1/2,3/5,2/3\), with the logarithmic factor in (8) removable by (11) for the last two cases.

## 1. The coupled energy inequality

Couple \(v_i(0)=w_i(0)\) and let the \(v_i(t)\) follow the deterministic mean-field vector field. At each fixed time these variables are iid with law \(\rho_t\). Define

\[
 \bar f_t^m=\frac1m\sum_i\phi(v_i(t)),\quad
 \zeta_t=\bar f_t^m-f_t,\quad\eta_t=\|\zeta_t\|,
\]
\[
 e_i=w_i-v_i,\quad y(t)=\frac1m\sum_i|e_i(t)|^2,
 \quad J_T=\int_0^T\eta_s^2\,ds.                         \tag{12}
\]

Independence and centering yield

\[
 \mathbb E\eta_t^2
 =\frac{\mathbb E\|\phi(v_1(t))\|^2-\|f_t\|^2}{m}
 \le\frac{A^2}{m},\qquad
 \mathbb E J_T\le\frac{A^2T}{m}.                         \tag{13}
\]

No independence between times is used in the second assertion, which follows by Tonelli.

Write \(\delta=f_t^m-f_t\) and \(\Delta=f_t^m-\bar f_t^m\). Subtracting velocities in (2) gives the identity

\[
 \frac12y'=-\frac1m\sum_i
  \langle r_t,(D\phi(w_i)-D\phi(v_i))e_i\rangle
       -\left\langle\frac1m\sum_iD\phi(w_i)e_i,\delta\right\rangle.
                                                               \tag{14}
\]

Integrating \(D^2\phi\) along each segment from \(v_i\) to \(w_i\) bounds the first term by \(h(t)y\). A second application of the fundamental theorem of calculus gives

\[
 R_t:=\frac1m\sum_iD\phi(w_i)e_i-\Delta
 =\frac1m\sum_i\int_0^1
  [D\phi(w_i)-D\phi(v_i+\theta e_i)]e_i\,d\theta,
\]
\[
                         \|R_t\|\le\frac M2y.           \tag{15}
\]

Since \(\Delta=\delta-\zeta_t\), completion of a square in (14) gives

\[
\begin{split}
 \frac12y'
 &\le h(t)y-\|\delta\|^2+\langle\zeta_t-R_t,\delta\rangle\\
 &\le h(t)y+\frac14\|\zeta_t-R_t\|^2\\
 &\le h(t)y+\frac12\eta_t^2+\frac{M^2}{8}y^2.
\end{split}
\]

In particular, with \(\alpha=M^2/4\),

\[
                y'\le2h(t)y+\eta_t^2+\alpha y^2,
                \qquad y(0)=0.                         \tag{16}
\]

For completeness, the required scalar comparison follows directly. Put \(z=e^{-2H}y\). Integrating (16), using \(H\ge0\), gives for \(t\le T\)

\[
 z(t)\le J_T+\alpha\int_0^t e^{2H(s)}z(s)^2\,ds.
\]

If \(J_T>0\), call the right side \(Z(t)\). Then \(z\le Z\), \(Z(0)=J_T\), and \(Z'\le\alpha e^{2H}Z^2\). Thus

\[
 \frac1{Z(t)}\ge\frac1{J_T}-\alpha\int_0^t e^{2H(s)}\,ds.
\]

It follows that on the event

\[
 \mathcal G_T=\{\alpha S_TJ_T\le1/2\},\qquad
 y(t)\le2e^{2H(T)}J_T\quad(0\le t\le T).                \tag{17}
\]

If \(J_T=0\), the same conclusion follows by replacing \(J_T\) in the comparison by \(J_T+\varepsilon\) and sending \(\varepsilon\) to zero. If \(M=0\), direct integration of (16) gives \(y(t)\le e^{2H(t)}J_T\) without an event restriction.

By (1), \(\|\Delta\|\le B\sqrt y\). Therefore, for each fixed \(t\le T\),

\[
 \mathbb E[\mathbf1_{\mathcal G_T}\|\delta_t\|^2]
 \le 2B^2\mathbb E[\mathbf1_{\mathcal G_T}y(t)]
                +2\mathbb E\eta_t^2
 \le\frac{4A^2B^2 T e^{2H(T)}+2A^2}{m}.                 \tag{18}
\]

This uses unconditional expectations in (13), so conditioning has not changed any iid claim.

## 2. Concentration on trajectory space

For a deterministic \(T\), let

\[
 \mathcal K_T=L^2([0,T];\mathcal H),\qquad
 X_i(s)=\phi(v_i(s)),\qquad \mu(s)=f_s.
\]

The \(X_i\) are iid \(\mathcal K_T\)-valued random variables. They satisfy \(\|X_i\|_{\mathcal K_T}\le A\sqrt T\), and their Bochner mean is \(\mu\). Define

\[
 F(X_1,\ldots,X_m)
  =\left\|\frac1m\sum_iX_i-\mu\right\|_{\mathcal K_T}
  =\sqrt{J_T}.
\]

Equations (13) and Jensen give \(\mathbb EF\le A\sqrt{T/m}\). Replacing a single coordinate \(X_i\) by \(X_i'\) changes \(F\) by at most

\[
                  c_i=\frac{2A\sqrt T}{m}.              \tag{19}
\]

Here is a proof of the scalar bounded-difference inequality used below. For any real random variable \(U\) of mean zero in an interval of length \(c\), put \(\psi(\lambda)=\log\mathbb E e^{\lambda U}\). Under exponential tilting, \(\psi''(\lambda)\) is the variance of a variable in the same interval. Its variance is at most \(c^2/4\), by bounding its squared distance from the interval midpoint. Since \(\psi(0)=\psi'(0)=0\), integration gives

\[
                 \mathbb E e^{\lambda U}
                         \le e^{\lambda^2c^2/8}.
\]

For a bounded function of independent coordinates with coordinate differences bounded by \(c_i\), the Doob martingale increments have conditional mean zero and conditional range of length at most \(c_i\). Indeed, with the previous coordinates fixed, the conditional expectation over all future coordinates changes by at most \(c_i\) when coordinate \(i\) changes. Applying the preceding exponential bound conditionally and iterating gives

\[
 \mathbb E e^{\lambda(F-\mathbb EF)}
       \le\exp\!\left(\frac{\lambda^2}{8}\sum_i c_i^2\right).
\]

Exponential Markov inequality and minimization at \(\lambda=4u/\sum_i c_i^2\) yield

\[
 \mathbb P(F-\mathbb EF\ge u)
          \le\exp\!\left(-\frac{2u^2}{\sum_i c_i^2}\right).
\]

Substituting (19) proves

\[
 \mathbb P\!\left(\sqrt{J_T}\ge A\sqrt{T/m}+u\right)
             \le\exp\!\left(-\frac{mu^2}{2A^2T}\right),
             \qquad u\ge0.                             \tag{20}
\]

Only different initial neurons are independent here. For example, trajectories constant in time are allowed.

Suppose now \(AM>0\). The complement of (17) has
\(F>(2\alpha S_T)^{-1/2}\). Using (20), or the trivial bound one if this threshold is below \(A\sqrt{T/m}\), gives

\[
 \mathbb P(\mathcal G_T^c)
 \le \exp\!\left[-\frac12
    \left(\sqrt{\frac{m}{2\alpha A^2 T S_T}}-1\right)_+^2\right].
                                                               \tag{21}
\]

Under (4), \(m\ge8\alpha A^2 T S_T\), so the square root in (21) is at least two. For \(x\ge2\), \((x-1)^2\ge x^2/4\). Hence

\[
 \mathbb P(\mathcal G_T^c)
 \le\exp\!\left(-\frac{m}{16\alpha A^2 T S_T}\right)
 =\exp\!\left(-\frac{m}{4M^2 A^2 T S_T}\right).          \tag{22}
\]

There is no estimate of a time supremum of \(\eta_t\) in this argument.

## 3. Output bound and all later times

Both outputs have norm at most \(A\). Combining this cap with (18) and (22) gives

\[
 \sup_{0\le t\le T}\mathbb E\|f_t^m-f_t\|^2
 \le D_T:=\frac{2A^2+4A^2B^2 T e^{2H(T)}}m
       +4A^2\exp\!\left(-\frac{m}{4M^2 A^2 T S_T}\right).
                                                               \tag{23}
\]

Let \(L_t^m=\|f_t^m-g\|^2\). Direct differentiation gives

\[
 (L_t^m)'=-\frac2m\sum_i|D\phi(w_i)^*(f_t^m-g)|^2\le0,
 \quad L_t'=-2\int|D\phi(v)^*r_t|^2\rho_t(dv)\le0.
                                                               \tag{24}
\]

For any deterministic \(t\ge T\), two squared triangle inequalities give

\[
\begin{split}
 \mathbb E\|f_t^m-f_t\|^2
 &\le2\mathbb E L_t^m+2L_t
 \le2\mathbb E L_T^m+2L_T\\
 &\le4\mathbb E\|f_T^m-f_T\|^2+6L_T
 \le4D_T+6L_T.
\end{split}                                               \tag{25}
\]

Together with (23), this proves (5). If \(M=0\), (17)--(18) hold for all initializations, so omit the bad-event terms. If \(A=0\), both outputs are identically zero. These observations prove the degenerate cases of Theorem 1.

## 4. Horizon choices and constants

Under (6), write \(u=1+T\). Then

\[
 T e^{2H(T)}\le e^{2h_0}u^{b-1},\qquad
 T S_T\le T^2e^{2H(T)}\le e^{2h_0}u^b.                 \tag{26}
\]

For Corollary 2 choose

\[
 \ell=\log(em),\qquad u=\left(\frac{m}{R\ell}\right)^{1/q}.
                                                               \tag{27}
\]

The width condition ensures \(u\ge2\), so \(T=u-1\ge1\). Since \(q\ge b\) and \(R\ell\ge Q\),

\[
 m=R\ell u^q\ge(Q/2)u^b\ge2M^2A^2 T S_T.
\]

Thus (4) holds. If \(Q>0\), (26) also gives

\[
 \frac{m}{4M^2A^2 T S_T}
 \ge\frac{m}{Qu^b}
 =\frac{R\ell}{Q}u^{q-b}\ge\ell.
\]

The exponential term in (5) is at most \(16A^2/(em)\). If \(Q=0\), this term is absent. Finally \(q\ge c\), \(m\ge u^q\), and \(b-1-q\le-c\) imply

\[
 \frac1m\le u^{-c},\qquad
 \frac{u^{b-1}}m=\frac{u^{b-1-q}}{R\ell}\le u^{-c}.
\]

Insert these bounds and \(L_T\le C u^{-c}\) into (5). The constant \(K\) in (7) is sufficient, proving (8).

For Corollary 3 let \(q=c+1+2\kappa\), and choose \(u=m^{1/q}\). Then \(u\ge2\) and

\[
 \frac m{u^b}=m^\beta\ge Q/2.
\]

Equations (26) again ensure (4). The nonexponential terms in (5) are at most

\[
 (8A^2+16A^2B^2 e^{2h_0}+6C)m^{-a},
\]

because \((b-1)/q-1=-c/q\) and \(a<1\). For \(Q>0\), the exponential term is at most \(16A^2e^{-m^\beta/Q}\). Differentiating \(x^r e^{-x}\) shows that its maximum on \(x\ge0\) is \((r/e)^r\), attained at \(x=r\). Therefore

\[
 e^{-m^\beta/Q}
       \le(rQ/e)^r m^{-\beta r}
       =(rQ/e)^r m^{-a},
\]

where \(\beta r=a\). This proves (10)--(11), also for \(Q=0\) by omission of the exponential term.

The strict comparison with the old exponent follows from \(q<c+2+2\kappa\): for \(c\le1\) the difference of denominators is \(c\); for \(c>1\) it is one. For fixed \(c,\kappa\), polynomial dimension dependence follows directly from (7), (10), and their width conditions. The logarithm in (8) costs no fixed positive decrease in the exponent: if \(\epsilon=a-a'>0\), then \((\log(em))^a m^{-\epsilon}\) is bounded for \(m\ge1\).

## Scope and the remaining question

For neural networks, \(\mathcal H=L^2(P_X)\) and \(\phi(w)(x)=\sigma(w^\top x)\). If \(S_j=\|\sigma^{(j)}\|_\infty\) and \(Q_j=\sup_{|u|=1}(\mathbb E|u^\top X|^j)^{1/j}\), then (1) holds with \(A=S_0\), \(B=S_1 Q_2\), \(M=S_2 Q_4^2\), by Cauchy--Schwarz on the product of the two directional derivatives in \(D^2\phi\). This is the same bounded-feature, fixed-output-coefficient, Euclidean population-flow scope as the preceding two reports. Sphere constraints, unbounded features, trained output coefficients, finite-data error, and time discretization are not treated.

Loss decay alone only bounds

\[
 H(T)\le M\sqrt C\int_0^T(1+t)^{-c/2}\,dt.
\]

For \(0<c<2\), this grows like \((1+T)^{1-c/2}\). In (5), both the good-event term and the concentration threshold still contain exponential amplification through \(H\). The new concentration estimate does not justify a polynomial horizon from this envelope. The preceding logarithmic uniform bound remains available; no polynomial bound from decay alone, necessity result for (6), or output-error counterexample is established here. At \(c=2\), (6) follows with \(h_0=0\), \(\kappa=M\sqrt C\); (11) then yields exponent \(2/(3+2M\sqrt C)\) in this subclass. Polynomial endpoint coverage is already in the source and is not a new settlement.

Margalit Glasgow and Joan Bruna, *Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks*, [arXiv:2605.22010v3](https://arxiv.org/html/2605.22010v3), Remark 6 and Section 6, respectively cover the endpoint and pose the slower-decay question. The background source is Song Mei, Andrea Montanari, and Phan-Minh Nguyen, *A Mean Field View of the Landscape of Two-Layers Neural Networks*, [arXiv:1804.06561](https://arxiv.org/abs/1804.06561). The new assertions are the concentration bound (5) and its consequences relative to the preceding reports. No literature-priority claim is made.
