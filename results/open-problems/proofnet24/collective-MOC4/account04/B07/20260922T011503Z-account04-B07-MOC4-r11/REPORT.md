# MOC4 account04/B07 r11 — Spin(6) block realization of the shared mixed-minor constraint

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** account04/B07  
**Assignment:** representation-theoretic / exterior-algebra attack on the shared mixed-minor constraint, without assuming a false positive common permutation lift  
**Candidate/result:** `MOC4-SPIN6-BLOCK-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; the unrestricted MOC4 target remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact inherited state used

The target is: for every pair of complex normal 4-by-4 matrices with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in \operatorname{conv}\left\{
 v_\sigma:=\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}.
\tag{MOC4}
\]

No invertibility or simple-spectrum assumption is made in this report.

I read the team lead's latest complete version, account03/B07 run `20260922T010550Z-account03-B07-MOC4-r11b`, candidate `MOC4-DRURY-UPPER-FACET-v1`. It reduces the support problem to Drury's single exceptional Saxl-facet orbit and proves that arbitrary nonnegative functions in the 13-dimensional identity-vanishing endpoint space are too large a cone: the campaign's rational orthogonal witness has negative determinantal-quasidistribution expectation `-224/15625` on one such nonnegative separator.

I also directly consume the named OTHER-account partner result account01/B08 run `20260922T003726Z-b08-moc4-r11`. Its exact signed common-minor lift reproduces every compound-minor marginal from one unitary and reduces any target-level counterexample to the upper Drury-facet obstruction; it explicitly preserves the fact that the common lift is signed rather than positive.

The mixed-minor coordinates used below are from account01/B07 `MOC4-MIXED-ASSIGNMENT-v1`. After `A=diag(a)` and `B=U diag(b)U*`, write

\[
p_{ij}=|u_{ij}|^2,
\qquad q_{S,T}=|\det U[S,T]|^2.
\]

For the three complementary pair classes, take

\[
S_1=T_1=12,\quad S_2=T_2=13,\quad S_3=T_3=14,
\]

and define

\[
r_{\alpha\beta}=q_{S_\alpha,T_\beta}+q_{S_\alpha,T_\beta^c},
\qquad
 d_{\alpha\beta}=q_{S_\alpha,T_\beta}-q_{S_\alpha,T_\beta^c}.
\tag{1}
\]

Let `P=(p_ij)`, `R=(r_{alpha beta})`, `D=(d_{alpha beta})`, and let

\[
H=\frac12\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}.
\]

The exact account01/B07 identity is

\[
HPH^T=\begin{pmatrix}1&0\\0&D\end{pmatrix}.
\tag{2}
\]

Its remaining support inequality has the form

\[
\langle P,C\rangle+\frac12\langle R,X\rangle
\le
\max_{\sigma\in S_4}\left\{
\sum_i C_{i,\sigma(i)}+rac12\sum_{\alpha=1}^3
X_{\alpha,\rho_\sigma(\alpha)}
\right\},
\tag{MI}
\]

where `(C,X)` is the structured coefficient pair determined by `(a,b,eta)` for the chosen support direction. Account04/B09 proved that `(P,R)` need not lie in the convex hull of the 24 coupled permutation pairs, so `(MI)` cannot be replaced by an unrestricted positive joint-lift assertion.

Primary-source/status references retained from the campaign source check and the lead report are S. W. Drury, *The external vertices conjecture in case n=4*, ELA 11 (2004), DOI `10.13001/1081-3810.1131`; N. Bebiano--J. P. da Providencia, *Revisiting the Marcus-de Oliveira Conjecture*, Mathematics 13 (2025), 711, DOI `10.3390/math13050711`; and J. I. Mulero-Martinez, LAA 740 (2026), 19-38, DOI `10.1016/j.laa.2026.03.019`. None is treated as a proof of full MOC4.

## 2. Conditional end-to-end route and the exact missing object

A complete proof follows once `(MI)` is established for every **actual common unitary**. The important point is that the actual feasible set is much smaller than arbitrary doubly stochastic `P,R`, but the needed extra structure must be derived rather than asserted.

The result below gives an exact representation-theoretic realization of that common-unitary structure. It turns `(P,R)` into two block invariants of one real orthogonal 6-by-6 matrix. The previously known scalar bounds become local shadows of a system of exact 2-by-2 matrix orthogonality equations.

## 3. The `SU(4) -> SO(6)` exterior-square realization

Multiplying `U` by a scalar unit phase does not change `U diag(b)U*`. Choose the phase so that `det U=1`.

Let

\[
V=\Lambda^2\mathbb C^4.
\]

For `xi,zeta in V`, define the complex symmetric bilinear form `Q` by

\[
\xi\wedge\zeta=Q(\xi,\zeta)e_{1234}.
\tag{3}
\]

Because `det U=1`, the operator `C_2(U)=\Lambda^2U` preserves `Q`; because `U` is unitary, `C_2(U)` is unitary for the natural Hermitian inner product.

Choose oriented complementary-pair vectors

\[
x_1=e_{12},\ x_2=e_{13},\ x_3=e_{14},
\]

\[
y_1=e_{34},\ y_2=-e_{24},\ y_3=e_{23}.
\tag{4}
\]

Then `x_alpha wedge y_beta = delta_{alpha beta} e_{1234}`. Let the anti-linear involution `K` interchange `x_alpha` and `y_alpha` and conjugate coefficients. Preservation of both the Hermitian form and `Q` gives

\[
C_2(U)K=KC_2(U).
\tag{5}
\]

The fixed real subspace of `K` has the orthonormal real basis

\[
f_\alpha=\frac{x_\alpha+y_\alpha}{\sqrt2},
\qquad
g_\alpha=\frac{i(x_\alpha-y_\alpha)}{\sqrt2}.
\tag{6}
\]

Hence `C_2(U)` restricts there to a real orthogonal matrix

\[
O(U)\in SO(6).
\tag{7}
\]

This is the classical exceptional `Spin(6)=SU(4)` representation, but the only facts needed here are (3)-(7). For completeness, surjectivity onto `SO(6)` is also immediate at the Lie-algebra level: if `X in su(4)` acts trivially on `Lambda^2`, diagonalizing the skew-Hermitian `X` gives eigenvalues `i theta_i` with every pair sum `theta_i+theta_j=0`, hence every `theta_i=0`; the differential is injective. Both Lie algebras have real dimension 15. The image is therefore a connected full-dimensional closed subgroup of connected `SO(6)`, hence all of `SO(6)`.

## 4. New exact block formula for the mixed-minor variables

Partition `O(U)` into 3-by-3 blocks of size 2-by-2 according to the real planes

\[
E_\alpha=\operatorname{span}_\mathbb R\{f_\alpha,g_\alpha\},
\qquad
O=(B_{\alpha\beta})_{\alpha,\beta=1}^3.
\tag{8}
\]

Let

\[
m_{\alpha\beta}=\det U[S_\alpha,T_\beta],
\qquad
n_{\alpha\beta}=\text{the consistently oriented }\det U[S_\alpha,T_\beta^c].
\]

In the complex complementary basis, the corresponding two-dimensional block has the reality form forced by (5). Passing to `(f_beta,g_beta)` and `(f_alpha,g_alpha)` gives a real matrix unitarily equivalent to

\[
B_{\alpha\beta}=
\begin{pmatrix}
\Re(m+n)&-\Im(m-n)\\
\Im(m+n)& \Re(m-n)
\end{pmatrix}.
\tag{9}
\]

Therefore

\[
\boxed{
\frac12\|B_{\alpha\beta}\|_F^2
=|m_{\alpha\beta}|^2+|n_{\alpha\beta}|^2
=r_{\alpha\beta},
}
\tag{10}
\]

and

\[
\boxed{
\det B_{\alpha\beta}
=|m_{\alpha\beta}|^2-|n_{\alpha\beta}|^2
=d_{\alpha\beta}.
}
\tag{11}
\]

Combining (2), (10), and (11) gives the promised exact realization:

\[
\boxed{
R_{\alpha\beta}=\frac12\|B_{\alpha\beta}\|_F^2,
\quad
D_{\alpha\beta}=\det B_{\alpha\beta},
\quad
P=H^T\!\begin{pmatrix}1&0\\0&D\end{pmatrix}\!H.
}
\tag{12}
\]

Thus the one-minor and complementary-two-minor transports are **not two unrelated bistochastic objects**: they are respectively the determinant and block-energy images of the same `O in SO(6)`.

This is the representation-theoretic common-unitary constraint sought by this assignment. It does not assert positivity of the determinantal quasidistribution and is compatible with both the account04/B09 joint-lift counterexample and the lead's negative Saxl-cone separator.

## 5. The exact global constraints hidden by the scalar relaxation

Since `O` is orthogonal, its 2-by-2 blocks satisfy the matrix identities

\[
\boxed{
\sum_{\beta=1}^3 B_{\alpha\beta}B_{\gamma\beta}^T
=\delta_{\alpha\gamma}I_2,
}
\tag{13}
\]

\[
\boxed{
\sum_{\alpha=1}^3 B_{\alpha\beta}^TB_{\alpha\delta}
=\delta_{\beta\delta}I_2.
}
\tag{14}
\]

These are four real equations for each off-diagonal block-row or block-column pair. They are strictly the sort of simultaneous common-unitary information lost by treating `P` and `R` independently.

They also explain the scalar constraints already derived by account01/B07. The squared singular values of a block `B=B_{alpha beta}` are

\[
\lambda_\pm=r\pm\sqrt{r^2-d^2}.
\tag{15}
\]

Hence `|d|<=r`. Because every block is a compression of an orthogonal matrix, `lambda_+<=1`, which is equivalent to

\[
r\le\frac{1+d^2}{2}.
\tag{16}
\]

So the old entrywise interval is exactly the local singular-value shadow of the stronger block-orthogonality system (13)-(14).

### A phase-eliminated cross-block consequence

Set

\[
s_{\alpha\beta}=\sqrt{r_{\alpha\beta}^2-d_{\alpha\beta}^2}.
\]

Fix distinct block rows `alpha,gamma`. From (13), the three 2-by-2 matrices

\[
M_\beta=B_{\alpha\beta}B_{\gamma\beta}^T
\]

sum to zero. For every `beta`, the triangle inequality gives

\[
\|M_\beta\|_F\le\sum_{\delta\ne\beta}\|M_\delta\|_F.
\tag{17}
\]

The trace rearrangement inequality for two 2-by-2 positive semidefinite matrices, together with (15), gives

\[
2(r_{\alpha\beta}r_{\gamma\beta}-s_{\alpha\beta}s_{\gamma\beta})
\le \|M_\beta\|_F^2
\le
2(r_{\alpha\beta}r_{\gamma\beta}+s_{\alpha\beta}s_{\gamma\beta}).
\tag{18}
\]

Consequently every actual common unitary satisfies the purely `(R,D)` inequality

\[
\boxed{
\sqrt{2(r_{\alpha\beta}r_{\gamma\beta}-s_{\alpha\beta}s_{\gamma\beta})}
\le
\sum_{\delta\ne\beta}
\sqrt{2(r_{\alpha\delta}r_{\gamma\delta}+s_{\alpha\delta}s_{\gamma\delta})}.
}
\tag{19}
\]

There is an identical column version. Equation (19) is only a necessary scalar consequence; (13)-(14), with the latent real 2-by-2 blocks retained, are the exact constraint.

### A second exact local mixed-minor bound involving `P`

For `S={i,k}` and `T={j,l}`,

\[
q_{S,T}=|u_{ij}u_{kl}-u_{il}u_{kj}|^2.
\]

Therefore, with `x=p_{ij}p_{kl}` and `y=p_{il}p_{kj}`,

\[
\boxed{
(\sqrt x-\sqrt y)^2\le q_{S,T}\le(\sqrt x+\sqrt y)^2.
}
\tag{20}
\]

Using `q=(r+d)/2` for the chosen orientation and `q=(r-d)/2` for its complement gives an explicit interval constraint linking each `R` entry to the four relevant entries of `P`. This is elementary but phase-faithful; it is stronger than using only `|d|<=r` at that cell.

## 6. Representation-theoretic meaning of the 13-dimensional Saxl space

The lead's exact enumeration found a 13-dimensional nonconstant determinant-endpoint space. The block picture identifies it naturally.

The permutation action on four points is

\[
\mathbf 1\oplus [31],
\]

so its nonconstant matrix-coefficient space has dimension `3^2=9`. This is exactly the mean-zero `P` block `D` in (2).

The action on the three complementary pair classes factors through `S_4/V_4 \cong S_3` and is

\[
\mathbf 1\oplus [22],
\]

so its nonconstant matrix-coefficient space has dimension `2^2=4`. This is exactly the four-dimensional doubly-stochastic tangent carried by `R`.

Thus

\[
\boxed{13=9+4}
\]

is the representation split `End([31]) \oplus End([22])` underlying the lead/partner Saxl formulation. Equations (12)-(14) are the missing common-unitary compatibility between those two irreducible sectors.

## 7. Rewriting the exact support problem as one structured quadratic on `SO(6)`

This gives a concrete next proof object rather than another positivity conjecture. Let

\[
\widehat C=HCH^T,
\qquad K=(\widehat C_{\alpha\beta})_{\alpha,\beta=1}^3
\]

be the lower 3-by-3 block; the scalar `widehat C_00` is absorbed into the support constant. By (2) and (12),

\[
\langle P,C\rangle
=\widehat C_{00}+\sum_{\alpha,\beta}K_{\alpha\beta}\det B_{\alpha\beta},
\]

while

\[
\frac12\langle R,X\rangle
=\frac14\sum_{\alpha,\beta}X_{\alpha\beta}\|B_{\alpha\beta}\|_F^2.
\]

Hence `(MI)` is exactly the assertion that, for the **structured** `(K,X)` arising from `(a,b,eta)`,

\[
\boxed{
Q_{K,X}(O):=
\sum_{\alpha,\beta}
\left[
K_{\alpha\beta}\det B_{\alpha\beta}
+\frac14X_{\alpha\beta}\|B_{\alpha\beta}\|_F^2
\right]
}
\tag{21}
\]

never exceeds its maximum on the 24 `S_4` endpoint images inside `SO(6)`.

This is the first unpaid implication in this representation-theoretic route:

> **`MOC4-SO6-QUADRATIC-v1` (OPEN).** For every structured support coefficient pair `(K,X)` coming from complex spectra and one support direction, the block-separable quadratic (21) on `SO(6)` is maximized by an endpoint image of a permutation.

It is important that (21) is **not** claimed for arbitrary real `(K,X)`: that stronger statement is another form of the already-refuted unrestricted joint-lift/positivity mechanism. The actual next attack should combine the exact global equations (13)-(14) with the structured spectral coefficient identities from account04/B09, rather than enlarge `(K,X)` to all coefficient matrices.

This reduction includes singular and repeated spectra automatically: no spectral gap or inverse was used. It also remains compatible with the account02/B08 repeated-spectrum theorem, which can be viewed as an already-settled boundary of (21).

## 8. Exact verification on the campaign rational orthogonal witness

The attached `verify_spin6_blocks.py` uses only Python standard-library `Fraction` arithmetic and the exact rational orthogonal matrix used earlier in the campaign. It checks orthogonality and determinant one, the Hadamard identity (2), both block-orthogonality systems (13)-(14), recovery of all 18 oriented/complementary two-minor squares from `(R,D)`, and the exact real-instance form of (20).

Exact output:

```text
U_orthogonal_det1 PASS
D_equals_HPH_mean_zero_block PASS entries=9
row_block_orthogonality PASS equations=9
column_block_orthogonality PASS equations=9
q_recovery_from_R_D PASS checks=18
phase_interval_exact_rational_witness PASS checks=18
R=
4329/15625 251136/390625 31264/390625
4896/15625 31264/390625 236961/390625
256/625 4329/15625 4896/15625
D=
-279/15625 209664/390625 -7936/390625
-2304/15625 -7936/390625 223839/390625
256/625 279/15625 2304/15625
```

The computation is a consistency check, not the proof; the general identities are proved above.

## 9. Status and handoff

**Status:** `ESSENTIAL_STEP_APPLIED`; MOC4 remains open.

What is now paid:

- the exact same-unitary mixed-minor feasibility problem has a real `SO(6)` block realization;
- `P` and `R` are respectively block-determinant and block-energy images of one orthogonal matrix;
- the known local scalar bounds are recovered from block singular values;
- new exact global 2-by-2 matrix equations (13)-(14) and the phase-eliminated consequence (19) are available;
- the 13 nonconstant Saxl dimensions split canonically as `9+4`, explaining how the lead's Drury-facet route and the mixed-minor route encode the same two irreducible sectors.

What is not paid:

- no proof of the upper Drury facet `(UF)`;
- no proof of `MOC4-SO6-QUADRATIC-v1`;
- no target-level counterexample;
- no claim that arbitrary nonnegative Saxl functions, arbitrary `(P,R)`, or arbitrary `(K,X)` are admissible.

Recommended next use by the team lead: combine (21) with account04/B09's structured coefficient discriminant/inverse formulas and attack the orthogonal-block stationarity/global-max problem while keeping (13)-(14) exact. The partner account01/B08 upper-facet fan provides an independent purely spectral route against which any proposed maximizer can be checked.
