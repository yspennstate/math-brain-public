SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-24T10:25:11Z.
attacking: the all-tiny-diagonal survivor after fleet02/B20 r52; use the new all-sign pair gate to obtain a literal entry cap, then convert the third target singular mode into either fixed physical E3 currency, an ultrathin rank-two full cut with large E2, or a 15-arm diffuse physical star.

# fleet01/B20 — r52 tiny-diagonal two-volume / diffuse-star compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T102511Z-fleet01-B20-QFORM-auto11i`  
Status: **ESSENTIAL_STEP_APPLIED / NEW_STRUCTURAL_COMPILER / FULL_QFORM_OPEN / NOT_PROVED / NOT_DISPROVED**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted theorem remains OPEN. No counterexample is claimed. Full-target continuity remains OPEN separately. The paid physical-E3 branch below has a continuous `C_0` density; no continuity claim is made for the unpaid structural branches.

No Gaussian, moment, iid, compact-support, connected-support, log-concavity, post-rotation independence, arbitrary-joint coarea, conditional projection-density cap, fiber-supremum shortcut, law-uniform pointwise quadratic oscillatory decay, one-good-minor inference, or deletion of a nonzero coefficient tail is used. Every cut, row, entry, pair and star below is in the ORIGINAL product coordinates.

## 1. Fresh source-pinned inputs


The newest completed designated partner at the final dependency refresh is fleet02/B20 r52,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260924T095927Z-fleet02-B20-QFORM-auto11-r52/REPORT.md`.

Its completed **all-sign physical-pair gate** uses

`D0 = 9.530157744638501e-7`,
`kappa0 = 6.075614261408114e-5`.

On every still-unpaid target instance:

- no literal definite principal pair has `|det B| >= D0`;
- no literal indefinite principal pair has simultaneously `|det B| >= D0` and `s_min(B) >= kappa0`.

The immediately preceding fleet01/B20 theorem is `QFORM-R51-MODERATE-DIAGONAL-OR-PHYSICALSTAR-PAYMENT-v1`: with

`alpha := 1007/4096 = 0.245849609375`,

if `s_3(A)>=1`, `max_i |A_ii|>=1/64`, and every physical off-diagonal row has norm at most `alpha`, then the full law is paid by `<9763`. Hence every globally unpaid state is already constrained by

`max_i |A_ii| < 1/64`  OR  `max_i ||A[i,-i]||_2 > alpha`.

This run closes the first deterministic implication inside the all-tiny-diagonal side and sharply quantifies the large-star side under the same pair-free gate.

## 2. Main theorem

### Theorem 2.1 — `QFORM-R52-TINYDIAG-E2CUT-OR-15ARM-DIFFUSESTAR-v1`

Let `A=A^T` satisfy `s_3(A)>=1`. Assume

`max_i |A_ii| < d := 1/64`,

and assume the completed fleet02/B20 r52 all-sign pair gate has not paid the law. Put

`beta := d + kappa0 = 0.01568575614261408114...`,
`alpha := 1007/4096`,
`sigma := 1-d = 63/64`.

Then:

1. **Global literal entry cap.** Every off-diagonal coefficient obeys

   `|A_ij| < beta` for `i!=j`.

2. If every physical row star obeys `||A[i,-i]||_2 <= alpha`, then there is a literal full physical partition `L sqcup R=[n]` for which `M=A[L,R]` satisfies

   `e_2(M M^T) >= c2`,

   where

   `c2 = (3/16) sigma^2 (sigma^2-alpha^2)`
   `   = 0.1650715633559229900129...`.

   Consequently, with `zeta=2^-24`, either

   `e_3(M M^T) >= zeta`,

   in which case the existing source-valid marginal-free physical-E3 receiver pays the full ambient law (numerically `<169` with the current E3 constant), and the density is continuous `C_0`; or

   `dist_F(M, rank<=2) < sqrt(3 zeta/c2)`
   `                    = 0.0010407934422325723...`.

3. If instead some physical hub `h` has `rho:=||A[h,-h]||_2>alpha`, then there are **fifteen pairwise-disjoint literal leaf groups** `G_1,...,G_15 subset [n]\{h}` such that

   `rho^2/16 <= sum_{j in G_q} A_hj^2 < rho^2/15`

   for every `q=1,...,15`. In particular

   `||A[h,G_q]||_2 > alpha/4 = 1007/16384 = 0.06146240234375`,

   while every individual hub coefficient still satisfies `|A_hj|<beta`.

Thus an unpaid all-tiny-diagonal state is no longer an arbitrary tiny-diagonal matrix: it has either a fixed positive physical two-volume cut which is ultrathin rank two after E3 failure, or a quantitatively diffuse fifteen-arm original-coordinate star.

## 3. Actual application of fleet02/B20 r52: pair-free => entry cap

Fix `i!=j` and write the literal principal pair

`B = [[a,b],[b,c]]`,

with `a=A_ii`, `c=A_jj`, `b=A_ij`. Since `|a|,|c|<d`, suppose for contradiction that

`|b| >= beta = d+kappa0`.

Then `|b|>d`, so `B` is indefinite because

`det B = ac-b^2 < d^2-b^2 < 0`.

Moreover

`|det B| = b^2-ac >= b^2-d^2 >= beta^2-d^2`.

At the actual r52 constants,

`beta^2-d^2-D0`
` = 9.4930499109152809e-7 > 0`.

Hence `|det B|>D0`. Also compare

`B = [[0,b],[b,0]] + diag(a,c)`.

The first summand has both singular values `|b|`, so Weyl gives

`s_min(B) >= |b|-max(|a|,|c|) > |b|-d >= kappa0`.

Therefore the **completed fleet02/B20 r52 indefinite-pair terminal applies at these actual inequalities** and pays the law, contrary to the assumed unpaid state. Hence

`boxed: |A_ij| < beta for every i!=j`.                         (3.1)

This is the designated partner result consumed in the new proof.

## 4. A new deterministic S3 disjoint-tetrad lemma

The previous B20 run used an S2 version. The full target supplies an extra singular mode and yields a substantially stronger inequality.

### Lemma 4.1 — `QFORM-ZERODIAG-S3-TETRAD-LOWERBOUND-v1`

Let `O=O^T` have zero diagonal, let `s_3(O)>=sigma>0`, and write

`rho = max_i ||O e_i||_2`,
`T = ||O||_F^2`.

Define the ordered disjoint tetrad energy

`W_2(O) = sum_{|I|=|J|=2, I cap J=empty} det O[I,J]^2`.

If `rho<sigma`, then

`boxed: W_2(O) >= 3 sigma^2 (sigma^2-rho^2)`.                  (4.1)

#### Proof

Let `x_1>=x_2>=...>=0` be the squared singular values, so `x_1,x_2,x_3>=s:=sigma^2` and `T=sum x_r`.

Cauchy-Binet gives `e_2(OO^T)` as the sum of squares of all `2x2` minors. For a symmetric zero-diagonal matrix, the total contribution of row/column pairs which are not disjoint is at most `rho^2 T` (the exact count is the same as in the preceding B20 S2 lemma). Therefore

`W_2(O) >= e_2(OO^T) - rho^2 T`.                              (4.2)

We now use the third mode. Let `S=x_1+x_2+x_3` and `R=T-S`. For fixed `S` with all three `x_i>=s`, the minimum of `x_1x_2+x_1x_3+x_2x_3` is attained at `(S-2s,s,s)`, so

`e_2(x_1,x_2,x_3) >= 2sS-3s^2`.                              (4.3)

The cross contribution between the top three and the tail is `SR>=3sR`; the tail-tail contribution is nonnegative. Thus

`e_2(OO^T) >= 2sS-3s^2+3sR`
`              = 3sT-sS-3s^2`
`              >= 2sT-3s^2`,                                  (4.4)

because `S<=T`. Combining (4.2)-(4.4),

`W_2(O) >= (2s-rho^2)T-3s^2`.

Finally `T>=3s`, and when `rho<sigma` the coefficient `2s-rho^2` is positive, so

`W_2(O) >= 3s(2s-rho^2)-3s^2`
`         = 3s(s-rho^2)`.

This is (4.1). QED.

## 5. No-large-star tiny-diagonal branch => fixed physical E2 cut

Write

`A = Delta + O`,

where `Delta=diag(A)` and `O` has zero diagonal. Since `||Delta||op<d` and `s_3(A)>=1`, Weyl gives

`s_3(O) > 1-d = sigma = 63/64`.                                (5.1)

Assume now that every physical off-diagonal row has norm at most `alpha`. Then `rho<=alpha<sigma`, so Lemma 4.1 gives

`W_2(A)=W_2(O)`
` >= 3 sigma^2 (sigma^2-alpha^2)`
` =: W_*`
` = 2.6411450136947678402066...`.                              (5.2)

The equality holds because a disjoint `2x2` cross minor contains no diagonal coefficient.

Randomly color every original coordinate left/right independently with probability `1/2`; let `M=A[L,R]`. Each ordered disjoint tetrad contributing to `W_2(A)` appears in the Cauchy-Binet expansion of `e_2(MM^T)` with probability exactly `1/16`. Therefore

`E e_2(MM^T) = W_2(A)/16`,                                    (5.3)

so some literal physical cut satisfies

`boxed: e_2(MM^T) >= W_*/16 = c2`
`       = 0.1650715633559229900129...`.                         (5.4)

No spectral-coordinate random variable has been introduced.

## 6. Spend any third cross-volume; otherwise the cut is ultrathin rank two

Let `y_1>=y_2>=...>=0` be the squared singular values of `M`, and put

`T_tail=sum_{r>=3} y_r = dist_F(M,rank<=2)^2`.

A useful elementary exterior-volume inequality is

`e_2(y) T_tail <= 3 e_3(y)`.                                   (6.1)

Indeed

`3e_3 = sum_{i<j} y_i y_j sum_{k!=i,j} y_k`,

and for every pair `i<j`, sortedness gives `y_i+y_j<=y_1+y_2`, hence

`sum_{k!=i,j}y_k >= sum_{k>=3}y_k=T_tail`.

Take `zeta=2^-24`. If `e_3(MM^T)>=zeta`, the already-proved marginal-free physical-E3 theorem applies to this literal cut, paying the **full ambient law** while retaining all same-bank curvature, all outside coordinates/couplings, signs, affine terms and extra spectrum. With the current E3 constant this is `<169`; this subbranch has a continuous `C_0` density.

Otherwise, (5.4) and (6.1) give

`dist_F(M,rank<=2)^2 < 3*2^-24/c2`,

hence

`boxed: dist_F(M,rank<=2) < 0.0010407934422325723...`.           (6.2)

This is coefficient geometry only: the nonzero rank-two tail is retained in `Q` and is not discarded probabilistically.

## 7. Large-star tiny-diagonal branch => fifteen diffuse physical arms

Assume instead that a literal hub `h` satisfies

`rho=||A[h,-h]||_2>alpha`.

Set `w_j=A_hj^2` and `S=sum_{j!=h}w_j=rho^2`. By the partner-driven entry cap (3.1),

`max_j w_j < beta^2`.

Numerically, with the actual r52 `kappa0`,

`beta^2/alpha^2 = 0.004070726016578102... < 1/240`,              (7.1)

so, since `S>alpha^2`, every atom satisfies

`w_j < S/240`.                                                   (7.2)

Greedily form a group from unused leaves until its accumulated weight first reaches `S/16`. Because each atom is `<S/240`, every completed group has weight

`S/16 <= weight < S/16+S/240 = S/15`.                          (7.3)

After at most fourteen such groups the consumed mass is `<14S/15`, leaving `>S/15>S/16`, so the construction succeeds fifteen times. This yields pairwise-disjoint literal groups `G_1,...,G_15` with (7.3). Therefore

`||A[h,G_q]||_2 >= rho/4 > alpha/4`
`                = 1007/16384`
`                = 0.06146240234375`.                           (7.4)

Thus failure of the no-large-star branch is not a one-edge phenomenon: pair-freeness forces the star to scatter over at least fifteen quantitatively strong physical arms. No density payment is claimed from the star alone; a third smoothing resource is still needed.

## 8. Updated first unpaid implication

Combining this run with the preceding fleet01/B20 moderate-diagonal theorem and fleet02/B20 r52, the formerly broad tiny-diagonal/star frontier reduces to

`QFORM-R52-ULTRATHIN-E2CUT-OR-15ARM-THIRDRESOURCE-PAYMENT-v1`:

- **ultrathin-cut endpoint:** a literal full cut has `e_2>=0.16507156` and, after every physical-E3 payment fails, is within Frobenius distance `<0.001041` of rank two;
- **diffuse-star endpoint:** a literal physical star is split into fifteen disjoint arms, each of norm `>0.0614624`, while every individual coefficient is `<0.0156858`;
- the r52 rank-12/rank-11 retained-tail/common-plane descriptors and both incident-collapse currencies remain present when applicable and are not deleted;
- the separate shared-bank nonzero-modulation minority/two-sheet endpoint remains separate and unresolved.

The next closure step should spend the target's remaining third spectral resource jointly with one of these two source-coordinate packets. For the ultrathin cut, the productive route is a rank-two crossing plus transverse same-bank curvature / finite-carrier receiver. For the fifteen-arm packet, the productive route is grouped hub+square / pair-completion aggregation, not a worst conditional-density supremum and not one-good-pair extraction.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full continuity: **OPEN**.
