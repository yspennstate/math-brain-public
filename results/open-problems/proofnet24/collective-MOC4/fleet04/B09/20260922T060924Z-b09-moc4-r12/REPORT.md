# MOC4 fleet04/B09 — saturated pair gates are impossible at a violating maximizer

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T060924Z-b09-moc4-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact state consumed

The latest complete lead tree consumed is fleet03/B07 `20260922T055130Z-fleet03-B07-MOC4-r11`, coordination commit `e8eaccf8e3393ae7a5b75f12310d54ef92c15775`, together with its proved `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`, coordination commit `f81667d2ddb67bfa45c96cae39320b078c3e4c4c` and scientific commit `a9e219decc08f9a5f7bf4d73e7854f1114affc1c`. The lead had isolated a saturated pair `T=|C|` as the first missing branch and asked for `MOC4-FLAT-PAIR-MIXED-RIGIDITY-v1`.

The named OTHER-account result applied here is fleet01/B07 `MOC4-BIORIENTATION-PAIR-GATE-v1`, scientific report commit `a643a4e465e4f0243a961c10cad73aeb60089be2`. At a genuine global support maximizer it proves, for all three block-row pairs and all three block-column pairs,

\[
T^L_{\alpha\gamma}\ge |C^L_{\alpha\gamma}|,
\qquad
T^R_{\beta\delta}\ge |C^R_{\beta\delta}|,
\]

and, more precisely, for each orientation sign `epsilon=+-1`, the exact support loss to the corresponding `SO(6)` block-plane swap is

\[
s(O)-s(W_{\alpha\gamma,\epsilon}O)=T^L_{\alpha\gamma}-\epsilon C^L_{\alpha\gamma},
\tag{1}
\]

with the column analogue. I also retain fleet01/B07's later exact Spin(6) stationarity balances, coordination commit `06b94d9eccff5122288e51bd1992eeb42a84f975`: any residual global maximizer satisfies `N_12=N_13=N_23=0` and the corresponding right-hand system.

Two same-account results are essential inputs, not re-proved here:

- fleet04/B08 `MOC4-PAIR-FLAT-BOUNDARY-v1`, coordination commit `e8ea294115f41ca1f77047e21af4b712528780a9`: at a global support maximizer, if one elementary row/column pair-swap ties, the support is constant on the entire genuine embedded `SU(2)` pair orbit. This is adjugate-based and singular-safe.
- fleet04/B09 `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`, coordination commit `fd15e478451b6ebd01baa7b7148cbf6f8342b980`: the Haar average of the complete `k=1,2,3` squared-minor data over such an elementary `SU(2)` pair orbit admits an exact probability lift to the 24 permutation matrices. Hence a support functional flat on that orbit cannot exceed the largest permutation-product support.

## 2. New theorem — `MOC4-ROOT-SATURATION-EXCLUSION-v1`

Let `U` be a global maximizer for one separating support functional. If its support is strictly larger than all 24 permutation-product endpoint supports, then every fleet01/B07 bi-orientation gate is strict:

\[
\boxed{T^L_{\alpha\gamma}>|C^L_{\alpha\gamma}|\quad\text{for all }\alpha<\gamma,}
\tag{2L}
\]

\[
\boxed{T^R_{\beta\delta}>|C^R_{\beta\delta}|\quad\text{for all }\beta<\delta.}
\tag{2R}
\]

Equivalently, no support-violating global maximizer lies on the saturated branch of the lead's mixed Hessian gate. Thus the lead's `MOC4-FLAT-PAIR-MIXED-RIGIDITY-v1` is not an unpaid target-level branch: saturation itself is already incompatible with support violation.

This statement has no simple-spectrum, invertibility, nonzero-minor, or genericity hypothesis.

### Proof

Fix a block-row pair `alpha<gamma`. Suppose

\[
T^L_{\alpha\gamma}=|C^L_{\alpha\gamma}|.
\]

Choose `epsilon in {+1,-1}` so that `epsilon C^L_{\alpha\gamma}=|C^L_{\alpha\gamma}|`. Equation (1) then gives

\[
s(O)=s(W_{\alpha\gamma,\epsilon}O).\tag{3}
\]

It remains only to identify this block-plane endpoint with an elementary pair endpoint in the original `4 x 4` unitary. This is exact root geometry, not an arbitrary Spin(6) element.

Use the grouped exterior-square basis

\[
(12,34)\mid(13,24)\mid(14,23).
\]

For an original coordinate pair `ij`, let `J_ij in SU(4)` be identity off `i,j` and equal to

\[
\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\]

on those two coordinates. Direct exterior-square calculation gives:

| original root | mixed block planes | `det Z` |
|---|---|---:|
| 12 | 23 | +1 |
| 34 | 23 | -1 |
| 13 | 13 | -1 |
| 24 | 13 | +1 |
| 14 | 12 | +1 |
| 23 | 12 | -1 |

In every row the nontrivial `4 x 4` part of `Lambda^2 J_ij` is exactly

\[
\begin{pmatrix}0&Z\\-Z^T&0\end{pmatrix},
\qquad \det Z=\epsilon.\tag{4}
\]

Consequently, for each block-plane pair and each sign `epsilon`, one of the two complementary original roots supplies a representative of the same endpoint class used in the pair-gate proof. The adjacent exact verifier checks all six identities over the rationals and also checks that complementary roots have opposite `det Z`.

Moreover `J_ij=D_ij P_ij`, where `P_ij` is the coordinate swap and `D_ij` is diagonal unitary. Left diagonal phases commute with `D_a`, so `J_ij U` and `P_ij U` have the same determinant support. Therefore (3) is exactly a tie at an elementary row-pair swap in the sense of `MOC4-PAIR-FLAT-BOUNDARY-v1`.

Because `U` is a global maximizer, that theorem upgrades the tie to flatness on the entire embedded `SU(2)` row-pair orbit:

\[
h_\eta(GU)=h_\eta(U)\qquad\text{for every }G\in SU(2)_{ij}.\tag{5}
\]

Apply `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`. Haar averaging (5) leaves the support unchanged, while the averaged complete squared-minor vector is a convex combination of the 24 permutation squared-minor vectors. Hence

\[
h_\eta(U)
=\int h_\eta(GU)\,dG
\le \max_{\sigma\in S_4}
\Re\!\left(\eta\prod_i(a_i+b_{\sigma(i)})\right),\tag{6}
\]

contradicting the assumed strict support violation.

Thus every row gate is strict. The column proof is identical, using right embedded roots; right diagonal phases commute with `D_b`. This proves (2L)-(2R). `QED`

## 3. Interaction with the new full pair Hessian theorem

The lead's `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1` gives, for each block-plane pair,

\[
\bigl(\rho(\mathsf A)+\rho(\mathsf G)\bigr)^2
\le 4(T^2-C^2).\tag{7}
\]

Before this run, the lead treated `T=|C|` as a separate algebraic classification problem because (7) then forces weighted Gram anisotropies to vanish. The theorem above shows that, **at a support-violating global maximizer**, this equality case cannot occur at all. Therefore the Gram-collinearity classification generated by equality in (7) is not needed for target closure. On the only surviving branch,

\[
T^2-C^2>0
\]

for every left and right block-plane pair.

This does not prove the strict branch. It removes a branch rather than replacing the remaining interior implication by an unsupported assertion.

## 4. Compact conditional end-to-end chain after this run

If MOC4 fails in some support direction, compactness gives a support-violating global maximizer. Compatible campaign boundary/repeated-spectrum results may be retained, but they are not needed to justify the present exclusion. For the maximizer itself:

1. exact exterior-square compatibility holds: one true `U` supplies `O=Lambda^2U`, `(D,R)`, and `D=(1/4)E^TPE`;
2. all 24 subgroup roofs and the current support ceilings hold;
3. by fleet01/B07 the exact first-order Spin(6) stationarity equations hold;
4. by fleet03/B07 all left/right full mixed Hessian gates hold;
5. by `MOC4-ROOT-SATURATION-EXCLUSION-v1`, **every one of the twelve elementary pair spheres is strict**, equivalently all six absolute-value block-plane gates have positive slack.

Thus the first essential remaining implication is now the strict interior statement

**`MOC4-STRICT-SPIN6-SIX-WITNESS-v2`.** For structured spectral coefficient pairs `(K,X)` arising from one MOC4 support direction, prove the six-fiber support inequality at every genuine `Lambda^2 U` global maximizer satisfying the complete left/right stationarity equations, all strict bi-orientation gates, all lead mixed-Hessian inequalities, all 24 subgroup roofs, and the exact same-unitary `P/R/D` identities.

This is strictly narrower than the partner's earlier `MOC4-SPIN6-STATIONARY-SIX-WITNESS-v1`: the equality/flat-pair branch and its limit cases have now been removed rigorously. The parent MOC4 target remains open because the strict interior implication is not yet proved.

## 5. Exact computation and scope

`verify_root_saturation.py` uses only Python's standard library and exact `Fraction` arithmetic. It constructs the six determinant-one elementary root rotations `J_ij`, computes their exterior-square matrices in the grouped complementary-pair basis, verifies orthogonality and determinant `+1`, extracts the exact block `Z`, checks the form (4), and verifies complementary roots have opposite `det Z`. `VERIFY_OUTPUT.txt` records the complete output.

No numerical tolerance, arbitrary doubly-stochastic surrogate, independent compound-minor assignment, or non-source matrix model is used. The computation verifies only the root/block identification; the mathematical support implication is the analytic composition of the cited exact peer theorems.

No benchmark data, credentials, scheduler identifiers, machine paths, unrelated private material, email, Drive, public posting, paid API/model/Codex execution, or remote workflow was used.
