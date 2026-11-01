# fleet03 / B05 / QFORM r24

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound  
**Status:** `SUPPORTING_GLOBAL_COAREA_THEOREM_PROVED / FINITE-PLUECKER-FRAME_CS_BRANCH_CLOSED / FULL_QFORM_OPEN`  
**Continuity:** the results below prove absolute continuity with an `L^infty` bound in their stated branch; they do **not** prove full-target continuity.  
**Brain state:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Compact end-to-end target for this run

The current single-hub/two-sheet obstruction contains the sliced map

\[
\Phi(x)=(L(x),Y(x)),\qquad
L(x)=w\cdot x,\qquad
Y(x)=\lambda(V(x)-V_0)^2+\beta B(x)+\text{constant},
\]

where `w,v,b` are orthonormal original-coordinate coefficient vectors,
`V=v·x`, `B=b·x`, and the input law has density

\[
F(x)=\prod_{k=1}^n f_k(x_k),\qquad 0\le f_k\le1,\qquad \int f_k=1.
\]

The open curved-section estimate `(CS)` in the shared single-hub record asks for a dimension-free bound on the joint density of `(L,Y)` away from the fold `|V-V0|<=r`.  A generic bounded joint density of `(L,V,B)` is not enough, and a coordinate-by-coordinate fiber supremum can lose dimension.

This run proves a global, product-preserving coarea inequality for *every linear/quadratic codimension-two fibre*.  It then gives an explicit `(CS)` receiver whenever two (or finitely many) original-coordinate Pluecker components capture the two-dimensional normal pencil.  The remaining branch is therefore not merely “curved”: it is quantitatively **Pluecker-diffuse**.

## 2. Global coordinate-pair coarea inequality

Let

\[
F_1(x)=a\cdot x-a_0
\]

be nonconstant affine linear and let `F2` be any real polynomial of degree at most two.  At a regular fibre

\[
M=M_{s,t}=\{x:F_1(x)=s,\ F_2(x)=t\}
\]

write

\[
J(x)=|\nabla F_1(x)\wedge\nabla F_2(x)|
\]

and, for an original-coordinate pair `alpha={i,j}`,

\[
D_{ij}(x)=\left|
\frac{\partial(F_1,F_2)}{\partial(x_i,x_j)}
\right|
=|a_i\partial_jF_2-a_j\partial_iF_2|,
\qquad
j_{ij}(x)=\frac{D_{ij}(x)}{J(x)}.
\tag{2.1}
\]

Cauchy--Binet gives

\[
\sum_{i<j}j_{ij}(x)^2=1.
\tag{2.2}
\]

### Theorem 2.1 — one coordinate pair costs at most two

For every `i<j`,

\[
\boxed{
\int_M \prod_{k=1}^n f_k(x_k)\,j_{ij}(x)\,d\mathcal H^{n-2}(x)\le2.
}
\tag{2.3}
\]

#### Proof

Let `pi_{ij}` be the orthogonal coordinate projection deleting coordinates `i,j`.  The tangential Jacobian of `pi_{ij}|_M` is exactly `j_{ij}`.  This is the standard implicit-function/coarea identity: the complementary `2x2` minor of the normal matrix divided by the Euclidean norm of all its `2x2` minors is the Jacobian of the complementary coordinate projection.

Apply the area formula to `pi_{ij}|_M`.  Fixing all coordinates except `x_i,x_j`, the two fibre equations consist of one affine-linear equation and one quadratic equation in `(x_i,x_j)`.  At points where `j_{ij}>0`, elimination of the linear equation leaves a nonzero univariate polynomial of degree at most two.  Hence there are at most two regular preimages.  If elimination is identically zero, the projection Jacobian is zero on that positive-dimensional fibre and it contributes nothing to the left side of (2.3).

At every regular preimage, `f_i(x_i)f_j(x_j)<=1`.  Therefore

\[
\begin{aligned}
\int_M F(x)j_{ij}(x)d\mathcal H^{n-2}(x)
&=\int_{\mathbb R^{n-2}}
\sum_{x\in M:\pi_{ij}x=z}F(x)\,dz\\
&\le2\int_{\mathbb R^{n-2}}\prod_{k\ne i,j}f_k(z_k)\,dz
=2.
\end{aligned}
\]

No rotated coordinate is declared independent and no support or moment hypothesis is used.  QED.

### Corollary 2.2 — Pluecker-weighted nonlinear Finner inequality

For any probability weights `p_{ij}>=0`, `sum_{i<j}p_{ij}=1`,

\[
\boxed{
\int_M F(x)\prod_{i<j}j_{ij}(x)^{p_{ij}}d\mathcal H^{n-2}(x)\le2.
}
\tag{2.4}
\]

Indeed, because the weights sum to one,

\[
F\prod j_{ij}^{p_{ij}}=\prod(Fj_{ij})^{p_{ij}},
\]

and Holder followed by (2.3) gives (2.4).

This is a global nonlinear coarea inequality with a dimension-free constant.  Its weight is exactly the normalized Pluecker geometry of the curved fibre; there is no local flattening or patch-counting loss.

## 3. Finite Pluecker-frame receiver

Let `S` be a fixed collection of `m` original-coordinate pairs.  Suppose that on the fibre

\[
\left(\sum_{\alpha\in S}j_\alpha(x)^2\right)^{1/2}\ge\eta>0.
\tag{3.1}
\]

### Theorem 3.1

Then

\[
\boxed{
\int_M F(x)d\mathcal H^{n-2}(x)\le\frac{2m^{3/2}}{\eta}.
}
\tag{3.2}
\]

#### Proof

Partition `M` measurably according to which `j_alpha`, `alpha in S`, is maximal.  On each piece the maximal component is at least `eta/sqrt(m)`.  Therefore, using (2.3) separately on each piece,

\[
\int_MF
\le\sum_{\alpha\in S}\frac{\sqrt m}{\eta}\int_MFj_\alpha
\le m\frac{\sqrt m}{\eta}\,2.
\]

QED.

For `m=2`,

\[
\boxed{\int_MF\le4\sqrt2\,\eta^{-1}.}
\tag{3.3}
\]

## 4. Application to the exact curved-section obstruction `(CS)`

Take orthonormal `w,v,b` and

\[
L=w\cdot x,\qquad
Y=\lambda(V-V_0)^2+\beta B,
\qquad V=v\cdot x,\quad B=b\cdot x.
\tag{4.1}
\]

On the fibre `{L=l,Y=y}` put

\[
t=2\lambda(V-V_0).
\]

The two normal vectors are

\[
w,\qquad tv+\beta b,
\]

so

\[
J=|w\wedge(tv+\beta b)|=\sqrt{t^2+\beta^2}.
\tag{4.2}
\]

Define the two orthonormal bivectors

\[
a=w\wedge v,\qquad c=w\wedge b
\]

inside `Lambda^2 R^n`.  If coordinate pairs index their components, then

\[
j_\alpha
=\left|
\frac{t}{\sqrt{t^2+\beta^2}}a_\alpha
+\frac{\beta}{\sqrt{t^2+\beta^2}}c_\alpha
\right|.
\tag{4.3}
\]

Let `P_S:span{a,c}->R^S` be restriction to a fixed set `S` of `m` coordinate-pair components.  If

\[
\sigma_{\min}(P_S)\ge\eta,
\tag{4.4}
\]

then (3.1) holds for every value of `t,beta`, hence (3.2) is uniform on every curved fibre.

On the off-fold region `|V-V0|>=r`, (4.2) gives

\[
J\ge2|\lambda|r.
\]

The coarea formula therefore gives the joint density `h(l,y)` of `(L,Y)`, restricted off the fold,

\[
\boxed{
 h(l,y)\le\frac{m^{3/2}}{\eta|\lambda|r}.
}
\tag{4.5}
\]

Thus `(CS)` holds in this branch with

\[
\boxed{K_1=m^{3/2}/\eta.}
\tag{4.6}
\]

No bounded-support assumption, no moment assumption, and no conditional-density cap is used.

### Two physical coordinate-pair certificate

Take two coordinate pairs `alpha,gamma`.  Form

\[
R_{\alpha\gamma}
=\begin{pmatrix}
 a_\alpha&c_\alpha\\
 a_\gamma&c_\gamma
\end{pmatrix},
\qquad
\Delta_{\alpha\gamma}=|\det R_{\alpha\gamma}|.
\tag{4.7}
\]

Because `[a\ c]` has orthonormal columns, every coordinate restriction has operator norm at most one.  Hence

\[
\sigma_{\min}(R_{\alpha\gamma})
=\frac{|\det R_{\alpha\gamma}|}{\sigma_{\max}(R_{\alpha\gamma})}
\ge\Delta_{\alpha\gamma}.
\tag{4.8}
\]

Therefore any certificate

\[
\Delta_{\alpha\gamma}\ge\Delta>0
\]

gives

\[
\boxed{
 h(l,y)\le\frac{2\sqrt2}{\Delta|\lambda|r}.
}
\tag{4.9}
\]

This is an explicit, purely original-coordinate curved coarea receiver.

## 5. Feed into the single-hub bathtub

The shared `single_hub_core/REPORT.md`, Lemma 3.1, proves that if the slice measure obeys a square-root small-ball bound `mu_l(S)<=K|S|^{1/2}`, then an arbitrary cap-one hub law gives

\[
\|p_Q\|_\infty\le\frac12+2\sqrt2\,K.
\tag{5.1}
\]

The same source records the standard fold decomposition: a fold slab of width `r` has sliced mass at most `4r`, while an off-fold density bound `K_1/(|lambda|r)` yields

\[
K=4\sqrt{K_1}\,|\lambda|^{-1/2}.
\tag{5.2}
\]

Combining (4.6), (5.1), and (5.2), the finite-Pluecker-frame branch has

\[
\boxed{
\|p_Q\|_\infty
\le\frac12+8\sqrt2\,m^{3/4}\eta^{-1/2}|\lambda|^{-1/2}.
}
\tag{5.3}
\]

For two coordinate pairs with determinant certificate `Delta`,

\[
\boxed{
\|p_Q\|_\infty
\le\frac12+8\,2^{5/4}(\Delta|\lambda|)^{-1/2}
<\frac12+19.028(\Delta|\lambda|)^{-1/2}.
}
\tag{5.4}
\]

This closes a genuine part of the spread-leak/two-sheet receiver for arbitrary unbounded product laws.  It is not a bounded-support or coordinate-frame subclass: the normal pencil may be spread over all coordinates; the hypothesis asks only that two fixed physical Pluecker components form a quantitatively nondegenerate frame for that pencil.

## 6. Exact aggregate identity and the remaining factor

Since `a` and `c` are orthonormal in `Lambda^2 R^n`, the `N x 2` matrix `[a\ c]`, `N=binom(n,2)`, has orthonormal columns.  Cauchy--Binet therefore gives

\[
\boxed{
\sum_{\alpha<\gamma}
\Delta_{\alpha\gamma}^2=1.
}
\tag{6.1}
\]

So the total two-minor curvature packet is exactly one.  The failure of (5.4) to be universal can occur only when this unit packet is diffused among arbitrarily many physical pair-of-pair minors, making every individual `Delta_{alpha gamma}` small.

This identifies the next B05 factor more sharply than a generic “curved-section bound”:

`QFORM-PLUECKER-AGGREGATE-BEFORE-PAIR-SELECTION-v1`

> Upgrade (2.3)--(2.4) so that the exact aggregate identity (6.1) can be spent before selecting a coordinate pair, with a dimension-free unweighted bound on the quadratic section.  Equivalently, prove the `(CS)` bound for the Pluecker-diffuse normal pencil without paying `1/max Delta_{alpha gamma}`.

This is precisely where naive patching loses dimension.  The theorem above shows that no other local curvature is missing in the finite-frame branch.

## 7. Designated partner fleet04/B05 applied to an actual inequality

The completed designated-partner result

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B05/20260923T041255Z-fleet04-B05-dominant-slope-r2/REPORT.md`

proves, for the current ratio-packet exact-slope mass `m_*`,

\[
\|p_Q\|_\infty<51.6(\mu m_*)^{-1/3}.
\tag{7.1}
\]

Apply it to the concrete branch

\[
\mu\ge1,\qquad m_*\ge\frac18.
\]

Then

\[
\boxed{
\|p_Q\|_\infty<51.6\,8^{1/3}=103.2.
}
\tag{7.2}
\]

Hence any packet with at least one eighth of the Schur-direction mass on one exact physical slope is already uniformly closed.  The non-atomic/slope-diffuse transition is the branch in which the new Pluecker aggregate receiver is relevant.

## 8. Literature check

A fresh literature search found Jennifer Duncan, *An Algebraic Brascamp--Lieb Inequality*, J. Geom. Anal. 31 (2021), 10136--10163, arXiv:2001.03141.  Theorem 1.5 is a global nonlinear Brascamp--Lieb inequality for quasialgebraic maps, but it necessarily includes the local weight `BL(dB(x),p)^{-1}`.  It therefore does **not** directly give the unweighted `(CS)` estimate: precisely where a coordinate projection degenerates, that published weight vanishes.  The elementary inequality (2.4) is a tailored dimension-free version of the same weighted principle for our degree-two fibres; the still-unpaid step is removing/aggregating the Pluecker weight using the original product structure.

## 9. Scope

- Full QFORM: **OPEN / not proved / not disproved**.
- This report proves a global product-preserving codimension-two quadratic coarea inequality and closes the finite-Pluecker-frame `(CS)` branch.
- It does not silently assume Gaussianity, log-concavity, moments, compact or connected support, or independence after rotation.
- Essential bounded density is proved in the stated branch.  A continuous representative is **not** proved here.
- Independent end-to-end review of this r24 theorem: `PENDING`.
