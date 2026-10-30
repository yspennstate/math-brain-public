# MOC4 fleet01/B07 — Spin(6) stationarity equations for the exact mixed-minor objective

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal `4 x 4` Marcus-de Oliveira target  
**Worker:** fleet01/B07  
**Assignment:** exact exterior-power/minor expansion and the mixed-minor inequality needed for the hull bound  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and current conditional chain

For complex normal `4 x 4` matrices `A,B` with spectra `a_1,...,a_4` and `b_1,...,b_4`, the target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

After diagonalizing `A` and writing `B=U diag(b)U*`, the established fleet01/B07 mixed-minor reduction writes every real support functional, up to its scalar constant, as

\[
Q_{K,X}(O)=\sum_{\alpha,\beta=1}^3\left[
 K_{\alpha\beta}\det B_{\alpha\beta}
 +\frac14X_{\alpha\beta}\|B_{\alpha\beta}\|_F^2
\right],                                      \tag{1}
\]

where the same true unitary `U` determines `O=O(U) in SO(6)` and its `2 x 2` blocks `B_{alpha beta}`.  This is the exact fleet04/B07 `MOC4-SPIN6-BLOCK-v1` realization; no arbitrary `(P,R)` relaxation is being made.  In its notation

\[
D_{\alpha\beta}=\det B_{\alpha\beta},\qquad
R_{\alpha\beta}=\frac12\|B_{\alpha\beta}\|_F^2,              \tag{2}
\]

and the block equations

\[
\sum_\beta B_{\alpha\beta}B_{\gamma\beta}^{T}
 =\delta_{\alpha\gamma}I_2,
\qquad
\sum_\alpha B_{\alpha\beta}^{T}B_{\alpha\delta}
 =\delta_{\beta\delta}I_2                                  \tag{3}
\]

retain the exact common-unitary compatibility.

I directly consume the named OTHER-account partner result **fleet02/B08, `MOC4-REPEATED-MINIMAL-LIFT-v2`** (scientific commit `fab8368ce6b7854675947d7808cf85989623fbf8`).  It proves the repeated-eigenvalue face by a smaller source-valid fractional orientation lift and gives a strict collar away from explicit zero-nonrepeated-row / supported-collinearity strata.  Thus a hypothetical failure cannot be hidden by simply approaching a generic repeated-spectrum face.

I also use fleet02/B09 `MOC4-BIPAIR-MAX-v1` and its r12 six-fiber compression.  For

\[
T=|K|+X/2,\quad
c_\rho=\langle R_\rho,T\rangle,\quad
q_\rho=c_\rho-2m_\rho(K),
\]

where `m_rho=0` on a parity-good `K` transversal and otherwise is its smallest selected `|K|`, the exact support inequality is

\[
\theta:=\langle D,K\rangle+\frac12\langle R,X\rangle
\le \max_{\rho\in S_3}q_\rho.                              \tag{4}
\]

The unconditional parity-slack and scalar-roof shortcuts have now both been refuted on genuine generic true-unitary data.  The surviving interior route is therefore maximizer-local: a violating support direction has a global maximizing unitary, and that maximizer must satisfy the exact unitary stationarity constraints.  This report derives those constraints in closed block/minor form.

The campaign lead's zero-entry common-lift shortcut is also refuted; the zero-entry support branch itself is still an unpaid branch.  Accordingly the honest end-to-end split is:

1. close `MOC4-ZERO-FACE-SUPPORT-v1`; and
2. on the pair-strict interior, prove (4) at a genuine support maximizer from the stationarity equations below plus (3) and the structured spectral form of `(K,X)`.

## 2. Cofactor-channel decomposition of the Spin(6) quadratic

For a real `2 x 2` matrix `B`, let `cof(B)` denote the cofactor matrix, i.e. the Frobenius gradient of `det B`.  The map `B -> cof(B)` is a self-adjoint involution.  Define

\[
B^+=\frac12(B+\operatorname{cof}B),\qquad
B^-=\frac12(B-\operatorname{cof}B).
\]

The two channels are Frobenius-orthogonal and satisfy

\[
\|B\|_F^2=\|B^+\|_F^2+\|B^-\|_F^2,
\qquad
\det B=\frac12(\|B^+\|_F^2-\|B^-\|_F^2).                  \tag{5}
\]

Consequently each summand of (1) is exactly

\[
K\det B+\frac X4\|B\|_F^2
=\frac{X+2K}{4}\|B^+\|_F^2
 +\frac{X-2K}{4}\|B^-\|_F^2.                              \tag{6}
\]

In the consistently oriented complementary-minor coordinates of `MOC4-SPIN6-BLOCK-v1`, write the real map represented by `B_{alpha beta}` as

\[
z\longmapsto m_{\alpha\beta}z+n_{\alpha\beta}\bar z.
\]

Then

\[
R_{\alpha\beta}=|m_{\alpha\beta}|^2+|n_{\alpha\beta}|^2,
\qquad
D_{\alpha\beta}=|m_{\alpha\beta}|^2-|n_{\alpha\beta}|^2,   \tag{7}
\]

so, with

\[
u_{\alpha\beta}=X_{\alpha\beta}/2+K_{\alpha\beta},\qquad
v_{\alpha\beta}=X_{\alpha\beta}/2-K_{\alpha\beta},
\]

we have the exact two-channel energy form

\[
\boxed{
Q_{K,X}(O)=\sum_{\alpha,\beta}
\left(u_{\alpha\beta}|m_{\alpha\beta}|^2
     +v_{\alpha\beta}|n_{\alpha\beta}|^2\right).
}                                                               \tag{8}
\]

This is useful because the 24 target endpoint values are precisely the even-parity signed block-matchings of the two channel weights, while `(m,n)` still obey the true `SO(6)` orthogonality relations rather than an invented common permutation law.

## 3. Exact first-order stationarity: three `2 x 2` balance equations

Let

\[
G_{\alpha\beta}
:=K_{\alpha\beta}\operatorname{cof}(B_{\alpha\beta})
  +\frac12X_{\alpha\beta}B_{\alpha\beta}.                 \tag{9}
\]

This is the Frobenius gradient of the corresponding block summand in (1).

For distinct block rows `alpha,gamma`, and an arbitrary real `2 x 2` matrix `Z`, let `A_{alpha gamma}(Z)` be the skew `6 x 6` matrix with off-diagonal blocks

\[
A_{\alpha\gamma}=Z,\qquad A_{\gamma\alpha}=-Z^T,
\]

and all other blocks zero.  Along the genuine `SO(6)` curve

\[
O(t)=e^{tA_{\alpha\gamma}(Z)}O,
\]

we have at `t=0`

\[
\dot B_{\alpha\beta}=ZB_{\gamma\beta},\qquad
\dot B_{\gamma\beta}=-Z^TB_{\alpha\beta}.
\]

Therefore

\[
\frac d{dt}Q(O(t))\bigg|_{0}
=\left\langle N_{\alpha\gamma},Z\right\rangle_F,            \tag{10}
\]

where

\[
\boxed{
N_{\alpha\gamma}:=
\sum_{\beta=1}^3
\left(
G_{\alpha\beta}B_{\gamma\beta}^T
-B_{\alpha\beta}G_{\gamma\beta}^T
\right).
}                                                               \tag{11}
\]

Hence every critical point, in particular every global support maximizer, satisfies

\[
\boxed{N_{12}=N_{13}=N_{23}=0.}                              \tag{12}
\]

These are twelve real scalar equations.  They are not merely a relaxation: fleet04/B07 proved `SU(4) -> SO(6)` is onto, so every tangent used above is realized by a genuine unitary variation.  Conversely, the only remaining three left-tangent directions rotate each individual `2`-plane; (1) is invariant under those rotations because both determinant and Frobenius norm are unchanged.  Thus (12) is the complete nontrivial first-order stationarity system for (1).

Expanding (11),

\[
N_{\alpha\gamma}
=\sum_\beta\left[
K_{\alpha\beta}\operatorname{cof}(B_{\alpha\beta})B_{\gamma\beta}^T
-K_{\gamma\beta}B_{\alpha\beta}\operatorname{cof}(B_{\gamma\beta})^T
+\frac{X_{\alpha\beta}-X_{\gamma\beta}}2
 B_{\alpha\beta}B_{\gamma\beta}^T
\right].                                                       \tag{13}
\]

This is the desired direct bridge from the exterior-power/minor expansion to maximizer geometry.

### Equivalent complex-minor balances

Using (7)-(8), equation (12) is equivalent, for every `alpha<gamma`, to the following two complex equations:

\[
\boxed{
\sum_\beta
\big[(u_{\alpha\beta}-u_{\gamma\beta})
 m_{\alpha\beta}\overline{m_{\gamma\beta}}
+(v_{\alpha\beta}-v_{\gamma\beta})
 n_{\alpha\beta}\overline{n_{\gamma\beta}}\big]=0,
}                                                               \tag{14}
\]

and

\[
\boxed{
\sum_\beta
\big[(u_{\alpha\beta}-v_{\gamma\beta})
 m_{\alpha\beta}n_{\gamma\beta}
+(v_{\alpha\beta}-u_{\gamma\beta})
 n_{\alpha\beta}m_{\gamma\beta}\big]=0.
}                                                               \tag{15}
\]

Thus the twelve pair-orbit north-pole conditions can be compressed into six complex weighted orthogonality identities on the *same genuine complementary minors*.  No phases have been independently chosen.

## 4. Exact scalar block-pair north-pole and a phase-free curvature inequality

A particularly useful one-parameter suborbit is obtained by taking `Z=I_2`, which rotates the two entire block planes.  Put

\[
h_{\alpha\gamma,\beta}
=\langle\operatorname{cof}(B_{\alpha\beta}),B_{\gamma\beta}\rangle_F,
\qquad
p_{\alpha\gamma,\beta}
=\langle B_{\alpha\beta},B_{\gamma\beta}\rangle_F.
\]

Let

\[
J_{\alpha\gamma}
=\sum_\beta\left[
(K_{\alpha\beta}-K_{\gamma\beta})h_{\alpha\gamma,\beta}
+\frac{X_{\alpha\beta}-X_{\gamma\beta}}2p_{\alpha\gamma,\beta}
\right],                                                       \tag{16}
\]

and

\[
H_{\alpha\gamma}
=\sum_\beta\left[
2(K_{\alpha\beta}-K_{\gamma\beta})(D_{\alpha\beta}-D_{\gamma\beta})
+(X_{\alpha\beta}-X_{\gamma\beta})(R_{\alpha\beta}-R_{\gamma\beta})
\right].                                                       \tag{17}
\]

A direct `2 x 2` determinant polarization gives the *exact entire circle*

\[
Q(O(t))=C+\frac14H_{\alpha\gamma}\cos(2t)
          +\frac12J_{\alpha\gamma}\sin(2t).                 \tag{18}
\]

Therefore a global maximizer must obey

\[
\boxed{J_{\alpha\gamma}=0,\qquad H_{\alpha\gamma}\ge0}       \tag{19}
\]

for all three block-row pairs; the analogous block-column identities follow as well.  In particular (17) is a completely phase-free necessary inequality in `(D,R,K,X)`.

Summing the second variations over the standard left `SO(6)` generators also gives a compact trace consequence.  A `2 x 2` minor is a matrix coefficient of `Lambda^2 R^6` and has left Casimir eigenvalue `8`, while `||B_{alpha beta}||^2-2/3` is a traceless quadratic with eigenvalue `12`.  Equivalently, this can be checked directly by summing coordinate rotations.  At any local maximum,

\[
\boxed{
4\langle D,K\rangle+3\langle R,X\rangle
\ge \sum_{\alpha,\beta}X_{\alpha\beta}.
}                                                               \tag{20}
\]

Equation (20) is only a necessary maximizer condition, not the MOC4 inequality; it is recorded to prevent future routes from treating arbitrary generic `(D,R)` data as if it were a support maximizer.

## 5. Exact check on the previous parity-slack counterexample

The preceding fleet01/B07 run produced a source-valid simple-spectrum, irreducible, strict-compound true-unitary datum refuting the *unconditional* parity-slack gate while the true MOC4 support inequality still held with a large positive gap.  The present stationarity mechanism explains why that example does not obstruct a maximizer-local proof.

Using the same exact rational orthogonal `U`, spectra and support direction `eta=1`, differentiate the true determinant support under the genuine row-pair `(1,3)` conjugation.  Exact Gaussian-rational arithmetic gives

\[
\frac d{dt}\operatorname{Re}\det\big(A+G_{13}(t)UBU^*G_{13}(t)^*\big)\bigg|_{t=0}
=
\frac{284796813152662076044041}
     {244140644531250390625000}
>0.                                                            \tag{21}
\]

So that exact generic witness is not even stationary, hence cannot be a global maximizer for its support direction.  This does not prove MOC4, but it cleanly separates the already-refuted unconditional scalar gates from the still-live stationarity-conditioned route.

The exact standard-library verifier is `verify_stationarity_witness.py` (creation commit `507162df01bbbd674ecd6dfa48f6603e3c3a8248`); captured output is `VERIFICATION.txt` (creation commit `fbca9facc01fa9cc3ea90da03c548205a3e4726b`).

## 6. First remaining implication

The new exact interior target is:

> **`MOC4-SPIN6-STATIONARY-SIX-WITNESS-v1`.** For every structured support coefficient pair `(K,X)` arising from complex spectra and a support direction, and every pair-strict `O in SO(6)` satisfying block orthogonality (3) and the critical equations (12) (equivalently (14)-(15)), prove
> \[
> \langle D,K\rangle+\frac12\langle R,X\rangle
> \le\max_{\rho\in S_3}\{c_\rho-2m_\rho(K)\}.                \tag{22}
> \]
> It is enough to prove this for a global maximizer; stationarity alone may admit saddles.

This is the first unpaid implication in the pair-strict branch.  It is strictly more source-faithful than the refuted universal parity-slack, unconditional scalar-roof, common-permutation-lift and spectral-only upper-facet mechanisms: (22) keeps the actual shared minor phases through (14)-(15) and keeps the exact structured `(K,X)`.

The other live branch remains `MOC4-ZERO-FACE-SUPPORT-v1`; no claim is made that (22) closes that branch.  The fleet02/B08 repeated-spectrum theorem already supplies the needed repeated-eigenvalue boundary result rather than requiring a limiting assumption here.

## 7. Sources and peer dependencies actually used

- S. W. Drury, *The external vertices conjecture in case n=4*, Electronic Journal of Linear Algebra 11 (2004), DOI `10.13001/1081-3810.1131` — status/weak n=4 background as recorded in the campaign source file, not treated as full MOC4.
- N. Bebiano and J. da Providencia, *Revisiting the Marcus-de Oliveira Conjecture*, Mathematics 13 (2025), 711, DOI `10.3390/math13050711` — campaign status/special-case background.
- J. I. Mulero-Martinez, *A variational framework for determinantal inequalities of normal matrices: Successes and obstructions*, Linear Algebra and its Applications 740 (2026), 19–38, DOI `10.1016/j.laa.2026.03.019` — variational-obstruction background; no first-order extremum is promoted to a proof.
- fleet02/B08 `MOC4-REPEATED-MINIMAL-LIFT-v2`, scientific commit `fab8368ce6b7854675947d7808cf85989623fbf8` — named assigned partner, directly used for the repeated-face reduction/collar.
- fleet04/B07 `MOC4-SPIN6-BLOCK-v1`, scientific commit `7dc542c7644686c649d19b90e7001a64be711355` — exact `SU(4)->SO(6)` block realization directly extended here.
- fleet02/B09 `MOC4-BIPAIR-MAX-v1` and r12 parity-excess handoff — exact pair-orbit maximizer condition and current six-witness formulation.
- fleet01/B07 preceding r11b, scientific commit `a0fac94c9342ee4a2c18ed94f7fe770bdf0b12df` — exact X-aware gap identity and source-valid parity-slack refutation reused only as a stationarity test datum.

No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API calls, Codex, remote workflows or permission changes were used.
