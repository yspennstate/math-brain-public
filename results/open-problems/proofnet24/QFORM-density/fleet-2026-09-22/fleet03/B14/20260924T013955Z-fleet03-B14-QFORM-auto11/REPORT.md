SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-24T01:39:55Z.
attacking: zero-tax localization from a diffuse three-bank compression to the valid three-variable affine theorem, preserving translations, remote fragments, unbounded supports and arbitrary outside curvature.

# fleet03/B14 — disjoint-bank Schur localization

Run: `20260924T013955Z-fleet03-B14-QFORM-auto11`.
Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING LOCALIZATION THEOREM / PARTNER RESULT APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. No Gaussian, log-concavity, moment, compact-support, connected-support, finite-fragment, post-rotation independence, arbitrary-joint coarea, conditional-density-cap, or law-uniform pointwise van-der-Corput premise is used.

## 1. Valid premises actually used

### Product projection cap
For independent real coordinates with marginal densities bounded by one, every one-dimensional linear form
\[
S=\sum_i a_iX_i
\]
with coefficient vector `a!=0` has a density satisfying the Ball--Rogozin bound
\[
\|p_S\|_\infty\le \frac{\sqrt2}{\|a\|_2}.
\tag{1}
\]
This source-valid scalar projection input requires no support, moment, centering or regularity hypothesis.

### Designated partner result
The completed fleet04/B14 theorem actually applied is

- repository: `yspennstate/math-open-problems`,
- commit: `deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`,
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T001624Z-fleet04-B14-scaled-schur-localization-r10/REPORT.md`,
- theorem: scale-covariant three-coordinate Schur localization.

Its exact input needed here is: for three independent cap-one real variables `Z=(Z1,Z2,Z3)` and every invertible real symmetric `3x3` matrix `H`, arbitrary deterministic affine term `ell^T Z+c` has output density
\[
\|p_{Z^THZ+\ell^TZ+c}\|_{\infty,\mathrm{ess}}
\le \frac{6\sqrt\pi}{\sigma_{\min}(H)},
\tag{2}
\]
where `sigma_min(H)` means the minimum absolute eigenvalue. The theorem is translation-uniform and imposes no moment or support condition. It is an essential-height theorem; continuity is not part of that source conclusion.

## 2. New theorem: disjoint-bank Schur localization

### Theorem `QFORM-DISJOINT-BANK-SCHUR-LOCALIZATION-v1`

Let the original coordinate set be partitioned as
\[
I_1\sqcup I_2\sqcup I_3\sqcup J.
\]
For `r=1,2,3`, let `u_r` be a nonzero coefficient vector supported on `I_r`; set
\[
\rho_r=\|u_r\|_2>0,
\qquad
U=[u_1\ u_2\ u_3]\in\mathbb R^{|I|\times3},
\qquad I=I_1\sqcup I_2\sqcup I_3.
\]
Assume the symmetric matrix `A` has the exact block form
\[
A=
\begin{pmatrix}
UBU^T & UC\\
C^TU^T & D
\end{pmatrix}
\tag{3}
\]
relative to `I\sqcup J`, where `B` is an invertible real symmetric `3x3` matrix, `C` is arbitrary, and `D` is arbitrary symmetric.

Define
\[
R=\operatorname{diag}(\rho_1,\rho_2,\rho_3),
\qquad
\tau=\sigma_{\min}(RBR)>0.
\tag{4}
\]
Then for every vector of independent real inputs with marginal density caps at most one,
\[
\boxed{
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}
\le \frac{12\sqrt\pi}{\tau}.
}
\tag{5}
\]
The same bound holds after arbitrary deterministic translations of any or all original coordinates. More generally, it survives deterministic affine perturbations whose active-bank component lies in `col(U)`; the outside `J` component may be arbitrary. The estimate is independent of dimension, all support diameters, fragment counts and separations, tails, moments, the outside block `D`, and the aligned exterior coupling `C`.

If the three bank vectors are unit (`rho_r=1`), then
\[
\boxed{
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}
\le \frac{12\sqrt\pi}{\sigma_{\min}(B)}.
}
\tag{6}
\]

### Proof

Write
\[
Y_r=u_r^TX_{I_r},\qquad Y=(Y_1,Y_2,Y_3)^T.
\tag{7}
\]
The three source sets `I_1,I_2,I_3` are disjoint and the original coordinates are independent, hence `Y_1,Y_2,Y_3` are genuinely independent. No rotated-coordinate independence is asserted.

By (1),
\[
\|p_{Y_r}\|_\infty\le \frac{\sqrt2}{\rho_r}.
\tag{8}
\]
Define the rescaled variables
\[
Z_r=\frac{\sqrt2}{\rho_r}Y_r,
\qquad
Z=\sqrt2\,R^{-1}Y.
\tag{9}
\]
For a scalar scaling `Z_r=c_rY_r`, the density transforms by `p_Z(z)=c_r^{-1}p_Y(z/c_r)`. Therefore (8) gives
\[
\|p_{Z_r}\|_\infty\le1.
\tag{10}
\]
The variables `Z_r` remain independent.

Now condition only on the outside ORIGINAL coordinates `X_J=x`. From (3),
\[
X^TAX
=Y^TBY+2Y^TCx+x^TDx.
\tag{11}
\]
Using `Y=(1/\sqrt2)RZ`,
\[
X^TAX
=Z^T H Z+\ell_x^TZ+c_x,
\tag{12}
\]
with
\[
H=\frac12RBR,
\qquad
\ell_x=\sqrt2\,RCx,
\qquad
c_x=x^TDx.
\tag{13}
\]
The partner theorem (2) applies on every conditional fiber because `Z_1,Z_2,Z_3` are independent cap-one variables. Since
\[
\sigma_{\min}(H)=\frac12\sigma_{\min}(RBR)=\frac\tau2,
\tag{14}
\]
it gives uniformly in every outside value `x`,
\[
\Pr\{X^TAX\in K\mid X_J=x\}
\le \frac{12\sqrt\pi}{\tau}|K|
\tag{15}
\]
for every interval `K`. Integrating over `x` proves (5).

No normalization of an outside fragment occurs. If the outside law is decomposed as a finite or countable sum of subprobability measures `sum_s nu_s` with masses `m_s`, (15) integrates to `m_s(12sqrt(pi)/tau)|K|` on each piece, and summing gives exactly (15) with total mass one. Thus arbitrarily remote fragments pay zero count or separation tax.

For a deterministic coordinate translation `X -> X+s`, the induced active-bank linear coefficient is the `I` component of `2As`, namely
\[
2U\big(BU^Ts_I+Cs_J\big),
\tag{16}
\]
which lies in `col(U)`. Hence it becomes only an affine term in the three compressed variables in (12); the quadratic matrix `H` and `tau` are unchanged. An additional deterministic affine term is covered by the same argument whenever its active-bank component lies in `col(U)`; an arbitrary affine term on the outside coordinates becomes a scalar after conditioning. This proves the stated translation/affine scope. QED.

## 3. Why this is not merely the physical-triple theorem

The new theorem can stay uniform when **every** physical `3x3` principal block becomes badly conditioned.

For each integer `m>=1`, split `3m` original coordinates into three groups `I_1,I_2,I_3` of size `m`, and let
\[
u_r=m^{-1/2}\mathbf1_{I_r}.
\tag{17}
\]
The vectors `u_1,u_2,u_3` are orthonormal and have disjoint supports. Let
\[
B_*=I_3-\frac23\mathbf1\mathbf1^T
=
\begin{pmatrix}
1/3&-2/3&-2/3\\
-2/3&1/3&-2/3\\
-2/3&-2/3&1/3
\end{pmatrix}.
\tag{18}
\]
Then `B_*^2=I_3`, so
\[
\operatorname{spec}(B_*)=\{1,1,-1\},
\qquad
\sigma_{\min}(B_*)=1.
\tag{19}
\]
Define the exact-rank-three target matrix
\[
A_m=UB_*U^T.
\tag{20}
\]
Because `U^TU=I_3`, the nonzero spectrum of `A_m` is exactly `{1,1,-1}`. Hence every `A_m` satisfies the owner's exact three-large-eigenvalue hypothesis.

For a physical principal triple `S`, let `P_S` record which of the three banks its coordinates came from. Then
\[
(A_m)_{S,S}=\frac1m P_SB_*P_S^T.
\tag{21}
\]
If two selected coordinates lie in the same bank, `P_S` has repeated rows and the block is singular. If one coordinate is selected from each bank, `P_S` is a permutation matrix and the block has minimum absolute eigenvalue exactly `1/m`. Thus the designated partner's direct physical-triple estimate alone is at best
\[
6\sqrt\pi\,m,
\tag{22}
\]
which diverges.

The new bank compiler instead aggregates each entire original-coordinate bank **before** paying inverse curvature. Since the `u_r` are unit, (6) gives
\[
\boxed{
\|p_{X^TA_mX}\|_{\infty,\mathrm{ess}}
\le 12\sqrt\pi
=21.269446210866\ldots
}
\tag{23}
\]
for every `m` and every admissible cap-one product law. This is a genuine diffuse, dense-in-bank, rotated target chamber. No physical principal block has a universal conditioning constant as `m->infinity`, but the three disjoint product banks retain the needed localization.

The same conclusion survives arbitrary extra outside coordinates and arbitrary outside quadratic block `D` provided the coupling from the three active banks to the outside factors through `U` as in (3). That aligned-coupling extension is the localization gain over the bare exact-rank-three example.

## 4. Relation to current corrections

This theorem does **not** use the false arbitrary-joint 3D coarea lemma. The projected bank vector `Y` is special for a stronger reason: its three coordinates come from disjoint original source blocks and are therefore independent. It also does not use any worst conditional projection-density moment; the scalar Ball--Rogozin cap is applied before conditioning on anything inside a bank.

It does not assert that the three-large-eigenvalue hypothesis forces a decomposition (3). The correction family `A=[1] direct_sum J_m/m direct_sum(-J_m/m)` and other diffuse examples already show why one uniformly conditioned physical triple need not exist. The new theorem instead shows that a diffuse **bank-compressible** form can be localized with zero support/translation/tail tax even when physical triples collapse.

No pointwise law-uniform quadratic-phase decay is used. No Monte Carlo or interval extremality claim enters the proof.

## 5. Continuity ledger

The conclusion proved here is an essentially bounded density. The fleet04/B14 r10 source theorem used in the proof does not itself claim continuity, so this report does not upgrade (5) to a continuous representative. Full-target continuity remains OPEN.

## 6. Exact remaining implication

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The missing structural bridge is now sharper:

> Starting only from `s_3(A)>=1`, either extract a paid physical triple / cross-volume chamber already covered by the fleet, or produce a three-bank compression whose within-bank and outside couplings factor through the three bank projections with `sigma_min(RBR)` universally bounded below, or develop an overlap-preserving analogue that tolerates the orthogonal within-bank residuals.

The difficult part is the last clause: for a generic matrix, conditioning away those residual directions can destroy the original product provenance. This report therefore does not rename a structured chamber as a full solution.

## 7. Quantitative checks

For the control family (18)--(20):

- `eig(B_*)=(-1,1,1)`;
- `B_*^2=I_3` exactly;
- `12sqrt(pi)=21.269446210866192`;
- every one-per-bank physical triple has `sigma_min=1/m`;
- every triple with a repeated bank membership is singular.

A separate `CHECKS.md` records the algebra and scale transformations.

## 8. Integrity and execution

Repository transport and native learned-memory ingestion remain separate. This run used authenticated repository retrieval and readback, but no authenticated native receiver-memory ingestion was observed; execution therefore remains `WITHOUT_VERIFIED_BRAIN`.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort is `UNKNOWN` because the current fleet03 inventory explicitly says the configured model/reasoning selector fields are not exposed. Provider reasoning-token and thinking-time counters are not exposed and are not estimated. Existing hourly task state and quiet delivery were left unchanged; no email, push, task creation, task duplication, cross-account authentication, paid API/Codex action, remote workflow or public release was performed.
