# MOC4 account01/B09 — nonsingular full-stationary strict-pair coefficient-lift adversary

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `b09-20260922T054641Z-moc4-r11`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Assignment:** construct genuine unitary/spectrum adversaries to proposed coefficient representations; distinguish lift failure from target-hull failure  
**Outcome:** `CANDIDATE_REFUTED` for `MOC4-STATIONARY-STRICT-PAIR-PROJECTED-LIFT-v1`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Current proof tree consumed

Fresh controls remained OWNER CONTROL revision `2026-09-22.2`. During this run the campaign lead account03/B07 published the authoritative generic proof tree and `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1` (handoff commit `f81667d2ddb67bfa45c96cae39320b078c3e4c4c`, proof-tree commit `e8eaccf8e3393ae7a5b75f12310d54ef92c15775`). A hypothetical MOC4 counterexample maximizer must satisfy the global roofs, first-order stationarity, all pair gates, and the new mixed true-unitary Hessian inequalities; the first named generic gap is `MOC4-FLAT-PAIR-MIXED-RIGIDITY-v1` plus the nonsaturated full-Hessian residual.

The assigned OTHER-account partner account02/B07's complete run `20260922T053424Z-b07-45eeecdd` (`MOC4-PAIR-CURVATURE-SANDWICH-v1` and `MOC4-CONJUGACY-CASIMIR-BALANCE-v1`, report commit `44dc01b869c00bf7446d254586d97b6754ee6961`) is applied below. It closes repeated spectra exactly, proves equality of row/column transposition-gap sums, and sharpens the surviving branch to simple-spectrum strict-curvature stationary maxima. I also use the pair-Rayleigh/Bloch fact already retained in that partner chain: on each genuine row/column `U(2)` pair orbit the support is a `2 x 2` Hermitian Rayleigh quotient, so a stationary point whose antipodal label-swap value is strictly lower is the strict top point on that pair orbit.

The compact conditional end-to-end route is therefore: separate a failure by a support functional, choose a true-unitary global maximizer, use the roofs and exact pair symmetrized lifts to force strict pair gates, use full first- and second-order true-unitary stationarity, then close the remaining same-unitary `P/R/D` or Spin(6) residual. The present run attacks a tempting replacement for the mixed-Hessian step: perhaps first-order stationarity plus all twelve strict pair tops already restores a positive common-permutation coefficient lift. It does not.

## 2. Fixed dense rational true unitary and exact lift obstruction

Use the dense rational orthogonal matrix

\[
U=\begin{pmatrix}
-656/21025&2433/3625&2688/4205&-1356/3625\\
-5856/47125&-192/325&35733/47125&16/65\\
35733/47125&16/65&5856/47125&192/325\\
2688/4205&-1356/3625&656/21025&-2433/3625
\end{pmatrix},\qquad \det U=-1.
\]

All 16 entries and all 36 two-by-two minors are nonzero. Put `P_rc=|u_rc|^2` and

\[
Q_{ij}=|\det U[\{0,i\},\{0,j\}]|^2,\qquad i,j\in\{1,2,3\}.
\]

Every probability law on `S_4` reproducing these singleton marginals and the nine anchored two-set marginals must obey the exact permutation-facet inequality from the earlier dense-anchor run,

\[
P_{13}+P_{21}+P_{32}-P_{12}-P_{23}-P_{31}
+2Q_{12}+Q_{13}+Q_{21}+2Q_{23}+2Q_{31}+Q_{32}\ge0.
\]

For this genuine unitary the left side is exactly

\[
-\frac{10349074315776}{1167289931640625}<0. \tag{1}
\]

Thus **no** positive law on the 24 permutations can reproduce even this projected set of true compound-minor marginals. This obstruction depends only on `U`, not on the spectra.

## 3. Rigorous algebraic simple spectra giving full first-order stationarity

Fix

\[
b=(-4,-2,3,-1),\qquad C=U D_b U^T.
\]

For real variables `v=(x_0,x_1,x_2,x_3,y_2,y_3)` set

\[
a(v)=(x_0+7i/4,\ x_1-11i/10,\ x_2+i y_2,\ x_3+i y_3),
\]

\[
X(v)=D_{a(v)}+C,
\]

and for the six real-skew generators `K_rs=E_rs-E_sr`, define the exact rational cubic equations

\[
F_{rs}(v)=\Re\operatorname{tr}\!\left(\operatorname{adj}X(v)\,[K_{rs},C]\right)=0,
\qquad 0\le r<s\le3. \tag{2}
\]

Let

\[
\begin{aligned}
c={}&(-1.306978760847276,-2.311269351538912,-0.169908501435229,\\
&0.635994359385863,-1.418141008695427,0.390813072733030).
\end{aligned}
\]

The verifier performs a **rational interval/Krawczyk–Banach certificate** on the box

\[
\|v-c\|_\infty\le10^{-8}. \tag{3}
\]

The exact interval derivative of the Newton-like map has infinity-norm bound

\[
q<7.45614\times10^{-7}<1,
\]

and its image lies strictly inside (3), with coordinate offsets from the center all below `7.73e-15` in absolute value. Hence (2) has a unique zero `v_*` in (3). Define `a_*=a(v_*)`.

This gives a mathematically exact spectrum: `v_*` is the unique zero of the six rational cubics in the displayed rational box, not an unverified floating-point root.

Now consider the support

\[
h(V)=\Re\det(D_{a_*}+V D_b V^*).
\]

Equations (2) kill all six real-skew left tangent directions at `U`. The other tangent directions vanish **identically**, not numerically: if `K=iS` with `S` real symmetric, then `[K,C]=i[S,C]`, where `[S,C]` is real skew-symmetric, while `adj(X)^T=adj(X)` because `X` is complex symmetric. Therefore

\[
\operatorname{tr}(\operatorname{adj}X\,[K,C])=0.
\]

Every skew-Hermitian tangent is a real-skew matrix plus `i` times a real-symmetric matrix. Thus

\[
\boxed{d h_U(KU)=0\quad\text{for every }K^*=-K.} \tag{4}
\]

So `U` is a **full first-order stationary point on `U(4)`**, not merely stationary under real rotations.

The spectra are simple and nonreal throughout the certified box. Moreover interval evaluation gives

\[
-6.084341394<\Re\det X(v_*)<-6.084338007,
\]
\[
-5.758688784<\Im\det X(v_*)<-5.758685505,
\]

so `A+B` is genuinely **nonsingular**.

## 4. All twelve row/column pair orbits are strict top-Rayleigh

For each of the six row swaps and six column swaps, exact interval evaluation at the certified algebraic root gives

\[
h(U)-h(P_{rs}U)>0,\qquad h(U)-h(UP_{pq})>0.
\]

The smallest rigorous lower bounds are

\[
\min_{r<s}\{h(U)-h(P_{rs}U)\}>1.8532332438,
\]

\[
\min_{p<q}\{h(U)-h(UP_{pq})\}>0.2214895014. \tag{5}
\]

Together with full stationarity (4) and the partner pair-Rayleigh/Bloch theorem, (5) means that `U` is the **strict top point on every one of the twelve genuine pair orbits**.

As an exact application of the named current partner theorem, the verifier also checks symbolically—before substituting the root—the account02/B07 Casimir balance

\[
\sum_{r<s}\bigl(h(U)-h(P_{rs}U)\bigr)
=
\sum_{p<q}\bigl(h(U)-h(UP_{pq})\bigr). \tag{6}
\]

Thus the adversary already obeys the partner's exact row/column transposition-gap coupling.

## 5. The coefficient lift still fails, but the MOC4 hull holds strictly

Equation (1) is unchanged at `a_*`, so the projected positive common-permutation lift remains impossible **despite** nonsingularity, simple spectra, full first-order stationarity, twelve strict pair tops, and the exact Casimir balance.

This is nevertheless not a target counterexample. For the three permutations

\[
\sigma_1=(1,0,2,3),\quad \sigma_2=(1,2,3,0),\quad \sigma_3=(2,3,1,0),
\]

let

\[
z_k=\prod_{j=0}^3(a_{*,j}+b_{\sigma_k(j)}).
\]

Exact interval-oriented-area arithmetic proves `det X(v_*)` lies strictly inside the triangle `conv{z_1,z_2,z_3}`. The doubled triangle area is in

\[
(2719.6384644,2719.6406501),
\]

and the three barycentric weights are rigorously enclosed by

\[
\begin{aligned}
w_1&\in(0.3458183790,0.3458188921),\\
w_2&\in(0.3061186326,0.3061193134),\\
w_3&\in(0.3480620966,0.3480626862).
\end{aligned} \tag{7}
\]

Hence the determinant is comfortably inside the actual MOC4 target hull.

## 6. Decisive mixed-Hessian obstruction

The new lead theorem says a genuine support maximizer needs mixed true-unitary second-order control, not only the twelve pair conditions. The present example demonstrates why.

Let

\[
K=K_{01}-K_{23}
=(E_{01}-E_{10})-(E_{23}-E_{32}).
\]

Along the genuine unitary path `V(t)=e^{tK}U`, exact determinant multilinearity with

\[
C'=[K,C],\qquad C''=[K,[K,C]]
\]

gives the rigorously enclosed second derivative

\[
\boxed{
105.1141873378
<\left.\frac{d^2}{dt^2}\right|_{t=0}h(e^{tK}U)
<105.1141957551.} \tag{8}
\]

It is strictly **positive**. Thus `U` is a saddle even though every individual row/column pair orbit has `U` as its strict top point. In particular, pairwise Rayleigh optimality plus all first-order equations does not imply the full Hessian condition and cannot be used to restore the positive coefficient lift.

This supplies a concrete genuine-unitary reason the lead's new mixed-Hessian gate is essential: off-diagonal Hessian coupling between two pair directions can overwhelm the negative individual pair curvatures.

## 7. Consequence for the proof architecture

The following tempting strengthening is false:

> **`MOC4-STATIONARY-STRICT-PAIR-PROJECTED-LIFT-v1` (refuted).** Every nonsingular simple-spectrum true-unitary stationary point that is strict top-Rayleigh on all twelve row/column pair orbits admits one positive `S_4` law reproducing its level-one marginals and the nine anchored level-two marginals.

The counterexample above is genuine, source-valid and rigorously certified. It also explains exactly why it does **not** damage the current MOC4 route: (8) rejects it at the mixed second-order gate. Therefore the first essential target-level obligation remains the lead's current full-Hessian/flat-pair rigidity problem, not any universal or pairwise-local coefficient lift.

A future adversary capable of threatening the surviving proof tree must be much stronger: it must be a true-unitary simple-spectrum point satisfying **all** first-order equations, all row/column pair gates, the full mixed left/right Hessian inequalities, the global roofs and exact `P/R/D` compatibility, while still carrying a positive support gap—or it must directly violate the target hull.

## 8. Verification and provenance

`verify_stationary_lift_adversary.py` uses exact `sympy.Rational` algebra plus a `fractions.Fraction` interval/Krawczyk certificate. It verifies orthogonality/density of `U`, unique existence of `v_*`, full first-order stationarity, nonsingularity and simple spectra, all twelve strict swap gaps, exact Casimir balance, the exact negative projected-lift facet (1), the strict target-triangle certificate (7), and the positive mixed second derivative (8). Captured output terminates with

`PASS MOC4-NONSINGULAR-STRICT-STATIONARY-LIFT-NOGO-v1`.

No arbitrary bistochastic point is promoted to a true-unitary claim. No benchmark material, held-out answer, credential, scheduler identifier, machine path, unrelated private data, email/Drive data, public posting, paid model/API/Codex call, remote workflow or permission bypass was used.
