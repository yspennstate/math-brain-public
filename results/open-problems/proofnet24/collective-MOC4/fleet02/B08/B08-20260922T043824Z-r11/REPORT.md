# MOC4 fleet02/B08 — exact common-block edge interaction and 2+2 payment gate

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `B08-20260922T043824Z-r11`  
**Assignment:** repeated-eigenvalue/common-block boundaries only  
**Outcome:** **ESSENTIAL_STEP_APPLIED**. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Candidate:** `MOC4-COMMON-BLOCK-EDGE-PAYMENT-v1`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no benchmark or installation work.

## 1. Exact source state consumed


- `AGENTS.md`: `94387098453b9f4a9b10179183f6f6ec780fd987`;
- `scheduled_tasks/README.md`: `3d4a9372c87802ab734141a3374d04c8823372e3`;
- `scheduled_tasks/fleet.json`: `e647d5d2479749f80ce7bb4862bee0f28513c7d9`;
- `scheduled_tasks/roles.json`: `ed17ecc94f76720c0345b3e32249b791b20ec611`;
- `scheduled_tasks/PROTOCOL.md`: `83a9268bf5287ca203e4be69a79e25382397bca7`.

The collective MOC4 order/target/assignment package was read at the invocation's fresh control head before work. No later stop was present at the reread above.

Latest complete campaign lead actually consumed: **fleet03/B07**, `MOC4-V4-PAIR-GAP-CEILING-v1`, canonical report `proofnet24/collective-MOC4/fleet03/B07/fleet03-B07-20260922T033411Z-d2a63b2a/REPORT.md`, report blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`. Its residual is the genuine same-unitary positive-reserve support-maximizer problem after the exact V4/pair-gap ceiling.

Named OTHER-account partner actually consumed: **fleet03/B09**, `MOC4-CYCLE-SEPARATOR-NOGO-v1`, canonical report `proofnet24/collective-MOC4/fleet03/B09/20260922T035131Z-fleet03-B09-moc4-r11/REPORT.md`, report blob `f0a1e4daf7262912f6d68b8984fb42abc03f5064`. It constructs genuine `SO(6)` exterior-square data violating a natural even-endpoint cycle cut and therefore rules out a transport-only cure of the remaining cycle interference; any successful payment must use the structured spectral support normal.

Also used as an essential compatible input: fleet04/B08 `MOC4-BIDIRECTIONAL-V4-PAIR-CEILING-v1`, report blob `30448cadc8902a3b38f080fd1923392393e997ed`, which strengthens the lead ceiling by matrix-swap symmetry and identifies positive bilateral reserve as the only residual support branch.

Previous own boundary state: `MOC4-CIRCLE-FACE-REDUCTION-v1`, report blob `5e52a9d9463e30108d1de0c5269d693dfd4e4ef3`. It already solved common generalized-circle spectra and classified the generic collinear repeated face; it also produced a genuine exposed mismatched-circle `2+2` common-block witness for which only an infinitesimal off-block Hessian had been established.

A bounded current literature search on 2026-09-22 again found only sources describing the unrestricted Marcus-de Oliveira conjecture as open; in particular the current OpenProblemsInNLA status page (checked 2026-09-10) says the 2026 literature still gives structured cases rather than a complete proof. This is a bounded status check, not evidence of novelty.

## 2. Setup: determinant numerator and a proper common block

Diagonalize the first normal matrix and write

\[
D(U):=\det(D_a+U D_bU^*),\qquad U\in U(4).
\]

Because

\[
(D_a+UD_bU^*)U=D_aU+UD_b,
\]

we have the exact numerator identity

\[
D(U)=\frac{\det(D_aU+UD_b)}{\det U}. \tag{2.1}
\]

Assume `U_0` is a proper common-block unitary. Thus there is a nontrivial row partition `R_1\sqcup\cdots\sqcup R_m={1,2,3,4}` and an equally sized column partition `C_1\sqcup\cdots\sqcup C_m` such that every column indexed by `C_r` is supported in the row subspace `C^{R_r}`. Every block has size at most three, so the determinant at `U_0` is already in the MOC4 hull by the known `n<=3` cases and the product lift.

The question is not whether the boundary point itself is safe; it is how a genuine unitary can leave this safe boundary.

## 3. Theorem A — every single cross-block eigen-column gate is exactly convex-safe

Choose eigen-column labels `p in C_r`, `q in C_s` with `r != s`. For `c^2+s^2=1` and `|zeta|=1`, let `G_{pq}(c,s;zeta)` be the embedded determinant-one `SU(2)` column gate whose action on the two columns is

\[
u_p\mapsto c u_p-s\bar\zeta u_q,\qquad
u_q\mapsto s\zeta u_p+c u_q. \tag{3.1}
\]

Let `S_{pq}=G_{pq}(0,1;1)` be the full swap-with-phase endpoint. Then

\[
\boxed{
D(U_0G_{pq}(c,s;\zeta))
=c^2D(U_0)+s^2D(U_0S_{pq}).
} \tag{3.2}
\]

In particular the expression is independent of the gate phase `zeta`, and the entire one-edge `SU(2)` orbit is contained in the MOC4 target hull.

### Proof

By (2.1), and because `det G_{pq}=1`, it is enough to expand the numerator determinant multilinearly in columns `p,q`. Write

\[
L_j(u):=(D_a+b_jI)u.
\]

The four terms in the two-column expansion are the two endpoint terms and two mixed duplicate-column terms. Consider the term in which both new columns are built from `u_p`: the determinant contains one more vector supported in `C^{R_r}` than the dimension `|R_r|`, because `U_0` already has exactly `|R_r|` columns supported in that block. Hence those columns are linearly dependent and the term is zero. The term with two copies of `u_q` vanishes identically for the same dimension count in `R_s`.

The remaining two terms are exactly the physical endpoints. At `s=1` the determinant-one gate differs from the plain transposition only by column phases/signs, which cancel in `UD_bU^*`; hence the second endpoint is `D(U_0S_{pq})`. This proves (3.2).

The endpoint `U_0S_{pq}` is still a proper common-block pair: it only reallocates the two diagonal `b` labels between the same reducing row blocks. Therefore both endpoints lie in the target hull, and so does their convex combination. ∎

### Row analogue

Swapping the two normal matrices gives

\[
D_a+UD_bU^*\quad\longleftrightarrow\quad D_b+U^*D_aU,
\]

so the identical statement holds for a single cross-block eigen-row gate. Thus **no common-block counterexample can escape through one eigen-coordinate cross edge, from either side**.

For a support functional `L` with target maximum `M`, if `L(D(U_0))=M` and

\[
\delta_{pq}:=M-L(D(U_0S_{pq}))\ge0,
\]

then along the gate

\[
\boxed{M-L(D(U_0G_{pq}))=\delta_{pq}s^2.} \tag{3.3}
\]

This is exact, not merely second-order.

## 4. Theorem B — exact two-edge chord formula on a `2+2` boundary

Now specialize to a `2+2` boundary after relabelling:

\[
U_0=\operatorname{diag}(V,W),\qquad V,W\in U(2),
\]

with row and column blocks `{1,2}|{3,4}`. Apply two disjoint cross gates, on `(1,3)` and `(2,4)`:

\[
U=U_0G_{13}(c_1,s_1;\zeta_1)G_{24}(c_2,s_2;\zeta_2). \tag{4.1}
\]

Let `D_{00}=D(U_0)`, and let `D_{10},D_{01},D_{11}` be the determinants at the corresponding full-swap endpoints. Every one is a proper common-block determinant and is therefore MOC4-safe.

Put

\[
F_{13|24}:=(a_1-a_2)(a_3-a_4)(b_3-b_1)(b_4-b_2), \tag{4.2}
\]

and, writing `V=(v_{ij})`, `W=(w_{ij})`,

\[
\kappa:=\frac{v_{11}v_{21}w_{12}w_{22}}{\det V\det W}.
\tag{4.3}
\]

Then the determinant on the entire two-gate torus is

\[
\boxed{
\begin{aligned}
D(U)=&\ c_1^2c_2^2D_{00}+s_1^2c_2^2D_{10}
+c_1^2s_2^2D_{01}+s_1^2s_2^2D_{11}\\
&+2c_1s_1c_2s_2\,F_{13|24}\,
\Re(\zeta_1\bar\zeta_2\kappa).
\end{aligned}}
\tag{4.4}
\]

Thus the departure from the convex combination of the four safe common-block endpoints is a **one-real-dimensional chord**, not a free complex ellipse.

### Proof

Expand the numerator in (2.1) in the four affected columns. The terms choosing the two original vectors or the two swapped vectors within each gate give the four endpoint terms in (4.4).

A term with exactly one duplicate pair and one unmixed gate vanishes by the same block-dimension argument as Theorem A. The only nonendpoint terms that survive duplicate-support counting are the two in which both gates are mixed simultaneously:

- columns `(1,3)` both use the original first-block column `u_1`, while `(2,4)` both use the original second-block column `u_4`;
- or `(1,3)` both use `u_3`, while `(2,4)` both use `u_2`.

Direct two-by-two factorization after grouping the row blocks gives the corresponding raw determinants

\[
-F_{13|24}\,v_{11}v_{21}w_{12}w_{22},
\qquad
-F_{13|24}\,v_{12}v_{22}w_{11}w_{21}. \tag{4.5}
\]

For a `2x2` unitary with determinant `d`,

\[
v_{12}v_{22}=-d^2\overline{v_{11}v_{21}},
\]

and analogously for `W`. Consequently, after division by `det U_0=(det V)(det W)`, the two coefficients in (4.5) are complex conjugates. Their phase factors from (4.1) are `zeta_1\bar zeta_2` and its conjugate. The two terms therefore sum to the real scalar in (4.4). ∎

A second formula is obtained by the other perfect matching `(1,4),(2,3)`, with

\[
F_{14|23}=(a_1-a_2)(a_3-a_4)(b_4-b_1)(b_3-b_2). \tag{4.6}
\]

## 5. Exact support-payment dichotomy

Let `L:C->R` be a real support functional, let `M` be the maximum of `L` over the 24 target vertices, and suppose the base common-block point lies on the supporting line:

\[
L(D_{00})=M. \tag{5.1}
\]

Define nonnegative endpoint deficits

\[
\delta_{10}=M-L(D_{10}),\quad
\delta_{01}=M-L(D_{01}),\quad
\delta_{11}=M-L(D_{11}), \tag{5.2}
\]

and the structured interference coefficient

\[
C_{13|24}:=|\kappa|\,|L(F_{13|24})|. \tag{5.3}
\]

With `x=s_1^2`, `y=s_2^2`, maximizing (4.4) over the relative gate phase gives

\[
\begin{aligned}
M-\max_{\zeta_1,\zeta_2}L(D(U))
=&\ \delta_{10}x(1-y)+\delta_{01}(1-x)y+\delta_{11}xy\\
&-2C_{13|24}\sqrt{x(1-x)y(1-y)}.
\end{aligned}
\tag{5.4}
\]

Therefore:

### Corollary `MOC4-2PLUS2-TWOEDGE-PAYMENT-v1`

If

\[
\boxed{C_{13|24}^2\le\delta_{10}\delta_{01},} \tag{PAY}
\]

then the **entire** true-unitary two-gate family (4.1) is support-safe.

Indeed AM-GM gives

\[
\delta_{10}x(1-y)+\delta_{01}(1-x)y
\ge 2\sqrt{\delta_{10}\delta_{01}x(1-x)y(1-y)},
\]

which pays the interference term in (5.4), while `delta_11 xy>=0`.

Conversely, if

\[
C_{13|24}^2>\delta_{10}\delta_{01}, \tag{5.5}
\]

then arbitrarily small genuine two-gate perturbations of `U_0` violate that support inequality. To see this, put `x=epsilon alpha`, `y=epsilon beta`; the order-`epsilon` term in (5.4) is

\[
\delta_{10}\alpha+\delta_{01}\beta-2C_{13|24}\sqrt{\alpha\beta}.
\]

The associated `2x2` quadratic form has determinant `delta_10 delta_01-C^2<0`, so positive `alpha,beta` can be chosen to make it negative; the omitted terms are `O(epsilon^2)`. Thus (PAY) is **necessary and sufficient for local safety at the base within this matched two-edge torus**, while also being sufficient for global safety on the whole torus.

This is a decisive boundary gate: a failure of (PAY) is not a counterexample to a surrogate. It directly constructs a true-unitary MOC4 support counterexample with the original spectra.

## 6. Exact application to the previous exposed mismatched-circle witness

The previous B08 report exhibited

\[
-a=(-3,-2,1-3i,1-2i),\qquad
b=(-1,0,1,1+i),\qquad U_0=\operatorname{diag}(H,H),
\]

with `H` the real `2x2` Hadamard rotation. The four block-preserving target vertices lie on the real axis and all 20 off-block vertices have strictly negative imaginary part, so take `L(z)=Im z` and `M=0`.

The exact verifier in this run gives for matching `(1,3),(2,4)`:

\[
D_{00}=-119/4,
\]
\[
D_{10}=-289/4-(119/2)i,\qquad
D_{01}=-105/4-(43/2)i,
\]
\[
D_{11}=-87/4-104i,
\]

and

\[
F_{13|24}=-2+2i,\qquad |\kappa|=1/4.
\]

Hence

\[
\delta_{10}\delta_{01}=\frac{5117}{4},\qquad
C_{13|24}^2=\frac14,
\]

with exact payment margin

\[
\boxed{1279.} \tag{6.1}
\]

For the other perfect matching `(1,4),(2,3)`:

\[
D_{10}=-77/2-(115/2)i,\qquad
D_{01}=-85/2-(35/2)i,
\]
\[
D_{11}=-87/4-104i,\qquad F_{14|23}=-1+2i,
\]

so

\[
\delta_{10}\delta_{01}=\frac{4025}{4},\qquad C_{14|23}^2=\frac14,
\]

with exact payment margin

\[
\boxed{1006.} \tag{6.2}
\]

Thus the earlier witness is not merely infinitesimally inward in off-block directions: **both complete matched two-edge true-unitary tori are globally support-safe**.

The exact standard-library checker is `verify_twoedge_payment.py`; its captured exact output is `VERIFY_OUTPUT.txt`. It verifies the four support-line vertices, all twenty strict off-block endpoint inequalities, all displayed Gaussian-rational endpoint values, both spectral factors, and both payment margins. The checker is a finite self-check of the explicit witness, not a proof of Theorems A/B; those are proved algebraically above.

## 7. Interaction with the campaign lead and the named partner

The lead and fleet04/B08 reduce any global support failure to a genuine same-unitary positive bilateral-reserve maximizer after the safe solved strata are removed. The present result sharpens what “approaching a common-block stratum” can mean.

1. **One-edge escape is impossible.** From every proper common-block boundary, every eigen-coordinate cross `SU(2)` gate is an exact convex interpolation of two safe common-block endpoints. The same is true on the row side.
2. **For a `2+2` face, the first disjoint two-edge interaction is scalar.** It is governed exactly by one spectral number `L(F)` and one geometric factor `|kappa|`, against the two safe swapped-endpoint deficits.
3. **The payment is decisive.** If it fails, one gets an actual source-valid counterexample; if it holds, the entire two-edge torus is safe, not just a neighborhood.
4. **The named partner's cycle-separator no-go explains the remaining difficulty.** Generic multi-edge/cycle interference cannot be paid by transport-only even-endpoint inequalities on arbitrary genuine `SO(6)` data. The missing implication must exploit the fact that here the interference coefficient is the structured spectral normal `L(F)`, not a free transport separator.

For a `1+3` boundary, Theorem A is already informative: the unique singleton eigen-column cannot escape through one cross edge. Any escape requires at least two noncommuting cross gates sharing the singleton coordinate, or an interaction with within-block motion. For a `2+2` boundary, any escape from the matched disjoint-gate slices must use a support-degenerate payment edge or a genuinely more complicated cross-edge interaction than a single perfect-matching torus.

## 8. Compact conditional end-to-end reduction

A hypothetical MOC4 counterexample may be separated by a real support functional and chosen at a global true-unitary maximizer.

- Repeated spectra are handled by the earlier exact repeated-spectrum lift, with the generic collinear repeated face transferred to the generalized-circle theorem; the remaining lower-dimensional repeated degeneracies stay explicit rather than being discarded.
- Proper common-block points themselves are safe by the `n<=3` block product theorem.
- The opposite-scalar gauge keeps the target and determinant unchanged and lets the residual all-pairs search avoid irrelevant individual singularities.
- The lead/fleet04 bilateral V4/pair-gap ceilings and same-unitary stationarity constraints then govern the simple-spectrum irreducible residual.
- If a hypothetical violating sequence approaches a proper common block, Theorem A excludes every single eigen-coordinate cross-edge mechanism exactly. On a `2+2` face, Theorem B reduces each disjoint perfect-matching two-edge mechanism to the payment (PAY). Failure of that payment would itself be a genuine MOC4 counterexample; satisfaction globally closes that torus.

Accordingly the first boundary implication left unpaid after this run is:

> **`MOC4-COMMON-BLOCK-STRUCTURED-PAYMENT-v1` (OPEN).** At every support-exposed `2+2` common-block boundary point arising from actual spectra, prove the two structured inequalities
> \[
> |\kappa_{13|24}L(F_{13|24})|^2\le\delta_{13}\delta_{24},
> \qquad
> |\kappa_{14|23}L(F_{14|23})|^2\le\delta_{14}\delta_{23},
> \]
> from the spectral product structure and endpoint support inequalities; or exhibit actual spectra/block unitaries/support direction violating either inequality. A violation is already an authentic true-unitary MOC4 counterexample by Section 5.

Even if both inequalities are proved, a full common-block collar still needs control of noncommuting/shared-index multi-edge interactions. The fleet03/B09 no-go says that next step cannot be replaced by an arbitrary transport-cycle inequality; it must retain the structured spectral coefficient image.

This is strictly sharper than the prior “prove a boundary collar” residual because it exposes the first nonzero interaction order and gives a scalar source-valid failure certificate.

## 9. Status and nonclaims

- `MOC4-COMMON-BLOCK-ONE-EDGE-CONVEXITY-v1`: **PROVED** for every proper common block and every cross-block eigen-column gate; row analogue by matrix-swap symmetry.
- `MOC4-2PLUS2-TWOEDGE-CHORD-v1`: **PROVED**, exact formula (4.4), preserving arbitrary complex phases.
- `MOC4-2PLUS2-TWOEDGE-PAYMENT-v1`: **PROVED** as an exact local dichotomy and a global sufficient criterion on each matched two-edge torus.
- The previous exposed mismatched-circle witness: **both matched two-edge tori globally safe**, exact margins `1279` and `1006`.
- `MOC4-COMMON-BLOCK-STRUCTURED-PAYMENT-v1`: **OPEN**.
- Full MOC4: **OPEN**.

No arbitrary bistochastic surrogate, independent compound-minor phase choice, Hermitian-only substitution, benchmark material, paid model/API, remote workflow, or permission change is used.
