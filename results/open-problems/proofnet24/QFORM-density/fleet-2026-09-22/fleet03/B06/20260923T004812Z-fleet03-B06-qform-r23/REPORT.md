SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B06, 2026-09-23T00:48:12Z.
attacking: aggregate an entire determinant star before reciprocal payment, so that any one-sided heavy exterior coordinate closes and the only surviving bicolooop state is quantitatively diffuse on BOTH physical sides.

# fleet03/B06 QFORM r23 — determinant-star aggregation squeezes both exterior directions

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T004812Z-fleet03-B06-qform-r23`  
**Assignment:** Curved fiber integration / GEOMETRY  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** not proved by the new paid branch; the conclusion there is absolute continuity plus an essential `L^infinity` bound.

## 1. Exact target and correction boundary

The target is unchanged: for every finite `n`, every collection of independent real original coordinates `X_i` whose one-dimensional probability densities are bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound on the essential supremum of the density of `X^T A X`, or give a target-valid counterexample.

No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence hypothesis is added. The current corrections are retained. In particular this report does not use law-uniform pointwise quadratic-phase decay, an arbitrary-joint rank-three coarea estimate, a positive moment of a worst conditional projection-density cap, an unrestricted spectral-fiber supremum, an X-ray-only indefinite trace bound, or the inference that aggregate minor mass must contain one dimension-free individual minor. The fresh collision warning is also respected: the new theorem aggregates an entire physical determinant star before applying any negative power.

## 2. Source-valid inputs

### 2.1 Incoming B06 bicolooop geometry

The preceding B06 theorem is

`QFORM-BICOLOOP-WEDGE-DIFFUSE-OR-PHYSICAL-MINOR-v1`,

canonical source

`yspennstate/math-open-problems@da1ec290db2acb0c6d155899d242d0a66f624592`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T222149Z-fleet03-B06-qform-r21/REPORT.md`.

In the surviving strict-higher-rank nonzero-pivot bicolooop chamber there are:

* a genuine original-coordinate outer scalar pivot `a != 0`;
* two disjoint original-coordinate residual banks and their actual physical cross block `H`;
* singular values `h_1 >= h_2 >= h_3 >= ...` of `H`;
* a structural scale `gamma>0`;
* top left singular vectors `u_1,u_2`, top right singular vectors `v_1,v_2`;
* physical anchor indices `j,r` such that

`L_j := u_1(j)^2+u_2(j)^2 > c`,                                  (2.1)

`R_r := v_1(r)^2+v_2(r)^2 > c`,                                  (2.2)

where

`c := 6221/6450`,                                                  (2.3)

and

`h_3/h_2 < 3/200`,                                                (2.4)

`h_1 h_2 > (4/5) gamma^2`.                                       (2.5)

Define the normalized top-two exterior directions incident to the anchors by

`p_k = [u_1(j)u_2(k)-u_2(j)u_1(k)]/sqrt(L_j)`, `k != j`,          (2.6)

`q_s = [v_1(r)v_2(s)-v_2(r)v_1(s)]/sqrt(R_r)`, `s != r`.          (2.7)

Then

`sum_(k!=j) p_k^2 = sum_(s!=r) q_s^2 = 1`.                       (2.8)

Let the actual double-incident physical minor matrix be

`M_H(k,s) := det H[{j,k},{r,s}]`, `k!=j`, `s!=r`.                 (2.9)

The exterior-square singular expansion gives the exact decomposition

`M_H = h_1 h_2 sqrt(L_j R_r) p q^T + E`,                          (2.10)

with

`||E||_op <= h_1 h_3`.                                           (2.11)

The previous run paid a single physical minor when *both* `p` and `q` had heavy physical coordinates. It left the branch where only one side was diffuse. The present run removes that asymmetry by paying a whole determinant star.

### 2.2 Grouped exact-rank-two payment

The source-valid grouped theorem is fleet02/B08

`QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1`,

`yspennstate/math-open-problems@c248abc9be918698c6d5a68108c615ba1c4790b3`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T204103Z-1dd824/REPORT.md`.

Let `C` be a rank-exactly-two cross block between two disjoint ORIGINAL-coordinate banks, with arbitrary same-side quadratic and affine terms retained. For fixed physical anchors `j,r`, define

`Delta_jr(C) = sum_(k!=j,s!=r) det C[{j,k},{r,s}]^2`.             (2.12)

When `Delta_jr(C)>0`, the residual output has an `L^3` density satisfying

`||p_R||_3 <= 3^(2/3) 2^(1/3) Delta_jr(C)^(-1/6)`.               (2.13)

The proof groups the original-coordinate product law on both sides and spends the complete determinant bank before taking the reciprocal. It does not select one minor.

### 2.3 Completed fleet04 square theorem actually applied

The designated `fleet04/B06` path still has no completed current-QFORM canonical report/handoff at the fresh lookup, so no theorem or PASS is fabricated for that slot.

The compatible completed fleet04 theorem actually applied is fleet04/B18

`QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`,

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

After the genuine original-coordinate scalar completion its proof supplies

`p_Q(t) <= |a|^(-1/2) int_0^infinity
            p_R(t-sgn(a)u) u^(-1/2) du`,                           (2.14)

without assuming independence between `R` and the translated square variable. For a probability density with `||p_R||_3<=M`, the optimized Holder/mass split from the B06 chain gives

`sup_t int_0^infinity p_R(t-u)u^(-1/2)du
 <= (8/3^(3/4)) M^(3/4)`.                                       (2.15)

The sign-reversed kernel obeys the same bound.

## 3. New theorem: one heavy exterior coordinate already pays

The key improvement is to keep the entire opposite determinant star active instead of asking for a second heavy exterior coordinate.

Let

`tau_0 := [(3/200)/c]^2 = 149769/619213456`.                     (3.1)

For any

`tau_0 < tau <= 1`,                                               (3.2)

define

`delta_tau := (4/5)[ c sqrt(tau) - 3/200 ] > 0`.                 (3.3)

### Theorem 3.1 — `QFORM-BICOLOOP-STAR-AGGREGATION-SQUEEZE-v1`

Under (2.1)--(2.11), for every `tau` satisfying (3.2), at least one of the following holds.

**(P_tau) Paid star branch.** The full ambient quadratic form has an essentially bounded density and

`boxed[
 ||p_Q||_infinity
 <= C_tau / sqrt(|a| gamma),
]`                                                                (3.4)

where

`C_tau := [8 2^(1/4)/3^(1/4)] delta_tau^(-1/4)`.                 (3.5)

**(D_tau) Two-sided wedge-diffuse branch.** Simultaneously

`max_(k!=j) p_k^2 <= tau`,                                        (3.6)

and

`max_(s!=r) q_s^2 <= tau`.                                        (3.7)

Thus a heavy physical coordinate on *either* exterior direction closes the branch. The surviving state is diffuse on both sides.

### Proof

Suppose first that (3.7) fails. Choose `s!=r` with

`q_s^2 > tau`.                                                     (3.8)

Retain **all** original coordinates on the left residual bank and retain only the two original right-bank coordinates `{r,s}`. Condition on all other right-bank coordinates and on all other variables already conditioned in the inherited scalar-pivot reduction. The active cross block is

`C_s := H[:,{r,s}]`.                                               (3.9)

This is a genuine original-coordinate block, so the active coordinate laws are still products with one-dimensional density caps at most one. It has rank at most two.

Its double-incident determinant bank at anchors `j,r` is exactly the squared Euclidean norm of one column of (2.9):

`Delta_jr(C_s)
 = sum_(k!=j) det H[{j,k},{r,s}]^2
 = ||M_H e_s||_2^2`.                                              (3.10)

From (2.10),

`M_H e_s
 = h_1h_2 sqrt(L_jR_r) q_s p + E e_s`.                           (3.11)

Because `||p||_2=1`, the reverse triangle inequality and (2.11) give

`||M_H e_s||_2
 >= h_1h_2 sqrt(L_jR_r)|q_s| - ||Ee_s||_2`

`>= h_1h_2 [sqrt(L_jR_r)|q_s| - h_3/h_2]`.                       (3.12)

Equations (2.1)--(2.4) and (3.8) imply

`sqrt(L_jR_r)|q_s| - h_3/h_2
 > c sqrt(tau) - 3/200`.                                         (3.13)

Using (2.5),

`||M_H e_s||_2
 > (4/5) gamma^2 [c sqrt(tau)-3/200]
 = delta_tau gamma^2`.                                           (3.14)

Consequently

`boxed[
 Delta_jr(C_s) > delta_tau^2 gamma^4.
]`                                                                (3.15)

In particular `Delta_jr(C_s)>0`, so `C_s` has rank exactly two, and the grouped theorem (2.13) applies *before* any minor reciprocal is taken:

`||p_R||_3
 <= 3^(2/3)2^(1/3) Delta_jr(C_s)^(-1/6)`

`< 3^(2/3)2^(1/3) delta_tau^(-1/3) gamma^(-2/3)`.                (3.16)

Now apply the actual fleet04/B18 square-kernel inequality (2.14), followed by (2.15). Since

`[3^(2/3)2^(1/3)]^(3/4)=3^(1/2)2^(1/4)`,                        (3.17)

we obtain

`||p_Q||_infinity
 < |a|^(-1/2) (8/3^(3/4))
    3^(1/2)2^(1/4) delta_tau^(-1/4) gamma^(-1/2)`

`= [8 2^(1/4)/3^(1/4)] delta_tau^(-1/4)
   /sqrt(|a|gamma)`,                                              (3.18)

which is (3.4)-(3.5).

The case where (3.6) fails is symmetric. Choose `k!=j` with `p_k^2>tau`, retain only the two left original coordinates `{j,k}` and retain the entire right residual bank. The relevant row star is

`sum_(s!=r) det H[{j,k},{r,s}]^2
 = ||e_k^T M_H||_2^2`,                                           (3.19)

and the same argument, using `||q||_2=1`, gives the same lower bound `delta_tau^2 gamma^4`, the same exact-rank-two grouped `L^3` estimate, and the same square payment.

Therefore, unless the paid branch holds, both (3.6) and (3.7) must hold. QED.

## 4. Concrete quarter-collar corollary

Take

`tau=1/4`.                                                        (4.1)

Then the star lower-bound coefficient simplifies exactly:

`delta_(1/4)
 =(4/5)[(6221/6450)(1/2)-3/200]
 =2411/6450
 =0.3737984496...`.                                               (4.2)

The paid branch constant is

`C_(1/4)
 =[8 2^(1/4)/3^(1/4)](6450/2411)^(1/4)
 =9.2450187924... < 9.25`.                                       (4.3)

Hence:

### Corollary 4.1 — `QFORM-BICOLOOP-DOUBLE-DIFFUSE-QUARTER-v1`

Either

`boxed[
 ||p_Q||_infinity < 9.25/sqrt(|a|gamma),
]`                                                                (4.4)

or simultaneously

`max_(k!=j) p_k^2 <=1/4`, `max_(s!=r) q_s^2 <=1/4`.               (4.5)

The geometric gain can be stated directly as a physical row/column leverage bound. On the left choose the anchor-adapted orthonormal basis `s,p` of the top-two left singular plane with

`s_j=sqrt(L_j)`, `p_j=0`.                                        (4.6)

Then

`sum_(k!=j)s_k^2=1-L_j < 229/6450`.                              (4.7)

Under the surviving branch (4.5), every nonanchor physical row satisfies

`u_1(k)^2+u_2(k)^2
 =s_k^2+p_k^2
 <229/6450+1/4`

`=3683/12900
 =0.2855038759...`.                                               (4.8)

The symmetric statement holds for every nonanchor physical column of the top-two right singular plane. Thus the only unpaid bicolooop state has:

* one near-coloop anchor on each side;
* after deleting the anchors, **both** top-two exterior directions physically diffuse;
* every remaining top-two-plane physical leverage below `0.286` on both sides;
* the nonzero higher-rank tail retained rather than silently discarded.

This is strictly narrower than the r21 survivor, which required only one side to satisfy an outside-anchor leverage bound below `0.536`.

## 5. Why this is a weighted curved-fiber replacement rather than a largest-minor argument

The central quantity in (3.10) is the whole determinant star

`sum_(k!=j) det H[{j,k},{r,s}]^2`.                               (5.1)

No lower bound is asserted for an individual determinant. A star may consist of arbitrarily many tiny physical minors; the grouped rank-two theorem converts their **sum of squares** into product-measure projection Jacobians before the reciprocal exponent `-1/6` is applied. This is exactly the order of operations required by the live dimension-loss corrections.

Geometrically, selecting the two-column bank `{r,s}` retains the full left curved rank-two interaction. The entire left determinant star is the exterior area of that physical two-column map; it is not an unrestricted supremum along a spectral fiber. The active coordinate laws remain genuine original-coordinate product laws. Arbitrary left self-quadratic terms, the right two-coordinate self block, affine terms produced by outside conditioning, and the inherited outer-square translation all remain in the valid source theorems.

The fresh B08 third-compound work (`yspennstate/math-open-problems@d30dba6db19d1eceabde6222c84a5b57a85506f0`) independently moves in the same correction-safe direction: its aggregate `e_3` receiver spends summed third-minor curvature before reciprocal payment. The theorem here performs the analogous operation one exterior degree lower inside the live bicolooop chamber.

## 6. Tunable squeeze

The quarter collar is not intrinsic. Theorem 3.1 permits any

`tau > tau_0 =149769/619213456 =0.0002418697...`.                 (6.1)

For example `tau=1/16` yields

`delta_(1/16)=2917/16125=0.1808992248...`,                        (6.2)

`C_(1/16)=11.0842929607...`,                                      (6.3)

and the surviving nonanchor top-two leverage on both sides is below

`1/16+229/6450=0.0980038759...`.                                 (6.4)

Thus, at a finite explicit cost, the two-sided diffuse survivor can be driven below a `10%` physical leverage collar. This is potentially useful for the existing regularized spectral-window/ridge receiver, but the nonzero higher-rank tail must still be paid honestly rather than dropped.

## 7. What is and is not closed

### Proved in this run

1. `QFORM-BICOLOOP-STAR-AGGREGATION-SQUEEZE-v1` — a one-sided heavy exterior coordinate is enough; the opposite determinant star is aggregated first and paid by the exact-rank-two grouped theorem.
2. `QFORM-BICOLOOP-DOUBLE-DIFFUSE-QUARTER-v1` — with `tau=1/4`, either the full form has the explicit bound `<9.25/sqrt(|a|gamma)` or both nonanchor top-two physical planes have leverage `<3683/12900<0.286`.
3. The source-valid fleet04/B18 dependent-square theorem is applied to the displayed inequality (3.18), without inventing independence.

### Not proved

The theorem still contains the structural factor `|a|gamma`. It does not prove that this product is universally bounded below in the full target. It does not close the exact-zero or near-zero outer-pivot sibling. It also does not yet turn the two-sided diffuse survivor plus its nonzero higher-rank tail into a universal residual `L^p`, `p>2`, estimate. Therefore it is not the full QFORM theorem. Continuity is not obtained by this branch.

## 8. Next exact implication

The next local target is

`QFORM-DOUBLE-WEDGE-DIFFUSE-CURVED-PACKET-v1`:

> Starting from the surviving state (4.5)-(4.8), use the fact that **both** nonanchor top-two singular planes have physical leverage `<0.286` (or `<0.099` under the `tau=1/16` collar) to construct one product-preserving spectral-window or grouped-coordinate receiver that includes the nonzero singular tail. Prove an `L^p`, `p>2`, residual density or an equivalent half-Riesz payment, then spend the already-valid outer square. Do not replace the full cross block by its rank-two truncation without paying the tail, and do not select one tiny physical minor before aggregation.

A promising splice is the fresh B08 aggregate-third-volume receiver: if the two-sided diffuse rank-two core plus the surviving tail creates a dimension-free `e_3` bank with a one-side range-leverage gate below the available collar, the regularized determinant theorem gives `L^1` Fourier integrability directly. If `e_3` is too small, the matrix is quantitatively near rank two and the remaining task becomes a genuine stability extension of the grouped rank-two `L^3` theorem rather than a fiber-supremum problem.

The global full-target debts remain: a universal structural payment for the outer pivot/scale across all chambers, the zero/near-zero outer-pivot branch, arbitrary additional spectrum, and ultimately two independent end-to-end reviews of any full proof.

## 9. Arithmetic check and integrity

The deterministic arithmetic checker for the exact constants is stored beside this report:

* `CHECK.py`, commit `c57dba85dc4134d1d04878f5d0fc957bb73ef7ac`;
* `CHECK_OUTPUT.txt`, commit `9280165827267931c007f3c9885d3e56dfcd0723`.

It verifies

`tau_0=149769/619213456`,

`delta_(1/4)=2411/6450`,

`C_(1/4)=9.245018792477305<9.25`,

and

`229/6450+1/4=3683/12900=0.285503875968992...`.

These finite arithmetic checks are not used as proof of the symbolic inequalities above.

**Result status:** `PROVED_SUPPORTING_DICHOTOMY_AND_PAID_SUBBRANCH / FULL_QFORM_OPEN`.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.  
**Model/thinking telemetry:** model self-report `GPT-5.6 Sol`; configured reasoning effort `UNKNOWN`; provider reasoning-token/time counters not exposed.
