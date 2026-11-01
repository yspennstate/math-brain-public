SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T22:49:09Z.
attacking: heavy-carrier incident-or-zero-pivot routing via product Fourier and aggregate compound-volume inequalities.

# fleet03/B04 r43 — banked rank-two half-Riesz plus a diffuse projection square

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `NEW SUPPORTING THEOREM / DIFFUSE EXACT-RANK3 BANK RECEIVER / DESIGNATED-PARTNER RESULT APPLIED / FULL TARGET OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: **not proved by the new theorem below**; it proves an essentially bounded density. Full-target continuity remains OPEN.

The unrestricted conjecture is not proved here. The point is to replace a vanishing physical scalar pivot by a whole independent coordinate bank carrying one spectral square. No random coordinate is rotated and then declared independent. No pointwise law-uniform quadratic-phase decay, moment assumption, support assumption, arbitrary-joint coarea lemma, or worst-fiber supremum is used.

## 1. Fresh sources


The main analytic dependency is the completed orientation-free rank-two fractional theorem

`QFORM-RANK2-AFFINE-HALF-RIESZ-v1`,

at

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

It proves, for an orthonormal two-frame `U`, invertible symmetric `2x2` matrix `Lambda`, and arbitrary affine vector `b`,

`sup_t E |(U^T X)^T Lambda(U^T X)+b^T X-t|^(-1/2)
 <=128 |det Lambda|^(-1/4)`,                                      (1.1)

and improves `128` to `16 sqrt(30)` when the affine term lies in `Ran(U)`, in particular when it is zero.

The second input is the Rogozin--Ball / sharp marginal-density theorem for product measures: if `a!=0` and the coordinates of `Y` are independent with one-dimensional densities at most one, then the scalar projection `L=a^T Y` has a density satisfying

`||p_L||_infinity <= sqrt(2)/||a||_2`.                           (1.2)

A source already recorded in the rank-two report is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949; their `k=1` marginal estimate gives (1.2) after scaling.

## 2. Main theorem — replace a physical pivot by an independent diffuse projection

### Theorem 2.1 — `QFORM-BANKED-RANK2-PLUS-PROJECTION-SQUARE-v1`

Let `X=(X_1,...,X_m)` and `Y=(Y_1,...,Y_n)` be two disjoint banks of the original independent cap-one coordinates. Let `U` be `m x 2` with `U^T U=I_2`, let `Lambda` be invertible symmetric `2x2`, let `b in R^m`, `a in R^n\{0}`, `d!=0`, and let `h:R^m->R` be measurable. Put

`R(X)=(U^T X)^T Lambda(U^T X)+b^T X+c`,

`Q=R(X)+d(a^T Y+h(X))^2`.                                      (2.1)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=128 sqrt(2) |d|^(-1/2) ||a||_2^(-1) |det Lambda|^(-1/4).`    (2.2)

If `b in Ran(U)`, in particular if `b=0`, then

`boxed:
 ||p_Q||_infinity
 <=16 sqrt(60) |d|^(-1/2) ||a||_2^(-1) |det Lambda|^(-1/4).`    (2.3)

The theorem is deliberately stated for arbitrary measurable `h`; in the QFORM application `h` is linear. Thus the cross-bank shear created by the third spectral square is retained exactly rather than treated as an independent additive perturbation.

#### Proof

Write `L=a^T Y`. By (1.2), `L` has a density `g` with

`M:=||g||_infinity <=sqrt(2)/||a||_2`.                          (2.4)

Fix `X=x`. Translation does not change the density cap of `L+h(x)`. For `d>0`, the density of

`W_x=d(L+h(x))^2`

is, for `y>0`,

`p_{W_x}(y)=
 [g(-h(x)+sqrt(y/d))+g(-h(x)-sqrt(y/d))]/[2 sqrt(d y)]`,        (2.5)

and is zero for `y<0`. Hence

`p_{W_x}(y) <= M |d|^(-1/2)|y|^(-1/2)`                         (2.6)

on its half-line. For `d<0`, reflection gives the identical bound with `|d|`.

Conditioning on `X=x`, `Q=R(x)+W_x`, so for almost every `s`,

`p_{Q|X=x}(s)
 <= M |d|^(-1/2)|s-R(x)|^(-1/2)`.                              (2.7)

Tonelli supplies an unconditional density and

`p_Q(s)
 <= M |d|^(-1/2) E|s-R(X)|^(-1/2).`                            (2.8)

Now apply the completed half-Riesz theorem (1.1):

`sup_s E|s-R(X)|^(-1/2)
 <=128 |det Lambda|^(-1/4)`.                                   (2.9)

Combining (2.4), (2.8) and (2.9) proves (2.2). If `b in Ran(U)`, use the source theorem's sharper constant `16 sqrt(30)` to get (2.3). QED.

The proof uses a decreasing square-kernel rearrangement only after a genuine product-space projection estimate. It never needs a pointwise estimate on `E exp(itX_i^2)`.

### Continuity status

The argument above gives absolute continuity and an essential `L^infinity` bound. It does not supply a uniform `L^1` characteristic-function envelope, so **continuity is not claimed** from Theorem 2.1. This is intentionally separated from the continuous `C_0` conclusions of the physical cross-`E_3` branches.

## 3. Exact-rank-three banked corollary

Let `H,L` be disjoint original-coordinate banks. Suppose `u_1,u_2` are orthonormal vectors supported in `H`, `v` is a unit vector orthogonal to both, and

`A=lambda_1 u_1u_1^T + lambda_2 u_2u_2^T + d vv^T`,             (3.1)

with all three coefficients nonzero. Write `v=v_H+v_L` according to the physical bank split and let

`eta=||v_L||_2>0`.                                               (3.2)

Then

`X^TAX = lambda_1(u_1^T X_H)^2+lambda_2(u_2^T X_H)^2
       +d(v_H^T X_H+v_L^T X_L)^2`,                              (3.3)

so Theorem 2.1 with the improved zero-affine core constant yields

`boxed:
 ||p_{X^TAX}||_infinity
 <=16 sqrt(60) eta^(-1)|d|^(-1/2)|lambda_1lambda_2|^(-1/4).`    (3.4)

In particular, if `|lambda_1|,|lambda_2|,|d|>=1`,

`||p_{X^TAX}||_infinity <=16 sqrt(60)/eta`.                     (3.5)

All signs are allowed. The useful point is that the third direction can be spread over arbitrarily many physical coordinates: only its **total mass** `eta` in the independent bank is paid, not the reciprocal of a single coefficient or diagonal entry.

This is a product-preserving receiver for a quantitative shear-flat exact-rank-three geometry. It does not say that the bare three-large-eigenvalue hypothesis always admits such a two-plus-one physical bank split.

## 4. Diffuse zero/near-pivot family with a dimension-free bound

This family demonstrates why (3.4) is not merely a repackaged physical-pivot estimate.

Let `N` be divisible by four. On an `N`-coordinate bank `H`, choose three flat orthonormal Walsh sign vectors

`u_1=sigma_0/sqrt(N),
 u_2=sigma_1/sqrt(N),
 w  =sigma_2/sqrt(N)`,                                          (4.1)

where `sigma_0` is all `+1`, `sigma_1` is `+1` on the first half and `-1` on the second half, and `sigma_2` is constant with signs `+,-,+,-` on four consecutive blocks of size `N/4`. On a disjoint `N`-coordinate bank `L`, let

`z=(1,...,1)/sqrt(N)`

and define

`v=(w/sqrt(2), z/sqrt(2))`.                                     (4.2)

Extend `u_1,u_2` by zero on `L`, and put

`A_N=2u_1u_1^T-u_2u_2^T-2vv^T`.                                (4.3)

The three displayed eigenvectors are orthonormal, hence

`spec_nonzero(A_N)={2,-1,-2}`.                                  (4.4)

Thus every `A_N` satisfies the exact owner spectral hypothesis, with exactly three nonzero eigenvalues, and is genuinely rotated/diffuse in the independent coordinates.

The physical diagonals are tiny:

- for every `i in H`,
  `A_ii=2/N-1/N-1/N=0`;
- for every `j in L`,
  `A_jj=-1/N`.

Therefore

`max_k |A_kk|=1/N ->0`.                                         (4.5)

Moreover every physical `3x3` principal determinant vanishes at least cubically in `N`. Indeed write

`A_N=R diag(2,-1,-2) R^T`, `R=[u_1,u_2,v]`.

For any physical triple `S`,

`|det A_N[S,S]|
 =4 |det R_S|^2
 <=4 product_{i in S} ||R_{i,*}||_2^2`.                        (4.6)

A row in `H` has squared spectral leverage `5/(2N)`, while a row in `L` has leverage `1/(2N)`. Hence

`boxed:
 max_{|S|=3}|det A_N[S,S]| <=125/(2N^3).`                       (4.7)

So neither one nonzero physical diagonal nor one fixed principal triple carries target-scale currency as `N` grows.

Nevertheless (3.4) is dimension-free. Here

`eta=1/sqrt(2), |d|=2, |lambda_1lambda_2|=2`,

so for every admissible independent cap-one input law,

`boxed:
 ||p_{X^T A_N X}||_infinity
 <=16 sqrt(60) 2^(-1/4)
 =104.21688998922089...`                                       (4.8)

uniformly in `N`.

This family is the intended quantitative gain: a whole diffuse independent bank substitutes for a physical scalar pivot. The source rank-three pivot estimate scales poorly on the light diagonal `|A_jj|=1/N`, whereas (4.8) remains fixed. The local zero-pivot triple estimate likewise cannot obtain a dimension-free constant from (4.7) alone.

## 5. Designated partner fleet04/B04 applied at an actual inequality

The completed designated-partner report is

`yspennstate/math-open-problems@3224f273e92d97a8bff7424e9b1191c1e49d0611:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B04/20260923T214340Z-fleet04-B04-QFORM-r1/REPORT.md`.

It supplies a literal cross block `M=A[I,J]`, a fixed physical row `i`, a fixed physical column `j`, and

`J_3^sep(i,j)>delta,
 delta=47045881/(12*10^18)`.                                   (5.1)

Every summand in the partner packet is a third minor incident to row `i`. Therefore the full incident row currency obeys the actual inequality

`J_i >= J_3^sep(i,j)>delta`.                                    (5.2)

Applying the completed incident-third-volume product-Fourier receiver from fleet03/B04 r39 gives

`||p_Q||_infinity
 <3*2^(4/3) delta^(-1/6)
 =602.0111324191176... <602.012`,                               (5.3)

with a continuous `C_0` density on that partner branch. This is an equation-level consumption of the designated partner result, not a status citation.

The partner report identifies a remaining `rank-five heavy-carrier` branch and also names a shear-flat exact-rank-three hybrid among the open glue. Theorem 2.1 supplies a new receiver for the part of such a hybrid that admits the explicit two-core-plus-one-independent-bank decomposition (3.1)-(3.2). It is **not** asserted that the current rank-five heavy-carrier survivor automatically has that decomposition.

## 6. Relation to the live heavy-carrier frontier

The latest finite-core compiler in the fleet leaves a branch with a bounded heavy physical set and, in one alternative, a strong carrier direction having more than `1/2` of its square mass in a light complement. Theorem 2.1 says what would finish that alternative if the remaining two strong directions can be isolated as an orientation-free rank-two quadratic on the complementary bank while the light direction enters through one square: the cost is only the reciprocal of the **total light norm**, not of an individual light coordinate.

The first missing structural implication is therefore narrower than a generic zero-pivot problem:

`QFORM-HEAVY-CARRIER-TWOCORE-PLUS-DIFFUSE-SQUARE-OR-CROSSING-v1` — in the live rank-at-most-five carrier survivor, either extract a genuine two-core-plus-one-independent-bank representation to which (2.2)/(2.3) applies with `eta>=c`, or force a target-scale literal cross `E_3`, incident `E_3`, grouped-bank, rank-two crossing, star/ridge, or half-Riesz endpoint. Extra spectral terms may not be deleted merely because their operator norm is small.

The full QFORM conjecture remains OPEN, and full-target continuity remains OPEN separately.
