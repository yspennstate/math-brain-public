SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-24T09:33:25Z.
attacking: the global-null localized packet by deleting one ORIGINAL hub coordinate, then aggregating the exact tail-plane Pluecker/Gram volume before any reciprocal minor and routing the retained three-dimensional child immediately to a diffuse product theorem.

# fleet03/B06 r57 — global-null tail-plane compiler and one-shot diffuse-child exit

Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`.  
Immediate B06 inputs: r55 `QFORM-GLOBALNULL-PHYSICAL-DELETION-v1` and `QFORM-APPROXNULL-PRINCIPAL-RETENTION-v1`, current-master path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260924T082141Z-fleet03-B06-qform-r55/REPORT.md`; r56 kernel-area/global-null certificates, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260924T090040Z-fleet03-B06-qform-r56/REPORT.md`.  
Diffuse analytic input: `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.  
Designated partner actually applied in Section 7: fleet04/B06 `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`, current source path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B06/20260924T001014Z-fleet04-B06-QFORM-r3/REPORT.md`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full QFORM conjecture remains OPEN. The result below closes a large part of the **exact global-null endpoint inside the localized rank-three packet** without another near-null deletion. The new mechanism is: global null forces the entire tail carrier into a two-plane; deleting one original hub then has an exact determinant equal to a weighted sum of one-tail and two-tail Pluecker mass; if the resulting physical three-frame is diffuse, the existing separable-phase theorem pays the full scalar output. No unrestricted fiber supremum and no post-rotation independence is used.

## 1. Exact localized packet and the first missing implication

Work in the localized packet inherited from r53--r56:

\[
A=[I_3\ Z]^T B[I_3\ Z]+\operatorname{diag}(D_H,\Delta),
\tag{1.1}
\]

where `B=B^T` is an **invertible** real `3 x 3` matrix, `D_H` is diagonal on the three literal hub coordinates, `Delta` is arbitrary diagonal on the tail coordinates, and `Z=(z_1 ... z_m)` is `3 x m`. Thus the actual hub block is

\[
F=B+D_H.
\tag{1.2}
\]

Suppose one of the exact singular-hub branches from r54/r56 has reached an actual global null vector supported on these three literal hubs:

\[
A\binom w0=0,
\qquad w\ne0.
\tag{1.3}
\]

The r55 theorem already shows how to delete one original hub product-preservingly and retain the third singular value. The missing point was to identify what the null certificate forces on the complete tail geometry and to spend it **before** another deletion can lose scale.

## 2. `QFORM-GLOBALNULL-TAILPLANE-RANKDROP-v1`

From (1.1)--(1.3),

\[
Fw=0,
\qquad Z^TBw=0.
\tag{2.1}
\]

Put

\[
u:=Bw=-D_Hw.
\tag{2.2}
\]

Because `B` is invertible and `w!=0`,

\[
\boxed{u\ne0.}
\tag{2.3}
\]

Equation (2.1) then becomes

\[
\boxed{Z^Tu=0.}
\tag{2.4}
\]

Hence every tail carrier column lies in the fixed physical two-plane `u^perp`:

\[
\boxed{\operatorname{rank}Z\le2.}
\tag{2.5}
\]

This is the first new structural implication. The exact hub-supported global null does not merely remove one spectral direction: inside the localized rank-three representation it collapses the **entire tail core** to a two-dimensional spectral fiber.

Normalize `w` to unit length and choose a literal hub coordinate `i` with

\[
\alpha:=|w_i|=\max_h|w_h|\ge1/\sqrt3.
\tag{2.6}
\]

Let `J={1,2,3}\setminus{i}`. By r55 `QFORM-GLOBALNULL-PHYSICAL-DELETION-v1`, conditioning on the ORIGINAL coordinate `X_i=t` translates the remaining independent coordinates but preserves their density caps, and the conditional quadratic matrix is the principal child

\[
C_i=A[i^c,i^c].
\tag{2.7}
\]

If the parent satisfies the target spectral hypothesis `s_3(A)>=1`, then

\[
\boxed{s_3(C_i)\ge\alpha^2s_3(A)\ge1/3.}
\tag{2.8}
\]

No rotation of random variables occurs.

## 3. Exact child carrier and its weighted Pluecker determinant

Let `e_1,e_2,e_3` be the standard basis of `R^3`, and form the complete child carrier

\[
L_i=[e_j\ e_k\ Z]\in\mathbb R^{3\times(m+2)},
\qquad \{j,k\}=J.
\tag{3.1}
\]

Then

\[
\boxed{
C_i=D_i+L_i^TBL_i,
}
\tag{3.2}
\]

where

\[
D_i=\operatorname{diag}((D_H)_{jj},(D_H)_{kk},\Delta_1,\ldots,\Delta_m).
\tag{3.3}
\]

All linear terms created by conditioning are coordinate-separable and will be retained by the diffuse theorem.

Put

\[
G_i=L_iL_i^T=e_je_j^T+e_ke_k^T+ZZ^T.
\tag{3.4}
\]

When `rank Z=2`, let

\[
n=u/\|u\|,
\qquad
W_Z=\operatorname{pdet}_+(ZZ^T)
=\sum_{a<b}\|z_a\times z_b\|^2.
\tag{3.5}
\]

Since all `z_a` lie in `n^perp`, each cross product `z_a x z_b` is parallel to `n`. Cauchy--Binet for the `3 x (m+2)` matrix `L_i` therefore gives the exact identity

\[
\boxed{
\det G_i
=\|Z^Te_i\|_2^2+(1-n_i^2)W_Z.
}
\tag{3.6}
\]

Indeed the three-column minors using both physical hub columns are

\[
\det(e_j,e_k,z_a)^2=(z_a)_i^2,
\]

while the minors using one physical hub and two tail columns sum to

\[
(n_j^2+n_k^2)W_Z=(1-n_i^2)W_Z,
\]

and every three-tail minor vanishes because `rank Z<=2`.

If `rank Z<=1`, put `W_Z=0`; the same Cauchy--Binet argument gives

\[
\boxed{\det G_i=\|Z^Te_i\|_2^2.}
\tag{3.7}
\]

Thus (3.6)--(3.7) are an exact **aggregate-before-inversion** replacement: the child three-volume is the sum of all one-tail and two-tail physical Pluecker contributions. No individual tail minor is selected or inverted.

A useful consistency identity is

\[
\sum_{i=1}^3\det G_i
=\|Z\|_F^2+2W_Z
\qquad(\operatorname{rank}Z=2),
\tag{3.8}
\]

because `sum_i(1-n_i^2)=2`.

## 4. `QFORM-GLOBALNULL-DIFFUSE-CHILD-COMPILER-v1`

Assume `G_i` is positive definite. Define

\[
U_i=L_i^TG_i^{-1/2},
\qquad
K_i=G_i^{1/2}BG_i^{1/2}.
\tag{4.1}
\]

Then `U_i` has three orthonormal columns and

\[
C_i=D_i+U_iK_iU_i^T,
\qquad
|\det K_i|=|\det B|\det G_i.
\tag{4.2}
\]

For each surviving original coordinate `q`, let `ell_q` be its physical three-frame leverage,

\[
\ell_q=(L_i)_{:,q}^TG_i^{-1}(L_i)_{:,q}.
\tag{4.3}
\]

Then `sum_q ell_q=3`. If

\[
\boxed{\max_q\ell_q\le1/2,}
\tag{4.4}
\]

the completed `QFORM-DIFFUSE-SEPARABLE-PHASE-v1` theorem applies **conditionally on the deleted original coordinate**. It allows the whole diagonal `D_i`, every conditioning-induced linear term, and arbitrary translations of the cap-one coordinate laws. Its characteristic-function majorant is uniform in the conditioning value. Consequently averaging the conditional characteristic functions preserves the same integrable envelope and the original full scalar output has a continuous `C_0` density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le3e\,[|\det B|\det G_i]^{-1/3}.
}
\tag{4.5}
\]

Using the exact weighted currency from Section 3, in the rank-two-tail case

\[
\boxed{
\|p_Q\|_\infty
\le3e\,|\det B|^{-1/3}
\Bigl[\|Z^Te_i\|_2^2+(1-n_i^2)W_Z\Bigr]^{-1/3}.
}
\tag{4.6}
\]

This is a target-level implication in its stated localized/global-null/diffuse-child scope. The curved/product geometry is paid jointly through the full Gram/Pluecker volume rather than through a fiber maximum.

## 5. One-shot universal payment when the child diagonal is small

The preceding formula still contains the carrier determinant. The retained target spectrum from (2.8) removes that denominator whenever the physically diagonal child part is small.

Assume

\[
\|D_i\|_{op}\le1/6.
\tag{5.1}
\]

Set `S_i=L_i^TBL_i=U_iK_iU_i^T`. Weyl's singular-value inequality and (2.8) give

\[
s_3(S_i)
\ge s_3(C_i)-\|D_i\|_{op}
\ge1/3-1/6
=1/6.
\tag{5.2}
\]

Hence `S_i` has rank three, so `G_i` is automatically positive definite. The three nonzero singular values of `S_i` are exactly those of `K_i`, and therefore

\[
|\det K_i|\ge(1/6)^3=1/216.
\tag{5.3}
\]

Under the same diffuse leverage gate (4.4), (4.5) now yields the **universal** full-scalar bound

\[
\boxed{
\|p_Q\|_\infty\le18e
=48.9290729123\ldots .
}
\tag{5.4}
\]

The density is continuous and vanishes at infinity. This pays the exact global-null packet in one shot; there is no repeated principal-child deletion and hence no accumulation of the `1/3` spectral factor.

If `G_i` is singular, then `rank S_i<=2`, and Weyl gives directly

\[
\boxed{\|D_i\|_{op}\ge s_3(C_i)\ge1/3.}
\tag{5.5}
\]

Thus singular child carrier cannot occur in the small-diagonal chamber.

## 6. What remains when the universal exit fails

The exact global-null localized packet is now reduced to a finite/coordinate-separable obstruction. For the maximal null coordinate `i`, at least one of the following holds:

1. **paid diffuse child:** `max ell_q<=1/2` and `||D_i||op<=1/6`, giving the continuous bound `18e`;
2. **literal diagonal certificate:** `||D_i||op>1/6`; hence at least one surviving original coordinate has physical diagonal perturbation of magnitude `>1/6`;
3. **finite heavy-frame certificate:** `max ell_q>1/2`. Since `sum_q ell_q=3`, there are at most five original coordinates with `ell_q>1/2`;
4. if `G_i` is singular, the stronger diagonal certificate `||D_i||op>=1/3` holds by (5.5).

This is sharper than allowing another near-null deletion. The remaining problem is to compile the literal large diagonal or the at-most-five heavy-frame coordinates with the retained `s_3(C_i)>=1/3` without losing the full same-bank curvature.

## 7. Actual designated partner application

The freshest completed fleet04/B06 theorem is `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`. Here is a genuine application on the current global-null tail-plane geometry.

Take the rank-two-tail subbranch, condition on the two surviving literal hub coordinates, and additionally suppose the tail diagonal perturbation is zero on this scoped subbranch. The tail quadratic matrix is then

\[
T_Z=Z^TBZ,
\tag{7.1}
\]

of rank at most two. Suppose it has rank two, with nonzero eigenvalues `lambda_1,lambda_2` and orthonormal physical tail eigenvectors `w,v`. The hub conditioning creates only a tail linear statistic in `range(Z^T)=span{w,v}`, so it is exactly tangential shared leakage. If

\[
\max_a(w_a^2+v_a^2)\le1/2,
\tag{7.2}
\]

the partner theorem applies after completing the `v` square. A determinant-one output shear `(l,y)->(l,y-lambda_1 l^2-\text{affine}(l))` removes the `L`-only part without changing two-dimensional Lebesgue measure. Therefore, on the actual off-fold event `|V-v_*|>r`, the two-output section obeys

\[
\boxed{
\|g_r\|_\infty\le\frac4{|\lambda_2|r}.
}
\tag{7.3}
\]

At `r=1/64`,

\[
\boxed{
\|g_{1/64}\|_\infty\le\frac{256}{|\lambda_2|}.
}
\tag{7.4}
\]

This is an actual completed-partner inequality on the present tail-plane geometry. Its scope is a continuous `C_0` **two-output off-fold section**; it is not promoted to a full scalar bound through an arbitrary same-tail diagonal perturbation, which lies outside the partner theorem.

## 8. Deterministic checks

A fixed-seed numerical checker generated random invertible symmetric `B`, random unit `w`, chose `D_H` so `(B+D_H)w=0`, and generated arbitrary tail columns in `(Bw)^perp`. Over 10,000 admissible instances it checked (2.1), (2.4), and (3.6). The largest normalized discrepancy in (3.6) was approximately `1.70e-14`. This is only a finite algebraic diagnostic; the proof is Cauchy--Binet and the exact null equations above.

## 9. Status and next precise debt

New proved supporting claims:

- `QFORM-GLOBALNULL-TAILPLANE-RANKDROP-v1`: a hub-supported global null in the invertible localized rank-three packet forces `rank Z<=2`;
- `QFORM-GLOBALNULL-TAILPLANE-PLUCKER-GRAM-v1`: after deleting one original hub, the exact child carrier volume is (3.6)--(3.7), aggregating the whole tail bank before inversion;
- `QFORM-GLOBALNULL-DIFFUSE-CHILD-COMPILER-v1`: the diffuse child has the continuous bound (4.5)--(4.6);
- `QFORM-GLOBALNULL-SMALLDIAG-UNIVERSAL-v1`: if additionally `||D_i||op<=1/6`, the full scalar density is continuous and bounded by `18e`.

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains OPEN, although the paid diffuse-child branch here has a continuous `C_0` density.

The next exact B06 debt is `QFORM-GLOBALNULL-HEAVY5-OR-LARGEDIAG-CURVED-COMPILER-v1`: consume the at-most-five `>1/2` child-frame coordinates or the literal `>1/6` diagonal certificate together with `s_3(C_i)>=1/3`, while retaining the entire two-plane tail core and arbitrary diagonal tail phase. The goal is a finite physical-hub/curved-bank receiver, not another scale-losing null deletion.
