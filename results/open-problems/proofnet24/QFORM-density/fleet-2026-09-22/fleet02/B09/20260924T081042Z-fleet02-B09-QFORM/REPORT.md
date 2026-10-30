SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-24T08:10:42Z.
attacking: near-singular physical-pair interpolation through a determinant-one hub-only shear, keeping the sheared hubs correlated but jointly cap-one and spending a source-coordinate mixed frame before any reciprocal pair determinant.

# fleet02/B09 — joint-hub mixed-frame bridge across a near-singular definite pair

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid obstructions  
Partner: fleet03/B09  
Status: **NEW SUPPORTING THEOREM + TARGET-VALID NEAR-SINGULAR BRIDGE / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN` unless native learned-memory receiver use is separately verified.

All stochastic source coordinates are arbitrary independent real variables with probability densities at most one. No moments, bounded support, connected support, log-concavity, iid hypothesis, law-uniform pointwise quadratic decay, or post-rotation independence is used. The only non-product coordinates introduced below are a determinant-one shear *inside a two-coordinate hub bank*; their **joint** density cap is tracked exactly and independence is never asserted.

## 1. First unpaid implication

The latest designated fleet03/B09 r46 closes the **exact singular** physical-pair face by the polynomial star theorem, while explicitly leaving the punctured near-singular definite pair

`delta X_q^2 + 2 X_q <g,X_R> + W(X_R)`

unpaid when `delta=det(B)/a !=0` tends to zero and `W` is arbitrary on the same active bank.

This run pays the near-singular coefficient uniformly on a substantial mixed-frame subbranch. The first unpaid implication is therefore sharpened to

**`QFORM-NEARSINGULAR-GENERAL-CURVATURE-COMPILER-v1`.**  
After a hub-only determinant-one square-completion shear, if the active leaf curvature is low-rank-plus-diagonal and the resulting mixed frame is diffuse, the density bound is uniform in the Schur coefficient all the way through `delta=0`. What remains is to route **general same-bank curvature** into such a mixed frame, a grouped-crossing/volume receiver, or a bounded physical core without deleting `delta X_q^2`, taking a worst conditional projection-density supremum, or treating a small matrix norm as a small random perturbation.

So the small scalar `delta` is not itself the analytic obstruction in the mixed-frame chamber; structural compilation of the active leaf curvature is.

## 2. Required source refresh and completed input

The pinned completed source at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was reread at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The relevant proved result is Theorem H. In its notation, for hubs `H`, leaves `I`, and conditioned coordinates `J`, if

`A_II = sum_{k=1}^r lambda_k v_k v_k^T + D`

with `D` diagonal, and the mixed rows

`rho_i=((v_k)_i ; A_{ih}, h in H)`

have Gram `G=sum_i rho_i rho_i^T>0` and normalized leverages at most `1/2`, then

`|phi_Q(t)| <= (2|t|)^(-|H|)
                prod_k (4 pi |t lambda_k|)^(-1/2)
                (4 pi)^(r+|H|) det(G)^(-1/2)`.

The blocks `A_HH,A_HJ,A_IJ,A_JJ` are arbitrary. The current master copy retains this exact Theorem-H mechanism and adds later continuations, but does not invalidate it. The pinned and current counterexample searches report no valid counterexample to the unrestricted conjecture.

The key proof line for this run is that the hub laws are used only before the substitution `y=2t x_H`, through the pointwise cap on their density; the later Brascamp--Lieb step is entirely on the original product leaf bank.

## 3. New analytic lemma — joint-hub extension of Theorem H

### Theorem 3.1 — `QFORM-JOINT-HUB-CAP-MIXEDFRAME-v1`

Let the hub vector `Z_H in R^h` have an arbitrary joint probability density `F_H` with

`||F_H||_infinity <= M`,

and suppose `Z_H` is independent of the original-coordinate product leaf bank `X_I` and of the coordinates that are conditioned away. Assume the same leaf hypotheses and mixed frame as pinned Theorem H:

`A_II=sum_{k=1}^r lambda_k v_k v_k^T + D`,

`D` diagonal, `lambda_k !=0`,

`rho_i=((v_k)_i ; A_{ih}, h in H)`,

`G=sum_i rho_i rho_i^T>0`,

`rho_i^T G^(-1) rho_i <=1/2` for every `i in I`.

Then, with arbitrary hub core, arbitrary hub/outside and leaf/outside couplings, arbitrary outside curvature, and arbitrary affine terms,

`|phi_Q(t)| <= M (2|t|)^(-h)
                prod_k (4 pi |t lambda_k|)^(-1/2)
                (4 pi)^(r+h) det(G)^(-1/2)`.                 (3.1)

Let

`alpha=h+r/2`.

If `alpha>1`, put

`K=M 2^(-h) (4 pi)^alpha
      (prod_k |lambda_k|)^(-1/2) det(G)^(-1/2)`.

Then

`|phi_Q(t)| <= min(1,K|t|^(-alpha))`,

so `phi_Q in L^1`, the law has a continuous density, and

`boxed:
 ||p_Q||_infinity <= [alpha/(pi(alpha-1))] K^(1/alpha).
`                                                               (3.2)

The same coefficient gives `P{Q in L}<=C|L|` for every interval `L`.

### Proof

Condition on the outside bank `J`. All `J`-dependence becomes fixed affine terms and phases. For fixed hub value `z`, let `Phi_I(t;2A_IH z+ell)` be the leaf expectation. The hub-only phase has modulus one. Therefore

`|phi_Q(t)|
 <= int F_H(z) |Phi_I(t;2A_IH z+ell)| dz
 <= M int |Phi_I(t;2A_IH z+ell)| dz`.                           (3.3)

Now substitute `y=2t z`. This produces exactly the pinned Jacobian `(2|t|)^(-h)`. Apply the pinned Fresnel linearisation to the `r` leaf squares. The remaining expectation is still over the **original independent leaf coordinates**, with only diagonal quadratic twists and linear frequencies. Thus the same geometric Brascamp--Lieb argument and the same cap-one `L^p` Fourier lemma apply verbatim, giving the factor

`(4 pi)^(r+h) det(G)^(-1/2)`.

This proves (3.1). Integrating `min(1,K|t|^(-alpha))` gives

`int_R min(1,K|t|^(-alpha)) dt
 = 2 alpha/(alpha-1) K^(1/alpha)`,

and Fourier inversion gives (3.2). QED.

### Scope warning

This theorem does **not** justify a shear mixing a hub with leaf coordinates. If the new hub is `X_h+q(X_I)`, its density multiplier depends on the active leaf vector and destroys the factorisation needed for the leaf Brascamp--Lieb step. The valid transformation below acts only within the finite hub bank, so the sheared hub vector remains independent of the leaf bank as a vector and its joint density cap is explicit.

## 4. Determinant-one pair completion is legal at the joint-hub level

### Corollary 4.1 — `QFORM-PAIR-SHEAR-MIXEDFRAME-DELTAFREE-v1`

Let two **original independent** cap-one hub coordinates be `(X_p,X_q)` and let their physical core be

`B=[[a,c],[c,b]]`, with `a!=0`.

Write their leaf coupling vectors as `h_p,h_q`. Make the determinant-one triangular shear

`U=X_p+(c/a)X_q`, `V=X_q`.                                      (4.1)

Then

`F_{U,V}(u,v)=f_p(u-(c/a)v)f_q(v) <=1`;                          (4.2)

`U,V` are generally dependent, and no independence is claimed. The pair core and leaf couplings become

`a U^2 + delta V^2`,

`delta=b-c^2/a=det(B)/a`,                                       (4.3)

and

`2U<h_p,X_I> + 2V<h_q-(c/a)h_p,X_I>`.                           (4.4)

Consequently, if the active leaf block is low-rank-plus-diagonal and the mixed rows formed from its Fresnel directions together with

`h_p`, `h_q-(c/a)h_p`

satisfy Theorem 3.1, its density bound is **independent of `delta`**. In particular the same estimate holds for every punctured near-singular value and at the exact singular face.

This is precisely the algebraic square completion needed in the partner's r46 debt, but used without the forbidden inference that `(U,V)` are independent.

## 5. Actual target-valid near-singular family with dense same-side curvature

Let `m>=8` be a Sylvester--Walsh size and choose flat orthonormal vectors

`c,d,w in R^m`,

so every coordinate has squared magnitude `1/m`. Put `M0=4`. For arbitrary independent cap-one `X_1,X_2,Y_1,...,Y_m` and `0<=delta<=1`, define

`Q_delta
 = X_1^2 + 2 X_1 X_2 + (1+delta) X_2^2
   + 2 M0 X_1 <c,Y>
   + 2 M0 X_2 <c+d,Y>
   + <w,Y>^2`.                                                    (5.1)

The literal physical two-hub core is

`B_delta=[[1,1],[1,1+delta]]`,

`det B_delta=delta`.                                             (5.2)

Thus for `delta>0` it is positive definite and becomes exactly rank-one PSD at `delta=0`.

Complete the pair by the **hub-only** determinant-one shear

`U=X_1+X_2`, `V=X_2`.                                            (5.3)

The sheared joint density is

`F_{U,V}(u,v)=f_1(u-v)f_2(v)<=1`,                                (5.4)

and (5.1) becomes exactly

`Q_delta
 = U^2 + delta V^2
   + 2 M0 U<c,Y>
   + 2 M0 V<d,Y>
   + <w,Y>^2`.                                                    (5.5)

The physical dense same-side block `w w^T` is retained; it is not conditioned away or treated as a perturbation.

Take the active leaf bank to be the literal `Y` coordinates. With mixed coordinates ordered `(w,U,V)`, its rows are

`rho_i=(w_i,M0 c_i,M0 d_i)`.                                     (5.6)

Hence

`G=diag(1,M0^2,M0^2)`,

`det G=M0^4`,                                                     (5.7)

and every normalized row leverage is

`rho_i^T G^(-1) rho_i = w_i^2+c_i^2+d_i^2=3/m<=3/8<1/2`.        (5.8)

Theorem 3.1 with `h=2,r=1,lambda=1,M=1` gives

`|phi_{Q_delta}(t)|
 <= 8 pi^(5/2) M0^(-2) |t|^(-5/2)`,                             (5.9)

uniformly for **all `delta in [0,1]`**. Exact integration gives

`boxed:
 ||p_{Q_delta}||_infinity
 <= (5/3) 2^(6/5) M0^(-4/5)
 = 5/(3*2^(2/5))
 = 1.263097138758665... .
`                                                               (5.10)

Therefore

`boxed:
 P{Q_delta in L} <= 1.263097138758665... |L|
`                                                               (5.11)

for every interval `L`, and this branch has a continuous density. There is no Cauchy--Schwarz decoupling, no probability squaring, and no square-root small-ball loss.

### 5.1 Deterministic target certificate

The stochastic shear is used only through the joint density cap above. For deterministic spectral bookkeeping, set

`z'=(U,V,Y)=T z`,

where the hub block of `T` is

`S=[[1,1],[0,1]]`.                                                (5.12)

In the orthonormal deterministic coefficient basis `(U,V,c,d,w)`, the transformed quadratic matrix is

`A'_delta
 = [[1,M0],[M0,0]]
   direct_sum [[delta,M0],[M0,0]]
   direct_sum [1]`.                                               (5.13)

For `0<=delta<=1`, all four eigenvalues supplied by the two `2 x 2` blocks have modulus at least

`R=(sqrt(65)-1)/2`.                                               (5.14)

The least singular value squared of `S` is

`sigma_min(S)^2=(3-sqrt(5))/2`.                                  (5.15)

Since the original physical matrix is

`A_delta=T^T A'_delta T`,                                        (5.16)

standard singular-value monotonicity under multiplication by invertible matrices gives

`s_4(A_delta)
 >= sigma_min(T)^2 s_4(A'_delta)
 >= [(3-sqrt(5))/2][(sqrt(65)-1)/2]
 = 1.3487712112688728... >1`.                                    (5.17)

A real symmetric matrix has singular values equal to absolute eigenvalues. Hence every `A_delta` in this family has at least **four** eigenvalues of modulus greater than one. It is a genuine full-target near-singular family, not a conditional toy outside the owner's hypothesis.

## 6. Latest partner r46 applied on the same family

Fleet03/B09 r46 proves the exact singular-pair polynomial-star theorem. For a singular pair

`[[a,c],[c,b]]`

with outside arm vectors `u,v`, set

`H=a v-c u`.

Then, with completely arbitrary remaining curvature,

`||p_Q||_infinity <= 2^(11/4) ||H||_2^(-1/2)`.                  (6.1)

At `delta=0` in (5.1), the singular pair has

`a=c=1`,

`u=M0 c`,

`v=M0(c+d)`,

so

`H=M0 d`, `||H||=M0=4`.                                         (6.2)

Therefore the completed partner theorem gives the actual full-law inequality

`boxed:
 ||p_{Q_0}||_infinity <= 2^(7/4)=3.363585661014858...,
`                                                               (6.3)

and the same coefficient times interval length, while retaining the dense leaf curvature `w w^T` exactly. Continuity is not asserted by the partner theorem itself.

The new mixed-frame bridge is stronger on this specific geometry and, more importantly, remains valid for every `0<delta<=1`. Thus r46 and Theorem 3.1 meet on the exact singular face without any discontinuous deletion of `delta V^2`.

## 7. A quantitative obstruction to determinant-first near-singular routing

For the physical pair `B_delta` in (5.2),

`lambda_min(B_delta)
 = [2+delta-sqrt(4+delta^2)]/2
 = delta/2+O(delta^2)`.                                          (7.1)

Hence

`|det B_delta| sigma_min(B_delta)=Theta(delta^2) ->0`.           (7.2)

Any receiver that first pays a reciprocal positive power of this physical pair currency necessarily degenerates along the family. Yet the genuine source-coordinate law satisfies the uniform estimate (5.10) all the way to `delta=0`.

There is a second order-of-operations warning. After (5.3), completing the *small* `delta V^2` term would create a leaf square with coefficient of size `1/delta`. Under arbitrary unbounded/fragmented cap-one inputs that coefficient cannot be called a small probabilistic error or discarded. The mixed-frame proof instead keeps the small square inside the arbitrary hub core, where it is a unimodular phase and costs nothing in the Fourier envelope.

Thus the near-singular obstruction is not "small determinant implies bad density". It is "paying the small determinant before spending the aggregate star/square frame loses the correct currency."

## 8. Why this does not violate the no-post-rotation-independence correction

A previous fleet correction correctly rejects a transformation of the form

`Z=X_h+q(X_I)`

followed by an invocation of mixed-hub Theorem H: then the multiplier `f_h(z-q(x_I))` is nonseparable in the active leaf variables, so the leaf Fourier product and Brascamp--Lieb step are lost.

Here the map is instead

`(X_1,X_2) -> (U,V)=(X_1+X_2,X_2)`,

which acts only inside the hub bank. The resulting hub vector is still independent of the leaf bank as a vector, and its exact joint density satisfies (5.4). The proof of Theorem 3.1 never factors `F_{U,V}` and never calls `U,V` independent. This is precisely the distinction required by the correction history.

## 9. What remains

The present theorem closes the partner's punctured near-singular **analytic** problem whenever the same active leaf bank has a low-rank-plus-diagonal decomposition whose augmented post-completion rows form a diffuse mixed frame. It does **not** pay

`delta V^2+2V<g,Y>+W(Y)`

for arbitrary `W` on that same bank. At `delta=0`, r46 does pay arbitrary `W`; at `delta!=0`, the general-curvature interpolation is still open.

The next B09 target is therefore exactly:

`QFORM-NEARSINGULAR-GENERAL-CURVATURE-COMPILER-v1`.

A successful continuation should either

1. extend the singular-star half-Riesz mechanism to retain the small square jointly with arbitrary `W`, uniformly as `delta->0`; or
2. prove a structural compiler that forces the arbitrary-curvature survivor into a paid grouped-crossing, mixed-frame, localized-core, or volume branch **before** reciprocal near-singular pair selection.

No valid full-target counterexample was found. The required pinned and current counterexample searches likewise report none. Full unrestricted QFORM remains open; full-target continuity remains open, although the mixed-frame branch proved here has a continuous density via its `L^1` characteristic function.
