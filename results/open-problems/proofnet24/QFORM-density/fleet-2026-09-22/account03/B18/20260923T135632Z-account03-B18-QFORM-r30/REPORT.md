SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T13:56:32Z.
attacking: the two-sided scalar-hub/rank-two-cross gap by a source-valid augmented rank-three cross block; then dependence-safe Schur square smoothing.

# account03/B18 r30 — transverse two-sided hub closure by augmented rank-three cross smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** literature-to-proof transfer  
**Status:** NEW SUPPORTING IMPLICATION / SOURCE-MATCHED / FULL QFORM OPEN  
**Regularity:** the base theorem below gives a continuous `C_0` density; the outer dependent-square wrapper gives essential boundedness, with continuity not claimed through that wrapper.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact source and correction discipline

The only non-elementary external distributional input used here is:

Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877–889, arXiv:1507.07949, DOI 10.1007/s11856-016-1431-5.

Their theorem says: if `f(x)=prod_i f_i(x_i)` is a probability density on `R^n` and every `||f_i||_infinity<=1`, then every `r`-dimensional orthogonal marginal has density at most `2^(r/2)`. This matches the owner hypotheses exactly: no Gaussianity, log-concavity, moments, compact support, connected support, centering, identical laws, or smoothness is assumed.

The fleet already converted that published theorem plus Plancherel into the correction-safe cross-block theorem

`QFORM-CROSSBLOCK-RANK-r-FOURIER-v1`,

at `yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc`,
`proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md`.

I do **not** relabel that theorem as new. Its statement is: if the original coordinates split into independent physical banks `I,J` and the physical cross block `C=A[I,J]` has rank `r>2` with nonzero singular values `s_1,...,s_r`, then arbitrary same-side quadratic and affine terms are allowed and

`||p_Q||_infinity <= [2r/(r-2)] (prod_l s_l)^(-1/r)`.

The density is continuous and vanishes at infinity. In rank three this is exactly

`||p_Q||_infinity <= 6 (s_1 s_2 s_3)^(-1/3)`.

The proof uses only original-bank independence. It never declares singular-vector coordinates independent. The LPP marginal cap is used only to control the densities of the two orthogonal projections inside each independent original bank. The complex same-side phases are retained; Plancherel gives `|phi_Q(t)| <= (2 pi)^(r/2)|t|^(-r/2)(prod s_l)^(-1/2)` and Fourier inversion closes when `r>2`.

This run also consumes the live corrections forbidding law-uniform pointwise quadratic Fresnel decay, post-rotation independence, arbitrary-joint coarea, conditional-density-cap-as-independence, and deletion of a small random quadratic coefficient.

## 2. New transfer: two-sided scalar hub with a transverse rank-two cross bank

Let the original coordinates be split into three mutually independent blocks

`X in R^m`, `Y in R^k`, and a scalar `Z`,

with every original one-dimensional density bounded by one. Let `B` be an `m x k` real matrix of rank two, with nonzero singular values `s_1,s_2`, and put

`Delta = s_1 s_2 >0`.

Let `c in R^m`, `d in R^k`. Allow completely arbitrary measurable same-side phases `F(X)` and `G(Y,Z)` for which the displayed random variable is defined. In the quadratic-form application, `G` may contain arbitrary quadratic terms in `Y`, the term `a Z^2+bZ`, and the full second hub slope `2 Z d^T Y`.

Consider

`Q = F(X) + G(Y,Z) + 2 X^T B Y + 2 Z c^T X`.        (2.1)

Define the transverse hub slope

`gamma_X = dist(c, ran B)`.

### Theorem `QFORM-TWOSIDED-HUB-TRANSVERSE-CROSS-v1`

If `gamma_X>0`, then `Q` has a continuous `C_0` density and

`boxed( ||p_Q||_infinity <= 6 (Delta gamma_X)^(-1/3) ).`       (2.2)

Symmetrically, if the full quadratic form is written with an explicit second hub slope `2 Z d^T Y`, define

`gamma_Y = dist(d, ran B^T)`.

Then either transverse side may be used, and with

`gamma = max(gamma_X,gamma_Y)`

one has

`boxed( ||p_Q||_infinity <= 6 (Delta gamma)^(-1/3) )`          (2.3)

whenever `gamma>0`.

This is the concrete implication that was missing from the preceding account03/B18 one-sided scalar-slope theorem: a scalar may now couple to **both** physical banks. No source separation of the second scalar slope is needed. The only additional structural requirement is a quantitatively transverse component on at least one side of the rank-two cross block.

### Proof

Group the original coordinates as the two independent physical banks

`X` and `W=(Y,Z)`.

All terms in `F(X)` stay on the first side. All terms in `G(Y,Z)`, including `2 Z d^T Y`, stay on the second side. The entire cross interaction between these two independent original banks is

`2 X^T C W`,

where, after ordering the `Z` coordinate last,

`C=[ B  c ]`.                                                    (2.4)

Thus it suffices to compute the three-dimensional cross volume of `C`.

Take a thin SVD

`B=U diag(s_1,s_2) V^T`.

Write

`c=U q + c_perp`, with `c_perp perpendicular ran B`, and `||c_perp||=gamma_X`.

When `gamma_X>0`, `C` has rank three. The product of its three nonzero singular values is the square root of the pseudodeterminant of

`C C^T = B B^T + c c^T`.

On the three-dimensional space `ran B + span(c_perp)`, use the orthonormal basis formed by the two columns of `U` and `n=c_perp/gamma_X`. The matrix of `C C^T` is

`[[ D^2+q q^T,       gamma_X q ],
  [ gamma_X q^T,     gamma_X^2 ]]`,                              (2.5)

where `D=diag(s_1,s_2)`. Taking the Schur complement of the lower-right scalar gives exactly `D^2`; therefore

`pdet(C C^T) = gamma_X^2 det(D^2)
             = (gamma_X s_1 s_2)^2`.                            (2.6)

Hence the product of the three nonzero singular values of `C` is exactly

`Delta_3(C)=Delta gamma_X`.                                      (2.7)

Apply the already source-matched rank-three cross-block theorem to the independent original banks `X` and `(Y,Z)`. It gives (2.2), including continuity. Swapping the two sides gives the `gamma_Y` version. Taking the better of the two estimates proves (2.3). QED.

## 3. Why this is genuinely beyond the preceding one-sided slope packet

The preceding B18 packet treated

`2 Z c^T X + 2 X^T B Y`

with no `Z-Y` slope. Its proof used a scalar Plancherel gain and a rank-two cross Plancherel gain. If one naively inserts `2 Z d^T Y`, the scalar amplitude depends jointly on both cross banks and that factorization is lost.

The present proof does not attempt that invalid factorization. Instead it changes the deterministic grouping: `Z` is placed in the same original-coordinate bank as `Y`. The transverse part of `c` raises the physical cross rank from two to three. The published product-projection theorem plus the existing rank-three cross Fourier theorem then supplies the entire integrable `|t|^(-3/2)` decay in one step.

This is not a pointwise one-dimensional van-der-Corput claim. It is a joint, source-valid rank-three cross estimate.

## 4. Direct physical-star corollary

Let `h` be a physical hub and partition the remaining original coordinates into disjoint banks `J,K`. Write

`B=A[J,K]`, `c=A[J,h]`, `d=A[K,h]`.

Suppose `rank B=2`, with nonzero singular-value product `Delta`, and define

`gamma = max{ dist(c,ran B), dist(d,ran B^T) }`.

All diagonal blocks `A[J,J]`, `A[K,K]`, the hub diagonal `A_hh`, all affine terms induced by conditioning outside `{h} union J union K`, and the two hub slopes are retained. If `gamma>0`, then the conditional and hence full ambient quadratic form satisfies

`boxed( ||p_Q||_infinity <= 6 (Delta gamma)^(-1/3) )`,            (4.1)

with a continuous density in the unconditioned no-outside version, and with the same uniform bound after arbitrary outside-coordinate conditioning.

This turns the live star/bank structural problem into a sharper algebraic debt: a rank-two cross packet is unpaid by this mechanism only when **both** hub slope vectors are quantitatively close to the corresponding cross ranges. In the exact aligned case,

`c in ran B` and `d in ran B^T`,                                  (4.2)

the augmented cross rank stays two and this theorem deliberately makes no claim.

That aligned collar is the correct next target; it should not be hidden by treating a bounded projection density as independence.

## 5. Required account04/B18 result applied to an actual inequality

Use account04/B18's completed

`QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`,

scientific commit
`yspennstate/math-open-problems@4ea84670b15b538f2163d53bf31f81cd1f1eabfa`,
path
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

It states that if a residual random variable has density cap `M`, and an original physical scalar Schur pivot has coefficient `a!=0`, then after completing that original square the translated scalar retains conditional density cap one and

`||p||_infinity <= 2 sqrt(M/|a|)`,                                (5.1)

without assuming independence after completion of the square.

Insert the new base cap

`M = 6 (Delta gamma)^(-1/3)`.

The actual combined inequality is

`boxed(
 ||p_Q||_infinity
 <= 2 sqrt(6) |a|^(-1/2) (Delta gamma)^(-1/6).
)`                                                                  (5.2)

This is a dependence-safe outer-pivot wrapper around the new two-sided transverse packet. The wrapper proves an essentially bounded density; continuity is not claimed from (5.1) alone.

### Literal target-valid test

Take independent cap-one variables

`W,Z,X_1,X_2,X_3,Y_1,Y_2`

and

`Q=(W+Z)^2
   +2 Z X_3 +2 Z Y_1
   +2 X_1 Y_1 +2 X_2 Y_2`.                                       (5.3)

For the residual after the original `W` pivot,

`R=2 Z X_3 +2 Z Y_1+2X_1Y_1+2X_2Y_2`,

choose `X=(X_1,X_2,X_3)`, `Y=(Y_1,Y_2)`. Then

`B=[[1,0],[0,1],[0,0]]`,
`Delta=1`,
`c=(0,0,1)`,
`d=(1,0)`,
`gamma_X=1`.

The new theorem gives the continuous residual-density bound

`||p_R||_infinity <=6`.

The outer pivot has `a=1`, so account04/B18 gives the concrete full-form inequality

`boxed( ||p_Q||_infinity <=2 sqrt(6)=4.898979485566356... ).`       (5.4)

This example is inside the owner target. Indeed, the literal physical principal block on `(X_1,Y_1,X_2,Y_2)` is the direct sum of two matrices `[[0,1],[1,0]]`, with eigenvalues `-1,-1,1,1`. Cauchy interlacing therefore forces the full seven-dimensional symmetric matrix in (5.3) to have at least two eigenvalues `<=-1` and at least two eigenvalues `>=1`. No numerical histogram is used.

The example is genuinely two-sided: `Z` couples to both `X_3` and `Y_1`. The one-sided packet does not literally contain it, while the augmented-cross theorem does.

## 6. Literature audit and exact scope

I searched for an exact published theorem resolving the owner's full arbitrary-matrix target and did not identify one. The published theorem actually used here is the LPP marginal-density theorem; its hypotheses match exactly. The quadratic-form cross-block conversion is the fleet's existing Plancherel consequence at the immutable source above.

No claim of publication novelty is made for the new corollary. Its value is proof transfer: it recognizes that a two-sided hub plus a transverse rank-two cross block is already a rank-three **physical cross block after regrouping original coordinates**, so the source-valid published projection theorem and completed cross-block receiver apply without any new probabilistic assumption.

## 7. Remaining implication

The unrestricted QFORM conjecture remains OPEN / NOT PROVED. The live manifest and claims files still mark it open.

For the local packet addressed here, the first unpaid geometry is now the **doubly aligned rank-two collar**

`dist(c,ran B)` small and `dist(d,ran B^T)` small,                (7.1)

especially the exact case (4.2). A productive next step is to combine this alignment with the N3/star structural identities: alignment means the hub cross field is generated by the same two singular directions as the leaf cross block, so either a same-side curvature direction must provide the missing third dimension or the packet collapses to an effectively low-dimensional Schur form that can be routed to a scalar-pivot/zero-pivot receiver.

The full target still needs every structural branch and all signs; full-target continuity also remains open.
