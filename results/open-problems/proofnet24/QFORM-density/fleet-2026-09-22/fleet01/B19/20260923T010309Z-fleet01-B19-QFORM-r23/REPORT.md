SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T01:03:09Z.
attacking: the first product-provenance payment inside the robust O3 2+1 grouped block, plus a correction-safe global synthesis with the designated fleet02/B19 N3 routing.

# fleet01/B19 r23 — null-scalar payment and diffuse/heavy-row dichotomy for the robust 2+1 grouped block

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Owner control consumed:** revision `2026-09-22.15`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING TARGET-LEVEL THEOREMS / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (repository transport only; no authenticated native receiver use).

## 1. Sources and correction boundary

Fresh main control was read before the run. QFORM remains the sole research target. The full statement remains open: independent real coordinates with marginal densities at most one, symmetric `A`, and at least three eigenvalues of modulus at least one; prove one dimension- and law-uniform finite essential density bound for `X^T A X`. Continuity remains a separate debt.

Named other-account mathematics actually used:

1. **Designated partner fleet02/B19 r22**, late-corrected canonical mathematics `yspennstate/math-open-problems@34d46a5906078d3c91ca4932f246885b53238ae6`. Its robust dense-twist statements pay an actual leaf-bank branch: if `A_LL=D+B0+E`, `rank(B0)<=r`, and some disjoint physical cut has `s_{r+5}(E[I,J])>=gamma`, then the completed D5 theorem gives

   `||p_Q||_infinity <= 5 sqrt(2e) / gamma`.

   In particular `gamma=1/64` gives `<746.127`. Its late correction explicitly forbids inferring such a singular-value resource merely from aggregate E2/E3/E5 currencies, and forbids localizing the remaining N3 geometry to one physical square/pair before aggregation.

2. **fleet03/B19 r20**, canonical `yspennstate/math-open-problems@0a3018cb14b94787c8f3f8d95a0e292ed230f8e0`. In the exactly-one-internal-rank-two O3 survivor it proves a robust product-preserving 2+1 grouped block. There are disjoint original-coordinate banks `H` and `G`, with `H` rank-one in spectral space and `G` rank two, such that after normalization

   `L=[sqrt(lambda) v, W]`,

   `L L^T = I - lambda_b v_b v_b^T`,

   and

   `det(L)^2 = 1-lambda_b > 1/6`.

   The internal bank has frame eigenvalues `1,tau` with `tau>1/3`. The ambient exact-rank-three spectral matrix `M` satisfies `s_min(M)>=1`.

3. **fleet02/B06 weighted affine-fiber BL theorem**, canonical source commit `8dd33c1abd4fd64140f59032feda2b13d4351da5`: a `k`-dimensional orthogonal projection of the original product law has density cap at most `exp(k/2)`. I use it only before nonlinear operations: cap `sqrt(e)` in dimension one and cap `e` in dimension two.

4. Own predecessor `QFORM-INDEPENDENT-LINEAR-SQUARE-SMOOTHING-v1`, canonical `yspennstate/math-open-problems@09bb706f11ea00995a61f0c7323bf67997c65932`.

No step below uses arbitrary-joint rank-three coarea, a positive moment of a conditional projection density, post-rotation independence, a fixed good physical minor, deletion of small coefficients, or the false implication from aggregate determinant mass to robust singular directions.

## 2. Product representation of the fleet03/B19 r20 grouped block

Because the spectral rows in `H` are collinear, write them as `u_i=alpha_i v` with

`sum_(i in H) alpha_i^2=lambda`.

Define the normalized scalar aggregate

`S=lambda^(-1/2) sum_(i in H) alpha_i X_i`.

Its coefficient vector has Euclidean norm one, so the weighted affine-fiber theorem gives

`||p_S||_infinity <= sqrt(e)`.                                      (2.1)

For the internal bank, let `U_G` be the `3 x |G|` matrix with columns the spectral rows and choose full-column-rank `W` with

`W W^T = U_G U_G^T`.

Set

`R=(W^T W)^(-1) W^T U_G`.

Then

`U_G=W R`, `R R^T=I_2`.                                             (2.2)

Thus

`Y=R X_G in R^2`

is a genuine two-dimensional orthogonal projection of the original independent coordinates in `G`, and

`||p_Y||_infinity <= e`.                                            (2.3)

Since `H` and `G` are disjoint original-coordinate banks, `S` and `Y` are genuinely independent. This is the provenance that will be spent below.

Condition on every original coordinate outside `H union G`. The remaining quadratic form has arbitrary affine and constant terms, but its quadratic core is

`(S,Y)^T K (S,Y)`,  `K=L^T M L`.                                  (2.4)

The outside conditioning does not change (2.1)-(2.3).

Because `L L^T=I-lambda_b v_bv_b^T`, its squared singular values are

`1,1,1-lambda_b`.

Hence

`s_min(L)^2=1-lambda_b=det(L)^2>1/6`.                              (2.5)

Therefore

`s_min(K) >= s_min(L)^2 s_min(M) > 1/6`,                           (2.6)

and

`|det K|=det(L)^2 |det M| > 1/6`.                                 (2.7)

These estimates are sign-free: `M` and `K` may have any nondegenerate real symmetric signature.

## 3. A cap-scaled version of the independent linear-square theorem

### Lemma 3.1 — `QFORM-INDEPENDENT-LINEAR-SQUARE-SMOOTHING-CAPS-v1`

Let `X` be independent of a pair `(Y,Z)`. Assume

`||p_X||_infinity <= L`, `||p_(Y,Z)||_infinity <= H`.

For arbitrary real affine terms, arbitrary `d,g`, and `sf!=0`, the random variable

`T=2sXY+dY^2+2gYZ+fZ^2 + (arbitrary affine/constant terms)`

has an essentially bounded density and

`boxed: ||p_T||_infinity <= 6 H^(2/3) L^(2/3) |s^2 f|^(-1/3).`       (3.1)

#### Proof

Put `X'=L X`. Then `p_(X')<=1`, and the coefficient of `X'Y` is `s/L`. Translations remove the affine term in `X` by translating `Y`; a determinant-one affine shear/translation in the `(Y,Z)` plane completes the square in `Z` and removes `YZ`; the pair density cap remains `H`, and independence from `X'` remains exact. A final translation of `X'` absorbs the remaining linear `Y` term. The predecessor theorem applies with `s/L` in place of `s`, giving

`6 H^(2/3) |(s/L)^2 f|^(-1/3)`,

which is (3.1). No moment or support assumption is used. QED.

## 4. New target-level payment: exact-null scalar side of the robust 2+1 block

### Theorem 4.1 — `QFORM-O3-ROBUST-2PLUS1-NULLSCALAR-PAYMENT-v1`

In the fleet03/B19 r20 robust grouped state, let

`a=K_11=lambda v^T M v`.

If

`a=0`,                                                               (4.1)

then the full target quadratic form, including all conditioned outside variables and all induced affine terms, has

`boxed: ||p_Q||_infinity < 6 e 6^(1/3) < 29.637.`                    (4.2)

This holds for every sign pattern of `M`, every dimension of the original source banks, and every independent marginal law with density at most one.

#### Proof

Write

`K=[[0,b^T],[b,C]]`.

Equation (2.7) implies `b!=0`. Rotate only the two-dimensional grouped coordinate `Y` by an orthogonal matrix `O` sending `b` to `(s,0)`. This does **not** assert independence of the two rotated coordinates; it only preserves their joint density cap `e`, and the whole rotated pair remains independent of `S` because the source banks are disjoint.

In those coordinates the quadratic core is

`2s S Y_1 + dY_1^2 + 2gY_1Y_2 + fY_2^2`.

Its determinant is

`det K = -s^2 f`,                                                    (4.3)

so by (2.7)

`|s^2 f|>1/6`.                                                       (4.4)

Apply Lemma 3.1 with `L=sqrt(e)` and `H=e`. Uniformly in the affine terms generated by the conditioned outside coordinates,

`||p_Q||_infinity
 <= 6 e^(2/3) e^(1/3) |det K|^(-1/3)
 < 6 e 6^(1/3)
 = 29.6366753256... .`                                               (4.5)

The conditional bound is uniform, so averaging over the outside coordinates preserves it. QED.

### What this pays

The r20 debt `QFORM-O3-ROBUST-2PLUS1-GROUPED-PAYMENT-v1` is now closed on the exact-null hypersurface of the rank-one aggregate scalar bank. This is strictly more general than the previous exact null-*physical-coloop* result: `S` may be a genuinely diffuse normalized sum of many original coordinates. The proof uses its true one-dimensional product projection density cap rather than pretending it is an original coordinate.

## 5. New structural dichotomy for the same robust grouped block

There is a second useful consequence of (2.5)-(2.7) that attacks the remaining nonzero-scalar chamber without choosing a reciprocal tiny minor.

Let `R_0` be the original-coordinate coefficient matrix for `(S,Y)`. Explicitly, on the disjoint banks it is block diagonal between the unit coefficient vector defining `S` and the two orthonormal rows defining `Y`. Hence

`R_0^T R_0=I_3`.                                                     (5.1)

The active quadratic core is

`A_0=R_0 K R_0^T`.                                                   (5.2)

Let `ell_i=||(R_0)_{i,*}||^2` be its spectral row leverage.

### Theorem 5.1 — `QFORM-O3-ROBUST-2PLUS1-DIFFUSE-OR-FIXEDROW-v1`

For every robust r20 grouped block, one of the following holds.

**Diffuse alternative.** If `max_i ell_i<=1/12`, then, uniformly in arbitrary affine terms,

`boxed: ||p_Q||_infinity <=144.`                                    (5.3)

**Heavy-row alternative.** Otherwise there is an original physical coordinate `i` in `H union G` for which the complete principal-triple determinant packet of the active core satisfies

`boxed: sum_(j<k; j,k != i) |det A_0[{i,j,k}]| > 1/72.`              (5.4)

#### Proof of the diffuse alternative

By (2.6), the three nonzero eigenvalues of `6A_0` have modulus greater than one, while its spectral row leverages are still `ell_i`. The completed theorem `QFORM-DIFFUSE-RANK3-C24-v1` therefore gives density at most `24` for `6` times the active quadratic form; its underlying cross-block theorem explicitly allows arbitrary linear and constant terms. Scaling the output back by six gives (5.3). Conditioning and averaging over coordinates outside the active banks preserve the bound.

#### Proof of the heavy-row alternative

For every physical triple `T`, exact rank three and (5.1) give

`det A_0[T,T] = det(K) det(R_0[T,:])^2`.                             (5.5)

Fix `i`. The fixed-row Cauchy--Binet identity is

`sum_(j<k; j,k != i) det(R_0[{i,j,k},:])^2 = ell_i`.                (5.6)

For completeness, rotate the three spectral columns so the `i`th row is `(sqrt(ell_i),0,0)`. The left side becomes `ell_i` times the sum of squares of all `2x2` minors formed from columns two and three of the remaining rows; ordinary Cauchy--Binet makes that latter sum one because the columns remain orthonormal and the `i`th row has zero entries in them.

Taking absolute values in (5.5), summing, and using (2.7) yields

`sum_(j<k) |det A_0[{i,j,k}]|
 = |det K| ell_i
 > (1/6)(1/12)=1/72`                                                 (5.7)

whenever `ell_i>1/12`. QED.

The point of (5.4) is **not** that one physical triple is uniformly good; that implication is forbidden and can lose dimension. Instead, the full constant packet is pinned to one fixed physical row. The next transducer may aggregate over the remaining pair indices while retaining that row as a genuine original-coordinate source.

## 6. Application of the designated fleet02/B19 result to an actual global inequality

The latest designated partner r22 closes a real N3 leaf, not merely a structural possibility. If a no-pivot mixed-hub decomposition has

`A_LL=D+B0+E`, `rank(B0)<=r`,

and there is a disjoint original-coordinate cut with

`s_(r+5)(E[I,J])>=1/64`,

then directly

`boxed: ||p_Q||_infinity <= 320 sqrt(2e) < 746.127.`                  (6.1)

This remains valid with arbitrary hub/self blocks, arbitrary signs, arbitrary affine terms and arbitrary independent cap-one laws. Thus any global N3 survivor after consuming r22 must avoid this robust high-cross-rank alternative. The r22 late correction is retained: aggregate E2/E3/E5 mass alone is not silently upgraded to (6.1).

## 7. Compact conditional end-to-end proof map

A correction-safe full proof can now be written conditionally as follows.

1. Existing diagonal, physical-pivot, sequential two-pivot/third-source, ridge-diffuse, exact-cross-rank at least three, D'/D5, null-coloop, and several grouped O3 branches supply uniform bounds at their stated hypotheses.
2. The designated fleet02/B19 r22 theorem pays every N3 dense-twist leaf with a genuine high enough fifth (or diffuse third) cross singular direction; hence the global no-pivot residue is the low-cross-rank / clustered-co-heavy mixed-hub chamber, not the already-refuted fantasy of extracting one universal local minor.
3. In the exact-rank-three O3 terminal chamber, fleet03/B19 r20 forces the robust 2+1 grouped block. Theorem 4.1 now pays its exact-null scalar boundary with `<29.637`. Theorem 5.1 pays every diffuse grouped frame with `<=144`; every remaining state has a fixed physical row carrying `>1/72` aggregate principal-triple mass.
4. Therefore a full proof would follow from two still-unpaid transducers: (i) the global `QFORM-N3-v1` low-cross-rank/co-heavy aggregation/repartition theorem for arbitrary additional spectrum, and (ii) in the r20 grouped terminal chamber, a **nonzero-small scalar / fixed-heavy-row aggregate transducer** that spends (5.4) without selecting a single tiny pair minor, or repartitions into an already-paid pivot/ridge/cross-bank branch.

The first global missing implication remains the partner-identified `QFORM-N3-v1`. The first missing implication inside the robust 2+1 exact-rank-three terminal is sharpened to

`QFORM-O3-2PLUS1-NONZERO-SCALAR-FIXEDROW-TRANSDUCER-v1`:

> assume the r20 robust grouped block, `K_11 !=0`, `max ell_i>1/12`, and hence a fixed physical row with total principal-triple packet `>1/72`; prove a universal density bound while aggregating the remaining pair packet before any reciprocal-minor operation, or force a completed heavy-coordinate, sequential-pivot, ridge, rank-three-cross, or determinant-pair certificate.

This is materially narrower than the previous entire grouped-payment debt. The exact-null interface and the diffuse source-frame chamber are no longer part of that residual.

## 8. Outcome and continuity

**Outcome:** `ESSENTIAL_STEP_APPLIED`.  
**Full target:** `OPEN / NOT PROVED / NOT DISPROVED`.  
**Continuity:** The diffuse branch inherits continuity from the cross-block Fourier theorem. The new null-scalar smoothing proof establishes essential boundedness; continuity is not claimed from that argument alone.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.
