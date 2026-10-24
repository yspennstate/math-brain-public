# MOC4 account04/B08 — double-transposition endpoint roofs and mixed-Schur defect payment

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T071406Z-account04-B08-MOC4-r12`  
**Campaign:** complex-normal `4 x 4` Marcus–de Oliveira target  
**Role:** extremal boundary / degeneracy classification  
**Assigned partner:** account01/B09  
**Team lead:** account03/B07  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN_RESEARCH`; `full_brain_connected=false`.

## 1. Exact inherited state

The latest complete campaign-lead report available before the scientific write is

`proofnet24/collective-MOC4/account03/B07/20260922T064004Z-account03-B07-MOC4-r12/REPORT.md`,
blob `ec11bc9937109dc0059b8e2ab78a485a9f646e3e`.

It gives the exhaustive local split at a hypothetical positive-gap global support maximizer. Every scalar Spin(4) sector is strict, so for each genuine four-dimensional pair Hessian

\[
H_{\rm pair}=\begin{pmatrix}-2aI_2&M\\M^T&-2bI_2\end{pmatrix}\preceq0,
\qquad a,b>0,
\tag{1}
\]

either `||M||_op<2sqrt(ab)` or the block lies on the mixed-Schur boundary `||M||_op=2sqrt(ab)`. On the boundary the lead proved the Lyapunov-Schmidt gate

\[
J_4(z)+3\langle\ell,(-H_{\rm pair})^+\ell\rangle\le0
\tag{2}
\]

for every Hessian-kernel direction `z`, together with annihilation of the full Hessian kernel by the cubic covector `ell`.

The named assigned OTHER-account result consumed is account01/B09 run
`20260922T064915Z-b09-moc4-r11`, report

`proofnet24/collective-MOC4/account01/B09/20260922T064915Z-b09-moc4-r11/REPORT.md`,
blob `894099b95b3aa65c5fa375a4ab8cbfa84510d74a`.

Its theorem `MOC4-ROOF-WEIGHTED-CUBIC-COERCIVITY-v1` identifies the two scalar coefficients in (1) with the exact complementary transposition gaps and, in simple singular-value coordinates, rewrites (2) as a positive weighted cubic reserve. This run applies that exact theorem rather than reopening the coefficient-lift route already refuted by the same partner.

The exact standard/complementary-pair representation used below is the one already fixed in the campaign-lead `V_4` fiber theorem: for a true unitary, `R` is the doubly-stochastic complementary-pair channel, `D` is the oriented standard channel, every block obeys `|D_{alpha beta}|<=R_{alpha beta}`, and an endpoint permutation is represented by a pair-class permutation together with one of the four even sign patterns.

## 2. Compact conditional full route

For a support direction `eta`, write

\[
h(U)=\Re\!\left(\overline\eta\det(D_a+UD_bU^*)\right),\qquad
M=\max_{\sigma\in S_4}H_\sigma,
\]

where `H_sigma` is the corresponding support of the endpoint product.

If MOC4 fails, compactness gives a genuine unitary global maximizer with

\[
h(U_*)=M+\gamma,\qquad \gamma>0.
\tag{3}
\]

Existing work forces all scalar Spin(4) sectors to be strict. The first live boundary branch is therefore mixed-Schur equality in (1); otherwise all six pair blocks are negative definite and one is in the lead's `NDI` branch. The present run attacks the mixed-Schur branch by deriving a new exact double-transposition roof and then identifying the lead/partner quartic reserve with the physical double-swap support drop.

## 3. New theorem: `MOC4-DOUBLE-TRANSPOSITION-TWO-POINT-LIFT-v1`

Let `v` be any nonidentity element of the Klein subgroup `V_4<S_4`, i.e. any double transposition. Then for every true unitary `U`, on either the row or column side,

\[
\boxed{\frac{h(U)+h(Uv)}2\le
R_v:=\max_{\sigma\in S_4}\frac{H_\sigma+H_{\sigma v}}2.}
\tag{4}
\]

For left multiplication the same statement holds with the corresponding left endpoint pairing.

### Proof

Fix the right-action version; the left version is its transpose analogue. In the exact `S_4 -> S_3` standard representation, `v in V_4` acts trivially on the pair-class channel and by a diagonal sign matrix on the standard channel. After relabeling the three standard coordinates,

\[
S_v=\operatorname{diag}(1,-1,-1).
\]

Hence the two-point average of the true-unitary exterior data has

\[
\bar R=R,
\qquad
\bar D=\frac{D+DS_v}{2},
\tag{5}
\]

so `bar D` retains exactly one standard column and zeros the other two.

Choose any Birkhoff decomposition

\[
R=\sum_{\rho\in S_3}\lambda_\rho P_\rho,
\qquad \lambda_\rho\ge0,
\qquad \sum_\rho\lambda_\rho=1.
\tag{6}
\]

Let `j` be the retained standard column. For `alpha=rho(j)`, the total Birkhoff mass landing in the cell `(alpha,j)` is exactly `R_{alpha j}`. If `R_{alpha j}>0`, put

\[
m_\alpha=\frac{D_{\alpha j}}{R_{\alpha j}}\in[-1,1];
\tag{7}
\]

if `R_{alpha j}=0`, then `D_{alpha j}=0` by `|D|<=R`, and set `m_alpha=0`.

The four permutations in a fixed `V_4` fiber carry the four even sign patterns

\[
(1,1,1),\ (1,-1,-1),\ (-1,1,-1),\ (-1,-1,1).
\tag{8}
\]

For a fixed `rho`, give each fiber element whose retained sign is `epsilon` the weight

\[
\frac{\lambda_\rho}{4}(1+\epsilon m_{\rho(j)}).
\tag{9}
\]

All weights are nonnegative. Their sum over the four signs is `lambda_rho`. For each prescribed retained sign there are exactly two even sign patterns; they are exchanged by right multiplication by `v`, and their other two sign coordinates cancel. Consequently the law (9):

1. has pair-class marginal exactly `R`;
2. has standard marginal exactly `bar D` from (5);
3. is invariant under `sigma -> sigma v`.

Thus it is one positive common endpoint lift of the **two-point averaged** true-unitary data. By the exact determinant/exterior expansion,

\[
\frac{h(U)+h(Uv)}2=\sum_\sigma\mu_\sigma H_\sigma.
\]

Grouping the `v`-invariant law into two-point orbits gives (4). `QED`

No individual-unitary positive lift is claimed. The theorem uses only true-unitary `R,D`, their exact common-unitary relation, and the universal block inequality `|D|<=R`.

### Exact double-swap gap consequence

Define the endpoint double-swap gap

\[
g_v:=2M-\max_\sigma(H_\sigma+H_{\sigma v})\ge0.
\tag{10}
\]

If `h(U)=M+gamma`, (4) gives

\[
\boxed{h(U)-h(Uv)\ge2\gamma+g_v.}
\tag{11}
\]

Thus a support-violating point is strictly above every one of its three `V_4` double-transposition antipodes on each physical side. In particular, a double-swap tie at a violator is impossible. This is stronger than the four-point `V_4` average for this boundary purpose.

## 4. Exact Spin(4) normal form for one mixed-Schur block

Use the lead's exact bi-affine `S^2 x S^2` Spin(4) representation for one complementary pair of coordinate roots. Put the current maximizer at the north-north pole `n=(0,0,1)` and write

\[
F(x,y)=\kappa+p\cdot x+q\cdot y+x^TCy,
\qquad x,y\in S^2,
\tag{12}
\]

with

\[
C=\begin{pmatrix}N&c\\d^T&c_0\end{pmatrix},
\qquad c,d\in\mathbb R^2.
\tag{13}
\]

Stationarity at `(n,n)` gives `p_perp=-c`, `q_perp=-d`. Let `tau,tau^c` be the two disjoint coordinate transpositions generating the two Spin(4) factors. Their genuine pair gaps are

\[
a=F(n,n)-F(-n,n)=2(p_3+c_0)>0,
\]
\[
b=F(n,n)-F(n,-n)=2(q_3+c_0)>0.
\tag{14}
\]

By the assigned partner theorem these are exactly the lead's `T-C` and `T+C` coefficients, up to the harmless exchange of labels.

On the simple mixed-Schur boundary choose singular-vector coordinates so

\[
M=4N=\operatorname{diag}(2\sqrt{ab},s_2),
\qquad 0\le s_2<2\sqrt{ab},
\tag{15}
\]

and write `c=(c1,c2)`, `d=(d1,d2)`,

\[
D_0:=4ab-s_2^2>0.
\tag{16}
\]

Use the exact local Bloch chart

\[
x=(2u,\sqrt{1-4|u|^2}),
\qquad
y=(2v,\sqrt{1-4|v|^2}).
\tag{17}
\]

Direct expansion gives, through degree four,

\[
\begin{aligned}
F-F(0)={}&-a|u|^2-b|v|^2+2\sqrt{ab}\,u_1v_1+s_2u_2v_2\\
&-4\{(c\cdot u)|v|^2+(d\cdot v)|u|^2\}\\
&-a|u|^4-b|v|^4+4c_0|u|^2|v|^2+O(5).
\end{aligned}
\tag{18}
\]

The mixed-Schur kernel direction is

\[
z=(\sqrt b\,e_1,\sqrt a\,e_1).
\tag{19}
\]

## 5. New theorem: `MOC4-MIXED-SCHUR-DOUBLE-SWAP-DEFECT-v1`

Let

\[
\delta:=F(n,n)-F(-n,-n).
\tag{20}
\]

Because applying both pair antipodes is the double transposition `v=tau tau^c in V_4`, this is the actual true-unitary double-swap gap `h(U)-h(Uv)`. From (14),

\[
\boxed{\delta=a+b-4c_0.}
\tag{21}
\]

At a local maximum on the simple mixed-Schur boundary, the cubic kernel condition is

\[
\boxed{\sqrt a\,c_1+\sqrt b\,d_1=0.}
\tag{22}
\]

Moreover the exact fourth derivative along (19) is

\[
\boxed{J_4(z)=-24ab\,\delta.}
\tag{23}
\]

The cubic covector entering the lead's Lyapunov-Schmidt reserve has singular-coordinate components

\[
\ell=(8ac_1,-8ac_2,-8\sqrt{ab}\,c_1,-8bd_2).
\tag{24}
\]

Substituting (24) into the assigned partner's exact reserve formula gives

\[
\mathcal R_{LS}=32ac_1^2+
\frac{128ab(ac_2^2+s_2c_2d_2+bd_2^2)}{D_0}.
\tag{25}
\]

Therefore the lead gate `J4+3 R_LS<=0` is **equivalent** to the physical double-swap defect inequality

\[
\boxed{
\delta\ge
\frac{4c_1^2}{b}
+
\frac{16(ac_2^2+s_2c_2d_2+bd_2^2)}{4ab-s_2^2}.}
\tag{26}
\]

The quadratic form in the second numerator is positive definite because its determinant is `(4ab-s2^2)/4>0`. Hence the right side of (26) vanishes only when `c1=c2=d2=0`; then (22) also gives `d1=0`.

Combining the new two-point roof (11) with (26), every positive-gap mixed-Schur maximizer on the simple stratum obeys the sharper exact boundary payment

\[
\boxed{
\delta\ge\max\left\{
2\gamma+g_v,
\frac{4c_1^2}{b}+
\frac{16(ac_2^2+s_2c_2d_2+bd_2^2)}{4ab-s_2^2}
\right\}.}
\tag{27}
\]

This is not a generic abstract `S^2 x S^2` statement: the first term uses the actual `S_4` endpoint support geometry and the same true-unitary exterior channels.

### Multiplicity-two Schur boundary

If both singular values equal `2sqrt(ab)`, the Hessian kernel is two-dimensional. Cubic vanishing on the whole kernel forces the vector identity

\[
\boxed{\sqrt a\,c+\sqrt b\,d=0.}
\tag{28}
\]

The lead pseudoinverse reserve on either unit kernel mode then gives

\[
\boxed{
\delta\ge\frac{4\|c\|^2}{b}
=\frac{4\|d\|^2}{a}.}
\tag{29}
\]

The endpoint theorem still gives `delta>=2gamma+g_v`, so (27) has the natural multiplicity-two replacement obtained by combining (29) with that same roof. Thus the singular-value multiplicity is an explicitly characterized degeneracy, not an omitted case.

## 6. Why this changes the live proof tree

Before this run, the mixed-Schur boundary was encoded by an abstract kernel, cubic covector and quartic reserve. The assigned partner converted the reserve into transposition-roof weights. Equations (21)-(27) identify the same quartic quantity with a **third physical permutation edge**: the disjoint double transposition joining the two pair antipodes.

Consequently a source-valid mixed-Schur violator must simultaneously pay:

- the two complementary transposition gaps `a,b`;
- the double-transposition endpoint roof `delta>=2gamma+g_v`;
- the exact positive local coupling defect in (26), or (29) on the multiplicity-two stratum;
- all pre-existing subgroup/V4 roofs, same-unitary `P/R/D` compatibility, stationarity and remaining Hessian constraints.

In particular, the mixed-Schur boundary cannot hide on a tied `V_4` edge. The double-swap tie is target-safe before any appeal to genericity, inverse matrices, or a coefficient lift of the individual unitary.

This also explains why account01/B09's earlier dense stationary strict-pair adversary is not a threat: it already fails the mixed Hessian gate. The new theorem does not infer monomiality from pair strictness and does not revive the refuted positive individual-unitary lift.

## 7. First remaining implication

The sharpened first boundary obligation is

**`MOC4-DOUBLE-SWAP-STRUCTURED-MS-EXCLUSION-v1` (OPEN).**  
For the determinant-specific common-unitary Spin(4) coefficients, exclude a positive-gap global maximizer on a mixed-Schur boundary that satisfies simultaneously the two transposition roofs, the exact double-transposition roof (11), the defect payment (26) or (29), the retained subgroup/V4 roofs, the exact same-unitary `P/R/D` identities and all stationarity/full-Hessian conditions.

If this boundary is excluded, the lead's separate `NDI` branch remains: all six pair blocks negative definite. Full MOC4 therefore remains open; this run does not replace either remaining branch by an unsupported condition.

## 8. Exact verification

`verify_double_v4_mixed_schur.py` was executed with exact `Fraction` arithmetic for the endpoint-fiber construction and exact `sympy` algebra for the local Taylor/reserve identities. It checks:

- the `V_4` two-point law has total mass one;
- its pair-class marginal is exactly `R`;
- its standard marginal is exactly the one-column projection in (5);
- it is invariant under multiplication by the chosen double transposition;
- the exact quadratic/cubic/quartic Taylor coefficients in (18);
- the kernel cubic factor (22), covector (24), identity (23), reserve (25), and equivalence (26).

Captured output terminates with

`PASS MOC4-DOUBLE-V4-MIXED-SCHUR-BRIDGE-v1`.

Verifier creation commit: `bc271ee2b03d0a1c27506b9568923edf94e6004d`.  
Captured-output creation commit: `46a4e4f3285c03f622b5aa59ded880e8924958dc`.

## 9. Scope and verdict

`ESSENTIAL_STEP_APPLIED`. The run adds an exact two-point endpoint roof for every nontrivial `V_4` double transposition and converts the live mixed-Schur Lyapunov-Schmidt reserve into a physical double-swap defect inequality, including the multiplicity-two singular stratum. This materially narrows the first boundary branch but does **not** prove or disprove MOC4.

Scoped privacy/provenance review found no benchmark material, held-out answer, credential, scheduler identifier, machine path, unrelated private data, email/Drive content, public posting, paid model/API/Codex call, remote workflow or permission bypass in the changed scientific files.
