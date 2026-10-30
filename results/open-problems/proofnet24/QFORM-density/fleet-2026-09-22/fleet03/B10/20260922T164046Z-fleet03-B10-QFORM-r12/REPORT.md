# fleet03/B10 — transverse two-null-pivot payment for exact rank three

**Run:** `20260922T164046Z-fleet03-B10-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Rank-three coupled case  
**Status:** supporting theorem proved; full QFORM target **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (repository retrieval/write is not native learned-memory ingestion)

## 1. Target and first unpaid implication

The target in this B10 lane is the exact-rank-three case

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_j(Lambda)|>=1`,

with arbitrary orientation and independent physical coordinates whose densities are bounded by one. Previous B10 work proved the nonisotropic scalar-pivot estimate

`||p_Q||_infinity < 97 [|A_ii| ||u_i||^2 |det Lambda|]^(-1/4)`

when a usable physical diagonal pivot is nonzero. The hard branch is therefore indefinite and near-isotropic/zero-pivot. The live fleet02/B10 cascade construction also shows that boundedly many scalar-pivot peelings cannot solve this branch: an arbitrarily long chain of heavy zero-pivot rows can persist along one null ray.

This run changes mechanism from scalar peeling to a **two-coordinate hyperbolic pivot**. The first missing implication attacked is: if two physical zero-pivot rows are transverse rather than lying on the same null ray, can their original-coordinate product structure pay the rank-one residual without replacing it by an unproved conditional-density surrogate?

The answer is yes, quantitatively.

## 2. Translation-uniform product-density envelope

### Lemma 2.1 — product logarithmic envelope

Let `X,Y` be independent real random variables with probability densities `f,g` satisfying `0<=f,g<=1`. Let `H=XY`, and let `h` denote its density. Then for almost every `w!=0`,

`h(w) <= 2 log(1/|w|)+2`, for `0<|w|<=1`,

and

`h(w) <= 2 |w|^(-1/2)`, for `|w|>=1`.                                     (2.1)

The same bounds hold after arbitrary deterministic translations of `X` and `Y`.

### Proof

For `w!=0`,

`h(w)= integral f(u) g(w/u) du/|u|`.                                      (2.2)

For `0<|w|<=1`, split into `|u|<|w|`, `|w|<=|u|<=1`, and `|u|>1`. On the middle region use only `f,g<=1`, giving

`integral_middle <= 2 log(1/|w|)`.                                        (2.3)

On `|u|>1`, `1/|u|<=1`, hence that contribution is at most `int f<=1`. On `|u|<|w|`, substitute `v=w/u`; then `|v|>1` and the contribution is

`integral_{|v|>1} f(w/v)g(v) dv/|v| <= int g <=1`.                        (2.4)

This proves the first line of (2.1).

For `|w|>=1`, split at `|u|=sqrt(|w|)`. The outer part is at most `|w|^(-1/2) int f`; after the same substitution, the inner part is at most `|w|^(-1/2) int g`. This proves the second line. Translation simply replaces `f,g` by translates, preserving independence, mass and the cap one. QED.

For `a!=0`, the density `k_a` of `2aXY` therefore obeys

`k_a(s) <= |a|^(-1) Phi(s/(2|a|))`,                                      (2.5)

where

`Phi(x)=1+log(1/|x|)` for `0<|x|<=1`,

`Phi(x)=|x|^(-1/2)` for `|x|>=1`.                                        (2.6)

This envelope is uniform under arbitrary translations of both factors.

## 3. A square-ridge averaging lemma with the correct scaling

The elementary one-dimensional quadratic sublevel estimate

`|{z: |A +/- z^2|<R}| <= 4 sqrt(R)`                                      (3.1)

holds for all real `A` and `R>0`.

### Lemma 3.1 — cap-K averaging of the product envelope

Let `G` be any probability density on `R` with `0<=G<=K`. Uniformly in real `A` and either sign,

`integral G(z) Phi(A +/- z^2) dz <= 8 K^(2/3)`.                           (3.2)

### Proof

Let

`m_A(t)=|{z: Phi(A +/- z^2)>t}|`.

For `0<t<1`, the event is contained in `|A +/- z^2|<t^(-2)`, so by (3.1)

`m_A(t)<=4/t`.                                                            (3.3)

For `t>=1`, only the logarithmic branch contributes and

`m_A(t)<=4 exp((1-t)/2)`.                                                 (3.4)

Layer cake and the density/mass constraints give

`integral G Phi <= integral_0^infinity min(1,K m_A(t))dt`.                (3.5)

If `K<=1/4`, (3.3)-(3.4) give exactly

`<=12K+4K log(1/(4K)) <= 8 K^(2/3)`.                                     (3.6)

Indeed, with `x=4K<=1`, the ratio to `K^(2/3)` is

`4^(2/3) x^(1/3)(3+log(1/x))`,

whose maximum on `(0,1]` is `3*4^(2/3)<8`.

If `K>=1/4`, split (3.4) at `t_0=1+2log(4K)`. Then

`integral G Phi <= 1+2log(4K)+2 = 3+2log(4K) <= 8K^(2/3)`,                (3.7)

because with `x=4K>=1`, `4^(2/3)(3+2log x)x^(-2/3)` is decreasing and has value `3*4^(2/3)<8` at `x=1`. QED.

## 4. Product-preserving hyperbolic-pair plus square theorem

I use the standard Ball--Rogozin linear-density consequence already used in the current QFORM proof graph: if `Z_k` are independent with densities at most one and `v` is a Euclidean unit vector, then `T=sum v_k Z_k` has density at most `sqrt(2)`.

### Theorem 4.1 — `QFORM-TRANSLATED-HYPERBOLIC-PAIR-SQUARE-v1`

Let `X,Y,Z_1,...,Z_m` be independent, each with density bounded by one. Let `v in R^m` satisfy `||v||_2=1`, put `T=v dot Z`, and let `alpha(Z), beta(Z)` be arbitrary measurable functions. For `a sigma !=0`, define

`W = 2a (X+alpha(Z))(Y+beta(Z)) + sigma T^2 + c`.                         (4.1)

Then `W` has an essentially bounded density and

`||p_W||_infinity <= 8*2^(2/3) (|a|^2 |sigma|)^(-1/3)
                  < 13 (|a|^2 |sigma|)^(-1/3)`.                          (4.2)

No independence between the translations `(alpha,beta)` and `T` is assumed.

### Proof

Condition on the entire vector `Z=z`. The two translated factors remain independent cap-one variables, so Lemma 2.1 yields, uniformly in `z`,

`p_{W|Z=z}(t) <= |a|^(-1) Phi((t-c-sigma T(z)^2)/(2|a|))`.                (4.3)

Average (4.3) over `Z`. Since the right side depends on `Z` only through `T`, replace the `Z` integral by the genuine marginal law of `T`; no conditional-law surrogate is introduced. Let `M=sqrt(2)` be its density cap and scale

`zeta=sqrt(|sigma|/(2|a|)) T`.

The density of `zeta` has mass one and cap

`K=M sqrt(2|a|/|sigma|)`.                                                (4.4)

Lemma 3.1 therefore gives

`p_W(t) <= (8/|a|) K^(2/3)
         =8*2^(1/3)M^(2/3)|a|^(-2/3)|sigma|^(-1/3)
         =8*2^(2/3)(|a|^2|sigma|)^(-1/3)`.                               (4.5)

This is uniform in `t`, proving (4.2). QED.

The key point is that the translations can depend arbitrarily on the same residual coordinates that create the square. The argument keeps the exact conditional **product** law of the two selected original physical coordinates, rather than replacing it by a bounded conditional scalar density. It therefore avoids the live `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` falsifier.

## 5. Exact-rank-three two-null-pivot theorem

### Theorem 5.1 — `QFORM-RANK3-TRANSVERSE-NULL-PAIR-v1`

Let

`A=U Lambda U^T`, `U^T U=I_3`,

have exact rank three, with `Lambda` invertible. Let `u_i,u_j` be two physical rows satisfying

`A_ii=u_i^T Lambda u_i=0`,
`A_jj=u_j^T Lambda u_j=0`,

and suppose `a=A_ij!=0`. Define the Euclidean Pluecker/wedge mass

`Delta_ij = ||u_i wedge u_j||^2
          = ||u_i||^2 ||u_j||^2-(u_i dot u_j)^2`.                        (5.1)

For independent physical coordinates with densities bounded by one,

`||p_{X^TAX}||_infinity
 <= 8*2^(2/3) [|det Lambda| Delta_ij]^(-1/3)
 < 13 [|det Lambda| Delta_ij]^(-1/3)`.                                   (5.2)

In the target normalization `|lambda_k|>=1`, this is at most

`13 Delta_ij^(-1/3)`.                                                     (5.3)

### Proof

Partition the physical coordinates into `I={i,j}` and its complement, writing

`A=[[B,D],[D^T,C]]`,

where the two-null-pivot hypothesis gives

`B=[[0,a],[a,0]]`.                                                        (5.4)

Thus `B` is invertible. Complete the square in the **two original coordinates**:

`Q=(X_I+B^(-1)DZ)^T B (X_I+B^(-1)DZ) + Z^T S Z`,

`S=C-D^T B^(-1)D`.                                                       (5.5)

Since `rank(A)=3` and `rank(B)=2`, Schur rank additivity gives `rank(S)=1`. Hence

`S=sigma vv^T`                                                           (5.6)

for a Euclidean unit vector `v` and `sigma!=0`. Equation (5.5) is therefore exactly of the form in Theorem 4.1, with the two entries of `B^(-1)DZ` supplying arbitrary translations of `X_i,X_j`.

It remains to identify the scale `|a|^2|sigma|`. Since `det B=-a^2`, for every `k` outside `{i,j}` the Schur determinant identity gives

`det A_{ijk}=det(B) S_kk=-a^2 sigma v_k^2`.                              (5.7)

Summing over `k` and using `sum v_k^2=1`,

`sum_k det A_{ijk}=-a^2 sigma`.                                          (5.8)

On the other hand, exact rank three gives

`det A_{ijk}=det(Lambda) det(U_{ijk})^2`.                                (5.9)

If `w=u_i wedge u_j`, then `det(U_{ijk})=w dot u_k`; since `U^T U=I_3`,

`sum_k det(U_{ijk})^2
 = w^T (sum_k u_k u_k^T) w
 = ||w||^2
 = Delta_ij`.                                                            (5.10)

Combining (5.8)-(5.10),

`-a^2 sigma = det(Lambda) Delta_ij`,                                     (5.11)

and hence

`|a|^2 |sigma|=|det Lambda| Delta_ij`.                                   (5.12)

Insert (5.12) into Theorem 4.1. QED.

This is an exact original-coordinate result. No spectral coordinate is declared independent, and no projected conditional density is used as a substitute for product provenance.

## 6. Quantitative consequence for the zero/near-isotropic obstruction

Theorem 5.1 proves a clean "departure from a null ray is paid" statement. For example, if two exact zero-pivot rows satisfy

`Delta_ij >= 1/64`,

then under the target eigenvalue normalization

`||p_Q||_infinity < 13*4 = 52`.                                         (6.1)

More generally a hypothetical hard zero-pivot cascade in which this branch does not fire at threshold `eta` must have

`Delta_ij<eta`

for every selected pair to which the cascade argument is applied. Thus the surviving heavy zero-pivot rows are quantitatively forced toward a common Euclidean ray; this is precisely the geometry exhibited by the fleet02/B10 arbitrarily-long null-ray construction. The local obstruction is no longer "zero scalar pivots" by itself; it is **high-cardinality near-collinearity along a null ray**, which must be aggregated as a bank.

## 7. Completed fleet04 mathematics applied to an actual local inequality

The exact assigned partner `fleet04/B10` still had no completed current-QFORM handoff in the fresh repository search for this run, so none is fabricated. A completed compatible result from the same account is fleet04/B18, canonical source

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

which proves for a physical `3x3` block `B_3=[[d,b^T],[b,C]]` with `d!=0` and **definite** Schur complement

`||p_Q||_infinity <= 2 sqrt(pi) [|d det B_3|]^(-1/4)`.                   (7.1)

Apply it together with Theorem 5.1 at a common scale `eta>0`:

* if a nonzero scalar pivot/definite-Schur triple has `|d det B_3|>=eta^4`, (7.1) gives `||p_Q||_infinity<=2sqrt(pi) eta^(-1)`;
* if instead a transverse zero-pivot pair has `|det Lambda| Delta_ij>=eta^3`, Theorem 5.1 gives `||p_Q||_infinity<13 eta^(-1)`.

Therefore on the union of these two genuinely different local gates,

`||p_Q||_infinity < 13 eta^(-1)`.                                       (7.2)

This is the compatible partner inequality actually used in the present rank-three reduction. The remaining branch is neither a definite-Schur branch nor a transverse-null-pair branch: it is a near-isotropic, near-null-ray aggregate branch.

## 8. Scope, continuity, and remaining implication

**Proved here:** an essentially bounded density under the translated-hyperbolic-pair-plus-rank-one-square hypothesis, and its exact-rank-three transverse two-null-pivot corollary with explicit determinant/Pluecker scale.

**Not proved here:** continuity of the density. The argument gives existence and an essential `L^infinity` bound; arbitrary input densities need not be continuous, so continuity requires a separate argument.

**Full QFORM remains OPEN.** The first unpaid B10 implication is now sharper:

> `QFORM-NULL-RAY-BANK-AGGREGATION-v1`: in the indefinite exact-rank-three branch where all useful scalar pivots are tiny/zero and all heavy zero-pivot rows have small pairwise wedge mass, aggregate the whole near-null-ray bank before paying the transverse directions. Departure from the ray is now quantitatively paid by Theorem 5.1; exact collinear-ray examples are already paid by existing three-bank cross-square theorems. What remains is a stable near-ray aggregation theorem connecting those two endpoints.

This mechanism is deliberately different from repeated scalar-pivot peeling, which the live cascade falsifier rules out as a finite-step universal strategy.

No pointwise law-uniform oscillatory decay, naive fiber supremum, post-rotation independence, Gaussian/log-concave/moment/support assumption, Monte Carlo evidence, or conditional-cap surrogate is used.
