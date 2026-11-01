# MOC4 fleet01/B07 — exact spectral-covariance reconstruction and edge-budgeted strict-margin payment

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T073048Z-fleet01-B07-MOC4-r12`  
**Assignment:** exact `4 x 4` exterior-power/minor expansion and the mixed-minor inequality needed for the shared hull bound  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact inherited state used

For diagonal spectra and one true unitary `U`, the exact Cauchy--Binet expansion is

\[
\det(D_a+UD_bU^*)
 =\sum_{S,T\subset[4],\ |S|=|T|}
 a_{S^c}b_T\,|\det U[S,T]|^2.                    \tag{1}
\]

In the `k=2` layer, after the standard complementary-pair change of basis,
`O=\Lambda^2U\in SO(6)` is a `3 x 3` array of real `2 x 2` blocks
`B_{\alpha\beta}`. Put

\[
R_{\alpha\beta}=\frac12\|B_{\alpha\beta}\|_F^2,
\qquad
D_{\alpha\beta}=\det B_{\alpha\beta}.
\]

The nonconstant support is exactly

\[
s(O)=\langle D,K\rangle+\frac12\langle R,X\rangle.       \tag{2}
\]

For

\[
p=(a_1a_2+a_3a_4,\ a_1a_3+a_2a_4,\ a_1a_4+a_2a_3),
\]
\[
q=(b_1b_2+b_3b_4,\ b_1b_3+b_2b_4,\ b_1b_4+b_2b_3),
\]
we have the structured middle-layer coefficient identity

\[
X_{\alpha\beta}=\Re(\eta p_\alpha q_\beta).               \tag{3}
\]

The latest complete campaign-lead result used is fleet03/B07
`MOC4-KERNEL-QUARTIC-RESERVE-v1`, run
`20260922T064004Z-fleet03-B07-MOC4-r12`.  It gives the exhaustive local split of every
positive-gap global maximizer into a mixed-Schur boundary branch or an all-pair negative-definite
interior branch, after all scalar sectors are strict.

The assigned OTHER-account partner result consumed and applied is fleet02/B08
`MOC4-2PLUS2-EVC-TRANSVERSAL-CLOSURE-v1`, run
`B08-20260922T053946Z-bf1307`, report blob
`a361d4996c79854aa569c85a83b94ea43367b66d`.  It proves the target support inequality on an
exact-four exposed `2+2` common-block face whenever its two local real ratios are not both
negative, by a source-valid spectral submersion plus Drury's proved `n=4` external-vertices
theorem.  Its only exact-four residual is the double-interlacing sign chamber.  Therefore the
strict generic interior analysis below is not being used as a substitute for an already-covered
common-block boundary.

I also use the exact campaign-lead pair-Hessian theorem
`MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`.  For a row-plane pair `alpha,gamma`, if

\[
Q_{\alpha\gamma}:=T_{\alpha\gamma}^2-C_{\alpha\gamma}^2,
\]
then, with the weighted traceless Gram sums defined below,

\[
\bigl(\rho(W_{\alpha\gamma}^{(\alpha)})+
       \rho(W_{\alpha\gamma}^{(\gamma)})\bigr)^2
\le 4Q_{\alpha\gamma}.                                    \tag{4}
\]

This is a genuine true-unitary Hessian inequality, not a free bistochastic relaxation.

## 2. Compact conditional end-to-end route

Assume MOC4 fails in a support direction.  Compactness gives a true-unitary global maximizer
`U_*` with support gap `gamma>0` over all 24 permutation products.  By the current team
reductions, after source-valid genericization one may work with simple nonzero spectra away from
the real-cross-ratio conditioning locus.  The lead then has two exhaustive live branches:

1. at least one genuine Spin(4) pair Hessian is on the mixed-Schur boundary;
2. all six left/right pair Hessians are negative definite.

The previous B07 theorem bounded exterior-block nonconformality by the six strict margins
`Q=T^2-C^2`, but it paid each pair separately at both endpoints and used only a smallest-singular-
value bound for the spectral interpolation system.  The first useful implication is to remove
both losses exactly.  That is done below.

## 3. Traceless-Gram variables

For a real symmetric traceless `2 x 2` matrix `S`, use the lead norm

\[
\rho(S)^2=\frac12\|S\|_F^2.
\]

For each exterior block define

\[
V_{\alpha\beta}:=
\operatorname{tf}(B_{\alpha\beta}B_{\alpha\beta}^T).
\]

A direct two-singular-value calculation gives the exact identity

\[
\boxed{\rho(V_{\alpha\beta})^2
       =R_{\alpha\beta}^2-D_{\alpha\beta}^2.}              \tag{5}
\]

Block-row orthogonality of `O` gives

\[
\sum_{\beta=1}^3 V_{\alpha\beta}=0.                       \tag{6}
\]

For distinct row planes `alpha,gamma`, put

\[
W_{\alpha\gamma}^{(\alpha)}
 :=\sum_{\beta=1}^3
 (X_{\alpha\beta}-X_{\gamma\beta})V_{\alpha\beta}.        \tag{7}
\]

Then the lead's anisotropy theorem is exactly (4).

## 4. New theorem — `MOC4-EXACT-SPECTRAL-COVARIANCE-RECONSTRUCTION-v1`

Fix a row `alpha` and write `gamma,delta` for the other two row indices.  Define the `2 x 3`
matrix

\[
C_\alpha=
\begin{pmatrix}
X_{\alpha1}-X_{\gamma1}&X_{\alpha2}-X_{\gamma2}&X_{\alpha3}-X_{\gamma3}\\
X_{\alpha1}-X_{\delta1}&X_{\alpha2}-X_{\delta2}&X_{\alpha3}-X_{\delta3}
\end{pmatrix},                                             \tag{8}
\]

and let

\[
P_0=I_3-\frac13{\bf1}{\bf1}^T,
\qquad
S_\alpha=C_\alpha P_0 C_\alpha^T.                         \tag{9}
\]

Assume the generic conditioning condition `det S_alpha>0`, equivalently the earlier
`3 x 3` matrix

\[
L_\alpha=\begin{pmatrix}{\bf1}^T\\ C_\alpha\end{pmatrix}
\]
is nonsingular.  Put

\[
G_\alpha=S_\alpha^{-1}.                                   \tag{10}
\]

If

\[
W_1=W_{\alpha\gamma}^{(\alpha)},\qquad
W_2=W_{\alpha\delta}^{(\alpha)},
\]
then the total nonconformality in that block row is **exactly**

\[
\boxed{
E_\alpha:=\sum_{\beta=1}^3(R_{\alpha\beta}^2-D_{\alpha\beta}^2)
 =G_{11}\rho(W_1)^2+2G_{12}\langle W_1,W_2\rangle_\rho
   +G_{22}\rho(W_2)^2.}                                   \tag{11}
\]

### Proof

Work coordinatewise in the two-dimensional Hilbert space of traceless symmetric matrices.
For one scalar coordinate write `v=(v_1,v_2,v_3)^T`.  Equation (6) says `v in 1^perp`, while
(7) says

\[
C_\alpha v=w.
\]

On `1^perp` this map is bijective under `det S_alpha>0`, and its exact inverse is

\[
v=P_0C_\alpha^T S_\alpha^{-1}w.                           \tag{12}
\]

Therefore

\[
\|v\|^2=w^TS_\alpha^{-1}w.                                \tag{13}
\]

Apply (13) to both orthogonal traceless coordinates and sum.  Using (5) gives (11). `QED`

Thus the previous `sigma_min(L_alpha)` estimate was a coarse operator-norm corollary of an
exact identity; no information is lost in the spectral interpolation step itself.

## 5. The covariance matrix has an explicit spectral determinant

Let

\[
z_1=p_\alpha-p_\gamma,\qquad z_2=p_\alpha-p_\delta,
\qquad \bar q=(q_1+q_2+q_3)/3.
\]

From (3),

\[
(S_\alpha)_{ij}
=\sum_{\beta=1}^3
 \Re\{\eta z_i(q_\beta-\bar q)\}
 \Re\{\eta z_j(q_\beta-\bar q)\}.                         \tag{14}
\]

Hence

\[
\boxed{
\det S_\alpha
=\frac{|\eta|^4}{3}
 \Im(z_1\overline{z_2})^2
 \Im\!\left((q_1-q_3)\overline{(q_2-q_3)}\right)^2.}      \tag{15}
\]

Equivalently,

\[
\boxed{(\det L_\alpha)^2=3\det S_\alpha.}                 \tag{16}
\]

Proof of (15): identify `C` with `R^2`; the centered three-point scatter matrix of
`q_1,q_2,q_3` has determinant

\[
\frac13\Im\!\left((q_1-q_3)\overline{(q_2-q_3)}\right)^2,
\]
while the real-linear map `z -> Re(eta z q)` has oriented-area multiplier
`|eta|^2 Im(z_1 overline{z_2})`.  Squaring the area multiplier gives (15).

For `alpha=1`, the first factor contains the exact spectral products

\[
p_1-p_2=(a_2-a_3)(a_1-a_4),\qquad
p_1-p_3=(a_2-a_4)(a_1-a_3),                                \tag{17}
\]
with analogous formulas for `q`.  Thus the metric `G_alpha` is a fully explicit spectral
covariance metric; its singular set is exactly the already-identified real-cross-ratio locus.

## 6. New theorem — `MOC4-EDGE-BUDGETED-SPECTRAL-PAYMENT-v1`

Let

\[
\Lambda_\alpha:=\lambda_{\max}(G_\alpha).
\]

For each row edge `e={alpha,gamma}`, set

\[
u_e^{(\alpha)}=\rho(W_{\alpha\gamma}^{(\alpha)}),\qquad
u_e^{(\gamma)}=\rho(W_{\alpha\gamma}^{(\gamma)}).
\]

By the true-unitary pair-Hessian theorem,

\[
u_e^{(\alpha)}+u_e^{(\gamma)}\le2\sqrt{Q_e}.            \tag{18}
\]

From the exact identity (11),

\[
E_\alpha\le\Lambda_\alpha
\left((u_{\alpha\gamma}^{(\alpha)})^2+
      (u_{\alpha\delta}^{(\alpha)})^2\right).             \tag{19}
\]

Summing rows and grouping by the three unordered row edges gives

\[
\sum_{\alpha,\beta}(R_{\alpha\beta}^2-D_{\alpha\beta}^2)
\le
\sum_{\{\alpha,\gamma\}}
\left[\Lambda_\alpha(u_e^{(\alpha)})^2+
      \Lambda_\gamma(u_e^{(\gamma)})^2\right].            \tag{20}
\]

For nonnegative `u,v` with `u+v<=2sqrt(Q)`, convexity on that segment gives

\[
\Lambda_\alpha u^2+\Lambda_\gamma v^2
\le4Q\max\{\Lambda_\alpha,\Lambda_\gamma\}.              \tag{21}
\]

Therefore

\[
\boxed{
\mathcal E:=\sum_{\alpha,\beta}(R_{\alpha\beta}^2-D_{\alpha\beta}^2)
\le4\sum_{\alpha<\gamma}
Q^L_{\alpha\gamma}\max(\Lambda^L_\alpha,\Lambda^L_\gamma).}
                                                                    \tag{22}
\]

The identical column argument gives another bound.  Hence the actual common-unitary exterior
point satisfies the two-sided-source estimate

\[
\boxed{
\mathcal E\le4\min\left\{
\sum_{\alpha<\gamma}Q^L_{\alpha\gamma}
 \max(\Lambda^L_\alpha,\Lambda^L_\gamma),
\sum_{\beta<\delta}Q^R_{\beta\delta}
 \max(\Lambda^R_\beta,\Lambda^R_\delta)
\right\}.}                                                \tag{23}
\]

This is strictly more economical than paying every edge independently at both endpoint rows:
each pair-Hessian reserve `Q_e` is now a **shared edge budget**.  It also replaces the coarse
`1/sigma_min(L)^2` factor by the exact spectral covariance inverse.

A still sharper finite residual is available directly from (11): maximize the three row
quadratic forms with the six nonnegative endpoint variables `u_e^(alpha)` under the three edge
constraints (18), retaining `|G_12|` rather than `Lambda_alpha`.  This is a six-variable compact
quadratic program with coefficients fixed by the spectra.  Equation (23) is its clean closed-form
upper bound.

## 7. Mixed-Schur consequence: a quantitative nonconformality floor

On a mixed-Schur pair edge, the lead's operator-norm inequality is saturated.  Since the mixed
matrix singular value is exactly the sum of the two weighted Gram anisotropies, (18) becomes

\[
u_e^{(\alpha)}+u_e^{(\gamma)}=2\sqrt{Q_e}.              \tag{24}
\]

Let

\[
\lambda_\alpha:=\lambda_{\min}(G_\alpha),\qquad
\lambda_\gamma:=\lambda_{\min}(G_\gamma).
\]

The exact reconstruction gives

\[
E_\alpha\ge\lambda_\alpha(u_e^{(\alpha)})^2,
\qquad
E_\gamma\ge\lambda_\gamma(u_e^{(\gamma)})^2.             \tag{25}
\]

Minimizing the right side subject to (24) yields the harmonic-weight split, hence

\[
\boxed{
E_\alpha+E_\gamma
\ge
4Q_e\frac{\lambda_\alpha\lambda_\gamma}
          {\lambda_\alpha+\lambda_\gamma}.}               \tag{26}
\]

Thus on the generic spectral locus a true mixed-Schur singularity cannot approach the
conformal exterior-block locus at fixed positive `Q_e`.  This converts the campaign lead's
abstract mixed-Schur boundary into a source-explicit amount of compulsory exterior-minor
nonconformality.

The newest compatible fleet04/B07 theorem
`MOC4-MIXED-SCHUR-SVD-PAYMENT-v1` independently forces a positive double-antipode/SVD reserve
inside the same mixed-Schur block.  Equation (26) is complementary: it measures the unavoidable
nonconformality in the actual `Lambda^2 U` blocks, with constants determined entirely by the
structured spectral covariance (14)-(15).

## 8. What this settles and what it does not

This run settles the interpolation/payment part of the earlier
`MOC4-STRICT-MARGIN-SPECTRAL-PAYMENT-v1` more sharply:

- the three exterior-block anisotropies in a row are reconstructed exactly from the two
  weighted pair-Hessian anisotropies;
- the spectral conditioning matrix and its determinant are explicit;
- the pair-Hessian reserves are shared edge budgets, yielding (23);
- a mixed-Schur edge forces the positive nonconformality floor (26).

It does **not** yet compare the remaining allowed nonconformality directly with the positive
MOC4 support gap `gamma`, so it does not exclude the mixed-Schur or all-negative-definite branch
by itself.

The first surviving implication is now:

**`MOC4-SIX-EDGE-GAP-TO-NONCONFORMALITY-v1` (OPEN).**  At a positive-gap structured support
maximizer, use the endpoint/subgroup roofs and the exact `(K,X)` coefficient identities to obtain
a lower bound on `mathcal E` from the support gap (or, equivalently, an upper bound on the gap in
terms of `mathcal E`) strong enough to contradict the edge-budget ceiling (23); on a mixed-Schur
edge combine that comparison with the compulsory floor (26) and the SVD/double-swap reserve.

The assigned partner's `MOC4-2PLUS2-EVC-TRANSVERSAL-CLOSURE-v1` already removes three of the
four exact-four common-block sign chambers.  Its double-interlacing residual remains a separate
boundary mechanism; no claim is made here that (23) resolves it.

## 9. Exact arithmetic check

A standard-library rational check accompanies this report.  For Gaussian-integer spectral
surrogates it verifies exactly that

- `det(C P0 C^T)=det(L)^2/3` and agrees with the area formula (15);
- the vector-valued reconstruction (11) agrees exactly with direct inversion;
- a rational edge-budget sample satisfies (21).

The check is diagnostic confirmation of constants/signs; the proof is the algebra above.

## 10. Verdict

`ESSENTIAL_STEP_APPLIED`.

The strict-margin part of the MOC4 mixed-minor problem is now an explicit spectral-covariance
resource-allocation inequality on the genuine exterior-square point, with no duplicate payment
of one pair reserve at both endpoint rows.  Full MOC4 remains open.
