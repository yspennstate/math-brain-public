# fleet04/B13 — no-attainment purification and rough ruled-side transfer

Run: 20260922T231352Z-fleet04-B13-rough-geometric-transfer-r5  
Programme: QFORM-DENSITY-3EIG-20260922, owner control revision 2026-09-22.15  
Status: PROVED TARGET-LEVEL REDUCTION AND ROUGH ONE-SHEET BRANCH / FULL CONJECTURE OPEN  
Execution: WITHOUT_VERIFIED_BRAIN

## 1. Scope and sources

The target is the universal essential density bound for \(X^TAX\) under independent one-dimensional densities \(0\le f_i\le1\), when \(A\) has at least three eigenvalues of modulus at least one. Continuity is separate.

Fresh controls were read from math-research-brain main, including AGENTS.md (blob e2aa9d53924e2d4e015b7c6680b0009241bec619), the owner request (blob ad68bf86f7c0437def9db625408081374700f08f), and the live correction inbox (blob c7000cf3822ae4935a2faf43b89ac92ea65ac0fe).

The geometric input is the Claude package at math-open-problems commit e5f71d79eff325201dd0274053d20268ce65b837, especially the RESULTS and COUNTEREXAMPLE_SEARCH reports in proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/. The completed fleet01/B13 result used below is math-open-problems@680ff828e47704689fde0ca4b1690860a9cbd71f, with handoff at brain commit 02f399acc9a279664063574cd2a7a6e088a428f4. The bang-bang source it applies is math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94.

No pointwise quadratic-phase decay, post-rotation independence, bounded support, moment condition, or arbitrary-joint coarea assertion is used.

## 2. Repair of the unattained bathtub step

Let
\[
\mathcal D=\{f\in L^1(\mathbb R):0\le f\le1,\ \int f=1\}.
\]

The usual threshold proof is unsafe as an attainment statement on the infinite line. For example, \(h(x)=1-(1+|x|)^{-1}\) has supremum one but no unit-measure set attaining the supremum of \(\int_E h\). What is true, and sufficient, is equality of suprema.

### Lemma 2.1 (unit-indicator closure, no attainment)

For every bounded measurable \(h\),
\[
\sup_{f\in\mathcal D}\int h f
=
\sup_{|E|=1}\int_E h.
\tag{2.1}
\]
Neither supremum need be attained.

#### Proof

Every \(f\in\mathcal D\) is an \(L^1\)-limit of finite convex combinations of indicators of bounded finite unions of intervals having measure one.

First replace the tail of \(f\) outside a sufficiently large compact interval by an indicator set of the missing mass. This preserves the cap and total mass and changes \(f\) by arbitrarily little in \(L^1\).

For the compactly supported density, choose a grid of mesh \(1/m\), extend it far enough to contain the support, and replace \(f\) by its cellwise conditional expectation
\[
g=\sum_{j=1}^N a_j1_{I_j},\qquad
0\le a_j\le1,\qquad
\sum_j a_j=m.
\]
These conditional expectations converge to \(f\) in \(L^1\). The vector \(a\) lies in the hypersimplex
\[
\{a\in[0,1]^N:\sum_j a_j=m\}.
\]
Its extreme points are the zero-one vectors with exactly \(m\) ones: if two coordinates are strictly between zero and one, a small opposite perturbation shows that the point is not extreme. Hence
\[
a=\sum_\nu\theta_\nu v^\nu,\qquad
\theta_\nu\ge0,\quad\sum_\nu\theta_\nu=1,
\]
where every \(v^\nu\) has exactly \(m\) ones. Consequently
\[
g=\sum_\nu\theta_\nu1_{E_\nu},
\qquad |E_\nu|=m/m=1.
\]
Each \(E_\nu\) is a bounded finite union of grid intervals.

Since \(h\) is bounded,
\[
\int hf
=\lim_k\sum_\nu\theta_{k,\nu}\int_{E_{k,\nu}}h
\le\sup_{|E|=1}\int_Eh.
\]
The reverse inequality follows from \(1_E\in\mathcal D\). This proves (2.1) without an optimizer or threshold set. ∎

### Corollary 2.2 (product purification)

For every measurable \(K:\mathbb R^n\to[0,1]\),
\[
\sup_{f_1,\dots,f_n\in\mathcal D}
\int K(x)\prod_i f_i(x_i)\,dx
=
\sup_{\substack{|E_i|=1\\E_i\ {\rm bounded\ finite\ interval\ unions}}}
\int_{\prod_iE_i}K(x)\,dx.
\tag{2.2}
\]

Approximate each \(f_i\) by the finite mixtures from Lemma 2.1 and expand their product. The product \(L^1\) error is at most the sum of the marginal errors, so the bounded functional converges. This is an exact supremum identity; it does not assert an attained optimizer, a single interval, bounded diameter, or bounded fragment count.

For \(K=1_{\{x^TAx\in J\}}\), (2.2) is the geometric slab reformulation needed for QFORM.

## 3. Rough-input one-sheet theorem

Let \(R=(r_1,r_2,r_3)\) have orthonormal columns and put \(Y=R^TX\). Consider
\[
Q=\lambda_1Y_1^2+\lambda_2Y_2^2-\mu Y_3^2,
\qquad \lambda_1,\lambda_2,\mu\ge1.
\tag{3.1}
\]
For an interval \(J\subset[0,\infty)\), define
\[
C(\lambda_1,\lambda_2,\mu)
=
(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
\left(
\frac{\sin^2\theta}{\lambda_1}
+\frac{\cos^2\theta}{\lambda_2}
+\frac1\mu
\right)^{-1/2}d\theta.
\tag{3.2}
\]
The ruled-surface calculation in the source proves for smooth cap-one product inputs that
\[
\Pr(Q\in J)\le C(\lambda_1,\lambda_2,\mu)|J|
\le\pi\sqrt2\,|J|.
\tag{3.3}
\]

### Theorem 3.1 (rough ruled-side interval theorem)

Inequality (3.3) holds for arbitrary independent cap-one input densities, with no support, moment, or regularity assumption.

#### Proof

By Corollary 2.2 it is enough to treat \(f_i=1_{E_i}\), where every \(E_i\) is a bounded finite union of intervals and \(|E_i|=1\). Let \(\gamma_\varepsilon\) be a centered Gaussian density and set
\[
f_{i,\varepsilon}=1_{E_i}*\gamma_\varepsilon.
\]
Then \(f_{i,\varepsilon}\) is positive analytic Schwartz, has mass one, satisfies \(\|f_{i,\varepsilon}\|_\infty\le1\), and converges to \(1_{E_i}\) in \(L^1\).

For the corresponding product laws,
\[
\left\|\bigotimes_i f_{i,\varepsilon}
-\bigotimes_i1_{E_i}\right\|_1
\le\sum_i\|f_{i,\varepsilon}-1_{E_i}\|_1\to0.
\tag{3.4}
\]
Measurable pushforwards contract total variation, so the laws of \(Q\) converge in total variation. Apply the smooth ruled estimate and then pass to the limit in the fixed interval event:
\[
\Pr(Q\in J)\le C(\lambda_1,\lambda_2,\mu)|J|.
\]
This proves the estimate for product indicators; Corollary 2.2 proves it for every cap-one product density.

The endpoint \(0\) creates no atom: the zero set of the nonzero polynomial (3.1) has Lebesgue measure zero, and the original joint law is absolutely continuous. ∎

Replacing \(Q\) by \(-Q\) gives the majority-sign one-sheet side of signature \((+,-,-)\). This proves essential boundedness only on that half-line. It is not the two-sheet theorem and not the full conjecture.

## 4. Application of completed fleet01/B13 mathematics

The completed fleet01/B13 exact-graph/null-pivot branch proves, under its stated exact-rank-three graph-bank hypotheses, that every unit product set satisfies
\[
\left|\left\{x\in\prod_iE_i:x^TAx\in J\right\}\right|
<335.063\,|J|.
\tag{4.1}
\]
Apply Corollary 2.2 with \(K=1_{\{x^TAx\in J\}}\). For arbitrary independent cap-one densities,
\[
\boxed{\Pr(X^TAX\in J)<335.063\,|J|.}
\tag{4.2}
\]
Therefore this branch has a density satisfying
\[
\boxed{\|p_{X^TAX}\|_\infty\le335.063.}
\tag{4.3}
\]
This is a zero-loss application to an actual target inequality. It retains arbitrary fragmented and unbounded original-coordinate laws. It does not extend the fleet01/B13 graph-bank hypotheses.

## 5. The remaining geometric slab

For the normalized signature
\[
q(y)=y_1^2+y_2^2-y_3^2,
\]
the unresolved two-sheet side is \(s=-a^2<0\). If \(\rho\) is a smooth density of \(Y\), coarea gives
\[
p_q(-a^2)
=
\frac12\int_0^\infty\int_0^{2\pi}
\frac{r}{\sqrt{r^2+a^2}}
\left[
\rho(re_\theta,\sqrt{r^2+a^2})
+\rho(re_\theta,-\sqrt{r^2+a^2})
\right]d\theta\,dr.
\tag{5.1}
\]
Unlike the one-sheet surface, this surface has no real rulings. Thus the codimension-two marginal cap cannot be inserted as a line-trace bound. The live arbitrary-joint correction shows that a bounded projected density or X-ray norm alone cannot control (5.1).

After the proved purification, the exact remaining geometric obligation is
\[
\left|
\left\{
x\in\prod_iE_i:
-a^2-\delta\le q(R^Tx)\le-a^2
\right\}
\right|
\le C\delta
\tag{5.2}
\]
uniformly in \(a,\delta,R,n\) and in bounded finite-union \(E_i\) of measure one.

A local cutoff shows why tails cannot be discarded. If one only knows \(\rho\le M\), then the part of the slab with \(r\le R_0\) is at most
\[
2\pi M R_0\,\delta,
\tag{5.3}
\]
because its Euclidean volume is at most \(2\pi R_0\delta\). No moment hypothesis controls the complementary \(r>R_0\) part, so optimizing (5.3) cannot yield a universal linear estimate. Product provenance must be used jointly with the curved trace before radial tails are paid.

## 6. Status

Proved here:

1. a rigorous repair of the infinite-line bathtub issue using \(L^1\)-closed finite mixtures, with no asserted optimizer;
2. the rough-product one-sheet interval theorem with constant \(C(\lambda_1,\lambda_2,\mu)\le\pi\sqrt2\);
3. the arbitrary-law inequality \(\|p_Q\|_\infty\le335.063\) in the completed fleet01/B13 exact-graph/null-pivot branch.

Still open:

* the convex/two-sheet estimate (5.2);
* compilation of all exact-rank-three matrices into paid geometric branches;
* arbitrary additional spectral directions;
* the full universal constant and the separate continuity assertion.
