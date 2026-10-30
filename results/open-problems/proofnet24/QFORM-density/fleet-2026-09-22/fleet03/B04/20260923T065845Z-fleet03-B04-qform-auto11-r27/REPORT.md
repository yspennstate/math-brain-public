SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T06:58:45Z.
attacking: double-star low-cross-rank obstruction via exact rank-two star factorization and product-preserving weighted half-Riesz aggregation.

# fleet03/B04 r27 — row-star clean-bank rearrangement and unconditional star closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control consumed: revision `2026-09-22.15`  
Assignment: Product Fourier rearrangement  
Execution status: `WITHOUT_VERIFIED_BRAIN`  
Full conjecture: `OPEN`.

## 1. Exact target and correction boundary

The target is unchanged. For every finite `n`, independent real ORIGINAL coordinates with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal finite `L^infinity` bound for the density of `X^T A X`, or give a valid counterexample. No Gaussianity, moments, compact support, connected support, log-concavity, or independence after rotation is assumed.

This report does not use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, positive conditional-projection moments, naive fiber suprema, or a selected-small-minor reciprocal. The new estimate uses original-coordinate product structure and a decreasing-rearrangement bound for an inverse-radius kernel.

The preceding B04 run proved that if the canonical physical `2x2`-minor support has zero three-sample overlap probability on the row side, then all supported row pairs share a physical hub `i_*`; equivalently deleting that row leaves cross rank at most one. The present run attacks precisely that exact star residue.

## 2. Source-pinned inputs actually used

### 2.1 Own exact-star result

Own predecessor:

`yspennstate/math-open-problems@053c462960cc0c0068d221ffece8029a662a7ab6`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T055256Z-fleet03-B04-qform-auto11-r26/REPORT.md`.

Its `QFORM-THREE-MINOR-STAR-DICHOTOMY-v1` says that zero three-sample row overlap is equivalent to a common row hub in the supported physical `2x2` minors, and then deleting that hub leaves rank at most one.

### 2.2 One-dimensional product projection

The bounded-density projection theorem used throughout the current QFORM archive gives, for independent cap-one original coordinates and every nonzero coefficient vector `c`,

`||p_{c^T X}||_infinity <= sqrt(2)/||c||_2`.                    (2.1)

A current source-recorded use is

`yspennstate/math-open-problems@e743f52c143097b7704e414647ad94511a74f1b1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/20260922T133816Z-qform-b16-r11/REPORT.md`.

Only this one-dimensional original-product projection fact is used below; no independence of spectral coordinates is asserted.

### 2.3 Fresh completed peer theorem applied at an actual inequality

Fleet01/B01 completed

`QFORM-PAIRVOLUME-HALF-RIESZ-UNCONDITIONAL-v1`

at

`yspennstate/math-open-problems@55255bcb25271145aa9f5a1a93a0cc84ad8e1c3d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T030821Z-fleet01-B01-qform-auto11/REPORT.md`.

For any physical cross block `M` between two disjoint original-coordinate banks, with

`E_2(M)=e_2(M^T M)=sum_{|S|=|T|=2} det(M_{S,T})^2>0`,

and arbitrary within-bank quadratic curvature, affine terms and outside-conditioned couplings, it proves

`sup_s E |R-s|^(-1/2) <= C_E2 E_2(M)^(-1/8)`,                  (2.2)

where

`C_E2 <= 12*2^(5/6)*e^(5/24)=26.3340461808...`.                (2.3)

Its physical-square lift gives

`||p_Q||_infinity <= C_E2 |a|^(-1/2)E_2(M)^(-1/8)`             (2.4)

whenever an untouched original coordinate appears after completion as `a[Z+m]^2` and `M` lies in the exact residual. Section 7 below applies (2.2) at an actual inequality and combines it with the preceding B04 overlap bound.

The designated partner is `fleet04/B04`. At the fresh lookup before this derivation it had current QFORM login/start evidence but no completed current-QFORM canonical report or shared handoff. I therefore do not invent a designated-partner theorem; (2.2) is the completed peer result actually consumed.

## 3. A two-dimensional inverse-radius rearrangement lemma

### Lemma 3.1 — `QFORM-2D-INVERSE-RADIUS-BATHTUB-v1`

Let `W` be a random vector in a two-dimensional Euclidean plane with probability density `g` with respect to planar Lebesgue measure and `||g||_infinity<=L`. Then for every center `w_0`,

`E ||W-w_0||_2^(-1) <= 2 sqrt(pi L)`.                            (3.1)

The constant is sharp within the class `0<=g<=L`, `int g=1`.

### Proof

The kernel `z -> ||z-w_0||^(-1)` is radial decreasing about `w_0`. By the bathtub/decreasing-rearrangement principle, subject to `0<=g<=L` and total mass one, its integral is maximized by putting density exactly `L` on the disk centered at `w_0` having area `1/L`. Its radius is

`R=(pi L)^(-1/2)`.

Therefore

`int g(w)||w-w_0||^(-1)dw
 <= L int_{|u|<=R}|u|^(-1)du
 = L*2*pi*R
 =2 sqrt(pi L)`.

This proves (3.1). QED.

A useful affine form follows immediately. If `Z in R^2` has density cap `K`, and `L:R^2->E` is a rank-two linear map into a Euclidean plane with two-dimensional Jacobian

`J_2(L)=sqrt(det(L^T L))`,

then, for every `d in E`,

`E ||2LZ+d||^(-1) <= sqrt(pi K/J_2(L))`.                         (3.2)

Indeed `2L` has planar Jacobian `4J_2(L)`, so the image density cap is `K/(4J_2(L))`, and (3.1) applies.

## 4. Exact algebra of a physical row star

Let `M` be a physical cross block from an original-coordinate bank `I` to a disjoint bank `J`. Suppose

`rank(M)=2`                                                       (4.1)

and there is a physical row hub `i_0 in I` such that

`rank(M_{I\{i_0},J})<=1`.                                       (4.2)

Because `rank(M)=2`, the deleted-row block has rank exactly one. After relabeling `i_0=0`, write

`M_{I\{0},J}=a v^T`,                                             (4.3)

with nonzero `a in R^(|I|-1)` and `v in R^|J|`, and write the hub row as `r^T`. Thus

`M = [ r^T ; a v^T ]`.                                           (4.4)

Rank two means that `r` and `v` are linearly independent.

Every physical `2x2` minor formed by two nonhub rows vanishes. For a hub/nonhub pair `{0,k}` and columns `{c,d}`,

`det M_{{0,k},{c,d}} = a_k (r_c v_d-r_d v_c)`.                  (4.5)

Consequently the complete pair-volume is exactly

`E_2(M)
 = ||a||_2^2 ||r wedge v||_2^2`,                                (4.6)

where

`||r wedge v||_2^2=||r||_2^2||v||_2^2-<r,v>^2`.                 (4.7)

This identity is invariant under the arbitrary rescaling `a -> c a`, `v -> v/c`; no local entry or local minor is selected.

The row-star condition (4.2) is precisely the structural residue produced by the preceding B04 three-minor theorem when `delta_3^r=0`.

## 5. Main new estimate: a row star pays a quadratically clean opposite bank

### Theorem 5.1 — `QFORM-ROWSTAR-CLEANBANK-LINF-v1`

Let `I,J,K` be disjoint original-coordinate sets. Let `X_I`, `Y_J`, `W_K` have the inherited independent cap-one product law. Let `M` satisfy (4.1)-(4.2), and let

`E_2=E_2(M)>0`.

Consider, after conditioning any further outside original coordinates if desired,

`Q = F(X_I,W) + 2 X_I^T M Y_J + b(W)^T Y_J + c(W)`,             (5.1)

where `F` is arbitrary measurable and finite almost surely. Thus the `I` side may contain arbitrary self-quadratic curvature and arbitrary dependence on conditioned outside coordinates; the `J` bank is quadratically clean, though arbitrary outside-conditioned affine terms `b(W)` are allowed.

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 2^(3/4) sqrt(pi) E_2^(-1/4)
 =2.98090017885818... E_2^(-1/4).
`                                                                  (5.2)

No continuity claim is made for arbitrary merely measurable cap-one input densities in the theorem itself.

### Proof

Fix `W=w`; all bounds below are uniform in `w`. Use the star factorization (4.4), write `X_I=(X_0,X')`, and define the aggregate tail projection

`A=a^T X'`.                                                       (5.3)

By the one-dimensional product projection theorem (2.1), `A` has a density satisfying

`||p_A||_infinity <= K_A := sqrt(2)/||a||_2`.                    (5.4)

Since `X_0` is an original coordinate disjoint from `X'`, `X_0` and `A` are independent. Therefore the two-dimensional vector

`Z=(X_0,A)`                                                       (5.5)

has a joint density cap `K_A`.

The star factorization gives the exact coefficient identity

`M^T X_I = r X_0 + v A =: LZ`,                                  (5.6)

where `L:R^2->span{r,v}` has planar Jacobian

`J_2(L)=||r wedge v||_2`.                                        (5.7)

For fixed `(X_I,W)`, expression (5.1) is an affine function of the independent original-coordinate vector `Y_J`, with coefficient

`q(X_I,w)=2M^T X_I+b(w)`.                                        (5.8)

The product projection theorem gives, whenever `q!=0`,

`||p_{q^T Y_J | X_I,W}||_infinity <= sqrt(2)/||q||_2`.          (5.9)

Let `P` be orthogonal projection onto `E=span{r,v}`. Because `2M^T X_I` belongs to `E`,

`||q||_2 >= ||Pq||_2
          = ||2LZ+P b(w)||_2`.                                   (5.10)

The exceptional equation `2LZ+P b(w)=0` has probability zero because `L` is rank two and `Z` has a two-dimensional density. Thus conditional affine degeneracy occurs only on a null set. Averaging (5.9), using (5.10), and then applying Lemma 3.1 in the affine form (3.2),

`||p_{Q|W=w}||_infinity
 <= sqrt(2) E ||2LZ+P b(w)||_2^(-1)
 <= sqrt(2) sqrt(pi K_A/J_2(L)).`                                (5.11)

Insert (5.4):

`||p_{Q|W=w}||_infinity
 <= 2^(3/4) sqrt(pi)
    [||a||_2 ||r wedge v||_2]^(-1/2).`                           (5.12)

By (4.6),

`||a||_2 ||r wedge v||_2 = sqrt(E_2)`,                           (5.13)

so (5.12) is exactly (5.2). The bound is uniform in `w`, and averaging over `W` preserves it. QED.

### What is new in (5.2)

A generic rank-two clean-bank argument may bound the two-dimensional projected `X` law by a universal joint-density constant. The star geometry is stronger: the active two-dimensional coefficient source is the **product pair** `(X_0,a^T X')`. The first component is an untouched original coordinate and the second comes from a disjoint product bank. This restores independence before the inverse-radius singularity is integrated and improves the clean rank-two constant while paying the entire aggregate `E_2` before any reciprocal operation.

## 6. Exact double-star factorization

If, in addition, the column `2x2`-minor support is a star at a hub column `j_0`, then after relabeling both hubs first the rank-two matrix has the exact form

`M = [[m_00, lambda b^T],
     [mu a,  a b^T]]`,                                           (6.1)

for nonzero tail vectors `a,b`. Equivalently,

`M=u v^T + Delta e_0 e_0^T`,
`Delta=m_00-lambda*mu !=0`,                                      (6.2)

for suitable `u,v`. Every nonzero two-minor then contains both hubs and

`det M_{{0,r},{0,c}} = Delta a_r b_c`,                           (6.3)

hence

`boxed: E_2(M)=Delta^2 ||a||_2^2 ||b||_2^2.`                    (6.4)

Thus the exact double-star residue from r26 is a rank-one cross packet plus one hub-hub defect. Theorem 5.1 already pays it whenever either bank can be made quadratically clean; no lower bound on any individual `a_r`, `b_c`, or physical minor is required.

## 7. Combining r26 with the fresh unconditional pair-volume theorem

The fresh fleet01/B01 theorem (2.2) removes the star singularity even when **both** banks carry arbitrary quadratic self-curvature, provided a usable independent physical square is available outside the residual.

Suppose

`Q=a_0[Z+m]^2+R`,                                                 (7.1)

where `Z` is an original cap-one coordinate independent of the residual variables, the shift `m` may depend arbitrarily on those residual variables, and `R` contains a disjoint original-coordinate cross block `M` with `E_2(M)>0`. The dependence-safe square kernel gives

`||p_Q||_infinity
 <= |a_0|^(-1/2) sup_s E|R-s|^(-1/2)`.                          (7.2)

Applying the completed peer theorem (2.2) at this exact inequality yields

`boxed:
 ||p_Q||_infinity
 <=26.3340461808...
   |a_0|^(-1/2) E_2(M)^(-1/8).
`                                                                  (7.3)

This holds with arbitrary within-bank quadratic leakage and arbitrary outside-conditioned affine terms in `R`.

The preceding B04 three-sample theorem remains quantitatively useful away from a star. With

`delta_3=max(delta_3^r,delta_3^c)`,
`C_3=6*3^(1/4)*sqrt(e)=13.0190353138...`,                         (7.4)

it gives, when `delta_3>0`,

`sup_s E|R-s|^(-1/2)
 <= C_3 E_2(M)^(-1/8) delta_3^(-1/24)`.                          (7.5)

Combining the two completed results produces the uniform compiler

`boxed:
 sup_s E|R-s|^(-1/2)
 <= E_2(M)^(-1/8)
    min{26.3340461808...,
        13.0190353138... delta_3^(-1/24)}
`                                                                  (7.6)

with the second term omitted when `delta_3=0`. Thus the overlap method supplies the better constant in sufficiently nonstar geometry, while the star-wedge theorem prevents any blow-up as `delta_3 ->0` and covers the exact star endpoint. Equation (7.3) is the corresponding density statement after a physical square peel.

This is a genuine application of a completed peer result to an actual density inequality, not merely a citation.

## 8. A diffuse genuinely rotated indefinite target family with explicit constant

The new row-star theorem gives a simple family in which **every physical cross coefficient tends to zero**, yet the density remains uniformly controlled.

For integer `m>=6`, let

`a_m=b_m=m^(-1/2)(1,...,1) in R^m`,                               (8.1)

and define the `(m+1)x(m+1)` cross block

`M_m = [[2/m,       2 b_m^T],
       [2 a_m,      2 a_m b_m^T]].`                               (8.2)

The active row and column spaces are the two-dimensional spans of the hub and the flat vector. In their orthonormal bases the nonzero part of `M_m` is exactly

`K_m=[[2/m,2],[2,2]].`                                            (8.3)

Hence

`det K_m=-4(1-1/m)`,
`E_2(M_m)=det(K_m)^2=16(1-1/m)^2`.                               (8.4)

The eigenvalues of the symmetric `K_m` are

`lambda_+(m)=1+1/m+sqrt(4+(1-1/m)^2)`,
`lambda_-(m)=1+1/m-sqrt(4+(1-1/m)^2)`.                            (8.5)

Thus its singular values are

`s_+(m)=lambda_+(m)`,
`s_-(m)=sqrt(4+(1-1/m)^2)-(1+1/m)`.                               (8.6)

The condition `s_-(m)>=1` is exactly `m>=6`, because squaring the equivalent inequality

`sqrt(4+(1-1/m)^2)>=2+1/m`

gives `1>=6/m`.

Let `X in R^(m+1)` and `Y in R^(m+1)` be arbitrary independent cap-one product inputs and set

`T_m=2 X^T M_m Y`.                                                (8.7)

Its symmetric quadratic coefficient matrix is

`A_m^cross=[[0,M_m],[M_m^T,0]]`,                                  (8.8)

whose nonzero spectrum is

`{+s_+(m),-s_+(m),+s_-(m),-s_-(m)}`.                              (8.9)

Therefore for every `m>=6`, `T_m` itself is a valid genuinely rotated indefinite target with four eigenvalues of absolute value at least one. Moreover every nonzero physical cross coefficient is at most `2/sqrt(m)` and hence tends to zero with dimension.

The tail rows in (8.2) are all multiples of `(2,2b_m^T)`, so the row-star hypothesis holds. Applying Theorem 5.1 and (8.4),

`boxed:
 ||p_{T_m}||_infinity
 <= [2^(-1/4) sqrt(pi)]/sqrt(1-1/m).
`                                                                  (8.10)

At the worst allowed `m=6`,

`||p_{T_6}||_infinity <=1.63270626964...`,                        (8.11)

and the bound decreases to

`2^(-1/4)sqrt(pi)=1.49045008943...`                               (8.12)

as `m -> infinity`.

This is aggregate-before-inversion control in a family where every individual cross coefficient vanishes.

For the owner's separate continuity request, add one further independent cap-one coordinate `Z` and set

`Q_m=Z^2+T_m`.                                                     (8.13)

The spectrum gains an additional eigenvalue `1`, so the target hypothesis remains satisfied. The law of `Z^2` has an `L^1` density, while `T_m` has the `L^1 cap L^infinity` density just proved. Their convolution is therefore continuous (indeed `C_0`) and obeys the same bound (8.10). Thus continuity is proved for this explicit family, though not for the full theorem 5.1 with arbitrary measurable contamination.

## 9. What is closed and what remains unpaid

This run closes the **analytic** exact-row-star endpoint when one opposite bank is quadratically clean, with the explicit constant `2^(3/4)sqrt(pi)`. It also shows, by applying the fresh fleet01/B01 theorem, that the earlier three-minor overlap penalty is no longer an analytic obstruction at all after a usable outside square: the complete pair-volume `E_2` is payable uniformly even at exact stars and near-stars.

The full QFORM conjecture remains OPEN. The first remaining B04 structural implication is now

`QFORM-SPECTRAL-TO-CLEANSTAR-OR-PIVOT-E2-v1`:

> Starting only from `s_3(A)>=1`, route every survivor of the already-paid ridge/grouped-square/local-block branches either (i) to a row/column-star cross packet with one quadratically clean bank, where Theorem 5.1 applies directly; (ii) to a nonzero original physical square whose exact Schur residual has a cross block with dimension-free control of `|a|^4 E_2`, where (7.3) applies; or (iii) to an already-paid grouped/hub/rank-two endpoint. The route must spend aggregate original-product currency before taking a reciprocal and must not demand a uniformly large individual physical coefficient or minor.

No such exhaustive spectral-to-physical routing theorem is proved here, so no full solution is claimed and no end-to-end review is requested yet.

## 10. Regularity and integrity status

- Theorem 5.1: absolute continuity and essential boundedness proved; continuity not established for arbitrary merely measurable input densities.
- Family `Q_m=Z^2+T_m`: continuous `C_0` density proved by independent convolution.
- No Gaussian, moment, support, log-concavity, diagonal-basis or post-rotation-independence assumption is used.
- No Monte Carlo or numerical histogram is used as proof; all constants and the spectral certificate are analytic.
- Full QFORM: OPEN.
- Native brain ingestion: `WITHOUT_VERIFIED_BRAIN`; repository retrieval and writes are not treated as learned-memory ingestion.
