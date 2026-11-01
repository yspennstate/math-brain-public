# fleet03/B09 — disjoint-bank cross-square compression

**Run:** `fleet03-B09-20260922T144807Z-qform11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Bilinear block mechanism  
**Classification:** `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository reads/writes are not native learned-memory ingestion.

## 1. Exact scope and live corrections

The full target is still open: for independent real physical coordinates with probability densities at most one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one law-, matrix-, and dimension-independent bound on the density of `X^T A X`, or give a target-valid counterexample. Continuity is tracked separately.

This run changes mechanism from the preceding scalar-pivot/rank-two-Schur route. The live corrections show that a single Schur rank-two extraction is not forced, fixed local minors can vanish on diffuse target families, and false post-rotation independence or conditional density caps cannot be used. The mechanism below therefore aggregates original coordinates into **three disjoint independent banks before any reciprocal local-minor payment** and uses conditional linear anti-concentration on the off-diagonal product.

The designated partner is `fleet04/B09`. At the startup and pre-derivation checks there was no completed current-QFORM handoff or canonical research directory for that slot, so no partner premise is fabricated. A final partner check is required before publication; if a completed artifact appears it can be incorporated in a later run. The completed source results actually applied here are:

1. `QFORM-CROSS-SQUARE-PRODUCT-v1`, source-pinned at `yspennstate/math-open-problems@1cb7cc3265c46a8509e4b5c4f5e2c064ef1640c2:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/b10-20260922T115000Z-qform-r1/REPORT.md`. It gives the cap-one scalar estimate for `2bUV+cW^2`.
2. Livshyts--Paouris--Pivovarov marginal-density transfer, as recorded in `yspennstate/math-open-problems@1cb7cc3265c46a8509e4b5c4f5e2c064ef1640c2:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260922T135329Z-qform-B18-a01-r11/REPORT.md`: every normalized one-dimensional projection of a cap-one product density has density at most `sqrt(2)`.

The newer fleet01/B18 two-bank definite transfer is complementary rather than duplicative: it treats a definite quadratic compression of two independent banks. The theorem below handles the **indefinite cross-square normal form** in three disjoint banks.

## 2. A singular half-potential bound

### Lemma 2.1

If `Y` has a probability density bounded by `M`, then

`sup_s E |s-Y|^(-1/2) <= 2 sqrt(2M)`.                                  (2.1)

### Proof

Among all probability densities bounded by `M`, the integral against the symmetric decreasing kernel `|s-y|^(-1/2)` is maximized by height `M` on the centered interval of length `1/M`. Hence

`E|s-Y|^(-1/2)`
` <= M integral_{-1/(2M)}^{1/(2M)} |y|^(-1/2)dy`
` = 2 sqrt(2M)`.

This is translation invariant, so the same bound holds uniformly in `s`. QED.

## 3. Cap-rescaled cross-square theorem

### Theorem 3.1 — `QFORM-CROSS-SQUARE-CAPS-v1`

Let `U,V,W` be mutually independent real random variables with probability-density caps

`||p_U||_infinity<=M_U`, `||p_V||_infinity<=M_V`, `||p_W||_infinity<=M_W`.

Let `beta,gamma` be nonzero and allow arbitrary aligned affine terms:

`T = 2 beta U V + gamma W^2 + r U + s V + t W + q`.

Then `T` has an essentially bounded density and

`boxed( ||p_T||_infinity
 <= 4 sqrt(2) M_W sqrt(M_U M_V) / sqrt(|beta gamma|). )`              (3.1)

Moreover `T` has a continuous density.

### Proof

Translations remove the affine terms without changing independence or density caps:

`U'=U+s/(2 beta)`, `V'=V+r/(2 beta)`, `W'=W+t/(2 gamma)`.

Up to an additive constant,

`T=2 beta U'V'+gamma W'^2`.

For fixed `u,v`, the density of `gamma W'^2` is bounded on its supporting half-line by

`M_W |gamma|^(-1/2) |y|^(-1/2)`.

Therefore, for almost every `x`,

`p_T(x) <= M_W |gamma|^(-1/2)
           E |x-2 beta U'V'|^(-1/2)`.                                (3.2)

Condition on `U'=u`. The variable `2 beta u V'` has density cap

`M_V/(2|beta u|)`.

Lemma 2.1 gives, uniformly in `x`,

`E_{V'} |x-2 beta u V'|^(-1/2)
 <= 2 sqrt( M_V/(|beta u|) )`.                                      (3.3)

Average in `U'`. Applying Lemma 2.1 once more, now centered at zero,

`E |U'|^(-1/2) <= 2 sqrt(2M_U)`.                                    (3.4)

Combining (3.2)--(3.4) gives exactly (3.1).

This is the same cap-rescaling one obtains by applying the completed cap-one `QFORM-CROSS-SQUARE-PRODUCT-v1` to `M_U U`, `M_V V`, `M_W W`; equations (3.2)--(3.4) give a self-contained derivation and exhibit the conditional linear anti-concentration explicitly.

For continuity, `2 beta U'V'` has an `L^1` density (condition on the almost surely nonzero `U'` and scale the density of `V'`), and `gamma W'^2` has an `L^1` density. They are independent. The convolution of two `L^1(R)` functions has a continuous representative vanishing at infinity. QED.

### Small-ball form

For every interval `J`,

`P(T in J)
 <= [4 sqrt(2) M_W sqrt(M_U M_V)/sqrt(|beta gamma|)] |J|`.          (3.5)

Thus the mechanism is genuinely linear in interval length; there is no square-root decoupling loss.

## 4. New disjoint-bank theorem

Let `I,J,K` be pairwise disjoint sets of original physical coordinates. Take nonzero vectors

`a in R^I`, `b in R^J`, `c in R^K`,

and define the independent bank projections

`U=<a,X_I>`, `V=<b,X_J>`, `W=<c,X_K>`.

By the Livshyts--Paouris--Pivovarov one-dimensional marginal theorem,

`M_U <= sqrt(2)/||a||_2`,
`M_V <= sqrt(2)/||b||_2`,
`M_W <= sqrt(2)/||c||_2`.                                           (4.1)

(The singleton case is even better, but `sqrt(2)` is a uniform bound.)

Apply Theorem 3.1.

### Theorem 4.1 — `QFORM-THREE-BANK-CROSS-SQUARE-v1`

For

`Q = 2 beta <a,X_I><b,X_J>
     + gamma <c,X_K>^2
     + r<a,X_I>+s<b,X_J>+t<c,X_K>+q`,                               (4.2)

with disjoint original-coordinate banks and cap-one independent inputs,

`boxed(
 ||p_Q||_infinity
 <= 8 sqrt(2) /
    sqrt( |beta gamma| ||a||_2 ||b||_2 ||c||_2^2 ).
)`                                                                    (4.3)

The density is continuous, and every interval `L` satisfies the same constant times `|L|`.

Define the two scale-invariant effective coefficients

`B = |beta| ||a||_2 ||b||_2`,
`C = |gamma| ||c||_2^2`.                                             (4.4)

Then (4.3) is simply

`boxed( ||p_Q||_infinity <= 8 sqrt(2) / sqrt(B C). )`                (4.5)

### Spectral interpretation

On the orthonormal bank vectors

`e_I=a/||a||`, `e_J=b/||b||`, `e_K=c/||c||`,

the physical quadratic matrix in (4.2) has the effective `3 x 3` block

`[[0, sign(beta) B, 0],
  [sign(beta) B, 0, 0],
  [0, 0, sign(gamma) C]]`.

Its three nonzero eigenvalues have magnitudes

`B, B, C`.                                                           (4.6)

Therefore if this exact-rank-three bank form lies in the owner's target, so `B>=1` and `C>=1`, then

`boxed( ||p_Q||_infinity <= 8 sqrt(2) < 11.314, )`                   (4.7)

with a continuous density. No physical-coordinate rotation is performed on the random vector: the only projections are one-dimensional marginals of disjoint coordinate banks, for which (4.1) is valid under the original product law.

## 5. Diffuse target family with every local coefficient small

For every integer `m>=1`, split `3m` physical coordinates into three banks `I,J,K` of size `m` and set

`U=m^(-1/2) sum_{i in I} X_i`,
`V=m^(-1/2) sum_{j in J} X_j`,
`W=m^(-1/2) sum_{k in K} X_k`,

`Q_m = 2 U V + W^2`.                                                 (5.1)

Its physical matrix has entries `1/m` on the `I x J` and `J x I` blocks, entries `1/m` on the `K x K` block, and zero elsewhere. The nonzero spectrum is exactly

`{1,-1,1}`.                                                          (5.2)

Thus it satisfies the three-large-eigenvalue target for every `m`. Yet the largest physical matrix entry is `1/m`, and any fixed-size principal submatrix has operator norm at most its size divided by `m` by the row-sum bound. Hence every fixed local-minor/coefficient certificate degenerates as `m->infinity`.

The bank theorem is insensitive to that degeneration: `B=C=1`, so for arbitrary independent cap-one input laws,

`boxed( ||p_{Q_m}||_infinity <= 8 sqrt(2) )`                         (5.3)

for all `m`, and the density is continuous. This is a direct high-cardinality example showing why aggregation must occur before reciprocal local-minor costs.

The exact verifier stored with this report checks, using rational arithmetic, that the physical matrices in (5.1) have eigenvectors supported on the three bank-constant directions with eigenvalues `+1,-1,+1`, and annihilate every within-bank zero-sum vector.

## 6. What this pays and what remains

This run pays a concrete part of the B09 structural debt:

- the off-diagonal interaction may be completely diffuse across two arbitrarily large physical banks;
- every individual cross coefficient may go to zero;
- the third curvature direction may likewise be a diffuse rank-one square on a third independent bank;
- nevertheless original-coordinate product structure compresses to three independent scalar marginals, and conditional linear anti-concentration gives a direct `O(|J|)` interval bound with no resampling exponent loss.

It also complements the current `QFORM-LPP-TWO-BANK-DEFINITE-v1`: the latter covers definite two-bank compression, while Theorem 4.1 covers the canonical **indefinite** bank-compressed signature `(+,-,+)` represented as `2UV+W^2`.

The full target remains open. The missing implication is an **extraction/absorption theorem**: starting from an arbitrary symmetric `A` with at least three large eigenvalues, produce either an already-paid diffuse/Schur/definite-bank certificate or a three-bank cross-square certificate of the form (4.2), while allowing the remaining spectral components and unaligned cross-bank couplings. Arbitrary extra spectrum can cancel a selected cross block, and generic rotations destroy independence, so neither can be discarded.

Continuity is **proved for Theorems 3.1 and 4.1**, but not for the full conjecture.

## 7. Partner and integrity status

- designated partner `fleet04/B09`: no completed current-QFORM artifact observed at the checks made during this derivation; none was fabricated or inferred from absence;
- completed scalar cross-square result: substantively applied through the cap-rescaling formula (3.1);
- LPP marginal theorem: substantively applied through (4.1)--(4.5);
- full QFORM conjecture: `OPEN`;
- native learned-memory retrieval/use: not observed; status remains `WITHOUT_VERIFIED_BRAIN`;
- no pointwise law-uniform Fresnel decay, rotated independence, generic fiber supremum, or arbitrary conditional-cap replacement is used.
