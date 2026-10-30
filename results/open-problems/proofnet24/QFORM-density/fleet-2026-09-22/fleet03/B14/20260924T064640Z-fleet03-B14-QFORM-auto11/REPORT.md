SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-24T06:46:40Z.
attacking: exact cap-saturation localization by product-preserving diagonal congruence, preserving the three-eigenvalue threshold and the entire quadratic output law.

# fleet03/B14 — cap-saturation congruence localization

Run: `20260924T064640Z-fleet03-B14-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: translations and localization  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full unrestricted QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.

## 1. Scope and correction discipline

The exact owner target is unchanged. The inputs are independent real coordinates with probability densities `0<=f_i<=1`; the real symmetric matrix has at least three eigenvalues of absolute value at least one. No Gaussianity, moments, log-concavity, compactness, connected support or spectral-coordinate independence is used.

This run consumes the live corrections excluding law-uniform pointwise quadratic-phase decay, projection-only indefinite pushforward control, naive fiber-sup bounds, bounded-diameter localization, fixed-fragment-count localization, the false arbitrary-joint coarea gate, the false conditional-projection positive-moment gate, and the false opposite-sign arbitrary-remainder slope rescue. The proof below is an exact original-coordinate change of scale; it uses none of those interfaces.

The completed designated-partner result actually applied is fleet04/B14 r10:

- source: `yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T001624Z-fleet04-B14-scaled-schur-localization-r10/REPORT.md`;
- theorem: if an original-coordinate `3 x 3` principal block `B` is invertible and `sigma=min_j |lambda_j(B)|`, then `||p_Q||_(infinity,ess)<=6 sqrt(pi)/sigma`, uniformly over all outside curvature, cross-couplings, affine leakage, tails and fragments.

A visible-corpus source search for the present exact `L^infinity`-cap saturation by diagonal congruence found no matching QFORM theorem. The earlier fleet01/B15 exact affine-homogenization theorem and this slot's prior compactification/quantile-gauge theorems are source-matched dependencies/cousins, not relabelled here.

## 2. Spectral threshold monotonicity under expansive congruence

For a real symmetric matrix `A` and `t>0`, write

`N_+(A;t)=#{j: lambda_j(A)>=t}`,

`N_-(A;t)=#{j: lambda_j(A)<=-t}`.

### Lemma 2.1 — expansive congruence cannot lose protected signed eigenvalues

Let `S` be real symmetric positive definite with `S>=I` in Loewner order, and put

`B=S A S`.

Then for every `t>0`,

`N_+(B;t)>=N_+(A;t)`,

`N_-(B;t)>=N_-(A;t)`.

#### Proof

Let `E_+` be the spectral subspace of `A` spanned by eigenvectors with eigenvalues at least `t`; put `k=dim E_+=N_+(A;t)`. For every `y in E_+`,

`y^T A y >= t ||y||_2^2`.

Set `F_+=S^{-1}E_+`. This is a `k`-dimensional subspace. If `x in F_+` and `y=Sx`, then

`x^T B x = y^T A y >= t ||y||_2^2 >= t ||x||_2^2`,

because `S>=I` implies `||Sx||_2>=||x||_2`. By the Courant-Fischer variational characterization, `B` has at least `k` eigenvalues at least `t`.

For the negative subspace `E_-`, every `y in E_-` satisfies

`y^T A y <= -t ||y||_2^2`.

On `F_-=S^{-1}E_-`,

`x^T B x <= -t ||Sx||_2^2 <= -t ||x||_2^2`.

The negative Courant-Fischer characterization gives at least `dim E_-=N_-(A;t)` eigenvalues of `B` at most `-t`. QED.

### Corollary 2.2

For every `t>0`, the number of eigenvalues of `SAS` with modulus at least `t` is at least the corresponding number for `A`.

This is a signed-threshold statement, not an assertion that individual eigenvalues can be paired monotonically across an indefinite congruence.

## 3. Exact cap-saturation theorem

### Theorem 3.1 — `QFORM-CAP-SATURATION-CONGRUENCE-LOCALIZATION-v1`

Let `X=(X_1,...,X_n)` have independent probability densities `f_i` satisfying `0<=f_i<=1`, and let `A` be any owner-target matrix. Define

`k_i=||f_i||_(infinity,ess)`.

Then `0<k_i<=1`. Put

`D=diag(k_1,...,k_n)`,

`Y=D X`,

`B=D^{-1} A D^{-1}`.

Then:

1. the `Y_i` remain independent probability variables;
2. their densities

   `g_i(y)=k_i^{-1} f_i(y/k_i)`

   satisfy `||g_i||_(infinity,ess)=1` exactly;
3. `B` has at least as many eigenvalues `>=1` and at least as many eigenvalues `<=-1` as `A`, hence is again an owner-target matrix;
4. there is exact samplewise equality

   `X^T A X = Y^T B Y`.

Consequently the full quadratic output law is unchanged, not merely approximated.

#### Proof

A probability density cannot have essential supremum zero, so every `k_i` is strictly positive. Coordinatewise deterministic scaling preserves independence. The density transformation formula gives `g_i` and

`||g_i||_infinity=k_i^{-1}||f_i||_infinity=1`.

Since every `k_i<=1`, the diagonal matrix `S=D^{-1}` satisfies `S>=I`. Therefore Lemma 2.1 at `t=1` shows that the positive and negative protected eigenvalue counts of

`B=SAS`

are each no smaller than those of `A`. Finally `X=D^{-1}Y`, giving

`X^T A X=Y^T D^{-1}AD^{-1}Y=Y^T B Y`.

No limiting argument occurs. QED.

## 4. Sharp-constant equality and localization consequences

Let `C_cap<=1` be the extended optimal interval-density constant over the full owner target, and let `C_cap=1` be the same supremum restricted to product sources satisfying

`||f_i||_(infinity,ess)=1`

for every coordinate.

### Corollary 4.1 — exact saturation of all marginal caps

`C_cap<=1 = C_cap=1`, including the value `+infinity`.

The inequality `C_cap=1<=C_cap<=1` is trivial because the saturated class is a subclass. The reverse inequality follows instance by instance from Theorem 3.1: every admissible unsaturated instance is represented by a saturated owner-target instance with the identical output law.

This reduction has zero tax for arbitrary deterministic translations of source supports, arbitrarily distant fragments, unbounded support, tails and all moments. It introduces no centering and no support geometry assumption. It also preserves every output-law property exactly. In particular, if the owner’s additional continuous-density conclusion is eventually proved on the saturated source class, it transfers to the original full class with no separate approximation argument.

### Corollary 4.2 — combined legal core

Combining this exact cap saturation with the already source-pinned exact affine closure and the earlier B14 quantile gauge, the height problem may, if useful, be attacked on source laws whose marginal caps are exactly one and whose chosen fixed quantiles are zero, provided arbitrary deterministic affine leakage is retained. This is only a gauge reduction; it does not assert centered or interval laws are extremal.

## 5. Cap-aware physical-triple inequality from fleet04/B14

The same scaling gives a concrete strengthening of the designated partner theorem.

Let `J={i_1,i_2,i_3}` be an original-coordinate triple for which the principal block

`B_0=A_{J,J}`

is invertible. Let

`K=diag(k_{i_1},k_{i_2},k_{i_3})`,

where `k_i=||f_i||_infinity`. Scale only these three coordinates by their caps and leave all outside coordinates unchanged. The new physical principal block is

`B_cap=K^{-1} B_0 K^{-1}`.

The selected input coordinates now have cap exactly one, the outside coordinates still have cap at most one, and the quadratic output is unchanged. Applying fleet04/B14 r10 gives the actual inequality

`boxed{
||p_Q||_(infinity,ess)
 <= 6 sqrt(pi) / sigma_min(B_cap).
}`

Moreover, if `sigma_0=min_j |lambda_j(B_0)|`, then Lemma 2.1 applied at `t=sigma_0` inside the three-dimensional block gives

`sigma_min(B_cap)>=sigma_0`.

Thus using the actual marginal caps can only improve, never worsen, the partner’s physical-triple certificate.

## 6. Concrete owner-target chamber and exact computation

Take the dense reflection

`B_* = I_3-(2/3) 11^T
     = [[1/3,-2/3,-2/3],
        [-2/3,1/3,-2/3],
        [-2/3,-2/3,1/3]]`.

Its spectrum is `{1,1,-1}`, so every ambient symmetric extension having `B_*` as this physical principal block is an actual owner-target matrix by interlacing.

Take first and second marginals with exact density caps `1/2` (for example `Uniform[0,2]`) and the third with cap `1`. Put

`K=diag(1/2,1/2,1)`, `S=K^{-1}=diag(2,2,1)`.

Then

`B_cap=S B_* S
 = [[4/3,-8/3,-4/3],
    [-8/3,4/3,-4/3],
    [-4/3,-4/3,1/3]]`.

The vector `(1,-1,0)` has eigenvalue `4`; on the complementary symmetric plane the remaining eigenvalues solve

`lambda^2+lambda-4=0`.

Hence

`spec(B_cap)={4,(-1+sqrt(17))/2,(-1-sqrt(17))/2}`

and

`sigma_min(B_cap)=(sqrt(17)-1)/2`.

The designated partner theorem therefore yields

`boxed{
||p_Q||_(infinity,ess)
 <= 12 sqrt(pi)/(sqrt(17)-1)
 = 6.810351221041301... .
}`

This is a strict improvement over the unscaled r10 certificate `6 sqrt(pi)=10.6347231054...` on the same physical matrix. All outside curvature, cross-couplings, translations, fragments and unbounded outside laws remain arbitrary because r10 already handles them.

## 7. Status and next implication

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. The full continuous-density conclusion also remains open globally.

What is now paid exactly is **slack in the marginal density caps**: a proof never needs a separate branch for `||f_i||_infinity<1`. One may saturate every cap to exactly one by a product-preserving coordinate scaling, while the three protected signed eigenvalue counts can only improve and the output law is identical.

The unresolved B14/full-fleet obstruction is still structural matrix/product geometry near delocalized or vanishing physical pivots. This theorem does not create a uniformly conditioned physical triple and does not make rotations preserve independence. A useful successor is to combine the cap-weighted congruence with grouped product projections: whenever aggregation produces independent bank variables whose density caps are substantially below one, saturate those caps before paying any reciprocal Schur scale, and test whether the resulting congruence compensates the punctured-hub/near-coloop loss from the live correction ledger.
