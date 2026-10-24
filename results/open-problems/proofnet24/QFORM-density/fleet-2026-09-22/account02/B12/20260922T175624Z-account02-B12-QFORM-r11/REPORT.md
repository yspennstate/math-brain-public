# account02/B12 — redundant mixed-packet stability under arbitrary spectral spikes

Run: `20260922T175624Z-account02-B12-QFORM-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Additional eigenvalue control`  
Status: `PROVED_SUPPORTING_STABILITY_THEOREM / SHARP_MECHANISM_BARRIER / FULL_TARGET_OPEN`  
Execution memory label: `WITHOUT_VERIFIED_BRAIN` (repository transport was used; no native learned-memory receiver was verified).

## 1. First live implication and source state

The full target is unchanged: for independent real coordinates with one-dimensional densities at most one and a real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal bound for the density of `X^T A X`, or produce a genuine counterexample.

Fresh owner control is revision `2026-09-22.9`. The latest designated partner result actually consumed is account03/B12, `QFORM-CONDITIONAL-3D-CAP-MOMENT-FALSE-v1`, canonical proof commit

`yspennstate/math-open-problems@e5aae2b611688b9e0711105cab1878cd9186b6c3`

with source-bound handoff

`yspennstate/math-research-brain@0be00f14d246c917032f588cc70e6a1a718456a7`.

It proves that the owner-message spectral-complement bridge

`E_Z ||p_{Y|Z}||_infinity^(2/3) <= C`

is false, even for three block-constant spectral directions of a product cube; the quantity grows at least `Gamma(4/3)^3 m`. Thus a valid extra-eigenvalue argument cannot pay a conditional spectral `L^infinity` cap after rotation.

This report therefore keeps the added spectrum in ORIGINAL coordinates. The positive analytic dependency is account03/B09 `QFORM-FULL-BLOCK-BILINEAR-ABSORPTION-v1`, canonical commit

`yspennstate/math-open-problems@446d0a33ef626b11ed5da529f2cec821732e97e9`.

Its exact statement used below is: if disjoint original-coordinate sets `P,Q` have equal size `m>=3` and the cross block `A[P,Q]` is invertible, then, with arbitrary same-side quadratic terms, arbitrary outside couplings and arbitrary independent cap-one input laws,

`||p_{X^T A X}||_infinity <= [m/(m-2)] |det A[P,Q]|^(-1/m)`.

For `m=3` this is

`||p||_infinity <= 3 |det A[P,Q]|^(-1/3)`,

and the density is continuous. The proof is a mixed-Hessian Plancherel argument in the original independent coordinates; it does not use post-rotation independence.

The first unpaid implication attacked here is therefore:

> How much physical mixed-Hessian redundancy is sufficient to survive one or more completely arbitrary added spectral directions, without conditioning on the spectral complement?

## 2. Main theorem: rank-r arbitrary spikes plus a small full-rank tail

Let `r>=0` and put `k=3+r`. Let `I_0,J_0` be disjoint sets of `k` ORIGINAL coordinates. Let `A_0` be real symmetric and assume its physical cross block

`B_0=A_0[I_0,J_0]`

satisfies

`s_k(B_0) >= sigma > 0`.                                           (2.1)

Let

`A=A_0+R+S`,                                                        (2.2)

where

- `R` is arbitrary real symmetric with `rank R <= r`; its nonzero eigenvalues may have arbitrary signs and arbitrarily large magnitudes;
- `S` is arbitrary real symmetric with `||S||_op <= delta < sigma`; it may have arbitrary rank and either signs.

Thus `R` is an arbitrary packet of at most `r` added spectral directions, and `S` is an arbitrary smaller spectral tail. No commutation with `A_0`, eigenvector alignment, support condition or probabilistic independence is assumed.

### Theorem 2.1 (`QFORM-REDUNDANT-MIXED-PACKET-SPIKE-STABILITY-v1`)

For every product law of independent real coordinates with densities bounded by one, `X^T A X` has a bounded continuous density and

`||p_{X^T A X}||_infinity`
` <= 3 * binom(3+r,3)^(1/3) / (sigma-delta).`                       (2.3)

In particular, for ONE arbitrary added eigen-direction (`r=1`), a physical `4x4` cross packet with `s_4(B_0)>=sigma` survives every rank-one symmetric perturbation of arbitrary sign and size plus every full-rank tail of operator norm `delta<sigma`, with

`||p||_infinity <= 3*4^(1/3)/(sigma-delta)`
` = 4.7622031559.../(sigma-delta).`                                (2.4)

This is a direct stability theorem for arbitrary larger/smaller added eigenvalues. It is not a claim that the bare three-large-eigenvalue hypothesis automatically supplies (2.1).

### Proof

Write the final cross block as

`B=A[I_0,J_0]=B_0+R_c+S_c`,

where `R_c=R[I_0,J_0]`, `S_c=S[I_0,J_0]`. Restricting rows and columns cannot increase rank or operator norm, so

`rank R_c <= r`, `||S_c||_op <= delta`.                            (2.5)

The rank-perturbation singular-value inequality gives

`s_3(B_0+R_c) >= s_{3+r}(B_0) >= sigma`.                           (2.6)

Indeed, for matrices of the same size and a perturbation of rank at most `r`, `s_{j+r}(M) <= s_j(M+E)`; take `j=3`. Weyl's singular-value inequality then gives

`s_3(B) >= sigma-delta =: gamma >0`.                               (2.7)

Now use the exact Cauchy--Binet/exterior-power identity

`e_3(BB^T)`
` = sum_{P subset I_0, Q subset J_0, |P|=|Q|=3} det(B[P,Q])^2`.    (2.8)

Since the first three singular values of `B` are each at least `gamma`,

`e_3(BB^T) >= s_1(B)^2 s_2(B)^2 s_3(B)^2 >= gamma^6`.            (2.9)

There are exactly `binom(k,3)^2` summands in (2.8). Hence some pair of disjoint physical triples `P subset I_0`, `Q subset J_0` satisfies

`|det B[P,Q]|`
` >= gamma^3 / binom(k,3).`                                       (2.10)

Apply the completed account03/B09 `m=3` mixed-Hessian theorem to this ACTUAL final physical `3x3` cross block. All coordinates outside `P union Q`, including the unused coordinates of `I_0 union J_0`, are simply conditioned; all same-side and outside quadratic curvature is allowed by that theorem. Therefore

`||p||_infinity`
` <= 3 |det B[P,Q]|^(-1/3)`
` <= 3 binom(k,3)^(1/3) / gamma`,                                 (2.11)

which is (2.3). The same source theorem gives continuity. No spectral rotation of `X` occurs anywhere. QED.

## 3. Why the redundancy threshold `3+r` is rank-sharp for this mechanism

The preceding theorem is not merely a loose rank count. One cannot replace the `3+r` redundant mixed directions by `2+r` and still guarantee that a three-direction mixed packet survives an arbitrary rank-`r` spectral addition.

Fix `sigma>=1` and let `k=2+r`. On `2k` original coordinates split into disjoint blocks `I,J`, take

`A_0 = [[0, sigma I_k],[sigma I_k,0]]`.                            (3.1)

Its spectrum is `+sigma` and `-sigma`, each with multiplicity `k`. For `a=1,...,r`, set

`z_a=(e_a^I+e_a^J)/sqrt(2)`

and add the symmetric rank-`r` perturbation

`R=-2 sigma sum_{a=1}^r z_a z_a^T`.                              (3.2)

The `z_a` are orthonormal. In the hyperbolic eigenbasis, each `z_a` is a `+sigma` eigenvector of `A_0`, so (3.2) changes its eigenvalue from `+sigma` to `-sigma`; the companion vector `(e_a^I-e_a^J)/sqrt(2)` remains at `-sigma`, and every untouched hyperbolic pair remains at `+/-sigma`. Thus EVERY eigenvalue of the final matrix `A_0+R` still has modulus exactly `sigma`. In particular this is a genuine target-class family, not a nearly singular spectral artifact.

But its final physical cross block is exactly

`(A_0+R)[I,J] = sigma diag(0,...,0,1,1)`,                         (3.3)

with `r` zeros and only TWO surviving singular directions. Hence every `3x3` mixed minor on this packet is zero.

For `r=1`, this says a single arbitrary spectral addition can annihilate a nondegenerate `3x3` mixed-Hessian certificate while leaving all full-matrix eigenvalues at modulus `sigma`. Therefore one redundant fourth mixed singular direction is genuinely necessary for a worst-case rank-only persistence theorem. More generally, `3+r` versus `2+r` is the exact rank threshold for guaranteeing three surviving mixed directions.

This construction does NOT refute QFORM: the resulting hyperbolic matrix has other source-valid smoothing descriptions. It refutes only the stronger stability assertion that fewer than `3+r` base mixed directions must leave a usable `3x3` mixed packet after an arbitrary rank-`r` spectral addition.

## 4. Relation to the latest partner correction and earlier B12 routes

The account03/B12 block-cube construction shows that spectral-complement conditioning can have conditional `L^infinity` cost growing linearly in dimension even when the same matrix is uniformly controlled by a physical principal-triple theorem. The present theorem provides a complementary replacement interface: when curvature is present as a redundant ORIGINAL-coordinate mixed packet, arbitrary spectral spikes are absorbed by rank interlacing BEFORE any local determinant is inverted.

The order is important:

1. keep the full physical cross packet;
2. spend only the rank of the arbitrary spectral perturbation, via (2.6);
3. spend the small spectral tail once, via (2.7);
4. aggregate the surviving third exterior power by (2.8);
5. only then select a final physical `3x3` determinant and apply the source-valid mixed-Hessian theorem.

Selecting a `3x3` minor first is invalid under arbitrary spikes, as Section 3 proves. Likewise, conditioning on spectral extra coordinates first is invalid as a universal cap-moment route, by the designated partner result.

Compared with the earlier B12 regularized-determinant stability theorem, which preserved five cross directions after arbitrary finite-rank perturbations, (2.3) lowers the physical redundancy needed for the direct arbitrary-curvature mixed-Hessian endpoint to exactly `3+r`. The price is the explicit fixed-r factor `binom(3+r,3)^(1/3)`; this grows like `r` and therefore is NOT a universal way to absorb an unbounded number of arbitrary added directions.

## 5. Exact remaining implication

Full QFORM remains OPEN.

The new theorem completely pays the following branch:

> a source matrix has a disjoint original-coordinate cross packet with `3+r` singular values at scale `sigma`, then at most `r` arbitrary added spectral directions of any signs/magnitudes plus an arbitrary mixed-sign operator-norm-`delta` tail (`delta<sigma`) cannot destroy bounded density; the explicit final constant is (2.3).

What remains is structural. The bare hypothesis `s_3(A)>=1` does not force such a redundant physical packet; diagonal matrices have none, and the live block-constant/diffuse corrections show that single-minor selection loses dimension. The replacement full proof must route every matrix into one of the already-paid diagonal/principal/grouped branches or an aggregate mixed packet WITHOUT paying a reciprocal diffuse minor first.

The fixed-r growth in (2.3) also identifies a real mechanism boundary: if arbitrarily many extra eigendirections are to be absorbed through mixed packets, one needs an aggregate Fourier/exterior-power theorem on the whole rank-three surviving image, not repeated selection of one `3x3` minor.

No claim of a continuous density is made outside the theorem's mixed-packet scope. No moments, support bounds, Gaussianity, post-rotation independence, law-uniform one-dimensional Fresnel decay, or conditional spectral density cap is used.
