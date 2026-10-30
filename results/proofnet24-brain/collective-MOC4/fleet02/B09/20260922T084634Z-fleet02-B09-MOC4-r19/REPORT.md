# fleet02/B09 MOC4 report — zero-face Bloch triangles and exact Procrustes elimination

Run: `20260922T084634Z-fleet02-B09-MOC4-r19`  
Outcome: **ESSENTIAL_STEP_APPLIED**; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: **WITHOUT_VERIFIED_BRAIN**.

## 1. Target and live scope

For every complex normal `4 x 4` pair `A,B`, with spectra `a=(a_1,...,a_4)` and `b=(b_1,...,b_4)`, prove

`det(A+B) in conv{prod_i(a_i+b_{sigma(i)}): sigma in S_4}`,

including singular and repeated spectra.  After diagonalizing the relative position, for a support direction `eta` write

`h(U)=Re(conj(eta) det(D_a+U D_b U*))`,

`M=max_sigma Re(conj(eta) prod_i(a_i+b_{sigma(i)}))`.

A counterexample is equivalent to a genuine unitary global maximizer with `h(U_*)=M+gamma`, `gamma>0`.

The owner allocation is still `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, revision `2026-09-22.2`; fleet02/B09 remains MOC4 geometric/polarization research.  No new brain-installation or benchmark work was done.

## 2. Exact current inputs consumed

### Campaign lead

Consumed the latest complete source-bound lead handoff fleet03/B07 run `20260922T074824Z-fleet03-B07-MOC4-r13`, blob `596e9f9853a152f91076a07ee3a9005db1cee647`, theorem `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`.  It leaves the generic positive-gap strict-interior split:

1. `MSQR`: some genuine pair block lies on the mixed-Schur singular boundary, where a full-tangent generalized-Schur cross reserve is compulsory;
2. `NDI`: all six pair blocks are negative definite.

The same lead lineage retains the earlier zero-face / strict-interior dichotomy produced by Spin(4) saturation.

### Named OTHER-account results actually applied

1. **fleet04/B09**, run `20260922T081236Z-b09-moc4-r37`, theorem `MOC4-ZERO-FACE-BOGOLIUBOV-COFACTOR-RIGIDITY-v1`, shared blob `0e97ddedfc13f677788b6b6921c8420dac0eed68`.  In a singleton even-even gauge with `u_ij=0`, the anti-linear spinor block `N` has singular values exactly `(1,1,0)` and the linear block has rank one.  If `u,v` are unit left/right kernel vectors of `N`, then

   `M_spin=e^{i phi} u v^T`,

   and, entrywise,

   `|M_spin(alpha,beta)|^2=|cof_{alpha beta}(N)|^2=(1-r_alpha)(1-c_beta)`,

   with `r_alpha=sum_beta |N_alpha beta|^2`, `c_beta=sum_alpha |N_alpha beta|^2`.

   The same run reduces a zero-face Drury/Saxl excess to 12 aligned external directions, so the unpaid zero-face step must genuinely exploit this nonlinear cofactor locus.

2. **fleet03/B08**, run `20260922T082441Z-b08-moc4-r13`, theorem `MOC4-PAIR-TRAP-NO-MARGIN-v1`, shared blob `be15f2db8f86a6d08847fdc04f022e7f45fa4f7f`.  It gives an exact true-unitary family where all six elementary pair orbits are strictly locally maximizing while a mixed two-root tunnel almost cancels the local losses.  Therefore a zero-face proof cannot be based on a uniform margin extracted from separate pair gates; it must retain the full mixed finite-distance geometry.

3. **fleet01/B08**, run `20260922T083848Z-fleet01-B08-MOC4-r12`, theorem `MOC4-ZERO-FACE-COMMON-LIFT-FACET-NOGO-v1`, shared blob `fba1d58f5920bcd31a027b6d10d40173c21607ca`.  It gives a true rational zero-entry orthogonal unitary whose degree-one and degree-two compound marginals admit no common probability law on `S_4`.  Thus the present argument must not manufacture a nonexistent all-compound permutation lift.

4. **fleet03/B20**, run `20260922T084401Z-fleet03-B20-MOC4-r11`, shared blob `af275c4b0ac9c471987b75e3b6b87848e5b45228`, sharpens the lead MSQR branch to four finite scalar residual-budget gates.  That is retained for the no-zero branch; the mathematics below attacks the complementary zero face by a different mechanism.

## 3. New theorem: `MOC4-ZERO-FACE-BLOCH-PROCRUSTES-v1`

Fix one singleton even-even gauge and a genuine zero-face point `u_ij=0`.  Let the corresponding anti-linear block be `N`.  By fleet04/B09, `N` is a rank-two partial isometry.  Let

`u in ker N*`, `v in ker N`, `||u||=||v||=1`,

and put

`x_alpha=|u_alpha|^2`, `y_beta=|v_beta|^2`,

`r_alpha=1-x_alpha`, `s_beta=1-y_beta`.

Then `sum x=sum y=1`, `sum r=sum s=2`.

Choose isometries `A,B in C^{3 x 2}` with

`A A*=I-u u*`, `B B*=I-v v*`, `A* A=B* B=I_2`.

### 3.1 Exact genuine residual fiber

Every rank-two partial isometry having these left/right kernels is

`N(W)=A W B*`, `W in U(2)`.

Conversely this entire `U(2)` family remains on the **genuine zero face**.  Indeed, with the rank-one companion `M_spin=e^{i phi}u v^T`, the first two Bogoliubov orthogonality identities hold because `A A*=I-u u*` and `B B*=I-v v*`, while the cross identity is automatic from

`N(W)v=0`, `N(W)*u=0`.

Starting from the actual zero-face point, varying `W` stays in the connected real-orthogonal component.  Hence the resulting Bogoliubov transformations lie in `SO(6)` and lift through `Spin(6) ~= SU(4)` to genuine common unitaries.  The mass identity `||N||_F^2=2(1-P_ij)=2` keeps `P_ij=0`.  Thus no arbitrary `SO(6)` or bistochastic relaxation has been introduced.

The central phase of `W` does not change squared entry moduli, so the moduli fiber is parametrized by the usual adjoint map

`SU(2) -> SO(3)`.

### 3.2 The two kernel triples are closed Bloch triangles

Write the alpha-th row of `A` as `a_alpha`.  If `r_alpha>0`, define its Bloch vector `n_alpha in S^2` by

`a_alpha* a_alpha / r_alpha = (I+n_alpha . sigma)/2`.

When `r_alpha=0`, choose `n_alpha` arbitrarily; it is multiplied by zero below.  Define `m_beta` from the rows of `B` similarly.

The tight-frame identities `A* A=B* B=I_2` give

`sum_alpha r_alpha n_alpha=0`,

`sum_beta s_beta m_beta=0`.

Set

`ell_alpha=r_alpha n_alpha`, `k_beta=s_beta m_beta`.

Then

`sum ell_alpha=sum k_beta=0`,

`|ell_alpha|=r_alpha`, `|k_beta|=s_beta`.

So each triple is literally the set of oriented side-vectors of a Euclidean triangle.  Because `r_alpha=1-x_alpha` and `sum r=2`, its semiperimeter is one, and Heron's formula gives

`Area_x^2=x_1 x_2 x_3`,

hence

`|det_plane(ell_1,ell_2)|=2 sqrt(x_1 x_2 x_3)`.

The analogous identity holds for the `k` triangle with `y`.

### 3.3 Exact entry-modulus polarization

Let `R_W in SO(3)` be the Bloch rotation induced by `W`.  The qubit overlap identity gives, for every alpha,beta,

`|N(W)_{alpha beta}|^2
 = (r_alpha s_beta/2) (1+n_alpha . R_W m_beta)`

or equivalently

`q_alpha beta(W)
 = r_alpha s_beta/2 + (1/2) ell_alpha^T R_W k_beta`.       (3.1)

This is an exact polarization of the entire true-unitary zero-face residual fiber.

### 3.4 Exact support reduction to an orthogonal Procrustes problem

Use the inherited Spin(6) support normalization

`R=q^+ + q^-`, `D=q^+ - q^-`,

so the structured MOC4 support is affine in the two gauge channels.  Equivalently, after collecting terms independent of `W`, there is a real `3 x 3` coefficient matrix `Y` — in the usual `(K,X)` normalization, `Y=X/2-K` for the anti-linear channel — such that

`h(W)=constant + <Y,q(W)>`.

The cofactor theorem fixes the companion channel because

`|M_spin(alpha,beta)|^2=x_alpha y_beta`.

Therefore only (3.1) varies on the fiber.  Put

`Z=sum_{alpha,beta} Y_alpha beta ell_alpha k_beta^T`.

The Haar mean over this genuine residual fiber is

`h_bar=constant + (1/2) sum_{alpha,beta}Y_alpha beta r_alpha s_beta`,

and

`h(W)=h_bar + (1/2) tr(R_W^T Z)`.                         (3.2)

Because both triangle spans are at most two-dimensional,

`rank Z <= 2`.                                                    (3.3)

The orthogonal Procrustes theorem therefore has **no orientation loss**: if `sigma_1>=sigma_2>=sigma_3=0` are the singular values of `Z`, a proper rotation can realize the optimal planar isometry and choose the unused normal sign to keep determinant `+1`.  Consequently

`boxed( max_W h(W) = h_bar + (1/2)(sigma_1+sigma_2)
                    = h_bar + (1/2)||Z||_* ).`                  (3.4)

This is an exact finite-dimensional maximization over the whole genuine residual zero-face fiber.  No local Hessian approximation is used.

## 4. Closed scalar form: `MOC4-ZERO-FACE-TRIANGLE-NUCLEAR-v1`

The nuclear norm in (3.4) can itself be written without choosing Bloch phases or coordinates.

Define the `3 x 3` triangle Gram matrix `G(x)` by

`G(x)_{aa}=r_a^2`,

and, for distinct `a,b,c`,

`G(x)_{ab}=(r_c^2-r_a^2-r_b^2)/2`.

This is exactly the Gram matrix of the three side vectors `ell_a`; it is positive semidefinite, has kernel containing `(1,1,1)`, and has rank at most two.  Define `G(y)` analogously.

For the three two-subsets ordered `(12),(13),(23)`, put signs

`epsilon=(+1,-1,+1)`

and define the alternating second-compound scalar

`Delta_2(Y)=sum_{I,J in C(3,2)} epsilon_I epsilon_J det Y[I,J]`.  (4.1)

Cauchy-Binet and the closed-triangle identities give

`|det_plane Z|
 = 4 sqrt(x_1 x_2 x_3 y_1 y_2 y_3) |Delta_2(Y)|`.                (4.2)

Also

`||Z||_F^2 = tr(G(x) Y G(y) Y^T)`.                               (4.3)

Since `rank Z<=2`,

`||Z||_*^2=||Z||_F^2+2|det_plane Z|`.

Combining (4.2)-(4.3),

`boxed(
 ||Z||_*^2
 = tr(G(x) Y G(y) Y^T)
   + 8 sqrt(x_1 x_2 x_3 y_1 y_2 y_3) |Delta_2(Y)|.
 )`                                                               (4.4)

Thus the exact true-unitary zero-face fiber maximum is

`boxed(
 max_W h(W)-h_bar
 = (1/2) sqrt(
     tr(G(x) Y G(y) Y^T)
     +8 sqrt(prod x prod y)|Delta_2(Y)|
   ).
 )`                                                               (4.5)

No division occurs.  If a kernel weight vanishes, the corresponding triangle degenerates and (4.4)-(4.5) remain valid directly (or by continuity).  The theorem is independent of spectral simplicity, invertibility of `A+B`, or endpoint uniqueness.

### Proof of the Cauchy-Binet factor

Choose oriented orthonormal coordinates in the two triangle planes.  Let `L` and `K` be the resulting `2 x 3` matrices with columns `ell_a` and `k_b`.  Then the nonzero part of `Z` is

`Z_2=L Y K^T`.

Because the columns sum to zero,

`det L_{12}=A_x`, `det L_{13}=-A_x`, `det L_{23}=A_x`,

and likewise for `K`, where

`|A_x|=2 sqrt(x_1x_2x_3)`, `|A_y|=2 sqrt(y_1y_2y_3)`

by Heron's formula.  Cauchy-Binet gives

`det Z_2=A_x A_y Delta_2(Y)`,

which is (4.2).  Equation (4.3) is the trace identity

`||L Y K^T||_F^2=tr(L^T L Y K^T K Y^T)`.

## 5. Exact zero-face target payment

The prior B09 zero-fiber Haar-lift theorem identifies `h_bar` as a convex combination of the 24 permutation endpoint supports.  Hence

`h_bar <= M`.

Put

`Delta_mu=M-h_bar >=0`.

If a global zero-face maximizer has target gap `gamma>0`, then because it must also maximize its fixed-kernel residual fiber, (3.4) gives the **exact identity**

`boxed( ||Z||_* = 2(gamma+Delta_mu). )`                            (5.1)

Therefore the entire zero-face support problem on each fixed kernel pair is equivalent to the single structured inequality

### `MOC4-ZERO-FACE-TRIANGLE-PAYMENT-v1`

`boxed( ||Z||_* <= 2 Delta_mu. )`                                 (5.2)

Using (4.4), this is the explicit scalar inequality

`sqrt( tr(G(x)Y G(y)Y^T)
       +8 sqrt(prod x prod y)|Delta_2(Y)| )
 <= 2 Delta_mu.`                                                  (5.3)

This is not merely a sufficient relaxation: after fixing the zero-face kernels, (5.2) is **equivalent** to support safety of the whole genuine residual `U(2)` fiber.

The remaining work is now phase-free but still source-structured: `Y` is the determinant-product spectral coefficient matrix, `x,y` are the kernel probabilities forced by the same true unitary, and `Delta_mu` is the exact Haar endpoint reserve.  They cannot be chosen independently.

## 6. A tempting chirality mechanism is ruled out exactly

Before using the closed-triangle identities, one might hope that the proper-rotation restriction `SO(3)` pays an orientation or chirality tax relative to an `O(3)` external relaxation.  That route is **universally unavailable on this zero face**.

Indeed, (3.3) gives `sigma_3(Z)=0` identically.  For a rank-two Procrustes matrix, the `SO(3)` and `O(3)` maxima coincide: any optimal planar reflection can be accompanied by a sign flip on the unused normal direction to make the full three-dimensional map proper without changing the objective.

So the genuine cofactor payment is **not** an orientation-sign penalty.  It is the much sharper structural reduction (4.4)-(5.3), which couples the spectral coefficient matrix to the two kernel triangles.  This prevents wasting the next run on an impossible chiral-gap argument.

This also explains why fleet03/B08's pair-trap family is relevant: separate local pair curvatures can miss a nearly cancelling mixed tunnel, whereas (3.4) globally optimizes the entire residual mixed fiber in one shot.

## 7. Compatibility with the new common-lift no-go

Fleet01/B08 proves that a true zero-entry unitary need not admit any probability law reproducing both its degree-one and degree-two compound marginals.  The present theorem does **not** assume such a law.

The only convex-combination input is the already proved **Haar average of the support value** `h_bar<=M`; no individual `P` or `Q` marginal is represented by that same law.  The departure from the average is then computed exactly through the genuine `U(2)->SO(3)` residual orbit.  Hence the new common-lift facet obstruction does not invalidate (3.4)-(5.3).

## 8. Compact conditional end-to-end argument

Assume MOC4 fails.

1. Use the existing genericization architecture to take a positive-gap genuine global support maximizer in the generic simple/nonzero regime; singular and repeated spectra are recovered after generic closure by continuity.
2. By the lead Spin(4) dichotomy together with fleet02/B09 `MOC4-SPIN4-SATURATION-EXCLUSION-v1`, a violating maximizer cannot be supported by a flat/saturated physical pair orbit.
3. **Zero-entry branch:** choose the aligned singleton gauge.  Fleet04/B09 gives rank-two-partial-isometry/cofactor rigidity.  The present theorem then eliminates all residual phases and the entire residual `U(2)` search exactly.  This branch is closed once (5.3) is proved for the structured MOC4 data.
4. **No-zero branch:** the latest lead reduces the generic strict interior to `MSQR` versus `NDI`.  The lead cross-split reserve, B09 r18 cross-polarization cone/frame cap, and fleet03/B20 finite residual gates constrain `MSQR`; `NDI` remains the separate all-negative-definite branch.

Thus a full proof follows from the structured zero-face payment (5.3) plus closure of the lead's strict-interior `MSQR/NDI` branches.  No easier Hermitian/common-block replacement is being counted as target closure.

## 9. First essential missing implication after this run

### `MOC4-ZERO-FACE-TRIANGLE-PAYMENT-v1`

For every structured determinant-product coefficient matrix `Y=X/2-K`, every support direction, and every genuine zero-face kernel pair `x,y` arising from the same unitary, prove (5.3), with `Delta_mu=M-h_bar` evaluated from the exact same support data.

Equivalently, if (5.3) fails, construct actual complex spectra, one common support direction and a true zero-entry unitary whose fixed-kernel Procrustes maximum exceeds `M`.  An arbitrary real `Y`, arbitrary kernel probabilities, arbitrary bistochastic compound data, or a negative formal coefficient is not a source-valid counterexample.

The aligned-external theorem says any genuine zero-face violation must sit in one of 12 bad external support directions; (5.3) is now an exact two-triangle/nuclear-norm form of the nonlinear cofactor payment that such a direction would have to defeat.

## 10. Verdict / limits

**ESSENTIAL_STEP_APPLIED.**  The fleet04/B09 zero-face cofactor variety has been converted into an exact, global, true-unitary Bloch/Procrustes maximization and then into the closed scalar formula (4.5).  The residual phase optimization is eliminated completely.  A proposed orientation/chirality-tax shortcut is also ruled out universally by `rank Z<=2`.

Full MOC4 remains open because the structured inequality (5.3) has not yet been proved and the no-zero strict-interior branch remains independently open.

No numerical computation was used as mathematical evidence in this run.  No benchmark material, credentials, scheduler identifiers, machine paths, email, Drive data, public posting or unrelated private data are present in this report.
