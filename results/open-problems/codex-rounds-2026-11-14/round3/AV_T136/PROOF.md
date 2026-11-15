# Bare-system exponential augmentation

This proves the bare-endpoint case of the augmentation argument in Section 4 of OpenAI, *The low-temperature Sherrington–Kirkpatrick free-energy limiting law* (September 24, 2026). It does not prove the hierarchical-path version, the stopped pressure-increment proposition, or a fluctuation theorem.

## Statement

Fix an integer \(n\ge2\), a real \(\beta\), and \(\tau\ge0\). Let all \(g_{ij}\) and \(z\) be independent standard Gaussians, and set
\[
 L_\sigma(g,z)=\frac{\beta}{\sqrt n}\sum_{i<j}g_{ij}\sigma_i\sigma_j+\tau z,
 \qquad
 F(g,z)=\log\left(2^{-n}\sum_{\sigma\in\{-1,1\}^n}e^{L_\sigma(g,z)}\right).
\]
For \(0<a\le1\), let \(E_a\) be independent exponential noise with rate \(a\). Then \(F+E_a\) has a log-concave Lebesgue density. The assertion also holds with the counting spin sum, which adds the constant \(n\log2\).

In particular it applies to the paper's completed free energy with \(\tau=\beta/\sqrt2\) for \(\beta>1\), and to the uncompleted free energy with \(\tau=0\). There is no restriction to low temperature in this supporting lemma.

Moreover, let
\[
 r_n=n^{-1/6},\qquad Y_n=r_n(F_n-\mathbb E F_n),
 \qquad V=\sup_{n\ge2}\operatorname{Var}(Y_n)<\infty.
\]
Here each \(F_n\) can be the completed free energy above, with fixed \(\beta,\tau\). Put
\[
 b=\frac{\log3}{8},\qquad D=\sqrt{V+4},\qquad t_0=\frac{b}{D}.
\]
Then
\[
 \sup_{n\ge2}\mathbb E e^{t_0|Y_n|}
 \le \frac32\,3^{1/4}.
 \tag{1}
\]
The assumption \(V<\infty\) is conditional: it is not established here for low-temperature SK.

## 1. An exact gauge identity

Write \(x=(g,z)\), let \(\phi(x)\) be its standard Gaussian density, and let \(\sigma^+=(1,\ldots,1)\). The function \(F\) is convex, since it is a log sum of exponentials of linear functions.

For each \(\eta\in\{-1,1\}^n\), transform \(g_{ij}\) into \(\eta_i\eta_jg_{ij}\), leaving \(z\) fixed. This orthogonal map \(T_\eta\) preserves \(\phi(x)\,dx\), and
\[
 L_\sigma(T_\eta x)=L_{\sigma\eta}(x),\qquad
 F(T_\eta x)=F(x).
\]
For any bounded measurable \(h:\mathbb R\to\mathbb R\), define
\[
 I_\sigma=\int h(F(x))e^{L_\sigma(x)-F(x)}\phi(x)\,dx .
\]
These integrals exist because \(e^{L_\sigma-F}\le2^n\). The change of variables \(x=T_\eta y\) shows \(I_\sigma=I_{\sigma\eta}\). Therefore all \(I_\sigma\) are equal. Averaging gives
\[
 I_{\sigma^+}
 =\int h(F(x))\left(2^{-n}\sum_\sigma e^{L_\sigma(x)-F(x)}\right)\phi(x)\,dx
 =\mathbb E h(F).
 \tag{2}
\]
In particular \(p_+(x)=\phi(x)e^{L_{\sigma^+}(x)-F(x)}\) integrates to one, and the law of \(F(x)\) under this density is its original law.

There is also a probabilistic way to check the normalization. Sample \(x\) from its Gaussian law and then \(\sigma\) with Gibbs probability \(e^{L_\sigma(x)}/(2^n e^{F(x)})\). Gauge invariance makes the marginal spin uniform. Conditioning on \(\sigma=\sigma^+\), whose probability is \(2^{-n}\), gives exactly \(p_+\).

## 2. The augmented density

Sample \(x\) from \(p_+\), independently sample \(E_a\), and put \(u=F(x)+E_a\). The joint density of \((x,u)\) is
\[
 q(x,u)
 =a\phi(x)\exp\{L_{\sigma^+}(x)-(1-a)F(x)-au\}
   {\bf1}_{\{u\ge F(x)\}}.
 \tag{3}
\]
It integrates to one: integrating in \(u\) first gives \(p_+(x)\).

The support in (3) is the epigraph of the convex function \(F\), hence convex. On that support its logarithm, up to a constant, is
\[
 -\frac{|x|^2}{2}+L_{\sigma^+}(x)-(1-a)F(x)-au .
\]
This is concave because \(1-a\ge0\). Extending the density by zero preserves log-concavity. The log-concave marginal theorem (Prékopa's theorem) therefore makes \(\int q(x,u)\,dx\) a log-concave density in \(u\). All its hypotheses hold: \(q\) is measurable, nonnegative, integrable, and log-concave on the finite-dimensional Euclidean product space.

By (2), \(F\) under \(p_+\) has its original distribution. Independence of \(E_a\) then identifies this marginal as the original law of \(F+E_a\). This proves the assertion.

The completion has a second independent check. For \(\tau=0\) the argument proves log-concavity of the augmented uncompleted law. Adding independent \(\tau z\) convolves this law with a Gaussian, which preserves log-concavity by the same marginal theorem. Deterministic shifts also preserve it.

## 3. An explicit tail bound for a centered log-concave density

Let \(W\) have a log-concave density, mean zero, and variance \(d^2\in(0,\infty)\). Its survival function \(S(t)=\mathbb P(W\ge t)\) is log-concave: apply the same marginal theorem to the joint log-concave function \(f(w){\bf1}_{\{w\ge t\}}\), integrating in \(w\). The left survival function is handled by replacing \(W\) with \(-W\).

Chebyshev gives
\[
 S(2d)\le\frac14,\qquad S(-2d)\ge\frac34.
\]
For \(t\ge2d\), concavity of \(\log S\) implies
\[
 \log S(t)-\log S(2d)
 \le\frac{t-2d}{4d}\bigl(\log S(2d)-\log S(-2d)\bigr)
 \le-\frac{\log3}{4d}(t-2d).
\]
If \(S(2d)=0\), the resulting upper bound holds trivially. Thus, with \(A=(\log3)/4\),
\[
 \mathbb P(|W|\ge ud)\le\frac12e^{-A(u-2)}
 \qquad(u\ge2).
 \tag{4}
\]
There are no atoms, so endpoint conventions do not affect these estimates.

For \(b=A/2\), the layer-cake formula and (4) yield
\[
\begin{aligned}
 \mathbb E e^{b|W|/d}
 &=1+b\int_0^\infty e^{bu}\mathbb P(|W|/d>u)\,du\\
 &\le e^{2b}+\frac b2\int_2^\infty e^{bu-A(u-2)}\,du\\
 &=e^{2b}\left(1+\frac{b}{2(A-b)}\right)
 =\frac32e^{2b}=\frac32\,3^{1/4}.
\end{aligned}
 \tag{5}
\]

## 4. Application at the \(n^{1/6}\) scale

Take independent \(E_n\) of rate \(a_n=r_n/2\). Since \(0<a_n<1\), the first part applies. Define
\[
 W_n=Y_n+r_n(E_n-\mathbb E E_n).
\]
It is a centered affine image of \(F_n+E_n\), so it has a log-concave density. Direct computation gives
\[
 \mathbb E E_n=2/r_n,\qquad
 \operatorname{Var}(E_n)=4/r_n^2,\qquad
 d_n^2:=\operatorname{Var}(W_n)=\operatorname{Var}(Y_n)+4\le D^2.
 \tag{6}
\]
Equivalently, \(r_nE_n\) has exponential rate \(1/2\), giving the same variance four without using the variance formula in (6).

Apply (5) with \(d=d_n\). Since \(t_0=b/D\le b/d_n\), it gives \(\mathbb E e^{t_0|W_n|}\le(3/2)3^{1/4}\). Finally the centered independent noise has conditional mean zero given \(Y_n\). Convexity of \(y\mapsto e^{t_0|y|}\) and conditional Jensen give
\[
 e^{t_0|Y_n|}
 \le\mathbb E\left[e^{t_0|W_n|}\mid Y_n\right].
\]
Taking expectations proves (1).

## 5. Boundary checks and scope

The proof includes \(a=1\), when the coefficient of \(F\) in the log density vanishes. It does not include \(a=0\), which is not an exponential probability distribution, or assert the claim for \(a>1\), when the concavity argument changes sign. The zero-field symmetry and uniform spin prior are used explicitly in (2).

The unaugmented free energy need not have a log-concave density. At \(n=2\), without completion, its random part is \(U=\log\cosh(cg)\), \(c=|\beta|/\sqrt2>0\). A change of variables from the two Gaussian preimages gives, for \(u>0\),
\[
 f_U(u)=\frac{\sqrt{2/\pi}}c
 \exp\left(-\frac{\operatorname{arcosh}(e^u)^2}{2c^2}\right)
 \frac{e^u}{\sqrt{e^{2u}-1}} .
\]
Near zero, \(\log f_U(u)=\text{constant}-\frac12\log u+O(u)\), with an analytic remainder. Its second derivative is \(1/(2u^2)+O(1)>0\) for sufficiently small \(u\). Thus the augmentation cannot be silently omitted.

The gauge argument above treats a bare Gaussian model. It does not establish the source's corresponding identity for all continuations under hierarchical transition kernels. Nor does it prove the stopped increment, boundedness of \(\operatorname{Var}(Y_n)\), the claimed limiting law, or a zero-temperature fluctuation result.
