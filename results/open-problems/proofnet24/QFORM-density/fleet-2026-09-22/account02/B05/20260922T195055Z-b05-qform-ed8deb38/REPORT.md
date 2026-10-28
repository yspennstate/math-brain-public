SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B05, 2026-09-22T19:50:55Z.
attacking: pay the aggregate hyperbolic-square coefficient from the three-large-eigenvalue hypothesis after disjoint-bank aggregation, before any reciprocal physical-pair/minor cost.

# Three-bank spectral payment for the aggregate hyperbolic-square normal form

Run: `20260922T195055Z-b05-qform-ed8deb38`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: account02/B05, Quadratic coarea bound.  
Classification: **ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET-VALID BRANCH CLOSED / FULL QFORM OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication attacked

The completed aggregate hyperbolic-square theorem had reduced a large product-preserving class to the parameter

`eta = |ab| ||d||_2^2 ||e||_2 ||c||_2`,

with density bound `8 eta^(-1/2)`, but its stated next step still asked a structural argument to extract the normal form **and** prove a dimension-free lower bound on `eta`.

This run pays the second half exactly. Once an exact rank-three target core has already been put in that disjoint-bank triangular normal form, the spectral hypothesis itself forces

`eta >= s^2`,

where `s` is the smallest absolute eigenvalue of the compressed three-dimensional core. Hence the full target normalization `s>=1` gives the universal bound

`||p_Q||_infinity <= 8`

for the whole three-bank normal-form class, regardless of how diffuse the three banks are. No physical coordinate minor is selected.

The remaining debt is therefore **normal-form extraction / treatment of the forbidden U^2 and UZ couplings**, not a separate quantitative lower bound on the aggregate coefficient after the normal form has been obtained.

## 2. Source-pinned inputs actually used

1. **Aggregate hyperbolic-square theorem.** The completed account04/B20 theorem `QFORM-AGGREGATE-HYPERBOLIC-SQUARE-v1`, source commit `1f85677029fc5ae27fc69b278620ae89d789efd2`, proves for three disjoint independent aggregate blocks

   `T=2aUV+alpha(w)U+H_w(V)+b(Z+theta_w(V))^2+G(w)`

   the cap-parametric estimate

   `||p_T||_infinity <= 4 M_Z sqrt(M_U M_V)/sqrt(|ab|)`.

   Inserting the sharp one-dimensional product-projection bound gives

   `||p_T||_infinity <= 8/[sqrt(|ab|) ||d||_2 sqrt(||e||_2||c||_2)] = 8 eta^(-1/2)`.

2. **Sharp projection input.** Account03/B02 records the Rogozin--Ball / Rudelson--Vershynin consequence: for independent cap-one coordinates and a nonzero coefficient vector `v`, the linear form has density cap at most `sqrt(2)/||v||_2`. Source-read at `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T130245Z-account03-B02-QFORM-r11/REPORT.md`.

3. **Named partner actually applied.** account03/B05 run `20260922T194010Z-account03-B05-QFORM-r16`, canonical report commit `d6312e9c0de9a774079895ee3c7aad7043015e49`, proved `QFORM-NEARZERO-MOVING-TRANSLATION-PAIR-REPAIR-v1` and independently passed the arbitrary-rank pair-log extension. Section 6 below applies its near-zero theorem to a genuinely diffuse-bank lift.

4. **Pair-log proof read in full.** `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

5. **Arbitrary-rank pair extension read in full.** `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`. The partner's current run independently reviewed its Sections 3--5 as PASS.

No refuted arbitrary-joint three-dimensional coarea estimate, conditional-projection positive moment, post-rotation independence, unrestricted curved-fiber supremum, or law-uniform pointwise Fresnel estimate is used.

## 3. New spectral-payment lemma

### Lemma `QFORM-TRIBANK-ARROWHEAD-INVERSE-PAYMENT-v1`

Let

`M = [[0,x,0], [x,z,w], [0,w,y]]`

be a real symmetric invertible `3x3` matrix. If every eigenvalue of `M` has absolute value at least `s>0`, then

`|x|>=s`, `|y|>=s`, and therefore `|xy|>=s^2`.

### Proof

Direct inversion gives

`det M = -x^2 y`

and

`M^(-1) = [[(w^2-yz)/(x^2y), 1/x, -w/(xy)],
            [1/x,                 0,          0],
            [-w/(xy),             0,        1/y]].`

Because `M` is symmetric and all its eigenvalues have modulus at least `s`,

`||M^(-1)||_op <= 1/s`.

Every matrix entry has absolute value at most the operator norm. In particular

`1/|x| = |(M^(-1))_12| <=1/s`,
`1/|y| = |(M^(-1))_33| <=1/s`.

Hence `|x|,|y|>=s`, and multiplication gives `|xy|>=s^2`. QED.

The point is that `z` and `w` may be arbitrarily large and may have either sign. The triangular shear does not erode the two aggregate coefficients relevant to the nonlinear density theorem.

## 4. Three-bank target theorem

### Theorem `QFORM-THREE-BANK-ARROWHEAD-SPECTRAL-CLOSURE-v1`

Let `I,J,K` be pairwise disjoint original-coordinate banks. Let

`U = e dot X_I`, `V = c dot X_J`, `Z = d dot X_K`,

where `e,c,d` are nonzero real coefficient vectors. The underlying coordinates are mutually independent and have densities bounded by one. Put

`E=||e||_2`, `C=||c||_2`, `D=||d||_2`.

Consider the quadratic core

`T = 2a U V + h V^2 + b (Z+qV)^2`,

with `a,b !=0` and arbitrary real `h,q`. In the orthonormal bank directions `e/E,c/C,d/D`, its nonzero quadratic matrix is

`M = [[0, x, 0],
      [x, z, w],
      [0, w, y]]`,

where

`x=aEC`, `y=bD^2`,
`z=(h+bq^2)C^2`, `w=bqCD`.

Assume the three eigenvalues of this compressed matrix have absolute value at least `s>0`. Then `T` has an essentially bounded density and

`boxed( ||p_T||_infinity <= 8/s ).`

If an arbitrary quadratic form `R` in a fourth disjoint original-coordinate bank is added with no cross couplings to `I union J union K`, then the same bound holds for `T+R`.

### Proof

The aggregate theorem applies directly because the three banks are genuinely independent. Its projection insertion gives

`||p_T||_infinity
 <= 8/[sqrt(|ab|) D sqrt(EC)]`.

Define

`eta = |ab| D^2 E C`.

By the displayed bank matrix,

`eta = |(aEC)(bD^2)| = |xy|`.

The preceding inverse-payment lemma gives `eta>=s^2`. Thus

`||p_T||_infinity <= 8 eta^(-1/2) <=8/s`.

For an independent direct-sum remainder `R`, the law of `T+R` is the convolution of the bounded density of `T` with the probability law of `R`; convolution with a probability measure cannot increase the `L^infinity` norm. QED.

### Target corollary

If the compressed core itself supplies three target eigenvalues, so `s>=1`, then

`boxed( ||p_T||_infinity <=8 ).`

Thus, within the full disjoint-bank hyperbolic-square normal form, **the spectral hypothesis automatically pays the aggregate coefficient**. No additional determinant/minor lower bound is needed.

## 5. Fully diffuse exact-target stress family

For every `m>=1`, take three disjoint banks of `m` coordinates each and set

`U_m=m^(-1/2) sum_(i=1)^m X_i`,
`V_m=m^(-1/2) sum_(j=1)^m Y_j`,
`Z_m=m^(-1/2) sum_(k=1)^m Z_k`.

Let

`Q_m = 2 U_m V_m + Z_m^2`.

On the three normalized bank directions its nonzero matrix is

`[[0,1,0],[1,0,0],[0,0,1]]`,

so its nonzero spectrum is exactly `{1,-1,1}`. Hence every `Q_m` is an exact target instance and the theorem gives

`||p_(Q_m)||_infinity <=8`

for arbitrary independent input densities bounded by one, uniformly in `m`.

Yet all useful physical coefficients are diffuse: each I--J entry is `1/m`, and every principal triple containing one coordinate from each bank has determinant `-1/m^3`. There are `m^3` such triples, so

`sum_(i,j,k) |det A[{i,j,k}]| = 1`

while every individual determinant tends to zero. This is a source-valid target witness against paying a reciprocal of one selected physical triple before aggregation. The correct currency is the aggregate bank product `eta=1`.

This family is more symmetric than the earlier singleton-plus-two-banks stress test: all three active spectral directions may be arbitrarily diffuse.

## 6. Named partner application: diffuse lift of the near-zero repair

The current account03/B05 partner theorem treats

`A_a=[[a,sqrt(1+a),0],[sqrt(1+a),0,0],[0,0,1]]`, `0<a<=1/3`,

and proves

`||p||_infinity <=8*2^(1/4)(1+a)^(-1/4)<9.514`.

It extends immediately, without any post-rotation independence, to a diffuse original-coordinate bank. Let `H,W` be two original scalar coordinates and let

`L = sum_j b_j Y_j`, `beta=||b||_2=sqrt(2(1+a))`,

with the leaf bank disjoint from `H,W`. By the sharp projection theorem,

`Z=(sqrt(2)/beta)L`

has density cap at most one and is independent of `H,W`. Since

`L=(beta/sqrt(2))Z=sqrt(1+a) Z`,

the diffuse form

`W^2 + a H^2 + 2HL`

has exactly the partner's three-variable law after this bank compression. Therefore the partner theorem gives the same uniform `<9.514` bound for arbitrary cardinality and arbitrary admissible laws in the leaf bank.

For equal leaf coefficients and `a=1/m`, every individual hub--leaf indefinite pair becomes poorly conditioned as `m` grows, while this aggregate partner bound remains uniform. This is an actual use of the named partner result, not merely a citation.

The aggregate hyperbolic-square theorem is stronger on this no-leakage subfamily (it gives `4(1+a)^(-1/4)` because `H,W` are singleton cap-one variables), but the partner proof is an independent pair-coarea confirmation that the near-zero scalar-pivot divergence is an artifact of paying before aggregation.

## 7. Exact missing factor after this run

The run removes one quantitative debt:

`OLD: extract disjoint hyperbolic-square banks AND prove eta bounded below.`

becomes

`NEW: extract the disjoint hyperbolic-square bank normal form; eta is then paid automatically by the three-eigenvalue spectral scale.`

The first genuinely unpaid implication for B05 is therefore

`QFORM-TRIBANK-NORMAL-FORM-EXTRACTION-OR-LEAKAGE-v1`:

> Starting from an arbitrary symmetric target matrix with `s_3(A)>=1`, either produce disjoint original-coordinate aggregate banks whose conditioned quadratic core has no `U^2` or `UZ` term and whose three-dimensional compressed core carries the active three-eigenvalue scale, or control those forbidden couplings by a dependence-safe curved/coarea estimate **before** any reciprocal local minor is paid.

The remaining obstruction is precisely leaf-bank leakage/overlap. A bounded marginal density for one aggregate is not enough once the residual quadratic depends on the same bank; this run does not replace that dependence by an unrestricted fiber supremum.

## 8. Corrections respected

The proof does not use:

- the refuted law-uniform pointwise oscillatory decay route;
- the refuted arbitrary-joint rank-three coarea inequality;
- the refuted conditional projection-cap or positive conditional-moment interfaces;
- post-rotation independence;
- a selected uniformly conditioned physical pair or principal triple;
- bounded support, moments, log-concavity, or a diagonal basis;
- an unrestricted curved-fiber supremum.

The fresh correction inbox was re-read at `yspennstate/math-research-brain@ac3ce51d3d8bf01b7e906c0fe41dcb7f5bb94646`, blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`, before publication.

## 9. Exact check used

`CHECK.py` symbolically verifies

`det M=-x^2y`, `(M^-1)_12=1/x`, `(M^-1)_33=1/y`,

and prints numerical stress-family / partner constants. Its output terminates with

`QFORM_B05_TRIBANK_CHECK ... PASS`.

The computation is supporting algebra only; the proof above is uniform and does not rely on finite enumeration.

## 10. Status

**ESSENTIAL_STEP_APPLIED.** The full QFORM conjecture remains **OPEN**. The new theorem closes the exact-rank-three disjoint-bank arrowhead/hyperbolic-square normal form with universal constant `8` and shows that, after this normal form is present, the aggregate coefficient lower bound follows from the spectral hypothesis automatically. The unresolved work is the global product-preserving extraction / overlap-leakage step.
