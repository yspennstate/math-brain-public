SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B13, 2026-09-22T18:21:58Z.
attacking: an exhaustive heavy/light original-coordinate reduction for exact rank three, after the exact extreme-product reduction.

# fleet02/B13 — heavy/light rank-three reduction with explicit paid branches

**Run:** `20260922T182158Z-fleet02-B13-qform-4ebdd821`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Extremal product laws  
**Classification:** `PROVED_SUPPORTING_REDUCTION / TWO-OF-THREE-RANK3-GRAM-REGIMES-PAID / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full quadratic-form density conjecture remains **OPEN / NOT PROVED**. This report keeps the exact cap-one-to-product-indicator reduction already proved by this slot as the front end, and attacks the first unpaid geometric implication from the previous run: aggregate local curvature/determinant currency before taking a reciprocal. The new result is a quantitative heavy/light Gram trichotomy for the exact-rank-three spectral frame. Two of the three regimes are paid with universal constants using existing product-preserving theorems. The only exact-rank-three regime left by this reduction is a one-heavy-direction / two-diffuse-plane mixed configuration.

No interval, centered-uniform, compact-support, moment, bounded-diameter, bounded-fragment, or post-rotation independence hypothesis is introduced.

## 1. Fresh controls, corrections, and sources actually used


The live correction inbox was reread before publication. In particular, this report does **not** use the refuted arbitrary-joint rank-three coarea inequality, the divergent positive conditional-projection-moment bridge, law-uniform pointwise Fresnel decay, post-rotation independence, a universal good fixed minor, bounded-diameter localization, or bounded fragment count.

Mathematical inputs used at their stated scopes are:

1. **Exact extreme-product reduction**, fleet02/B13, `yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T115714Z-fleet02-B13-qform-480ba28b/REPORT.md`. For every fixed slab kernel, the supremum over independent densities `0<=f_i<=1`, `int f_i=1`, equals the supremum over product indicators `prod_i 1_{E_i}` with `|E_i|=1`. This is used only as an exact front-end equivalence; no interval extremality is inferred.

2. **Designated partner, fleet03/B13, null-pair product smoothing**, `yspennstate/math-open-problems@a7594ff13b36fbc1819f60ec287e8232bd39974d`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260922T165804Z-fleet03-B13-qform-r12/REPORT.md`. Its translation-uniform product envelope is the source mechanism behind the near-null aggregate theorem from this slot's previous run.

3. **This slot's support-free near-null interpolation**, `yspennstate/math-open-problems@94bb5d8d6a87b78d1cdda3e8db9f00d07c494e5c`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T172625Z-fleet02-B13-productset-r13/REPORT.md`. In exact rank three, for spectral rows `r_i,r_j`, wedge mass `Delta=||r_i wedge r_j||^2`, physical coefficients `a=r_i^T Lambda r_i`, `b=r_i^T Lambda r_j`, `c=r_j^T Lambda r_j`, if `b!=0` and `|a|,|c|<=|b|/2`, then

`||p_Q||_infinity <= C_agg (|b| |det Lambda| Delta)^(-1/4)`,

with `C_agg=43.323633263897`.

4. **Diffuse separable-phase theorem**, `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, path `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`. If `U` has three orthonormal columns and every row leverage is at most `1/2`, then for arbitrary independent cap-one inputs and arbitrary coordinate-separable real measurable perturbations,

`||(U^T X)^T M(U^T X)+sum_i V_i(X_i)||_density,infinity <= 3e |det M|^(-1/3)`.

5. **Orientation-free physical-pivot theorem**, summarized in current research from the completed rank-two half-Riesz proof: for exact rank three `A=R Lambda R^T`, a physical coordinate `i` of spectral-row leverage `c_i=||r_i||^2` and nonzero physical pivot `a=A_ii` satisfies

`||p_Q||_infinity <= 128 (c_i |a| |det Lambda|)^(-1/4)`.

The theorem retains arbitrary outside affine/coupling terms in its stated conditioning scope.

6. **Newest designated-partner result**, fleet03/B13 run `20260922T182042Z-fleet03-B13-qform-r14`, full report `yspennstate/math-open-problems@58dc674aade01aa82bb10fcaf254af03f41575fa:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260922T182042Z-fleet03-B13-qform-r14/REPORT.md`. If a physical pair has `A_ii=A_jj=A_ij=0` and its full `2 x (n-2)` cross bank `C` obeys `D_cross=det(CC^T)>0`, then

`||p_Q||_infinity <= 2 sqrt(e) D_cross^(-1/4)`.

This newest partner theorem is applied below as an additional arbitrary-rank paid branch; it also clarifies why exact-rank-three needs a different mechanism.

## 2. First unpaid implication at start of run

The preceding B13 run paid every **fixed** invertible physical triple, including its near-null binary-pair collar, but the full spectral hypothesis does not force one physical triple with a uniformly large determinant. The missing implication was therefore an aggregation/selection statement that converts Parseval-frame mass into a product-preserving density payment before reciprocal fourth roots are taken.

This report attacks that implication first in exact rank three, where the frame geometry is transparent and all three spectral eigenvalues already have target scale. The resulting reduction is quantitative and uses only original physical coordinates.

## 3. Heavy/light spectral-frame setup

Let

`A = R Lambda R^T`,  `R^T R = I_3`,

where every eigenvalue of the symmetric invertible `3 x 3` matrix `Lambda` has magnitude at least one. Write `r_i in R^3` for the `i`-th physical spectral row of `R`, and

`c_i = ||r_i||^2`,  so `0<=c_i<=1` and `sum_i c_i=3`.

Fix the threshold

`tau = 3/10`.

Define the heavy and light physical coordinates

`H={i:c_i>3/10}`,  `L=H^c`.

Then `|H|<=9`. Define the light and heavy Gram operators

`S = sum_{i in L} r_i r_i^T = R_L^T R_L`,
`G = sum_{i in H} r_i r_i^T = I_3-S`.

Let the eigenvalues of `S` be

`s_1 >= s_2 >= s_3 >=0`.

Because `G=I-S`, the two operators commute and the decreasing eigenvalues of `G` are

`1-s_3 >= 1-s_2 >= 1-s_1`.

The next theorem pays the `s_3>=3/5` and `s_2<=3/5` regimes. Only

`s_3 < 3/5 < s_2`

remains.

## 4. Diffuse-full branch: `s_3 >= 3/5`

### Theorem 4.1 — `QFORM-RANK3-LIGHT-FULL-DIFFUSE-v1`

If `s_3>=3/5`, then for arbitrary independent input densities bounded by one,

`||p_Q||_infinity <= 5e < 13.592`.

The same constant bounds every product-indicator slab density after the exact extreme-product reduction.

### Proof

Condition on the finitely many heavy original coordinates. The light coordinates remain independent with the same density cap. Their conditional quadratic polynomial is

`x_L^T R_L Lambda R_L^T x_L + ell^T x_L + const`,

where `ell` is an arbitrary deterministic vector depending on the conditioned heavy values.

Since `s_3>0`, set

`U=R_L S^(-1/2)`,  `M=S^(1/2) Lambda S^(1/2)`.

Then `U^T U=I_3` and

`R_L Lambda R_L^T = U M U^T`.

For every light row,

`||u_i||^2 = r_i^T S^(-1) r_i <= ||r_i||^2/s_3 <= (3/10)/(3/5)=1/2`.

Thus the diffuse separable-phase theorem applies even with the arbitrary conditional linear term, giving

`||p_{Q|X_H}||_infinity <= 3e |det M|^(-1/3)`.

Now

`|det M| = det(S)|det Lambda| >= s_3^3`,

because all three eigenvalues of `S` are at least `s_3` and `|det Lambda|>=1`. Therefore

`||p_{Q|X_H}||_infinity <= 3e/s_3 <= 5e`.

The bound is uniform in the conditioned heavy coordinates, so averaging gives the same bound for `Q`. QED.

This is an actual product-preserving conditioning argument: the only conditioning is on original independent coordinates, and the remaining nonseparable quadratic form is handled by the proved diffuse theorem.

## 5. Heavy-pair branch: `s_2 <= 3/5`

The opposite side of the trichotomy has enough two-dimensional heavy Gram mass to force a physical pair with a quantitative Euclidean wedge.

### Lemma 5.1 — heavy Cauchy--Binet pair

If `s_2<=3/5`, then there are heavy indices `i<j` such that

`Delta_ij := ||r_i wedge r_j||^2 >= 1/225`.

### Proof

The two largest eigenvalues of `G` obey

`1-s_3 >= 1-s_2 >= 2/5`.

Hence the second elementary symmetric function satisfies

`e_2(G)>= (2/5)^2 = 4/25`.

Exterior Cauchy--Binet gives the exact physical-coordinate identity

`e_2(G)=sum_{i<j, i,j in H} ||r_i wedge r_j||^2`.

There are at most `binom(9,2)=36` heavy pairs. Therefore some pair satisfies

`Delta_ij >= (4/25)/36 = 1/225`. QED.

The next elementary lemma converts Euclidean wedge mass into a physical quadratic coefficient without assuming a favorable sign pattern.

### Lemma 5.2 — compression max-entry from wedge mass

For any two linearly independent spectral rows `r_i,r_j`, write

`Delta=||r_i wedge r_j||^2`,
`a=r_i^T Lambda r_i`, `b=r_i^T Lambda r_j`, `c=r_j^T Lambda r_j`.

Then

`max(|a|,|b|,|c|) >= Delta/4`.

### Proof

Let `T:R^2 -> span{r_i,r_j}` send the standard basis to `r_i,r_j`. Then

`det(T^T T)=Delta`,

while

`sigma_max(T)^2 <= tr(T^T T)=c_i+c_j<=2`.

Therefore

`sigma_min(T)^2 >= Delta/2`.

Let `L` denote the compression of `Lambda` to the two-plane `span{r_i,r_j}` in an orthonormal basis. By Cauchy interlacing in dimension three and the hypothesis that **all three** eigenvalues of `Lambda` have magnitude at least one,

`||L||_op >=1`.

Indeed, for signature `(2,1)` the top compressed eigenvalue is at least the second ambient eigenvalue, hence at least one; for signature `(1,2)` the bottom compressed eigenvalue is at most the second ambient eigenvalue, hence at most `-1`; the definite cases are immediate.

Write the polar-coordinate factorization `T=U K`, where `U` is an isometry onto the pair plane and `K=(T^T T)^(1/2)`. The physical `2 x 2` coefficient matrix is

`M_2=T^T Lambda T = K L K`.

Choose a unit eigenvector `v` of `L` with eigenvalue `mu`, `|mu|>=1`, and put `x=K^(-1)v`. Then

`x^T M_2 x = mu`,  `||x||<=sigma_min(T)^(-1)`.

After normalizing `x`,

`||M_2||_op >= sigma_min(T)^2 >= Delta/2`.

A symmetric `2 x 2` matrix whose entries all have magnitude at most `m` has operator norm at most `2m`. Thus

`max(|a|,|b|,|c|)>=Delta/4`. QED.

### Theorem 5.3 — `QFORM-RANK3-HEAVY-PAIR-PAID-v1`

If `s_2<=3/5`, then

`||p_Q||_infinity <1127`.

More precisely, the physical pair from Lemma 5.1 is paid by one of two source-valid mechanisms:

- a nonzero physical scalar pivot, giving at most `1126.544`; or
- the near-null product/aggregate theorem, giving at most `919.034`.

### Proof

Take the heavy pair from Lemma 5.1 and abbreviate its wedge by `Delta>=1/225`. Both row leverages exceed `3/10`.

By Lemma 5.2,

`max(|a|,|b|,|c|)>=Delta/4`.

**Case 1: one physical diagonal is not tiny.** If

`|a|>=Delta/8` or `|c|>=Delta/8`,

apply the completed physical-pivot theorem at that heavy coordinate. Since its leverage exceeds `3/10` and `|det Lambda|>=1`,

`||p_Q||_infinity
 <=128[(3/10)(Delta/8)]^(-1/4)
 <=128*6000^(1/4)
 =1126.5430230955435...`.

**Case 2: both physical diagonals are tiny.** Suppose

`|a|<Delta/8` and `|c|<Delta/8`.

Then Lemma 5.2 forces

`|b|>=Delta/4`,

and therefore

`|a|,|c| <= |b|/2`.

The support-free near-null exact-rank-three aggregate theorem applies:

`||p_Q||_infinity
 <= C_agg (|b||det Lambda|Delta)^(-1/4)
 <= C_agg (Delta^2/4)^(-1/4)
 = C_agg sqrt(2) Delta^(-1/2)`.

With `Delta>=1/225` and `C_agg=43.323633263897`, this is

`<=43.323633263897*sqrt(2)*15
 =919.0330459962196...`.

Thus both cases are bounded by `1127`. QED.

The point of this case split is that it never divides by whichever local coefficient is small. If the scalar pivot is useful, the orientation-free half-Riesz theorem pays it. If both scalar pivots are small, the **same pair** is forced into the near-null hyperbolic collar, where the partner-derived logarithmic product envelope plus the aggregate third direction pays it.

## 6. Exact-rank-three trichotomy and the only surviving Gram geometry

Combining Theorems 4.1 and 5.3 gives:

### Corollary 6.1 — `QFORM-RANK3-HEAVY-LIGHT-TRICHOTOMY-v1`

Every exact-rank-three target instance satisfies one of the following:

1. `s_3>=3/5`, and `||p_Q||_infinity<=5e`;
2. `s_2<=3/5`, and `||p_Q||_infinity<1127`;
3. the unique unpaid mixed geometry

   `s_3<3/5<s_2`.

In the third case, after removing at most nine heavy original coordinates, the light spectral rows carry two uniformly nondegenerate directions (their second Gram eigenvalue exceeds `3/5`) but are weak in exactly one direction (their third Gram eigenvalue is below `3/5`). Equivalently, the heavy rows carry more than `2/5` of the Parseval mass in the missing spectral direction, while they do **not** carry two directions strongly enough to trigger the heavy-pair Cauchy--Binet payment.

So the exact-rank-three obstruction is narrowed to a one-heavy-direction / two-diffuse-plane interaction. This is precisely the regime in which a single good minor is the wrong currency and a grouped product-preserving mechanism is needed.

The threshold `3/10` was chosen because it makes the diffuse normalization exactly hit the proved row-leverage threshold `1/2` when `s_3=3/5`, while keeping at most nine heavy rows. No optimization of the resulting constant is claimed.

## 7. Application of the newest fleet03/B13 whole-cross-bank theorem

The newest designated-partner result landed during this run and is compatible with the full arbitrary-rank target. It supplies a third, independent paid branch that is invisible to one-minor selection:

### Corollary 7.1 — zero-pair whole-bank branch

For an arbitrary target matrix, if some original physical pair `i,j` satisfies

`A_ii=A_jj=A_ij=0`

and the determinant of its full two-row cross-bank Gram matrix satisfies

`D_cross=det(CC^T)>=1/225`,

then the partner theorem gives

`||p_Q||_infinity
 <=2 sqrt(e) D_cross^(-1/4)
 <=2 sqrt(e) 225^(1/4)
 =2 sqrt(15e)
 =12.770940047919...`.

This is a genuine group-before-reciprocal payment and survives arbitrarily many outside coordinates and arbitrary fragmented input supports.

It does **not** collapse the exact-rank-three mixed regime above. In exact rank three, two independent physical spectral rows cannot simultaneously be `Lambda`-null and mutually `Lambda`-orthogonal: a nondegenerate 3D indefinite form has Witt index one. Hence an exact zero physical pair either has dependent spectral rows, in which case its two cross-bank rows are proportional and `D_cross=0`, or it is impossible. The partner theorem therefore pays a genuinely higher-rank branch, while Sections 4--6 supply the complementary rank-three frame reduction.

This is an actual application of the completed partner result, not a claim that its hypothesis follows universally.

## 8. Product-indicator formulation

By the exact B13 bang-bang theorem, every density estimate proved above is equivalent, with the same constant, to the corresponding geometric slab-volume bound for arbitrary measurable product factors `E_i` of measure one. In particular, in either paid exact-rank-three Gram regime,

`|{x in prod_i E_i : t <= x^T A x <= t+epsilon}| <=1127 epsilon`

for every `t`, `epsilon>0`, with the sharper `5e` constant in the diffuse-full branch.

No connectedness or fragment-count restriction is placed on any `E_i`. This is essential because the live localization counterexamples show that such restrictions are false as exact extremal reductions.

## 9. What remains unpaid

This report does not prove the full conjecture. The first unpaid implication is now sharper:

`QFORM-RANK3-MIXED-ONEHEAVY-TWODIFFUSE-v1`:

> In exact rank three, prove a universal density/slab bound in the sole remaining heavy/light regime `s_3<3/5<s_2`, where at most nine heavy coordinates carry the missing one-dimensional spectral mass while the light coordinates form a quantitatively diffuse two-dimensional plane; or give a genuine independent product-law counterexample.

A promising next mechanism is to aggregate the light two-plane **before** conditioning on the heavy variables, then combine an orientation-free rank-two fractional trace with the one-dimensional heavy bank. This must retain original-coordinate independence and cannot replace the product source by an arbitrary joint projected density.

For the full theorem there is an additional debt: arbitrary extra spectral components. The ridge-window theorem already pays one large diffuse full-rank branch, and the newest partner theorem pays a whole-cross-bank zero-pair branch, but an exhaustive bridge from the bare three-large-eigenvalue hypothesis to these product-preserving payments is not yet proved.

## 10. Deterministic sanity check

A fixed-seed standard numerical checker tested the exact algebra used by the reduction, not the theorem by sampling:

- `10,000` random Parseval frames with dimensions `3..60`;
- `2,408` sampled cases with `s_2<=3/5`;
- maximum `||S+G-I||` entry error `1.1102230246251565e-15`;
- maximum error in `e_2(G)=sum_{i<j in H}||r_i wedge r_j||^2`: `3.1086244689504383e-15`;
- zero failures of the forced `Delta>=1/225` pair bound;
- `20,000` independent random checks of Lemma 5.2, with zero failures and minimum observed ratio `max(|a|,|b|,|c|)/(Delta/4)=3.4484261531...`.

The checker also recomputed the displayed constants. These finite checks are diagnostic only; the proof is the analytic argument above.

**Status:** full QFORM remains **OPEN / NOT PROVED**. The target-level movement is the explicit two-paid-branches trichotomy; the mechanism-level movement is from local hyperbola interpolation to global heavy/light Parseval-frame aggregation plus exterior Cauchy--Binet forcing.