SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T17:30:57Z.
attacking: route the at-most-two-ORIGINAL-coordinate fused-volume concentration branch into localized square mass versus a quantitative transverse chain hub, retaining the complete physical cross block and all conditioning weights.

# account02/B06 — fused concentration splits into localized square or transverse chain hub

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `b06-20260923T173057Z-64327663bdd3`  
**Status:** `NEW SUPPORTING STRUCTURAL LEMMA + TARGET-LEVEL OBSTRUCTION PAID / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. All coordinates below are ORIGINAL independent coordinates with one-dimensional densities bounded by one. No moment, support, log-concavity, iid, diagonal-basis, post-rotation independence, or continuity assumption is added.

## 1. First unpaid implication

The preceding B06 run proved `QFORM-FUSION-GATE-OR-2HUB-CONCENTRATION-v1`: in the rank-one-Fresnel / one-cross-volume setup, either the weighted Brascamp--Lieb gate pays the density, or more than `3/4` of the fused determinant mass touches at most two original coordinates. It also showed that such concentration need not make the corresponding physical cross row large.

The first unpaid implication here is therefore:

`QFORM-FUSED-2HUB-CONCENTRATION-ROUTING-v1`.

The goal of this run is to identify exactly what the concentrated fused mass *does* force before attempting a new analytic receiver.

Fresh designated partner: account03/B06 r39, canonical mathematics

`yspennstate/math-open-problems@9ac8f055fe86ee993b00125fdcfbc1d528147632`,

which keeps the complete cross tail and on the live near-rank-two physical block `N` gives

`x_2 > 11907/1048576`,

where `x_2` is the second squared singular value.

The owner-required pinned newest-Claude package actually consumed is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed localized three-coordinate Theorem A is applied in Section 6 to a genuine target obstruction produced by the present structural split.

## 2. Fused setup

Consider the physical-coordinate form

`Q = X^T(D + lambda v v^T)X + 2 X^T M Y + R(Y) + affine`,              (2.1)

where `D` is diagonal in the original `X` coordinates, `||v||_2=1`, `M` is the COMPLETE physical cross block, and `R` is arbitrary. Put

`C=(I-vv^T)M`,
`Z=||C||_F^2`.                                                         (2.2)

Assume `Z>0`. For `p<q` and a physical cross column `t`, define

`w_{pqt}=(v_p M_{qt}-v_q M_{pt})^2/Z`.                                (2.3)

Lagrange's identity, column by column, gives `sum w_{pqt}=1`. The preceding B06 exact row-marginal identity is

`alpha_i := P_w(i in {p,q})
          = v_i^2 + ||C_{i,*}||_2^2/Z`.                               (2.4)

The point is that `C`, not `M`, is the cross curvature genuinely transverse to the same-bank square.

## 3. Main new structural split

### Theorem 3.1 — `QFORM-FUSED-CONCENTRATION-SQUARE-OR-TRANSVERSE-HUB-v1`

Let `H` be any set of at most two original `X` coordinates and let

`tau_H := P_w({p,q} intersect H != empty)`.                            (3.1)

Then

`||v_H||_2^2 + ||C_H||_F^2/Z
   = sum_{h in H} alpha_h
   = E_w |{p,q} intersect H|
   >= tau_H`.                                                          (3.2)

Consequently, if `tau_H>3/4`, then at least one of the following holds:

**(S) Localized-square branch**

`||v_H||_2^2 > 1/2`.                                                   (3.3)

**(T) Transverse-residual-hub branch**

there is `h in H` such that

`||C_{h,*}||_2 > sqrt(Z/8)`.                                           (3.4)

#### Proof

The equality in (3.2) is just (2.4) summed over `H`. A sampled pair contributes `0,1`, or `2` to `|{p,q} intersect H|`, and contributes at least one whenever it touches `H`; hence the final inequality.

If (3.3) fails, then `||v_H||^2<=1/2`, so (3.2) and `tau_H>3/4` imply

`||C_H||_F^2/Z > 1/4`.                                                 (3.5)

Because `|H|<=2`, one row has squared norm greater than `Z/8`. QED.

This is strictly stronger than the preceding statement that two physical coordinates carry most fused mass: failure of square localization forces a dimension-free *row norm in the transverse residual*, while retaining every cross-tail coordinate.

## 4. Exact light-bank rank-one identity

The same concentration has a second exact interpretation that is useful for routing.

Let `K=H^c`, set `s^2=||v_K||_2^2`, and define the fused mass completely avoiding `H`,

`Z_K := sum_{p<q in K,t}(v_pM_{qt}-v_qM_{pt})^2`.                     (4.1)

If `s>0`, define

`r^T := s^{-2} v_K^T M_K`.                                             (4.2)

Then

`boxed: Z_K = s^2 ||M_K-v_K r^T||_F^2.`                               (4.3)

#### Proof

For one column `m=M_{K,t}`, Lagrange's identity on the coordinates in `K` gives

`sum_{p<q in K}(v_p m_q-v_q m_p)^2
 = ||v_K||^2 ||m||^2-(v_K^T m)^2
 = s^2 ||m-v_K(v_K^Tm)/s^2||^2`.                                      (4.4)

Sum over `t`. QED.

Since `Z_K/Z=P_w({p,q} subset K)=1-tau_H`, the concentrated branch `tau_H>3/4` yields

`||M_K-v_K r^T||_F < sqrt(Z)/(2s)`.                                   (4.5)

If the localized-square branch (3.3) fails, then `s^2>=1/2`, hence

`boxed: ||M_K-v_K r^T||_F < sqrt(Z/2).}`                               (4.6)

Thus the nonlocalized survivor is not an arbitrary cross matrix: away from at most two original rows it is quantitatively close, in the *same fused currency*, to a common rank-one row pattern parallel to `v_K`.

## 5. Partner r39 applied at an actual inequality

On partner r39's complete near-rank-two physical cross block `N`, for every unit `v`,

`Z=||(I-vv^T)N||_F^2
 >= sum_{j>=2} x_j
 >= x_2
 > 11907/1048576`.                                                     (5.1)

Apply Theorem 3.1 to the previous B06 concentrated branch. If `||v_H||^2<=1/2`, some original coordinate `h in H` obeys

`boxed:
 ||C_{h,*}||_2
 > sqrt(11907/8388608)
 = 0.0376752572742529... .}`                                           (5.2)

There is then a further exact physical split because

`C_h=M_h-v_h(v^TM)`.                                                   (5.3)

By the triangle inequality, (5.2) implies at least one of

`boxed: ||M_h||_2 > 0.0188376286371264...}`                            (5.4)

or

`boxed: |v_h| ||v^T M||_2 > 0.0188376286371264... .}`                  (5.5)

So the previous vague two-coordinate concentration branch becomes a three-way, product-coordinate certificate:

1. more than half of the same-bank square lies on at most two original coordinates;
2. an actual physical cross hub has a dimension-free row norm; or
3. a dimension-free two-step chain runs through physical coordinate `h`, the square vector `v`, and the common cross coefficient `v^TM`.

No local minor is inverted and no singular tail is deleted.

## 6. Stronger candidate refuted inside a genuine target

A tempting strengthening would replace the transverse row `C_h` in branch (T) by the physical cross row `M_h`. That is false even when the square is *not* localized on `h`.

Take

`v=(3/5,4/5)`, `M=(0,4)^T`, `lambda=4`, `D=0`, `R=0`.                  (6.1)

Then

`4vv^T = [[36/25,48/25],[48/25,64/25]]`,

and the full symmetric three-coordinate matrix is

`A_* = [[36/25,48/25,0],
        [48/25,64/25,4],
        [0,4,0]].`                                                     (6.2)

There is only one fused pair `{1,2}`, so for `H={1}` we have `tau_H=1`, while

`v_1^2=9/25<1/2`,
`M_{1,*}=0`.                                                           (6.3)

Nevertheless

`C=(I-vv^T)M=(-48/25,36/25)^T`,
`Z=144/25`,
`alpha_1=9/25+(2304/625)/(144/25)=1`.                                 (6.4)

So this lies strictly in the transverse-residual branch while the alleged physical hub row vanishes exactly.

This is not a counterexample to QFORM. The characteristic polynomial of `A_*/4` is

`(25 t^3-25 t^2-25 t+9)/25`.                                          (6.5)

For `|t|<=1/4`,

`25 t^3-25 t^2-25 t+9
 >= 9-25(1/64+1/16+1/4)
 = 51/64>0`,                                                           (6.6)

so `A_*/4` has no eigenvalue in `[-1/4,1/4]`; since it is symmetric, every eigenvalue of `A_*` has modulus greater than one. Hence (6.2) is an exact target matrix with three large eigenvalues.

Now apply the completed localized three-coordinate **Theorem A** from the owner-required pinned `COUNTEREXAMPLE_SEARCH.md`: conditioning is unnecessary because the whole form is three-dimensional, and `sigma_min_abs(A_*)>1`. It gives the real all-law bound

`boxed: ||p_{X^T A_* X}||_infinity <= 6 sqrt(pi)
       =10.6347231054... .}`                                          (6.7)

Thus the stronger physical-row inference fails inside the exact target, but the target instance is uniformly paid. The example identifies the correct object for the unresolved compiler: the determinant-chain residual `C_h`, not `M_h` alone.

## 7. What changed in the proof map

The previous unpaid branch was merely “at most two coordinates carry most fused determinant mass.” The present identities refine it into a deterministic source-valid compiler:

`fused 2-coordinate concentration`

`=> localized square on <=2 original coordinates`

`   OR transverse residual row >=0.037675 on the live r39 packet`

`=> physical cross hub >=0.0188376`

`   OR rank-one chain product |v_h| ||v^TM|| >=0.0188376`.

The example (6.2) proves that the final chain alternative is indispensable; it cannot be replaced by a strong physical cross row.

## 8. First remaining implication

The first unpaid implication is now

`QFORM-TRANSVERSE-CHAIN-HUB-RECEIVER-v1`:

> In partner r39's complete near-rank-two physical tube, retain arbitrary original-coordinate diagonal twist `D`, arbitrary opposite-bank quadratic curvature `R`, and the full cross tail. On the nonlocalized branch, use either the physical-row lower bound (5.4) or the chain product lower bound (5.5), together with the third large spectral direction, to obtain an all-level product-preserving density bound; alternatively route the localized-square branch (3.3) into an already-paid physical-pair / grouped-square / projected-crossing receiver. The receiver must depend on the determinant chain itself and must not replace it by a worst conditional fiber supremum.

This is strictly narrower than the preceding fused-concentration debt and explicitly preserves the only cancellation pattern exhibited by the target example (6.2).

## 9. Verification scope

A deterministic finite checker verifies the exact row-marginal identity, the complement identity (4.3), the partner numerical constants, and the target example's spectrum. Random checks are sanity checks only; the universal statements above are proved algebraically.

Full QFORM status: **OPEN / NOT PROVED / NOT DISPROVED**. Essential boundedness is claimed only in the explicit paid branches above; no new continuity claim is made.
