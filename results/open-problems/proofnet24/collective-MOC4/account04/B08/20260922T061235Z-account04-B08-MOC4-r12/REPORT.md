# MOC4 account04/B08 — strict Spin(4) sectors and mixed-Hessian boundary gates

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T061235Z-account04-B08-MOC4-r12`  
**Campaign:** Marcus–de Oliveira, complex normal `4 x 4` case  
**Role:** extremal boundary / degeneracy classification  
**Assigned partner:** account01/B09  
**Team lead:** account03/B07  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN_RESEARCH`; `full_brain_connected=false`.

## 1. Fresh compatible source state

The latest complete team-lead report was re-resolved after this run began and is account03/B07,
`proofnet24/collective-MOC4/account03/B07/20260922T060726Z-account03-B07-MOC4-r11/REPORT.md`, blob
`c8911d75149115eb15810e4f8fac624cfc5e34f5`, result `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`.
It starts from the lead's exact mixed-conformal Hessian theorem. In the real exterior-square model

\[
O=\Lambda^2 U\in SO(6),\qquad
s(O)=\langle D,K\rangle+\frac12\langle R,X\rangle,
\]

write `O` as a `3 x 3` array of real `2 x 2` blocks. For a selected block-row pair the four-dimensional true-unitary Hessian is

\[
\mathcal H=
\begin{pmatrix}
-2(T-C)I_2&M\\
M^T&-2(T+C)I_2
\end{pmatrix}\preceq0,
\tag{1}
\]

so

\[
T\ge |C|,\qquad \|M\|_{op}^2\le4(T^2-C^2).
\tag{2}
\]

The newest lead report identifies the conformal and anticonformal sectors with the two coordinate `SU(2)` factors of the relevant `Spin(4)` subgroup and proves that `T=|C|` makes one genuine coordinate pair orbit support-flat. It then sends that flat orbit to an equal-support zero-entry representative.

I also consume the complete account04/B09 theorem `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`,
`proofnet24/collective-MOC4/account04/B09/20260922T022417Z-b09-moc4-r11/REPORT.md`, blob
`1ec092caac4aa78fb3998199849f632387a0c18f`. It proves that the full exterior-minor data Haar-averaged over any coordinate row-pair or column-pair embedded `SU(2)` orbit have an exact positive lift to the 24 permutation endpoints. Hence a support functional that is constant on such an orbit is automatically at most the target permutation maximum. This is stronger than merely moving a flat orbit to a zero-entry point.

The named assigned OTHER-account result consumed is the latest complete account01/B09 report,
`proofnet24/collective-MOC4/account01/B09/b09-20260922T054641Z-moc4-r11/REPORT.md`, blob
`b12c5f150c244bcb5c6111233a8dcac845ee07b3`, result `MOC4-NONSINGULAR-STRICT-STATIONARY-LIFT-NOGO-v1`. Its genuine dense example is simple-spectrum, nonsingular, fully first-order stationary and strict top-Rayleigh on all twelve coordinate pair orbits, yet it has a rigorously positive mixed second derivative. Thus strict pair optimality alone cannot replace (1)-(2).

## 2. Compact conditional end-to-end chain

If MOC4 fails, support separation and compactness give a real support direction and a genuine global maximizer `U_*` with

\[
h(U_*)=M+\gamma,\qquad \gamma>0,
\tag{3}
\]

where `M` is the largest of the 24 endpoint supports.

The newest lead theorem says a saturated scalar Spin(4) sector `T=|C|` is an exactly flat coordinate `SU(2)` pair orbit. Account04/B09 says the Haar average of that entire orbit has a positive common endpoint lift. Since the support is constant on the orbit, its value equals the support of that endpoint mixture and is therefore at most `M`. This contradicts (3).

Consequently **no support-violating global maximizer can have `T=|C|` on any left or right Spin(4) gate**. The lead's saturation-to-zero-face branch can be strengthened to direct target safety; no separate zero-face inequality is needed merely to dispose of a saturated Spin(4) sector.

After that strictness reduction, the only singular boundary inside one four-dimensional pair Hessian is the genuinely mixed Schur-complement equality in (2). Sections 5-6 derive exact third- and fourth-order conditions on that remaining boundary.

## 3. Explicit root dictionary

For independent verification of the lead's Spin(4) identification, let `e_rs=e_r wedge e_s`. The real form of `Lambda^2 C^4` fixed by Hodge-star conjugation has three real two-planes

\[
V_0:\ \frac{e_{01}+e_{23}}{\sqrt2},\ \frac{i(e_{01}-e_{23})}{\sqrt2},
\]
\[
V_1:\ \frac{e_{02}-e_{13}}{\sqrt2},\ \frac{i(e_{02}+e_{13})}{\sqrt2},
\]
\[
V_2:\ \frac{e_{03}+e_{12}}{\sqrt2},\ \frac{i(e_{03}-e_{12})}{\sqrt2}.
\tag{4}
\]

For each coordinate pair `r<s`, the embedded row-pair `SU(2)` root plane is spanned by

\[
X_{rs}=E_{rs}-E_{sr},\qquad Y_{rs}=i(E_{rs}+E_{sr}).
\tag{5}
\]

Using

\[
d(\Lambda^2)(Z)(u\wedge v)=Zu\wedge v+u\wedge Zv,
\tag{6}
\]

one obtains exactly:

| coordinate pair | active block planes | Spin(4) sector |
|---|---|---|
| `01` | `V_1 <-> V_2` | anticonformal |
| `23` | `V_1 <-> V_2` | conformal |
| `02` | `V_0 <-> V_2` | anticonformal |
| `13` | `V_0 <-> V_2` | conformal |
| `03` | `V_0 <-> V_1` | anticonformal |
| `12` | `V_0 <-> V_1` | conformal |

Here conformal means `span{E_1,E_2}` and anticonformal means `span{F_1,F_2}` for

\[
E_1=I,\ E_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
F_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\ F_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

`verify_root_strictness.py` computes these six exterior-square matrices exactly in the real basis (4), including the determinant sign of each `2 x 2` off-diagonal block. Thus the lead's geometric Spin(4) statement and the coordinate-pair twirl theorem are literally about the same six row root planes; the right/column statement follows by right multiplication or by applying the same calculation to `U^*`.

## 4. New theorem — `MOC4-STRICT-SPIN4-SECTORS-v1`

Every support-violating genuine global maximizer obeys, for all three left block-plane pairs and all three right block-plane pairs,

\[
\boxed{T^L_{\alpha\gamma}>|C^L_{\alpha\gamma}|},\qquad
\boxed{T^R_{\beta\delta}>|C^R_{\beta\delta}|}.
\tag{7}
\]

### Proof

At a global maximizer, (2) gives `T>=|C|`. If `T=|C|`, the newest lead theorem proves that one of the two genuine coordinate `SU(2)` factors is support-flat. Account04/B09's exact Haar-twirl lift gives a probability law `mu` on `S_4` whose full exterior-minor moments equal the orbit average. Therefore, for the fixed support direction,

\[
h(U_*)=\int h(GU_*)\,dG
=\sum_{\sigma\in S_4}\mu(\sigma)H_\sigma\le M.
\]

That contradicts `h(U_*)=M+gamma`, `gamma>0`. Hence equality is impossible and (7) follows. The same argument applies to every left and right gate. `QED`

No inverse, simple-spectrum assumption, nonzero-minor assumption or arbitrary bistochastic relaxation is used. The twirl theorem itself allows zero edge masses, so singular/degenerate minor configurations on this branch are included.

### Exact consequence for the latest lead proof tree

The latest lead report reduced `T=|C|` to a zero-entry face and retained a separate zero-face obligation. Equation (7) strictly improves that branch for a hypothetical violator: **Spin(4) saturation itself is already target-safe**, before any zero-entry support theorem is invoked. The zero-entry problem may still matter for unrelated boundary mechanisms, but it is no longer needed to close the mixed-conformal saturation branch.

The weighted Gram-cancellation identities derived in the preceding lead report on the premise `T=|C|` remain mathematically valid, but that premise cannot occur at a positive-gap global maximizer.

## 5. The only remaining singular boundary inside one pair Hessian

Put

\[
a=T-C>0,\qquad b=T+C>0.
\tag{8}
\]

Then (1) is

\[
\mathcal H=\begin{pmatrix}-2aI_2&M\\M^T&-2bI_2\end{pmatrix}.
\tag{9}
\]

With `a,b>0`, negative semidefiniteness is equivalent to

\[
\|M\|_{op}\le2\sqrt{ab}.
\tag{10}
\]

If the inequality is strict, this four-dimensional block is negative definite. If equality holds, choose unit singular vectors `u,v` with

\[
Mv=2\sqrt{ab}\,u,\qquad M^Tu=2\sqrt{ab}\,v.
\tag{11}
\]

Then

\[
Z_*=\sqrt b\,(u_1E_1+u_2E_2)+\sqrt a\,(v_1F_1+v_2F_2)
\tag{12}
\]

is an explicit Hessian-kernel direction. Both its conformal and anticonformal components are nonzero because `a,b>0`. Therefore any singular pair-Hessian direction surviving (7) is genuinely mixed; it is not a flat coordinate pair root.

This is the exact boundary dichotomy:

1. `||M||_op < 2 sqrt(T^2-C^2)`: negative-definite pair block;
2. `||M||_op = 2 sqrt(T^2-C^2)` with `T>|C|`: mixed Schur kernel (12).

## 6. New higher-order gates on a mixed Schur kernel

These are polynomial identities and are singular-safe. For arbitrary real `2 x 2` `Z`, put

\[
P=ZZ^T,\qquad Q=Z^TZ,
\]

and on a chosen block-row pair write `A_beta=B_{alpha beta}`, `G_beta=B_{gamma beta}`. Along the genuine Spin(6) path generated by

\[
L_Z=\begin{pmatrix}0&Z\\-Z^T&0\end{pmatrix}
\]

one has

\[
A'=ZG,\quad A''=-PA,\quad A'''=-ZQG,\quad A''''=P^2A,
\]
\[
G'=-Z^TA,\quad G''=-QG,\quad G'''=QZ^TA,\quad G''''=Q^2G.
\tag{13}
\]

Let

\[
q(S,T)=\det(S+T)-\det S-\det T.
\tag{14}
\]

Then

\[
(\det A)'''=q(A,A''')+3q(A',A''),
\tag{15}
\]
\[
(\det A)''''=q(A,A'''')+4q(A',A''')+3q(A'',A''),
\tag{16}
\]

and likewise for `G`. For `R(A)=||A||_F^2/2`,

\[
R(A)'''=-4\langle Z^TA,QG\rangle_F,\qquad R(G)'''=-R(A)''',
\tag{17}
\]
\[
R(A)''''=4\{\langle A,P^2A\rangle_F-\langle G,Q^2G\rangle_F\},\qquad R(G)''''=-R(A)''''.
\tag{18}
\]

With `delta X_beta=X_{alpha beta}-X_{gamma beta}`, the exact third derivative of the structured support is

\[
\begin{aligned}
J_3(Z)=\sum_\beta\{&K_{\alpha\beta}[q(A_\beta,-ZQG_\beta)+3q(ZG_\beta,-PA_\beta)]\\
&+K_{\gamma\beta}[q(G_\beta,QZ^TA_\beta)+3q(-Z^TA_\beta,-QG_\beta)]\\
&-2\delta X_\beta\langle Z^TA_\beta,QG_\beta\rangle_F\}.
\end{aligned}
\tag{19}
\]

At a local maximum, a Hessian-kernel direction must satisfy

\[
\boxed{J_3(Z)=0.}
\tag{20}
\]

Otherwise the cubic term changes sign under `t -> -t` and increases the support on one side. This is `MOC4-MIXED-SCHUR-CUBIC-GATE-v1`.

The exact fourth derivative is

\[
\begin{aligned}
J_4(Z)=\sum_\beta\{&K_{\alpha\beta}[q(A_\beta,P^2A_\beta)-4q(ZG_\beta,ZQG_\beta)+3q(PA_\beta,PA_\beta)]\\
&+K_{\gamma\beta}[q(G_\beta,Q^2G_\beta)-4q(Z^TA_\beta,QZ^TA_\beta)+3q(QG_\beta,QG_\beta)]\\
&+2\delta X_\beta[\langle A_\beta,P^2A_\beta\rangle_F-\langle G_\beta,Q^2G_\beta\rangle_F]\}.
\end{aligned}
\tag{21}
\]

If `Z` is a Hessian-kernel direction and (20) holds, local maximality further requires

\[
\boxed{J_4(Z)\le0.}
\tag{22}
\]

This is `MOC4-MIXED-SCHUR-QUARTIC-GATE-v1`. In particular, every equality case of (10) at a hypothetical violator must satisfy (11)-(12), (20), and (22).

The verifier checks (15)-(18) as exact symbolic polynomial identities rather than by finite differences.

## 7. Direct application of the assigned OTHER-account result

Account01/B09's newest adversary is an important negative control. Its true unitary is strict top-Rayleigh on all twelve coordinate pair orbits, so it lies on the **strict** side of (7), exactly as the new reduction permits. Yet account01/B09 rigorously finds a genuine mixed tangent with positive second derivative about `105.11419`, so the point is a saddle and is rejected by the lead's mixed Hessian condition.

Thus the present theorem removes the scalar-flat boundary without making the false inference “all pair roots strict implies a target proof” or “all pair roots strict restores a positive common-permutation lift.” The partner example demonstrates that the mixed block `M` is indispensable.

## 8. Smallest honest remaining implication

The first unpaid target-level implication is now:

**`MOC4-STRICT-ROOT-MIXED-SCHUR-RESIDUAL-v1` (OPEN).** Exclude a genuine common-unitary global support maximizer with positive gap that simultaneously satisfies the retained endpoint/subgroup roofs and same-unitary `P/R/D` identities, full first-order stationarity, every strict inequality (7), every mixed-Hessian inequality (2), and, on each equality case of the mixed Schur bound, the exact kernel/cubic/quartic conditions (11)-(12), (20), (22).

If all pair Hessian blocks are negative definite, the remaining obstruction is a strict-interior coupling problem involving different root blocks and Cartan directions. If one pair block is singular, the explicit mixed-kernel algebra above is the exact next boundary stratum. A source-valid counterexample would have to survive all of these conditions; a nonmonomial stationary point by itself remains irrelevant.

## 9. Verification, failures, and provenance

`verify_root_strictness.py` and `VERIFY_OUTPUT.txt` are in this run directory. The exact output is:

```text
PASS MOC4-SPIN6-ROOT-PAIR-DICTIONARY-v1
pair (0, 1): block planes 1<->2, sector=anticonformal, dets=(-1,-1)
pair (0, 2): block planes 0<->2, sector=anticonformal, dets=(-1,-1)
pair (0, 3): block planes 0<->1, sector=anticonformal, dets=(-1,-1)
pair (1, 2): block planes 0<->1, sector=conformal, dets=(1,1)
pair (1, 3): block planes 0<->2, sector=conformal, dets=(1,1)
pair (2, 3): block planes 1<->2, sector=conformal, dets=(1,1)
PASS MOC4-MIXED-SCHUR-CUBIC-GATE-v1 symbolic third-derivative identities
PASS MOC4-MIXED-SCHUR-QUARTIC-GATE-v1 symbolic fourth-derivative identities
```

A late team-lead run appeared after the initial report write. It was read in full and incorporated into this canonical replacement; Git history preserves the earlier same-run version. The late lead independently established the Spin(4)-to-coordinate-pair identification and saturation-to-zero-face theorem. The genuinely new strengthening here is to combine that exact flatness conclusion with the already-proved pair-Haar-twirl lift, eliminating the saturation branch entirely for a target violator, and then to characterize the remaining mixed Schur boundary with the explicit cubic/quartic gates.

No numerical optimization supports the proof claims. No arbitrary bistochastic point, inverse matrix, benchmark material, held-out answer, credential, scheduler identifier, machine path, unrelated private data, email/Drive data, public posting, paid model/API/Codex call, remote workflow or permission bypass was used. Status remains `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.
