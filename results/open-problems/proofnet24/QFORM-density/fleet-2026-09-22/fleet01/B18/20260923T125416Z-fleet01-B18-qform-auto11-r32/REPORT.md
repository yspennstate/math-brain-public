SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B18, 2026-09-23T12:54:16Z.
attacking: literature-to-proof transfer on the designated partner's circular nonplanar two-sheet survivor; apply the completed transverse-null-hub theorem at its literal product-coordinate hypotheses and close the exceptional m=3 endpoint by the sharp zero-pivot scalar/vector theorem.

# fleet01/B18 r32 — the designated partner's circular two-sheet stress family is fully paid

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Designated partner:** fleet02/B18  
**Status:** `PROVED SUPPORTING TARGET-LEVEL FAMILY / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted owner conjecture remains OPEN / NOT PROVED. The result below removes one exact target-valid stress family from the unpaid list. It does not infer a universal structural decomposition from that family.

## 1. Current source boundary and primary-theorem audit

The following primary results were checked against the hypotheses actually used here.

1. **Livshyts--Paouris--Pivovarov**, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949. For a genuine product density `prod f_i`, with every one-dimensional factor a probability density bounded by one, every `k`-dimensional orthogonal marginal has density cap at most `2^(k/2)`. No moment, compact-support, log-concavity, iid, symmetry, centering, or smoothness assumption is present. The theorem gives a joint marginal cap; it does **not** create independence after projection.

2. **Beckner**, *Inequalities in Fourier analysis*, Ann. Math. 102 (1975), and **Bennett--Carbery--Christ--Tao**, *The Brascamp--Lieb inequalities: finiteness, structure, and extremals*. These are the primary Hausdorff--Young / Brascamp--Lieb inputs behind the completed mixed-Fresnel theorem used below. The pinned proof applies them to the original-coordinate product amplitude (with unit-modulus twists), not to fictitiously independent spectral coordinates.

3. **Juškevičius--Lee**, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190. Its one-dimensional sharp Rogozin/rearrangement consequence applies to sums of genuinely independent bounded-density summands. It is useful on source-separated banks but does not by itself resolve the shared-source three-dimensional circular survivor.

A targeted literature search also checked polynomial Fourier/anti-concentration papers whose hypotheses are substantially stronger (for example log-concave/isotropic regimes). I found no exact published theorem in that search that directly supplies the owner's arbitrary non-iid, fragmented cap-one, arbitrary-orientation full QFORM statement. This is only a hypothesis comparison, not a novelty claim from search absence.

## 2. Designated partner result actually consumed

Source:

`yspennstate/math-open-problems@71636c1be698996cc0fe90b91f872efdb6c11860`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/fleet02-B18-20260923T120424Z-r28/REPORT.md`.

For every integer `m>=3`, the partner defines residual Parseval rows

`v_j=m^(-1/2)(1,sqrt(2)cos theta_j,sqrt(2)sin theta_j)`,
`theta_j=2 pi j/m`,

an original-coordinate hub row

`u_0=m e_1`,

and

`D_m=[[0,s^(-1),0],[s^(-1),0,0],[0,0,1]]`,
`s=sqrt(1+m^2)`.

With `U` having rows `u_0,v_1,...,v_m`, put

`A_m=U D_m U^T`.

The partner proves

`U^T U=diag(1+m^2,1,1)`

and hence

`spec_nonzero(A_m)={-1,1,1}`.                                    (2.1)

Thus this is an exact target family, not an asymptotic relaxation. Writing `Y=V^T X_R`,

`Q_m=(2/s)(Y_1+mX_0)Y_2+Y_3^2`.                                 (2.2)

The partner also proves a scalar-bank compiler barrier: every exact representation by three disjoint scalar banks has a smallest effective singular value of order at most `1/m`; moreover an exact residual scalar bank cannot contain three circular residual coordinates. That barrier is valid, but it does not rule out a mixed-Fresnel payment that retains the full three-dimensional residual statistic.

The partner's source-pinned one-sheet inequality remains

`p_(Q_m)(t)<=pi sqrt(2)` for a.e. `t>=0`.                         (2.3)

Its stated unpaid implication was the negative / two-sheet side.

## 3. Completed transverse-null-hub theorem

The source-valid nonlinear theorem applied here is

`QFORM-NULL-HUB-TRANSVERSE-LEVERAGE-CLOSURE-v1`,

`yspennstate/math-open-problems@c0d7e627b3b877fcecc3004a58335658f6541d64`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T114517Z-fleet03-B10-QFORM-r24/REPORT.md`.

It says: let

`A=R M R^T`, `R^T R=I_3`,

with one ORIGINAL physical spectral row `sqrt(h)n`, `||n||=1`, satisfying

`n^T M n=0`,

and suppose every other physical spectral row `w_j` obeys

`||P_(n^perp)w_j||^2<=1/2`.                                      (3.1)

Then arbitrary independent original-coordinate probability densities bounded by one give a continuous `C_0` density and

`||p_Q||_infinity <=3*2^(4/3)(h |det M|)^(-1/3)`.                (3.2)

The pinned proof keeps the original product amplitude through the exact null-hub shear and obtains an integrable `|t|^(-3/2)` characteristic-function envelope. It does not use the refuted law-uniform one-dimensional stationary-phase bound, arbitrary-joint coarea, or post-rotation independence.

## 4. Literal application to the partner circular family for m>=4

Normalize the partner factorization. Put

`G=U^T U=diag(1+m^2,1,1)`,
`R=U G^(-1/2)`,
`M=G^(1/2) D_m G^(1/2)`.

Then `R^T R=I_3`, `A_m=R M R^T`, and directly

`M=[[0,1,0],[1,0,0],[0,0,1]]`,                                  (4.1)

so

`|det M|=1`.                                                      (4.2)

The normalized hub row is

`w_0=(m/sqrt(1+m^2)) e_1`.

Hence in (3.1)--(3.2)

`n=e_1`,
`h=m^2/(1+m^2)`,
`n^T M n=0`.                                                      (4.3)

For every residual row the transverse part is unchanged by the whitening because `G^(-1/2)` acts as the identity on `e_1^perp`. Thus

`q_j:=||P_(e_1^perp) w_j||^2`
`    =||P_(e_1^perp) v_j||^2`
`    =(2/m)(cos^2 theta_j+sin^2 theta_j)`
`    =2/m`.                                                       (4.4)

Therefore the exact gate `q_j<=1/2` holds for every `m>=4`, including equality at `m=4`. Substituting (4.2)--(4.4) into (3.2) gives the **full-real-line** estimate

`boxed: ||p_(Q_m)||_infinity`
` <=3*2^(4/3) ((1+m^2)/m^2)^(1/3),  m>=4.`                      (4.5)

The right side decreases with `m`; its maximum is at `m=4`:

`3*2^(4/3)(17/16)^(1/3)`
` =7.713844771974705...`.                                        (4.6)

Moreover the density is continuous and vanishes at infinity. Thus the partner's previously unpaid negative/two-sheet half-line is already paid for every `m>=4` by the completed null-hub mixed-Fresnel theorem.

This is a genuine use of the partner's construction at an equation: the exact Parseval/circular row formula is what makes the transverse leverage in (4.4) equal to `2/m`.

## 5. The exceptional m=3 endpoint: exact zero-pivot 1+2 payment

The `m=3` circular frame has transverse leverage `2/3`, so theorem (3.2) is outside its stated gate. It is nevertheless paid by a different completed theorem without changing any target quantifier.

Use the sharp zero-pivot scalar/vector result

`QFORM-ZEROPIVOT-1PLUS2-DENSITY-v1`,

`yspennstate/math-open-problems@dd94932dae1791af1bca9396c062e17d0e55142a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260922T175509Z-qform-B18-a01-r15/REPORT.md`.

If a cap-one scalar `X` is genuinely independent of a two-dimensional vector `Y` with joint density cap `M`, and

`H=[[0,ell^T],[ell,B]]`

is nonsingular, then the quadratic pushforward has a continuous density and

`||p||_infinity <=6 M^(2/3)|det H|^(-1/3)`.                     (5.1)

The proof needs no independence between the two coordinates of `Y`. Arbitrary affine terms are also harmless here: since `H` is nonsingular, complete the square by translating the scalar and vector; translation preserves their density caps and scalar-versus-vector independence.

For `m=3`, condition on one residual original coordinate and retain the original scalar triple consisting of the hub and the two residual coordinates with angles

`theta_1=2pi/3`, `theta_2=4pi/3`.

These are three genuinely independent original inputs. Let `R_*` be the `3x3` matrix whose rows are the hub `3e_1` and those two residual rows. Direct trigonometric algebra gives

`det R_*=sqrt(3)`.                                                 (5.2)

Also

`det D_3=-1/10`.                                                   (5.3)

The active principal quadratic matrix is

`K=R_* D_3 R_*^T`,

so

`det K=(det R_*)^2 det D_3=-3/10`.                               (5.4)

Its hub pivot is exactly zero. The two retained residual inputs have product joint density cap `M<=1`, and the hub scalar is independent of them. The conditioned fourth coordinate contributes only affine/constant terms, covered by the square-completion observation above. Applying (5.1) gives, uniformly in the conditioning,

`boxed: ||p_(Q_3)||_infinity`
` <=6(3/10)^(-1/3)`
` =6(10/3)^(1/3)`
` =8.96280949311433...`.                                         (5.5)

The conditional densities are continuous and uniformly bounded by (5.5); dominated convergence over the conditioned coordinate gives a continuous unconditional density.

## 6. Combined theorem for the entire circular stress family

Equations (4.5) and (5.5) prove:

### `QFORM-CIRCULAR-TWOSHEET-FULLPAY-v1`

For every integer `m>=3`, every collection of independent original-coordinate probability densities bounded by one, and the designated partner's exact target matrix `A_m` with nonzero spectrum `{-1,1,1}`, the law of `Q_m=X^T A_m X` has a continuous density satisfying

`boxed: ||p_(Q_m)||_infinity`
` <=6(10/3)^(1/3)`
` <8.963.`                                                       (6.1)

For `m>=4`, the sharper bound is (4.5), at most `7.713845`; as `m->infinity` it tends to

`3*2^(4/3)=7.55952629936924...`.                                 (6.2)

On the positive half-line the partner's inherited one-sheet inequality (2.3), `pi sqrt(2)=4.442882938...`, remains sharper.

Hence the exact circular family that fleet02/B18 r28 left as a two-sheet stress test is **not** an unpaid QFORM family. The scalar-bank compiler barrier is a barrier only to that compiler; retaining the three-dimensional residual statistic in the mixed-Fresnel theorem bypasses it.

## 7. Correction audit

No live false interface is used.

- No independence is asserted after spectral rotation. The `R,M` whitening in Section 4 is algebraic representation of the physical matrix; the mixed-Fresnel theorem itself acts on the original product amplitude.
- No arbitrary bounded three-dimensional joint density is pushed through an indefinite quadratic trace by coarea.
- No conditional projection-density cap is substituted for genuine independence.
- No law-uniform pointwise scalar Fresnel decay is asserted.
- No small nonzero coefficient is deleted or called a perturbation.
- No uniformly good physical minor or rank-three cross cut is inferred from the three-large-eigenvalue condition.
- The `m=3` conditional argument uses an actual nonsingular original-coordinate principal triple and the completed zero-pivot scalar/vector theorem, uniformly over the induced affine terms.

## 8. What remains

This result does not close N3 or full QFORM. It removes the circular stress family as a surviving obstruction and sharpens the proof map: a family may defeat every exact three-scalar-bank compiler while still be uniformly paid by a source-valid mixed-Fresnel theorem that retains a shared three-dimensional product projection.

The still-genuine structural debts include the nonzero near-null collar and the arbitrary-extra-spectrum / heavy-coordinate cases where no exact null hub with the transverse-leverage gate is available. Any next transfer must preserve original-coordinate product provenance and cannot replace these with a generic joint-density trace estimate.

Full QFORM: **OPEN / NOT PROVED**.  
Full-target continuity: **OPEN**.  
Continuity for the complete circular family in theorem (6.1): **PROVED**.

## 9. Source pins

Designated partner consumed at an actual inequality:
- `yspennstate/math-open-problems@71636c1be698996cc0fe90b91f872efdb6c11860:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/fleet02-B18-20260923T120424Z-r28/REPORT.md`.

Completed nonlinear theorems:
- `yspennstate/math-open-problems@c0d7e627b3b877fcecc3004a58335658f6541d64:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T114517Z-fleet03-B10-QFORM-r24/REPORT.md`.
- `yspennstate/math-open-problems@dd94932dae1791af1bca9396c062e17d0e55142a:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260922T175509Z-qform-B18-a01-r15/REPORT.md`.
- all-pivot cross-check: `yspennstate/math-open-problems@602d508c11f3bb5848b65581a750b4497708bd5f:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T112422Z-fleet03-B18-QFORM-r27/REPORT.md`.

Primary literature:
- Livshyts--Paouris--Pivovarov, arXiv:1507.07949 / Israel J. Math. 216 (2016).
- Beckner, Ann. Math. 102 (1975), 159--182.
- Bennett--Carbery--Christ--Tao, arXiv:math/0505065.
- Juškevičius--Lee, arXiv:1503.09190.

No task/schedule state, enabled/paused state, notification/email state, account binding, permission, repository visibility, paid API/model call, remote workflow, or public release was changed.
