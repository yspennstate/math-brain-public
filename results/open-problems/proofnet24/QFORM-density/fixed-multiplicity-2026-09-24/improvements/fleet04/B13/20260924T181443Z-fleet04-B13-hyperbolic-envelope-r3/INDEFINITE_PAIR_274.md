# Indefinite-pair branch below 274

Assume independent cap-one original coordinates, an indefinite principal
\(2\times2\) pivot of determinant \(-D\) with \(D\ge1/400\), arbitrary affine
terms, and a conditional critical value \(v\) whose quadratic matrix has norm
at least one. The hyperbolic coarea estimate is

\[
p_{Q\mid\mathcal G}(z)
\le D^{-1/2}\left(6+\log_+\frac{16\sqrt D}{|z-v|}\right).
\]

Use the square-root concentration estimate

\[
\Pr(|v-z|<\rho)\le\min\{1,19\sqrt\rho\}.
\]

For \(c=16\sqrt D\ge4/5\), layer cake gives directly

\[
\mathbb E\log_+\frac c{|z-v|}
\le\int_0^\infty\min\{1,19\sqrt c\,e^{-u/2}\}\,du
=2+2\log19+\log c.
\]

Consequently

\[
p_Q(z)\le D^{-1/2}
\left(8+2\log19+\log(16\sqrt D)\right).
\]

Writing \(x=\sqrt D\ge1/20\), the right side is decreasing in \(x\), hence

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le20\left(8+\log\frac{1444}{5}\right)
=273.31\ldots<274.
}
\]

This replaces the earlier separated-logarithm estimate \(<337\) for the same
branch. It preserves arbitrary rough cap-one coordinate laws, all affine
terms, all dimensions, and the remaining spectrum. It does not improve the
global \(375\) constant because the no-pivot branch remains larger.

Source audited: eeb752c8943536541b34b42b8bf48e924f4d3d2f,
blob 19fb119877426b640b2c0dae19ec2f78a399fe11,
SHA-256 bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3.
