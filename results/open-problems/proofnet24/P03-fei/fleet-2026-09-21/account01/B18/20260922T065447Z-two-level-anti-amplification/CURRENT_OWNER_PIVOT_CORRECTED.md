# B18 current-owner pivot — corrected source-bound statement

**Primary classification:** `CANDIDATE_REFUTED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The fresh OWNER MESSAGE is later and narrower than the older selector subroute. Its operative current question for the read-once base potential is whether the gate requiring the largest quadratic correction is decomposable/AND, or whether a genuine gate asks for more. The latter has already been proved by an exact other-account artifact, so this run applies that falsifier instead of continuing to optimize the failed fixed candidate.

## 1. Actual sign of the gate margin

The gate reformulation uses

D_Gamma(G;p) = RHS(G;p) - LHS(G;p).

For

Gamma_c(z) = Gamma_0(z) + c z(1-z),

the defect changes by

D_{Gamma_c}(G;p) = D_{Gamma_0}(G;p) + c W_G(p),

where

W_G(p) = I(G;p)/4 - p_out(1-p_out) >= 0.

Thus for W_G>0 the correction requested by a gate is

c_G(p) = -D_{Gamma_0}(G;p)/W_G(p).

A common correction is safe only when c >= c_G(p) for every gate and bias vector. Therefore the binding gate **maximizes** c_G. The phrase “minimum of c_G” in the owner prose is a sign/wording slip relative to the displayed source convention and to the accompanying statement that previously tested genuine gates asked for less.

## 2. Exact composition-prime counterexample

Consumed and applied exactly:

- account04/B14, `20260922T003849Z-prime-gate-falsifier/REPORT.md`, blob `43ad8483eb8a56cb7141a33821ab89e4119dbc49`, which proves Numaro’s balanced 18-input gate is composition-prime by rejecting all 262124 proper decomposition blocks with the ANF rank-one criterion;
- account03/B12, `20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`, blob `36fea824c2dcae8c65c3d485e5d5714899699855`, which evaluates that exact prime gate at

p_1 = 3/8,   p_2 = ... = p_18 = 1/2,   p_out = 967/2048.

For this witness,

W = 1078193/4194304 > 0.

For the fixed source-exact candidate

Gamma^dagger = Gamma_0 + 0.268204856 p(1-p),

the certified defect is

D_{Gamma^dagger}(G;p)
= -0.0176114199558017537894958865691... < 0.

Hence the current fixed candidate is refuted on a **composition-prime** gate.

Since the defect is affine in the quadratic coefficient, the requested margin relative to the base Gamma_0 is

c_G
= 0.268204856 - D_{Gamma^dagger}/W
= 0.3367154558335169298319482272843... .

Even the coarse certified inequality D_{Gamma^dagger} < -0.017611 gives

c_G > 0.336713822153555... .

The current AND/read-once correction floor recorded in the owner source is about 0.0043974. Thus this prime gate asks for roughly 76.6 times that correction. The intended AND/decomposable-extremality statement for this base potential is decisively false.

## 3. Exact affine repair constraint

Let a replacement be

Gamma = Gamma^dagger + eta.

At the same exact prime witness, the change in defect is

L(eta)
= (57/256) eta(3/8)
  + (465/256) eta(1/2)
  - eta(967/2048).

Therefore every replacement potential that repairs this witness must satisfy

L(eta)
>= 0.0176114199558017537894958865691... .

This is the first source-bound constraint that should be imposed on any replacement potential. It explains why merely increasing the old quadratic lift is inefficient: with eta(z)=delta_c z(1-z), the same witness forces the total quadratic coefficient above 0.3367154, hence a center above 6.53897885 if Gamma_0 is kept.

For calibration only, if the other two sampled values were frozen:

- changing only the output value would require eta(967/2048) <= -0.0176114199558...;
- changing only the center would require eta(1/2) >= 0.00969574948104...;
- changing only eta(3/8) would require eta(3/8) >= 0.0790969036611... .

These are local necessary calibrations, not constructions; a valid Gamma must still satisfy all AND/read-once and all other gate inequalities.

## 4. Status of the earlier B18 selector calculation

`REPORT.md` and `PATH_EXTENSION.md` in this same run root remain valid **conditional calculations for the now-refuted Gamma^dagger candidate**. They are preserved for possible reuse in a future potential with the same local posterior-credit profile, but they are not counted as current target-level convergence after the exact prime-gate refutation.

## 5. Old/new implication

**Old candidate:** the current read-once base potential, or its 0.268204856 p(1-p) lift, has its largest requested correction at a decomposable/AND gate and survives every composition-prime gate/bias point.

**Result:** `CANDIDATE_REFUTED` by the exact 18-input prime gate above, with c_G = 0.3367154558... and strictly negative fixed-candidate defect.

**New missing implication:** construct a different symmetric nonnegative finite-cap potential satisfying the all-gate inequality, with the affine prime-witness constraint above imposed from the outset while retaining the proved two-input/read-once inequalities. A useful next object is a source-valid prime-gate envelope operator whose fixed point is tested first on this exact 18-input gate and its one-coordinate bias line.

No replacement potential is proved here. Full FEI remains **OPEN / NOT PROVED**.
