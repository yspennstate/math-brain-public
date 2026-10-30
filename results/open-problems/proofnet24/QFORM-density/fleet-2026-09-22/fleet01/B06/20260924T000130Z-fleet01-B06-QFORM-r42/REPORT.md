SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-24T00:01:30Z.
attacking: the near-collinear two-star survivor — retain the full three-dimensional physical cross volume, identify its exact twisted-wedge decomposition, and route every nonflat packet through a product-preserving rank-three crossing estimate before any fiber maximum.

# fleet01/B06 r42 — twisted-wedge three-hub receiver and exact collinear-flat rigidity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T000130Z-fleet01-B06-QFORM-r42`  
Role: curved fiber integration / analytic derivation and exact structural identities  
Status: **NEW SUPPORTING CONTINUOUS-DENSITY THEOREM / DESIGNATED PARTNER APPLIED / EXACT COLLINEAR-FLAT SURVIVOR CLASSIFIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. This report proves an exact original-coordinate three-hub volume identity in the live zero-anchor/two-star geometry. Whenever the resulting twisted wedge or its genuine three-row curvature companion has target scale, the full ambient quadratic form has a bounded continuous density. In the exact collinear-star limit, simultaneous vanishing of the twisted wedges forces the active background off-diagonal matrix to be diagonal plus rank at most two. The missing step is quantitative stability: small, rather than zero, twisted wedges must be converted to a target-scale grouped receiver without dimension loss.

No Gaussianity, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation independence is introduced. All probabilistic groups below are literal disjoint sets of original coordinates.

## 1. Fresh source boundary and premises


The live full claim and global continuity claim remain OPEN. Corrections retained include: no law-uniform pointwise quadratic-phase decay; no post-rotation independence; no dimension-free unrestricted fiber supremum; no arbitrary-joint three-dimensional coarea cap; no positive moment of worst conditional projection caps; no inference of one uniformly good physical minor from aggregate compound mass; and the recent failure of the critical rank-one same-bank half-Riesz interface.

The designated partner theorem actually used below is fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical mathematics

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For an orthonormal `k`-frame `V` in a bank of independent cap-one original coordinates,

`||p_(V^T Z)||_infinity <= exp(k/2)`.                              (1.1)

The exact-rank crossing theorem used at its checked scope is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

If two independent banks have a cross matrix `B` of exact rank `r`, singular-value product `Pi_r`, projected density caps `M_L,M_R`, and arbitrary measurable internal phases on the two banks, then

`|phi(t)| <= min(1,(pi/|t|)^(r/2)(M_L M_R)^(1/2) Pi_r^(-1/2))`,   (1.2)

and for `r>2`,

`||p||_infinity <= [r/(r-2)] (M_L M_R/Pi_r)^(1/r)`.              (1.3)

The theorem also yields a continuous `C_0` density because the right side of (1.2) is integrable for `r>2`.

Own predecessor is r41,

`yspennstate/math-open-problems@d5064b38d386be7e6e2e3c6968002d04bc0f0717`,

which paid an indefinite physical pair plus a rank-one crossing by a quarter-Riesz average. The present run changes mechanism: no pair is inverted. It keeps a whole literal three-hub cross volume.

## 2. Zero-anchor chamber and the literal three-hub cross matrix

Consider the live two-star / zero-anchor form

`A = [[0,0,a^T],
      [0,0,b^T],
      [a,b,C]]`,                                                   (2.1)

where the first two coordinates are the original physical hubs `X,Y` and the background coordinates are `Z_1,...,Z_m`.

Fix distinct background indices `i,j`, and let

`K={1,...,m}\{i,j}`.                                               (2.2)

Take the **literal original-coordinate hub bank**

`H=(X,Z_i,Z_j)`                                                    (2.3)

and the disjoint original-coordinate complement

`R=(Y,Z_K)`.                                                       (2.4)

The physical cross matrix from H to R is

`B_ij^X = [[0,       a_K^T],
           [b_i, C_{iK}],
           [b_j, C_{jK}]]`.                                       (2.5)

Define its three-dimensional row volume

`Pi_ij^X := sqrt(det(B_ij^X (B_ij^X)^T))`.                        (2.6)

No probabilistic rotation has occurred in (2.3)-(2.5).

## 3. Exact twisted-wedge decomposition

For row vectors `u,v`, write `u wedge v` for their exterior product, with squared norm equal to the sum of squares of all corresponding `2 x 2` minors. Similarly for a three-fold wedge.

### Theorem 3.1 — `QFORM-THREEHUB-TWISTED-WEDGE-IDENTITY-v1`

For every distinct `i,j`,

`boxed:
 (Pi_ij^X)^2
 = || a_K wedge (b_i C_{jK}-b_j C_{iK}) ||_2^2
   + || a_K wedge C_{iK} wedge C_{jK} ||_2^2.`                   (3.1)

Symmetrically, taking the physical hub bank `(Y,Z_i,Z_j)` and complement `(X,Z_K)`,

`boxed:
 (Pi_ij^Y)^2
 = || b_K wedge (a_i C_{jK}-a_j C_{iK}) ||_2^2
   + || b_K wedge C_{iK} wedge C_{jK} ||_2^2.`                   (3.2)

#### Proof

Write the three rows of (2.5) as

`r0=(0,a_K),   r1=(b_i,C_{iK}),   r2=(b_j,C_{jK})`.              (3.3)

Then

`r1 wedge r2
 = e0 wedge (b_i C_{jK}-b_j C_{iK})
   + C_{iK} wedge C_{jK}`.                                       (3.4)

Wedge with `r0=(0,a_K)`. The first resulting term contains `e0`; the second does not. They therefore lie in orthogonal coordinate subspaces of the third exterior power. Hence

`||r0 wedge r1 wedge r2||^2
 =||a_K wedge (b_i C_{jK}-b_j C_{iK})||^2
  +||a_K wedge C_{iK} wedge C_{jK}||^2`.                         (3.5)

Finally `||r0 wedge r1 wedge r2||^2=det(B_ij^X(B_ij^X)^T)`. This proves (3.1); (3.2) follows by exchanging `a,X` with `b,Y`. QED.

The first term is the **twisted two-star curvature**. In coordinates,

`Theta_ij^2
 :=||a_K wedge (b_i C_{jK}-b_j C_{iK})||^2
 =sum_{k<l; k,l in K} T_{ij;kl}^2`,                               (3.6)

where

`T_{ij;kl}
 =a_k(b_i C_{jl}-b_j C_{il})
  -a_l(b_i C_{jk}-b_j C_{ik})`.                                  (3.7)

Thus (3.1) aggregates the entire four-index packet before any reciprocal, minor selection, or fiber supremum.

## 4. Product-preserving continuous-density receiver

### Theorem 4.1 — `QFORM-TWISTED-WEDGE-THREEHUB-RECEIVER-v1`

If `Pi_ij^X>0`, then the full ambient quadratic form has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity <= 3 sqrt(e) (Pi_ij^X)^(-1/3).`                 (4.1)

The same bound holds with `Pi_ij^Y`.

Consequently, each component of (3.1) is separately a valid currency. For example,

`Theta_ij:=||a_K wedge (b_i C_{jK}-b_j C_{iK})||>0`

implies

`boxed:
 ||p_Q||_infinity <= 3 sqrt(e) Theta_ij^(-1/3).`                  (4.2)

Numerically `3 sqrt(e)=4.9461638121...`.

#### Proof

The left bank H in (2.3) consists of exactly three original independent cap-one scalars. If an SVD of `B_ij^X` is `U Sigma V^T`, then `U` is a `3 x 3` orthogonal matrix. The joint density of `U^T H` is merely the orthogonal pullback of the product density of H and is therefore bounded by one:

`M_L<=1`.                                                         (4.3)

No independence among the rotated components is asserted.

On the right, apply the designated fleet02/B06 theorem (1.1) at the actual three-dimensional projection `V^T R`:

`boxed: M_R=||p_(V^T R)||_infinity <= e^(3/2).`                   (4.4)

This is the partner-result splice required in this run. Now apply the checked exact-rank crossing theorem (1.3) with `r=3` and singular-value product `Pi_ij^X`:

`||p_Q||_infinity
 <=3 (e^(3/2)/Pi_ij^X)^(1/3)
 =3 sqrt(e) (Pi_ij^X)^(-1/3)`.                                   (4.5)

The characteristic-function majorant in (1.2) decays as `|t|^(-3/2)` and is integrable, so the Fourier inversion supplied by the same theorem yields a continuous `C_0` density. Equations (3.1) and `Pi_ij^X>=Theta_ij` give (4.2). QED.

### Target-scale form

If `s=s_3(A)>0` and, for some literal pair `i,j`,

`Theta_ij >= eta s^3`                                             (4.6)

or

`||a_K wedge C_{iK} wedge C_{jK}|| >= eta s^3`,                  (4.7)

then

`boxed:
 ||p_Q||_infinity <= 3 sqrt(e) eta^(-1/3) / s.`                  (4.8)

This is scale invariant and has no dimension factor.

## 5. Exact collinear-star flatness forces diagonal plus rank two

The receiver above identifies the exact zero-volume obstruction particularly cleanly in the coefficient-plane collinear limit.

Assume on an active background set `S` that

`b=lambda a`, `lambda !=0`, `a_i !=0` for every `i in S`,         (5.1)

with `|S|>=4`. Assume that for every distinct `i,j in S`, the twisted wedge restricted to the other active coordinates vanishes:

`a_{S\{i,j}} wedge
 (a_i C_{j,S\{i,j}}-a_j C_{i,S\{i,j}})=0`.                       (5.2)

(The factor `lambda` from `b_i C_j-b_j C_i` is immaterial.)

### Theorem 5.1 — `QFORM-COLLINEAR-TWIST-FLAT-RIGIDITY-v1`

Under (5.1)-(5.2), there exists a vector `v in R^S` and a diagonal matrix `D` such that

`boxed:
 C_{S,S}=D+a_S v^T+v a_S^T.`                                     (5.3)

Thus the entire active background block is diagonal plus a matrix of rank at most two.

#### Proof

For distinct `i,j,k,l in S`, the `(k,l)` minor of (5.2) vanishes:

`a_k(a_i C_{jl}-a_j C_{il})
 -a_l(a_i C_{jk}-a_j C_{ik})=0`.                                 (5.4)

Divide by the nonzero product `a_i a_j a_k a_l` and set, for `u!=v`,

`R_uv=C_uv/(a_u a_v)`.                                           (5.5)

Then every four distinct indices satisfy

`R_jl-R_il=R_jk-R_ik`,                                           (5.6)

or equivalently all three pairings have the same pair sum,

`R_ij+R_kl=R_ik+R_jl=R_il+R_jk`.                                (5.7)

We now use the elementary complete-graph four-point lemma. Pick three distinct base indices `p,q,r` and define

`u_p=(R_pq+R_pr-R_qr)/2`,
`u_q=(R_pq+R_qr-R_pr)/2`,
`u_r=(R_pr+R_qr-R_pq)/2`.                                        (5.8)

For every other `i`, put

`u_i=R_ip-u_p`.                                                   (5.9)

Using (5.7) on `{i,p,q,r}` gives `R_iq=u_i+u_q` and `R_ir=u_i+u_r`. Using (5.7) on `{i,j,p,q}` then gives, for all distinct `i,j`,

`R_ij=u_i+u_j`.                                                   (5.10)

Set

`v_i=a_i u_i`.                                                    (5.11)

For `i!=j`, equations (5.5) and (5.10) give

`C_ij=a_i a_j(u_i+u_j)=a_i v_j+v_i a_j`.                         (5.12)

Finally choose the diagonal entries

`D_ii=C_ii-2a_i v_i`.                                             (5.13)

Then (5.3) holds on all entries. QED.

### Interpretation

In the exact collinear-star limit there are now only two possibilities on the active bank:

1. some twisted wedge is nonzero, in which case Theorem 4.1 supplies an original-coordinate rank-three crossing receiver; or
2. every twisted wedge vanishes, in which case the active background off-diagonal structure collapses to diagonal plus rank at most two.

This is an exact classification, not yet a uniform target proof. It is valuable because the r40/r41 near-collinear residue is no longer an unstructured same-bank curvature problem at its limiting geometry.

## 6. What remains unpaid

The first missing implication is now

`QFORM-NEARCOLLINEAR-TWIST-STABILITY-OR-DIAGPLUSRANK2-v1`:

> Quantitatively show that if the two star rows are near collinear and every target-scale three-hub twisted wedge in (3.6) is small, then the relevant active background block is close, in a norm usable by an existing product-preserving receiver, to `diagonal + rank <=2`; or else produce a target-scale `Pi_ij` and fire Theorem 4.1. The reduction must not sum reciprocal tiny physical minors or discard a small quadratic tail on unbounded inputs.

The exact theorem above does not supply this stability constant. Sparse active support (`|S|<=3`), `lambda=0`, and background coordinates outside the chosen active set also require separate routing rather than being silently absorbed into (5.3).

This is the main limitation of r42. The full arbitrary-dimensional QFORM conjecture remains **OPEN**. No target counterexample is produced.

## 7. Checks

The exterior identity (3.1) was checked numerically on random symmetric matrices in background dimensions 5 and 8 by comparing `det(BB^T)` with the two Gram-determinant wedge terms; discrepancies were below numerical roundoff. The rigidity normal form was checked on generated examples `C_ij=a_i a_j(u_i+u_j)` and all twisted wedges vanished to numerical precision. These finite checks are diagnostics only; the proofs in Sections 3 and 5 are exact.

## 8. Regularity and status

Theorem 4.1 proves a continuous `C_0` density in its stated nonzero three-hub-volume branch. Theorem 5.1 is deterministic structural algebra. The full target's essential boundedness remains OPEN, and the requested global continuous-density conclusion remains OPEN. The new results have not yet received two independent end-to-end reviews.
