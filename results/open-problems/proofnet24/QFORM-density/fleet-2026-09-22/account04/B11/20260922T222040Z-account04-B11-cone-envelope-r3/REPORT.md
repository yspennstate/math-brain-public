# B11 report: cone-Jacobian cancellation and a partition-stable indefinite branch

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B11, 2026-09-22T22:20:40Z.

attacking: cone-envelope formulation and disjoint-bank null-scalar smoothing.

## Status

**PROVED_SUPPORTING_THEOREM / PARTNER_RESULT_APPLIED / FULL TARGET OPEN.**

Execution status: **WITHOUT_VERIFIED_BRAIN**.

The new result below is a target-level conditional theorem for both genuinely indefinite signatures \((+,+,-)\) and \((+,-,-)\). It gives an \(O(|I|)\) interval estimate with an explicit constant whenever an original-coordinate partition exposes one independent null scalar direction and an independent two-dimensional projection bank. It allows arbitrary conditioned outside coordinates and their affine couplings. It does not prove that every matrix with three large eigenvalues has such a partition.

## 1. Exact cone coordinates: where the third direction removes the logarithm

Start with the spectral model
\[
q(u,v,w)=u^2+v^2-w^2.
\]
Write \(u=r\cos\theta,\ v=r\sin\theta\), and set
\[
a=r-w,\qquad b=r+w.
\]
Thus
\[
r=\frac{a+b}{2},\qquad w=\frac{b-a}{2},\qquad q=ab,
\]
with domain \(a+b\ge0\). Since
\[
du\,dv\,dw=r\,dr\,d\theta\,dw
=\frac{a+b}{4}\,da\,db\,d\theta,
\]
a density \(g\) in \((u,v,w)\)-space gives
\[
p_q(y)=\frac14\int_{a+b\ge0}(a+b)G(a,b)\delta(ab-y)\,da\,db,
\tag{1}
\]
where
\[
G(a,b)=\int_0^{2\pi}g\!\left(\frac{a+b}{2}\cos\theta,
\frac{a+b}{2}\sin\theta,\frac{b-a}{2}\right)d\theta.
\]

At \(y=0\), the two axes of \(ab=0\) give
\[
p_q(0)=\frac14\left(\int_0^\infty G(0,b)\,db+
\int_0^\infty G(a,0)\,da\right).
\tag{2}
\]
The rank-two hyperbolic coarea factor is \(1/|b|\) on \(a=0\) and \(1/|a|\) on \(b=0\). The third-dimensional radial Jacobian \((a+b)/4\) cancels it exactly. This is the geometric reason the local rank-two logarithm disappears.

Equation (2) also isolates what is still missing: it leaves a ray-trace integral. A mere cap on the three-dimensional projected density does not control that integral. A density may concentrate in a long thin cone tube, giving arbitrarily large cone trace. Product provenance must therefore control the ray envelope, not merely the ambient projected density.

## 2. Quantitative null-scalar smoothing theorem

The following theorem is the completed account01/B11 result, written in a form used below.

### Theorem 2.1

Let \(Z\) be independent of \((V,W)\). Assume \(Z\) has density \(f\) with \(\|f\|_\infty\le L\), and \((V,W)\) has an arbitrary joint density \(g\) with \(\|g\|_\infty\le M\). Let \(\alpha\beta\ne0\). For arbitrary \(\gamma,\delta\) and arbitrary affine terms, set
\[
T=2\alpha ZW+\beta V^2+2\gamma VW+\delta W^2+\text{affine}.
\]
Then \(T\) has a density satisfying
\[
\boxed{\|p_T\|_\infty\le
3\,2^{2/3}(LM)^{2/3}|\alpha|^{-2/3}|\beta|^{-1/3}.}
\tag{3}
\]
Equivalently, for every interval \(I\),
\[
\Pr\{T\in I\}\le
3\,2^{2/3}(LM)^{2/3}|\alpha|^{-2/3}|\beta|^{-1/3}|I|.
\tag{4}
\]

### Proof, including the singularity balance

An affine term in \(Z\) changes \(2\alpha WZ\) to \(2\alpha(W-w_0)Z\). Translate \(W\) by \(w_0\); the joint density cap is unchanged. Hence it is enough to treat coefficient \(2\alpha W\).

Fix \(w\ne0\). Completing the square in \(V\), the \(V\)-part is a translate of \(\beta(V-c_w)^2\). The pushforward of the slice \(g(\cdot,w)\,dv\) under this square has density bounded by
\[
k_w(s)\le \frac{M}{\sqrt{|\beta|}}|s-s_w|^{-1/2}
\]
on one side of \(s_w\). Meanwhile \(2\alpha wZ\) has a probability density bounded by
\[
a_w=\frac{L}{2|\alpha w|}.
\]
For any probability density \(h\le a\), the bathtub bound against the decreasing half-kernel gives
\[
\int_0^\infty h(x_0-s)s^{-1/2}\,ds
\le a\int_0^{1/a}s^{-1/2}\,ds=2\sqrt a.
\]
Therefore the contribution of the \(w\)-slice to the density of \(T\) is at most
\[
\frac{\sqrt2\,M\sqrt L}{\sqrt{|\alpha\beta w|}}.
\tag{5}
\]
This is the precise analytic form of the third-direction improvement: the rank-two \(1/|w|\) kernel has become \(|w|^{-1/2}\), which is locally integrable.

Split at \(|w|=r\). Integrating (5) over \(|w|\le r\) yields
\[
\sup_t p_T^{\rm near}(t)
\le\frac{4\sqrt2\,M\sqrt L}{\sqrt{|\alpha\beta|}}\sqrt r.
\tag{6}
\]
On \(|w|>r\), integrate first in \(Z\). Its linear coefficient gives
\[
\sup_t p_T^{\rm far}(t)\le\frac{L}{2|\alpha|r}.
\tag{7}
\]
Thus
\[
\|p_T\|_\infty\le Ar^{1/2}+Br^{-1},\qquad
A=\frac{4\sqrt2\,M\sqrt L}{\sqrt{|\alpha\beta|}},\quad
B=\frac{L}{2|\alpha|}.
\]
At the minimizer \(r^{3/2}=2B/A\), the right side is \(3\,2^{-2/3}A^{2/3}B^{1/3}\), which simplifies to (3). The interval estimate (4) follows by integrating the density. \(\square\)

The quadratic Hessian block is
\[
H=\begin{pmatrix}0&0&\alpha\\0&\beta&\gamma\\\alpha&\gamma&\delta\end{pmatrix},
\qquad \det H=-\alpha^2\beta.
\tag{8}
\]
Since \(H\) is invertible but \(e_1^THe_1=0\), it is indefinite. If \(\beta>0\), its signature is \((+,+,-)\); if \(\beta<0\), its signature is \((+,-,-)\). Hence (3) is equivalently
\[
\boxed{\|p_T\|_\infty\le
3\,2^{2/3}(LM)^{2/3}|\det H|^{-1/3},}
\tag{9}
\]
covering both signs.

## 3. New integration: stability under an outside coordinate bank

### Theorem 3.1 (partition-stable null-scalar branch)

Partition the original independent coordinates into three disjoint banks
\[
X=(Z,Y,U),
\]
so \(Z\), \(Y\), and \(U\) are mutually independent. Let
\[
V=v\cdot Y,\qquad W=w\cdot Y,
\]
where \(v,w\) are orthonormal coefficient vectors. Suppose that, for every fixed outside value \(U=u\), the quadratic form can be written
\[
Q(Z,Y,u)=2\alpha ZW+\beta V^2+2\gamma VW+\delta W^2
+\ell_u(Z,V,W)+c(u),
\tag{10}
\]
where \(\alpha\beta\ne0\), while \(\ell_u\) is affine and may depend arbitrarily on \(u\).

Then, for arbitrary cap-one product inputs and every interval \(I\),
\[
\boxed{\Pr\{Q(X)\in I\}\le
3(2e)^{2/3}|\alpha|^{-2/3}|\beta|^{-1/3}|I|.}
\tag{11}
\]
Numerically, \(3(2e)^{2/3}=9.275505197\ldots\). Equivalently,
\[
\boxed{\|p_Q\|_\infty\le9.276\,|\det H|^{-1/3}.}
\tag{12}
\]

### Proof

The scalar \(Z\) has density cap \(L=1\). By the standard two-dimensional product-projection theorem used in the completed account01/B11 result, the orthonormal projection \((V,W)\) has a joint density bounded by \(M\le e\). This pair remains independent of \(Z\).

Condition on \(U=u\). All couplings to the outside bank become the affine term \(\ell_u\) and scalar \(c(u)\); the coefficients \(\alpha,\beta,\gamma,\delta\) are unchanged. Theorem 2.1 therefore gives, uniformly in \(u\),
\[
\Pr\{Q(X)\in I\mid U=u\}\le
3\,2^{2/3}e^{2/3}|\alpha|^{-2/3}|\beta|^{-1/3}|I|.
\]
Average over \(U\). This proves (11), and (12) follows from (8). \(\square\)

This is a genuine target-level inequality: the inputs are arbitrary independent cap-one laws with unbounded and disconnected supports; no moments, log-concavity, Gaussianity, compactness, or diagonal-basis assumption is used. The outside bank may be arbitrarily large and its values arbitrary.

## 4. Opposite-sign rank two versus the third direction

For two independent cap-one variables, an opposite-sign rank-two form such as
\[
UV\qquad\text{or}\qquad S^2-T^2=(S-T)(S+T)
\]
has the familiar \(1/|u|\) coarea kernel and can have a logarithmically unbounded density at zero. Theorem 2.1 identifies the exact cure in the null-scalar chamber:

- the linear null direction contributes a far-field cost \(r^{-1}\);
- transverse quadratic curvature contributes a near-field cost \(r^{1/2}\), because it replaces \(1/|w|\) by \(|w|^{-1/2}\);
- optimizing those two scales yields the determinant-homogeneous exponent \(|\det H|^{-1/3}\).

This specifies the kernel exponent and the exact balance that yields linear small-ball scaling.

## 5. Scope and unresolved implication

The theorem does **not** solve the full conjecture. It requires a product-preserving partition that leaves one scalar original-coordinate bank independent of a complementary two-dimensional projection bank, with a nonzero null coupling \(\alpha\) and nonzero transverse curvature \(\beta\).

In a fully overlapping rotated frame, conditioning to expose the scalar can destroy the bounded joint-density certificate for the pair, and a bounded spectral projection density alone cannot control the cone trace. The first unpaid structural step is:

> **Near-unit null-overlap compiler.** Starting from a three-large-eigenvalue matrix whose heavy null row has leverage \(0<h<1\), produce either a disjoint partition of the form (10) with determinant payment aggregable at universal cost, or route to an already completed diffuse/ridge/two-pivot branch without replacing product independence by a conditional cap.

Arbitrary extra spectral directions are also not absorbed unless they become affine after conditioning as in (10), or an independent completed full-matrix branch applies.

## 6. Continuity

The argument above proves an essentially bounded density and the exact interval estimate (11). It does not itself prove continuity for arbitrary \(L^\infty\) inputs. Existing account04/B15 work gives a separate qualitative \(C_0\)-density theorem for each fixed nonzero target quadratic-form instance; when invoked, that supplies continuity but no universal modulus. The universal height bound remains open.

## Sources consumed

- Owner control revision **2026-09-22.15**, programme QFORM-DENSITY-3EIG-20260922.
- Live correction inbox blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.
- Completed partner: `yspennstate/math-open-problems@1515e474fa8110a0b704a6ff73a25fc554005017`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T211147Z/REPORT.md`.
- Prior cone-trace obstruction: `yspennstate/math-open-problems@44e7ab6750fbc3dccd77f1dd9e8bdba0bba2f0f5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T161514Z-b11-cone-trace-r1/REPORT.md`.
- Separate regularity source: `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.

No refuted pointwise oscillatory estimate, projection-only cone trace, conditional-cap-as-independence step, small-coefficient perturbation, or fixed-good-minor implication is used.
