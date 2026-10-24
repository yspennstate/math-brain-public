SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T13:04:35Z.
attacking: coordinate-minor selection — convert the remaining fixed-double-pair/large-diagonal survivor into determinant-weighted E2 curvature currency and a fractional-trace receiver, without selecting or reciprocating one tiny pivot.

# account01/B07 r25 — E3-to-E2 shadow, mixed-volume payment through leverage 2/5, and an E2 half-Riesz receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Coordinate minor selection / GEOMETRY  
Run: `account01-B07-20260923T130435Z-r25`  
Status: `ESSENTIAL_STEP_APPLIED / NEW E3→E2 SHADOW + FRACTIONAL TRACE RECEIVER / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

## 1. Scope and source boundary

The target remains the unrestricted conjecture: for every dimension, independent real ORIGINAL-coordinate inputs with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one universal essential-supremum bound, or give a valid target-level counterexample. No Gaussianity, moments, compact/connected support, log-concavity, iid assumption, diagonal-basis assumption, or independence after rotation is introduced. Continuity is tracked separately.

The final pre-publication control refresh was `math-research-brain@c90bd5cd5bb247315da726ad09cf034e6c578fc6`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no B07 pause. The live correction inbox was reread. This report does not use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, positive conditional projection-density moments, naive fiber-sup integration, or a one-good-minor reduction.

Actual mathematical dependencies:

1. Own r24 fixed-double-pair report: `yspennstate/math-open-problems@6360df8421f192175027c1e5334028e2f047533b`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T120512Z-r24/REPORT.md`.
2. Own r20 mixed-order fractional-compound BL theorem: `yspennstate/math-open-problems@7bf5a0bd8a8d2fa12a5c2370811ecfe5d2cf7444`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T090322Z-r20/REPORT.md`.
3. Latest completed designated partner account02/B07: `yspennstate/math-open-problems@646c1395596ed9c4b1f77cecdc9e9506cf793c22`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/account02-B07-20260923T123606Z-fa88b2df/REPORT.md`. Its exact anchored-volume marginal identity and mixed E3/E2 transport theorem are applied below at explicit inequalities.

Full QFORM and the full-target continuity conclusion remain OPEN.

## 2. Start from the entire fixed-double-pair bank

Let `I,J` be disjoint physical ORIGINAL-coordinate banks and let `M=A[I,J]`. Fix physical row anchors `r,s in I` and physical column anchors `a,b in J`. The r24 bank is

`H = sum_(i in I\{r,s}, j in J\{a,b}) det M[{r,s,i},{a,b,j}]^2 >0`.      (2.1)

Let the complete two-fixed-row third-volume packet be

`Gamma = sum_(i in I\{r,s}) sum_(|T|=3) det M[{r,s,i},T]^2`.             (2.2)

Trivially

`Gamma >= H`.                                                            (2.3)

Write the two fixed physical rows as vectors `u,v in R^J`, set `K=[u;v]`, and define their complete second-volume mass

`Z2 := sum_(|T|=2) det K[:,T]^2 = det(KK^T)`.                            (2.4)

Let `P` denote orthogonal projection in coefficient space `R^J` onto `span{u,v}` and let `w_i` be every residual physical row. The designated partner's exact anchored-volume identity gives

`Gamma = Z2 sum_i ||(I-P) w_i||_2^2`.                                    (2.5)

Since the residual squared norm in (2.5) is at most `||M||_F^2`, writing

`F:=||M||_F`,                                                            (2.6)

we obtain the new scale-matching shadow inequality

`boxed: Z2 >= Gamma/F^2 >= H/F^2.`                                      (2.7)

This is the first main coordinate-minor conclusion of the run. A complete third-minor bank containing a fixed physical row pair automatically generates a complete physical `E2` packet on that same row pair at the correct determinant scale. No individual `2x2` or `3x3` minor is selected, and no determinant is reciprocated.

## 3. Actual application of the latest designated-partner theorem

Let `ell_j=P_jj` be the column inclusion marginals of the canonical squared-`2x2`-minor law of `K`. The designated partner proves that the anchored `E3` column marginals satisfy exactly

`beta_j = ell_j + c_j`,                                                 (3.1)

where `c_j>=0`, `sum_j ell_j=2`, `sum_j c_j=1`, and `sum_j beta_j=3`.

If

`ell_*:=max_j ell_j <=1/4`,                                             (3.2)

the partner's completed `QFORM-MIXED32-DISJOINT-VOLUME-v1` gives a continuous full-ambient density with

`||p_Q||_infinity < 16.488 (Gamma Z2)^(-1/10)`.                         (3.3)

Applying (2.3) and (2.7) to the actual inequality gives

`boxed:
 ||p_Q||_infinity <16.488 F^(1/5) H^(-1/5).`                            (3.4)

This is the required current-run use of the designated partner's completed result. It retains arbitrary same-bank curvature, outside couplings, affine terms, signs and additional spectrum.

The partner also pays the genuinely diffuse anchored-volume branch: if

`max_j beta_j <=2/3`,                                                    (3.5)

then

`boxed:
 ||p_Q||_infinity <=9 sqrt(3e) Gamma^(-1/6)
                  <=9 sqrt(3e) H^(-1/6),`                               (3.6)

again with a continuous density.

For the inherited live scale from r23/r24,

`H >= c_* F^6,   c_*:=1/64123518131896320`,                             (3.7)

(3.4) is `<37894.09 F^(-1)` and (3.6) is `<16259.98 F^(-1)`. These scale-sensitive constants are controls, not a claim that `F` itself is universally bounded below in every decomposition.

## 4. Extend the mixed-volume payment from leverage 1/4 to leverage 2/5

The partner threshold `ell_*<=1/4` comes from insisting on a disjoint coupling of canonical E2 and E3 samples. The older r20 mixed-order BL theorem allows a direct weighted mixture and therefore a larger leverage window.

Take mixing weight

`w=1/10`,                                                           (4.1)

put the anchored `E3` packet at weight `w` and the fixed-row-pair `E2` packet at weight `1-w`, and use `q=1`. The effective determinant order is

`r=2+w=21/10 >2`.                                                     (4.2)

By (3.1), the mixed column inclusion marginal is

`p_j = w beta_j +(1-w)ell_j = ell_j +(1/10)c_j`.                    (4.3)

Hence

`ell_*<=2/5  ==>  p_j<=1/2=q/2` for every `j`.                       (4.4)

The r20 theorem is therefore applicable on the physical column side. Its determinant constant is

`K = 10^(1/10)(10/9)^(9/10) Gamma^(1/10) Z2^(9/10)`.              (4.5)

Since `r-2q=1/10`, the density bound is

`||p_Q||_infinity <=21e K^(-5/21)`.                                  (4.6)

Using (2.3) and (2.7),

`boxed:
 ||p_Q||_infinity
 <= C_(2/5) F^(3/7) H^(-5/21),`                                     (4.7)

where

`C_(2/5)
 =21e [10^(1/10)(10/9)^(9/10)]^(-5/21)
 =52.8322463052...`.                                                  (4.8)

At the live scale (3.7), this is

`||p_Q||_infinity < 530358.914 F^(-1)`.                              (4.9)

The conclusion in this branch is a continuous density, because the r20 proof produces an `L^1` characteristic-function majorant.

Thus an unpaid fixed-row-pair survivor must satisfy

`boxed: ell_*>2/5.`                                                   (4.10)

Since `sum ell_j=2`, there can be at most four physical columns with leverage `>2/5`. This does not itself finish the branch, but it converts a diffuse coordinate-minor obligation into a bounded physical hub set while preserving the full determinant packet.

## 5. New analytic receiver: an E2 packet controls the half-Riesz potential

The next step is designed for a scalar physical pivot, where one does not need an `L^infinity` density theorem for the residual form; a uniform `1/2`-Riesz potential is exactly the right currency.

### Theorem 5.1 — `QFORM-E2-FRACTIONAL-TRACE-v1`

Let `C=A[I,J]` be any physical cross block between disjoint ORIGINAL-coordinate banks, and let `P2` be any positive packet of physical `2x2` minors with squared-determinant mass

`Z2 = sum_((S,T) in P2) det C[S,T]^2 >0`.                            (5.1)

Let `alpha_i` be its normalized inclusion marginals on one physical side, so `sum alpha_i=2`. Suppose for some

`1<=q<2`                                                            (5.2)

we have

`max_i alpha_i <=q/2`.                                               (5.3)

Then the full ambient quadratic-plus-affine form `R`, retaining arbitrary within-bank quadratic terms, outside couplings and all other coefficients, satisfies

`boxed:
 sup_s E |R-s|^(-1/2)
 <= [8 sqrt(e/2)/(2-q)] q^(-1/4) Z2^(-1/8).`                       (5.4)

The same theorem holds with the other physical side's marginals.

#### Proof

Use the same original-coordinate Weyl differencing as in r20. The degree-two determinant packet alone gives, through the diagonal-plus-Gram determinant expansion and weighted AM--GM, a Brascamp--Lieb determinant certificate of order two. Repeating the r20 Jensen/Hausdorff--Young calculation with determinant order `r=2` yields

`|phi_R(t)|
 <= min(1,
        e^(1/q) q^(-1/(2q)) pi^(1/q)
        Z2^(-1/(4q)) |t|^(-1/q)).`                                (5.5)

Equivalently, with

`t0 = pi e q^(-1/2) Z2^(-1/4),`                                    (5.6)

we have

`|phi_R(t)| <= min(1,(t0/|t|)^(1/q)).`                             (5.7)

The Fourier transform of the one-dimensional Riesz kernel `|x|^(-1/2)` is `sqrt(2pi)|t|^(-1/2)` under the convention used here. Abel regularization and monotone convergence therefore give

`E|R-s|^(-1/2)
 <=(2pi)^(-1/2) integral_R |phi_R(t)| |t|^(-1/2) dt.`              (5.8)

Because `q<2`, (5.7) is integrable against `|t|^(-1/2)`. Directly,

`integral_R min(1,(t0/|t|)^(1/q)) |t|^(-1/2) dt
 = [8/(2-q)] sqrt(t0).`                                             (5.9)

Substituting (5.6) into (5.8) gives exactly (5.4). QED.

At the useful fixed threshold `q=3/2`, condition (5.3) is `max alpha_i<=3/4` and

`boxed:
 sup_s E|R-s|^(-1/2)
 <=16.8550253878 Z2^(-1/8).`                                      (5.10)

The theorem is deliberately a fractional-potential statement, not a claim that every order-two quadratic form has bounded density; the latter is false in opposite-sign rank-two controls.

## 6. Pay a large physical diagonal unless the Schur E2 packet has a near-coloop

Return to the fixed-double-pair bank. The preceding r23/r24 edge extraction gives an actual physical off-diagonal coefficient `b=A_rs` satisfying

`|b| >= sqrt(H)/F^2`.                                               (6.1)

One branch of the principal-pair alternative has a physical diagonal, say

`|a|:=|A_rr| >= |b|/2 >= sqrt(H)/(2F^2).`                          (6.2)

Let `u=A[r,J]`, `v=A[s,J]`, and let `w_i=A[i,J]` be the residual physical rows of the same cross block. Complete the square only in the ORIGINAL coordinate `X_r`. In the exact scalar Schur remainder the cross rows become

`v' = v-(A_sr/a)u`,
`w_i' = w_i-(A_ir/a)u`.                                            (6.3)

Wedge antisymmetry gives the exact identities

`u wedge v' wedge w_i' = u wedge v wedge w_i`.                      (6.4)

Define the complete incident second-volume packet in the Schur cross block by

`Z2^S := sum_i ||v' wedge w_i'||^2`.                               (6.5)

Since the complete two-fixed-row third volume satisfies

`Gamma = sum_i ||u wedge v wedge w_i||^2`,                          (6.6)

(6.4) and the elementary exterior-product bound give

`Gamma <= ||u||_2^2 Z2^S <= F^2 Z2^S`.                             (6.7)

Therefore

`boxed: Z2^S >= Gamma/F^2 >= H/F^2.`                               (6.8)

This is a second E3-to-E2 shadow, now *after an exact physical scalar Schur complement*. No small Schur determinant has been inverted; the incoming third-volume bank is retained by the wedge identity.

Writing the completed-square decomposition as

`Q = a (X_r+L(Y)/a)^2 + R(Y)`,                                     (6.9)

where `Y` is the collection of all remaining original coordinates, the cap-one density of `X_r` gives conditionally

`p_(a(X_r+h)^2)(y) <= |a|^(-1/2)|y|^(-1/2)`.                      (6.10)

Thus

`||p_Q||_infinity
 <= |a|^(-1/2) sup_t E|R-t|^(-1/2).`                              (6.11)

Let `theta_j` be the column inclusion marginals of the packet (6.5). If

`max_j theta_j <=3/4`,                                             (6.12)

Theorem 5.1 at `q=3/2`, together with (6.2) and (6.8), gives

`boxed:
 ||p_Q||_infinity
 <=23.8366054976 F^(5/4) H^(-3/8).`                               (6.13)

At the live scale (3.7),

`||p_Q||_infinity < 4.7849336e7 F^(-1).`                           (6.14)

This branch establishes absolute continuity and an essential `L^infinity` bound. I do **not** promote it to a continuity statement: (5.4) is a half-Riesz estimate and the present argument does not prove a continuous representative after averaging the conditional square kernels.

If (6.12) fails, the exact retained structural conclusion is

`boxed: max_j theta_j>3/4.`                                        (6.15)

Since the marginal sum is two, at most two physical columns can satisfy `theta_j>3/4`. The formerly generic "large diagonal" branch is therefore reduced to a fixed-row E2 packet with a one- or two-column near-coloop hub, while all nonzero Schur curvature and the remaining spectrum stay present.

## 7. What is now paid and what is not

For the fixed-double-pair survivor, the new aggregate shadow (2.7) and the designated partner pay the low anchor-plane leverage branch; the weighted mixed-volume theorem enlarges this paid window to `ell_*<=2/5`. The new fractional-trace theorem pays a large physical diagonal whenever the exact scalar-Schur E2 packet has column marginals at most `3/4`. The prior conditioned-indefinite principal-pair/high-tail branch remains paid by r24's completed partner application.

The first remaining B07 implication is now:

`QFORM-DOUBLEHUB-OR-E2-NEARCOLOOP-RECEIVER-v1`.

After the current exits fail, the fixed two-row anchor plane has a physical column hub of leverage `>2/5` (hence at most four such hubs); if the anchored E3 diffuse theorem also fails there is a physical column with anchored-E3 marginal `>2/3`; and the scalar-large-diagonal branch can survive only if the exact Schur E2 packet has a column marginal `>3/4` (at most two such near-coloops). The next receiver must spend these grouped-coordinate hubs before reciprocal pivot inversion and must retain arbitrary same-bank curvature and every nonzero low-rank tail. The R1/R2/rank-four-tube faces recorded in r24 are not silently discarded and remain obligations where the present E2-shadow exits do not apply.

No full target solution is claimed. Full-target continuity remains open.
