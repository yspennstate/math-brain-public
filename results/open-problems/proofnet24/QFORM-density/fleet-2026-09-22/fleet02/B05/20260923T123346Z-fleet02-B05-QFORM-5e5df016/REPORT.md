SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-23T12:33:46.065394143Z.
attacking: the punctured heavy-null innovation bridge — use product-preserving finite-Pluecker coarea to make the two-sheet estimate uniform as the same-bank innovation tends to zero, then exhibit a target-valid diffuse obstruction to bounded finite-frame selection.

# fleet02/B05 — finite-Pluecker punctured-innovation bridge

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound / complementary constructions and source-valid counterexamples  
**Run:** `20260923T123346Z-fleet02-B05-QFORM-5e5df016`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / SOURCE_VALID_STRUCTURAL_OBSTRUCTION / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** only essential boundedness is asserted by the new bridge; full-target continuity remains separate.

The full conjecture remains OPEN. Nothing below assumes moments, compact support, connected support, log-concavity, iid inputs, a diagonal independent basis, or independence after spectral rotation.

## 1. First unpaid implication before the calculation

The preceding fleet02/B05 result reduced the exact-rank-three heavy-null two-sheet survivor to two transverse original-coordinate banks. In one bank, the longitudinal coefficient row has the orthogonal regression decomposition

\[
 u=a v+d w+\tau\xi,
 \qquad \xi\perp v,w,\qquad \|\xi\|_2=1,\qquad \tau>0.
\]

The positive-innovation cross-volume theorem costs `tau^{-1/3}` and therefore is not uniform as `tau -> 0`, while the exact `tau=0` endpoint is already paid. The first unpaid issue was the punctured bridge.

This run proves that **there is no punctured singularity at all whenever the two-dimensional curved normal pencil has a finite original-coordinate Pluecker frame**. The estimate is uniform in `tau>0` and survives `tau -> 0`. It then gives an exact target family showing that no fixed-size finite Pluecker frame can be extracted universally. Thus the remaining factor is now specifically a **Pluecker-diffuse aggregate-before-selection problem**, not an innovation-size problem.

Result name:

`QFORM-PUNCTURED-INNOVATION-FINITE-PLUECKER-BRIDGE-v1`.

First unpaid implication after this run:

`QFORM-HEAVY-NULL-PLUECKER-DIFFUSE-BRIDGE-v1`.

## 2. Source inputs actually used

### 2.1 Required newest-Claude package

I read the owner-pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its ruled one-sheet Theorem C is applied quantitatively in Section 8 to the exact target stress family constructed there:

\[
\sup_{s\ge0}p_Q(s)\le \pi\sqrt2.
\]

Thus that family is a genuine **two-sheet** obstruction to finite-frame extraction, not a counterexample hidden on the already-paid ruled side.

### 2.2 Previous fleet02/B05 heavy-null reduction

The immediate predecessor is

`yspennstate/math-open-problems@3c4c6882813d9530dc5c3884ce3e25f5993c7062`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260923T102208Z-fleet02-B05-QFORM-a4c7d9e1/REPORT.md`.

It supplies the exact heavy-null normal form and the bank innovation invariant. In particular, after conditioning a disjoint transverse bank, the active bank has coefficients `u,v,w` with

\[
u=a v+d w+\tau\xi,\qquad \xi\perp v,w,
\]

and transverse Gram matrix

\[
S=\begin{pmatrix}\|v\|^2&\langle v,w\rangle\\
\langle v,w\rangle&\|w\|^2\end{pmatrix},
\qquad d_0:=\det S\ge1/640.
\]

The homogeneous spectral core can be written

\[
M=\begin{pmatrix}0&b&0\\ b&\alpha&\delta\\0&\delta&\gamma\end{pmatrix},
\qquad |b|\ge1,\qquad |\gamma|\ge1,
\]

and the hub leverage is `c>1/2`.

### 2.3 Latest compatible designated partner fleet03/B05

The freshest fleet03/B05 run present before publication is r23, whose new theorem is a kappa-free **ambient-gradient** density estimate for a different grouped ratio packet and explicitly leaves an ambient-to-level product-trace step unpaid. Its late refresh records the completed r24 theorem as the relevant curved-section result.

The compatible theorem used here is therefore fleet03/B05 r24:

`yspennstate/math-open-problems@b0e14a08fe8abb97f7aeb518cfa8cf4cef568d36`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260923T094405Z-fleet03-B05-QFORM-r24/REPORT.md`.

For a product density `F=prod f_k`, one affine-linear map `F1` and one quadratic map `F2`, write on a regular codimension-two fiber

\[
j_{ij}=\frac{|\partial(F_1,F_2)/\partial(x_i,x_j)|}
{|\nabla F_1\wedge\nabla F_2|}.
\]

r24 proves

\[
\int_M F j_{ij}\,d\mathcal H^{n-2}\le2,
\]

and, if a fixed set `S0` of `m` coordinate pairs captures the normalized normal bivector with strength `eta`,

\[
\Big(\sum_{\alpha\in S_0}j_\alpha^2\Big)^{1/2}\ge\eta
\quad\Longrightarrow\quad
\int_MF\,d\mathcal H^{n-2}\le {2m^{3/2}\over\eta}.
\tag{2.1}
\]

The same completed report records the single-hub bathtub receiver: if the `L=l` slice measure of the residual variable obeys

\[
\mu_l(E)\le K|E|^{1/2}
\]

uniformly, then for a cap-one independent hub in the normalized form `2XL+Y`,

\[
\|p_Q\|_\infty\le {1\over2}+2\sqrt2 K.
\tag{2.2}
\]

Equations (2.1)-(2.2) are applied below, not merely cited.

### 2.4 Product projection cap

The Livshyts--Paouris--Pivovarov / Rogozin--Ball product-projection bound, in the normalization already used in the rank-two-fusion record, gives for any two coefficient vectors with Gram matrix `S`

\[
\|p_{(V,W)}\|_\infty\le {2\over\sqrt{\det S}}.
\tag{2.3}
\]

This is used only for an ORIGINAL-coordinate linear projection of one product bank; no transformed coordinates are declared independent.

## 3. Condition one bank and expose the exact parabolic shear

Condition the disjoint bank `K`. Its contributions are constants. On the live bank `J`, write

\[
U=aV_J+dW_J+\tau T,
\qquad T=\xi\cdot X_J,
\]

with `xi` orthogonal in coefficient space to both `v,w`. Let

\[
L=V_J+v_0,\qquad W=W_J+w_0
\]

be the corresponding affine total transverse coordinates after the conditioned bank is inserted.

The full active form is

\[
Q=2b\sqrt c\,X_iL+Y,
\tag{3.1}
\]

where, after collecting terms depending only on `L`,

\[
Y=2b\tau LT+A L^2+2D LW+\gamma W^2+E L+F.
\tag{3.2}
\]

The exact values of `A,D,E,F` are irrelevant. They may depend on the conditioned bank.

Crucially, (3.2) keeps the same-bank dependence of `(T,L,W)` intact. No conditional density of `T` given `(L,W)` is introduced.

## 4. The curved normal pencil is two-dimensional and fixed

Consider the map on the live product bank

\[
\Phi=(L,Y).
\]

Its first normal is `v`. Differentiating (3.2), all multiples of `v` disappear after wedging with `v`, and

\[
 v\wedge\nabla Y
 =2b\tau L\,(v\wedge\xi)
   +2(DL+\gamma W)\,(v\wedge w).
\tag{4.1}
\]

Set

\[
E_\wedge=\operatorname{span}\{v\wedge\xi,\ v\wedge w\}
\subset\Lambda^2\mathbb R^J.
\]

Because `xi` is orthogonal to both `v` and `w`, the two displayed bivectors are orthogonal:

\[
\langle v\wedge\xi,v\wedge w\rangle
=\|v\|^2\langle\xi,w\rangle-\langle v,w\rangle\langle\xi,v\rangle=0.
\tag{4.2}
\]

Also

\[
\|v\wedge w\|^2=d_0=\det S.
\tag{4.3}
\]

Assume that a fixed set `S0` of `m` ORIGINAL-coordinate pairs has the intrinsic finite-frame property

\[
\|P_{S_0}z\|_2\ge\eta\|z\|_2
\qquad(z\in E_\wedge)
\tag{4.4}
\]

for some `eta>0`. Then every normalized regular normal bivector in (4.1) has at least `eta` of its Euclidean mass on `S0`. The partner r24 theorem (2.1) therefore gives, on every regular fiber `{L=l,Y=y}`,

\[
\boxed{
\int_{\{L=l,Y=y\}}F_J\,d\mathcal H^{|J|-2}
\le {2m^{3/2}\over\eta}.
}
\tag{4.5}
\]

This is the first key point: the bound is completely independent of `tau`, including in the punctured regime `tau -> 0`.

## 5. Rough-input fold/off-fold interval estimate

Define the affine fold coordinate

\[
Z=DL+\gamma W.
\tag{5.1}
\]

By (4.1)-(4.3), the codimension-two coarea Jacobian is

\[
J_2:=|v\wedge\nabla Y|
=2\sqrt{(b\tau L)^2\|v\wedge\xi\|^2+Z^2d_0}.
\tag{5.2}
\]

Hence on the off-fold set `|Z|>=r`,

\[
J_2\ge2r\sqrt{d_0}.
\tag{5.3}
\]

Combining (4.5) with the codimension-two coarea formula gives the off-fold joint density bound

\[
 h_{L,Y}^{\rm off}(l,y)
 \le {m^{3/2}\over\eta r\sqrt{d_0}}.
\tag{5.4}
\]

No pointwise representative of a curved spectral fiber is used: (5.4) is obtained from the physical-coordinate coarea inequality before taking any level supremum.

For the fold slab, `(L,W)` is an ORIGINAL-coordinate two-dimensional product projection. By (2.3),

\[
\|p_{(L,W)}\|_\infty\le {2\over\sqrt{d_0}}.
\tag{5.5}
\]

The affine map `(L,W)->(L,Z)` has determinant `gamma`, so

\[
\|p_{(L,Z)}\|_\infty\le {2\over|\gamma|\sqrt{d_0}}.
\tag{5.6}
\]

Consequently the `L=l` slice mass of the fold slab obeys

\[
\mu_l\{|Z|<r\}
\le {4r\over|\gamma|\sqrt{d_0}}.
\tag{5.7}
\]

Let `I` be any Borel interval of length `epsilon`. Split its slice preimage into the fold slab and its complement. Equations (5.4) and (5.7) give, for every `r>0`,

\[
\mu_l\{Y\in I\}
\le {4r\over|\gamma|\sqrt{d_0}}
 +{m^{3/2}\epsilon\over\eta r\sqrt{d_0}}.
\tag{5.8}
\]

Optimizing in `r` yields the rough-input square-root interval estimate

\[
\boxed{
\mu_l\{Y\in I\}
\le K_J\,|I|^{1/2},
\qquad
K_J={4m^{3/4}\over\sqrt{\eta|\gamma|d_0}}.
}
\tag{5.9}
\]

The estimate is valid for arbitrary fragmented/unbounded cap-one input laws and is uniform in the innovation size `tau>0`. No continuity of the output law was assumed.

## 6. Feed the slice theorem into the independent hub

Equation (3.1) is

\[
Q=2a_h X_iL+Y,
\qquad a_h=b\sqrt c.
\]

Replace `L` by `L'=a_hL`. Under this scalar change, the slice constant in (5.9) becomes `K_J/|a_h|`. Applying the partner single-hub receiver (2.2),

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le {1\over2}
 +{8\sqrt2\,m^{3/4}
 \over |b|\sqrt c\,\sqrt{\eta|\gamma|d_0}}.
}
\tag{6.1}
\]

In the target-normalized heavy-null branch

\[
|b|\ge1,\qquad |\gamma|\ge1,\qquad c>{1\over2},\qquad d_0\ge{1\over640},
\]

so

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le {1\over2}+128\sqrt{10}\,m^{3/4}\eta^{-1/2}
< {1\over2}+404.772\,m^{3/4}\eta^{-1/2}.
}
\tag{6.2}
\]

### Theorem 6.1 — `QFORM-PUNCTURED-INNOVATION-FINITE-PLUECKER-BRIDGE-v1`

Under the heavy-null bank hypotheses above, any finite Pluecker-frame certificate (4.4) closes the complete punctured innovation range `tau>0` with the uniform bound (6.1), hence (6.2) under the target normalization. The bound does not deteriorate as `tau -> 0`.

This removes the previous `tau^{-1/3}` collar loss on the entire finite-frame branch. The exact `tau=0` endpoint remains separately paid by the dependence-safe null-scalar theorem from the preceding B05 run.

## 7. Why a bounded finite frame cannot be forced

The finite-frame hypothesis is not an automatic consequence of the exact target. Here is an exact target-valid family proving that.

Let `N=2^k` and let `xi,v,w` be three distinct normalized Walsh--Hadamard columns in `R^N`. Thus they are pairwise orthonormal and every coordinate is `+/-N^{-1/2}`. Fix any `c in (1/2,1)` and put

\[
\tau=\sqrt{1-c}.
\]

Define an `(N+1) x 3` Parseval frame `R` by the hub row

\[
r_0=(\sqrt c,0,0)
\]

and residual rows

\[
r_j=(\tau\xi_j,v_j,w_j),\qquad 1\le j\le N.
\tag{7.1}
\]

Then `R^TR=I_3`. Take

\[
M=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},
\qquad A=RMR^T.
\tag{7.2}
\]

The nonzero spectrum of `A` is exactly

\[
\{-1,1,1\},
\]

so (7.2) lies inside the exact QFORM target. Its quadratic form is

\[
Q=2(\sqrt c\,X_0+\tau T)V+W^2,
\quad
T=\xi\cdot X_{1:N},\ V=v\cdot X_{1:N},\ W=w\cdot X_{1:N}.
\tag{7.3}
\]

For the normal pencil

\[
E_\wedge=\operatorname{span}\{v\wedge\xi,v\wedge w\},
\]

the two displayed bivectors are orthonormal. Every coordinate-pair component of either bivector is in `{0,+/-2/N}`. Therefore for **every** collection `S0` of `m` physical coordinate pairs,

\[
\|P_{S_0}|_{E_\wedge}\|_{\rm HS}
\le {\sqrt{8m}\over N},
\]

and hence

\[
\boxed{
\sigma_{\min}(P_{S_0}|_{E_\wedge})
\le {\sqrt{8m}\over N}.
}
\tag{7.4}
\]

For fixed `m`, the right side tends to zero. Thus no theorem selecting a uniformly bounded number of physical Pluecker coordinates with a dimension-free lower frame bound can close QFORM.

This is **not** a counterexample to QFORM. It is a source-valid counterexample to the finite-frame-extraction mechanism.

## 8. Required newest-Claude result applied to the stress family

The matrix `M` in (7.2) has signature `(+,+,-)` and all three nonzero eigenvalue magnitudes equal one. Deterministically diagonalizing this three-dimensional spectral matrix preserves the fact that its spectral vectors form an orthonormal projection of the original product source; no probabilistic independence after rotation is asserted.

Therefore the pinned newest-Claude ruled one-sheet Theorem C applies to (7.3) on the one-sheet half-line and gives the actual inequality

\[
\boxed{
\sup_{s\ge0}p_Q(s)\le\pi\sqrt2.
}
\tag{8.1}
\]

So the Hadamard family (7.3) cannot hide a one-sheet counterexample. Its relevance is exactly the surviving convex/two-sheet geometry: it shows that the finite-coordinate Pluecker receiver can fail maximally while the already-paid ruled side stays uniformly bounded.

## 9. The sharpened missing factor

The preceding run's punctured parameter `tau` is no longer the right obstruction on the finite-frame branch. The new theorem is uniform in `tau`.

The actual survivor is:

**`QFORM-HEAVY-NULL-PLUECKER-DIFFUSE-BRIDGE-v1`.**  
In the heavy-null exact-rank-three two-sheet normal form, prove the slice estimate (5.9), or an equivalent hub-compatible level estimate, when the normal pencil

\[
\operatorname{span}\{v\wedge\xi,v\wedge w\}
\]

is Pluecker-diffuse in the sense that every bounded collection of original-coordinate pair components has vanishing lower frame constant. The estimate must spend the aggregate identity before selecting a physical pair and must preserve the original product law.

The Hadamard construction shows that this diffuse regime is genuinely present inside the exact target. The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` shows why replacing the pencil by an arbitrary joint density or a line-X-ray cap cannot solve it. The natural next move is therefore an **aggregate nonlinear Finner/coarea inequality for a decomposable shared-factor two-plane of bivectors**, rather than another local pair selector.

## 10. Finite checks

A deterministic Walsh--Hadamard check at `N=8,16,32,64`, with `c=3/4`, verified:

- `||R^TR-I_3||_op` at floating-point roundoff;
- the three nonzero eigenvalues of `A=RMR^T` are exactly `(-1,1,1)` to numerical precision;
- the largest Euclidean norm of a row of the two-column Pluecker restriction matrix equals `sqrt(8)/N`, matching the analytic component bound.

The numerical value in (6.2) was independently recomputed:

\[
8\sqrt2\sqrt{1280}=128\sqrt{10}=404.7715405015\ldots
\]

The checks are diagnostics only; Sections 4-8 are the proof and obstruction.

## 11. Scope

Proved this run:

- a dimension-free rough-input interval/slice theorem through the full punctured innovation range under a finite physical Pluecker-frame certificate;
- the resulting essential density bound (6.1)/(6.2);
- a target-valid Hadamard family proving that bounded-cardinality finite-frame extraction is not universal;
- an actual application of newest-Claude Theorem C to that family, giving (8.1).

Not proved:

- the Pluecker-diffuse aggregate-before-selection step;
- the unrestricted exact-rank-three convex/two-sheet theorem;
- the full arbitrary-rank QFORM conjecture;
- full continuity.

Every probabilistic independence used is between disjoint ORIGINAL-coordinate banks or the independent hub and the residual bank. Curved fiber geometry is retained throughout; no unrestricted fiber supremum is taken.
