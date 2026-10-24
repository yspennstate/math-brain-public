SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B19, 2026-09-22T18:35:30Z.
attacking: scale-free heavy-overlap factorization of the O0 third-compound cross bank, with exact payment of the three-heavy-row branch and reduction of the remaining one/two-heavy cases to aggregate residual determinant banks.

# account02/B19 — raw O0 heavy-overlap factorization and three-row payment

**Run:** `20260922T183530Z-account02-B19-qform-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Fresh owner control:** revision `2026-09-22.11` (the programme header remains revision `2026-09-22.5`)  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL O0 SUBBRANCH PAID / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction discipline

The target is unchanged: for arbitrary independent real coordinates with one-dimensional probability densities bounded by one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential-supremum bound for the density of `X^T A X`, or give a valid counterexample. No moment, support, log-concavity, diagonal-basis or post-rotation-independence hypothesis is added.

The live revision-11 corrections are enforced. In particular I do not use the refuted arbitrary-joint rank-three coarea cap, the refuted worst scalar-conditioned rank-three density supremum, a law-uniform pointwise quadratic-phase decay estimate, conditional spectral projection caps, or a one-good-minor selection followed by reciprocal payment. The scalar-conditioning proposal in the owner message is retained only as historical context; account03/B03 has supplied a target-valid four-variable counterexample to the uniform conditional-supremum bridge.

No full theorem is claimed here.

## 2. Source-pinned incoming state

I use the following completed inputs at their exact scopes.

1. **Full-matrix third-compound O0 reduction.** account03/B07, `QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1`, canonical source `yspennstate/math-open-problems@987b364e280070b1de6eec307557cc00f489e581`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T163733Z-account03-B07-qform-r12/REPORT.md`. In its O0 alternative there is a disjoint original-coordinate cut `L disjoint_union R` whose physical cross block `B=A[L,R]` satisfies

`E_3(B):=e_3(BB^T)=sum_{|S|=|T|=3} det(B[S,T])^2 >=1/256`.       (2.1)

2. **Finite heavy row set.** account01/B07, `QFORM-RIDGE-HEAVY-CORE-SCHUR-FACTOR-v1`, canonical source `yspennstate/math-open-problems@0b704e4e040938a4707d92de6931d449dda725d6`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/a01-b07-20260922T170700Z-qform-r13/REPORT.md`. At its calibrated O0 ridge scale there is a physical heavy row set `H subset L` with `|H|<=4`. Its report factors a selected *regularized* determinant occupancy pattern. The argument below instead factors the *raw third-compound mass* by the same finite physical set and is independent of the regularization scale.

3. **Named partner, current completed version.** account03/B19 r16, `QFORM-EXACT-CROSS-RANK-L2-v1`, canonical report commit `yspennstate/math-open-problems@9d55d9ca5a7beaed6f693a57bd32b5fc9949b981`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T172719Z-account03-B19-QFORM-r16/REPORT.md`. If a disjoint original-coordinate cross block `C` has exact rank `r>=3`, then

`||p_Q||_infinity <= e r/(r-2) Pi_r(C)^(-1/r)`,                (2.2)

and if one active bank consists of exactly `r` physical coordinates the factor `e` improves to `sqrt(e)`. Thus for a three-row full-row-rank cross bank,

`||p_Q||_infinity <=3 sqrt(e) det(CC^T)^(-1/6)`.              (2.3)

Arbitrary self terms, affine shifts, outside couplings, signs and extra spectrum are retained by conditioning outside the two active original-coordinate banks.

4. **Newest compatible O0 structure.** account03/B07 r15, source `yspennstate/math-open-problems@77bcf0cdd3ff67910a64a3833c21589408358d6b`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T183653Z-account03-B07-qform-r15/REPORT.md`, sharpens the one-heavy ridge survivor into either a near-coloop, a replacement pair, or a bounded-cardinality regularized area bank. The theorem below is complementary: it is a scale-free raw-third-compound decomposition and directly pays one heavy-overlap subbranch.

A further compatible source, account03/B03 r17 at `yspennstate/math-open-problems@924b3c4c70f86a64402863fe228f641bf3db60b2`, gives determinant-bank half-Riesz estimates from aggregate `e_k(BB^T)` resources. I use it only in the updated proof map, not to claim a payment whose Schur/product hypotheses have not been established.

## 3. New theorem: raw third-compound mass factors through a finite heavy pattern

Let `B` be any real `m x n` matrix and let `H subset {1,...,m}` satisfy `|H|<=4`. Put `C=H^c` (inside the row index set). For `T subset H` with linearly independent rows define

`P_T^perp = I - B_T^T (B_T B_T^T)^(-1) B_T`.                 (3.1)

For `T=emptyset`, put `P_T^perp=I` and `det(B_TB_T^T)=1`.

### Theorem 3.1 — `QFORM-O0-RAW-HEAVY-OVERLAP-FACTOR-v1`

Assume

`e_3(BB^T)>=delta>0`.                                           (3.2)

Then there exist `r in {0,1,2,3}` and `T subset H`, `|T|=r`, such that `B_T` has full row rank when `r>0` and

`det(B_TB_T^T) * e_(3-r)( B_C P_T^perp B_C^T )
 >= delta / [4 binom(4,r)].`                                    (3.3)

The convention is `e_0=1`. In particular, for the O0 value `delta=1/256`, one of the following four **scale-free** alternatives holds:

`r=0:  e_3(B_C B_C^T) >=1/1024`;                               (3.4)

`r=1:  ||b_i||_2^2 e_2(B_C P_i^perp B_C^T) >=1/4096`;          (3.5)

`r=2:  det(B_TB_T^T) ||B_C P_T^perp||_F^2 >=1/6144`;           (3.6)

`r=3:  det(B_TB_T^T) >=1/4096`.                                (3.7)

Here `b_i` is the selected row in the `r=1` case.

### Proof

By the principal-minor identity for a Gram matrix,

`e_3(BB^T)=sum_{S subset [m], |S|=3} det(B_S B_S^T)`.           (3.8)

Every summand is nonnegative. Partition the sum by

`r=|S intersect H| in {0,1,2,3}`.                              (3.9)

One of the four bins has total mass at least `delta/4`. Fix such an `r`. Split that bin again by the exact heavy pattern

`T=S intersect H`, `|T|=r`.                                    (3.10)

There are at most `binom(4,r)` such patterns. Hence for some `T`,

`M_T:=sum_{R subset C, |R|=3-r}
       det(B_(T union R) B_(T union R)^T)
 >=delta/[4 binom(4,r)].`                                      (3.11)

If `r>0`, positivity of `M_T` means some three-row family containing `T` is independent, so the rows in `B_T` are independent and `B_TB_T^T` is invertible.

For every `R subset C`, `|R|=3-r`, write the Gram matrix in the `T,R` block order. The Schur determinant formula gives

`det(B_(T union R) B_(T union R)^T)
 =det(B_TB_T^T)
  det( B_R [I-B_T^T(B_TB_T^T)^(-1)B_T] B_R^T )`               (3.12)

`=det(B_TB_T^T) det( B_R P_T^perp B_R^T ).`                    (3.13)

Summing (3.13) over all `R` of size `3-r` and using the principal-minor expansion once more yields

`M_T=det(B_TB_T^T)
     e_(3-r)(B_C P_T^perp B_C^T)`.                             (3.14)

Combine (3.11) and (3.14). This proves (3.3), and substituting `delta=1/256` gives (3.4)-(3.7). QED.

### Remarks

1. No ridge scale `gamma` occurs in (3.3). Thus the raw third-compound currency cannot disappear into the `gamma small / D_res large` normalization issue.
2. No single coordinate minor is selected unless there are already three rows in the fixed finite heavy set. The `r<=2` conclusions remain **aggregate** elementary-symmetric resources.
3. The theorem is deterministic matrix algebra and is valid for arbitrary rectangular `B`; no distributional assumption enters until an analytic payment is invoked.

## 4. Named-partner application: the three-heavy-row O0 subbranch is completely paid

Apply Theorem 3.1 to the O0 block (2.1) and the account01/B07 physical heavy set `H`, `|H|<=4`. Suppose the selected alternative has `r=3`. Then (3.7) gives a physical triple `T subset L` with

`det(B_TB_T^T)>=1/4096`.                                      (4.1)

Condition on every original coordinate outside `T union R`. The active left bank now consists of exactly the three original coordinates in `T`; the active cross block is the `3 x |R|` matrix `B_T`, which has exact row rank three. All conditioned couplings become affine terms and all within-`T` and within-`R` quadratic terms are allowed by the named-partner theorem.

Therefore account03/B19 r16, inequality (2.3), applies exactly:

`||p_(X^TAX)||_infinity
 <=3 sqrt(e) det(B_TB_T^T)^(-1/6)
 <=3 sqrt(e) (4096)^(1/6)
 =12 sqrt(e)
 <19.785.`                                                     (4.2)

This is a **target-level payment**: arbitrary dimension, arbitrary admissible product input laws, arbitrary self blocks, arbitrary signs, and arbitrary extra spectrum remain present. The branch is not merely an exact-rank-three whole-matrix special case; only the conditioned cross bank has three physical rows.

Thus any surviving O0 heavy state in this synthesis may be assumed to lie in one of the `r=0,1,2` alternatives (3.4)-(3.6).

## 5. Quantitative form of the surviving raw packets

The remaining cases can be stated without the previous vague phrase “large residual determinant.” They are exactly:

### R0 — no heavy row in the selected raw triple bank

`e_3(B_C B_C^T)>=1/1024`.                                     (5.1)

This is an unconditional third-order cross-volume bank entirely on the non-heavy physical rows. account03/B03 r17 supplies a half-Riesz payment from an aggregate `e_3` resource without selecting one minor, but converting that half-Riesz estimate into a density still requires a product-compatible extra square/pivot or another direct grouped mechanism.

### R1 — one heavy physical row

For some `i in H`,

`||b_i||^2 e_2(B_C P_i^perp B_C^T)>=1/4096`.                  (5.2)

In particular, by the elementary product dichotomy, either

`||b_i||^2>=1/64`                                              (5.3)

or

`e_2(B_C P_i^perp B_C^T)>=1/64`.                              (5.4)

This cleanly isolates a quantitative aggregate rank-one row versus a quantitative second exterior-power residual. It does **not** assert that the heavy coordinate is a usable scalar Schur pivot; the physical diagonal may vanish and the Schur residual need not equal the orthogonal row-space residual in (5.2).

### R2 — two heavy physical rows

For some pair `T subset H`,

`det(B_TB_T^T) ||B_C P_T^perp||_F^2>=1/6144`.                 (5.5)

Thus either

`det(B_TB_T^T)>=1/(32 sqrt(6))`                                (5.6)

or

`||B_C P_T^perp||_F^2>=1/(32 sqrt(6))`.                        (5.7)

Again, (5.5) is a product-preserving aggregate resource, not a claim that one residual row or one `3 x 3` minor is universally large.

These three explicit packets are compatible with the newest account03/B07 r15 classification: the replacement-pair/near-coloop and bounded-cardinality regularized-bank alternatives describe how ridge determinant weight behaves after exclusion, while (5.1)-(5.5) state what the **raw third-compound mass** must still do relative to a finite heavy set. Neither theorem subsumes the other.

## 6. Conditional end-to-end proof map after this run

The strongest source-valid assembly I can currently justify is:

1. The completed low-offdiagonal theorem pays the quantitative small-`s_2(A-diag A)` branch; the ridge-window theorem pays the diffuse regularized-cross branch.
2. The full third-compound reduction routes every remaining target matrix into O0/O1/O2/O3 original-coordinate aggregate packets. No fixed-good-minor inference is made.
3. In O0, completed ridge arguments pay the diffuse-leverage branch. The newest B07 exclusion analysis reduces one-heavy survivors to near-coloop/replacement-pair or bounded-cardinality regularized-bank geometry.
4. Independently, Theorem 3.1 forces one of the scale-free raw packets R0/R1/R2 or the `r=3` physical triple.
5. **New:** the `r=3` physical-triple branch is paid completely by the current named partner account03/B19 r16 with the universal bound `12 sqrt(e)<19.785`.
6. Therefore an unpaid O0 state must simultaneously satisfy the newest exclusion/replacement constraints and one of the aggregate raw packets R0/R1/R2. This is a strictly smaller intersection than either previous residual description alone.
7. O1/O2/O3 remain separate full-synthesis obligations.

The rank-two cross-bank half-Hoelder theorem and the newer zero-internal/one-sided half-Riesz theorems remain available as analytic endpoints when the required product-compatible self-block geometry is actually extracted. They are not silently applied outside those hypotheses.

## 7. First unpaid implication with exact quantifiers

`QFORM-O0-RLE2-RAW-PLUS-EXCLUSION-PAYMENT-v1` (OPEN):

> There exist universal constants such that every O0 ridge-heavy state which satisfies the current account03/B07 exclusion/replacement classification and one of the raw packet inequalities (5.1), (5.2), or (5.5) has a universally bounded density, unless it quantitatively descends to an already-paid ridge, physical-pivot, zero-internal cross-bank, one-sided Schur-bank, or exact-cross-rank branch.
>
> The proof must retain arbitrary within-bank self quadratic terms and additional spectrum, and may not replace (5.1)-(5.5) by one reciprocal tiny coordinate minor or by a worst conditional spectral/rank-three density supremum.

A quantitatively useful sufficient replacement would be a product-preserving transducer that converts either `e_3(RR^T)>=1/1024`, `||b_i||^2 e_2(RR^T)>=1/4096`, or `det(G_T)||R||_F^2>=1/6144`, together with the replacement-pair/near-coloop information, directly into linear small-ball scaling. account03/B03's determinant-bank half-Riesz theorem identifies the correct aggregate analytic currency in the first two cases, but an admissible extra half-order/pivot has not yet been forced in the full parent form.

## 8. Failures and no-go statements preserved

- The revision-11 scalar-conditioned **supremum** bridge is not used; account03/B03 r17 supplies a target-valid counterexample to it.
- Aggregate `e_3` mass is not converted to a single universally large `3 x 3` coordinate minor except when three rows already lie in the fixed four-row heavy core, where finite pigeonholing makes that step valid.
- A large cross row norm is not called a scalar quadratic pivot.
- `B_C P_T^perp` is not identified with a physical Schur complement; those are different objects without extra identities.
- No post-rotation independence, conditional projection cap, moment/support assumption, finite-dimensional census, or numerical experiment is used.

## 9. Status

`QFORM-O0-RAW-HEAVY-OVERLAP-FACTOR-v1`: **PROVED**.  
O0 three-heavy-row subbranch: **PAID**, density `<19.785` by named partner r16.  
O0 surviving raw packets: **R0/R1/R2 exactly quantified** by (5.1), (5.2), (5.5).  
Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.  
Continuity is not claimed for the new algebraic reduction; partner r16 gives continuity on the paid exact-cross-rank branch.

No code or numerical experiment was used in this derivation; all constants follow from exact determinant identities and finite pigeonholing.
