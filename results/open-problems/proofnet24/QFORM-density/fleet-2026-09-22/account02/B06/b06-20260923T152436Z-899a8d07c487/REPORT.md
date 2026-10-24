SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T15:24:36Z.
attacking: partner r38 recursive rank-two cross tube: derive a tail-retaining weighted reciprocal receiver on an exact physical null bank, then identify why nonzero self-curvature must consume the third large direction.

# account02/B06 — null-bank two-singular receiver and non-null obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`, programme revision `2026-09-22.5`  
**Run:** `b06-20260923T152436Z-899a8d07c487`  
**Status:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`; full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The exact target remains: arbitrary independent ORIGINAL real coordinates with density caps one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment/support/log-concavity/iid/diagonal-basis/post-rotation-independence assumption is introduced. Continuity remains separate.

Source pins actually consumed:

- newest-Claude package `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`; its Ball/Livshyts-Paouris-Pivovarov product-projection bounds are used below, and its ruled Theorem C is applied to a real target family in Section 6;
- designated partner account03/B06 r38, canonical `yspennstate/math-open-problems@ba023626f934128aadad51710c9ee8428dfe33c7`, which retains the complete small cross tail in the recursive rank-two tube;
- its immediate r37 predecessor `yspennstate/math-open-problems@fa9d5dd3cc78a092484480b536872d332e22c90a`, which supplies the literal original-coordinate N3 cross cut and the quantitative second-singular-value floor used in Section 4.

## 1. A weighted reciprocal lemma in two dimensions

### Lemma 1.1 — `QFORM-2D-RECIPROCAL-BATHTUB-v1`

Let `Z` be any random vector in `R^2` with probability density bounded by `K`. Then, for every `z0 in R^2`,

`boxed: E |Z-z0|^{-1} <= 2 sqrt(pi K).`                                 (1.1)

No moment or support assumption is needed.

#### Proof

Layer cake gives

`E |Z-z0|^{-1}
 = integral_0^infinity P(|Z-z0|^{-1}>t) dt
 = integral_0^infinity P(|Z-z0|<1/t) dt.`                              (1.2)

The density cap implies

`P(|Z-z0|<r) <= min(1, K pi r^2).`                                     (1.3)

With `t0=sqrt(pi K)`, split (1.2):

`<= integral_0^t0 1 dt + integral_t0^infinity K pi t^{-2} dt
 = t0 + K pi/t0
 = 2 sqrt(pi K).`                                                       (1.4)

QED.

This is the exact weighting mechanism wanted by the B06 assignment: the reciprocal singularity is integrated against the actual two-dimensional product-derived density. It is not replaced by an infinite fiber supremum.

## 2. Null-bank receiver retaining the entire cross tail

Partition the ORIGINAL coordinates into two independent product banks `I` and `J`. Write the full quadratic-plus-affine form as

`Q = F(X_I) + 2 X_I^T M X_J + b_J^T X_J`,                              (2.1)

where `F` is arbitrary measurable. In the quadratic-form application, (2.1) is exactly the condition that the physical principal block on the J bank vanishes: `A_JJ=0`; every quadratic and affine term on the I bank is absorbed into `F`.

Let the singular values of `M` be

`s1 >= s2 >= ...`,                                                     (2.2)

and assume `s2>0`.

### Theorem 2.1 — `QFORM-NULL-BANK-TWO-SINGULAR-RECEIVER-v1`

For arbitrary independent original coordinates with density caps one,

`boxed: ||p_Q||_infinity <= 2 sqrt(pi) / sqrt(s1 s2).}`                 (2.3)

In particular, every singular direction of `M` beyond the first two may be arbitrary and is retained. The theorem needs no finite support, moments, diagonal basis, or independence after a spectral rotation. It gives essential boundedness; continuity is not asserted.

#### Proof

Condition on the ORIGINAL I-bank, `X_I=x`. The conditional law is a one-dimensional linear form in the untouched independent J-coordinates:

`Q | X_I=x = F(x) + c(x)^T X_J`,

`c(x) := 2 M^T x + b_J.`                                               (2.4)

The completed product-projection theorem used throughout the pinned newest-Claude package gives, for any coefficient vector `a`,

`||p_{a^T X_J}||_infinity <= sqrt(2)/||a||_2.`                          (2.5)

Thus, for almost every `x` with `c(x)!=0`,

`||p_{Q|X_I=x}||_infinity <= sqrt(2)/||c(x)||.`                         (2.6)

Let `u1,u2` and `v1,v2` be the first two left/right singular vectors of `M`. Define

`U=(u1^T X_I, u2^T X_I).`                                              (2.7)

Because `u1,u2` are orthonormal and `X_I` is an original-coordinate product law with density caps one, the two-dimensional product-projection theorem in the pinned source gives

`||p_U||_infinity <= 2.`                                                (2.8)

Put `d_k=v_k^T b_J`. Projection of (2.4) onto `span(v1,v2)` yields

`||c(X_I)||
 >= |(2 s1 U1+d1, 2 s2 U2+d2)|.`                                      (2.9)

Call the two-vector on the right `Z`. The affine map from `U` to `Z` has Jacobian `4s1s2`, so (2.8) gives

`||p_Z||_infinity <= 2/(4s1s2)=1/(2s1s2).`                             (2.10)

Lemma 1.1 therefore gives

`E ||c(X_I)||^{-1}
 <= E |Z|^{-1}
 <= 2 sqrt(pi/(2s1s2))
 = sqrt(2pi/(s1s2)).`                                                   (2.11)

Average the actual conditional bound (2.6), not its supremum:

`P(Q in B)
 <= |B| sqrt(2) E ||c(X_I)||^{-1}
 <= |B| 2sqrt(pi)/sqrt(s1s2)`                                          (2.12)

for every finite-measure Borel set `B`. Thus the law is absolutely continuous and its Radon-Nikodym density has the essential bound (2.3). The exceptional set `c(X_I)=0` has probability zero because the two-dimensional vector `Z` has a density. QED.

### Why this is tail-retaining

Nothing in the proof replaces `M` by its rank-two approximation. The complete coefficient vector `c(x)=2M^Tx+b_J` remains inside the conditional linear form. Only the lower bound

`||c(x)|| >= ||Proj_span(v1,v2) c(x)||`                                (2.13)

is used. Extra cross singular directions, including arbitrarily small nonzero ones, cannot invalidate the estimate.

## 3. Exact target family with diffuse physical edges

Take two independent product banks of size at least two and any rank-two cross matrix `M` with `s1=s2=1`, for example a diffuse orthogonal two-frame on each side, and set

`A=[[0,M],[M^T,0]].`                                                    (3.1)

Then the nonzero spectrum of `A` is `{1,1,-1,-1}`. Hence this is already inside the exact QFORM target, even though every individual physical edge can tend to zero in a diffuse sequence. Theorem 2.1 gives

`boxed: ||p_{X^TAX}||_infinity <= 2sqrt(pi)=3.5449077018... .}`         (3.2)

This explicitly pays a four-large-eigenvalue family by aggregate original-coordinate product structure rather than by selecting one good physical edge.

## 4. Real application to partner account03/B06 r38

The designated partner r38 keeps the entire literal original-coordinate cross matrix `N` alive on its recursive branch; it does **not** delete the small nonzero tail. Its r37 input is the true near-rank-two N3 chamber, with squared singular values `x_k=s_k(N)^2`,

`E=||N||_F^2 > 11907/16384,`                                           (4.1)

`x2 >= E/64,`                                                          (4.2)

and the tail `sum_{k>=3}x_k<E/64`. The latest r38 theorem further splits by anchored cofactor three-volume versus a Frobenius tube around rank two, but the full matrix `N` remains the physical cross block in every branch.

Suppose now that **either one of the two physical same-bank principal blocks on this r37/r38 partition is exactly zero**. Apply Theorem 2.1 with the null bank as `J`. Since `s1(N)>=s2(N)` and (4.2),

`sqrt(s1 s2) >= s2 >= sqrt(E)/8.`                                      (4.3)

Therefore

`||p_Q||_infinity
 <= 2sqrt(pi)/sqrt(s1s2)
 <= 16sqrt(pi)/sqrt(E)
 < 2048sqrt(pi)/sqrt(11907)
 = 33.2662396488... .`                                                  (4.4)

This is a genuine full-density payment in the partner's near-rank-two tube. It applies **before or after** the r38 cofactor split and retains the complete cross tail. Arbitrary quadratic curvature on the opposite bank remains inside the arbitrary function `F` and is fully retained.

Thus the partner's next debt `QFORM-ABSOLUTE-RANK2-TUBE-TAIL-RETAINING-RECEIVER-v1` is closed on its exact physical null-bank subbranch with an explicit universal constant `<33.267`.

## 5. The tempting near-null extension is false without spending the third direction

The exact-null hypothesis in Theorem 2.1 cannot be weakened by simply calling a small same-bank quadratic block a perturbation.

Fix `0<delta<=1`. Let `X1,X2,Y1,Y2` be four independent `Unif[-1/2,1/2]` variables and set

`q_delta
 = delta(Y1^2-Y2^2)
   +2X1Y1+2X2Y2
   +delta^{-1}(X1^2-X2^2)`                                             (5.1)

`= delta^{-1}(X1+delta Y1)^2
  -delta^{-1}(X2+delta Y2)^2.`                                         (5.2)

Relative to the banks `X=(X1,X2)` and `Y=(Y1,Y2)`, the cross block is exactly the identity, so

`s1(M)=s2(M)=1,`                                                        (5.3)

while the Y-self block is `delta diag(1,-1)` and has operator norm `delta`.

For `S=X+delta Y`, its density equals one on a neighborhood of zero. Hence `S1=X1+delta Y1` and `S2=X2+delta Y2` are independent with densities bounded below near zero. Writing

`S1^2-S2^2=(S1-S2)(S1+S2)`,                                            (5.4)

the joint density of the two factors is positive near the origin. The product-density formula therefore contains

`int dp/|p|`                                                            (5.5)

on every sufficiently small punctured neighborhood, so the density of `S1^2-S2^2`, and hence of `q_delta`, diverges logarithmically at zero.

The matrix of (5.1) has only the two nonzero eigenvalues

`+(delta+delta^{-1}),  -(delta+delta^{-1}).`                            (5.6)

Therefore this is **not a QFORM counterexample**. It is a source-valid counterexample to the intermediate claim

> two strong cross singular directions + an arbitrarily small self-block can be handled by a perturbative extension of the null-bank receiver without consuming a third large direction.

That claim is false for every `delta>0`.

## 6. The third direction repairs the obstruction; pinned newest-Claude result applied

Add one fresh independent cap-one variable `Z` and define

`Q_delta^* = q_delta + Z^2.`                                            (6.1)

The full physical matrix now has nonzero spectrum

`{delta+delta^{-1}, 1, -(delta+delta^{-1})}`,                           (6.2)

so it is an exact QFORM target for `0<delta<=1`.

This is also a direct real application of the pinned newest-Claude ruled-level-set Theorem C: on every one-sheet level `s>=0`, its signature `(+, +, -)` theorem gives

`boxed: p_{Q_delta^*}(s) <= pi sqrt(2).}`                               (6.3)

No post-rotation independence is used in invoking that theorem; it was proved for the product-projection provenance of the target.

For this particular family one can in fact pay all levels more sharply by preserving the original grouping. Let

`S1=X1+delta Y1`, `S2=X2+delta Y2`.

The pairs `(X1,Y1)`, `(X2,Y2)`, and `Z` are independent, so `S1,S2,Z` are independent. Convolution with `X_i`, whose density cap is one, gives

`||p_{S1}||_infinity, ||p_{S2}||_infinity <=1.`                         (6.4)

Then

`Q_delta^* = delta^{-1}S1^2 - delta^{-1}S2^2 + Z^2.`                   (6.5)

The completed separable theorem applies to the two same-sign coefficients `delta^{-1}` and `1`, both at least one, and yields

`boxed: ||p_{Q_delta^*}||_infinity <= pi.}`                             (6.6)

So the route counterexample in Section 5 is genuinely repaired once a usable third large direction is consumed; it is not evidence against QFORM.

## 7. First unpaid implication after this run

The null-bank subbranch of the partner r38 tube is now paid. The remaining exact debt is narrower:

`QFORM-RANK2-TUBE-NONNULL-BANK-THIRD-DIRECTION-v1`:

> In the r37/r38 near-rank-two original-coordinate cross tube, retain the full small nonzero cross tail and arbitrary nonzero quadratic curvature on **both** banks. Use the third large spectral direction to produce either (i) a product-preserving two-dimensional random critical-value payment that regularizes the rank-two hyperbolic singularity, or (ii) an already-completed third-volume / mixed-hub / physical-pair exit. No argument may treat a nonzero self-block as a small additive random error solely because its coefficient matrix norm is small.

The family (5.1) proves why this third-direction consumption is mathematically necessary: the exact null endpoint is stable under the weighted reciprocal theorem, but every nonzero opposite-sign self-curvature can recreate the rank-two logarithmic singularity if the third direction is ignored.

A promising next interface is therefore not a perturbative `||A_JJ||` estimate. It is a three-source estimate in which the two singular directions of the cross coefficient map are averaged as in Theorem 2.1 while the third large direction controls the random critical value created by completing the non-null J-bank quadratic form.

## 8. Integrity/status

`QFORM-2D-RECIPROCAL-BATHTUB-v1`: **PROVED**.  
`QFORM-NULL-BANK-TWO-SINGULAR-RECEIVER-v1`: **PROVED supporting density theorem**.  
`QFORM-NEARNULL-PERTURBATIVE-RECEIVER`: **REFUTED intermediate mechanism** by (5.1)-(5.6).  
Partner r38 null-bank near-rank-two subbranch: **PAID**, bound `<33.267`.  
Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.  
Universal continuity: **OPEN**; Theorem 2.1 asserts essential boundedness only.

The deterministic arithmetic/algebra check is in `check_null_bank_receiver.py` and `CHECKS.md`. No FEI, installation, benchmark, scheduler, notification, email, account, permission, or public-release action is part of this run.
