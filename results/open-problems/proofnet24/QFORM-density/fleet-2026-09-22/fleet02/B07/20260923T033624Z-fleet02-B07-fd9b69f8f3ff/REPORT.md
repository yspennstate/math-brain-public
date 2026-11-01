SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T03:36:24Z.
attacking: fifth-volume versus relative rank-four tube; integrate the bounded-rank survivor into determinant-weighted physical-core extraction without selecting one tiny minor.

# fleet02/B07 — D5 payment or a rank-3/4 biheavy core, with bounded physical support paid separately

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Role:** Coordinate minor selection / complementary constructions and source-valid counterexamples  
**Run:** `20260923T033624Z-fleet02-B07-fd9b69f8f3ff`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW RANK-3-OR-4 CORE ALTERNATIVE / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target, correction boundary, and first unpaid implication

The target remains the unrestricted statement: for arbitrary dimension, arbitrary independent real original-coordinate inputs with one-dimensional probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential density bound for `Q=X^TAX`, or produce a valid target counterexample. No moments, compact support, connected support, iid, log-concavity, diagonal-basis hypothesis, or independence after a spectral rotation is introduced. Continuity is tracked separately.

The live corrections exclude law-uniform pointwise quadratic-phase decay, arbitrary-joint 3D coarea, worst conditional projection-density moments, and any assertion that aggregate compound mass contains one universally good coordinate minor. Every block below is an ORIGINAL-coordinate block, and all completed Fourier receivers used here retain arbitrary self blocks, outside couplings and affine terms.

**First unpaid implication after this run:** `QFORM-T4-RANK34-BIHEAVY-SUPPORT-DIFFUSE-PAYMENT-v1`. In the partner's four-bank no-pivot branch, after the large-star, low-rank-two, high-fifth-volume, diffuse-rank-3/4, and bounded-physical-support exits below have failed, pay a rank-3-or-4 singular core with (i) two heavy ORIGINAL physical coordinates, one on each side, (ii) every retained singular direction quantitatively non-negligible, (iii) a quantitatively operator-small remainder, and (iv) determinant volume still diffuse outside every fixed small physical support. The receiver must retain arbitrary within-bank quadratic curvature. The exact rank-three bi-anchor diffuse family from the previous B07 run shows that a bounded physical core cannot simply be asserted in this survivor.

## 2. Sources actually applied

The latest completed designated partner is fleet03/B07 r22, source

`yspennstate/math-open-problems@ac54330d3df42a48098ef7c704ac268382accd7c`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T030701Z-fleet03-B07-qform-r22/REPORT.md`.

Its incoming disjoint four-bank packet has star norms `C,R`, a disjoint physical cross block `M`, and

`C R F > kappa`, `F=||M||_F`, `kappa=1/(256 sqrt(3))`.                    (2.1)

For squared singular values `lambda_1>=lambda_2>=...` of `M`, put

`S=sum_j lambda_j=F^2`, `T_2=sum_{j>=3} lambda_j`.                         (2.2)

On the partner's non-low-tail branch `T_2>=theta S`, `0<theta<=1/2`, its proved tail-to-volume lemma gives

`E_3(M):=e_3(lambda) >= (theta^2/6) S^3`.                                 (2.3)

The mandatory newest-Claude e5 source actually used at an inequality is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

Its proved fifth-volume theorem D5 says for any physical cross block, with no determinant-marginal condition,

`||p_Q||_infinity <= 5 sqrt(2e) E_5(M)^(-1/10)`.                           (2.4)

The newer volume-stability theorem used below is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

If `M=M0+E`, `s_3(M0)>=a>0`, `max diag P_range(M0)<=1/2`, and `||E||op<=a/16`, then the full form has a continuous density with

`||p_Q||_infinity < 23/a`.                                                 (2.5)

The previous own-slot physical-support receiver, used in Section 7, is

`yspennstate/math-open-problems@1f5ab2ddba6e99675fb9177666c5e64e396e54e5`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T023322Z-r11/REPORT.md`.

## 3. Compound-tail ladder

Let `lambda_1>=lambda_2>=...>=0`, `E_k=e_k(lambda)`, and

`T_k=sum_{j>k} lambda_j`.                                                   (3.1)

Thus `sqrt(T_k)` is exactly the Frobenius distance from `M` to its best rank-`k` truncation.

### Lemma 3.1 — `QFORM-COMPOUND-TAIL-LADDER-v1`

For every `k>=1`,

`boxed: T_k E_k <= (k+1) E_{k+1}.`                                         (3.2)

### Proof

Expand by first choosing a `k`-subset:

`(k+1)E_{k+1}
 = sum_{|I|=k} (prod_{i in I} lambda_i) (sum_{j notin I} lambda_j).`         (3.3)

The top `k` indices maximize the removed sum, so every complement sum in (3.3) is at least `T_k`. Hence

`(k+1)E_{k+1}
 >= T_k sum_{|I|=k} prod_{i in I}lambda_i
 =T_k E_k`. QED.

For `k=3,4`,

`T_3 E_3<=4E_4`, `T_4 E_4<=5E_5`.                                         (3.4)

Since `T_3>=T_4`,

`boxed: E_5 >= (T_3 T_4/20)E_3 >= (T_4^2/20)E_3.`                          (3.5)

Consequently

`boxed: dist_F(M,{rank<=4})=sqrt(T_4) <= (20E_5/E_3)^(1/4).`               (3.6)

This is an aggregate compound estimate. No physical minor is selected.

## 4. D5-or-relative-rank-four dichotomy

Assume the partner non-low-tail bound (2.3). Fix `eta>0`.

If

`E_5(M)>=eta S^5=eta F^10`,                                               (4.1)

then the e5 D5 theorem (2.4) gives the actual full-form estimate

`boxed: ||p_Q||_infinity <=5sqrt(2e) eta^(-1/10) F^(-1).`                  (4.2)

If the partner's large-star branch has also failed, `CR<=Lambda`, then (2.1) implies `F>kappa/Lambda`, and

`boxed: ||p_Q||_infinity <5sqrt(2e) eta^(-1/10) Lambda/kappa.`             (4.3)

This is the requested equation-level use of a completed e5 result.

Suppose instead

`E_5(M)<eta S^5`.                                                          (4.4)

By (2.3) and (3.5),

`T_4^2 <=20 E_5/E_3
       < (120 eta/theta^2) S^2`.                                          (4.5)

Thus

`boxed:
 dist_F(M,{rank<=4})/F
 < (120 eta/theta^2)^(1/4).
`                                                                             (4.6)

The point is scale invariance: a failure of the fifth-volume receiver does not merely say `E_5` is small; relative to the already forced `E_3`, it puts the whole physical cross block in a dimension-free Frobenius tube around rank four.

## 5. Quantitative reduction from the rank-four tube to rank 3 or 4

Set the fixed threshold

`eta_*(theta)=theta^6/(120*3072^2).`                                       (5.1)

Assume (4.4) with `eta=eta_*(theta)`. Then (4.5) gives

`rho:=T_4/S < theta^2/3072`.                                                (5.2)

Let `M_4` be the top-four singular truncation. Write `E_3^(4)=e_3(lambda_1,...,lambda_4)`. The contribution to `E_3(M)` from terms using at least one tail eigenvalue is exactly

`E_2^(4) T_4 + E_1^(4)e_2(tail)+e_3(tail)`.                                (5.3)

Using `E_2^(4)<=S^2/2`, `E_1^(4)<=S`, `e_2(tail)<=T_4^2/2`, and `e_3(tail)<=T_4^3/6`,

`E_3(M)-E_3^(4)
 <= S^3 (rho/2+rho^2/2+rho^3/6).`                                          (5.4)

For `rho<=1/4`, the parenthesis is below `(2/3)rho`. Since (5.2) is much smaller than `theta^2/8`, equations (2.3)-(5.4) yield the convenient bound

`boxed: E_3^(4) >= (theta^2/12) S^3.`                                      (5.5)

Now every one of the four triple products in `E_3^(4)` is at most `lambda_1 lambda_2 lambda_3`, while `lambda_1 lambda_2<=S^2/4`. Therefore

`E_3^(4)<=4 lambda_1lambda_2lambda_3<=S^2 lambda_3`.                        (5.6)

Combining with (5.5),

`boxed: s_3(M)>=a:=theta F/sqrt(12).`                                      (5.7)

Furthermore, `s_5(M)^2=lambda_5<=T_4`, so (5.2) and (5.7) give

`boxed: s_5(M)<=a/16.`                                                     (5.8)

This is the crucial dimensional compression: after D5 fails at the scale (5.1), three singular directions are quantitatively substantial and everything beyond the first four is operator-small at exactly the stability scale.

## 6. Main new structural theorem

### Theorem 6.1 — `QFORM-T4-D5-OR-RANK34-BIHEAVY-v1`

Assume the partner T4 packet (2.1). Fix `Lambda>0` and `0<theta<=1/2`. Suppose the large-star and low-rank-two alternatives fail:

`CR<=Lambda`, `T_2>=theta F^2`.                                             (6.1)

Put `eta_*=eta_*(theta)` as in (5.1), and `a=theta F/sqrt(12)`.

Then at least one of the following holds.

**(A) Fifth-volume payment.**

`E_5(M)>=eta_*F^10`, and the full ambient form satisfies

`||p_Q||_infinity
 <=5sqrt(2e) eta_*^(-1/10) Lambda/kappa`.                                   (6.2)

**(B) Stable diffuse rank-3/4 payment.**

The full ambient form has a continuous density satisfying

`boxed: ||p_Q||_infinity <23/a
       <23sqrt(12) Lambda/(theta kappa).`                                   (6.3)

**(C) Rank-3-or-4 biheavy core.**

There is `r in {3,4}` and the top-`r` singular truncation `M_r` such that

`rank(M_r)=r`, `s_3(M_r)>=a`, `||M-M_r||op<=a/16`,                          (6.4)

and if `r=4` also

`s_4(M_r)>a/16`.                                                            (6.5)

Moreover both ORIGINAL-coordinate range projections are heavy: there exist a physical row coordinate `i` and a physical column coordinate `j` with

`(P_range(M_r))_ii>1/2`, `(P_range(M_r^T))_jj>1/2`.                         (6.6)

The corresponding retained-core row and column norms obey

`boxed:
 ||e_i^T M_r||_2,
 ||M_r e_j||_2
 > a/(16sqrt(2))
 > theta kappa/(16sqrt(24) Lambda).
`                                                                             (6.7)

### Proof

If (A) fails, Sections 4-5 give (5.7)-(5.8).

If `s_4(M)<=a/16`, take `r=3`, `M_r=M_3`. Then `s_3(M_3)>=a` and the exact singular truncation identity gives

`||M-M_3||op=s_4(M)<=a/16`.                                                 (6.8)

If either the left top-three range projection or the right top-three range projection has maximum physical leverage at most `1/2`, apply the stability theorem (2.5), transposing `M` if needed, and obtain (B). If neither side is diffuse, choose physical coordinates satisfying (6.6). Because every retained singular value is at least `a`,

`||e_i^T M_3||^2 >=a^2(P_range(M_3))_ii>a^2/2`,                            (6.9)

and similarly on the column side. This is stronger than (6.7).

If instead `s_4(M)>a/16`, take `r=4`, `M_r=M_4`. Equation (5.8) gives the operator-tail condition in (6.4), while (6.5) holds by the case assumption. Again, if either rank-four range projection is diffuse, (2.5) yields (B). Otherwise choose heavy physical row/column coordinates. Since the smallest retained singular value is now `s_4>a/16`,

`||e_i^T M_4||^2
 >=s_4^2(P_range(M_4))_ii
 >a^2/(512)`,                                                              (6.10)

and similarly on the column side, which is exactly (6.7). QED.

This improves the partner r22 high-dimensional selected core in a different direction. Once the new D5 split is inserted, the genuinely unpaid core can be taken to have **rank only three or four**, every retained direction has a quantitative scale, and the operator remainder is already at the volume-stability threshold. The price is a very large but universal constant in the paid alternatives; no constant optimization is intended.

For the partner's convenient `theta=1/16`, `Lambda=1`,

`eta_*=1/18999560927969280 =5.2632795241e-17`.                              (6.11)

The two paid bounds are approximately

`D5 branch <2.19436e5`, `stability branch <5.65248e5`,                       (6.12)

and any surviving biheavy core has physical retained-core row and column norms greater than

`1.79827e-6`.                                                               (6.13)

Only universality matters here.

## 7. Integration with the actual bounded physical-core receiver

The rank-3/4 core in Theorem 6.1 is a singular core, not yet a bounded set of physical coordinates. The previous B07 theorem `QFORM-DETERMINANT-MARGINAL-TAIL-CORE-v1` supplies the correct interface and prevents a false one-minor conclusion.

Normalize the **actual** third-volume squares of `M` to a determinant law and let `delta_R,delta_C` be the row/column inclusion-marginal tails outside physical supports `R0,C0`, each of size at most `m`. If

`delta_R+delta_C<=1/2`,                                                     (7.1)

then at least half of `E_3(M)` lies on the physical block `M[R0,C0]`. The previous theorem conditions only outside the original-coordinate core and gives

`||p_Q||infinity
 <=2sqrt(6pi |R0 union C0|) sqrt(binom(m,3)) ||M[R0,C0]||op^2
     /sqrt(E_3(M)/2).`                                                      (7.2)

Using `|R0 union C0|<=2m`, `||M[R0,C0]||op<=F`, and (2.3),

`boxed:
 ||p_Q||infinity
 <= [24 sqrt(pi m binom(m,3))/(theta F)]
 < [24 sqrt(pi m binom(m,3)) Lambda/(theta kappa)].
`                                                                             (7.3)

Thus **every bounded-support portion of the new rank-3/4 branch is already paid without selecting any individual minor**. For example `m=4` is a completely explicit eight-coordinate receiver.

Consequently the actual survivor after Theorem 6.1 and (7.3) is not merely “a heavy low-rank core.” It must simultaneously be:

- rank `3` or `4` up to an operator error at most `a/16`;
- biheavy in original physical coordinates as in (6.6)-(6.7);
- and determinant-support-diffuse, in the sense that (7.1) fails for every fixed bounded support size at which one attempts the physical-core exit.

That is a substantially narrower interface for the hub/star workers than the incoming arbitrary-rank T4 packet.

## 8. Exact obstruction to a stronger bounded-core conclusion

The preceding support-diffuse condition is real. The prior B07 source-valid target family can be reused as a regression against the tempting but false strengthening “biheavy rank-3/4 core implies bounded physical spectral core.”

For even `N`, let

`u=v=N^(-1/2)(1,...,1)`, `x=y=N^(-1/2)((-1)^j)_j`,

`M_N=[[0,u^T],[v,xy^T]]`, `A_N=[[0,M_N],[M_N^T,0]]`.                        (8.1)

The singular values of `M_N` are exactly `1,1,1`, so `A_N` has nonzero spectrum `{+1,+1,+1,-1,-1,-1}`. The top-three left and right range projections each contain the physical anchor exactly, hence have a diagonal entry equal to one: this is maximally biheavy. Yet every fixed-cardinality physical principal block has operator norm `O(N^(-1/2))`, while the anchored third-volume mass remains one and its residual coordinate inclusion marginals are exactly `2/N`.

Therefore even an **exact rank-three**, zero-remainder, biheavy core need not yield a bounded physical spectral core. The survivor in Section 7 cannot be eliminated by a deterministic bounded-cardinality selection lemma.

This family is not a QFORM counterexample. The mandatory e5 mixed-hub theorem pays it by the special low-rank residual geometry, giving `||p_Q||infinity<=3*2^(1/3)<3.780`, as proved in the previous run. What remains here is the same support-diffuse biheavy geometry with **arbitrary same-side quadratic curvature**, outside that special mixed-hub light-block hypothesis.

## 9. Deterministic verification

The companion exact checker verifies on every nonincreasing integer spectrum with entries in `{1,...,5}` and lengths `5,...,8` the inequalities

`T_3E_3<=4E_4`, `T_4E_4<=5E_5`, `20E_5>=T_4^2E_3`,

for 1161 spectra. It also records the exact `theta=1/16` value of `eta_*` and the constants in (6.12)-(6.13). The checker is a regression only; the proof is Sections 3-7.

## 10. End-to-end position

Starting from fleet03/B07 r22, the T4 branch now routes as follows. If `CR>Lambda`, retain the genuine two-star branch. If `T_2<theta F^2`, retain the partner's near-rank-two branch. Otherwise, the mandatory e5 D5 theorem either pays a substantial fifth volume, or the new compound-tail ladder forces a relative rank-four tube. At the explicit scale (5.1), the c241 stability theorem then either pays the tube or leaves only a rank-3/4 biheavy singular core with a small operator remainder. If its determinant mass has bounded physical support, the previous aggregate physical-core theorem pays that as well. No reciprocal single-minor step appears anywhere in this chain.

The first unpaid implication is therefore exactly the one stated in Section 1: pay the remaining **support-diffuse rank-3/4 biheavy core with arbitrary curvature**, or route it to a valid pair/zero-pivot/grouped/hub mechanism without rotating the input law. Full QFORM and global continuity remain OPEN / NOT PROVED / NOT DISPROVED. Independent review of the new theorem is not claimed.
