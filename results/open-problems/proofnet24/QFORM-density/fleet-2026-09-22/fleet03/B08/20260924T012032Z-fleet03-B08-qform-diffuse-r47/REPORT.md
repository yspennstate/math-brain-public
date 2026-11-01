SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-24T01:20:32Z.
attacking: the r46 cancelled-twist / singular-carrier endpoint by a product-safe triangular shear that turns an opposite-sign physical diagonal twist into a genuine second hub and exposes a two-row diffuse Fresnel arm.

# fleet03/B08 r47 — rank-one aligned cancelled twist -> two-hub shear receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / quantitative inequalities and rigorous computation  
Run: `20260924T012032Z-fleet03-B08-qform-diffuse-r47`  
Status: **NEW SUPPORTING THEOREM / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN. This report proves a new end-to-end estimate for the singular aligned-carrier state left by fleet03/B08 r46. The argument never rotates the random product coordinates. It uses a triangular translation of one ORIGINAL coordinate, whose conditional density remains bounded by one, and then applies the already-proved two-hub Fresnel/Brascamp-Lieb theorem in the remaining ORIGINAL light coordinates. No moment, support, log-concavity, connectedness, Gaussianity, or post-rotation independence assumption is used.

## 1. Source boundary


The analytic source actually used is the proved Theorem H (hub coordinates) in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

For two ORIGINAL hub coordinates and a diagonal light block, if the two-row physical hub-to-light arm `C` has full row rank and every normalized physical row leverage is at most `1/2`, Theorem H gives

\[
 |\phi_Q(t)|\le 4\pi^2 |t|^{-2}\,\det(CC^T)^{-1/2}.
\]

Integrating `min(1, RHS)` gives

\[
\boxed{\|p_Q\|_\infty\le 4\,\det(CC^T)^{-1/4}},\qquad p_Q\in C_0(\mathbb R).
\tag{1.1}
\]

Arbitrary hub self-curvature, arbitrary conditioned outside coordinates/couplings, affine terms, and arbitrary physical diagonal light curvature are retained.

The inherited r46 state is

\[
 A=\begin{pmatrix}
 B&M\\
 M^T&M^TRM+D
 \end{pmatrix},
\tag{1.2}
\]

with two ORIGINAL hub coordinates, `M in R^{2 x m}` of row rank two, symmetric `R`, and physical diagonal `D=diag(d_1,...,d_m)`. r46 paid the `det R != 0` non-cancelled pivot branch and left the singular carrier / cancelled-twist endpoint.

## 2. Rank-one singular carrier normal form

Assume now

\[
 R=\lambda rr^T,\qquad \lambda\ne0,\qquad \|r\|_2=1,
\tag{2.1}
\]

and put

\[
 w=M^Tr,\qquad G=MM^T,\qquad
 \ell_j=m_j^TG^{-1}m_j,\qquad \mu=\max_j\ell_j,
\tag{2.2}
\]

where `m_j` is the `j`th physical arm column. Write the actual physical light diagonal coefficient

\[
 a_j=d_j+\lambda w_j^2.
\tag{2.3}
\]

The rank-one common-plane curvature is `lambda w w^T`. The difficult state is that a large physical twist `d_j` is nearly cancelled by this common-plane diagonal, so `a_j` is small or zero.

## 3. Main theorem

### Theorem `QFORM-RANK1-ALIGNED-CANCELLED-TWIST-SHEAR-v1`

In (1.2)-(2.3), suppose

\[
\mu\le \frac13
\tag{3.1}
\]

and for some physical light coordinate `j`

\[
 d_j\ne0,\qquad |a_j|\le\theta |d_j|,
 \qquad 0\le\theta<1.
\tag{3.2}
\]

Let `s_2(M)>0` be the smaller singular value of the actual two-row arm. Then the full quadratic form for every cap-one product input has a continuous `C_0` density and

\[
\boxed{
 \|p_{X^TAX}\|_\infty
 \le
 4(1-\theta)^{-1/4}\bigl(|d_j|\,s_2(M)\bigr)^{-1/2}.
}
\tag{3.3}
\]

More precisely, without replacing the exact geometry by (3.1), one obtains a physical two-hub arm `C_j` satisfying

\[
\sqrt{\det(C_jC_j^T)}
\ge
\frac1{\sqrt2}\sqrt{-\lambda d_j}\,
\sqrt{\det(MM^T)}\sqrt{1-\ell_j},
\tag{3.4}
\]

and its physical row leverages agree exactly with the row leverages of the deleted arm `M_{-j}`. Therefore (1.1) applies whenever those deleted-arm leverages are at most `1/2`.

### Proof

Because `|a_j|<|d_j|`, the two summands in (2.3) cannot have the same sign. Hence

\[
\boxed{\lambda d_j<0.}
\tag{3.5}
\]

Condition on all outside coordinates and on one of the two original hub coordinates; these operations preserve the remaining original-coordinate product law and only create affine terms. We shall choose which original hub remains after the algebra below.

Write the selected physical light coordinate as `z=X_j`, the other light coordinates as `y=X_{-j}`, and

\[
 V=w_{-j}^Ty.
\]

The part of the light quadratic polynomial involving the common-plane rank-one term and the physical diagonal is

\[
 a_j z^2+2\lambda w_j zV+\lambda V^2
 +\sum_{k\ne j}d_k y_k^2.
\tag{3.6}
\]

Choose a real number `alpha` solving

\[
 a_j\alpha^2-2\lambda w_j\alpha+\lambda=0.
\tag{3.7}
\]

This equation has a real solution precisely because its discriminant is

\[
4(\lambda^2w_j^2-a_j\lambda)
=4\lambda(\lambda w_j^2-a_j)
=-4\lambda d_j>0.
\tag{3.8}
\]

If `a_j != 0`, one may take

\[
 \alpha=\frac{\lambda w_j+\sqrt{-\lambda d_j}}{a_j}.
\tag{3.9}
\]

If `a_j=0`, necessarily `w_j != 0` and the finite root is

\[
 \alpha=\frac1{2w_j}.
\tag{3.10}
\]

Make the triangular change

\[
 z=z'-\alpha V.
\tag{3.11}
\]

It has Jacobian one. The original density factor `f_j(z)` becomes
`f_j(z'-alpha V)`, which is still pointwise at most one. The other light coordinates keep their original independent product density. This is the only sense in which a shear is used; no claim of post-shear independence is made.

By (3.7), the `V^2` coefficient cancels exactly. The remaining mixed coefficient is

\[
 \gamma:=\lambda w_j-a_j\alpha,
\]

and (3.7) gives the exact identity

\[
 \boxed{\gamma^2=-\lambda d_j.}
\tag{3.12}
\]

Thus (3.6) becomes

\[
 a_j(z')^2+2\gamma z'\,w_{-j}^Ty
 +\sum_{k\ne j}d_k y_k^2.
\tag{3.13}
\]

The common-plane square has disappeared completely from the remaining light-light block: that block is now diagonal.

Let the two rows of `M` be `m_1^T,m_2^T`. The conditioned-away original hub contributes only affine terms. Keep the original hub `p` chosen as follows. If `|r_2|>=|r_1|`, keep hub `p=1`; otherwise keep hub `p=2`. In both cases the coefficient of the *other* arm row in `w=r_1m_1+r_2m_2` has modulus at least `1/sqrt(2)`.

After the shear, the two genuine hub variables are `z'` and the retained original hub. Their physical arm into `y` is

\[
 C_j=
 \begin{pmatrix}
 \gamma w_{-j}^T\\
 m_{p,-j}^T-\alpha m_{p,j}w_{-j}^T
 \end{pmatrix}.
\tag{3.14}
\]

All hub-hub curvature is arbitrary and therefore admissible in Theorem H. The light block is the diagonal matrix `diag(d_k:k != j)`.

Suppose first `p=1`. Relative to the two deleted-arm rows `(m_{1,-j},m_{2,-j})`, the coefficient matrix in (3.14) has determinant `-gamma r_2`; if `p=2`, it has determinant `gamma r_1`. Therefore, with `r_perp` denoting the selected opposite coefficient,

\[
\boxed{
 \sqrt{\det(C_jC_j^T)}
 =|\gamma|\,|r_{\perp}|\,
 \sqrt{\det(M_{-j}M_{-j}^T)}.
}
\tag{3.15}
\]

The matrix determinant lemma gives

\[
 \det(M_{-j}M_{-j}^T)
 =\det(G)(1-\ell_j).
\tag{3.16}
\]

Since `|r_perp|>=1/sqrt(2)` and `|gamma|=sqrt(-lambda d_j)`, equations (3.15)-(3.16) prove (3.4).

The row transformation from `M_{-j}` to `C_j` is invertible, so

\[
 \operatorname{row}(C_j)=\operatorname{row}(M_{-j}).
\tag{3.17}
\]

Hence the normalized physical row leverages are identical. Sherman-Morrison gives, for every `k != j`,

\[
 \ell_k^{(-j)}
 \le \frac{\ell_k}{1-\ell_j}
 \le \frac{\mu}{1-\mu}
 \le\frac12.
\tag{3.18}
\]

Thus Theorem H applies to the sheared integral. The light-dependent translation in the `z` density does not alter its proof: after the Jacobian-one change, the proof uses only the pointwise hub cap `f_j(z'-alpha V)<=1`; the remaining `y` density is still the original product density. From (1.1),

\[
 \|p_Q\|_\infty
 \le 4\,[\sqrt{\det(C_jC_j^T)}]^{-1/2},
\tag{3.19}
\]

and the characteristic function has an integrable `|t|^{-2}` majorant, so `p_Q in C_0`.

It remains to obtain the scale-transparent inequality (3.3). From (3.2),

\[
 |\lambda|w_j^2=|a_j-d_j|\ge(1-\theta)|d_j|.
\tag{3.20}
\]

The leverage identity implies the operator inequality

\[
 m_jm_j^T\preceq \ell_j MM^T,
\]

so, because `||r||=1`,

\[
 |w_j|=|r^Tm_j|\le\|m_j\|_2
 \le \sqrt{\mu}\,s_1(M).
\tag{3.21}
\]

Combining (3.20)-(3.21),

\[
 \sqrt{-\lambda d_j}
 \ge
 \frac{\sqrt{1-\theta}\,|d_j|}
      {\sqrt\mu\,s_1(M)}.
\tag{3.22}
\]

Using (3.4), `sqrt(det(MM^T))=s_1(M)s_2(M)`, and `1-ell_j>=1-mu`, we obtain

\[
\sqrt{\det(C_jC_j^T)}
\ge
 |d_j|s_2(M)
 \sqrt{\frac{(1-\theta)(1-\mu)}{2\mu}}.
\tag{3.23}
\]

For `mu<=1/3`, the last square-root is at least `sqrt(1-theta)`. Substitution in (3.19) is exactly (3.3). QED.

## 4. Concrete inherited-scale consequence

The theorem consumes a substantial part of r46's cancelled-twist debt without any `det R` denominator. For example, in the rank-one carrier state, if

\[
 \mu\le\frac13,\qquad
 |d_j|\ge\frac{L}{128},\qquad
 |a_j|\le\frac12|d_j|,\qquad
 s_2(M)\ge\frac L8,
\tag{4.1}
\]

then

\[
\boxed{
 \|p_Q\|_\infty
 \le \frac{4\,2^{1/4}\sqrt{1024}}{L}
 <\frac{152.219}{L},
 \qquad p_Q\in C_0(\mathbb R).
}
\tag{4.2}
\]

This is exactly the regime where r46's scalar physical pivot may be almost zero. The triangular shear turns that cancellation into a second genuine hub and pays it by integrated Fourier decay rather than by dividing by the cancelled pivot.

The remaining rank-one singular-carrier obstruction is now quantitatively anisotropic: after excluding localized arm leverage, a near-cancelled large twist can evade (4.2) only by having `s_2(M)<L/8` (or by falling outside the large-twist threshold). That is a much sharper successor than `det R=0` by itself.

## 5. Target-valid diffuse stress family

For every `L>0`, take six physical light coordinates and two original hubs. Let

\[
 m_1=\frac{L}{\sqrt3}(1,1,1,0,0,0),\qquad
 m_2=\frac{L}{\sqrt3}(0,0,0,1,1,1),
\]

so `M=[m_1;m_2]` has singular values exactly `L,L` and every physical arm leverage is exactly `1/3`. Put

\[
 B=0,\qquad
 R=L^{-1}e_1e_1^T,\qquad
 D=\operatorname{diag}(-L/3,0,0,0,0,0).
\tag{5.1}
\]

For `j=1`, `w=M^Te_1=m_1^T`, so

\[
 a_1=-L/3+L^{-1}(L/\sqrt3)^2=0.
\]

The matrix decomposes into two independent deterministic coordinate sectors. The sector consisting of hub 2 and light coordinates 4,5,6 is the pure star

\[
\begin{pmatrix}0&m_2\\m_2^T&0\end{pmatrix},
\]

which has eigenvalues `+L,-L,0,0`. In the other sector, with `u=(1,1,1)/sqrt3`, the unit vector `(1,u)/sqrt2` has Rayleigh quotient

\[
 L\left[1+\frac12\left(1-\frac19\right)\right]
 =\frac{13}{9}L.
\]

Therefore the full matrix has at least three eigenvalues of modulus at least `L`: `+L`, `-L`, and one positive eigenvalue at least `13L/9`. At `L=1` this is an exact target-class family.

The new theorem gives the dimension-free estimate

\[
\boxed{\|p_Q\|_\infty\le \frac{4\sqrt3}{L}<\frac{6.929}{L}.}
\tag{5.2}
\]

Using the exact shear arm instead of the worst-case `mu<=1/3` simplification improves this family to

\[
 \sqrt{\det(C_jC_j^T)}=\frac{\sqrt2}{3}L^2,
\]

hence

\[
\boxed{
 \|p_Q\|_\infty
 \le \frac{4\sqrt{3/\sqrt2}}{L}
 <\frac{5.826}{L}.
}
\tag{5.3}
\]

This family is useful because the actual light diagonal at the selected physical coordinate is cancelled exactly, `R` has rank one, and the original arm is diffuse at the sharp `1/3` threshold of the theorem.

## 6. Designated fleet04/B08 partner applied

The designated partner result was reread at

`yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B08/20260923T212412Z-fleet04-B08-QFORM-r2/REPORT.md`,
Theorem `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1`.

Apply it to the same physical twist coordinate `j` used above. Write the full matrix after moving this ORIGINAL coordinate first as

\[
 A=\begin{pmatrix}a&b^T\\b&C\end{pmatrix}.
\]

If the deletion child `C` has three eigenvalues of modulus at least `L/64` and its spectral projection onto `|lambda(C)|>=L/4096` has every physical leverage at most `1/32`, then the partner theorem gives the actual full-form inequality

\[
\boxed{
 \|p_Q\|_\infty
 \le \frac{288\sqrt{3e}}{13(L/64)}
 <\frac{4096}{L},
 \qquad p_Q\in C_0(\mathbb R).
}
\tag{6.1}
\]

The scalar `a`, the entire star `b`, the rank-one common-plane carrier, all signs, and all additional child coefficients are retained by conditioning only on the original coordinate `X_j`.

Thus the new shear theorem and the designated partner theorem give a clean split on the r46 singular-carrier state: a moderately isotropic cancelled twist is paid directly by (3.3)/(4.2); regardless of that shear currency, a deletion child that remains three-dimensional and diffuse is paid by (6.1). Any survivor must therefore exhibit either strong arm anisotropy, child spectral loss, or a high-leverage child window.

## 7. Regression checks

A seeded 5000-instance numerical algebra check verifies:

1. the shear coefficient identity `a alpha^2-2 lambda w_j alpha+lambda=0`;
2. `gamma^2=-lambda d_j`;
3. the exact area identity (3.15);
4. equality of the physical row-leverage vectors of `C_j` and `M_{-j}`;
5. the target-family arm singular values/leverage and the claimed target spectrum numerically.

The largest floating residuals in deliberately unconditioned random matrices were approximately `6.6e-12` for the cancelled `V^2` coefficient and `2.5e-8` relative for the area/leverage identities (the latter occurs only in nearly singular sampled matrices). These are regression checks, not proof substitutes; the identities above are exact algebra.

## 8. What remains

The unrestricted conjecture and global continuity remain OPEN. The first B08 successor is now

`QFORM-RANK1-CANCELLED-TWIST-ANISOTROPIC-OR-CHILDLOCALIZED-v1`:

> In the aligned rank-one carrier state, consume the survivor with a large near-cancelled physical twist but `s_2(M)<<L`, or consume the designated-partner failure in which deletion loses the third spectral direction / produces a high-leverage child window. The route must retain the full same-bank diagonal and common-plane carrier and must not infer a bounded arm anisotropy ratio from the three-eigenvalue hypothesis.

This run deliberately does not claim that the target hypothesis forces `s_2(M)>=cL`; the existing correction boundary contains anisotropic counterexamples to analogous shortcuts. It also does not claim a full solution from the target-valid family in Section 5.
