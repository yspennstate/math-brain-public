# MOC4 account03/B07 — full pair-Hessian anisotropy gate

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Target:** Marcus–de Oliveira, complex normal `4 x 4` case  
**Worker/run:** account03/B07, `20260922T055130Z-account03-B07-MOC4-r11`  
**Role:** account03 team lead  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Fresh compatible state and named other-account result consumed

Fresh owner control revision `2026-09-22.2` keeps B07 on MOC4 under `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`.

The named other-account result consumed directly in this run is **account04/B09 `MOC4-REL-STATIONARY-24ROOF-v1`**, report commit `126eef8c1843137b4e827a013b9ae6667000e420`. Its reduction says that a genuine counterexample support maximizer in the retained generic branch must simultaneously be left/right stationary, satisfy every pair gate `T>=|C|`, obey the pair structural relation, and evade all 24 subgroup roofs. This report attacks the missing *local true-unitary stationarity rigidity* by deriving the full four-real-dimensional second-order gate for each pair, instead of keeping only the two orthogonal-sector scalar inequalities.

The exact block notation is the one used in account01/B07 `MOC4-BIORIENTATION-PAIR-GATE-v1` (`REPORT.md` blob `629288d290e89315693afda2f95b48ad8c23a8e3`): after a harmless phase,

\[
O=\Lambda^2U\in SO(6),\qquad
s(O)=\langle D,K\rangle+\frac12\langle R,X\rangle,
\]

where `O` is written as a `3 x 3` array of real `2 x 2` blocks `B_{alpha beta}`, with

\[
D_{\alpha\beta}=\det B_{\alpha\beta},\qquad
R_{\alpha\beta}=\frac12\|B_{\alpha\beta}\|_F^2.
\]

Everything below is a constraint on the same genuine exterior-square point. No arbitrary bistochastic surrogate is introduced.

## 2. New theorem — `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`

Fix a row-plane pair `alpha<gamma` and abbreviate, for each block column `beta`,

\[
A_\beta=B_{\alpha\beta},\qquad G_\beta=B_{\gamma\beta},\qquad
\delta X_\beta=X_{\alpha\beta}-X_{\gamma\beta}.
\]

Put

\[
A_0=\sum_\beta\left(K_{\alpha\beta}D_{\alpha\beta}+K_{\gamma\beta}D_{\gamma\beta}\right),
\]

\[
C=C^L_{\alpha\gamma}=\sum_\beta\left(K_{\alpha\beta}D_{\gamma\beta}+K_{\gamma\beta}D_{\alpha\beta}\right),
\]

and

\[
T=T^L_{\alpha\gamma}=A_0+\frac12\sum_\beta\delta X_\beta\left(R_{\alpha\beta}-R_{\gamma\beta}\right).
\]

For an arbitrary real `2 x 2` matrix `Z`, let `L_Z` be the skew-symmetric `6 x 6` generator that mixes only these two row planes:

\[
L_Z\big|_{\alpha\oplus\gamma}=
\begin{pmatrix}0&Z\\-Z^T&0\end{pmatrix}.
\]

Then `exp(tL_Z)O` stays in `SO(6)` and, by the exact `SU(4)->SO(6)` exterior-square covering used throughout the campaign, is the exterior square of a genuine unitary path. Hence these are true-unitary tangent directions for **every** real `Z`.

At a local support maximizer define

\[
H_{\alpha\gamma}(Z)=\left.\frac{d^2}{dt^2}s(e^{tL_Z}O)\right|_{t=0}.
\]

Then

\[
\boxed{
H_{\alpha\gamma}(Z)=
-A_0\|Z\|_F^2+2C\det Z
+\frac12\sum_\beta\delta X_\beta
\left[
\operatorname{tr}(Z^TZ\,G_\beta G_\beta^T)
-\operatorname{tr}(Z^T A_\beta A_\beta^T Z)
\right].
}\tag{1}
\]

In particular `H_{alpha gamma}(Z)<=0` for every real `Z`.

### Proof of (1)

Along this path the two affected block rows obey

\[
A_\beta'=ZG_\beta,\qquad G_\beta'=-Z^TA_\beta,
\]

\[
A_\beta''=-ZZ^TA_\beta,\qquad G_\beta''=-Z^TZG_\beta.
\]

For `2 x 2` matrices, if `q` is determinant polarization then

\[
\frac{d^2}{dt^2}\det A(t)\big|_0=q(A,A'')+2\det A',
\]

and the polynomial identity

\[
q(A,SA)=\operatorname{tr}(S)\det A
\]

holds without any invertibility assumption. Therefore the determinant part contributes

\[
-A_0\|Z\|_F^2+2C\det Z.
\]

For `R(A)=\frac12\|A\|_F^2`,

\[
R(A_\beta)''=\|ZG_\beta\|_F^2-\langle A_\beta,ZZ^TA_\beta\rangle,
\]

\[
R(G_\beta)''=\|Z^TA_\beta\|_F^2-\langle G_\beta,Z^TZG_\beta\rangle
=-R(A_\beta)''.
\]

Multiplying by the exact support coefficients `X/2` gives the last term in (1). This proves (1). `QED`

## 3. Four-dimensional Hessian block and the new coupling inequality

Use the Frobenius-orthogonal basis

\[
E_1=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
E_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
F_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
F_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

The `E` plane is conformal (`det>=0`) and the `F` plane anticonformal (`det<=0`). The already-known pair-circle gates are exactly

\[
H(E_1)=H(E_2)=-2(T-C),\qquad
H(F_1)=H(F_2)=-2(T+C),
\]

with zero within-sector cross terms.

Define the mixed `2 x 2` matrix `M=M_{alpha gamma}` by polarization,

\[
M_{ij}=\frac12\{H(E_i+F_j)-H(E_i)-H(F_j)\}.
\]

By (1),

\[
M_{ij}=\frac14\sum_\beta\delta X_\beta
\left[
\operatorname{tr}((E_i^TF_j+F_j^TE_i)G_\beta G_\beta^T)
-2\operatorname{tr}(E_i^T A_\beta A_\beta^T F_j)
\right].\tag{2}
\]

Thus the full pair Hessian in coordinates `(E_1,E_2,F_1,F_2)` is

\[
\mathcal H_{\alpha\gamma}=
\begin{pmatrix}
-2(T-C)I_2 & M\\
M^T & -2(T+C)I_2
\end{pmatrix}.\tag{3}
\]

Negative semidefiniteness of (3) is equivalent to the old sector conditions `T>=|C|` together with the genuinely new mixed-sector gate

\[
\boxed{\|M_{\alpha\gamma}\|_{\mathrm{op}}^2\le 4\,(T_{\alpha\gamma}^2-C_{\alpha\gamma}^2).}\tag{4}
\]

The same theorem holds for every column-plane pair by right multiplication.

## 4. Stronger anisotropy form

Define the weighted symmetric Gram sums

\[
\mathsf A=\sum_\beta\delta X_\beta A_\beta A_\beta^T,
\qquad
\mathsf G=\sum_\beta\delta X_\beta G_\beta G_\beta^T.
\]

For a real symmetric `2 x 2` matrix `S`, write

\[
\rho(S)=\sqrt{\left(\frac{S_{11}-S_{22}}2\right)^2+S_{12}^2}
=\frac1{\sqrt2}\left\|S-\frac{\operatorname{tr}S}{2}I_2\right\|_F.
\]

Writing

\[
\mathsf G=\begin{pmatrix}g_{11}&g_{12}\\g_{12}&g_{22}\end{pmatrix},
\quad
\mathsf A=\begin{pmatrix}a_{11}&a_{12}\\a_{12}&a_{22}\end{pmatrix},
\]

(2) gives explicitly

\[
M=
\begin{pmatrix}
\frac{g_{11}-g_{22}}2-\frac{a_{11}-a_{22}}2 & g_{12}-a_{12}\\
-g_{12}-a_{12} & \frac{g_{11}-g_{22}}2+\frac{a_{11}-a_{22}}2
\end{pmatrix}.
\]

Its singular values are

\[
\rho(\mathsf G)+\rho(\mathsf A),\qquad
|\rho(\mathsf G)-\rho(\mathsf A)|.
\]

Therefore (4) is exactly

\[
\boxed{
\bigl(\rho(\mathsf A)+\rho(\mathsf G)\bigr)^2
\le 4\,(T^2-C^2).
}\tag{5}
\]

This is strictly stronger information than `T>=|C|` unless the weighted Gram anisotropies vanish.

### Flat-pair rigidity corollary

If a pair gate saturates at a local/global maximizer,

\[
T=|C|,
\]

then (5) forces

\[
\boxed{
\sum_\beta\delta X_\beta\left(A_\beta A_\beta^T-\frac{\operatorname{tr}(A_\beta A_\beta^T)}2I_2\right)=0,
}\tag{6a}
\]

\[
\boxed{
\sum_\beta\delta X_\beta\left(G_\beta G_\beta^T-\frac{\operatorname{tr}(G_\beta G_\beta^T)}2I_2\right)=0.
}\tag{6b}
\]

Hence a support-flat pair sector cannot carry arbitrary transverse anisotropy: both weighted traceless Gram sums vanish separately.

Because block-row orthogonality also gives the unweighted identities

\[
\sum_\beta\operatorname{tf}(A_\beta A_\beta^T)=0,
\qquad
\sum_\beta\operatorname{tf}(G_\beta G_\beta^T)=0,
\]

if the three weights `delta X_beta` are distinct, the three traceless Gram vectors in either affected row must be collinear. Explicitly, each triple is proportional (as a triple of vectors in the two-dimensional traceless-symmetric space) to

\[
(\delta X_2-\delta X_3,\ \delta X_3-\delta X_1,\ \delta X_1-\delta X_2).
\tag{7}
\]

This converts pair-flatness into an exact low-dimensional algebraic rigidity condition on the same true exterior-square point.

## 5. Smallest conditional full deduction now visible

The current generic residual can be closed if one proves the following same-unitary implication.

**`MOC4-FLAT-PAIR-MIXED-RIGIDITY-v1` (missing).** At a genuine global support maximizer satisfying the existing exact `P/R/D` compatibility, the 24 subgroup roofs, and the row/column stationarity conditions, a saturated pair sector together with (6)–(7) forces either:

1. a proper coordinate/block boundary already covered by the campaign's boundary/circle-face reductions, or
2. a second compatible saturated row/column pair whose combined Gram-collinearity constraints force the support to an endpoint roof.

More generally, away from pair saturation, the full theorem would follow from the finite residual implication that no true-unitary stationary point satisfying all row **and** column versions of (5), all 24 roofs, and the exact same-unitary identities can have support above the permutation maximum.

The first implication to attack is therefore no longer “derive more stationarity”; it is the concrete algebraic classification of true `SO(6)=Lambda^2 SU(4)` block arrays obeying the flat-pair Gram cancellation (6) and collinearity (7).

## 6. Why this is not a bistochastic relaxation

Every perturbation used above is `exp(tL_Z)O` with `L_Z in so(6)`. The `Spin(6)=SU(4)` covering lifts it to a genuine unitary path. The proof never optimizes over free doubly-stochastic `R`, free unistochastic `P`, or independent `D`; all block quantities belong to one exterior-square image of one unitary.

## 7. Status and next exact subclaims

MOC4 remains **OPEN**. This run proves an additional necessary second-order compatibility theorem and a strong saturation corollary; it does not claim the target theorem.

Suggested same-account subclaims for the shared handoff:

- **B08 / geometric route:** classify the true-unitary flat-pair locus under (6)–(7), looking first for forced zero-entry/common-reducing-block faces.
- **B09 / verification route:** encode the left/right full Hessian gate (5) together with `D=(1/4)E^TPE`, `R>=|D|`, orthogonality, and the 24 roofs; search for a genuine stationary positive-support witness or certify small algebraic strata. Any computational output remains diagnostic unless converted to an exact certificate.
- **B07 / lead integration:** combine any resulting flat-locus classification with the existing boundary/circle-face closures and maintain the authoritative proof tree.
