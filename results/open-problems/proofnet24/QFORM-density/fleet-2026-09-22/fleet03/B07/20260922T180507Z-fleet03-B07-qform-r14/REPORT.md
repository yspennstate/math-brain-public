SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B07, 2026-09-22T18:05:07Z.
attacking: O0 one-/two-heavy coordinate skeletons; convert aggregate third-compound mass into a product-preserving ridge payment without reciprocal-minor loss.

# fleet03/B07 — one-heavy exclusion collar and exact skeleton currency

**Run:** `20260922T180507Z-fleet03-B07-qform-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control before this publication:** revision `2026-09-22.11` at `yspennstate/math-research-brain@08728c79e01efc6499ce917d127ac3b78f51f1e6`  
**Assignment:** Coordinate minor selection  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW FULL-MATRIX PAID SUBBRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and current correction state

The full target remains open: for every dimension, independent real coordinates `X_i` with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound on the essential supremum of the density of `Q=X^TAX`, or give a target-valid counterexample. Continuity is a separate requested conclusion.

This run works only in original physical coordinates. It does not rotate the independent input variables, does not invoke law-uniform pointwise quadratic-phase decay, does not take an unrestricted fiber supremum, and does not pay by inverting one tiny coordinate minor.

Owner control revision `.11` proposed a worst-case scalar-`Q_rest` conditional-density bridge. A concurrent completed correction from fleet03/B16, `yspennstate/math-open-problems@850ab3e996732591f8bf32b3f905528079545870`, proves that this worst-condition bridge is itself unbounded even for a diagonal target form whose full density is bounded by `pi`. Thus the identity behind scalar conditioning remains valid, but the universal `sup_b` interface is not available. The present coordinate/ridge mechanism does not use that retired interface.

The designated partner `fleet04/B07` still had no completed current-QFORM artifact in the fresh canonical/search check. No partner result is fabricated. Two completed compatible peer results are used below at their exact scopes:

1. fleet01/B07, `QFORM-RIDGE-SET-DELETION-v1`, canonical commit `0b704e4e040938a4707d92de6931d449dda725d6`, which gives the exact determinant survival identity under deletion of physical rows;
2. fleet01/B04, `QFORM-O0-EFFECTIVE3-ADAPTIVE-Q-v1`, canonical commit `c03349badbdfce229ca3a1548d3de8615d1028c5`, which converts a calibrated original-coordinate ridge block into a continuous-density bound.

## 2. Recovered B07 state

The newest compatible B07 state before this run is

`yspennstate/math-open-problems@f2d3682e9f9d24d67ea14dc990d9f49bebeb5a6e`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T173711Z-fleet03-B07-qform-r13/REPORT.md`.

In the O0 overlap branch it starts with disjoint original-coordinate sets `L,R` and cross block

`B=A[L,R]`

satisfying

`E:=e_3(s_1(B)^2,s_2(B)^2,...) >= 1/256`.                   (2.1)

At the effective-dimension-three ridge scale,

`K=B B^T (gamma^2 I+B B^T)^(-1)`, `tr K=3`,                 (2.2)

with the limiting range projection used when `rank B=3`. The completed fleet01/B04 theorem pays the branch whenever `max_i K_ii<3/4`. The r13 report then isolated a constant third-volume packet when at least three rows are heavy, and reduced the other residual to one or two physical heavy coordinates carrying constant aggregate third-volume currency.

The first unpaid implication was therefore to use that finite physical skeleton without selecting a reciprocal tiny local minor.

## 3. Exact fixed-skeleton third-volume factorization

The following identity records exactly what the aggregate currency becomes after one or two physical rows are fixed.

### Lemma 3.1 — `QFORM-FIXED-SKELETON-EXTERIOR-FACTOR-v1`

Let the rows of a real matrix `B` be `b_s`. Fix a linearly independent physical row set `J` of size `r in {1,2}`. Let `W=span{b_j:j in J}` and, for every `k notin J`, put

`c_k=P_{W^perp} b_k`.

Let `C_J` be the matrix whose rows are the `c_k`. Then

`boxed(
 sum_{S superset J, |S|=3} det(B_S B_S^T)
 = det(B_J B_J^T) e_{3-r}(C_J C_J^T).
)`                                                               (3.1)

#### Proof

For `S=J union T`, with `|T|=3-r`, orthogonally eliminate the components of the rows in `T` lying in `W`. Gram determinant invariance under this block elimination gives

`det(B_S B_S^T)=det(B_JB_J^T) det(C_T C_T^T)`.

Sum over all `T`. Cauchy--Binet, equivalently the exterior-power identity for Gram matrices, gives

`sum_{|T|=3-r} det(C_T C_T^T)=e_{3-r}(C_J C_J^T)`.

This proves (3.1). QED.

In particular,

`r=1:  M_i=||b_i||^2 e_2(C_i C_i^T)`,                         (3.2)

`r=2:  M_ij=det Gram(b_i,b_j) ||C_ij||_F^2`.                  (3.3)

Applied to the r13 O0 skeleton and (2.1):

* if one heavy row carries at least `E/2`, its product in (3.2) is at least `1/512`;
* in the two-heavy `r=1` alternative, one fixed heavy row carries at least `E/6`, hence the product is at least `1/1536`;
* in the two-heavy `r=2` alternative, the fixed pair carries at least `E/3`, hence the product in (3.3) is at least `1/768`.

These are aggregate lower-dimensional currencies. No individual `3x3` minor is inverted.

An exact rational sanity check used

`B=[[1,2,0,1],[0,1,1,2],[2,0,1,1],[1,-1,2,0],[2,1,-1,1]]`.

For `J={0}`, the left side of (3.1) is `428`, while `||b_0||^2=6` and `e_2(C_0C_0^T)=214/3`, again giving `428`. For `J={0,1}`, the triple mass is `230`, while `det Gram(b_0,b_1)=20` and `||C_{01}||_F^2=23/2`, again giving `230`.

## 4. Main new payment: delete one heavy row without losing determinant scale

The key point is that the determinant loss after deleting a physical heavy coordinate is known exactly and can be paid before any local minor is selected.

Assume first `rank B>3`, so the scale `gamma>0` in (2.2) is finite. Put

`L_0=gamma^(-2) B B^T`,
`D=det(I+L_0)`.

Choose a physical row `i` and write

`ell=K_ii`, `C=L\{i}`.

Let `B^-=B[C,:]` and calibrate it at the **same** `gamma`:

`K^-=B^-B^{-T?}`

more explicitly,

`K^- = B^- B^{-T}` is not used; throughout the proof the actual definition is

`K^- = B^- (B^-)^T [gamma^2 I+B^- (B^-)^T]^(-1)`.            (4.1)

Set

`theta^-=tr K^-`, `m=max_j (K^-)_jj`,
`D^-=det(I+gamma^(-2)B^-(B^-)^T)`.

### Lemma 4.1 — exact exclusion identities

One has

`D^-=D(1-ell)`,                                                (4.2)

and

`K^- = K_CC + K_Ci K_iC/(1-ell)`.                             (4.3)

Therefore

`3-ell <= theta^- <=3`.                                       (4.4)

#### Proof

Equation (4.2) is exactly fleet01/B07's completed `QFORM-RIDGE-SET-DELETION-v1` for a singleton deletion. Equation (4.3) is the L-ensemble exclusion-kernel identity, or follows directly from block inversion of `I+L_0`. Taking traces gives

`theta^-=3-ell+||K_Ci||_2^2/(1-ell)`.

Since `0<=K<=I`, one has `K^2<=K`, hence

`ell^2+||K_Ci||_2^2=(K^2)_ii<=ell`,

so `||K_Ci||_2^2<=ell(1-ell)`. This proves (4.4). QED.

### Theorem 4.2 — `QFORM-O0-ONE-HEAVY-EXCLUSION-COLLAR-v1`

Assume (2.1)-(2.2), `3/4<=ell<=7/8`, and define `theta^-`, `m` by (4.1). If

`m <= tau(theta^-):=max(1/2, theta^-/4-1/16)`,                (4.5)

then the **full ambient quadratic form**, retaining arbitrary self blocks, all outside couplings, all additional eigenvalues and all signs, has a continuous density satisfying

`boxed( ||p_Q||_infinity <190. )`                              (4.6)

#### Proof, finite ridge scale

Because `ell<=7/8`, (4.4) gives

`theta^- >= 17/8`.                                             (4.7)

Choose

`q=max(1,2m)`.

If `m<=1/2`, then `q=1`, `max diag K^-<=q/2`, and

`theta^- -2q >=17/8-2=1/8`.                                   (4.8)

If `m>1/2`, (4.5) implies

`theta^- -2q=theta^- -4m >=1/4`.                              (4.9)

Thus in all cases `1<=q<=2`, `max diag K^-<=q/2`, and `theta^->2q`. Apply the completed full-form ridge theorem underlying fleet01/B04 to the **actual row-deleted physical cross block** `B^-`:

`||p_Q||_infinity
 <= e/(sqrt(2q) gamma) * theta^-/(theta^--2q)
       * (D^-)^(-1/(2theta^-)).`                              (4.10)

No other part of `A` is discarded by that theorem.

At the original trace-three scale, if `x_j=s_j(B)^2/gamma^2` and `k_j=x_j/(1+x_j)`, then `sum k_j=3` and the elementary-symmetric concentration inequality gives `e_3(k)>=1`. Hence

`gamma^6 <= E`,                                               (4.11)

while the regularized determinant expansion gives

`D>=E/gamma^6`.                                                (4.12)

Using (4.2),

`gamma^(-1)(D^-)^(-1/(2theta^-))
 <= (1-ell)^(-1/(2theta^-)) E^(-1/6).`                        (4.13)

Indeed the residual factor is

`gamma^(3/theta^- -1) E^(-1/(2theta^-))`,

and (4.11) converts it exactly to `E^(-1/6)` because `theta^-<=3`.

Now `1-ell>=1/8` and `theta^->=17/8`, so

`(1-ell)^(-1/(2theta^-)) <= 8^(4/17)`.                         (4.14)

Also `E^(-1/6)<=256^(1/6)=2^(4/3)`, `theta^-<=3`, the denominator in (4.10) is at least `1/8`, and `sqrt(2q)>=sqrt2`. Therefore

`||p_Q||_infinity
 <= (24e/sqrt2) 2^(4/3) 8^(4/17)
 =189.607632263... <190.`                                     (4.15)

The ridge theorem supplies continuity. QED.

### Rank-exactly-three endpoint

When `rank B=3`, use the limiting row projection `K`. If `ell<=7/8`, deleting row `i` preserves rank three and the exact singular-volume identity is

`E^- = E(1-ell) >= 1/2048`.                                   (4.16)

The deleted limiting projection has trace three. Condition (4.5) becomes

`m<=11/16`.

Applying fleet01/B04's completed `QFORM-O0-EFFECTIVE3-ADAPTIVE-Q-v1` directly to `B^-` gives, at the worst endpoint `q=11/8`,

`||p_Q||_infinity
 <= [3e/(sqrt(11/4)(1/4))] (1/2048)^(-1/6)
 <70.10 <190.`                                                (4.17)

Again this is a full-form continuous-density conclusion, not an exact-rank-three-only argument.

## 5. What the theorem removes

The r13 first residual contained a one-heavy physical coordinate with aggregate third-volume mass. The new theorem shows that such a branch is already paid unless one of two sharply localized events occurs:

1. **near-coloop:** `ell>7/8`; or
2. **nested heavy row after deletion:** the physical row-deleted ridge kernel has

`m>max(1/2,theta^-/4-1/16) >=1/2`.                            (5.1)

Thus a one-heavy obstruction cannot remain genuinely one-heavy. Either the first coordinate captures almost an entire regularized direction, or deleting it exposes a second conditionally heavy physical coordinate. This reduction tracks the exact determinant loss `(1-ell)` rather than paying a reciprocal coordinate minor.

The fixed-skeleton identity (3.1) simultaneously records the third-volume currency available when the second heavy coordinate is incorporated. In the two-row alternative the invariant is

`det Gram(b_i,b_j) ||C_ij||_F^2`,                              (5.2)

and r13 guarantees a constant lower bound in the corresponding aggregate branch.

## 6. Current smallest conditional end-to-end deduction

The surviving structural route is now:

1. the third-compound overlap theorem reduces the full target to O0/O1/O2/O3 aggregate banks;
2. in O0, fleet01/B04 pays the calibrated ridge branch with all leverages `<3/4`;
3. r13 isolates and partly pays the three-heavy packet and reduces the remainder to one/two physical heavy coordinates;
4. the present theorem pays every one-heavy state with `ell<=7/8` whose row-deleted kernel is below the explicit conditional-heavy threshold (4.5);
5. hence the first unpaid O0 implication is now

`QFORM-O0-NESTED-HEAVY-OR-NEAR-COLOOP-PAYMENT-v1`:

> starting either from `ell>7/8`, or from a pair of successively heavy physical coordinates supplied by (5.1), use the exact two-row currency (5.2), the orientation-free rank-two affine half-Riesz theorem, or grouped-square smoothing to pay the branch while retaining arbitrary higher-rank residual terms.

The O1/O2/O3 aggregate overlap classes remain separate debts in the global synthesis. The concurrent B16 scalar-conditioning correction means they should not be routed through a worst-case `sup_b` conditional core bound.

## 7. Status and integrity

**Proved this run:**

* `QFORM-FIXED-SKELETON-EXTERIOR-FACTOR-v1`;
* `QFORM-O0-ONE-HEAVY-EXCLUSION-COLLAR-v1`, including the explicit full-form continuous-density constant `<190`;
* exact reduction of the remaining one-heavy O0 obstruction to near-coloop or nested-heavy geometry.

**Not proved:** the unrestricted QFORM conjecture; the nested-heavy/near-coloop payment; O1/O2/O3 closure; a universal continuity conclusion.

The exact-rank-three case is already reported solved in current control and was not re-proved. The designated fleet04/B07 partner had no completed compatible QFORM output at the source check. No schedule, task, notification, email, public release, paid model/API, Codex, account authentication, permission, or unrelated-data action is part of this mathematics. `full_brain_connected=false`.
