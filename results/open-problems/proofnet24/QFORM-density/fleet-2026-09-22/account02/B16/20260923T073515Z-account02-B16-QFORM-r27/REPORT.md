# account02/B16 r27 — rank-one nonaligned slice-Wiener barrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Projection-product interaction / complementary source-valid constructions  
Run: `20260923T073515Z-account02-B16-QFORM-r27`

Source pins used in this run:
- owner/control brain snapshot initially resolved at `398784a523ebbda01243fad6975e70c5c4b96e1d` (fresh head was re-resolved again before writes);
- required completed source package `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially the proved two-dimensional product-marginal input used in Theorem C and the proved Fresnel/BL routes;
- compatible continuation source `math-open-problems@7ffd1ed79398611eb06752f622be0ce33dcacb5a`, `20260922T231000Z-semidefinite-and-hub-reduction/hub_decoupling/REPORT.md`, Section 7.3;
- designated partner account03/B16 r26, `QFORM-EXACT-R3-TWO-BANK-COCIRCUIT-COMPLETION-v1`.

## Status and first unpaid implication

**FULL TARGET CHANGE: NONE.** This note neither proves nor disproves the unrestricted conjecture. It proves that a natural proposed product-preserving bridge in the dense/nonaligned hub continuation is false even for a rank-one arbitrarily weak nonaligned coupling.

**First unpaid implication.** In the exact-rank-three near-coloop chamber left by account03/B16 r26, one must exploit the *special semi-aligned rank-three leakage structure* (or a different original-coordinate regrouping / physical-pivot route). One cannot close that chamber by asking for a dimension-free arbitrary-nonaligned slice-Wiener bound of the Section 7.3 form

\[
\Omega=\int d\tau\;\sup_z\left\|\int e^{isl}p(l,z,\tau)\,dl\right\|_{L^1(ds)}<\infty,
\]

because the theorem below gives \(\Omega=\infty\) with a four-coordinate cap-one product law and rank-one \(E\), however small \(\|E\|\) is.

## Theorem `QFORM-RANK1-NONALIGNED-SLICE-WIENER-BARRIER-v1`

Let \(X_1,\dots,X_4\) be independent uniform random variables on \([-1/2,1/2]\). Define

\[
L=\frac{X_1+X_2+X_3+X_4}{2},\qquad
V=\frac{X_1+X_2-X_3-X_4}{2},
\]
\[
T=\frac{X_1-X_2}{\sqrt2},\qquad
K=\frac{X_3-X_4}{\sqrt2}.
\]

Then:

1. \((L,V,T,K)\) is an orthogonal image of the original product cube.
2. The completed two-dimensional product-projection theorem applies to \((L,V)\) and gives
   \[
   \boxed{\|p_{L,V}\|_\infty\le2}.
   \]
   No independence between \(L\) and \(V\) is asserted or used.
3. The exact joint density of \((L,V,T)\) is
   \[
   \boxed{
   p_{L,V,T}(l,v,t)
   =\sqrt2\,(1-|l-v|)_+\,
   \mathbf1_{\{|l+v|\le1-\sqrt2|t|\}}
   },
   \]
   with the indicator interpreted as zero if \(|t|>1/\sqrt2\).
4. For every \(0<|t|<1/\sqrt2\), the one-dimensional Fourier transform in the \(l\)-variable of the slice \(p(l,0,t)\) is not in \(L^1(ds)\).
5. Consequently, for every \(\varepsilon>0\), after replacing \(T\) by the arbitrarily weak nonaligned coordinate \(\tau=\varepsilon T\), the Section-7.3 mixed Wiener quantity
   \[
   \Omega_\varepsilon
   :=\int d\tau\;\sup_v
   \left\|\int e^{isl}p_{L,V,\varepsilon T}(l,v,\tau)\,dl\right\|_{L^1(ds)}
   \]
   is infinite:
   \[
   \boxed{\Omega_\varepsilon=\infty\quad\text{for every }\varepsilon>0.}
   \]

Thus bounded two-dimensional product marginals plus arbitrarily weak rank-one nonaligned leakage do **not** imply the conjectural slice-Fourier \(L^1\) estimate.

### Proof: valid two-dimensional product marginal

The original-coordinate row vectors defining \((L,V)\) are

\[
(1/2,1/2),\ (1/2,1/2),\ (1/2,-1/2),\ (1/2,-1/2).
\]

Their frame operator is the identity on \(\mathbb R^2\), and every normalized row leverage is exactly \(1/2\). The completed two-dimensional product-marginal theorem from the pinned source package therefore gives

\[
\|p_{L,V}\|_\infty\le2.
\]

This is the required use of a completed projection theorem. Notice that it gives a joint density cap and nothing more: \(L,V\) are overlapping projections of the same product bank and generally dependent.

### Proof: exact projected density

The inverse orthogonal change of variables is

\[
X_1=\frac{L+V}{2}+\frac{T}{\sqrt2},\qquad
X_2=\frac{L+V}{2}-\frac{T}{\sqrt2},
\]
\[
X_3=\frac{L-V}{2}+\frac{K}{\sqrt2},\qquad
X_4=\frac{L-V}{2}-\frac{K}{\sqrt2}.
\]

The first pair of cube constraints is exactly

\[
|l+v|+\sqrt2|t|\le1.
\]

For fixed \((l,v,t)\), the second pair permits

\[
|k|\le\frac{1-|l-v|}{\sqrt2},
\]

so its allowed \(k\)-interval has length \(\sqrt2(1-|l-v|)_+\). Since the four-dimensional cube density is one and the transform is orthogonal, integrating out \(K\) gives the displayed formula for \(p_{L,V,T}\).

### Proof: boundary jumps force infinite Wiener norm

Fix \(v=0\) and \(0<|t|<1/\sqrt2\), and put

\[
b=1-\sqrt2|t|\in(0,1).
\]

Then

\[
p(l,0,t)=\sqrt2(1-|l|)\mathbf1_{\{|l|\le b\}}.
\]

At \(l=\pm b\), this slice has nonzero jumps of magnitude

\[
\sqrt2(1-b)=2|t|.
\]

With Fourier convention \(\widehat f(s)=\int e^{isl}f(l)\,dl\), direct integration gives

\[
\widehat p_t(s)
=2\sqrt2\left[
(1-b)\frac{\sin(bs)}{s}
+\frac{1-\cos(bs)}{s^2}
\right].
\]

Hence

\[
\widehat p_t(s)
=4|t|\frac{\sin(bs)}s+O(s^{-2}).
\]

On infinitely many disjoint intervals \(|\sin(bs)|\ge1/2\); for sufficiently large \(|s|\) the \(O(s^{-2})\) term is smaller than half the first term there. The harmonic integral over those intervals diverges, so

\[
\boxed{\|\widehat p_t\|_{L^1(ds)}=\infty.}
\]

Now set \(\tau=\varepsilon T\). Then

\[
p_{L,V,\tau}(l,v,\tau)
=\varepsilon^{-1}p_{L,V,T}(l,v,\tau/\varepsilon).
\]

For every \(0<|\tau|<\varepsilon/\sqrt2\), the \(v=0\) slice still has a nonzero boundary jump, hence its Fourier \(L^1\) norm is infinite. The integrand defining \(\Omega_\varepsilon\) is therefore infinite on a positive-measure set of \(\tau\), proving \(\Omega_\varepsilon=\infty\).

The same conclusion holds in the continuation source's actual frequency-scaled variable \(2tEX_I\): for every fixed Fourier frequency \(t\ne0\), replace \(\varepsilon\) above by \(2|t|\varepsilon\). Small frequency or small operator norm does not restore Wiener integrability.

## Exact match to the continuation source's nonaligned algebra

In the four-coordinate source bank \(I\), set

\[
w_I=\ell=(1,1,1,1)/2,\quad
v_I=v=(1,1,-1,-1)/2,\quad
u=(1,-1,0,0)/\sqrt2.
\]

These vectors are orthonormal. In a partner bank \(J_0\), take \(w_{J_0}=e_0\), and let \(e_2\perp e_0\). Define the rank-one map

\[
E=\varepsilon e_2\nu^\top:\mathbb R^I\to\mathbb R^{J_0}.
\]

Then

\[
Ew_I=0,\qquad E^\top w_{J_0}=0,\qquad \|E\|=\varepsilon,
\]

exactly the nonaligned hypotheses in Section 7.3, while \(EX_I=\varepsilon e_2T\). Therefore the failure above is not caused by an aligned hub-partner component.

## Target-class embedding: obstruction is source-valid, but not a QFORM counterexample

Add independent cap-one variables \(X_h,Y_0,Y_1,Y_2\), disjoint from the four-cube bank, and define

\[
Q_\varepsilon
=2X_h(L+Y_0)+2VY_1+2\varepsilon TY_2.
\]

This is a quadratic form in the original independent variables. An orthogonal change is used only to compute its spectrum, not to claim probabilistic independence. In the orthonormal compressed coordinates \((X_h,L,V,T,K,Y_0,Y_1,Y_2)\), the quadratic matrix is the direct sum of

\[
\begin{pmatrix}0&1&1\\1&0&0\\1&0&0\end{pmatrix},\qquad
\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\begin{pmatrix}0&\varepsilon\\\varepsilon&0\end{pmatrix},
\]

plus a zero direction. Hence

\[
\boxed{
\operatorname{spec}_{\ne0}(A_\varepsilon)
=\{\sqrt2,-\sqrt2,1,-1,\varepsilon,-\varepsilon\}.
}
\]

For every \(0<\varepsilon\le1\), this family belongs to the user's target class (indeed it has four eigenvalues of modulus at least one). It is **not** a counterexample to the bounded-density conjecture; it is a counterexample only to the proposed generic slice-Wiener proof interface. The family also contains strong physical structure that other proved routes may pay.

## Consequence for the designated partner r26 reduction

Account03/B16 r26 proves a uniform exact-rank-three bound whenever the maximum physical leverage satisfies \(c\le63/64\), leaving the near-coloop chamber \(c>63/64\). The present theorem does not contradict or weaken that result. Instead it rules out using the continuation source's broad arbitrary-nonaligned \(\Omega\)-estimate as the missing transition mechanism: that estimate already fails for rank-one \(E\) and an arbitrarily small nonalignment parameter.

Accordingly the next B16 target is narrower and more structural:

`QFORM-NEAR-COLOOP-SEMI-ALIGNED-TRANSDUCER-v1`: in the exact-rank-three near-coloop geometry, exploit the forced semi-alignment/rank-three coefficient relations and retain the original-product weights through the curved pushforward, or route the geometry into a bounded number of original-coordinate bank / physical-block certificates. Do not normalize conditional fibers, infer independence after projection, or replace the special rank-three leakage by an arbitrary nonaligned map.

## Validity notes

- The compact support in this note is an intentional admissible choice for a source-valid counterexample to a *proof mechanism*; no support assumption is inserted into the target conjecture.
- The only independence used is the original independence of the source coordinates. No independence of \(L,V,T\) is asserted.
- The bounded two-dimensional marginal estimate is used exactly where it is valid, but the theorem shows that such a cap alone does not control the required curved/sliced Wiener norm.
- Continuity of the final quadratic pushforward is a separate issue and is not claimed here.
- Full conjecture status remains OPEN.
