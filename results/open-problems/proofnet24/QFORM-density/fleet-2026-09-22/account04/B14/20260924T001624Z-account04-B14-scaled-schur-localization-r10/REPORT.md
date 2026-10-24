SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B14, 2026-09-24T00:16:24Z.
attacking: scale-covariant Schur zero-tax localization from an actual invertible three-coordinate block, retaining arbitrary affine leakage, fragments and unbounded outside laws.

# account04/B14 — scale-covariant three-coordinate Schur localization

Run: `20260924T001624Z-account04-B14-scaled-schur-localization-r10`.
Full unrestricted QFORM status: `OPEN_NOT_PROVED`.

## Inputs

Required Claude package retained from
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The completed account01/B14 theorem actually used is
`QFORM-SCHUR-COMPLETE-SQUARE-ZERO-TAX-LOCALIZATION-v1` at
`yspennstate/math-open-problems@be9d93b288079c9261fea04074bac234974da89c`,
with checks at `d7796450572115ec054f1541b01d41db18a82711`.
The completed three-dimensional affine theorem used by that source is pinned there to account02/B14 at
`7a0ffb7d9c4c6074cc6e13375db70828740e1bd4`.

## Theorem

Let \(A\) be any real symmetric \(n\times n\) matrix. Suppose that some three original coordinates form an invertible principal block \(B\). Put
\[
\sigma=\min_{1\le j\le3}|\lambda_j(B)|>0.
\]
Then, for every vector \(X\) of independent real random variables with marginal densities bounded by one,
\[
\boxed{
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}
\le \frac{6\sqrt\pi}{\sigma}.
}
\tag{1}
\]
The estimate is uniform over dimension, the outside symmetric block, every outside coupling, all conditioning-generated affine terms, arbitrary fragmented or unbounded supports, and all moments and tails.

If \(\sigma\ge1\), then \(A\) itself automatically has at least three eigenvalues of absolute value at least one, so (1) is an actual full-target chamber.

## Proof

After permuting original coordinates only, write
\[
A=\begin{pmatrix}B&C\\ C^T&D\end{pmatrix},
\qquad X=(U,Y).
\]
Condition on the outside original coordinates \(Y=y\). The exact Schur identity is
\[
U^TBU+2U^TCy+y^TDy
=
(U+B^{-1}Cy)^TB(U+B^{-1}Cy)
+y^T(D-C^TB^{-1}C)y.
\tag{2}
\]
For fixed \(y\), the shift \(B^{-1}Cy\) is deterministic and coordinatewise. Thus the three coordinates of \(U+B^{-1}Cy\) remain independent and their marginal density caps remain at most one. No rotation, support assumption, or moment estimate occurs.

Scale \(B=\sigma\widetilde B\). All three eigenvalues of \(\widetilde B\) have modulus at least one. The completed three-dimensional affine theorem gives, uniformly for every deterministic affine term and scalar translation,
\[
\Pr\!\left\{
U^T\widetilde B U+\ell^TU+c\in J
\right\}
\le 6\sqrt\pi\,|J|.
\tag{3}
\]
Applying (3) to \(J=\sigma^{-1}(I-c_y)\), or equivalently scaling the output by \(\sigma\), yields on every fiber
\[
\Pr\{X^TAX\in I\mid Y=y\}
\le \frac{6\sqrt\pi}{\sigma}|I|.
\tag{4}
\]
Integrating (4) over \(y\) proves
\[
\Pr\{X^TAX\in I\}
\le \frac{6\sqrt\pi}{\sigma}|I|
\tag{5}
\]
for every interval \(I\), which is equivalent to (1).

### Fragment ledger

Let the outside law be any finite or countable sum of subprobability measures
\[
\mu_Y=\sum_r\nu_r,\qquad \nu_r(\mathbb R^{n-3})=m_r,\qquad \sum_r m_r=1.
\]
Without normalizing any fragment, (4) gives
\[
\int \Pr\{X^TAX\in I\mid Y=y\}\,d\nu_r(y)
\le m_r\frac{6\sqrt\pi}{\sigma}|I|.
\]
Tonelli therefore gives (5) with no fragment-count loss. Remote components, arbitrary translations and unbounded supports cost exactly zero.

## Actual principal-block spectral gate

If \(\sigma\ge1\), Cauchy interlacing transfers each positive threshold crossing of \(B\) to the top eigenvalues of \(A\), and each negative threshold crossing to the bottom eigenvalues of \(A\). Hence \(A\) has at least three eigenvalues of absolute value at least one.

This is an actual principal-block gate; it does not infer the target hypothesis from a low-rank component plus a cancelling diagonal.

## Concrete dense example

For
\[
B_*=
I_3-\frac23\mathbf1\mathbf1^T
=
\begin{pmatrix}
1/3&-2/3&-2/3\\
-2/3&1/3&-2/3\\
-2/3&-2/3&1/3
\end{pmatrix},
\]
one has \(B_*^2=I_3\), so \(\sigma=1\) and \(\operatorname{spec}(B_*)=\{1,1,-1\}\). Therefore every ambient extension
\[
A=\begin{pmatrix}B_*&C\\C^T&D\end{pmatrix}
\]
with completely arbitrary \(C,D\) satisfies
\[
\boxed{
\Pr\{X^TAX\in I\}\le6\sqrt\pi\,|I|,
\qquad
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}\le6\sqrt\pi<10.635.
}
\tag{6}
\]

## Regularity ledger and remaining gap

Equation (1) is an essential-height theorem. It does not by itself assert continuity of a chosen density representative. Continuity may be compiled separately only when a valid conditional-\(C_0\) domination theorem applies.

The unrestricted conjecture remains open because the global condition \(s_3(A)\ge1\) does not presently force an actual three-coordinate principal block with \(\sigma\) bounded below universally. Diffuse spectral directions may leave every physical triple nearly singular. The missing step is structural extraction, not translation control: once an invertible physical triple is found, arbitrary affine leakage, outside curvature, fragmentation, tails and support geometry are already paid with zero tax.
