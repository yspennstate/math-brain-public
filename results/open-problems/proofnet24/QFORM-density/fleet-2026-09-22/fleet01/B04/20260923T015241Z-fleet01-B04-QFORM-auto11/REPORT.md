SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T01:52:41Z.
attacking: two-sided product-Fourier determinant aggregation at the rank-three threshold, seeking a direct e3 bound that bypasses high volume marginals and local-minor selection.

# fleet01/B04 auto11 — disjoint Pluecker-volume random cut closes a new exact-rank-three regime

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred; no native learned-memory receiver/ingestion was observed).  
**Continuity:** proved in the exact-rank-three branch below; NOT proved for the full target.

## 1. Exact target, conditional end-to-end route, and first unpaid implication

The owner target is: for every finite `n`, every independent real original-coordinate vector `X=(X_i)` with one-dimensional densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density with one universal `L^infinity` bound, or produce a target-valid counterexample.

No Gaussianity, moments, compact support, connected support, log-concavity, identical laws, or post-rotation independence is assumed here. In particular the argument below never asks for law-uniform pointwise quadratic-phase decay. It uses only original-coordinate cuts and an integrated joint bilinear Fourier theorem.

A compact conditional end-to-end route is:

1. Choose an original-coordinate cut `I sqcup J`.
2. Retain *all* self-quadratic curvature inside `I` and `J`.
3. If the physical cross block `B=A[I,J]` has exact rank three and product of its three nonzero singular values `Delta`, invoke fleet02/B04's completed two-sided-contamination Fourier theorem:

   `||p_Q||_infinity <= 3e Delta^(-1/3)`,

   and the density is continuous because the corresponding characteristic-function majorant is integrable.
4. Therefore the structural problem is to produce such a physical cut with aggregate rank-three currency before taking any reciprocal local minor.

The first implication attacked below is exactly step 4 for **every exact-rank-three ambient matrix**. The new mechanism is a random original-coordinate cut weighted by the entire Pluecker-volume distribution. It does not require a good individual 3x3 minor and does not require the volume-marginal gate `<=1/2` used by a different decoupling theorem.

The full arbitrary-rank target remains open because a higher-rank cross block cannot simply be spectrally truncated to rank three: that would rotate/condition the product coordinates in an unauthorized way. This exact-rank obstruction is the first remaining implication after the theorem below.

## 2. Source-pinned completed inputs actually used

### 2.1 Designated partner fleet02/B04

I use the completed theorem `QFORM-RANKR-TWOSIDED-CONTAMINATION-FOURIER-v1` from

`yspennstate/math-open-problems@8f8913581643a7e7bcbe7d8c178a2255194dfc3d`

at the fleet02/B04 r22 report.

Its exact scope is the one needed here. If two disjoint original-coordinate product banks `X_I,X_J` have physical cross block `B` of exact rank `r>=2`, with nonzero singular values `sigma_1,...,sigma_r` and `Delta=prod sigma_j`, then arbitrary measurable/self-quadratic contamination on both banks is allowed. For `r>=3` it proves

`||p||_infinity <= e r/(r-2) Delta^(-1/r)`.

Thus at `r=3`,

`||p||_infinity <= 3e Delta^(-1/3)`.                              (2.1)

The proof is a joint product-space Fourier/Plancherel estimate, not the refuted one-dimensional pointwise Fresnel claim. At `r=3` its characteristic-function envelope is in `L^1`, so it gives a bounded continuous density.

The newest completed fleet02/B04 comparison, source

`yspennstate/math-open-problems@2f2e25957d3a687bbe89e855661b4a55d477e0cf`,

reinforces the same aggregate-before-inversion principle on a no-pivot Hadamard family: volume and ridge certificates stay uniform while every local pair certificate degenerates. The theorem below implements that principle through a different exact random-cut identity.

### 2.2 Corrections retained

I use none of the refuted interfaces: no law-uniform pointwise quadratic-phase decay; no naive spectral-fiber supremum; no arbitrary-joint coarea theorem; no positive moment of a worst conditional projected-density cap; no post-rotation independence; and no inference that aggregate minor mass forces one dimension-free physical minor.

## 3. Exact rank-three Pluecker volume

Let `A` be real symmetric of exact rank three. Choose a thin spectral factorization

`A = U M U^T`,                                                     (3.1)

where `U` is `n x 3` with orthonormal columns and `M` is an invertible real symmetric `3 x 3` matrix. The three nonzero eigenvalues of `A` are exactly those of `M`.

For every physical triple `S subset [n]`, `|S|=3`, define

`w_S := det(U_S)^2`.                                                (3.2)

Cauchy--Binet gives

`sum_{|S|=3} w_S = det(U^T U)=1`.                                  (3.3)

Thus `(w_S)` is a probability law on physical triples. It is the rank-three projection-volume / fixed-size determinantal distribution associated with the physical spectral frame.

Define its **disjoint collision mass**

`d(U) := sum_{S,T: |S|=|T|=3, S cap T=empty} w_S w_T`.              (3.4)

Equivalently, if `S,T` are two independent triples sampled from `(w_R)`,

`d(U)=P(S cap T=empty)`.                                            (3.5)

This is global aggregate physical-coordinate currency; it does not select one large minor.

## 4. Random-cut identity

For an original-coordinate cut `I sqcup J=[n]`, set

`B_I := A[I,J]=U_I M U_J^T`.                                       (4.1)

Define

`E_3(B_I) := e_3(B_I B_I^T)`.                                      (4.2)

Because `rank(B_I)<=3`, Cauchy--Binet on the third compound gives

`E_3(B_I)
 = sum_{S subset I, T subset J, |S|=|T|=3} det(B_I[S,T])^2`.       (4.3)

For every such `S,T`, the exact rank-three factorization (3.1) gives

`det(B_I[S,T])
 = det(U_S) det(M) det(U_T^T)`,                                    (4.4)

hence

`det(B_I[S,T])^2 = det(M)^2 w_S w_T`.                              (4.5)

Now choose the cut by putting each physical coordinate independently in `I` or `J` with probability `1/2`. For any fixed disjoint ordered pair `(S,T)`, the event `S subset I, T subset J` has probability `2^-6=1/64`; if `S cap T` is nonempty the event is impossible. Therefore

`boxed:
 E_I E_3(B_I) = det(M)^2 d(U)/64.
`                                                                      (4.6)

This identity is exact.

Consequently, whenever `d(U)>0`, there exists a physical cut with

`E_3(B_I) >= det(M)^2 d(U)/64`.                                    (4.7)

Since `rank(B_I)<=3` and `E_3(B_I)>0`, this selected cross block has **exact rank three**. If its nonzero singular values are `sigma_1,sigma_2,sigma_3`, then

`Delta^2=(sigma_1 sigma_2 sigma_3)^2=E_3(B_I)`.                    (4.8)

## 5. Main theorem

### Theorem 5.1 — `QFORM-RANK3-DISJOINT-VOLUME-CUT-v1`

Let `A=UMU^T` be any real symmetric exact-rank-three matrix as in (3.1), and suppose `d(U)>0`. Let `X_i` be arbitrary independent real random variables with densities bounded by one. Then `Q=X^TAX` has a **bounded continuous density** and

`boxed:
 ||p_Q||_infinity
 <= 6e |det M|^(-1/3) d(U)^(-1/6).
`                                                                      (5.1)

If the three nonzero eigenvalues of `A` all have modulus at least one, then `|det M|>=1`, so

`boxed:
 ||p_Q||_infinity <= 6e d(U)^(-1/6).
`                                                                      (5.2)

#### Proof

Choose a cut satisfying (4.7). The full quadratic form can be written exactly as

`Q = X_I^T A[I,I] X_I
    + X_J^T A[J,J] X_J
    + 2 X_I^T B_I X_J`.                                             (5.3)

The two banks are disjoint sets of the original independent coordinates. Thus the designated partner theorem (2.1) applies directly, with *both* self blocks retained as arbitrary contamination. By (4.8),

`||p_Q||_infinity <= 3e E_3(B_I)^(-1/6)`.                          (5.4)

Using (4.7),

`E_3(B_I)^(-1/6)
 <= [64/(det(M)^2 d(U))]^(1/6)
 =2 |det M|^(-1/3)d(U)^(-1/6)`.                                   (5.5)

Substituting into (5.4) proves (5.1). The partner theorem's rank-three characteristic-function bound is integrable, hence the inverse Fourier transform gives a continuous density. If all three nonzero eigenvalues have modulus at least one, `|det M|>=1`, proving (5.2). QED.

**Actual partner-result application.** Equation (5.4), with the cut furnished by (4.7), is the requested direct application of a completed fleet02/B04 result to a new inequality. It is not merely a citation or analogy.

## 6. A leverage-only diffuse corollary

Let

`alpha_i := ||U_{i,*}||_2^2`.                                      (6.1)

For projection-volume sampling, `alpha_i=P(i in S)`. Indeed the one-point inclusion probabilities of the rank-three projection DPP are the diagonal entries of `UU^T`; equivalently this follows by Cauchy--Binet after fixing row `i`. Also

`sum_i alpha_i=3`.                                                  (6.2)

Let `h=max_i alpha_i`. For two independent sampled triples `S,T`,

`E |S cap T| = sum_i alpha_i^2 <= h sum_i alpha_i=3h`.             (6.3)

Since `1_{S cap T != empty} <= |S cap T|`,

`d(U)=P(S cap T=empty) >= 1-3h`.                                  (6.4)

Hence:

### Corollary 6.1 — diffuse exact-rank-three branch

If `h<1/3`, then every exact-rank-three target matrix satisfies

`boxed:
 ||p_Q||_infinity <= 6e (1-3h)^(-1/6),
`                                                                      (6.5)

and the density is continuous.

This threshold is only a sufficient diffuse criterion. The sharper currency is `d(U)` itself, which may be positive (and much larger than `1-3h`) outside the `h<1/3` range.

## 7. Exact collision identity

The aggregate `d(U)` can be computed without enumerating ordered disjoint pairs. Put

`beta_ij := P(i,j in S)=det[(UU^T)_{\{i,j\},\{i,j\}}]`             (7.1)

for `i<j`. Because `K:=|S cap T|` takes values only in `{0,1,2,3}`,

`1_{K=0}=1-K+C(K,2)-C(K,3)`.                                      (7.2)

Taking expectations for independent `S,T` gives the exact identity

`boxed:
 d(U)
 =1-sum_i alpha_i^2
   +sum_{i<j} beta_ij^2
   -sum_{|S|=3} w_S^2.
`                                                                      (7.3)

Indeed `E K=sum alpha_i^2`, `E C(K,2)=sum beta_ij^2`, and `P(S=T)=sum w_S^2`. This identity may be useful in the remaining concentrated/hub regime because it exposes the precise second-order overlap correction that the crude union bound (6.4) discards.

## 8. Fully dense rotated indefinite target example

Take the normalized Sylvester Hadamard matrix `H_16/4`, let `U` be its first three columns, and put

`M=diag(1,1,-1)`,
`A=U M U^T`.                                                        (8.1)

Then:

- `U^T U=I_3`, so `A` has exact nonzero spectrum `{1,1,-1}`;
- every row leverage is `alpha_i=3/16`;
- every entry of `A` is nonzero, in fact belongs to `{-1/16,1/16,3/16}`; hence this is a genuinely dense/non-coordinate-aligned indefinite matrix;
- the sixteen rows of `U` fall into four sign patterns, each repeated four times;
- a triple has nonzero Pluecker weight exactly when it uses three distinct sign patterns;
- there are `4*4^3=256` such triples, each with

  `w_S=1/256`.

For a fixed nonzero triple `S`, the number of nonzero-weight triples `T` disjoint from `S` is

`3^3 + 3*(4*3*3)=27+108=135`.                                     (8.2)

Therefore exactly

`d(U)=135/256`.                                                     (8.3)

The general theorem already gives

`||p_Q||_infinity
 <=6e (135/256)^(-1/6)
 =18.1452698708...`.                                               (8.4)

There is an even cleaner explicit physical cut. Split the first eight and last eight physical coordinates. By the Sylvester recursion, the first three normalized Hadamard columns agree on the two halves, while their restrictions have mutually orthogonal columns of squared norm `1/2`. Hence the `8 x 8` cross block

`B=A[1:8,9:16]`

has exactly three nonzero singular values

`1/2,1/2,1/2`.                                                      (8.5)

Applying the designated fleet02/B04 rank-three theorem directly to this concrete physical cut gives

`boxed:
 ||p_Q||_infinity <= 3e (1/8)^(-1/3)=6e
 =16.3096909708... .
`                                                                      (8.6)

The density is continuous. This is an all-input-law bound for a fully dense rotated indefinite target matrix; no Monte Carlo or centered-interval extremality is involved.

## 9. What this changes and the remaining exact gap

Paid now:

1. Every exact-rank-three target whose two independent Pluecker-volume triples have positive disjointness mass `d(U)` has an explicit product-Fourier `L^infinity` bound (5.2).
2. In particular every exact-rank-three target with maximum spectral-frame row leverage `<1/3` is closed, with continuity.
3. The proof aggregates all third-compound mass *before* choosing a physical cut and never pays a reciprocal individual physical minor.
4. A completed fleet02/B04 theorem is applied at the exact new cut, retaining arbitrary same-bank quadratic contamination.

Not paid:

- a general higher-rank physical cross block may have rank greater than three. The fleet02/B04 theorem then depends on the product of **all** its nonzero singular values; one cannot discard the extra small singular directions after a spectral rotation while retaining original-coordinate independence.
- `d(U)` can vanish or be tiny in concentrated exact-rank-three frames, so (5.1) alone is not an exhaustive exact-rank-three routing theorem. Existing scalar-pivot, pair, ridge and grouped-coordinate branches remain needed there.

The first new unpaid implication is therefore

**`QFORM-HIGHER-RANK-DISJOINT-VOLUME-SMEARING-v1` (OPEN):** starting from an arbitrary unresolved matrix with `s_3(A)>=1`, convert a dimension-free amount of third-compound disjoint physical-cut mass into an `L^1` product-Fourier estimate **without** truncating a higher-rank cross block to spectral rank three and without requiring a good individual physical minor. If that aggregate is too concentrated, route its collision identity / high marginals into the already-paid scalar-pivot, ridge, determinant-star, grouped-hub or two-sided-contamination branches.

This is materially narrower than the previous generic aggregate-to-packet problem: the exact-rank-three Fourier payment is now complete once disjoint Pluecker mass is present. The remaining issue is a higher-rank smearing/concentration interface, not the analytic rank-three product-Fourier estimate itself.

## 10. Status

`full_qform_proved=false`  
`full_target_continuity_proved=false`  
`supporting_branch_continuity_proved=true`  
`counterexample_to_full_target=false`  
`native_brain_ingestion_verified=false`  
`execution_label=WITHOUT_VERIFIED_BRAIN`
