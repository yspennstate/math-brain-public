# account02/B09 — rank-two cross-block integrability ladder and third-pivot absorption

**Run:** `20260922T124417Z-account02-B09-QFORM-r2`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Bilinear block mechanism  
**Classification:** `ESSENTIAL_STEP_APPLIED`; full conjecture remains OPEN / not proved / not disproved  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Target, corrections, and first unpaid implication

The full target is the universal interval estimate

`P(X^T A X in [t,t+h]) <= C h`

for every dimension, every independent real coordinates with densities at most one, and every real symmetric `A` with at least three eigenvalues of modulus at least one.

Corrections consumed before this report: law-uniform pointwise one-dimensional Fresnel decay is false; post-rotation independence is unavailable; naive fiber-supremum integration loses dimension; an invertible rank-two cross block alone does **not** force bounded density; universal `C=pi` is false; generic two-sheet X-ray control alone is insufficient.

The previous B09 run already proved direct `O(h)` smoothing when one pivot-side principal block vanishes, and refuted the stronger claim that an invertible rank-two cross block alone suffices. The present first unpaid implication was therefore the named partner's `QFORM-BILINEAR-BLOCK-ABSORPTION-v1`: retain rank-two cross smoothing when both within-block quadratics are present, without a Cauchy--Schwarz/decoupling exponent loss.

This run closes that implication at the correct intermediate regularity scale and shows how one genuine third quadratic pivot upgrades it to `L^infinity`.

## 1. Sources actually applied

### Named partner account03/B09

Canonical report:

- repository `yspennstate/math-open-problems`
- commit `41fc39eccdd44a0dcae6619676bf41f5ea21bb3e`
- path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T114536Z-account03-B09-qform-r11/REPORT.md`

It proves `QFORM-RANK2-BILINEAR-DIRECT-v1`: for independent product vectors `U,V`, cross matrix `M` with two singular values `s1>=s2>0`, and arbitrary measurable `H(U)`,

`||p_{H(U)+2U^T M V}||_infinity <= 2 sqrt(pi)/sqrt(s1 s2)`.

It also proves the exact Pluecker identity for a rank-two spectral component across a coordinate cut,

`sigma1 sigma2 = |lambda1 lambda2| sqrt(W_S W_T)`.

### Cross-block Fourier theorem

Interactive canonical report:

- repository `yspennstate/math-open-problems`
- commit `8624982153e5a2154e4ae8922d2fe4dc77080efc`
- path `proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md`

Its `QFORM-CROSSBLOCK-RANK-r-FOURIER-v1` proves for a rank-`r` original-coordinate cross block with nonzero singular-value product `Delta` that

`|phi_Q(t)| <= (2 pi)^(r/2) |t|^(-r/2) Delta^(-1/2)`.

The report used this for `r>2`; at the borderline `r=2` the bound is `O(1/|t|)` and is not integrable.

### Dependent third-square smoothing

Canonical account01/B11 report:

- repository `yspennstate/math-open-problems`
- commit `2279571f59ade7a9ec478af1e4818f6c117ac224`
- path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T121344Z/REPORT.md`

Its `QFORM-DEPENDENT-SQUARE-L3-SMOOTHING-v1` says: if `R` has density with `||p_R||_3=M`, and conditional on `R=r` a real variable `V` has density at most one, then for `d!=0`,

`||p_{R+dV^2}||_infinity <= 4 |d|^(-1/2) M^(3/4)`.

No independence between `R` and `V` is required.

## 2. New theorem: the rank-two cross integrability ladder

### Theorem 2.1 — `QFORM-RANK2-CROSS-LP-v1`

Partition the original independent coordinates into two disjoint blocks `I,J`. Write

`Q = q_I(X_I) + 2 X_I^T M X_J + q_J(X_J)`

where `q_I,q_J` are arbitrary quadratic-affine functions and the original-coordinate cross block `M` has rank exactly two with nonzero singular values `s1>=s2>0`. Put

`Delta = s1 s2`.

Then for every `p` with `2<=p<infinity`, `Q` has a density and

`boxed( ||p_Q||_p <= (2p)^(1-1/p) Delta^(-(p-1)/(2p)) ).`                 (2.1)

In particular,

`boxed( ||p_Q||_2 <= 2 Delta^(-1/4), )`                                    (2.2)

and

`boxed( ||p_Q||_3 <= 6^(2/3) Delta^(-1/3). )`                              (2.3)

Thus arbitrary within-block quadratic terms do **not** destroy rank-two bilinear smoothing; what fails at rank two is only the endpoint `L^infinity` estimate.

### Proof

Apply the rank-`r` cross-block Fourier argument at the borderline `r=2`. It keeps both within-block phases inside complex pushforward densities, so no assumption is made that either principal block vanishes. It gives, for `t!=0`,

`|phi_Q(t)| <= C/|t|`,  with  `C=2 pi Delta^(-1/2)`,                       (2.4)

while trivially `|phi_Q(t)|<=1`.

Let `q=p/(p-1)`, so `1<q<=2`. Splitting the integral at `|t|=C`,

`||phi_Q||_q^q
 <= 2 [ C + C^q int_C^infinity t^(-q) dt ]
 = 2 C [1 + 1/(q-1)]
 = 2 C p.`                                                                  (2.5)

With Fourier convention `hat f(t)=int exp(itx)f(x)dx`, Riesz--Thorin between inverse Fourier `L^1 -> L^infinity` and Plancherel gives

`||F^{-1} g||_p <= (2 pi)^(-1/q) ||g||_q`.                                 (2.6)

Therefore the inverse transform of `phi_Q` belongs to `L^p`; tested against Schwartz functions it represents the law of `Q`, hence is its density. Combining (2.5)--(2.6),

`||p_Q||_p
 <= (2 pi)^(-1/q) (2 C p)^(1/q)
 = (2p)^(1/q) Delta^(-1/(2q))`,

which is exactly (2.1) since `1/q=1-1/p`. Equations (2.2) and (2.3) are `p=2,3`. QED.

### Why this is the correct absorption level

The previous B09 source-valid counterexample

`(X1+Y1)^2-(X2+Y2)^2`

has a rank-two cross block but a logarithmically unbounded density at zero. A logarithm is nevertheless in every finite `L^p`, fully consistent with Theorem 2.1. Thus the theorem repairs the rank-two mechanism exactly as far as a third smoothing direction can use it, without asserting the false endpoint.

## 3. New theorem: rank-two Schur-cross plus one physical pivot

### Theorem 3.1 — `QFORM-RANK2-SCHUR-PIVOT-v1`

Let the original coordinates be partitioned into disjoint sets `I,J,{k},R`, and condition on the outside block `R`. On `I,J,{k}` write the quadratic matrix as

`[[B, M, r],
  [M^T, C, s],
  [r^T, s^T, d]]`,

where `d!=0`. Define the cross block of the scalar-pivot Schur complement

`N = M - r s^T/d`.                                                         (3.1)

Assume `N` has rank exactly two, with nonzero singular values `sigma1>=sigma2>0`, and put

`Delta_S = sigma1 sigma2`.

Then, uniformly over every outside conditioning and hence unconditionally,

`boxed(
 ||p_{X^T A X}||_infinity
 <= 4 sqrt(6) |d|^(-1/2) Delta_S^(-1/4).
)`                                                                          (3.2)

All couplings inside `B,C`, all couplings `r,s` to the pivot, all affine terms created by outside conditioning, and all arbitrary permitted input laws are retained.

### Proof

After conditioning outside, write the pivot coordinate as `Z`, the two coordinate blocks as `U,V`, and complete the square in the **original independent coordinate** `Z`:

`Q = d ( Z + theta(U,V) )^2 + R(U,V)`,                                     (3.3)

where `theta` is affine and the cross block of the residual quadratic `R` is exactly `N` in (3.1). The within-block quadratic matrices of `R` are `B-rr^T/d` and `C-ss^T/d`; they are arbitrary and need no sign condition.

Theorem 2.1 at `p=3` gives, uniformly in every affine term,

`||p_R||_3 <= 6^(2/3) Delta_S^(-1/3).`                                     (3.4)

Put `W=Z+theta(U,V)`. Conditional on `R(U,V)=rho`, the law of `W` is a mixture of translates of the original law of `Z`. Since the density of `Z` is at most one, that conditional density is also at most one. Therefore account01/B11's dependent-square theorem applies to (3.3):

`||p_Q||_infinity
 <=4 |d|^(-1/2) [6^(2/3) Delta_S^(-1/3)]^(3/4)
 =4 sqrt(6) |d|^(-1/2) Delta_S^(-1/4).`

The bound is uniform in the outside variables, so averaging conditional densities proves (3.2) for the full quadratic form. QED.

This is a direct `O(|I|)` interval bound. No squaring of the desired probability, no resampling, and no `h^(1/2)` or `h^(1/4)` exponent loss occurs.

## 4. Direct application of the named partner result

The partner theorem gives a sharper constant when one Schur-complement side is free. Suppose in Theorem 3.1 that, after completing the pivot square, the residual has the form

`R = H(U) + 2 U^T N V`

with `rank N=2`. The named account03/B09 result gives

`K := ||p_R||_infinity <= 2 sqrt(pi) Delta_S^(-1/2).`                      (4.1)

Since `||p_R||_1=1`,

`||p_R||_3 <= K^(2/3)`.                                                     (4.2)

Feeding the **actual inequality (4.2)** into the dependent-square theorem yields

`boxed(
 ||p_Q||_infinity
 <= 4 sqrt(2) pi^(1/4) |d|^(-1/2) Delta_S^(-1/4).
)`                                                                          (4.3)

Thus the named partner's completed theorem is not merely cited: it quantitatively improves the pivot bound on its compatible free-side branch.

Likewise, in the partner's rank-two spectral-component setting

`Delta_S=|lambda1 lambda2| sqrt(W_S W_T)`,

so (3.2) becomes the explicit product-structure inequality

`||p_Q||_infinity
 <=4 sqrt(6) |d|^(-1/2)
   |lambda1 lambda2|^(-1/4) (W_S W_T)^(-1/8)`,                              (4.4)

whenever that rank-two component is the actual Schur-cross block under consideration. This identifies exactly how disjoint Pluecker mass pays part of the third-direction bound.

## 5. Target-level stress instance: the old rank-two obstruction becomes safe after one square

Let five independent inputs have arbitrary densities bounded by one and set

`Q=(X1+Y1)^2-(X2+Y2)^2+Z^2`.                                               (5.1)

Its matrix is permutation-similar to

`diag(J_2,-J_2,[1])`, where `J_2=[[1,1],[1,1]]`,

so its eigenvalues are

`{2,-2,1,0,0}`.

Hence (5.1) is a genuine instance of the full target's three-large-eigenvalue regime. With the split `I={X1,X2}`, `J={Y1,Y2}`, the cross block is

`M=diag(1,-1)`,

so `Delta=1`; the pivot `Z` has `d=1` and is decoupled, hence its Schur-cross is unchanged. Theorem 3.1 gives the universal law-independent bound

`boxed( ||p_Q||_infinity <=4 sqrt(6). )`                                    (5.2)

By contrast, deleting `Z^2` gives exactly the previous B09 method counterexample with a logarithmic singularity. This is a concrete demonstration that the new `L^3 -> L^infinity` pivot mechanism spends the third spectral direction rather than falsely trying to make the two-direction saddle bounded by itself.

## 6. What remains open

The new local absorption theorem is not yet a full extraction theorem. The spectral hypothesis `s_3(A)>=1` does not currently force an original-coordinate scalar pivot `d` and disjoint Schur cut `I|J` for which

`|d|^(1/2) (sigma1(N)sigma2(N))^(1/4)`

is bounded below universally. Fixed principal triples and fixed cross blocks can both lose dimension on diffuse frames, and arbitrary extra spectrum can cancel a selected cross block.

The first unpaid implication is therefore:

> **`QFORM-SCHUR-CROSS-OR-DIFFUSE-AGGREGATION-v1` (OPEN).** From `s_3(A)>=1`, produce a dimension-free product-preserving dichotomy: either (a) a physical scalar pivot whose Schur complement has a quantitatively rank-two disjoint cross block, so Theorem 3.1 applies; or (b) a diffuse/high-cardinality branch controlled by the existing rank-three cross-block / separable-phase mechanisms. The aggregation must occur before reciprocal coordinate-minor costs are paid.

A valid falsifier must be an actual symmetric matrix with three eigenvalues of modulus at least one for which every such pivot/cut resource degenerates, not an arbitrary bistochastic or rotated-coordinate surrogate.

## 7. Status

`ESSENTIAL_STEP_APPLIED`.

Proved in this run:

1. `QFORM-RANK2-CROSS-LP-v1`, an all-finite-`p` integrability ladder for a genuine rank-two original-coordinate cross block with **arbitrary both-side quadratic terms**;
2. `QFORM-RANK2-SCHUR-PIVOT-v1`, which converts that `L^3` control plus one original physical quadratic pivot into a direct `L^infinity` / `O(h)` bound;
3. a quantitatively sharper compatible branch obtained by applying the named account03/B09 theorem;
4. closure of the exact target instance `(X1+Y1)^2-(X2+Y2)^2+Z^2`, which is the previous rank-two obstruction plus precisely one third large direction.

The universal conjecture remains OPEN. No numerical computation is used as mathematical evidence in this report.
