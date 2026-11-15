# A linear-activation benchmark for simultaneous two-layer gradient descent

Let

\[
 f_{a,W}(x)=a^{\mathsf T}Wx,\qquad
 a\in\mathbb R^p,\quad W\in\mathbb R^{p\times d},\qquad
 \mathcal L(a,W)=\frac1{2n}\|XW^{\mathsf T}a-y\|^2.
\]

There are no biases and no ridge penalty. Both layers are updated simultaneously
by full-batch gradient descent with the same constant step size. This is the
linear activation special case; no assertion about nonlinear feature learning
is implicit in it.

## 1. Convergence of the factor gradient descent

**Proposition 1.** Suppose \(X\ne0\). Initialize \(W_0=0\) and \(a_0=q\),
where \(\|q\|=1\), for any \(p\ge1\). Write

\[
 A=X/\sqrt n,\quad b=y/\sqrt n,\quad
 h=\|A\|_{\mathrm{op}}^2,\quad
 s=\text{smallest positive singular value of }A,
\]
\[
 L_0=\tfrac12\|b\|^2,\quad B=2\|b\|/s,\quad
 M=\sqrt{1+4B^2},\quad G=\sqrt h\,\|b\|,\quad D=6hM+G.
\]

For any fixed

\[
 0<\eta\le\min\left\{\frac1{1+G},\frac1{1+D},
                         \frac1{1+8L_0}\right\},                 \tag{1}
\]

the factors converge, and their predictor converges to

\[
 \widehat\beta=\lim_{t\to\infty}W_t^{\mathsf T}a_t=X^+y.       \tag{2}
\]

Here \(X^+\) is the Moore--Penrose inverse. This conclusion is independent of
\(p\) and of the direction \(q\).

**Proof.** Put \(S=\operatorname{range}(X^{\mathsf T})\). The gradients, with
\(\beta=W^{\mathsf T}a\), are

\[
 g=A^{\mathsf T}(A\beta-b),\quad
 \nabla_a\mathcal L=Wg,\quad \nabla_W\mathcal L=ag^{\mathsf T}.
\]

Induction shows that \(a_t=c_tq\) and \(W_t=qw_t^{\mathsf T}\), with
\(c_0=1,w_0=0\), \(w_t\in S\), and

\[
 c_{t+1}=c_t-\eta\langle w_t,g_t\rangle,\qquad
 w_{t+1}=w_t-\eta c_tg_t,\qquad
 g_t=A^{\mathsf T}(Ac_tw_t-b).                                \tag{3}
\]

These are exactly gradient descent on
\(F(c,w)=\tfrac12\|Acw-b\|^2\). In particular no layer is frozen.

Set \(K=c^2-\|w\|^2\), \(T=c^2+\|w\|^2\), and \(\beta=cw\).
The identity

\[
 T^2=K^2+4\|\beta\|^2                                       \tag{4}
\]

will bound the factors. Suppose at the start of a step that
\(F\le L_0\) and \(1/2\le K\le1\). Since \(\beta\in S\),

\[
 s\|\beta\|\le\|A\beta\|
 \le\|A\beta-b\|+\|b\|\le2\|b\|.
\]

Thus \(\|\beta\|\le B\) and (4) gives \(T\le M\). Moreover,

\[
 \|g\|\le G,\qquad
 \|\nabla F\|^2=\langle w,g\rangle^2+c^2\|g\|^2
 \le T\|g\|^2\le MG^2.                                     \tag{5}
\]

Every point on the straight segment from \((c,w)\) to its gradient step has
Euclidean norm at most
\(\sqrt M+\eta\sqrt M G\le2\sqrt M\), by (1). On that segment, therefore,
\(T\le4M\) and \(\|cw\|\le T/2\le2M\).

To bound the Hessian there, let \(J=[w,\,cI_d]\) be the derivative of
\((c,w)\mapsto cw\). Then

\[
 \nabla^2F=J^{\mathsf T}A^{\mathsf T}AJ+
 \begin{pmatrix}0&g^{\mathsf T}\\g&0\end{pmatrix},\qquad
 \|J\|_{\mathrm{op}}^2\le T.
\]

The second matrix has operator norm \(\|g\|\), and on the segment

\[
 \|g\|\le \|A\|_{\mathrm{op}}
                  (\|A\|_{\mathrm{op}}\,2M+\|b\|)=2hM+G.
\]

Consequently \(\|\nabla^2F\|_{\mathrm{op}}\le6hM+G=D\) there. Taylor's
formula and \(\eta D\le1\) give the actual-step decrease

\[
 F_{t+1}\le F_t-\tfrac\eta2\|\nabla F_t\|^2.                 \tag{6}
\]

Direct expansion of (3), rather than a continuous-time conservation law, gives

\[
 K_{t+1}=K_t-\eta^2\big(c_t^2\|g_t\|^2
                          -\langle w_t,g_t\rangle^2\big).     \tag{7}
\]

When \(K_t\ge0\), the bracket is nonnegative, by Cauchy--Schwarz, and at
most \(\|\nabla F_t\|^2\). Starting from \(K_0=1,F_0=L_0\), equations
(6)--(7) give, for every finite string of such steps,

\[
 K_{t+1}\ge1-\eta^2\sum_{j=0}^t\|\nabla F_j\|^2
 \ge1-2\eta L_0>\tfrac34.                                  \tag{8}
\]

This proves the induction hypotheses for the next step: \(F_{t+1}\le L_0\)
and \(3/4<K_{t+1}\le1\). There is no assumption about an unverified future
iterate in the descent estimate. In particular the factors stay bounded and
\(c_t^2\ge3/4\).

Let \(\beta_*=X^+y\) and \(F_*\) be the least-squares minimum. Both
\(\beta_t=c_tw_t\) and \(\beta_*\) lie in \(S\). The normal equations yield

\[
 F_t-F_*=\tfrac12\|A(\beta_t-\beta_*)\|^2,\qquad
 g_t=A^{\mathsf T}A(\beta_t-\beta_*).
\]

On \(S\), the smallest eigenvalue of \(A^{\mathsf T}A\) is \(s^2\).
Hence \(\|g_t\|^2\ge2s^2(F_t-F_*)\). Combining this with
\(\|\nabla F_t\|^2\ge c_t^2\|g_t\|^2\) and (6), using the weaker lower
bound \(c_t^2\ge1/2\), gives

\[
 F_{t+1}-F_*\le(1-\eta s^2/2)(F_t-F_*).                    \tag{9}
\]

The multiplier is in \((0,1)\): indeed \(D\ge6hM\ge6s^2\).
Equation (9) and
\(\|\beta_t-\beta_*\|^2\le2(F_t-F_*)/s^2\) prove (2).
Also \(\|g_t\|^2\le2h(F_t-F_*)\). With (5) and \(T_t\le M\), this
implies \(\sum_t\eta\|\nabla F_t\|<\infty\); the factors themselves
are Cauchy and converge. If \(b=0\), all gradients vanish initially and the
same conclusion holds directly. ∎

If \(X=0\), all predictor gradients vanish; this exceptional deterministic
case is not needed for Gaussian designs.

## 2. An elementary inverse-Gram identity

**Lemma 2.** Let \(Z\) be an \(m\times r\) matrix of independent standard
normal entries, \(m\ge r\ge1\), and let \(z\sim N(0,I_r)\) independently.
Then

\[
 z^{\mathsf T}(Z^{\mathsf T}Z)^{-1}z
 \ \stackrel{d}=\ \frac{U_r}{V_{m-r+1}},                    \tag{10}
\]

where \(U_r\) and \(V_{m-r+1}\) are independent chi-square variables with
the indicated degrees of freedom.

**Proof.** Gaussian matrices have full column rank almost surely, since the
vanishing of any fixed square minor is a nonzero-polynomial zero set. Partition
\(Z=[z_1,Z_2]\). The Schur complement formula gives

\[
 [(Z^{\mathsf T}Z)^{-1}]_{11}
  =\{z_1^{\mathsf T}(I-P_{Z_2})z_1\}^{-1}.                  \tag{11}
\]

For \(r=1\), take \(P_{Z_2}=0\). Conditional on \(Z_2\), the projection
\(I-P_{Z_2}\) has rank \(m-r+1\), and \(z_1\) is an independent standard
Gaussian. Diagonalizing the projection proves that the denominator of (11)
has law \(\chi^2_{m-r+1}\).

Write \(z=Ru\). Its squared radius \(R^2\sim\chi^2_r\) is independent
of its uniform spherical direction \(u\) and of \(Z\). Right orthogonal
invariance of \(Z\) shows that
\(u^{\mathsf T}(Z^{\mathsf T}Z)^{-1}u\) has the law of (11).
It is independent of \(R^2\), since it is a function only of \((u,Z)\).
Multiplication by \(R^2\) proves (10). ∎

## 3. Exact prediction risk and its proportional limit

Let the entries of \(X\) be independent \(N(0,1)\), let

\[
 y=X\theta_d+\varepsilon,\qquad
 \varepsilon\sim N(0,\sigma^2 I_n),\qquad \sigma>0,
\]

independently of \(X\). The vector \(\theta_d\) is deterministic.
For an independent test covariate \(x\sim N(0,I_d)\), define excess prediction
risk conditional on the training data by

\[
 R_{n,d,p}=\mathbb E_x[(f_{a_\infty,W_\infty}(x)
                               -x^{\mathsf T}\theta_d)^2]
          =\|\widehat\beta-\theta_d\|^2.                    \tag{12}
\]

Risk against an independently noisy test label is \(R_{n,d,p}+\sigma^2\).
All statements below take the training limit first for each finite data set,
with any step satisfying (1).

**Proposition 3.** Put \(r=\min(n,d)\), \(\nu=|n-d|+1\),
\(P=X^+X\), and

\[
 B_X=\|(I-P)\theta_d\|^2,\qquad N_X=\|X^+\varepsilon\|^2.
\]

Then, exactly,

\[
 R_{n,d,p}=B_X+N_X,\qquad
 N_X\stackrel d=\sigma^2\frac{U_r}{V_\nu},                 \tag{13}
\]

with independent numerator and denominator in the displayed distributional
representation. No independence between \(B_X\) and \(N_X\) is asserted
or needed. If \(n\ge d\), then \(B_X=0\). If \(d>n\) and
\(\theta_d\ne0\), then

\[
 \frac{B_X}{\|\theta_d\|^2}
 \stackrel d=\frac{U_{d-n}}{U_{d-n}+\widetilde U_n},         \tag{14}
\]

where the two chi-square variables in (14) are independent.

Suppose \(n,d,p\to\infty\), \(p/n\to\rho\in(0,\infty)\),
\(d/n\to\gamma\in(0,\infty)\setminus\{1\}\), and
\(\|\theta_d\|^2\to\tau^2<\infty\). Then

\[
 R_{n,d,p}\xrightarrow{\mathbb P}
 \begin{cases}
 \displaystyle\sigma^2\frac{\gamma}{1-\gamma},&0<\gamma<1,\\[6pt]
 \displaystyle\tau^2(1-\gamma^{-1})+
                     \frac{\sigma^2}{\gamma-1},&\gamma>1.
 \end{cases}                                               \tag{15}
\]

The curve is independent of \(\rho\). With the same bounded-signal assumption,
at fixed integer gap \(|d-n|=k\ge0\), instead,

\[
 \frac{R_{n,d,p}}n\ \Rightarrow
                 \frac{\sigma^2}{V_{k+1}}.                 \tag{16}
\]

In particular, the normalized risk has a nondegenerate random limit at
\(d=n\), for every proportional width sequence. The unnormalized risk
diverges to infinity in probability there.

**Proof.** Proposition 1 gives
\(\widehat\beta=P\theta_d+X^+\varepsilon\). The two terms in
\(\widehat\beta-\theta_d=-(I-P)\theta_d+X^+\varepsilon\) are orthogonal:
the first is in \(\ker X\), the second in \(\operatorname{range}(X^{\mathsf T})\).
This proves the risk decomposition in (13).

For \(n\ge d\), conditional on \(X\),

\[
 X^+\varepsilon\sim
 N\big(0,\sigma^2(X^{\mathsf T}X)^{-1}\big).
\]

Thus its squared norm has the unconditional law of
\(\sigma^2 z^{\mathsf T}(X^{\mathsf T}X)^{-1}z\), with a fresh standard
normal \(z\in\mathbb R^d\) independent of \(X\). Lemma 2 with
\((m,r)=(n,d)\) proves (13). For \(d>n\), direct multiplication gives

\[
 \|X^+\varepsilon\|^2
 =\varepsilon^{\mathsf T}(XX^{\mathsf T})^{-1}\varepsilon.
\]

Apply Lemma 2 to \(Z=X^{\mathsf T}\), \((m,r)=(d,n)\), and
\(z=\varepsilon/\sigma\).

When \(d>n\), the Gaussian row space is an orthogonally invariant random
\(n\)-plane. Rotating a fixed vector into a uniform spherical vector shows
that its squared projection onto the complementary \((d-n)\)-plane has
the ratio law (14): generate a uniform spherical vector by dividing a
standard Gaussian vector by its length and split its coordinates into
blocks of sizes \(d-n\) and \(n\).

For \(U_j\sim\chi^2_j\), its mean is \(j\) and variance is \(2j\).
Chebyshev's inequality gives \(U_j/j\to1\) in probability as \(j\to\infty\).
If \(\gamma<1\), (13) therefore converges to
\(\sigma^2 d/(n-d)\to\sigma^2\gamma/(1-\gamma)\), and the bias is zero.
If \(\gamma>1\), the noise converges to
\(\sigma^2 n/(d-n)\to\sigma^2/(\gamma-1)\), while (14) converges to
\(1-1/\gamma\) whenever the signal is nonzero. Zero-signal subsequences
have zero bias; if \(\tau=0\), the bound \(B_X\le\|\theta_d\|^2\)
also gives the required limit directly. This proves (15), without any assumption about dependence
of the two summands.

For fixed gap \(k\), \(r/n\to1\), so \(U_r/n\to1\) in probability,
but the denominator in (13) keeps the fixed law \(\chi^2_{k+1}\).
It is positive almost surely. The bias is at most \(\|\theta_d\|^2=O(1)\),
and hence disappears upon division by \(n\). Slutsky's theorem proves (16).
The law on its right is nonconstant and gives probability zero to zero.
For any fixed \(C>0\) and \(\delta>0\), eventually \(C/n<\delta\), so

\[
 \limsup_n\mathbb P(R_{n,d,p}\le C)
 \le\limsup_n\mathbb P(R_{n,d,p}/n\le\delta)
 =\mathbb P(\sigma^2/V_{k+1}\le\delta).
\]

The equality holds since the limit has a continuous distribution. Letting
\(\delta\downarrow0\) proves divergence of the unnormalized risk. ∎

There is also a deterministic rate between the fixed-gap and fixed-ratio
regimes. If \(k_n=|d-n|\to\infty\) while \(k_n/n\to0\), and the signal
norm remains bounded, then

\[
 \frac{k_n}{n}R_{n,d,p}\xrightarrow{\mathbb P}\sigma^2.      \tag{19}
\]

Indeed, the scaled noise in (13) has distribution

\[
 \sigma^2\frac{U_r}{r}\frac{\nu}{V_\nu}
                  \frac rn\frac{k_n}{\nu},
\]

and all four factors after \(\sigma^2\) tend to one in probability. The
scaled bias is at most \(k_n\|\theta_d\|^2/n\to0\). Thus a diverging
dimension gap restores relative concentration, whereas a fixed gap does not.

## 4. Finite-sample mean and scope

For \(\nu>2\), direct integration of the chi-square density yields
\(\mathbb E[V_\nu^{-1}]=1/(\nu-2)\). Consequently

\[
 \mathbb ER_{n,d,p}=
 \begin{cases}
 \displaystyle\sigma^2\frac d{n-d-1},&n>d+1,\\[5pt]
 \displaystyle\|\theta_d\|^2\left(1-\frac nd\right)
                       +\sigma^2\frac n{d-n-1},&d>n+1.
 \end{cases}                                               \tag{17}
\]

For \(|n-d|\le1\), the mean risk is infinite when \(\sigma>0\), although
the risk is finite almost surely for each finite data set. For completeness,
if \(V_\nu\) has density
\(v^{\nu/2-1}e^{-v/2}/(2^{\nu/2}\Gamma(\nu/2))\), its inverse mean is
\(\Gamma(\nu/2-1)/(2\Gamma(\nu/2))=1/(\nu-2)\) when \(\nu>2\);
the integral diverges at zero otherwise. The bias mean in (17) follows
from \(\mathbb EP=(n/d)I_d\), by rotational invariance and trace.

This model interpolates arbitrary labels exactly when \(d\ge n\), almost
surely, regardless of positive width. With \(\sigma>0\) and \(d<n\), the
noise almost surely prevents exact fitting. Thus there is an input-dimension
interpolation singularity at \(d/n=1\), but no width singularity at \(p/n=1\)
for this initialization. Equation (15) may be regarded as an extended curve
with value \(+\infty\) at \(\gamma=1\); (16) says more about its fluctuations.

The initialization is singular and deliberately symmetric. For example,
\(q=(1,\ldots,1)/\sqrt p\) uses every hidden unit but keeps the factor
trajectory of rank one. Gaussian first-layer initialization generally does
not have this property. The step in (1) can shrink with the smallest singular
value as dimensions grow; no dimension-uniform training-time claim is made.
Neither nonlinear activations, generic initialization, positive ridge, nor
interchange of the training and dimension limits is covered.

## 5. Independent checks of the distribution and critical scale

Here is a second derivation of (10), without a Schur complement. Conditional on
\(Z\), let \(v\) have law \(N(0,(Z^{\mathsf T}Z)^{-1})\). Its squared norm
has the same law as the left side of (10). Integrating the conditional density
against the Gaussian density of \(Z\) gives

\[
 f(v)=C\int_{\mathbb R^{m\times r}}
 \det(Z^{\mathsf T}Z)^{1/2}
 \exp\{-\tfrac12\operatorname{tr}(Z^{\mathsf T}Z
                                    (I_r+vv^{\mathsf T}))\}\,dZ,
\]

where \(C\) is positive and independent of \(v\). Put
\(C_v=I_r+vv^{\mathsf T}\) and change variables
\(Y=ZC_v^{1/2}\). The determinant factor contributes
\(\det(C_v)^{-1/2}\) and the Jacobian, one factor for each row,
contributes \(\det(C_v)^{-m/2}\). Therefore

\[
 f(v)=C'\det(C_v)^{-(m+1)/2}
     =C'(1+\|v\|^2)^{-(m+1)/2}.
\]

The remaining Gaussian integral is a finite constant: the determinant factor
is bounded by a polynomial in the entries, and Gaussian polynomial moments
are finite. Radial integration with \(t=\|v\|^2\) now gives a density
proportional to

\[
 t^{r/2-1}(1+t)^{-(m+1)/2},\qquad t>0.                     \tag{18}
\]

Independently transforming two chi-square densities by
\((u,v)=(tv,v)\), with Jacobian \(v\), shows that the ratio
\(U_r/V_\nu\) has density proportional to
\(t^{r/2-1}(1+t)^{-(r+\nu)/2}\). Matching exponents with (18) gives
\(\nu=m-r+1\), confirming the denominator in (10) and (13).
The ratio's mean can also be obtained from (18), as

\[
 \frac{\mathrm B(r/2+1,\nu/2-1)}{\mathrm B(r/2,\nu/2)}
 =\frac r{\nu-2},\qquad \nu>2,
\]

which independently checks (17).

At the square boundary there is a third derivation. In pure noise, the
\(n\times(n+1)\) augmented matrix \([X,\varepsilon/\sigma]\) is Gaussian.
Its nullspace is a uniform random line, representable as the span of
\((G_1,\ldots,G_n,G_{n+1})\) with independent standard normal coordinates.
Since \(X\widehat\beta=\varepsilon\), that same line contains
\((\widehat\beta,-\sigma)\). Thus

\[
 \|\widehat\beta\|^2/\sigma^2
 \stackrel d=\frac{\sum_{j=1}^nG_j^2}{G_{n+1}^2},
\]

confirming (13) at \(d=n\) without inverse-Gram integration.

For \(T=1/V_1\), its cumulative distribution function and quantiles satisfy

\[
 \mathbb P(T\le t)=\mathbb P(|G|\ge t^{-1/2})
     =\operatorname{erfc}(1/\sqrt{2t}),\qquad
 t_q=\{\Phi^{-1}(1-q/2)\}^{-2}.
\]

These give, for \(q=0.1,0.5,0.9\), respectively,
\(0.369611509\), \(2.198109338\), and \(63.328117677\), rounded to nine
decimal places. They quantify the nonvanishing spread in (16); they are
not approximations to a finite mean.
