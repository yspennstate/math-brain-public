# Rudelson--Vershynin sharp scalar transfer into the fixed-multiplicity determinant engine

Source manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
Primary source: Mark Rudelson and Roman Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492, Theorem 1.2.

## 1. Improved scalar Fourier-power inequality

Let `f` be a one-dimensional probability density with `0<=f<=1`. For every `p>=2`,

\[
\int_{\mathbb R}|\widehat f(t)|^p\,dt\le \frac{4\pi}{\sqrt p}.
\]

Proof. Put `m=floor(p/2)`, so `m>=p/4`. Since `|fhat|<=1`,

\[
\int|\widehat f|^p\le\int|\widehat f|^{2m}.
\]

Let `X_1,...,X_m,X'_1,...,X'_m` be independent with density `f` and set

\[
S=\sum_{j=1}^m(X_j-X'_j).
\]

Then `|fhat|^{2m}` is the characteristic function of `S`, is integrable by Plancherel and `|fhat|<=1`, and Fourier inversion gives

\[
\int|\widehat f|^{2m}=2\pi p_S(0).
\]

The normalized sum `S/sqrt(2m)` is a linear combination with coefficient square-sum one of `2m` independent cap-one variables. Rudelson--Vershynin Theorem 1.2 gives density cap `sqrt(2)`, so

\[
p_S(0)\le \frac{\sqrt2}{\sqrt{2m}}=m^{-1/2}.
\]

Thus the integral is at most `2*pi/sqrt(m)<=4*pi/sqrt(p)`.

## 2. Improved regularized determinant theorem

Repeat the manuscript's geometric Brascamp--Lieb graph-frame proof. At a graph weight `d_i in (0,1]`, apply the preceding estimate with `p=2/d_i`:

\[
\int|\widehat f_i(t)|^{2/d_i}dt\le 2\sqrt2\pi\sqrt{d_i}.
\]

After the graph-coordinate scaling, the factors `d_i^{d_i/2}` cancel exactly as in the manuscript. The coordinate-entropy factor from the complementary weights remains `e^{theta/2}`. Therefore the scalar-Fourier constants and entropy cost combine to

\[
(2\sqrt2\pi)^\theta e^{\theta/2}=(2\pi\sqrt{2e})^\theta.
\]

Choosing

\[
\alpha=(2\pi\sqrt{2e})^2=8\pi^2e
\]

cancels this factor. With the manuscript's `a=2t` and fourth-power decoupling,

\[
\boxed{
|\phi_Z(t)|\le
\det\left(I+\frac{t^2}{2\pi^2e}M^TM\right)^{-1/8}.}
\]

No hypothesis changes: the variables remain arbitrary independent rough cap-one physical coordinates, and `F(X_I),G(X_J)` remain arbitrary measurable same-bank phases.

## 3. Crossing-volume consequences

Let

\[
Z_k(M)=\sum_{|S|=|T|=k}\det(M_{S,T})^2.
\]

Cauchy--Binet yields

\[
|\phi_Z(t)|\le\min\left\{1,
\left(\frac{u_k}{|t|}\right)^{k/4}\right\},
\qquad u_k:=\pi\sqrt{2e}\,Z_k(M)^{-1/(2k)}.
\]

For `k=5`, direct Fourier inversion gives

\[
\boxed{\|p_Z\|_\infty\le 5\sqrt{2e}\,Z_5(M)^{-1/10}.}
\]

For `k=3`, the manuscript's Riesz representation gives

\[
\boxed{
\sup_a\mathbb E|Z-a|^{-1/2}
\le 12(e/2)^{1/4}Z_3(M)^{-1/12}.}
\]

At the manuscript random-cut value `Z_k^{-1/(2k)}<=160`, these become

\[
\|p_Z\|_\infty\le800\sqrt{2e}=1865.3151852776994\ldots
\]

and

\[
\sup_a\mathbb E|Z-a|^{-1/2}
\le12(e/2)^{1/4}\sqrt{160}=163.89185052344388\ldots .
\]

## 4. Scope

This is a quantitative strengthening of the fixed-multiplicity analytic engine, not a lower-multiplicity theorem. The unconditional threshold remains 17 in the present architecture because bounded-density inversion still requires crossing order five, and the worst volume-ratio seed `r=4` still needs `m>=4r+1=17` in the completion/diagonal-dominance step.

No claim of novelty is made; the new ingredient is a direct source-valid transfer of Rudelson--Vershynin's sharp scalar theorem into the manuscript's self-contained determinant calculation.
