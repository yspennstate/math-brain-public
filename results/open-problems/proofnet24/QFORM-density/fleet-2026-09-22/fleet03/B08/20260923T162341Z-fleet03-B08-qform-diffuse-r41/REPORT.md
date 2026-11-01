SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T16:23:41Z.
attacking: join diffuse volume exits to high-leverage/low-cross-rank survivors quantitatively while retaining the full spectrum.

# fleet03/B08 r41 — erase the r40 high-leverage gap and sharpen the survivor to R1/R2

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T162341Z-fleet03-B08-qform-diffuse-r41`  
Owner control at final prepublication refresh: `2026-09-22.15`  
Fresh brain main used at final prepublication refresh: `07cdc0ed6068c8a519bdf3049cca666c11789d37`  
Assignment: diffuse eigenvector case  
Classification: `ESSENTIAL_STEP_APPLIED / NEW SOURCE-SYNTHESIS ROUTER / FULL TARGET OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Global continuity remains OPEN. The paid branch below has a continuous `C_0` density. All variables remain in original independent coordinates; no moment, compact-support, connected-support, Gaussian, log-concavity, iid, spectral-coordinate independence, arbitrary-joint coarea cap, pointwise scalar Fresnel decay, coefficient-small random perturbation, or worst-fiber supremum is used.

## 1. Immediate predecessor and first missing implication

The immediate predecessor is

`yspennstate/math-open-problems@6b6cd1c3be8a9c23a3424593a38b0450acb61cfa`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T144913Z-fleet03-B08-qform-diffuse-r40/REPORT.md`.

Its theorem `QFORM-TRIANGLE-RANK1-ESCAPE-v1` considers an ACTUAL physical triangle `T` and its complement,

```
A = [[T,C],
     [C^T,D]],
```

where the triangle has rank-one defect `Delta_T`. At the fixed target scale `s3(A)>=L`, if

`Delta_T<=L/4` and `||D||op<3L/8`,

r40 proves

`boxed: s1(C)>3L/8.`                                               (1.1)

It then used the required volume-stability result to pay the branch

`s3(C)>=L/16` AND `max row leverage<=1/2`

with a continuous `<368/L` density, while leaving two explicit survivors:

- high leverage at rank three;
- low cross rank.

The present run attacks exactly that interface.

## 2. Required newest-Claude theorem applied at the actual r40 implication

The required source is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its baseline theorem says that if an original-coordinate cross block `M=M0+E` has

`s3(M0)>=a`, `max_i(P_range(M0))_ii<=1/2`, `||E||op<=a/16`,

then the full ambient quadratic-affine form has a continuous `C_0` density with

`||p_Q||infinity <23/a`.

Apply it exactly to the r40 block with `M0=M=C^T`, `E=0`, and `a=L/16`. On the low-leverage rank-three branch it gives

`boxed: ||p_Q||infinity <368/L, p_Q in C_0.`                      (2.1)

All triangle curvature, all of `D`, outside couplings, and affine terms are retained. This is the required current-Claude result applied to an actual missing implication, not merely cited.

The remaining r40 gap after (2.1) was the same rank-three cross scale with a leverage-heavy physical coordinate.

## 3. Completed physical-three-side theorem that removes the leverage gate

A source search found a theorem matching this exact scope, so the early independent route in `CHECKPOINT.md` was stopped rather than duplicated.

Canonical source snapshot:

`yspennstate/math-open-problems@a9cb334579e92753035a96d258fa94cac01cdbfc`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/B02-20260922T120900Z-qform-r11/REPORT.md`.

Theorem `QFORM-PHYSICAL-PIVOT-CROSSBLOCK-FOURIER-v1` states: if one side of an ORIGINAL-coordinate cross block has exactly `r>2` physical coordinates, the block has rank `r`, and its nonzero singular values have product `Delta`, then the full ambient form has a continuous `C_0` density and

`||p_Q||infinity <=sqrt(2) r/(r-2) Delta^(-1/r).`                 (3.1)

For `r=3`,

`boxed: ||p_Q||infinity <=3sqrt(2) (s1 s2 s3)^(-1/3).`            (3.2)

The proof conditions only outside original coordinates. The three-coordinate side keeps its product density cap directly; the other side is projected only inside the Fourier/Plancherel argument. Arbitrary same-bank quadratic terms and outside couplings are retained. No random spectral rotation is declared independent.

In r40 the triangle is exactly three physical coordinates. Therefore orient the cross block with that triangle as the size-three side. Equation (3.2) applies to `C` whenever `rank C=3`, with no leverage hypothesis at all.

## 4. Main r41 compiler — `QFORM-R40-RANK3-OR-R1R2-v1`

Assume the r40 outside-cross state (1.1):

`Delta_T<=L/4`, `||D||op<3L/8`, `s3(A)>=L`, hence `s1(C)>3L/8`.

Then exactly one of the following three alternatives can be used.

### P. Paid physical-three-side branch

If

`s2(C)>=L/8` and `s3(C)>=L/64`,                                  (4.1)

then

`s1(C)s2(C)s3(C)
 > (3L/8)(L/8)(L/64)
 =3L^3/4096.`                                                    (4.2)

Apply (3.2):

`||p_Q||infinity
 <3sqrt(2)(3L^3/4096)^(-1/3)
 =(48sqrt(2)/3^(1/3)) L^(-1)`

`=47.0669240549.../L <47.067/L.`                                (4.3)

This branch has a continuous `C_0` density.

### R1. Quantitative rank-one tube

If

`s2(C)<L/8`,                                                     (4.4)

then, by Eckart--Young,

`boxed: dist_op(C,{rank<=1})<L/8.`                               (4.5)

The strong first singular direction `s1(C)>3L/8` is retained.

### R2. Quantitative rank-two tube

If (4.4) fails and the paid branch does not apply, then `s2(C)>=L/8` and necessarily

`boxed: s3(C)<L/64,}`                                            (4.6)

so

`boxed: dist_op(C,{rank<=2})<L/64.`                              (4.7)

Again `s1(C)>3L/8` and `s2(C)>=L/8` are retained.

Thus the former r40 trichotomy

`diffuse rank3 / high leverage / low cross rank`

is replaced, without any leverage condition, by the sharper compiler

`boxed: continuous <47.067/L  OR  R1 rank-one tube L/8  OR  R2 rank-two tube L/64.`    (4.8)

This is the substantive r41 advance. The high-leverage rank-three survivor is gone. The constants intentionally line up with the current fleet01/B20 R1/R2 thresholds, making the next grouped-low-rank handoff direct.

A simpler but weaker one-line consequence is: if merely `s3(C)>=L/16`, then (3.2) gives

`||p_Q||infinity <=48sqrt(2)/L<68/L`,                             (4.9)

again with no leverage gate. Hence even the exact branch split used in r40 is now fully paid at rank three.

## 5. Why this respects the live corrections

No bounded-density projection is pushed through a generic indefinite quadratic map. Instead the source theorem controls the characteristic function of the complete two-bank quadratic form, with arbitrary self phases retained as complex amplitudes and an integrable `|t|^{-3/2}` Fourier tail.

No tail matrix is treated as a small random variable. In R1 and R2 the operator-distance statements are deterministic coefficient geometry only; the tail remains inside the full quadratic form and is explicitly still unpaid.

No general rotation of the random coordinates is assigned product structure. The only exactly-three side is a set of three ACTUAL physical coordinates. Singular vectors are used only in matrix estimates inside the already-proved Fourier theorem.

The false one-good-minor principle is not used: (4.3) spends the entire singular-product determinant currency of the rank-three cross block.

## 6. Early checkpoint preserved but superseded by the stronger source match

Before locating the fleet02/B02 theorem, this run proved a narrower high-leverage statement and saved it in `CHECKPOINT.md`.

For a literal `m x 3` cross block with `s3(C)>=gamma` and a row leverage `ell_i>1/2`, the anchored volume identity gives

`Z_i=ell_i det(C^T C)`,

`2Z_i/||C_i|| >sqrt(2) gamma^5`.

The r28 mixed-order theorem would then pay the secondary-diffuse case by

`||p_Q||infinity <57.882/gamma`,

and failure yields two physical rows whose `2 x 3` cross block has `E2>(3/10)gamma^4`, hence an `L^3` grouped density credit.

Those identities are correct and regression-checked, but this route is no longer claimed as the preferred new theorem because (3.2) covers the entire rank-three scope more strongly and without the secondary occupancy split. This follows the owner rule that a source-matching completed theorem ends duplicate work on that exact scope.

## 7. Designated partner fleet04/B08 applied to the surviving low-rank geometry

The completed designated partner is

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B08/20260923T091414Z-fleet04-B08-QFORM-r1/REPORT.md`.

For the scaled anisotropic exact-rank-two family

`Q_(R,L)=L X0^2+2LR U1V1+2L R^(-1)U2V2`, `R>=3`,

it proves

`boxed: ||p_(Q_(R,L))||infinity <7.251/L.`                        (7.1)

This family lands on BOTH sides of the new low-rank taxonomy:

- for `3<=R<8`, its rank-two cross block has `s2=L/R>L/8` and `s3=0`, so it is an R2 endpoint;
- for `R>=8`, `s2=L/R<=L/8`, so it is an R1 endpoint.

Thus (7.1) is an actual partner-result application to the new r41 split: the grouped anisotropic mechanism uniformly pays an exact model spanning both surviving geometries. It also shows why R1/R2 should not be mistaken for counterexample geometry. What remains is leakage stability when those exact grouped arms sit inside the arbitrary full ambient form.

As an additional safe scope extension, any independent block-diagonal tail `W` on disjoint original coordinates preserves (7.1), because

`p_(Q_(R,L)+W)=p_(Q_(R,L))*mu_W`

and convolution with a probability measure cannot increase `L^infinity`. This does not cover coupled leakage and is not claimed to do so.

## 8. Updated first unpaid implication

Inside the r40 near-rank-one-triangle / small-`D` escape, the first unpaid cross implication is now

`QFORM-R40-R1R2-LEAKAGE-STABLE-GROUPED-RECEIVER-v1`:

1. **R1:** `s1(C)>3L/8`, `s2(C)<L/8`;
2. **R2:** `s1(C)>3L/8`, `s2(C)>=L/8`, `s3(C)<L/64`.

The correct next mechanism is not another leverage audit. It is to retain the exact low-rank core together with its full same-bank curvature and its actual operator tail, then either:

- extend the fleet04/B08 grouped anisotropic receiver stably to that leakage; or
- show the leakage itself necessarily regenerates a source-valid rank-three physical-cross product large enough for (3.2), or a separately paid curvature certificate.

The other r40 alternatives remain: genuine local determinant currency, or complementary principal curvature `||D||op>=3L/8`. They are not silently declared paid here.

## 9. Continuity and global status

The paid branch (4.3), and the weaker branch (4.9), have a continuous `C_0` density because their characteristic functions are integrable by the source Fourier theorem.

The designated partner endpoint (7.1) establishes essential boundedness but does not, from its cited proof, supply continuity. Global continuity therefore remains OPEN.

The unrestricted universal QFORM conjecture remains OPEN. No counterexample was found.

## 10. Computation / regression record

`CHECKS.py` and `CHECKS.txt` beside this report record

- `48sqrt(2)/3^(1/3)=47.066924054926076`;
- the weaker `48sqrt(2)=67.882250993908570`;
- the partner constant `7.250055108887958`;
- 1,000 seeded random-frame checks of the Cauchy--Binet/leverage and pair-inclusion identities used in the superseded checkpoint, with maximum relative errors `1.483e-14` and `4.542e-15`.

The checker terminates `QFORM_B08_R41_CHECK_PASS`. The numerical checks are regression evidence only; the main closure (4.3) is the exact analytic application above.
