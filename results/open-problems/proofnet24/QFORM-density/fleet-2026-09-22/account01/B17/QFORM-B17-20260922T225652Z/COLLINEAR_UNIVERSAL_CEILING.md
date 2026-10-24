# Addendum — a near-sharp universal ceiling for every collinear leverage split

Run: `QFORM-B17-20260922T225652Z`

This combines the exact arbitrary-weight branch theorem with Ball's sinc-integral inequality. Full QFORM remains OPEN.

## Theorem

Under the notation of `GENERAL_WEIGHTS_ADDENDUM.md`, for every finite real vector `a=(a_i)` with `sum a_i^2=1`,

\[
C(a)=6\,\mathbf E\exp\!\left[-6\Big(\sum_i a_iU_i\Big)^2\right]
\]

satisfies the dimension-free bound

\[
\boxed{
C(a)\le 3\sqrt2\left(\frac\pi3\right)^{1/4}
=4.291838853339765\ldots .
}
\]

Thus **every finite collinear splitting of the minority-sign spectral direction, with arbitrary leverage shares and arbitrary cap-one heavy laws, has global Gaussian-completion peak below 4.292**. The known lower obstruction `3sqrt(2)=4.242640687...` is only about `1.16%` below this entire-branch ceiling.

## Proof

Let

\[
S=\sqrt{12}\sum_i a_iU_i,
\qquad U_i\stackrel{iid}{\sim}{\rm Unif}[-1/2,1/2].
\]

Then `C(a)=6 E exp(-S^2/2)`. Fourier inversion of the Gaussian gives

\[
\frac{C(a)}6
=\frac1{\sqrt{2\pi}}
\int_{\mathbb R}e^{-t^2/2}
\prod_i \operatorname{sinc}(\sqrt3a_it)\,dt.
\]

Taking absolute values and applying generalized Holder with exponent `2` for the Gaussian factor and exponents

\[
p_i=\frac2{a_i^2}
\]

for the sinc factors is admissible because

\[
\frac12+\sum_i\frac1{p_i}
=\frac12+\frac12\sum_i a_i^2=1.
\]

The Gaussian norm is

\[
\|e^{-t^2/2}\|_2=\pi^{1/4}.
\]

Ball's sinc-integral inequality states that, for every `p>=2`,

\[
\int_{\mathbb R}\left|\frac{\sin u}{u}\right|^pdu
\le \pi\sqrt{\frac2p}.
\]

Since `p_i=2/a_i^2>=2`, a change of variables gives

\[
\begin{aligned}
\|\operatorname{sinc}(\sqrt3a_it)\|_{p_i}^{p_i}
&=\frac1{\sqrt3|a_i|}
\int_{\mathbb R}|\operatorname{sinc}u|^{p_i}du\\
&\le \frac1{\sqrt3|a_i|}\pi\sqrt{\frac2{p_i}}
=\frac\pi{\sqrt3}.
\end{aligned}
\]

Therefore

\[
\prod_i\|\operatorname{sinc}(\sqrt3a_it)\|_{p_i}
\le
\prod_i\left(\frac\pi{\sqrt3}\right)^{a_i^2/2}
=\left(\frac\pi{\sqrt3}\right)^{1/2}.
\]

Consequently

\[
\frac{C(a)}6
\le
\frac{1}{\sqrt{2\pi}}\pi^{1/4}
\left(\frac\pi{\sqrt3}\right)^{1/2}
=rac{\pi^{1/4}}{\sqrt2\,3^{1/4}},
\]

which is exactly

\[
C(a)\le3\sqrt2(\pi/3)^{1/4}.
\]

## Reference for the analytic input

The sinc inequality is Ball's integral inequality from K. Ball, *Cube slicing in R^n*, Proc. Amer. Math. Soc. 97 (1986), and is commonly written

\[
\int_{-\infty}^{\infty}|\sin u/u|^pdu\le\pi\sqrt{2/p},\qquad p\ge2.
\]

## Scope

This theorem does not close the roughly `0.0492` absolute gap between the collinear ceiling and `3sqrt(2)`, and it does not address non-collinear heavy rows. It nevertheless gives a uniform analytic exclusion for the entire arbitrary-leverage collinear architecture, not merely the equal-weight sequence.
