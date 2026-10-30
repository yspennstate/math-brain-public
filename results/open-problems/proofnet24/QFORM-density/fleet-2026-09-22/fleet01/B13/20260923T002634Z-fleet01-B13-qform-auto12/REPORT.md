SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B13, 2026-09-23T00:26:34Z.
attacking: a max-volume global skeleton for the partner's finite-grid/no-pivot cross-rank normal form, with exact control of the diagonal remainder and no rotation of the independent inputs.

# fleet01/B13 auto12 — max-volume cross-rank skeleton with controlled diagonal remainder

Status: **PROVED SUPPORTING STRUCTURAL THEOREM / FULL-QFORM OPEN / CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

## 1. Source pins and scope


The designated partner result actually used is `fleet02/B13` r15:

`yspennstate/math-open-problems@d59fc91cdb6c772a0b3c73ba5b90fb62e10e3bf`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T000555Z-fleet02-B13-productset-r15-482fba/REPORT.md`.

Its target-level normal form says that, if full QFORM is false, then for every integer `m>=2` there is a rational finite-grid product-indicator witness with slab ratio `>C3 m`, `C3=9 sqrt(3e)`, strict no-`m^-4` physical pivots, and for every disjoint original-coordinate cut `M=A[I,J]`, `s_5(M)<1/m`. It also proves the exact endpoint: if every disjoint cross block has rank at most `r`, then `A=D+R`, with `D` diagonal and symmetric `R` of rank at most `4r`. The unresolved issue is a quantitative/product-compatible stability version.

No pointwise quadratic oscillatory decay, post-rotation independence, arbitrary-joint coarea estimate, conditional projection-density shortcut, fixed physical minor dichotomy, support diameter bound, or fixed fragment count is used below.

## 2. New theorem: max-volume controlled completion

### Theorem 2.1 — `QFORM-MAXVOLUME-CROSSRANK-COMPLETION-v1`

Let `A` be a finite real symmetric matrix. Assume

`rank A[I,J] <= r`

for every pair of disjoint coordinate sets `I,J`. Put

`delta=max_i |A_ii|`,
`epsilon=max_{i!=j}|A_ij|`.

Then there exist a diagonal matrix `D` and a symmetric matrix `R` such that

`A=D+R`,
`rank R<=4r`,
`||D||_op <= delta+r epsilon`.                                      (2.1)

Consequently

`s_{4r+1}(A) <= delta+r epsilon`.                                  (2.2)

This strengthens the partner's exact completion theorem by controlling the diagonal remainder using only the original physical entry scale. In particular, the diagonal remainder need not be discarded perturbatively; it may be retained exactly as a coordinate-separable quadratic phase.

### Proof

If the maximum disjoint cross rank is zero, every off-diagonal entry vanishes and the claim is immediate with `R=0`, `D=A`. Otherwise replace `r` by the actual maximum disjoint cross rank `r0<=r`.

Choose disjoint sets `P,Q`, `|P|=|Q|=r0`, so that

`B=A[P,Q]`

is invertible and `|det B|` is maximal among all invertible disjoint `r0 x r0` cross minors. Let `S=P union Q` and `K=S^c`.

For every `k in K`, define

`x_k=A[k,Q] B^{-1}`,                                               (2.3)
`y_k=B^{-1} A[P,k]`.                                               (2.4)

Every coordinate of `x_k` has absolute value at most one. Indeed, replacing one row of `P` by `k` while keeping columns `Q` gives another disjoint `r0 x r0` minor, and its determinant is, up to sign, `(x_k)_p det B`. Maximality of `|det B|` gives `|(x_k)_p|<=1`. The identical column-replacement argument gives `|(y_k)_q|<=1`.

Now use the partner's symmetric Nyström completion. Set

`H=[[0,2B],[2B^T,0]]`,
`C=A[S,K]`,

and, in the block decomposition `S union K`,

`R1_SS=H`, `R1_SK=C`, `R1_KS=C^T`,
`R1_KK=C^T H^{-1} C`.                                             (2.5)

Because `H` is invertible and the Schur complement of `H` in `R1` is zero,

`rank R1=2r0`.                                                     (2.6)

For distinct `k,l in K`, the disjoint `(r0+1)x(r0+1)` cross minor with rows `P union {k}` and columns `Q union {l}` has determinant zero. Its Schur complement gives

`A_kl=A[k,Q]B^{-1}A[P,l]`.                                        (2.7)

Swapping `k,l` gives

`A_kl=A[k,P](B^T)^{-1}A[Q,l]`.                                    (2.8)

Since

`H^{-1}=(1/2)[[0,B^{-T}],[B^{-1},0]]`,

(2.7)-(2.8) show that `R1_kl=A_kl` for every distinct `k,l in K`. By construction `R1` already matches `A` on `S x K` and `K x S`.

Repair only the off-diagonal entries inside the `2r0`-coordinate core `S`: let `R2` be the symmetric matrix supported on `S x S`, with zero diagonal, whose off-diagonal entries are those of `A-R1`. Then

`rank R2<=2r0`.                                                     (2.9)

Set `R=R1+R2`. It matches every off-diagonal entry of `A`, so `D=A-R` is diagonal and

`rank R<=4r0<=4r`.                                                 (2.10)

It remains to control the diagonal. On `S`, both `H` and `R2` have zero diagonal, hence `R_ss=0` and `|D_ss|=|A_ss|<=delta`.

For `k in K`, direct use of (2.5) gives

`R_kk=A[k,Q]B^{-1}A[P,k]=x_k A[P,k]`.                              (2.11)

The vector `x_k` has `l_infinity` norm at most one, while every entry of `A[P,k]` is off-diagonal and hence at most `epsilon` in modulus. Therefore

`|R_kk|<=r0 epsilon`,

and so

`|D_kk|<=delta+r0 epsilon<=delta+r epsilon`.                        (2.12)

This proves (2.1). Since `R` has rank at most `4r`, the min-max inequality gives (2.2). QED.

## 3. Robust max-volume skeleton before exact rank closure

The same construction gives a useful approximate statement without claiming operator-norm stability.

### Proposition 3.1 — `QFORM-MAXVOLUME-CROSSRANK-SKELETON-v1`

Choose a maximal-volume invertible disjoint `r x r` minor `B=A[P,Q]` and form `R` exactly as above, but do not assume the `(r+1)`-cross minors vanish. Let `D` match the diagonal of `A-R`, and put

`E=A-D-R`.

Then

`rank R<=4r`,
`||D||_op<=delta+r epsilon`,

`E` is symmetric, has zero diagonal, and vanishes whenever at least one index lies in `S=P union Q`. For distinct `k,l in K`,

`|E_kl| <= (r+1) epsilon`.                                         (3.1)

Moreover, if every disjoint cross block has `(r+1)`st singular value at most `sigma`, then

`|E_kl| <= (r+1) sigma`,                                           (3.2)

hence

`|E_kl| <= (r+1) min(epsilon,sigma)`.                              (3.3)

### Proof of the singular-value bound

For fixed distinct `k,l in K`, let

`T=A[P union {k}, Q union {l}]`.

Every `r x r` minor of `T` is still a disjoint physical cross minor, so maximality of `B` gives absolute determinant at most `|det B|` for each of the `(r+1)^2` such minors. Cauchy-Binet therefore yields

`prod_{j=1}^r s_j(T) <= (r+1)|det B|`.                             (3.4)

The Schur-complement identity gives

`det T=det B * (A_kl-A[k,Q]B^{-1}A[P,l])`.                         (3.5)

Thus

`|A_kl-A[k,Q]B^{-1}A[P,l]|`
` <= (r+1) s_{r+1}(T)`.                                           (3.6)

The transposed orientation has the same estimate. The symmetric Nyström prediction is their average, proving (3.2). The coefficient bounds `||x_k||_infinity,||y_l||_infinity<=1` give (3.1). QED.

This is a **single global original-coordinate skeleton**, not unrelated cut-by-cut SVD approximations. It retains the product-coordinate provenance, but (3.3) is only entrywise; no claim is made that `||E||_op` is dimension-free or that it can be removed from a slab inequality on remote supports.

## 4. Application to the designated partner's no-pivot normal form

In the partner's r15 finite-grid normal form, set

`tau=m^{-4}`,
`delta<tau`,
`epsilon<sqrt(tau+tau^2)`,

and every disjoint cross block satisfies `s_5<1/m`.

If the disjoint cross rank is exactly at most four, Theorem 2.1 gives

`A=D+R`, `rank R<=16`,

`||D||_op < eta_m := m^{-4}+4 sqrt(m^{-4}+m^{-8})`.                (4.1)

For `m>=23`,

`eta_m < 1/128`.                                                    (4.2)

Hence

`s_17(A)<1/128`.                                                    (4.3)

In particular, the spectral projection

`P=1_{|A|>=1/64}`

has rank at most sixteen. If its physical leverages all obeyed `P_ii<=1/32`, the already-completed spectral-window theorem would give a universal density bound `<64`, contradicting the partner witness's slab ratio `>C3 m` for `m>=23`. Therefore any such bad exact-crossrank endpoint must contain a physical high-leverage core:

`max_i P_ii>1/32`.                                                  (4.4)

Moreover

`#{i:P_ii>1/32}<32 rank(P)<=512`.                                  (4.5)

Thus the exact crossrank-four endpoint is reduced to a bounded-rank spectral bank plus an **at-most-512-coordinate physical leverage core**, with the small diagonal kept exactly rather than discarded by an invalid support-sensitive perturbation argument.

For the partner's actual approximate normal form, Proposition 3.1 with `r=4` gives a single global decomposition whenever a disjoint invertible `4x4` cross minor exists:

`A=D+R+E`, `rank R<=16`,
`||D||_op < m^{-4}+4 sqrt(m^{-4}+m^{-8})`,

and, off an eight-coordinate core,

`|E_kl| <= 5 min(sqrt(m^{-4}+m^{-8}),1/m)`
`       = 5 sqrt(m^{-4}+m^{-8})`.                                  (4.6)

If no disjoint invertible `4x4` cross minor exists, every disjoint cross block has exact rank at most three and Theorem 2.1 applies with `r<=3` and `E=0`.

Equation (4.6) is **not** a full stability theorem: an entrywise `O(m^{-2})` residual can still interact with arbitrarily remote and fragmented supports, and the correction history forbids simply dropping it.

## 5. Extremal-product interpretation

The partner normal form is already source-valid at the exact product-indicator level: the arbitrary-law no-pivot slab supremum is represented by rational finite-grid product indicators, using finite-mixture purification rather than a fictitious attained global optimizer. Therefore the skeleton above applies directly to the coefficient matrix of the actual extreme-product witness; no single-interval or centered-uniform extremality is introduced.

The new theorem does not by itself bound the slab volume. Its contribution is to replace the partner's exact `D+rank<=16` endpoint by a quantitatively controlled decomposition and to give an inverse-free global skeleton in the approximate case.

## 6. First unpaid implication

`QFORM-NOPIVOT-MAXVOLUME-RESIDUAL-CLOSURE-v1`:

Starting from (4.6), control the zero-diagonal residual `E` jointly with the rank-16 skeleton and the finite-grid product law **without** converting the entrywise `O(m^{-2})` bound into raw operator-norm/slab continuity. A valid closure must be uniform in support translations, gaps and fragment count. One acceptable route would show that the residual either creates a D'/D5-payable cross-volume packet or can be absorbed into a product-preserving affine-uniform bank decomposition before reciprocal-coefficient payment.

The exact `E=0` subcase is now localized to the finite physical leverage core (4.4)-(4.5). The full arbitrary-dimensional QFORM conjecture remains OPEN.
