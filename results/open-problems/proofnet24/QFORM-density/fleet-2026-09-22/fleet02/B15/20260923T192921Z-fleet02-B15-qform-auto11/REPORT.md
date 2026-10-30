# fleet02/B15 — convex-contamination barrier for rough-source closure

Status: **FULL QFORM OPEN**.  This report does not assert a counterexample to the quadratic-form conjecture.  Its new contribution is a source-valid obstruction to extending the completed inverse-scale Gaussian-mixture theorem to arbitrary cap-one inputs by convexification, randomized mixture, or a fixed positive certified component plus an uncontrolled residual.  Continuity is kept separate from essential boundedness throughout.

## 0. First unpaid implication

The global unpaid statement is still

\[
\sup_{\substack{n\ge3,\ s_3(A)\ge1\\ X_i\ {m independent},\ 0\le f_i\le1}}
\|p_{X^\top A X}\|_\infty<\infty.
\]

At the present structural frontier, the already completed strong-physical-triple receiver and third-cross-volume receiver pay large subclasses.  The unresolved regime is the one with neither a uniformly conditioned physical principal triple nor a universally large usable third cross-volume; there the remaining receiver must exploit original-coordinate product provenance under overlapping leakage / approximate-hub geometry.  The new result below says that one cannot bridge this residual regime merely by writing rough sources as a nontrivial convex amount of the completed inverse-scale-certified Gaussian source class plus arbitrary contamination.

## 1. Source pins actually used


Required owner-pinned mathematical source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.  Its completed Theorem C is used below in a rough-law majority-side tent inequality.

Latest compatible designated-partner result actually used: fleet03/B15 handoff `20260923T182510Z-fleet03-B15-qform-auto25.md`, canonical mathematics `yspennstate/math-open-problems@ddcf32d5ae84f2e891a6fd56d8ba0cbdc2853a1e`.  The partner proves that every one-dimensional certified Gaussian mixture

\[
Y=M+\sqrt T\,G,\qquad \mathbb E T^{-1/2}\le\sqrt{2\pi},
\]

satisfies, for every unit interval \(J\),

\[
\Pr(Y\in J)\le \alpha,
\qquad
\alpha:=2\Phi(\sqrt{\pi/2})-1
=0.789908594556\ldots .
\]

Write \(\beta:=1-\alpha=0.210091405444\ldots\).

## 2. New theorem: convex-hull separation is permanent

### Theorem 2.1 (event-separation compiler)

Let \(\tau\) be a probability law, let \(E\) be measurable with \(\tau(E)=1\), and let \({\cal G}\) be any class of probability laws satisfying

\[
\sup_{\nu\in{\cal G}}\nu(E)\le a<1.
\]

Then every probability law \(G\) in the convex hull (indeed arbitrary barycentric mixture) of \({\cal G}\) satisfies

\[
d_{\rm TV}(G,\tau)\ge 1-a.
\]

More sharply, suppose a law \(P\) admits a contamination decomposition

\[
P=wG+(1-w)R,
\qquad 0\le w\le1,
\]

where \(G\) is any convex mixture of laws in \({\cal G}\), and \(R\) is an arbitrary probability law.  If

\[
d_{\rm TV}(P,\tau)\le\delta,
\]

then

\[
\boxed{\quad w\le \frac{\delta}{1-a}.\quad}
\]

In particular, if \(P=\tau\) exactly, then \(w=0\): the target contains no positive mixture component from the good class.

### Proof

Barycentric linearity gives \(G(E)\le a\).  Hence

\[
d_{\rm TV}(G,\tau)\ge |G(E)-\tau(E)|\ge1-a.
\]

For the contaminated law,

\[
P(E)=wG(E)+(1-w)R(E)
\le wa+(1-w)=1-w(1-a).
\]

On the other hand \(d_{\rm TV}(P,\tau)\le\delta\) and \(\tau(E)=1\) imply \(P(E)\ge1-\delta\).  Combining the two inequalities yields

\[
w(1-a)\le\delta.
\]

No regularity or topology is used.  \(\square\)

## 3. Application to the partner inverse-scale class

Let \(U_n\) denote the uniform law on the cube \([0,1]^n\), so its density is exactly the cap-one product density \(1_{[0,1]^n}\).  Let \({\cal G}_n\) consist of product laws

\[
\nu=\nu_1\otimes\cdots\otimes\nu_n
\]

for which every coordinate law \(\nu_i\) satisfies the partner inverse-scale certificate

\[
Y_i=M_i+\sqrt{T_i}G_i,
\qquad \mathbb E T_i^{-1/2}\le\sqrt{2\pi}.
\]

For the cube event \(E_n=[0,1]^n\), the completed partner theorem gives

\[
\nu(E_n)=\prod_{i=1}^n\nu_i([0,1])\le\alpha^n.
\]

Therefore Theorem 2.1 gives the dimension-amplified separation

\[
\boxed{
\inf_{G\in\operatorname{conv}({\cal G}_n)}
 d_{\rm TV}(G,U_n)
\ge 1-\alpha^n.
}
\]

The same statement holds for arbitrary latent mixtures

\[
G=\int \bigotimes_{i=1}^n \nu_{i,z}\,\pi(dz)
\]

provided every conditional coordinate law \(\nu_{i,z}\) obeys the partner certificate: latent randomization may destroy unconditional coordinate independence, but it cannot increase the cube mass beyond \(\alpha^n\).

Numerically,

\[
1-\alpha=0.2100914\ldots,
\]

\[
1-\alpha^2=0.3760444\ldots,
\qquad
1-\alpha^3=0.5071321\ldots,
\]

and \(1-\alpha^n\to1\) exponentially quickly.

Consequently, if

\[
P=wG+(1-w)R,
\qquad G\in\operatorname{conv}({\cal G}_n),
\]

and \(d_{\rm TV}(P,U_n)\le\delta\), then

\[
\boxed{
 w\le \frac{\delta}{1-\alpha^n}.
}
\]

For \(n=3\),

\[
w\le 1.97187\ldots\,\delta.
\]

For the exact cube source \(P=U_n\), necessarily \(w=0\).

This is strictly stronger than non-density of the certified class itself: taking arbitrary convex hulls, randomized certified components, or adding an arbitrary residual does not rescue the approximation route if the certified component is required to retain any fixed positive mass.  As the approximation error tends to zero, its admissible weight tends to zero.  In high dimension the coefficient tends to one.

A coordinatewise version is immediate.  If a one-dimensional law \(P\) with \(d_{\rm TV}(P,U_1)\le\delta\) is decomposed as \(P=wG+(1-w)R\) with certified \(G\), then

\[
w\le \delta/\beta=4.75950357\ldots\,\delta.
\]

Thus even before taking products, an exact uniform marginal has **no positive certified Gaussian-mixture component** in the measure-order sense.

## 4. QFORM consequence of the new obstruction

The completed Gaussian-mixture theorem is a genuine full-law QFORM receiver on its certified input class, but Theorem 2.1 shows that the arbitrary cap-one problem cannot be closed by the following generic strategy:

1. approximate each rough source (or the full product source) by a law with a fixed positive fraction of certified Gaussian-mixture mass;
2. apply the completed QFORM bound on that fraction;
3. discard or perturbatively absorb the residual.

Already for the exact cap-one cube source, the certified fraction in any positive mixture decomposition is zero.  Under \(\delta\)-TV approximation it is only \(O(\delta)\), and for the full cube the denominator is \(1-\alpha^n\).  Because density height is not controlled by an arbitrarily small uncontrolled residual, this decomposition cannot supply the missing universal output bound.

This is a proof-route obstruction, not a QFORM counterexample: the uniform cube source itself is admissible and may of course have bounded quadratic outputs for particular matrices.

## 5. Independent check of the owner-pinned ruled / rough-input bridge

The owner-pinned `e5f71d79...` source proves the following majority-side theorem for an exact rank-three form of signature \((2,1)\): if the eigenvalues are \(\lambda_1,\lambda_2,-\mu\) with \(\lambda_1,\lambda_2,\mu>0\), then on the one-sheet/majority side its output submeasure has interval-density coefficient

\[
C_B
=(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
\frac{d\theta}{
\sqrt{\sin^2\theta/\lambda_1+\cos^2\theta/\lambda_2+1/\mu}}
\le \frac{\pi\sqrt2}{\kappa},
\]

where \(\kappa=\min(\lambda_1,\lambda_2,\mu)\).  The geometric constants check: after spectral scaling, the ruling

\[
F(\theta,t)=\sqrt{s}\,e_\theta+t(e_\theta^\perp+e_3)
\]

has coarea quotient \(\tfrac12\,d\theta\,dt\), while \(t\) is not arclength and therefore the line integral carries the reciprocal speed \(1/|v_\theta|\).  Combining this with the completed two-dimensional product-projection cap \(2\) gives exactly the displayed \(C_B\).

Now let \(B=A_{SS}\) be an invertible original-coordinate physical \(3\times3\) block of signature \((2,1)\), and condition on all outside coordinates \(W=w\).  The active conditional form is

\[
Q_w(x)=x^\top Bx+2d(w)^\top x+c_0(w)
      =(x+B^{-1}d(w))^\top B(x+B^{-1}d(w))+c(w).
\]

The completion of the square is a translation in the **original independent coordinates**, so the three active translated marginals remain independent and cap one.  No post-rotation independence is asserted.

For arbitrary rough cap-one marginals, mollify only these three original-coordinate densities.  Convolution preserves the cap and product structure, and the active product densities converge in \(L^1\).  Hence their conditional laws converge in total variation.  Deterministic quadratic pushforward, and subsequent restriction to the majority event, cannot increase total variation.  The smooth ruled interval domination therefore passes with no constant loss to the original rough law:

\[
\boxed{
\Pr\{Q\in I,\ Q\ge c(W)\}\le C_B|I|
\qquad\text{for every interval }I.
}
\]

(For signature \((1,2)\), reverse signs and use the corresponding lower half-line.)  This is an essential-boundedness statement for a positive submeasure; it proves no continuity statement.

Applying the positive triangular kernel gives an owner-scale paid inequality.  Since

\[
\int_{\mathbb R}(\varepsilon-|z-y|)_+\,dz=\varepsilon^2,
\]

we obtain directly

\[
\boxed{
\mathbb E\!\left[(\varepsilon-|Q-y|)_+\,\mathbf1_{\{Q\ge c(W)\}}\right]
\le C_B\varepsilon^2
\le \frac{\pi\sqrt2}{\kappa}\varepsilon^2.
}
\]

No continuity of the output is invoked anywhere in this height payment.

## 6. Exact logical ledger

1. **Absolute continuity.**  If \(A\ne0\) and the joint input law has a Lebesgue density, then \(x\mapsto x^\top Ax\) has absolutely continuous pushforward.  For a null set \(N\), local coarea gives zero weighted measure on its preimage, and \(\nabla q(x)=2Ax\) vanishes only on the proper null subspace \(\ker A\).  This is qualitative and supplies no height constant.

2. **Essential boundedness.**  The QFORM target is a class-uniform interval domination / essential-height problem.  The ruled theorem above pays one positive submeasure directly; the strong-physical-triple and cross-volume receivers pay other structural regimes.  No continuity inference is needed.

3. **Continuity.**  Continuity is a separate individual-output conclusion.  It cannot be used to manufacture a uniform height bound, and the source obstruction in Sections 2–4 is purely measure-theoretic: it remains present regardless of output continuity.

## 7. Remaining implication

The local ruled residual is the minority/two-sheet term, but the current programme contains stronger full-law receivers when a strong physical triple or usable third cross-volume is available.  Globally the unpaid regime is therefore the structural intersection where neither receiver fires.  Any closure argument there must retain genuine original-coordinate product provenance.  The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` excludes replacing that provenance by generic projected X-ray control, and Theorem 2.1 now also excludes recovering arbitrary rough sources by a fixed positive convex amount of the completed inverse-scale Gaussian-mixture class.

A promising next step is a receiver that is **stable under product-source truncation/conditioning itself**, rather than under source smoothing with a hidden inverse-scale budget: one wants a positive-functional or conditional-height estimate whose payment depends on the structural matrix certificate and cap-one product geometry, not on how much regularized component mass is present.
