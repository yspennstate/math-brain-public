SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B09, 2026-09-22T20:49:53Z.
attacking: the one-strong-cross curved-bank residual by keeping one bank projection scalar and the opposite bank's transverse rank-one curvature jointly, without requiring independence inside that opposite bank.

# account03/B09 QFORM r17 — two-bank transverse-curvature smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account03/B09` — Bilinear block mechanism  
Run: `20260922T204953Z-account03-B09-QFORM-r17`  
Control at start: `yspennstate/math-research-brain@b5cde79f47c8be40a010cfcaf575534d10d0ae27`, OWNER CONTROL revision `2026-09-22.15`  
Prepublication refresh: `yspennstate/math-research-brain@7ea84c9c6ecc9fb6013b3e70f4e08c80a89acb26`, OWNER CONTROL revision `2026-09-22.15`  
Outcome: **SUPPORTING_THEOREM_PROVED / REAL CURVED-BANK SUBCASE CLOSED / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains open. This run proves a new direct `O(interval length)` estimate for a one-strong-cross geometry in which the third smoothing direction lives in the **same original-coordinate bank** as one endpoint of the strong cross edge. The two same-bank projections need not be independent. This closes a branch not covered by the previous three-independent-bank triangle theorem.

## 1. Source-pinned inputs and corrections

### 1.1 Completed worker result actually applied

I apply account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical proof

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For a `k`-dimensional orthogonal projection `R^T X` of a product density with one-dimensional caps one, that theorem gives a joint density cap at most `exp(k/2)`. In particular, if `v,w` are linearly independent vectors in one original-coordinate bank and

`V=<v,X>`, `W=<w,X>`,

then after passing through an orthonormal basis of `span{v,w}` and the resulting `2 x 2` linear map,

`||p_(V,W)||_infinity <= e / ||v wedge w||`.                         (1.1)

This exact inequality is used below; it is not merely cited.

For the scalar projection on the disjoint bank I use the source-valid Livshyts--Paouris--Pivovarov consequence recorded in account02/B18 and account02/B09 r6:

`||p_(<u,X>)||_infinity <= sqrt(2)/||u||_2`.                         (1.2)

The designated partner `account04/B09` was checked again in the current-QFORM canonical locations. No completed current-QFORM artifact was present, so no partner theorem is fabricated or awaited. Work therefore continues asynchronously using the completed compatible worker result above.

### 1.2 Corrections enforced

The proof does not use law-uniform pointwise Fresnel decay, post-rotation independence, arbitrary-joint rank-three coarea, positive conditional projection-density moments, worst scalar remainder conditioning, a fixed good physical minor, or the false near-zero half-Riesz interface. In particular, the only independence used after aggregation is genuine: the scalar variable from bank `I` is independent of the **pair** from disjoint bank `J`; the two coordinates of that pair are allowed to be dependent.

## 2. Analytic core: one scalar times one pair coordinate plus a square in the other pair coordinate

### Lemma 2.1 — `QFORM-SCALAR-PAIR-TRANSVERSE-SQUARE-v1`

Let `U` be independent of the random pair `(V,W)`. Assume `U` has a density bounded by `N`, while `(V,W)` has a joint density bounded by `M`. Let `a,c` be nonzero real numbers. For arbitrary real affine coefficients `alpha,beta,gamma,delta`, define

`T = 2 a U V + c W^2 + alpha U + beta V + gamma W + delta`.          (2.1)

Then `T` has an essentially bounded density and

`boxed: ||p_T||_infinity
 <= C0 (MN)^(2/3) |a|^(-2/3) |c|^(-1/3),`                            (2.2)

where

`C0=(3/2) 10^(2/3)=6.9623832504...`.                                (2.3)

Equivalently, for every interval `L`,

`P{T in L} <= C0 (MN)^(2/3) |a|^(-2/3)|c|^(-1/3) |L|`.              (2.4)

#### Proof

Constant translations remove all affine terms without changing the density caps or the independence split: set

`U'=U+beta/(2a)`, `V'=V+alpha/(2a)`, `W'=W+gamma/(2c)`.

Then (2.1) differs from `2aU'V'+c(W')^2` only by a constant. Thus it is enough to treat

`T=2aUV+cW^2`.                                                       (2.5)

Fix `t in R`, `epsilon>0`, and a threshold `r>0`. Split according to `|V|>r` and `|V|<=r`.

**Large `|V|`.** Conditional on `(V,W)=(v,w)`, the allowed set of `u` in

`|2auv+cw^2-t|<=epsilon`

is an interval of length `epsilon/(|a v|)`. Hence

`P{|T-t|<=epsilon, |V|>r} <= N epsilon/(|a| r)`.                    (2.6)

**Small `|V|`.** For fixed `u!=0`, let `A_u` be the Lebesgue area of

`{(v,w): |v|<=r, |2auv+cw^2-t|<=epsilon}`.                           (2.7)

Use the change of variables

`q=2auv+cw^2`, `w=w`,

whose Jacobian magnitude is `2|au|`. For fixed `q`, the constraint `|v|<=r` is

`|q-cw^2|<=2|au|r`.                                                  (2.8)

For every `d>0` and every real `q`,

`Leb{w: |cw^2-q|<=d} <= 2 sqrt(2d/|c|)`.                            (2.9)

Indeed, after reflecting the sign of `c`, the worst case is attained when the interval in `w^2` touches zero. With `d=2|au|r`, (2.9) gives a `w`-length at most

`4 sqrt(|au|r/|c|)`.                                                (2.10)

The `q`-window in (2.7) has length `2epsilon`, so

`A_u <= 4 epsilon sqrt(r) / sqrt(|a c u|)`.                          (2.11)

The density cap `M` for `(V,W)` therefore implies

`P{|T-t|<=epsilon, |V|<=r}
 <= 4M epsilon sqrt(r)/sqrt(|ac|) E|U|^(-1/2)`.                     (2.12)

A one-dimensional probability density bounded by `N` satisfies the translation-uniform estimate

`E|U|^(-1/2) <= 5 sqrt(N)`.                                         (2.13)

To see this, on `|u|<=1/N` integrate the cap `N`, obtaining `4sqrt(N)`; on the complement use `|u|^(-1/2)<=sqrt(N)` and total mass at most one. Consequently,

`P{|T-t|<=epsilon, |V|<=r}
 <= 20 M sqrt(N) epsilon sqrt(r)/sqrt(|ac|)`.                        (2.14)

Combining (2.6) and (2.14),

`P{|T-t|<=epsilon}
 <= epsilon [ A/r + B sqrt(r) ]`,                                   (2.15)

where

`A=N/|a|`,
`B=20 M sqrt(N)/sqrt(|ac|)`.                                        (2.16)

The exact minimizer is

`r=(2A/B)^(2/3)`,                                                    (2.17)

and

`min_{r>0}(A/r+B sqrt(r))
 = 3*2^(-2/3) A^(1/3) B^(2/3)
 = 3*10^(2/3) (MN)^(2/3)|a|^(-2/3)|c|^(-1/3)`.                     (2.18)

Since the centered interval in (2.15) has length `2epsilon`, (2.18) proves domination of the law by Lebesgue measure with density cap exactly half the coefficient in (2.18), namely (2.2). `QED`

The important point is that no square-root small-ball decoupling appears: the square-root singularity in the `W^2` direction is integrated jointly with the bilinear `UV` direction, and the final dependence on interval length is linear.

## 3. Product-bank theorem: one strong cross plus same-bank transverse rank-one curvature

### Theorem 3.1 — `QFORM-TWO-BANK-TRANSVERSE-RANKONE-CURVATURE-v1`

Let `I,J,R` be pairwise disjoint sets of original independent coordinates. Choose nonzero `u in R^I` and linearly independent `v,w in R^J`, and put

`U=<u,X_I>`, `V=<v,X_J>`, `W=<w,X_J>`.

Let `Z` be measurable with respect to the outside coordinates `X_R`. For nonzero `a,c`, arbitrary affine coefficients, and arbitrary outside shift, suppose the conditional active form is

`F = Z + 2aUV + cW^2 + alpha U + beta V + gamma W + delta`.          (3.1)

Define the aggregate strong-cross scale

`s = |a| ||u||_2 ||v||_2`,                                          (3.2)

and the **transverse same-bank curvature scale**

`kappa = |c| ||P_(v^perp) w||_2^2`.                                 (3.3)

Then

`boxed: ||p_F||_infinity <= C_* (s^2 kappa)^(-1/3),`                 (3.4)

with

`C_* = C0 (e sqrt(2))^(2/3) = 17.0856266561... < 17.086`.            (3.5)

Thus every interval `L` satisfies

`boxed: P{F in L} <= 17.086 (s^2 kappa)^(-1/3) |L|.`                (3.6)

#### Proof

Because banks `I` and `J` are disjoint, `U` is genuinely independent of the pair `(V,W)`. By (1.2),

`N <= sqrt(2)/||u||_2`.                                              (3.7)

By the completed account02/B06 affine-fiber theorem, applied to an orthonormal basis of `span{v,w}` and then transformed to the coordinates `(V,W)`,

`M <= e/||v wedge w||`.                                              (3.8)

Apply Lemma 2.1. Since

`||v wedge w||^2 = ||v||^2 ||P_(v^perp)w||^2`,                       (3.9)

we have

`|a|^2 |c| ||u||^2 ||v wedge w||^2 = s^2 kappa`.                    (3.10)

Substituting (3.7)-(3.10) into (2.2) gives (3.4)-(3.5). Conditioning on `X_R` only changes the affine coefficients and additive shift, so the same bound holds uniformly and averages back. `QED`

### Matrix form

The theorem applies to the ambient quadratic matrix whenever, after a disjoint original-coordinate partition,

`A[I,I]=0`,
`A[I,J]=a u v^T`,
`A[J,J]=c w w^T`,                                                    (3.11)

and conditioned outside couplings satisfy

`range A[I,R] subset span{u}`,
`range A[J,R] subset span{v,w}`.                                     (3.12)

No independence between `<v,X_J>` and `<w,X_J>` is asserted or needed. This is the new feature relative to the previous three-bank triangle theorem.

## 4. Direct application to the current one-strong-cross curved-bank residual

The previous B09 run paid a one-strong-cross geometry only when a **third disjoint bank** closed a bilinear triangle. Theorem 3.1 pays a different branch: the third smoother can instead be a rank-one quadratic direction in the same opposite bank, provided it is transverse to the cross direction.

If the current residual has

`s >= tau`, `kappa >= tau`,                                         (4.1)

then immediately

`||p_Q||_infinity < 17.086/tau`.                                    (4.2)

This is aggregate-before-inversion: no physical coefficient or fixed `3x3` minor is inverted. The completed account02/B06 theorem is used exactly at (3.8), turning product-fiber structure into the joint pair cap needed for the new small-ball inequality.

Combined with the previous B09 r16 triangle certificate and account02/B09 r6 wedge certificate, a flat coefficient-side bank is now paid whenever, at a common scale `tau`, either

1. a cross cut has two singular directions (`s_1 s_2 >= tau^2`), or
2. three rank-one disjoint-bank links close a cycle (product >= `tau^3`), or
3. one rank-one cross has strength `s>=tau` and the opposite bank has transverse rank-one curvature `kappa>=tau`.

The worst displayed constant across these three paid branches is `17.086/tau`.

## 5. Target-valid diffuse stress family

Let `m` be even. Take disjoint banks `I,J`, each of size `m`, and define unit vectors

`u=m^(-1/2)(1,...,1)` on `I`,
`v=m^(-1/2)(1,...,1)` on `J`,
`w=m^(-1/2)(1,...,1,-1,...,-1)` on `J`,

with `m/2` plus and `m/2` minus signs, so `v perpendicular w`. Let

`A[I,I]=0`, `A[I,J]=u v^T`, `A[J,I]=v u^T`, `A[J,J]=w w^T`.          (5.1)

On `span{u,v,w}`, the compressed matrix is

`[[0,1,0],[1,0,0],[0,0,1]]`,                                       (5.2)

hence the nonzero spectrum of the full `2m x 2m` matrix is exactly

`{-1,1,1}`.                                                         (5.3)

So (5.1) satisfies the exact three-large-eigenvalue target hypothesis for every `m`. Yet every physical matrix entry has magnitude at most `1/m`; fixed local minors therefore become arbitrarily small. Here `s=kappa=1`, and Theorem 3.1 gives uniformly over all admissible product input laws

`boxed: ||p_Q||_infinity < 17.086`,                                 (5.4)

independent of `m`.

The checker `verify.py` confirms (2.17)-(2.18), the constants, spectrum (5.3), and the `1/m` entry scale for representative even `m`. Its executed output is in `CHECKS.txt`. These finite checks support the displayed algebra only; they are not a universal proof certificate.

## 6. Remaining debt

This run does **not** solve arbitrary same-bank curvature. The exact remaining B09 implication is now narrower:

`QFORM-ONE-STRONG-CROSS-FULL-CURVATURE-v1` — after the wedge, triangle, scalar-square/ridge, and transverse rank-one-curvature payments, handle a flat coefficient-side bank with one strong aggregate cross direction when the opposite self block has genuinely higher-rank or incoherent curvature that cannot be isolated as one paid rank-one square without leaving correlated residual curvature.

A plausible next mechanism is a matrix-valued extension of Lemma 2.1 that keeps the entire opposite-bank quadratic form inside the two-bank sublevel-volume integral, rather than conditioning it to a fiber supremum. The correction controls `(U+V)^2`, near-zero rank-one squares, arbitrary-joint coarea, and conditional-cap blowup remain mandatory.

The unrestricted QFORM conjecture remains **OPEN**. This run proves essential boundedness in the stated scope; it does **not** prove continuity of the density. Repository transport was used but no authenticated native brain retrieval/receiver use was verified, so status remains `WITHOUT_VERIFIED_BRAIN`.
