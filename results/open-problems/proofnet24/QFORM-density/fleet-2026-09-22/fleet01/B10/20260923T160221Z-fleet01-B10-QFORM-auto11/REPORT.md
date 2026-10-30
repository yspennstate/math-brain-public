SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B10, 2026-09-23T16:02:21Z.
attacking: the punctured near-coloop two-hub Fresnel mechanism; integrate an arbitrary invertible physical pair exactly and determine whether its local determinant loss cancels before the remaining product-frame estimate.

# fleet01/B10 — two-hub Schur–Fresnel cancellation and the exact leftover-volume obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T160221Z-fleet01-B10-QFORM-auto11`  
Status: `ESSENTIAL_STEP_APPLIED / NEW_ANALYTIC_THEOREM / EXACT_BARRIER_IDENTITY / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full arbitrary exact-rank-three theorem and the owner-level three-large-eigenvalue conjecture remain **OPEN / NOT PROVED / NOT DISPROVED**. This run changes mechanism from the preceding aggregate-packing argument. Instead of selecting or inverting a local minor, it integrates an arbitrary invertible **physical two-coordinate block** exactly and proves that every dependence on that block's determinant and row-plane area cancels from the rank-three Fresnel coefficient. What remains is solely the product-frame concentration of the coordinates not integrated. This gives a new continuous-density theorem, and it identifies exactly why the previous disjoint pair-times-triple packet does not yet close the ultra-coloop collar.

## 1. Exact-rank-three setup

Write

\[
A=UMU^T,\qquad U^TU=I_3,
\]

where `M` is a real invertible symmetric `3x3` matrix. In the target application all three eigenvalues of `M` have absolute value at least one, hence

\[
D:=|\det M|\ge1.
\tag{1.1}
\]

All rows of `U` are deterministic coefficient vectors in spectral coefficient space. All random variables below remain the original independent coordinates `X_i`; no rotation of the random vector is made.

Choose two original coordinates, relabelled `1,2`, and let

\[
R=\begin{pmatrix}u_1^T\\u_2^T\end{pmatrix}\in\mathbb R^{2\times3},
\qquad
B:=RMR^T.
\tag{1.2}
\]

Assume only that the physical principal block `B` is invertible. Then `R` has row rank two. Put

\[
g:=\det(RR^T)>0,
\tag{1.3}
\]

and let `v` be either unit normal to the row plane `range(R^T)`.

For the remaining coordinates define the spectral aggregate

\[
z:=\sum_{j\ne1,2}u_jX_j
\tag{1.4}
\]

and the complementary row Gram

\[
G:=\sum_{j\ne1,2}u_ju_j^T=I_3-R^TR.
\tag{1.5}
\]

The theorem below requires `G>0` and a diffuse gate only on these remaining original coordinates. There is no lower bound on `|det B|`.

## 2. Exact two-coordinate Schur residual

The quadratic form is

\[
Q=X_{12}^TBX_{12}+2X_{12}^TRMz+z^TMz,
\qquad
X_{12}=(X_1,X_2)^T.
\tag{2.1}
\]

Complete the square in the **physical** pair:

\[
Q=
\left(X_{12}+B^{-1}RMz\right)^TB
\left(X_{12}+B^{-1}RMz\right)
+z^TNz,
\tag{2.2}
\]

where

\[
N:=M-MR^TB^{-1}RM.
\tag{2.3}
\]

Because

\[
NR^T=MR^T-MR^TB^{-1}RMR^T=0,
\tag{2.4}
\]

and `N` is symmetric, the two-dimensional row plane of `R` is contained in `ker N`. Since `M` and `B` are invertible, `N` has rank exactly one, hence

\[
N=\theta vv^T
\tag{2.5}
\]

for a nonzero real `theta`.

### Lemma 2.1 — exact coefficient identity

\[
\boxed{
\theta=\frac{\det M\;g}{\det B}.
}
\tag{2.6}
\]

#### Proof

Choose an orthonormal basis matrix `E` for the row plane and write

\[
R=KE^T
\]

with `K` invertible `2x2`. In the orthogonal basis `(E,v)`, write

\[
M=\begin{pmatrix}C&c\\c^T&d\end{pmatrix}.
\]

Then

\[
B=KCK^T,
\qquad
g=(\det K)^2,
\]

and (2.3) becomes the scalar Schur complement

\[
\theta=d-c^TC^{-1}c=\frac{\det M}{\det C}.
\]

Since `det B=g det C`, (2.6) follows. `square`

Thus a tiny or huge physical pair determinant is exactly reciprocated by the residual rank-one curvature. This is the two-coordinate analogue of the scalar pivot–Schur determinant transfer from the preceding B10 work.

## 3. Exact Fresnel transform of the physical pair

For fixed `t!=0` and `d in R^2`, define

\[
H_t(d):=
\int_{\mathbb R^2}
 f_1(x_1)f_2(x_2)
 e^{it(x+d)^TB(x+d)}\,dx.
\tag{3.1}
\]

Use the Fourier convention

\[
\widehat F(\xi)=\int_{\mathbb R^2}e^{i\xi\cdot d}F(d)\,dd.
\]

A Gaussian-regularized two-dimensional Fresnel calculation and the change `y=x+d` give the exact factorization

\[
\widehat H_t(\xi)
=
\mathfrak c_B(t)
\exp\!\left(-\frac{i}{4t}\xi^TB^{-1}\xi\right)
\psi_1(-\xi_1)\psi_2(-\xi_2),
\tag{3.2}
\]

where `psi_j(s)=E exp(isX_j)` and

\[
\boxed{
|\mathfrak c_B(t)|
=\frac{\pi}{|t|\sqrt{|\det B|}}.
}
\tag{3.3}
\]

This is exact. It uses probability normalization and the true product law of the two original coordinates, not a post-rotation independence assertion and not a pointwise van-der-Corput estimate.

## 4. The three-dimensional change of variables and complete local cancellation

By (2.2) and (2.5),

\[
\phi_Q(t)
=
\mathbb E_{j\ne1,2}
\left[
H_t(B^{-1}RMz)
 e^{it\theta(v^Tz)^2}
\right].
\tag{4.1}
\]

Fourier-invert `H_t` and use the one-dimensional Fresnel representation of `exp(it theta y^2)`. The resulting integral is over `(xi,s) in R^2 x R`, and the remaining original coordinates enter linearly through

\[
\eta=-MR^TB^{-1}\xi+s v.
\tag{4.2}
\]

Two exact identities make this representation useful.

First,

\[
R\eta=-RMR^TB^{-1}\xi=-\xi.
\tag{4.3}
\]

Therefore the two characteristic factors already present in (3.2) are precisely

\[
\psi_1(u_1^T\eta)\psi_2(u_2^T\eta)
\]

up to harmless sign/conjugation. Together with the untouched coordinates they reconstruct the full original-coordinate product.

Second, the Jacobian of (4.2) is

\[
\boxed{
\left|\det(MR^TB^{-1},v)\right|=g^{-1/2}.
}
\tag{4.4}
\]

Indeed, in the basis `(E,v)` used above,

\[
MR^TB^{-1}=ME C^{-1}K^{-1},
\]

whose upper `2x2` block is `K^{-1}`; appending `v` gives determinant `det(K^{-1})`, whose modulus is `g^{-1/2}`.

Hence

\[
d\xi\,ds=\sqrt g\,d\eta.
\tag{4.5}
\]

Now multiply the three geometric factors appearing after the two Fresnel transforms:

\[
|\det B|^{-1/2}
|\theta|^{-1/2}
\sqrt g.
\]

Using (2.6), they cancel **exactly**:

\[
\boxed{
|\det B|^{-1/2}
|\theta|^{-1/2}
\sqrt g
=D^{-1/2}.
}
\tag{4.6}
\]

No lower bound on the physical pair determinant survives.

## 5. Pair-invariant full-product representation and its precise limitation

Taking absolute values only after the three-dimensional change of variables gives

\[
\boxed{
|\phi_Q(t)|
\le
\frac{D^{-1/2}}{8\pi^{3/2}|t|^{3/2}}
\int_{\mathbb R^3}
\prod_i |\psi_i(u_i^T\eta)|\,d\eta.
}
\tag{5.1}
\]

Whenever the integral is finite, (5.1) is independent of which invertible physical pair was used. Thus every local pair determinant, every row-plane area, and the rank-one Schur coefficient are artificial currencies at this fully linearized level; they collapse to the single invariant `D^{-1/2}`.

But (5.1) is **not** a universal proof interface. The live correction `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1` already records that for the diagonal three-coordinate uniform example the absolute product integral is infinite although the output density is bounded and continuous. Therefore the new identity does not resurrect the invalid absolute-Wiener route. It says exactly where cancellation must be retained: before taking the absolute value of the complete transformed product.

This is useful for the present branch because it separates two issues cleanly:

1. local physical-pair conditioning is **not** the source of the blow-up — it cancels completely by (4.6);
2. the only remaining obstruction in an absolute-value proof is concentration/poor integrability of the residual original-coordinate product frame.

## 6. New theorem: diffuse complement after an arbitrary physical pair

Discard the two pair factors in (3.2) only by the safe bound `|psi_1|,|psi_2|<=1`, before applying the product-frame estimate to the remaining coordinates.

Assume

\[
G>0
\tag{6.1}
\]

and for every `j notin {1,2}`

\[
\boxed{
\ell_j^{(12)}:=u_j^TG^{-1}u_j\le\frac12.
}
\tag{6.2}
\]

The completed geometric Brascamp–Lieb/Hausdorff–Young estimate used in the preceding B10 Schur–Fresnel theorem gives

\[
\int_{\mathbb R^3}
\prod_{j\ne1,2}|\psi_j(u_j^T\eta)|\,d\eta
\le
(4\pi)^3(\det G)^{-1/2}.
\tag{6.3}
\]

Combining (3.3), the rank-one Fresnel factor, (4.4), (4.6), and (6.3) yields

\[
\boxed{
|\phi_Q(t)|
\le
8\pi^{3/2}[D\det G]^{-1/2}|t|^{-3/2}.
}
\tag{6.4}
\]

This gives the following theorem.

### Theorem 6.1 — `QFORM-TWO-HUB-SCHUR-FRESNEL-v1`

Let `A=UMU^T` be exact rank three with `U^TU=I_3` and `M` invertible symmetric. Suppose there exist two original coordinates whose physical principal `2x2` block `B` is invertible. Let `G` be the Gram matrix of all remaining spectral rows. If `G>0` and every remaining whitened leverage satisfies (6.2), then `Q=X^TAX` has a continuous density in `C_0(R)` and

\[
\boxed{
\|p_Q\|_\infty
\le
12[D\det G]^{-1/3}.
}
\tag{6.5}
\]

The statement is valid for definite or indefinite `B`, all signs of `M`, arbitrary independent cap-one input densities, arbitrary fragmented supports, and arbitrary orientation. There is no condition on `|det B|` beyond nonzero.

#### Proof of the density bound

Put

\[
K=8\pi^{3/2}[D\det G]^{-1/2}.
\]

Then

\[
|\phi_Q(t)|\le\min(1,K|t|^{-3/2}),
\]

and

\[
\int_{\mathbb R}\min(1,K|t|^{-3/2})dt=6K^{2/3}.
\]

Fourier inversion therefore gives

\[
\|p_Q\|_\infty
\le \frac{6}{2\pi}K^{2/3}
=12[D\det G]^{-1/3}.
\]

Since `phi_Q in L^1`, the density is continuous and vanishes at infinity. `square`

### Quantitative branch

If

\[
D\det G\ge2^{-9},
\]

then

\[
\boxed{\|p_Q\|_\infty\le96}
\tag{6.6}
\]

with continuity.

## 7. Exact application to the current near-coloop hub–leaf pairs

Return to the hard chamber from the immediate B10 predecessor. The physical hub is

\[
u_0=\sqrt h\,r,
\qquad
h>\frac{63}{64},
\]

and the leaf Gram is

\[
G_L=I-hrr^T.
\]

For a leaf `i`, put

\[
\ell_i=u_i^TG_L^{-1}u_i.
\tag{7.1}
\]

If its physical hub-pair determinant

\[
\Delta_i=\det A[\{0,i\}]<0,
\]

then the physical pair `B=A[{0,i}]` is automatically invertible, regardless of how small `|Delta_i|` is. The complement Gram after deleting the hub and this leaf is

\[
G_i=G_L-u_iu_i^T.
\]

The matrix determinant lemma gives the exact leftover-volume identity

\[
\boxed{
\det G_i=(1-h)(1-\ell_i).
}
\tag{7.2}
\]

Therefore, if `ell_i<1` and the remaining rows are diffuse after whitening by `G_i`, Theorem 6.1 gives the concrete density estimate

\[
\boxed{
\|p_Q\|_\infty
\le
12[D(1-h)(1-\ell_i)]^{-1/3}.
}
\tag{7.3}
\]

The local indefinite determinant `Delta_i` has disappeared completely. This is important for the fragmented hard state: a large local pair is unnecessary.

The post-deletion leverages can also be written exactly. For `j notin {0,i}`,

\[
\boxed{
\ell_{j\mid i}
=
\ell_j+
\frac{(u_j^TG_L^{-1}u_i)^2}{1-\ell_i}.
}
\tag{7.4}
\]

This is simply Sherman–Morrison. Hence the sole failure of the new theorem at a negative hub pair is now explicit: either `ell_i=1`, or the residual frame becomes concentrated through the second term in (7.4), or the leftover determinant `D(1-h)(1-ell_i)` is too small to give a universal number.

## 8. Why the previous pair-times-triple packet is not yet enough

The preceding run proved disjoint original-coordinate banks `H,J,K` with

\[
W_HT_{JK}>0.05379357,
\tag{8.1}
\]

where `W_H` is negative hub-pair determinant mass and `T_JK` is bordered triple mass with the **hub retained**.

For a particular negative pair `{0,i}`, however, the leftover determinant in Theorem 6.1 is, by Cauchy–Binet,

\[
\boxed{
\det G_i
=
\sum_{\substack{j<k<l\\j,k,l\ne0,i}}
\det(u_j,u_k,u_l)^2.
}
\tag{8.2}
\]

It consists only of triple volumes that avoid both the hub and the selected leaf. By contrast,

\[
\frac{T_{JK}}D
=
\sum_{j\in J,k\in K}
\det(u_0,u_j,u_k)^2,
\tag{8.3}
\]

which consists exactly of triple volumes **containing** the hub. Thus (8.2) and (8.3) are complementary geometric currencies. Peeling the hub as one of the two Fresnel variables discards the very third-rank packet guaranteed by the preceding run.

This is the precise obstruction to naively feeding (8.1) into Theorem 6.1. It is not a loss from `|det B|`: (4.6) proves that local pair determinant loss has already been removed. The next receiver must keep enough of the hub phase alive to spend (8.3) before the final absolute value.

## 9. Designated fleet02/B10 result applied at an actual inequality

The newest completed designated-partner result available before publication is

`yspennstate/math-open-problems@ebceb50f1e0c2589cb7599f57c4deb4a3ffd0f2b`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260923T141719Z-fleet02-B10-QFORM-r11/REPORT.md`.

Its theorem `QFORM-COLOOP-RANKONE-TRANSVERSE-MF-v1` treats the exact physical-coloop face with rank-one transverse compression and transverse leaf leverage at most one half. It proves

\[
\|p_Q\|_\infty
\le
3\,2^{4/3}D^{-1/3}.
\tag{9.1}
\]

Since the exact-rank-three target has `D>=1`, this gives the actual universal payment

\[
\boxed{
\|p_Q\|_\infty
\le3\,2^{4/3}<7.560.
}
\tag{9.2}
\]

The partner theorem also gives continuity. Thus the exact-coloop/rank-one-transverse boundary remains fully paid; the unresolved state is genuinely the punctured rank-two/transverse interaction described above. No conditional density cap is substituted for genuine independence.

A newer fleet02/B10 artifact at commit `d790e2e6cd2efb2ab7e2639431952996e2e946a2` was only a start record when checked, not a completed mathematical result, so it is not used as a premise.

## 10. First unpaid implication after this run

The first unpaid implication is now more sharply formulated as

`QFORM-PHASE-RETAINING-BORDERED-PAIR-TRIPLE-RECEIVER-v1`:

> In the punctured near-coloop chamber, use the disjoint original-coordinate certificate `W_H T_JK > 0.05379357` to obtain a dimension-free density bound while retaining the hub-containing triple phase through the first Fresnel integration. The proof may use the exact two-hub cancellation (4.6), but it must not replace the surviving transformed product by its full absolute Wiener integral and must not peel the hub before the bordered triple packet is spent.

The desired receiver should therefore be **phase-retaining** rather than another local-minor theorem. A successful estimate can lose a fixed negative power of `W_HT_JK`; the existing lower bound would then close the ultra-collar. Equation (4.6) shows that no reciprocal physical-pair determinant is needed.

## 11. Status and regularity

- `QFORM-TWO-HUB-SCHUR-FRESNEL-v1`: proved here, supporting theorem.
- Density conclusion in that theorem: bounded **and continuous** (`phi_Q in L^1`).
- Exact pair-invariant transformed bound (5.1): proved, but may be infinite and is not a universal receiver.
- Current disjoint pair-times-triple ultra-collar: still OPEN.
- Arbitrary exact-rank-three theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: OPEN.

No Gaussianity, log-concavity, moments, compact or connected support, iid assumption, post-rotation independence, arbitrary-joint coarea, conditional-projection supremum, or law-uniform pointwise quadratic-phase decay is used.

## 12. Source ledger and control refresh


The complement Brascamp–Lieb estimate (6.3) is the same completed product-frame input used in the preceding B10 Schur–Fresnel proof, source-pinned there to

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Immediate B10 structural predecessor:

`yspennstate/math-open-problems@79295a936c9f88cf9356c6ed5d52090fa1cedc37`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B10/20260923T152129Z-fleet01-B10-QFORM-auto11/REPORT.md`.

Designated partner actually applied:

`yspennstate/math-open-problems@ebceb50f1e0c2589cb7599f57c4deb4a3ffd0f2b`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260923T141719Z-fleet02-B10-QFORM-r11/REPORT.md`.

Repository transport is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
