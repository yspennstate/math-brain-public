# fleet02/B11 — heavy-Walsh indefinite smoothing and a principal-chart obstruction

Run: `20260922T125048Z-b11-qform-c9a4e7d2`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: **Indefinite signatures**  
Status: **ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM + STRATEGY REFUTATION / FULL CONJECTURE OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and first unpaid implication

The full target remains: for arbitrary independent real coordinates with marginal densities at most one and arbitrary symmetric `A` with at least three eigenvalues of magnitude at least one, prove one universal bound on the density of `X^T A X`, or give a valid counterexample.

The first unpaid implication at the beginning of this run was the global one left by the completed partner theorem: local determinant/pivot estimates for an indefinite physical `3 x 3` block must be converted into a dimension-free mechanism without selecting one coordinate triple whose determinant vanishes in diffuse frames.

This report does two things on that boundary.

1. It proves a genuinely rotated exact-rank-three `(+,+,-)` / `(+,-,-)` family with a universal density bound even though the third spectral direction overlaps the same original coordinates as the opposite-sign pair.
2. On the *same family*, every physical principal-triple determinant/pivot certificate tends to zero as the dimension grows. Hence a best-principal-triple use of the partner's local theorem cannot be the global assembly mechanism.

The proof keeps original-coordinate independence. It does not diagonalize the law, use law-uniform pointwise Fresnel decay, use a generic fiber supremum, or condition on a conjugate sum/difference and pretend the conditional density cap is preserved.

## 2. Sources actually applied

### Assigned partner: fleet03/B11

Canonical partner report:

`yspennstate/math-open-problems@860d849b7f2e0198bf7c3531a71b14e59f03e430`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260922T121353Z-fleet03-B11-QFORM-r11/REPORT.md`

The partner proves for every independent density-`<=1` pair and every indefinite binary quadratic with discriminant `Delta>0` the two one-sided half-potential bounds

`sup_t E[(t-R)_+^(-1/2)] <= 8 Delta^(-1/4)`,  
`sup_t E[(R-t)_+^(-1/2)] <= 8 Delta^(-1/4)`.

On the pure saddle `R=UV` it records the sharper saddle-axis constant `4 sqrt(2)` for density-capped-one inputs. It also proves the dependence-safe Abel smoothing lemma: if the conditional law of `V` given a base variable `R` is a mixture of translations of a density capped by one, then adding `a V^2` costs exactly the matching half-order potential and does **not** require independence after square completion.

### Diffuse rank-one projection estimate used as a sublemma

fleet01/B08 canonical report:

`yspennstate/math-open-problems@fce159beaecf924a3e500dc7865ae61f8b35c932`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260922T114116Z-fleet01-B08-qform-r11/REPORT.md`

Its Fourier--Brascamp--Lieb calculation through equation (3.3) works already in rank one: if `L=sum a_i X_i`, `sum a_i^2=1`, `max_i a_i^2<=1/2`, and all marginal densities are `<=1`, then `L` has a bounded continuous density with

`||p_L||_infinity <= sqrt(e)`.

Indeed the report gives `||hat mu||_1 <= 2 pi e^(1/2)` for rank one, and Fourier inversion yields the displayed cap.

### Corrections consumed

Fresh correction inbox included `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, and the new `QFORM-UV-CONDITIONAL-CAP-FALSE`. The theorem below avoids the last error because its two null factors are functions of **disjoint original coordinate sets** and therefore genuinely independent; no conditional density cap for a conjugate variable is asserted.

## 3. The heavy-Walsh rotated family

Fix an integer `m>=4` divisible by four and `c in [1/2,1)`. Choose three vectors

`v_0,v_1,v_2 in {+1/sqrt(m),-1/sqrt(m)}^m`

that are orthonormal. For example, three Walsh columns suffice. Define an `(m+1) x 3` matrix `U` by

- heavy row `u_0=(sqrt(c),0,0)`;
- for `1<=i<=m`,
  `u_i=(sqrt(1-c) v_0(i), v_1(i), v_2(i))`.

Then `U^T U=I_3`. Let

`Lambda=diag(1,1,-1)`, `A=U Lambda U^T`.

Thus `A` has exactly three nonzero eigenvalues `1,1,-1`, so it meets the owner's three-large-eigenvalue threshold exactly. The dual form `-A` gives signature `(+,-,-)`.

For independent coordinates `X_0,X_1,...,X_m` with densities at most one, put

`L_j=sum_{i=1}^m v_j(i) X_i`, `j=0,1,2`.

Then

`Q=X^T A X`

has the exact representation

`Q = (sqrt(c) X_0 + sqrt(1-c) L_0)^2 + L_1^2 - L_2^2`.      (3.1)

For `c<1`, all three spectral directions overlap every one of the `m` non-heavy physical coordinates. This is not a diagonal-coordinate instance.

## 4. The opposite-sign pair factors into two genuinely independent null factors

Because `v_1(i),v_2(i)` are equal-magnitude signs and `v_1 dot v_2=0`, exactly `m/2` rows satisfy `v_1(i)=v_2(i)` and exactly `m/2` satisfy `v_1(i)=-v_2(i)`.

Define

`P=L_1+L_2`, `N=L_1-L_2`.

Then

`R:=L_1^2-L_2^2=P N`.                                      (4.1)

Moreover `P` depends only on the coordinates in the equal-sign half and `N` only on the coordinates in the opposite-sign half. These two original coordinate sets are disjoint, hence `P` and `N` are genuinely independent.

Each nonzero coefficient of `P` or `N` has magnitude `2/sqrt(m)`. Therefore `P/sqrt(2)` and `N/sqrt(2)` are normalized linear forms with row leverage `2/m<=1/2`. Applying the rank-one specialization of the fleet01/B08 Fourier--Brascamp--Lieb estimate,

`||p_{P/sqrt(2)}||_infinity, ||p_{N/sqrt(2)}||_infinity <= sqrt(e)`.

Scaling back,

`||p_P||_infinity, ||p_N||_infinity <= M:=sqrt(e/2)`.        (4.2)

Rescale `P~=M P`, `N~=M N`. Their densities are at most one and

`R = M^(-2) P~ N~`.

For density-capped-one variables the partner's saddle-axis proof gives both one-sided half-potentials of the product `P~N~` at most `4 sqrt(2)`. Half-potentials scale with output dilation to the power `-1/2`, so from `M=sqrt(e/2)` we obtain

`sup_t E[(t-R)_+^(-1/2)] <= 4 sqrt(e)`,                    (4.3)

`sup_t E[(R-t)_+^(-1/2)] <= 4 sqrt(e)`.                    (4.4)

This is the exact retained control of the rank-two logarithmic regime.

## 5. The third direction removes the logarithmic singularity despite dependence

Rewrite the first term in (3.1) as

`c V^2`, where

`V=X_0 + sqrt((1-c)/c) L_0`.

The base `R=L_1^2-L_2^2` and the translation term `L_0` can be highly dependent because they use the same `m` original coordinates. That dependence is harmless here.

Condition on `R=r`. Since `X_0` is independent of all the other coordinates, the conditional law of `V` is a mixture of translations of the original density of `X_0`. Therefore, for almost every `r`, the conditional density of `V` is still bounded by one. This is exactly the dependence-safe hypothesis proved and used in the partner report.

Apply its Abel smoothing lemma to

`Q=R+cV^2`.

Using (4.3),

`||p_Q||_infinity <= c^(-1/2) 4 sqrt(e)`.

Since `c>=1/2`,

`boxed( ||p_Q||_infinity <= 4 sqrt(2e) < 9.327. )`           (5.1)

Reflection gives the identical statement for `-Q`, hence for the dual signature `(+,-,-)`.

### Theorem 5.1 — `QFORM-HEAVY-WALSH-INDEFINITE-v1`

For every `m>=4` divisible by four, every `c in [1/2,1)`, every Walsh triple as above, and every independent input law with marginal densities at most one, the exact-rank-three form `A=U diag(1,1,-1) U^T` has an essentially bounded density satisfying (5.1). The same bound holds for `-A`.

The mechanism is explicit: the opposite-sign rank-two piece is not made bounded; it is controlled by a half-order potential, and the third square contributes precisely the Abel kernel that consumes that potential. The first spectral coordinate may overlap all coordinates of the rank-two pair; conditional translation of the independent heavy physical coordinate preserves the density cap needed for smoothing.

## 6. Rank-two logarithmic control is genuinely present

Delete the third square and keep only

`R=L_1^2-L_2^2=P N`.

Take all original coordinates uniform on `[-1/2,1/2]`. Then `P` and `N` are independent symmetric sums of at least two bounded intervals, so their densities are continuous and strictly positive in a neighborhood of zero. Choose `delta>0` and `a,b>0` such that

`p_P(u)>=a`, `p_N(v)>=b` whenever `|u|,|v|<=delta`.

The product density satisfies, for `0<|t|<delta^2`,

`p_R(t)=integral p_P(u) p_N(t/u) du/|u|`

`>= 2ab integral_{|t|/delta}^{delta} du/u`

`= 2ab log(delta^2/|t|)`.

Hence `p_R(t)->infinity` logarithmically as `t->0`. The third direction in Theorem 5.1 therefore removes a real opposite-sign rank-two singularity rather than smoothing an already bounded base.

## 7. Same-family obstruction to best-principal-triple assembly

The partner's local physical-triple theorem for a nonzero scalar pivot uses the scale

`w(I,k) = |A_kk det A[I,I]|^(1/4)`

for a three-coordinate set `I` and `k in I`. A universal global proof by selecting one principal triple would require some such weight bounded below by a universal positive constant.

This family disproves that requirement.

Because `A=U Lambda U^T` has exact rank three,

`det A[I,I] = det(Lambda) det(U_I)^2 = -det(U_I)^2`.          (7.1)

The diagonal entries are

`A_00=c`,

`A_ii=(1-c)/m` for every `1<=i<=m`.                           (7.2)

### Triples containing the heavy coordinate

If `I={0,i,j}`, expansion along the heavy row gives

`|det U_I| <= 2 sqrt(c)/m`,

because the remaining `2 x 2` sign determinant is `0` or `2/m`. Hence

`|det A[I,I]| <= 4c/m^2`.                                    (7.3)

For the heavy pivot,

`w(I,0) <= sqrt(2c) m^(-1/2)`.                               (7.4)

For either non-heavy pivot,

`w(I,i) <= [4c(1-c)]^(1/4) m^(-3/4)`.                        (7.5)

### Triples entirely in the diffuse block

For `I subset {1,...,m}`, each row of `U_I` is

`m^(-1/2) (sqrt(1-c) eps_0, eps_1, eps_2)`

with signs `eps_j in {+1,-1}`. The determinant of a `3 x 3` sign matrix has absolute value at most four, so

`|det U_I| <= 4 sqrt(1-c) m^(-3/2)`,

`|det A[I,I]| <= 16(1-c)m^(-3)`.                             (7.6)

Using (7.2),

`w(I,k) <= 2 sqrt(1-c) m^(-1)`.                              (7.7)

Therefore, for every fixed `c in [1/2,1)`,

`max_{|I|=3,k in I} w(I,k) -> 0` as `m->infinity`.           (7.8)

So neither the partner's determinant-pivot bound nor the minority-sign Schur-pivot bound can be assembled globally merely by choosing the best physical principal triple. The target form itself stays uniformly bounded by (5.1). This is a source-valid counterexample to the **selection mechanism**, not to the QFORM conjecture.

The same determinant decay also forces the smallest singular value of every fixed principal triple to vanish along the family, consistent with the earlier flat-frame obstruction to the general `C/sigma_min` local theorem.

## 8. Exact symbolic sanity check

For `m=8`, `c=3/4`, the accompanying exact checker constructs Walsh signs and verifies

- `U^T U=I_3`;
- `rank(A)=3`;
- spectrum `1,1,-1,0,...,0`;
- diagonal entries `3/4,1/32,...,1/32`;
- maximum absolute principal `3 x 3` determinant `3/64`;
- maximum pivot weight exactly `sqrt(3)/4`, equal to the bound `sqrt(2c)/sqrt(m)`.

This computation is a check of the algebraic family, not a finite-census proof of any arbitrary-dimensional statement.

## 9. What changed and what remains

**Applied:** the assigned fleet03/B11 half-potential theorem is used in the central inequality (4.3), not merely cited. The dependence-safe square-smoothing step is also applied with the overlapping third spectral direction.

**New positive result:** the heavy-Walsh rotated indefinite family has the universal bound `4 sqrt(2e)` for both signatures.

**New negative result:** the same family makes every best-principal-triple determinant/pivot certificate vanish, even though the global density remains uniformly bounded.

**First unpaid implication now:** replace principal-triple selection by a genuinely aggregated heavy/diffuse mechanism. In this family the right aggregation is visible because the two null factors of the opposite-sign plane split into disjoint original-coordinate sets. The next structural question is whether an arbitrary heavy-row exact-rank-three frame admits either (i) a comparable null-factor decomposition with quantitatively controlled product-projection densities, or (ii) a diffuse Brascamp--Lieb chart after removing the heavy coordinate. For arbitrary full-rank `A`, the additional nonseparable spectral complement remains a separate debt.

Full QFORM remains OPEN / NOT PROVED.
