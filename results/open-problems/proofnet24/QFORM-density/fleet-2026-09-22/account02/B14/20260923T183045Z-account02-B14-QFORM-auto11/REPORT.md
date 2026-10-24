SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T18:30:45Z.
attacking: rough-law localization after the new arbitrary-matrix Gaussian-mixture theorem — quantify whether separated cap-one fragments can be approximated by admissible random-center Gaussian mixtures without paying component-scale mass before the translations are aggregated.

# account02/B14 — a quantitative Gaussian-mixture localization barrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T183045Z-account02-B14-QFORM-auto11`  
Status: `NEW PROVED LOCALIZATION / APPROXIMATION OBSTRUCTION; FULL QFORM OPEN`  
Continuity: separate; no unrestricted continuity claim.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The newest full arbitrary-matrix Gaussian-mixture theorem proves QFORM with constant `<3` when every original coordinate has a representation

\[
X_i=M_i+\sqrt{T_i}G_i,
\qquad \mathbb E T_i^{-1/2}\le\sqrt{2\pi}.
\]

Its source explicitly warns that random separated centers can leave the final marginal density capped by one while the inverse-scale budget becomes arbitrarily large. The exact remaining localization issue is therefore:

> **QFORM-ROUGH-CENTER-AGGREGATION-BEFORE-SCALE-INVERSION-v1.** Either aggregate the random translation/fragment labels before paying reciprocal Gaussian scale, or use a whole-law QFORM certificate that does not depend on component peak. A reduction that approximates every cap-one marginal by admissible Gaussian mixtures with a uniform inverse-half-scale budget cannot work.

This report proves the last sentence quantitatively, first on the latest designated partner's compact finite-fragment extreme law, then on an exact smooth random-center Gaussian mixture that lies inside the full three-eigenvalue target.

## 2. BV cost of a Gaussian location-scale mixture

Let

\[
g(x)=\mathbb E\,\varphi_T(x-M),
\qquad
\varphi_T(u)=(2\pi T)^{-1/2}e^{-u^2/(2T)},
\qquad H:=\mathbb E T^{-1/2}<\infty,
\]

where `(M,T)` may be arbitrarily dependent and no moment of `M` is assumed. Then `g` has bounded variation and

\[
\boxed{\operatorname{Var}(g)\le \sqrt{\frac2\pi}\,H.}
\tag{2.1}
\]

Indeed, for every compactly supported smooth test `psi`, Fubini and integration by parts give

\[
\int g\psi'
=-\mathbb E\int \varphi_T'(x-M)\psi(x)\,dx.
\]

Moreover

\[
\|\varphi_T'\|_1
=\frac1T\int |x|\varphi_T(x)\,dx
=\sqrt{\frac2\pi}\,T^{-1/2}.
\]

Taking the supremum over `|psi|<=1` proves (2.1). Notice that arbitrary translations disappear completely: the BV cost sees only the reciprocal scale.

## 3. Quantitative obstruction on the latest partner's fragmented extreme law

The latest designated partner account03/B14 constructs

\[
E_N=\bigcup_{j=1}^N[4j,4j+N^{-1}],
\qquad f_N=\mathbf 1_{E_N},
\tag{3.1}
\]

as a compact finite-fragment cap-one probability density. Its report uses exactly this geometry to show that interval-only half-Frostman control does not survive an arbitrary rough-hub receiver. Here the same `E_N` gives a different localization obstruction.

Choose a compact Lipschitz function `psi_N`, `|psi_N|<=1`, that rises linearly from `-1` to `+1` on every component of `E_N`, falls from `+1` back to `-1` across each gap, and tapers to zero outside the outer fragments. Because every active interval has length `1/N`, it may be chosen with

\[
\|\psi_N'\|_\infty\le2N,
\qquad
\int f_N(x)\psi_N'(x)\,dx=2N.
\tag{3.2}
\]

For any Gaussian location-scale mixture density `g` as in Section 2, put

\[
\delta=\|g-f_N\|_1.
\]

The BV duality bound and (3.2) imply

\[
\operatorname{Var}(g)
\ge\left|\int g\psi_N'\right|
\ge2N-2N\delta.
\]

Combining with (2.1) gives the quantitative theorem

\[
\boxed{
H\ge N\sqrt{2\pi}\,(1-\delta).
}
\tag{3.3}
\]

In particular, under the inverse-scale hypothesis required by the full Gaussian-mixture QFORM theorem,

\[
H\le\sqrt{2\pi},
\]

one necessarily has

\[
\boxed{
\|g-f_N\|_1\ge1-\frac1N.
}
\tag{3.4}
\]

Thus even the exact compact finite-fragment extreme class is not dense in `L^1` in the admissible Gaussian-mixture class with a uniform inverse-scale budget. As `N->infinity` the separation is order one. No bounded-diameter or fixed-fragment shortcut is involved; the gaps may be moved arbitrarily far apart, and a common translation changes none of the estimates.

Equation (3.4) is the main new localization result. It turns the qualitative warning “separated random centers can have a large average peak” into a sharp fragment-count obstruction to the proposed approximation interface.

## 4. A non-vacuous smooth cap-one random-center family

The preceding extreme density is compactly supported and therefore cannot itself be an exact positive mixture of nondegenerate Gaussians. To show that the obstruction is not merely an exact-representation artifact, define a genuinely smooth Gaussian mixture. Let

\[
\sigma_N=\frac1{2N},
\qquad
M_N\text{ uniform on }\{4,8,\ldots,4N\},
\qquad
X_N=M_N+\sigma_NG,
\tag{4.1}
\]

with `G` standard normal. Its density is

\[
g_N(x)
=\sqrt{\frac2\pi}\sum_{j=1}^N
   e^{-2N^2(x-4j)^2}.
\tag{4.2}
\]

This is an unbounded-support, arbitrarily translated/fragmented law. It is nevertheless cap one uniformly in `N`. To see this, on the Voronoi cell of a nearest center the other centers are at distances at least `4m-2`; outside the extreme cells the estimate is even smaller. Hence

\[
\begin{aligned}
 g_N(x)
 &\le \sqrt{\frac2\pi}
 \left(1+2\sum_{m\ge1}e^{-2N^2(4m-2)^2}\right)\\
 &\le \sqrt{\frac2\pi}
 \left(1+\frac{2e^{-8}}{1-e^{-64}}\right)
 <0.799<1.
\end{aligned}
\tag{4.3}
\]

But in the Gaussian-mixture representation (4.1),

\[
T_N=\sigma_N^2=\frac1{4N^2},
\qquad
\boxed{\mathbb E T_N^{-1/2}=2N.}
\tag{4.4}
\]

Thus the final marginal cap stays strictly below one while the component reciprocal-scale budget grows linearly. This is the smooth random-center version of the same fragmentation phenomenon.

## 5. Exact-target comparison: raw component inversion loses N^2, whole-law control stays constant

Take three independent copies of `X_N` and the exact-target quadratic form

\[
Q_N=X_{N,1}^2+X_{N,2}^2+X_{N,3}^2,
\qquad A=I_3.
\tag{5.1}
\]

The matrix has three eigenvalues equal to one, and every input density satisfies the original cap-one hypothesis by (4.3).

### 5.1 What the Gaussian component calculation pays

Condition on the three random centers. In the notation of the checked arbitrary-matrix Gaussian-mixture proof,

\[
D=T_NI_3,
\qquad B=D^{1/2}AD^{1/2}=T_NI_3,
\qquad W_3=e_3(B^2)=T_N^6.
\]

Its proved conditional Fourier calculation therefore gives

\[
\|p_{Q_N\mid M}\|_\infty
\le \frac{I_3}{2\pi}W_3^{-1/6}
=\frac{I_3}{2\pi}T_N^{-1}
=\boxed{\frac{2I_3}{\pi}N^2},
\tag{5.2}
\]

where `I_3=2.942468198...`. Numerically,

\[
\frac{2I_3}{\pi}=1.8732334345\ldots .
\]

Averaging these conditional density suprema over the translation labels retains the `N^2` loss. This is exactly the wrong order: reciprocal scale is paid before the separated centers are aggregated.

### 5.2 Required newest-Claude source applied to the same law

Now use the completed Theorem A in

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

For `n=3` and all eigenvalues of `A` of modulus at least `sigma=1`, that theorem gives, uniformly over all independent cap-one input laws and with linear terms allowed,

\[
\boxed{
\|p_{Q_N}\|_\infty\le6\sqrt\pi
=10.6347231054\ldots .
}
\tag{5.3}
\]

This is independent of `N`, of all center locations, and of the unbounded Gaussian tails. Hence on the very same exact-target family the whole-law source theorem stays uniformly bounded while the component-first Gaussian certificate (5.2) diverges quadratically.

For the compact extreme inputs `f_N` of Section 3, the same Theorem A also yields `||p_{X_1^2+X_2^2+X_3^2}||_infty<=6sqrt(pi)` uniformly in `N`, while (3.4) prevents approximation by admissible inverse-scale Gaussian mixtures. Thus both the rough extreme and its smooth random-center analogue point to the same proof-order obstruction.

## 6. Relation to the latest designated partner

The newest partner account03/B14 result shows, with the same `E_N`, that interval-only square-root slice control can coexist with logarithmically unbounded output in a rank-two rough-hub receiver. Applying that exact partner construction here gives the BV lower bound (3.3): every attempt to replace its finite-fragment law by a Gaussian mixture with `L^1` error `delta` must pay inverse-scale budget at least

\[
N\sqrt{2\pi}(1-\delta).
\]

So two seemingly different failed interfaces have the same source: **localizing/normalizing each distant fragment before the active smoothing mechanism erases the translation geometry.** The partner obstruction concerns Borel-profile information after interval localization; the present obstruction concerns inverse Gaussian scale after component localization.

This use is source-compatible: the partner's counterexample has only two large eigenvalues and is not promoted to a QFORM counterexample. The target-valid comparison is separately supplied by (5.1)--(5.3).

## 7. Consequence for localization and mixture strategies

A legitimate full-target localization argument may still restrict law-level optimization to finite-fragment extreme densities, because that operation keeps the whole law. What cannot follow is

\[
\text{finite fragments}
\longrightarrow
\text{narrow Gaussian component approximation}
\longrightarrow
\text{pay }\mathbb ET^{-1/2}\text{ componentwise}
\longrightarrow
\text{average translations}.
\]

Equations (3.4) and (5.2) quantify the two failures of this ordering. The safe direction must instead be one of:

- aggregate the translation labels/whole active marginal before reciprocal scale or curvature is inverted;
- use a whole-law D'/D5/projected-crossing/hub/pair/ridge certificate whose hypotheses are expressed directly in the original cap-one product law; or
- prove a new random-center Gaussian-mixture theorem controlled by the **final marginal density cap** rather than `E T^{-1/2}`. Such a theorem would have to exploit overlap/separation of the component images under the quadratic map, because no one-dimensional inverse-scale inequality can see it.

This leaves the full conjecture open, but removes a concrete approximation route from the remaining proof tree and identifies precisely what a successful rough-law extension of the Gaussian theorem must retain.

## 8. Exact status

New proved statements:

- `QFORM-GAUSSIAN-MIXTURE-BV-BUDGET-v1`: (2.1).
- `QFORM-FRAGMENTED-EXTREME-GAUSSIAN-APPROX-BARRIER-v1`: (3.3)--(3.4).
- `QFORM-RANDOM-CENTER-COMPONENT-INVERSION-BARRIER-v1`: smooth cap-one family (4.1)--(4.4) with target comparison (5.2)--(5.3).

These are proof-interface/localization results, not lower bounds on the universal QFORM constant and not counterexamples to QFORM. The full target and unrestricted continuity remain open.
