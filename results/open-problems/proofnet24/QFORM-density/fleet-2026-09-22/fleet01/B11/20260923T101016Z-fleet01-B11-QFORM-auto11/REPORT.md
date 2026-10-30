SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T10:10:16Z.
attacking: overlap-safe third-square smoothing for an indefinite physical pair via the exact pair-log envelope and a sharp square small-ball bound.

# fleet01/B11 — overlap-safe square smoothing of an indefinite physical pair

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T101016Z-fleet01-B11-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** only essential boundedness is proved by the new theorem.

## 1. Exact scope and source boundary

The owner target remains the unrestricted statement for arbitrary independent real coordinates with density caps one and arbitrary symmetric `A` having at least three eigenvalues of modulus at least one. The present result does not solve the structural extraction problem and does not treat arbitrary extra nonseparable spectrum. It pays a specific issue left open in the preceding B11 run and in the designated partner's latest run: the third square may be entangled with the *translations* of an indefinite physical pair, so one cannot regard the receiver and the square as independent after completing the pair.

The argument uses two completed inputs at their exact scopes.

1. **Pair-log theorem.** `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, path `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`. If an invertible indefinite original-coordinate pair has `D=|det B|`, `kappa=sigma_min(B)`, and after completing the pair the remainder `R(Z)` obeys

   `sup_t P(|R-t|<rho) <= H sqrt(rho)`,

   then, even when the two pair translations depend arbitrarily on `Z`,

   `||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.       (1.1)

   The proof retains the pair's logarithmic critical-value singularity and averages it by layer cake. It does not replace a conditional density cap by independence.

2. **Designated partner fleet02/B11.** `yspennstate/math-open-problems@f2835c54b9f384f8f83e34c46bef5c40953e32a7`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260923T042112Z-fleet02-B11-QFORM-2f47d35a/REPORT.md`. Its theorem `QFORM-INDEFINITE-PAIR-DIFFUSE-SQUARE-v1` gives, when the square bank is genuinely separated from a fixed pair receiver,

   `||p_Q||_infinity <= 16 sqrt(30) L |det B|^(-1/4)|d|^(-1/2)`,

   and for a normalized disjoint product-bank projection, `L<=sqrt(2)` and the constant is `16 sqrt(60)`. Its source package also records the sharp projection-density cap `sqrt(2)` used below.

The live corrections consumed include the failures of post-rotation independence, conditional-cap-as-independence, one-local-triple reciprocal-minor extraction, and the local-cross-rank-three dichotomy. No such step is used here.

## 2. Sharp small-ball estimate for a translated square

### Lemma 2.1 — square small ball

Let `W` be real with density bounded by `L`, let `a,c` be real and `d!=0`. Put

`R=d(W-a)^2+c`.

Then for every `rho>0`,

`boxed:
 sup_t P(|R-t|<rho)
 <= min(1, 2 sqrt(2) L sqrt(rho/|d|)).`                    (2.1)

### Proof

Set `eta=rho/|d|`. Translation and reflection reduce the preimage question to the Lebesgue length of

`E_y={x: |x^2-y|<eta}`.

If `y+eta<=0` the set is empty. If `-eta<y<eta`, then

`|E_y|=2 sqrt(y+eta) <=2 sqrt(2 eta)`.

If `y>=eta`, then

`|E_y|=2( sqrt(y+eta)-sqrt(y-eta) )`.

The last expression is decreasing in `y` on `[eta,infinity)` and equals `2sqrt(2eta)` at `y=eta`. Hence

`sup_y |E_y| = 2 sqrt(2 eta)`.

Multiplying by the density cap `L` proves (2.1). QED.

This estimate uses no moment, support, unimodality, or connected-support assumption.

## 3. Main theorem: overlap-safe square-log smoothing

### Theorem 3.1 — `QFORM-OVERLAP-SAFE-SQUARE-LOG-v1`

Let `Y=(X_1,X_2)` consist of two independent cap-one original coordinates. Let `Z` be the vector of all remaining original coordinates, independent of `Y`. Let `B` be an invertible indefinite symmetric `2x2` matrix, with

`D=|det B|`, `kappa=sigma_min(B)`.

Let `m(Z)` be an arbitrary measurable `R^2`-valued function. Let `W=W(Z)` be any scalar statistic whose **marginal** density is bounded by `L`; `W` may be arbitrarily dependent on every other statistic of `Z` and on `m(Z)`. For `d!=0` and arbitrary constants `a,c`, define

`Q=(Y+m(Z))^T B (Y+m(Z)) + d(W-a)^2+c`.                    (3.1)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 8*2^(1/4) L^(1/2) (D kappa |d|)^(-1/4).`               (3.2)

If `W` is a normalized linear projection of the product coordinates in `Z`, the sharp product-marginal estimate gives `L<=sqrt(2)`, hence

`boxed:
 ||p_Q||_infinity
 <= 8 sqrt(2) (D kappa |d|)^(-1/4).`                       (3.3)

### Proof

The pair-log theorem (1.1) was designed precisely for the dependence pattern in (3.1): the pair variables `Y` are independent of `Z`, but the completed-pair translation `m(Z)` may depend arbitrarily on the same `Z` that generates the remainder. Thus we need only verify its one-dimensional small-ball hypothesis for

`R(Z)=d(W(Z)-a)^2+c`.

Lemma 2.1 gives

`sup_t P(|R-t|<rho) <= H sqrt(rho),`

with

`H=2 sqrt(2) L |d|^(-1/2)`.                                  (3.4)

Substituting (3.4) into (1.1),

`4 sqrt(2H)
 =4 sqrt(4 sqrt(2) L |d|^(-1/2))
 =8*2^(1/4)L^(1/2)|d|^(-1/4).`

This is (3.2). If `L<=sqrt(2)`, then `2^(1/4)L^(1/2)<=sqrt(2)`, proving (3.3). QED.

### Why this is genuinely overlap-safe

The theorem does **not** condition on `W` and then claim that the translated pair is independent of `W`. Instead, for fixed `Z` the pair remains a product law with deterministic translations, and the pair-log envelope has a critical value that depends only on the Schur remainder. The layer-cake average then uses only the unconditional small-ball estimate (2.1). Thus arbitrary dependence between `m(Z)` and `W(Z)` is harmless.

## 4. Exact-rank-three indefinite corollary

### Corollary 4.1 — `QFORM-RANK3-INDEFINITE-PAIR-HOMOGENEOUS-v1`

Let `A` have exact rank three and let its three nonzero eigenvalues have absolute value at least `s>0`. Suppose two ORIGINAL coordinates form an invertible indefinite principal pair `B`, with `D=|det B|` and `kappa=sigma_min(B)`. Then for arbitrary independent cap-one inputs,

`boxed:
 ||p_(X^T A X)||_infinity
 <= 8 sqrt(2) (D kappa s)^(-1/4).`                           (4.1)

This applies to both signatures `(2,1)` and `(1,2)`.

### Proof

Write the selected pair first:

`A=[[B,C],[C^T,D_0]]`.

Completing the pair in the original coordinates gives the exact identity

`X^TAX
 =(Y+B^(-1)CZ)^T B (Y+B^(-1)CZ)
  + Z^T (D_0-C^T B^(-1)C) Z`.                              (4.2)

The exact-rank-three Schur calculation in the pair-log source shows

`D_0-C^T B^(-1)C = lambda h h^T`,                           (4.3)

where `||h||_2=1` and

`|lambda|>=s`.                                               (4.4)

Set `W=h^T Z`. Since `h` is a unit vector supported on original coordinates disjoint from the pair, the sharp one-dimensional product-projection theorem gives

`||p_W||_infinity<=sqrt(2)`.                                (4.5)

Apply Theorem 3.1 with `m(Z)=B^(-1)CZ`, `d=lambda`, `a=0`. Equations (4.4)-(4.5) yield (4.1). QED.

The important structural point is that `B^(-1)CZ` may depend strongly on the same coordinates that generate `W`. The proof never requires these statistics to be independent. In spectral language the third direction can overlap the pair; after the legitimate original-coordinate Schur completion, the overlap survives exactly as a correlated translation of the pair.

Compared with the generic affine rank-one remainder estimate in the pair-log source, (4.1) improves the homogeneous exact-rank-three constant from `8sqrt(5)` to `8sqrt(2)` in the same `D*kappa*s` scale. More importantly for B11, it makes explicit that **overlap itself is not the remaining obstruction once a quantitatively good indefinite physical pair has been found**.

## 5. Required partner application to an actual inequality

Use the designated partner's exact target family

`B_epsilon=[[epsilon,sqrt(1+epsilon^2)],
            [sqrt(1+epsilon^2),-epsilon]]`,

`W_m=m^(-1/2) sum_(j=1)^m X_(j+2)`,

`A_(m,epsilon)=B_epsilon direct_sum (b_m b_m^T)`.

The nonzero spectrum is

`{-sqrt(1+2epsilon^2), 1, sqrt(1+2epsilon^2)}`,

so this is an exact target family for every `m>=1`, `epsilon>=0`. Put

`D=|det B_epsilon|=1+2epsilon^2`,
`kappa=sigma_min(B_epsilon)=sqrt(1+2epsilon^2)`.

The completed **fleet02/B11** theorem applied at its exact scope gives

`boxed:
 ||p_Q||_infinity
 <=16 sqrt(60) (1+2epsilon^2)^(-1/4)
 <=16 sqrt(60)
 =123.9354670786... .`                                       (5.1)

Applying the new overlap-safe theorem to the same family gives the sharper inequality

`boxed:
 ||p_Q||_infinity
 <=8 sqrt(2) (1+2epsilon^2)^(-3/8)
 <=8 sqrt(2)
 =11.31370849899... .`                                       (5.2)

The point of (5.1) is not the numerical constant: it is an actual use of the designated partner theorem and confirms the aggregate-before-inversion behavior. Equation (5.2) shows that, once the pair-log critical-value structure is exploited, the same family can be paid through the square's `1/2`-small-ball exponent without conditioning away the pair translation.

## 6. The rank-two logarithm is still real

At the endpoint `epsilon=0` and singleton first two coordinates, take independent

`X_1,X_2 ~ Uniform[-1/2,1/2]`.

Then the pair term is

`P=2X_1X_2`

and, for `0<|t|<1/2`,

`p_P(t)=log(1/(2|t|))`.                                      (6.1)

Thus rank two remains genuinely singular. What the third direction supplies is not a bounded pair density. It supplies a remainder `R=d(W-a)^2+c` with

`P(|R-t|<rho)=O(sqrt(rho))`.                                 (6.2)

The pair-log envelope has the form `log_+(A/|t-R|)`. Layer cake converts (6.2) into

`E log_+(A/|t-R|)
 = integral_0^infinity P(|t-R|<A exp(-v)) dv
 <= 2H sqrt(A)`,                                             (6.3)

which is finite. This is a precise sign-specific explanation of how the third direction removes the rank-two logarithmic singularity.

## 7. What remains unpaid

The full conjecture is still open. The new result removes one ambiguity from the previous B11 handoff: the same-bank/transverse **dependence of the pair translation on the third square statistic is not itself fatal** in exact rank three. Once a quantitatively good indefinite physical pair exists, the Schur square plus (2.1) pays it.

The first B11 debt is therefore sharpened to

**`QFORM-INDEFINITE-PAIR-OR-AGGREGATE-EXTRACTION-v1`.** From a general exact-rank-three Parseval frame with signatures `(2,1)` or `(1,2)`, either force an original-coordinate indefinite pair with `D*kappa` bounded below by a universal constant, or aggregate disjoint original-coordinate banks before reciprocal-minor payment and reduce to an already-paid three-bank/ridge/volume/null-ray branch. The family `[1] direct_sum J_m/m direct_sum (-J_m/m)` shows that one cannot demand a uniformly good physical pair. Arbitrary extra nonseparable spectrum remains a separate interface to the full target.

No continuity conclusion is obtained here. A full target candidate would still need all higher-rank tails and two independent end-to-end reviews.

## 8. Verification

`VERIFY.py` and `VERIFY_OUTPUT.txt` in this directory check the constants, the partner family determinant/eigenvalue formulas, and the sharp square-preimage length formula. The captured execution ends

`QFORM_B11_OVERLAP_SQUARE_LOG_CHECK_PASS`.

The checker is regression evidence only; the universal inequalities are proved analytically above.
