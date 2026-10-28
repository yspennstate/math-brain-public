SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-24T10:34:26Z.
attacking: Extremal product laws — combine the new uniformly indefinite physical pair with an exact rank-two Schur normalization and a diffuse separable-phase half-Riesz receiver; force any surviving high-ratio branch into finitely many heavy original-coordinate Schur rows.

# account03/B13 r49 — diffuse Schur payment after a uniform physical indefinite pair

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T103426Z-account03-B13-qform-r49`  
Role: extremal product laws / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.

All coordinates below are the original independent physical coordinates. No random-coordinate rotation is performed. No moment, Gaussian, log-concave, compact-support, connected-support, interval-extremality, bounded-diameter, fixed-fragment-count, post-rotation-independence, uniform pointwise van-der-Corput estimate, unrestricted fiber-supremum, or coefficient-small-implies-random-small step is used. The diagonal tail of the Schur remainder is retained exactly as a coordinate-separable phase.

## 1. Exact assignment interface: optimizer-free product purification

For every measurable `0<=K<=1`,

\[
\sup_{\substack{0\le f_i\le1\\ \int f_i=1}}
 \int K(x)\prod_{i=1}^n f_i(x_i)\,dx
=
\sup_{|E_1|=\cdots=|E_n|=1}
 \int_{\prod_iE_i}K(x)\,dx .                                    \tag{1.1}
\]

Indeed, for a nonnegative one-coordinate section `g`, layer cake gives

\[
\int gf\le \int_0^\infty \min\{1,|\{g>t\}|\}\,dt
       =\sup_{|E|=1}\int_Eg,                                    \tag{1.2}
\]

for every `0<=f<=1`, `int f=1`. Apply this successively in the physical coordinates, choosing only epsilon-near maximizers, and then let epsilon decrease to zero. Indicator densities give the reverse inequality. By Lebesgue regularity the unit-measure sets can be approximated with arbitrarily small loss by bounded finite unions of intervals. No optimizer, one-interval form, common diameter, centering, or uniform component count is asserted.

For `K=1_{x^T A x in J}`, (1.1) is exactly the geometric sublevel formulation requested by the assignment.

## 2. Source-pinned inputs actually used


The mathematical inputs are:

1. **Own r48 physical-pair theorem.**  
   `yspennstate/math-open-problems@ba4c0f14cf9ca505e346b284a530662c6522b514`  
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260924T095803Z-account03-B13-qform-r48/REPORT.md`.

   In the exact diffuse rank-two chamber
   \[
   A=D+U\Lambda U^T,\qquad U^TU=I_2,\qquad
   c_i:=\|u_i\|^2\le\frac13,\qquad s_3(A)\ge1,                  \tag{2.1}
   \]
   a sufficiently high slab-ratio witness `rho` lies either in the ultracollapse packet
   \[
   |\det\Lambda|<6144e^2\rho^{-4},                              \tag{2.2}
   \]
   or there are two original coordinates `I={k,j}` for which
   \[
   |d_k|,|d_j|\ge\frac78,                                       \tag{2.3}
   \]
   and the physical pair
   \[
   B=A[I,I]
   \]
   is uniformly indefinite with
   \[
   D_B:=|\det B|\ge D_0:=\frac{1001}{12544},\qquad
   \kappa_B:=\sigma_{\min}(B)\ge \kappa_0:=\frac{13}{112}.     \tag{2.4}
   \]

2. **Designated partner account04/B13.**  
   `yspennstate/math-open-problems@c30866924d918185e908ae4b3e22e31169366296`  
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260924T061740Z-account04-B13-nearnull-star-r3/REPORT.md`.

   If `k` maximizes `|d_i|`, then every witness satisfies
   \[
   |\det\Lambda|<3072e^2\rho^{-4}
   \quad\text{or}\quad
   \|A_{-k,k}\|_2\ge2^{-1/2}.                                  \tag{2.5}
   \]
   For the four-coordinate top-diagonal core `C` containing `k`, the star branch further gives
   \[
   \|A_{C\setminus\{k\},k}\|_2\ge\frac12
   \quad\text{or}\quad
   \|A_{C^c,k}\|_2\ge\frac12.                                 \tag{2.6}
   \]

3. **Pair-log smoothing.**  
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`  
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

   If an original-coordinate invertible indefinite pair has determinant magnitude `D_B` and smallest singular value `kappa_B`, and after completing that pair the remaining scalar random variable `R` obeys
   \[
   \sup_t\Pr\{|R-t|<r\}\le H\sqrt r\qquad(r>0),                \tag{2.7}
   \]
   then
   \[
   \|p_Q\|_\infty\le4\sqrt{2H}\,(D_B\kappa_B)^{-1/4}.         \tag{2.8}
   \]
   Arbitrary pair shifts depending on the remaining original coordinates are allowed. This proves essential boundedness in its scope; continuity is not supplied by that argument.

4. **Diffuse separable-phase Fourier calculation.**  
   `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`  
   `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.

   Its proof before the final time integration is valid for rank two as well: if `W^TW=I_2`, every row leverage is at most `1/2`, `L` is invertible symmetric, and `V_i` are arbitrary coordinate-separable measurable phases, then for
   \[
   R=(W^TX)^TL(W^TX)+\sum_iV_i(X_i)                              \tag{2.9}
   \]
   one has
   \[
   |\phi_R(t)|\le\min\{1,e\pi|\det L|^{-1/2}|t|^{-1}\}.       \tag{2.10}
   \]
   Combining exactly this estimate with the Gaussian half-power representation used in the completed rank-two theorem gives
   \[
   \boxed{\sup_s\mathbb E|R-s|^{-1/2}
       \le4\sqrt{2e}\,|\det L|^{-1/4}.}                        \tag{2.11}
   \]
   This is an integrated Fourier/fractional-potential estimate, not the refuted law-uniform pointwise scalar quadratic-decay claim.

## 3. Exact two-coordinate Schur transport

Work in Alternative B of r48, and put `R=I^c`, where `I={k,j}`. Write `U_I` for the two selected rows and `D_I=diag(d_k,d_j)`. Because both selected `d`'s are nonzero, completing the physical pair gives the exact Schur matrix

\[
S=A[R,R]-A[R,I]B^{-1}A[I,R]
  =D_R+U_RMU_R^T,                                               \tag{3.1}
\]
where Woodbury gives

\[
M=\Lambda-\Lambda U_I^TB^{-1}U_I\Lambda
  =(\Lambda^{-1}+U_I^TD_I^{-1}U_I)^{-1}.                        \tag{3.2}
\]

Define

\[
G:=U_R^TU_R=I_2-U_I^TU_I.                                       \tag{3.3}
\]

Since each selected row has squared norm at most `1/3`,

\[
U_I^TU_I\preceq(c_k+c_j)I_2\preceq\frac23I_2,
\qquad G\succeq\frac13I_2,
\qquad \det G\ge\frac19.                                      \tag{3.4}
\]

Normalize the residual physical frame by

\[
W:=U_RG^{-1/2},\qquad W^TW=I_2,\qquad
L:=G^{1/2}MG^{1/2}.                                              \tag{3.5}
\]

Then

\[
S=D_R+WLW^T.                                                     \tag{3.6}
\]

The determinant transport is exact. The matrix determinant lemma gives

\[
\det B
=\det D_I\,\det\Lambda\,
  \det(\Lambda^{-1}+U_I^TD_I^{-1}U_I),                          \tag{3.7}
\]
so

\[
|\det M|=\frac{|d_kd_j\det\Lambda|}{D_B}.                       \tag{3.8}
\]

Consequently, using (2.3)-(2.4),

\[
|\det L|=\det G\,|\det M|
\ge\frac19\frac{49}{64}\frac{|\det\Lambda|}{D_B}
=\boxed{\frac{49}{576}\frac{|\det\Lambda|}{D_B}}.             \tag{3.9}
\]

No reciprocal small physical minor appears: `B` was already uniformly conditioned by r48, and the entire diagonal remainder `D_R` remains in (3.6).

## 4. New receiver: a diffuse normalized Schur carrier pays the branch

For every residual physical coordinate `r in R`, define its normalized Schur leverage

\[
\ell_r:=u_r^TG^{-1}u_r=\|w_r\|^2.                               \tag{4.1}
\]

### Theorem 4.1 — `QFORM-INDEFPAIR-DIFFUSE-SCHUR-HALFRIESZ-v1`

Under (2.1), Alternative B of r48, and

\[
\max_{r\in R}\ell_r\le\frac12,                                \tag{4.2}
\]

the full quadratic form has an essentially bounded density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le55.243772\,|\det\Lambda|^{-1/8}.}                           \tag{4.3}
\]

The proof retains arbitrary values of all diagonal coefficients in `D_R`.

#### Proof

By (3.6) and (4.2), apply the rank-two diffuse separable-phase half-Riesz estimate (2.11) with `V_r(x)=d_rx^2`:

\[
H_{1/2}(S):=\sup_t\mathbb E|X_R^TSX_R-t|^{-1/2}
\le4\sqrt{2e}\,|\det L|^{-1/4}.                                \tag{4.4}
\]

Therefore

\[
\Pr\{|X_R^TSX_R-t|<r\}
\le H_{1/2}(S)\sqrt r.                                          \tag{4.5}
\]

Apply pair-log smoothing (2.8) to the fixed original-coordinate pair `B`:

\[
\begin{aligned}
\|p_Q\|_\infty
&\le4\sqrt{2H_{1/2}(S)}(D_B\kappa_B)^{-1/4}\\
&\le4\sqrt{8\sqrt{2e}}
       (D_B\kappa_B)^{-1/4}|\det L|^{-1/8}.                     \tag{4.6}
\end{aligned}
\]

Insert (3.9):

\[
\|p_Q\|_\infty
\le4\sqrt{8\sqrt{2e}}
  \kappa_B^{-1/4}D_B^{-1/8}
  \left(\frac{576}{49}\right)^{1/8}
  |\det\Lambda|^{-1/8}.                                         \tag{4.7}
\]

Finally use `D_B>=1001/12544` and `kappa_B>=13/112`. The explicit prefactor is

\[
4\sqrt{8\sqrt{2e}}
\left(\frac{13}{112}\right)^{-1/4}
\left(\frac{1001}{12544}\right)^{-1/8}
\left(\frac{576}{49}\right)^{1/8}
=55.2437712392\ldots,                                           \tag{4.8}
\]

which proves (4.3). QED.

## 5. High-ratio consequence: the Schur carrier must have a heavy physical row

In the non-ultracollapse branch,

\[
|\det\Lambda|\ge6144e^2\rho^{-4}.                              \tag{5.1}
\]

If (4.2) held, (4.3) would imply

\[
\|p_Q\|_\infty
\le55.2437712392(6144e^2)^{-1/8}\rho^{1/2}
=14.4595007079\rho^{1/2}.                                       \tag{5.2}
\]

A slab witness of ratio `rho=P(Q in J)/|J|` satisfies `rho<=||p_Q||_infty`; hence

\[
\rho\le14.4595007079\sqrt\rho,
\qquad
\boxed{\rho\le209.077160720}.                                  \tag{5.3}
\]

Thus:

### Corollary 5.1 — `QFORM-NONULTRACOLLAPSE-FORCES-HEAVY-SCHUR-ROW-v1`

For every witness with

\[
\boxed{\rho>209.078}                                            \tag{5.4}
\]

in the r48 non-ultracollapse branch, there exists an original residual coordinate `h notin {k,j}` such that

\[
\boxed{\ell_h=u_h^TG^{-1}u_h>\frac12.}                          \tag{5.5}
\]

Because `W^TW=I_2`,

\[
\sum_{r\in R}\ell_r=2,                                         \tag{5.6}
\]

so there are at most three such heavy residual coordinates. The previously diffuse many-coordinate obstruction has therefore collapsed to an at-most-three-row physical Schur core once the uniform indefinite pair has been exposed.

## 6. Designated partner applied to the actual survivor

The partner theorem (2.5) is active on exactly the same non-ultracollapse packet, because

\[
|\det\Lambda|\ge6144e^2\rho^{-4}>3072e^2\rho^{-4}.             \tag{6.1}
\]

Therefore at the same maximizing original coordinate `k` used in r48,

\[
\boxed{\|A_{-k,k}\|_2\ge2^{-1/2}},                              \tag{6.2}
\]

and the partner's actual physical split gives

\[
\boxed{
\|A_{C\setminus\{k\},k}\|_2\ge\frac12
\quad\text{or}\quad
\|A_{C^c,k}\|_2\ge\frac12.}                                   \tag{6.3}
\]

Combining (5.5) with (6.2)-(6.3), every non-ultracollapse witness with `rho>209.078` now carries **simultaneously**:

- a uniformly conditioned original-coordinate indefinite pair `{k,j}`;
- a fixed original-coordinate star at `k` supplied by account04/B13; and
- at least one but at most three `>1/2`-leverage original rows in the normalized rank-two Schur carrier.

This is the concrete application of the designated partner result to the new inequality, not a status-only citation.

## 7. What is and is not closed

This run closes the **diffuse normalized Schur** alternative after the r48 physical pair. It does not close the heavy-Schur-row alternative. A row with leverage above `1/2` can interact strongly with the retained diagonal tail and the physical star; the live correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` forbids declaring that one heavy row plus one cross coefficient automatically absorbs arbitrary same-bank curvature.

The next B13 obligation is therefore

`QFORM-INDEFPAIR-HEAVY-SCHUR-ROW-RECEIVER-v1`:

use the fact that there are at most three heavy normalized Schur rows, together with the fixed physical star and the exact diagonal-plus-rank-two Schur structure, to obtain a finite physical receiver or force the latent determinant into the ultracollapse packet. All remaining quadratic curvature must stay inside the argument.

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.** The new branch theorem proves essential boundedness only; pair-log smoothing, as currently sourced, does not supply continuity of the final density.

## 8. Arithmetic verification

The accompanying deterministic checker evaluates only the exact constants in (4.8), (5.2), and (5.3). It is not a proof of the analytic estimates. Expected terminal marker:

`QFORM_B13_R49_DIFFUSE_SCHUR_CHECK_PASS`.
