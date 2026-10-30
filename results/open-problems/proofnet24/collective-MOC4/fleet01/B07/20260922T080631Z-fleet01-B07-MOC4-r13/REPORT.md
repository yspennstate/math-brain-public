# MOC4 fleet01/B07 — explicit cross-root annihilator and cubic residual on the mixed-Schur branch

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T080631Z-fleet01-B07-MOC4-r13`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no brain-on claim is made.

## 1. Exact target and live proof tree

For complex normal `4 x 4` matrices with spectra `a=(a_i)` and `b=(b_j)`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_i(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

After diagonalization, for every support direction it is enough to control the support of
`det(D_a+U D_b U*)` over true `U in U(4)`.

The exact exterior-minor expansion used throughout this slot is

\[
\det(D_a+UD_bU^*)
 =\sum_{S,T\subset[4],\ |S|=|T|}
 a_{S^c}b_T\,|\det U[S,T]|^2. \tag{1}
\]

In the `k=2` layer, after the complementary-pair/self-dual change of basis,
`O=Lambda^2 U in SO(6)` is a `3 x 3` array of real `2 x 2` blocks `B_{alpha beta}`. Put

\[
D_{\alpha\beta}=\det B_{\alpha\beta},\qquad
R_{\alpha\beta}=\frac12\|B_{\alpha\beta}\|_F^2.
\]

For fixed support direction the nonconstant middle-layer support is exactly

\[
s(O)=\langle D,K\rangle+\frac12\langle R,X\rangle, \tag{2}
\]

with the structured spectral coefficient

\[
X_{\alpha\beta}=\Re(\eta p_\alpha q_\beta),
\]

where

\[
p=(a_1a_2+a_3a_4,\ a_1a_3+a_2a_4,\ a_1a_4+a_2a_3)
\]

and `q` is the analogous vector for `b`.

The latest complete campaign-lead result actually consumed is fleet03/B07 run
`20260922T074824Z-fleet03-B07-MOC4-r13`, theorem
`MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`, report blob
`7724d19f793eb934c5fcc2b469bb9d0a108da4eb`.  It proves that on a mixed-Schur singular pair at a genuine global support maximizer the pair kernel is a **full-Hessian kernel** and upgrades the pair Lyapunov--Schmidt reserve by an exact nonnegative generalized-Schur-complement cross reserve.  Its first unpaid implication is to compute the cross residual from the structured determinant/exterior-square variables and either pay the remaining quartic slack or force target safety.

The assigned OTHER-account partner result actually consumed and applied is fleet02/B08 run
`B08-20260922T063644Z-ab01c7`, theorem
`MOC4-COMMON-BLOCK-EXTERNAL-FACET-COLLAR-v1`, report blob
`0c44199b655f0d726b3d0b2ace56b40dde415bcb`.  It proves a global true-unitary support certificate on repeated/common-block boundary data whenever the 48 external Saxl quantities lie below the permutation endpoint maximum, and gives an open collar when the external gap is positive.  Thus the cross-root calculation below is used on the genuine generic/irreducible core; if a candidate sequence degenerates to an external-safe common-block face, the partner theorem already closes that limiting support direction.  A later B08 run was START-only at the read snapshot and is not claimed as a completed dependency.

The current lead reduction is therefore: a strict source-valid counterexample can be genericized and maximized, and then lies either on at least one mixed-Schur (`MSQR`) pair-Hessian boundary or in the all-six-negative-definite (`NDI`) branch.  This report attacks `MSQR` by explicitly evaluating the cross equations and the raw cross cubic covector required by the lead's abstract Schur-complement theorem.

## 2. Quadratic block polarization

For `2 x 2` real matrices define determinant polarization

\[
\delta(A,B)=\frac12\{\det(A+B)-\det A-\det B\},
\]

so `delta(A,A)=det A`.  For row plane `r` and block column `beta`, define

\[
\Phi_{r\beta}(A,B)
=K_{r\beta}\delta(A,B)+\frac{X_{r\beta}}4\langle A,B\rangle_F. \tag{3}
\]

Then the block contribution to (2) is exactly

\[
\Phi_{r\beta}(B_{r\beta},B_{r\beta}).
\]

This makes an important point explicit: as a function of the ambient `6 x 6` exterior matrix, the middle-layer support is quadratic.  All higher derivatives appearing on the unitary manifold come from the exponential `SO(6)` constraint, not from a higher-degree ambient objective.

## 3. New theorem — `MOC4-CROSS-ROOT-HESSIAN-FORMULA-v1`

Choose three distinct block rows `alpha,gamma,delta`.  For each block column `beta` write

\[
A_\beta=B_{\alpha\beta},\quad
G_\beta=B_{\gamma\beta},\quad
H_\beta=B_{\delta\beta}.
\]

Let `L_{alpha gamma}(Z)` be the genuine `SO(6)` generator with nonzero row-plane blocks

\[
\begin{pmatrix}0&Z\\-Z^T&0\end{pmatrix}
\]

on `alpha direct_sum gamma`, and similarly let `L_{alpha delta}(Y)` mix `alpha` with `delta`.
Because `SU(4)->SO(6)` through `Lambda^2` is onto, these are true-unitary tangent directions.

At any stationary point of the true-unitary support,

\[
\boxed{
\begin{aligned}
D^2s[ L_{\alpha\gamma}(Z),L_{\alpha\delta}(Y)]
=\sum_\beta\{&2\Phi_{\alpha\beta}(ZG_\beta,YH_\beta)\\
&-\Phi_{\gamma\beta}(G_\beta,Z^TYH_\beta)\\
&-\Phi_{\delta\beta}(H_\beta,Y^TZG_\beta)\}.
\end{aligned}} \tag{4}
\]

### Proof

Use the exponential chart `exp(tL+sM)O`.  The two first variations are

`L O=(ZG,-Z^T A,0)` and `M O=(YH,0,-Y^T A)`.

The mixed acceleration is

\[
\frac12(LM+ML)O
=(0,-\tfrac12 Z^TYH,-\tfrac12Y^TZG).
\]

For a quadratic ambient functional with associated symmetric bilinear form `Phi`, the mixed manifold Hessian is ambient second variation plus the gradient paired with this mixed acceleration.  Substitution gives (4). `QED`

Equation (4) is already the explicit block/minor evaluation of the lead's abstract condition
`D^2h[z,Y]=0`.

## 4. Matrix annihilator form

Let `cof` denote the `2 x 2` cofactor matrix, which is linear in dimension two.  Put

\[
\chi_\beta=2X_{\alpha\beta}-X_{\gamma\beta}-X_{\delta\beta},
\]

\[
P_{\alpha\gamma|\delta}
=\sum_\beta K_{\alpha\beta}\,\operatorname{cof}(G_\beta)H_\beta^T, \tag{5}
\]

and

\[
\begin{aligned}
Q_{\alpha\gamma|\delta}=\sum_\beta\bigg[
&-\frac{K_{\gamma\beta}}2\operatorname{cof}(G_\beta)H_\beta^T
-\frac{K_{\delta\beta}}2G_\beta\operatorname{cof}(H_\beta)^T\\
&+\frac{\chi_\beta}{4}G_\beta H_\beta^T\bigg].
\end{aligned} \tag{6}
\]

Using `cof(ZG)=cof(Z)cof(G)`, (4) becomes

\[
\boxed{
D^2s[L_{\alpha\gamma}(Z),L_{\alpha\delta}(Y)]
=\langle Y,\mathcal C_{\alpha\gamma|\delta}(Z)\rangle_F,
}\tag{7}
\]

with the **linear cross-root annihilator**

\[
\boxed{
\mathcal C_{\alpha\gamma|\delta}(Z)
=\operatorname{cof}(Z)P_{\alpha\gamma|\delta}
+ZQ_{\alpha\gamma|\delta}.
}\tag{8}
\]

Thus the lead's full-Hessian-nullity statement is not merely abstract.  If a pair
`{alpha,gamma}` is mixed-Schur singular and `Z_*` is its kernel matrix, then for the third row
`delta`

\[
\boxed{\operatorname{cof}(Z_*)P+Z_*Q=0.} \tag{9}
\]

Applying the same formula after viewing the same pair from the `gamma` endpoint
(`Z` replaced by `-Z^T` with the row labels exchanged) gives the second adjacent-root matrix equation.  These two `2 x 2` equations are all nontrivial cross-root quadratic annihilation equations in the left `SO(6)` tangent decomposition; the three within-plane `SO(2)` directions are exact blockwise symmetries of (2).

## 5. New algebraic gate on a mixed-Schur survivor

Use the lead's strict-sector normalization

\[
a=T-C>0,\qquad b=T+C>0,
\]

and let `u,v` be unit singular vectors for the equality singular value of the mixed block `M`.
In the conformal/anticonformal basis `E_1,E_2,F_1,F_2`, choose the canonical kernel matrix

\[
Z_*=\sqrt b\,U_c+\sqrt a\,V_a,
\]

where `U_c=u_1E_1+u_2E_2` is conformal and
`V_a=v_1F_1+v_2F_2` is anticonformal.  Then exactly

\[
\boxed{\det Z_*=b-a=2C,\qquad \|Z_*\|_F^2=2(a+b)=4T.} \tag{10}
\]

Assume first `C != 0`.  Multiply (9) on the left by `Z_*^T` and use
`Z^T cof(Z)=det(Z)I`.  With

\[
S_*=Z_*^TZ_*>0
\]

we obtain

\[
\boxed{S_*Q=-2C\,P,\qquad \det S_*=4C^2,\qquad \operatorname{tr}S_*=4T.} \tag{11}
\]

This yields three immediately testable polynomial conditions on every generic mixed-Schur
survivor:

\[
\boxed{\det P=\det Q,} \tag{12}
\]

\[
\boxed{P\,\operatorname{adj}(Q)\ \text{is symmetric},} \tag{13}
\]

and

\[
\boxed{2T\det Q+C\operatorname{tr}(P\operatorname{adj}Q)=0.} \tag{14}
\]

If `Q` is invertible these sharpen to

\[
\boxed{-PQ^{-1}=\frac{S_*}{2C},\quad
\det(PQ^{-1})=1,\quad
\operatorname{tr}(PQ^{-1})=-\frac{2T}{C},\quad
-C\,PQ^{-1}>0.} \tag{15}
\]

So mixed-Schur equality plus global maximality forces a very specific symmetric-definite
`SL_2(R)` matrix, not merely the scalar pair-Hessian equality.

If `C=0`, then `det Z_*=0` while `Z_*` is nonzero rank one.  Equation (9) instead gives

\[
Z_*^TZ_*Q=0,
\]

hence

\[
\boxed{\det Q=0} \tag{16}
\]

for each adjacent cross-root operator.  Thus the `C=0` branch is also forced onto an explicit
algebraic locus rather than escaping (12)--(15) without replacement.

I call (12)--(16) **`MOC4-MSQR-CROSS-ROOT-ALGEBRAIC-GATE-v1`**.
They do not by themselves close `MSQR`, but any proposed mixed-Schur positive-gap maximizer
failing either adjacent-root gate is now excluded immediately.

## 6. New theorem — explicit raw cross cubic covector

The campaign lead's newest theorem needs not only the cross Hessian but the cubic covector
`beta(Y)=D^3s[Z_*,Z_*,Y]`.  The same ambient-quadratic structure permits an exact formula.

Let `Z` be any `alpha-gamma` pair direction, put

\[
S=ZZ^T,
\]

and let `Y` be an `alpha-delta` pair direction.  Direct third-order expansion of
`exp(tL_{alpha gamma}(Z)+sL_{alpha delta}(Y))` gives

\[
\boxed{
\begin{aligned}
D^3s[Z,Z,Y]=2\sum_\beta\bigg[&\frac13\{-\Phi_{\alpha\beta}(A_\beta,SYH_\beta)
+\Phi_{\delta\beta}(H_\beta,Y^TSA_\beta)\}\\
&-\Phi_{\alpha\beta}(YH_\beta,SA_\beta)
+\Phi_{\gamma\beta}(Z^TA_\beta,Z^TYH_\beta)\bigg].
\end{aligned}} \tag{17}
\]

Equivalently,

\[
D^3s[Z,Z,Y]=\langle Y,\mathcal B_{\alpha\gamma|\delta}(Z)\rangle_F, \tag{18}
\]

where, writing

\[
\nu_\beta=3X_{\gamma\beta}+X_{\delta\beta}-4X_{\alpha\beta},
\]

\[
\boxed{
\begin{aligned}
\mathcal B_{\alpha\gamma|\delta}(Z)=\sum_\beta\bigg[
&-\frac{K_{\alpha\beta}}3S\operatorname{cof}(A_\beta)H_\beta^T
+\frac{K_{\delta\beta}}3SA_\beta\operatorname{cof}(H_\beta)^T\\
&-K_{\alpha\beta}\operatorname{cof}(SA_\beta)H_\beta^T
+K_{\gamma\beta}\det(Z)\operatorname{cof}(A_\beta)H_\beta^T\\
&+\frac{\nu_\beta}{6}SA_\beta H_\beta^T\bigg].
\end{aligned}} \tag{19}
\]

This is the requested explicit exterior-block evaluation of the **cross component** of the
lead's cubic covector.

## 7. Direct formula for the lead's residual-zero equations

Let `B_pair=-H_pair>=0` on the singular pair slice, and let `u_pair` be the same-pair component
of the cubic covector `beta#`.  In the lead's conformal/anticonformal coordinate convention let
`W_0` be the actual `2 x 2` pair matrix corresponding to

\[
B_{pair}^+u_{pair}.
\]

The generalized-Schur residual is

\[
r=v-C^TB_{pair}^+u_{pair}.
\]

By (8) and (19), its component on the adjacent root `alpha-delta` is represented exactly by

\[
\boxed{
\mathcal R_{\alpha\gamma|\delta}
=\mathcal B_{\alpha\gamma|\delta}(Z_*)
-\mathcal C_{\alpha\gamma|\delta}(W_0).
}\tag{20}
\]

The analogous equation with the other endpoint of the singular pair gives the second adjacent
root component.  Therefore the lead's exceptional branch `r=0` is no longer an unspecified
full-tangent condition: after the already-known same-pair cubic polarization is inserted, it is
a finite system of **two explicit `2 x 2` matrix equations** of the form (20), together with the
quadratic annihilator equations (9).  Exact blockwise `SO(2)` symmetry accounts for the remaining
within-plane tangent directions.

This is the main handoff from this run.  It provides the concrete quantities needed to test or
bound the new positive cross reserve `3<r,S^+r>` in `MOC4-MSQR-CROSS-RESERVE-PAYMENT-v1`.

## 8. Conditional end-to-end implication after this run

Assume a strict MOC4 support violation and take a genuine global maximizer on the generic
simple/nonzero/cross-ratio-conditioned locus.  The current proof tree is exhaustive:

1. If a pair block is mixed-Schur singular, the lead gives a full-Hessian kernel `Z_*` and the
   full quartic reserve.  This run forces, for both adjacent roots, (9), the algebraic gates
   (12)--(16), and the explicit residual equations (20).  Thus `MSQR` closes if one proves that
   these structured equations either make the cross reserve exceed the available pair quartic
   slack or force support safety.
2. If all six pair blocks are negative definite, the separate `NDI` cross-root/Cartan closure is
   still required.
3. If a degeneration lands on a repeated/common-block boundary with nonnegative external gap,
   the assigned fleet02/B08 external-facet collar already certifies the true-unitary support
   inequality there (strictly on an open collar when the gap is positive).

Hence the first remaining implication on the branch attacked here is now narrower:

**`MOC4-MSQR-EXPLICIT-CROSS-RESERVE-PAYMENT-v2`** — substitute the existing exact same-pair
`J3/J4` data into `W_0`, use (20) for both adjacent roots, and prove either
`3<r,S^+r>` overdraws the pair quartic slack or the simultaneous residual-zero/algebraic-gate
system is target-safe.  No arbitrary bistochastic, unrestricted compound-minor, or free `SO(6)`
point may replace the common unitary.

## 9. Exact verification

`VERIFY_CROSS_ROOT.py` expands the true `SO(6)` exponential chart through degree three with exact
SymPy rational arithmetic and independently checks (4), (8), (17), and (19).  On its fixed
rational normalization datum it gives

- mixed Hessian coefficient `10891/84` from both derivations;
- mixed cubic coefficient `-38483/126` from both derivations.

It separately checks the algebraic consequences of (9) on a synthetic exact kernel normalization
with

\[
Z_*=\operatorname{diag}(3,1),\quad T=5/2,\quad C=3/2,
\]

obtaining `det P=det Q=5`, `tr(PQ^{-1})=-10/3=-2T/C`, and

\[
-C P Q^{-1}=\operatorname{diag}(9/2,1/2)>0.
\]

This synthetic calculation is only a factor/sign check for the algebraic theorem; it is not a
MOC4 witness.

## 10. Claim limits

- Full MOC4 remains open; no target-level proof or counterexample is claimed.
- The new equations are necessary conditions on a mixed-Schur global maximizer, not a proof that
  such a maximizer exists.
- No dimension-count/transversality shortcut is used to declare the algebraic locus empty.
- No unavailable historical context or brain retrieval is claimed.
- No benchmark data or sealed answers were used.

**Verdict:** `ESSENTIAL_STEP_APPLIED`.  The lead's abstract cross-Hessian-null and cross-cubic
residual objects have been evaluated explicitly in the `4 x 4` exterior-block variables.  A
mixed-Schur survivor must now satisfy two concrete matrix annihilator systems and, on `C != 0`,
a symmetric-definite `SL_2` algebraic constraint, while the exceptional residual-zero branch is
reduced to explicit matrix equations (20).
