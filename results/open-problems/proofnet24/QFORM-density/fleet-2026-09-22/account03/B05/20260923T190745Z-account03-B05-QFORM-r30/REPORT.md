SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T19:07:45Z.
attacking: QFORM-TWISTED-TWOHUB-PARTNER-PLANE-TRACE-v1 — determine exactly where the r29 transverse U currency goes under the current two-hub slice/decoupling theorems, and preserve it before full partner slicing.

# account03/B05 — partner-plane normal form and exact failure of full two-partner slicing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `NEW EXACT STRUCTURAL THEOREM / PRECISE MISSING FACTOR / FULL QFORM OPEN`  
**Regularity:** no new full density or continuity theorem is claimed in this report.

## 1. Sources and predecessor

The immediate B05 predecessor is

`yspennstate/math-open-problems@d13d6e8e5ee6d13d7dcc36ae1dd3fdb661f64b59:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T173708Z-account03-B05-QFORM-r30/REPORT.md`.

It proved the independent product-kernel half-Riesz splice and showed, on a target-valid four-variable stress form, that completing both scalar directions before averaging can erase the third curvature and leave a logarithmically divergent conditional envelope.

The earlier currency calculation is

`yspennstate/math-open-problems@954c8b881c4c60ac643b7c68da6d1ce924e6427f:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T172119Z-account03-B05-QFORM-r29/REPORT.md`.

The current verified interactive continuation used here is

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae:proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`.

Its Theorems 6.4 and 6.5 are useful as a diagnostic: Theorem 6.4 closes two hubs when the light remainder has a positive-power interval profile on the full two-partner slices, while Theorem 6.5 closes two hubs when some coordinate split leaves a Frobenius amount of remainder curvature transverse to the two partner rows. This report proves that **neither resource can see the r29 transverse currency `U` in the live ratio packet**: after both partner coordinates are exposed, `U` lies entirely inside their own plane and is frozen, not transverse.

## 2. Exact live ratio packet

Let the first original-coordinate product bank be `X in R^N`, with independent coordinate densities bounded by one. Let `Gamma` be an `N x 2` matrix with orthonormal columns, and set

\[
V=\binom SR=\Gamma^T X.
\]

Let `Y,Z` be scalar variables from two disjoint original product banks, independent of `X` and of one another. The relevant quadratic packet is

\[
Q=V^T C V+2Y\,p^TV+2Z\,q^TV+\begin{pmatrix}Y&Z\end{pmatrix}B\binom YZ + \text{affine/outside terms},
\]
where

\[
p=\binom\alpha r,\qquad q=\binom\beta s,\qquad
P=(p\ q)=\begin{pmatrix}\alpha&\beta\\ r&s\end{pmatrix},
\qquad \tau=\det P=\alpha s-\beta r.
\]

This run treats the active two-partner branch `tau != 0`. The `tau=0` branch has only one partner direction and belongs to the one-hub/escaped-curvature side.

The two physical partner coordinates seen by the independent scalar banks are

\[
\ell=P^TV=\binom{\ell_Y}{\ell_Z}
=\binom{\alpha S+rR}{\beta S+sR}.
\tag{2.1}
\]

Following r29, define

\[
u=(-r,\alpha)^T,\qquad v=(-s,\beta)^T,
\]

\[
T_Y=u^TCu,\qquad T_Z=v^TCv,\qquad U=u^TCv.
\tag{2.2}
\]

The r29 determinant identity is

\[
T_YT_Z-U^2=\tau^2\det C.
\tag{2.3}
\]

## 3. Main theorem — `QFORM-TRANSVERSE-U-IS-PARTNER-PLANE-CURVATURE-v1`

For `tau != 0`, the entire same-bank quadratic form `V^T C V` can be written in the two partner coordinates (2.1) as

\[
\boxed{
V^TCV
=\frac{1}{\tau^2}
\left(T_Z\ell_Y^2-2U\ell_Y\ell_Z+T_Y\ell_Z^2\right).
}
\tag{3.1}
\]

Equivalently, if

\[
K=P^{-1}CP^{-T},
\]
then

\[
\boxed{
K=\frac1{\tau^2}
\begin{pmatrix}
T_Z&-U\\
-U&T_Y
\end{pmatrix}.
}
\tag{3.2}
\]

In particular,

\[
\det K=\frac{\det C}{\tau^2},
\tag{3.3}
\]

and (2.3) is exactly the determinant identity for (3.2).

### Proof

Because `ell=P^T V` and `tau != 0`,

\[
V=P^{-T}\ell.
\]

Directly,

\[
P^{-T}=\frac1\tau
\begin{pmatrix}s&-r\\-\beta&\alpha\end{pmatrix}.
\]

Its first column is `(s,-beta)^T/tau=-v/tau`, and its second column is `(-r,alpha)^T/tau=u/tau`. Therefore

\[
P^{-1}CP^{-T}
=\frac1{\tau^2}
\begin{pmatrix}
v^TCv&-v^TCu\\
-u^TCv&u^TCu
\end{pmatrix},
\]
which is (3.2), hence (3.1). Taking determinants gives (3.3), and multiplying (3.3) by `tau^4` recovers (2.3). QED.

A symbolic exact check of the matrix identity and determinant residual was performed in this run; both residuals simplify identically to zero. The proof above is algebraic and does not depend on the finite check.

## 4. Consequence: full two-partner slicing freezes every r29 currency

Equation (3.1) gives a precise interpretation of the r29 currencies:

- `T_Z/tau^2` is the square coefficient along the first partner coordinate `ell_Y`;
- `T_Y/tau^2` is the square coefficient along the second partner coordinate `ell_Z`;
- `-U/tau^2` is the mixed coefficient **between the two partner coordinates themselves**.

Thus, once a proof conditions or slices on the full pair `ell=(ell_Y,ell_Z)`, all three quantities `T_Y,T_Z,U` have become a deterministic phase. No residual random coordinate remains on which this curvature can act.

This is stronger than the qualitative statement from r30 that “full scalar completion erases the third curvature.” It identifies exactly where the curvature went: it was not lost algebraically; it was converted into a quadratic function of the two partner values, and therefore disappears from every estimate that takes absolute values after fixing both partners.

## 5. Exact failure of the current two-hub transverse-block theorem on this packet

The current interactive Theorem 6.5 considers two hub coordinates and a light-coordinate partner map `M`, then splits the light coordinates into `I,J`. Its extra smoothing currency is

\[
F=\|A_R[I,J](I-\Pi_J)\|_F,
\tag{5.1}
\]
where `Pi_J` projects onto the row space of the restricted partner map `M_J`.

For the ratio packet, in the original independent coordinates of the first bank,

\[
M=P^T\Gamma^T,
\qquad
A_R=\Gamma C\Gamma^T.
\tag{5.2}
\]

Fix **any** coordinate split `I union J`. If `rank M_J<2`, the two-hub theorem cannot fire because its second partner singular value is zero. If `rank M_J=2`, then `P^T` is invertible and therefore

\[
\operatorname{row}(M_J)=\operatorname{row}(\Gamma_J^T).
\tag{5.3}
\]

But

\[
A_R[I,J]=\Gamma_I C\Gamma_J^T,
\tag{5.4}
\]
so every row of `A_R[I,J]` already lies in `row(Gamma_J^T)=row(M_J)`. Consequently

\[
\boxed{A_R[I,J](I-\Pi_J)=0}
\qquad\text{and hence}\qquad
\boxed{F=0.}
\tag{5.5}
\]

This holds for **every split** for which the partner map has rank two. Therefore the current two-hub cross-split theorem has no quantitative branch on this packet, no matter how large `|U|`, `|det C|`, or the r29 currency-compensation lower bound becomes.

This is an exact structural statement, not a small-parameter estimate.

## 6. Exact failure of a positive slice-profile hypothesis after full partner slicing

The same obstruction appears in the current two-hub slice theorem (interactive Theorem 6.4). Since `tau != 0`, fixing `ell=l` fixes

\[
V=P^{-T}l.
\]

Hence the light remainder

\[
R(X)=V^TCV
\]
is deterministic on each full partner slice:

\[
R\big|_{\ell=l}=l^TKl.
\tag{6.1}
\]

Thus, wherever the partner density is positive, the conditional/slice remainder law has an atom at `l^T K l`. No finite `K_b` can satisfy a positive-power interval estimate

\[
\mu_l(I)\le K_b |I|^b,\qquad b>0,
\tag{6.2}
\]
uniformly as intervals shrink around that atom. Therefore the positive `b` hypothesis of the two-hub slice theorem also fails maximally after the full two-dimensional partner slice.

Again, this does **not** refute that theorem and does **not** refute QFORM. It says only that the live ratio packet sits exactly at the theorem's rank-two logarithmic threshold if both partner variables are frozen before the same-plane quadratic phase is used.

## 7. The precise missing factor

The correct remaining coarea/Fourier interface is now sharper:

`QFORM-TWISTED-TWOHUB-PARTNER-PLANE-TRACE-v1`:

> Obtain an `O(epsilon)` interval bound for the ratio packet while retaining the phase
>
> \[
> \tau^{-2}(T_Z\ell_Y^2-2U\ell_Y\ell_Z+T_Y\ell_Z^2)
> \]
>
> **before** taking absolute values or slicing on both partner coordinates. In the mixed-cancellation chamber, the key currency is the moving mixed slope `-2U ell_Y/tau^2` (or symmetrically `-2U ell_Z/tau^2`) visible after slicing only one partner coordinate. A full two-partner slice freezes it and necessarily returns to the logarithmic rank-two threshold.

This identifies the exact additional factor missing from the r29/r30 half-Riesz splice: not another determinant of `C`, and not a cross-split Frobenius norm (which is identically zero here), but a **partial-slice estimate that keeps one partner coordinate random while spending the same-plane mixed coefficient `U` jointly with the second independent scalar bank**.

If `tau` collapses, this normal form is not the right receiver; that branch returns to the one-partner/escaped-curvature mechanism already isolated in earlier work.

## 8. Designated account04/B05 result applied to an actual branch

The completed designated partner result

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f`

proves

\[
\|p_Q\|_\infty<51.6(\mu m_*)^{-1/3}.
\tag{8.1}
\]

Therefore the concrete exact-slope branch

\[
\mu\ge1,\qquad m_*\ge\frac18
\]

is already closed by

\[
\boxed{\|p_Q\|_\infty<103.2.}
\tag{8.2}
\]

The new theorem addresses the complementary genuinely two-partner diffuse branch: it explains why the large `U` forced by r29 cannot simply be fed into the present two-hub slice or cross-split theorems.

As a consistency check, the completed account02/B05 localized double-zero theorem at

`yspennstate/math-open-problems@fcb8ba61036bee6535de7b0fb0077bb07d76bea6`

closes the earlier target-valid stress example by a different completion order. That is consistent with this report: the obstruction is to **full two-partner slicing as a universal interface**, not to boundedness of the actual target law.

## 9. Scope and next action

No Gaussianity, log-concavity, moments, compact support, connected support, post-rotation independence, arbitrary-joint coarea, conditional density-cap assumption, or law-uniform pointwise oscillatory decay was used.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**.

The next B05 mathematical step should attack a one-partner-at-a-time coarea/Fourier inequality in the exact partner-plane normal form (3.1), with `U` retained as a moving slope. A proof that first conditions on both `ell_Y` and `ell_Z`, or that attempts to invoke a transverse cross-split remainder norm, has now been ruled out algebraically for this packet.
