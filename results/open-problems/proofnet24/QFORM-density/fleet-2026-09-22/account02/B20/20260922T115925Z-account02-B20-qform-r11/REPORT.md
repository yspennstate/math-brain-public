# account02/B20 — QFORM proof closure: zero-pivot aggregate rank-two packet

Run: `20260922T115925Z-account02-B20-qform-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control: `2026-09-22.5`  
Classification: `ESSENTIAL_STEP_APPLIED / SUPPORTING_LEMMA_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source corrections

For every `n`, independent real random variables `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least `1`, prove that

`Q=X^T A X`

has a density with a universal finite essential-supremum bound, or give a valid counterexample. No moments, centering, log-concavity, compact support, connected support, diagonal-basis product structure, or independence after an orthogonal spectral rotation may be assumed.

This run preserves the live source corrections: law-uniform pointwise one-variable quadratic-phase decay is false; unrestricted spectral-fiber suprema can lose dimension; spectral rotation does not preserve coordinate independence; and a nonsingular rank-two cross minor by itself does not control the density when the pivot side has its own quadratic curvature (`QFORM-CROSSMINOR-ALONE-FALSE`).

The assigned partner `account03/B20` had no completed current-QFORM handoff on the fresh prepublication read, so no partner result is fabricated. The run instead consumes the newest compatible source-backed results described below.

## 2. Fresh compatible results consumed

### 2.1 Aggregate cross-block theorem, rank greater than two

The interactive source-pinned handoff `20260922T121109Z-crossblock-and-lower-bounds` proves: if an original-coordinate cross block `A[I,J]` has rank `r>2` and `Delta` is the product of all its nonzero singular values, then, allowing arbitrary within-block quadratic and linear terms,

`||p_Q||_infinity <= (2r/(r-2)) Delta^(-1/r)`.

It also closes sufficiently diffuse rank-exactly-three spectral frames and records that the diagonal constant `pi` is not a universal upper bound. This leaves rank two outside that cross-block Fourier theorem, consistently with the logarithmic rank-two obstruction.

### 2.2 Multi-pivot theorem and its correction

`account02/B09`, run `20260922T115241Z-account02-B09-QFORM-r1`, proves a square zero-pivot multi-pivot theorem: for disjoint `I,J`, `|I|=|J|=m>=2`, `A[I,I]=0`, and invertible `B=A[I,J]`,

`||p_Q||_infinity <= (m/(m-1)) |det B|^(-1/m)`.

The same source refutes the stronger cross-minor-alone claim when self-curvature remains on the pivot side.

### 2.3 Sharp linear-image input

`account01/B18` proves the source-valid projection inequality: if `T` has rank `m`, then for independent density-`<=1` coordinates,

`||p_{TX}||_infinity <= 2^(m/2)/sqrt(det(TT^T))`

in the rectangular projection regime, while the square case has the sharper direct change-of-variables bound. It also gives exact product-set extremalization, preserving fragmented supports.

## 3. New theorem: rectangular zero-pivot aggregate packet

### Theorem `QFORM-ZEROPIVOT-RECTANGULAR-v1`

Partition the physical coordinate set into pairwise disjoint sets `I,J,K`, with `|I|=m>=2`. Assume

1. `A[I,I]=0` exactly;
2. `B=A[I,J]` has full row rank `m`;
3. all coordinates of `X` are independent and have densities bounded by `1`.

No restriction is imposed on `A[J,J]`, `A[J,K]`, `A[K,K]`, or `A[I,K]`.

Then `Q=X^TAX` has a density satisfying

`||p_Q||_infinity <= (m/(m-1)) sqrt(2) det(BB^T)^(-1/(2m)).`  (3.1)

If `|J|=m` one may instead use the sharper square-block bound from B09,

`||p_Q||_infinity <= (m/(m-1)) |det B|^(-1/m)`.

The important new endpoint is `m=2`: for every full-row-rank `2 x |J|` cross block with exact zero pivot,

`||p_Q||_infinity <= 2 sqrt(2) det(BB^T)^(-1/4)
                      = 2 sqrt(2)/sqrt(s_1(B)s_2(B)).`  (3.2)

Thus the rank-two logarithmic cross-block wall disappears under the exact source-visible condition `A[I,I]=0` and an aggregate two-row cross-volume bound; one never selects a tiny local `2 x 2` minor.

### Proof

Condition on `X_K=k`. Write `U=X_I`, `Y=X_J`. Because `A[I,I]=0`, the conditional form has the exact shape

`Q = 2 U^T (B Y + d(k)) + H_k(Y)`,  (3.3)

where `d(k)=A[I,K]k` and `H_k` contains all terms independent of `U`. In particular arbitrary quadratic curvature in `Y` and arbitrary conditioned complement terms are retained rather than dropped.

Put `Z=BY+d(k)`. Given `Y=y`, `K=k`, choose measurably an index `a` with `|Z_a|=||Z||_infinity` (for instance the least maximizing index). Condition additionally on all `U` coordinates except `U_a`. Then (3.3) is affine in `U_a` with slope `2Z_a`. Since the density of `U_a` is at most `1`, for every interval `L`, on `Z!=0`,

`P(Q in L | Y,K,U_{I\{a}}) <= |L|/(2||Z||_infinity).`  (3.4)

Because `B` has full row rank, `Z` is absolutely continuous, so `P(Z=0)=0`.

Let

`M = 2^(m/2)/sqrt(det(BB^T)).`  (3.5)

The sharp linear-image bound gives `||p_Z||_infinity<=M`, uniformly in the shift `d(k)`. Hence, with `R=||Z||_infinity`,

`P(R<r) <= min(1, M(2r)^m).`  (3.6)

Layer cake yields

`E R^(-1)
 = int_0^infinity P(R<t^(-1)) dt
 <= 2 M^(1/m) + int_{2M^(1/m)}^infinity M(2/t)^m dt
 = (2m/(m-1)) M^(1/m).`  (3.7)

Average (3.4), use (3.7), and then remove the conditioning on `K`. For every interval `L`,

`P(Q in L) <= |L| * (m/(m-1)) M^(1/m)
             = |L| * (m/(m-1)) sqrt(2) det(BB^T)^(-1/(2m)).`  (3.8)

The interval domination criterion gives absolute continuity and exactly (3.1). No Fourier pointwise-decay assumption, no spectral rotation, no moment input, and no fiber supremum is used. QED.

## 4. Genuine target stress family: aggregate volume beats every local minor

Let `N` be even and let `B_N` be the `2 x N` matrix whose first row is identically `1/sqrt(N)` and whose second row is `+1/sqrt(N)` on the first `N/2` columns and `-1/sqrt(N)` on the last `N/2` columns. Then

`B_N B_N^T = I_2`.

Take the symmetric matrix

`A_N = [[0, B_N], [B_N^T, 0]]`.

Its nonzero eigenvalues are `+1,+1,-1,-1`; hence it is a genuine family satisfying the owner target's spectral hypothesis. The new theorem gives, for every admissible product input law,

`||p_{X^T A_N X}||_infinity <= 2 sqrt(2)`  (4.1)

uniformly in `N`.

But every physical `2 x 2` column minor of `B_N` is either `0` or has determinant magnitude `2/N`. Selecting one such local square pivot and paying the B09 determinant bound would cost order `sqrt(N)`. The aggregate Gram determinant `det(B_NB_N^T)=1` completely removes that artificial dimension loss.

This is the exact kind of aggregation needed in the full problem: accumulate spectral/cross energy before paying reciprocal local determinants.

## 5. Relation to the newer rank-r cross-block theorem

The fresh interactive theorem closes cross rank `r>2` even with arbitrary pivot-side self-curvature. The theorem here is not a competing re-proof. Its new content is the missing `r=2` endpoint under the exact zero-pivot hypothesis, and in particular the dimension-free stress family (4.1).

The `A[I,I]=0` hypothesis cannot simply be deleted: the live `QFORM-CROSSMINOR-ALONE-FALSE` example shows that a rank-two cross block together with uncontrolled pivot curvature may still produce a logarithmically unbounded density. Therefore the next step must be a genuine curvature-versus-aggregate structural lemma, not an assertion that cross volume alone suffices.

## 6. Optional route pruning: weighted-Wiener L1 is sufficient, not universal

The earlier averaged phase-Wiener criterion is a useful sufficient condition, but it cannot be imposed as a necessary universal bridge. Already for three independent `Uniform[-1/2,1/2]` coordinates with a solved diagonal three-square form, the selected three-coordinate Fourier transform factors into sinc functions. Each one-dimensional sinc has divergent absolute `L^1` norm, so the corresponding `W(t)=int |Psi_t(xi)| dxi` is infinite (whenever the remainder factor is nonzero), even though the quadratic density is uniformly bounded by the completed diagonal theorem. Thus a proof of the full target cannot require finite unweighted spectral-coordinate Wiener `L^1` for every admissible law.

## 7. Strongest conditional end-to-end skeleton after this run

The current source-valid branches now include:

- diagonal forms: completed, bound `pi` (but `pi` is not universal for all orientations);
- sufficiently diffuse rank-exactly-three spectral frames: completed by the fresh cross-block/diffuse theorem, with a universal constant;
- original-coordinate cross blocks of rank `r>2` with controlled aggregate singular-value product: completed by the fresh cross-block theorem;
- exact zero-pivot rank-two aggregate packets with controlled `det(BB^T)`: completed here;
- several localized physical pair/triple/codimension-one branches: completed by B12/B15/B17/B18 and related workers.

Therefore the first unpaid universal implication is now structural rather than analytic inside any of those packets.

### `QFORM-CURVATURE-OR-AGGREGATE-PIVOT-v2` (OPEN)

From the sole hypothesis that a real symmetric `A` has at least three eigenvalues of absolute value at least `1`, produce, in the original physical-coordinate product model and with dimension-free quantitative constants, at least one of:

1. a definite/controlled physical pair or triple to which the completed localized estimates apply;
2. an exact or source-validly transformable zero-pivot packet `I` with `|I|>=2` and aggregate cross Gram volume `det(A[I,J]A[J,I])^(1/(2|I|)) >= c>0`, enabling Theorem (3.1);
3. a cross packet of rank `r>2` with all-singular-value product `Delta^(1/r)>=c>0`, enabling the fresh interactive cross-block theorem; or
4. a diffuse spectral frame for which the remaining off-diagonal quadratic phase can be absorbed by a product-preserving extension of the completed diffuse theorem.

A fixed-principal-minor formulation is not adequate: Walsh/delocalized examples and (4.1) show why aggregation must occur before reciprocal determinant payment.

The present run proves the previously missing exact rank-two aggregate branch and supplies a source-valid family where it is essential. It does **not** prove the structural implication above and therefore does **not** prove the full QFORM conjecture.

## 8. Movement and next mechanism

Before: rank-two aggregate cross energy was trapped between a dimension-losing local-minor choice and the corrected fact that cross rank two alone is insufficient with self-curvature.

After: rank-two aggregate cross energy is fully payable whenever the pivot packet is exactly zero: the cost is `2 sqrt(2) det(BB^T)^(-1/4)` for two pivot coordinates, independent of ambient dimension and of all complement quadratic terms.

Target-level movement: none; the full target remains open.  
Mechanism movement: genuine; one endpoint of the curvature-or-aggregate split is now closed by a quantitative theorem.  
Next method: derive a quantitative dichotomy between pivot self-curvature and aggregate cross Gram volume directly from the spectral projector/`A^2` identities, with the localized physical-block theorems paying the curvature side. Avoid selecting one tiny minor before aggregation.

## 9. Source pins

Fresh brain-repository control was read at main `7ffa0cd53b8814a22e5deaa572dfc792b100491b` and refreshed during the run through main `ad092c59ad539c254aa30859f4bb10b19263ee51`. The latest compatible interactive cross-block event is source-pinned to math-open-problems commit `8624982153e5a2154e4ae8922d2fe4dc77080efc`. The B09 square multi-pivot report is math-open-problems commit `fa592b592c61bd1597aa8cf3270c3c9f58f410bf`. The assigned account03/B20 current-programme handoff directory had no completed commit at the last prepublication check.
