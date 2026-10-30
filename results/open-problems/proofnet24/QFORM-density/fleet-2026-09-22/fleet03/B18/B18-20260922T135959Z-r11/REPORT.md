# fleet03/B18 — product-projection transfer to a rank-two cross-averaging theorem

**Run:** `B18-20260922T135959Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Literature-to-proof transfer  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED

## 1. Exact target and purpose

The target is: for arbitrary independent real coordinates with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a dimension- and law-independent bound on the density of `X^T A X` (and separately address continuity), or exhibit a genuine counterexample.

This run transfers a sharp two-dimensional marginal-density theorem for product measures into a new quadratic-form branch. The new branch is deliberately stated in original independent coordinates; no rotation of the input vector is used.

## 2. Literature audit and hypothesis matching

### 2.1 Source actually transferred

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877–889; arXiv:1507.07949.

Their Theorem 1.1 states, in particular, that if

`f(x)=prod_i f_i(x_i)`, `||f_i||_1=1`, `||f_i||_infinity<=1`,

then every `k`-dimensional orthogonal marginal has density at most `2^(k/2)` (for the theorem's stated range `1<=k<n`). For `k=2<n`, the cap is `2`. No Gaussianity, moment assumption, compact support, connected support, identical-law assumption, or log-concavity is present. When the ambient dimension itself is two, the same needed cap follows directly (and more strongly) because the full product density is at most one and orthogonal maps preserve Lebesgue measure.

This is source-valid for the present target because the original coordinates are independent and have density caps one. It is applied only to an orthogonal projection of those original coordinates.

### 2.2 A tempting theorem that does *not* transfer directly

T. Juškevičius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190, proves a multidimensional Rogozin-type extremal theorem for sums of independent random vectors having finite ambient-dimensional maximum densities. It defines maximum density as infinity for a random vector that is not absolutely continuous in the ambient dimension.

Therefore it cannot be applied directly to

`B Y = sum_j b_j Y_j in R^2`,

because each summand `b_j Y_j` is supported on a line in `R^2` and has infinite two-dimensional maximum density. The Livshyts–Paouris–Pivovarov projection theorem closes exactly this hypothesis gap. In one dimension, the Juškevičius–Lee/Rogozin result is compatible with the elementary convolution bound used below, but it is not needed for the proof.

No exact published theorem matching the owner's full three-large-eigenvalue quadratic-form statement was identified in this source check; this is not a novelty claim.

## 3. New theorem: two-coordinate cross averaging

### Theorem 3.1 — `QFORM-TWOCOORD-CROSS-AVERAGING-v1`

Let `X_1,X_2,Y_1,...,Y_m` be independent real random variables, each with probability density bounded by one. Put `X=(X_1,X_2)` and `Y=(Y_1,...,Y_m)`. Let `B` be a real `2 x m` matrix of rank two, let `d in R^2`, and let `H:R^m->R` be measurable. Define

`R = 2 X^T (B Y + d) + H(Y)`.

If `sigma_1(B)>=sigma_2(B)>0` are the two singular values of `B`, then `R` has a **continuous** density and

`||p_R||_infinity <= 2 sqrt(2) / sqrt(sigma_1(B) sigma_2(B)).`        (3.1)

The conclusion is independent of `m`, of the laws, of `d`, and of `H`.

### Proof

Write an SVD

`B = U diag(sigma_1,sigma_2) V^T`,

where the two columns of `V` are orthonormal in `R^m`. If `m>2`, the `k=2` Livshyts–Paouris–Pivovarov marginal theorem gives the two-dimensional vector `V^T Y` a density bounded by `2`. If `m=2`, then `V` is square orthogonal, so `V^T Y` is merely an orthogonal image of the full product vector `Y`; its density is bounded by `1`, hence also by `2`. Thus in every allowed case

`Z := B Y + d`

has a two-dimensional density `g_Z` with

`||g_Z||_infinity <= M := 2/(sigma_1 sigma_2)`.                 (3.2)

Fix `Y=y` and write `z=By+d`. If `z != 0`, the conditional random variable

`2 z_1 X_1 + 2 z_2 X_2`

has a density. If both coefficients are nonzero, convolution and the elementary inequality `||f*g||_infinity <= min(||f||_infinity,||g||_infinity)` give

`||p_{2z_1X_1+2z_2X_2}||_infinity
 <= min(1/(2|z_1|),1/(2|z_2|))
 = 1/(2 ||z||_infinity).`                                      (3.3)

If exactly one coefficient vanishes, the same displayed bound follows from the remaining scaled coordinate alone. The event `Z=0` has probability zero by (3.2).

It remains to average the singular conditional bound without losing dimension. Set

`k(z)=1/(2||z||_infinity)`.

Among all probability densities `0<=g<=M` on `R^2`, the integral of the decreasing `l_infinity`-radial function `k` is maximized by filling its top level sets: `g=M` on a centered square of area `1/M`. If this square is `[-r,r]^2`, then `4r^2=1/M`, while

`integral_{[-r,r]^2} k(z) dz
 = integral_0^r [1/(2s)] d(4s^2)
 = 4r.`

Therefore

`E k(Z) <= M (4r) = 2 sqrt(M)
 = 2 sqrt(2/(sigma_1 sigma_2)).`                                (3.4)

Conditioning on `Y`, adding the deterministic shift `H(Y)`, and averaging conditional densities now gives a density `p_R` satisfying exactly (3.1).

For continuity, for almost every `Y=y` both coordinates of `Z` are nonzero, because `Z` has a two-dimensional density and the coordinate axes have Lebesgue measure zero. For such `y`, the conditional density in (3.3) is the convolution of two `L^1` densities and is continuous. The integrable majorant `k(Z)` from (3.4) is independent of the output point. Dominated convergence therefore gives a continuous representative of `p_R`. QED.

### Why this does not contradict the correction inbox

The correction `QFORM-CROSSMINOR-ALONE-FALSE` says that a nonsingular cross block by itself is not enough when uncontrolled same-side quadratic terms are present on both selected sides. Theorem 3.1 requires the **selected two-coordinate side to have zero self-quadratic block**; arbitrary self-interaction is allowed on the `Y` side through `H(Y)`. Thus the refuted premise is not used.

Likewise, the theorem does not assert that the three-large-eigenvalue hypothesis always produces such a pair. The correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` remains fully respected.

## 4. Application of completed partner result

The completed partner theorem is fleet04/B18's `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical source:

- repository `yspennstate/math-open-problems`
- commit `441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

It proves: if `R` has density at most `M` and, conditional on `R=r`, a random variable `V` has density at most one, then for `a!=0`, without assuming independence,

`||p_{R+aV^2}||_infinity <= 2 sqrt(M/|a|).`                     (4.1)

### Corollary 4.1 — pivot plus rank-two zero-self Schur pair

Let `A` be symmetric in the original independent-coordinate basis. Choose an original coordinate `z` with scalar pivot `a=A_zz !=0`. Let

`S = A_{bar z,bar z} - A_{bar z,z} A_{z,bar z}/a`

be the physical Schur residual. Suppose two remaining original coordinates form an index set `I` with

`S_{I,I}=0_{2x2}`,

and, writing `J=bar z \ I`, the physical cross block

`B=S_{I,J}`

has rank two with singular values `sigma_1>=sigma_2>0`. Then the full quadratic form has an essentially bounded density satisfying

`||p_{X^TAX}||_infinity
 <= 2^(7/4) |a|^(-1/2) (sigma_1 sigma_2)^(-1/4).`                (4.2)

**Proof.** Completing the square only in the original pivot coordinate gives

`X^TAX = a (X_z + a^(-1) A_{z,bar z} X_{bar z})^2
          + X_{bar z}^T S X_{bar z}.`

The residual is exactly of Theorem 3.1 form with `H` absorbing the arbitrary `J x J` block. Thus its density cap is

`M_R=2 sqrt(2)/(sigma_1 sigma_2)^(1/2).`

Conditional on the residual value, the shifted pivot variable is a mixture of translations of the original `X_z` density, hence its conditional density remains at most one. Applying (4.1) gives

`2 sqrt(M_R/|a|)
 =2^(7/4)|a|^(-1/2)(sigma_1 sigma_2)^(-1/4).`

No independence after completing the square is asserted. QED.

Corollary 4.1 proves an `L^infinity` density. The partner smoothing lemma does not by itself prove continuity, so continuity for this pivot-wrapped branch is **not claimed**. The residual theorem, Theorem 3.1, does prove continuity.

## 5. Concrete target-level family

The corollary applies to genuinely coupled matrices satisfying the owner's spectral hypothesis. Let

`S_2 = [[0,0,1,0],
        [0,0,0,1],
        [1,0,2,0],
        [0,1,0,-2]]`,

let `b=(1/20,1/20,1/20,1/20)^T`, and define

`A = [[2,b^T],
     [b,S_2 + (1/2) b b^T]].`

The Schur complement of the first coordinate is exactly `S_2`. Its selected first two residual coordinates have zero self block and cross matrix `B=I_2`, so (4.2) gives

`||p_{X^TAX}||_infinity <= 2^(5/4) = 2.378414230005442...`.      (5.1)

This matrix really satisfies the target spectral condition. Compare it with

`A_0 = diag(2,S_2)`.

The spectrum of `S_2` is

`{1+sqrt(2), sqrt(2)-1, 1-sqrt(2), -1-sqrt(2)}`.

The perturbation `A-A_0` is the sum of the off-diagonal pivot block and the lower block `(1/2)bb^T`, so

`||A-A_0||_op <= ||b||_2 + ||b||_2^2/2
 = 1/10 + 1/200 = 21/200.`

By Weyl's inequality, the second-largest eigenvalue of `A` is at least

`2-21/200 = 379/200 >1`,

and the smallest eigenvalue is at most

`-(1+sqrt(2))+21/200 < -1`.

Thus `A` has at least two eigenvalues greater than one and one eigenvalue less than minus one. All five original variables may have arbitrary independent densities bounded by one.

## 6. What this closes and what remains unpaid

This run closes a new product-preserving branch:

> a rank-two physical cross map is sufficient when one selected original-coordinate pair has zero self block, even if the opposite side has an arbitrary quadratic form, arbitrary dimension, arbitrary signs and arbitrarily small/large additional eigenvalues. After one physical scalar pivot, the same statement holds for a zero-self pair in the Schur residual via the partner dependent-square smoothing lemma.

The theorem is dimension-free and survives arbitrary fragmented input supports. It uses no pointwise quadratic-phase decay and no rotated-coordinate independence.

It does **not** derive the structural hypothesis from merely having three eigenvalues of modulus at least one. In particular, it does not solve the exact bank-aggregation families that refute one-minor extraction. The full conjecture remains open.

The next target-relevant implication is an aggregate replacement for exact zero-self extraction: use product-preserving coordinate banks to produce either (i) enough nearly-zero self energy plus a rank-two cross map so that a perturbative form of Theorem 3.1 survives, or (ii) a direct bank-averaged density estimate. The newly supplied regularized-determinant/diffuse theorem covers the low-leverage range branch; this theorem is complementary and should be tested in the leverage-heavy branch rather than treated as a full decomposition.

## 7. Status

- `QFORM-TWOCOORD-CROSS-AVERAGING-v1`: **PROVED**, with continuous density and explicit constant.
- `QFORM-PIVOT-CROSS-AVERAGING-v1` (Corollary 4.1): **PROVED SUPPORTING BRANCH**, with explicit `L^infinity` constant; continuity not established here.
- Partner result applied substantively: fleet04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`.
- Exact full QFORM target: **OPEN / NOT PROVED**.
