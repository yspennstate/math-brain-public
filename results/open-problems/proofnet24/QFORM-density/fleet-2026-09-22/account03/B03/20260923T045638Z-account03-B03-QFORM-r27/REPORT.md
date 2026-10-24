SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T04:56:38Z.
attacking: the heavy-right-plane endpoint by pivoting the actual heavy physical coordinate, computing its exact rank-two Schur determinant, and feeding that determinant into a dependence-safe half-Riesz time estimate.

# account03/B03 r27 — heavy-row Schur half-Riesz receiver

**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

The full owner target remains open. Nothing below rotates the independent physical coordinates into independent eigen-coordinates, assumes a law-uniform pointwise quadratic-phase decay, conditions on a sum/difference variable, or invokes the refuted arbitrary-joint coarea/conditional-density interfaces. The conclusion below pays a genuine current endpoint of the exact-rank-three proof route and narrows its remaining heavy-row obstruction to an explicit cancellation regime.

## 1. Source-valid inputs actually used

1. **Orientation-free rank-two fractional estimate.** Complete source:
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
   For an exact rank-two quadratic form with nonzero eigenvalue matrix `Lambda` and no affine term,

   `sup_t E |W^T K W-t|^(-1/2) <= 16 sqrt(30) |det Lambda|^(-1/4)`.

   The more general arbitrary-affine version has constant `128`; this run uses the sharper no-affine case.

2. **Current one-sided overlap geometry.** Account01/B06 r21 and r24:
   `yspennstate/math-open-problems@32bffc770e83aa6de4175a2a526e0a0670de1a5b:proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T013242Z-qform-r21-b06/REPORT.md`, and
   `yspennstate/math-open-problems@9838f01d705e379c6ff9b855bf1bb787d94b1c5c:proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T043620Z-account01-B06-QFORM-r24/REPORT.md`.
   They reduce one exact-rank-three zero-Schur-diagonal endpoint to a physical representation described below, with `x^2<1/6`, `y^2>1/2`, and a right-plane row of leverage `eta>1/2` in the still-unpaid heavy branch.

3. **Designated partner account04/B03.** Canonical source:
   `yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38:proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260922T193150Z-account04-B03-collision-l2-r1/REPORT.md`.
   Its weighted-L2 compiler is not used: its time-weight step was subsequently refuted. The elementary lemma

   `P(|Y-Y'|<=eps) <= 2 eps ||p_Y||_2^2`

   is valid and is applied in Section 6.

## 2. Exact physical packet

Let the original independent coordinates be split into a left bank `L`, right bank `R`, a physical pivot `i`, and possibly a residual bank `K`. In the exact-rank-three one-sided-overlap branch, the full homogeneous form has the product-preserving representation

`Q = a^(-1) H^2 + 2 sigma U V`,                                      (2.1)

where

`H = a X_i + h_L.X_L + h_R.X_R + h_K.X_K`,
`U = u.X_L`, `V=v.X_R`,                                             (2.2)

`u` and `v` are unit vectors, and

`h_R = beta v + m q`,                                                (2.3)

with `q` unit and orthogonal to `v`, `m>0`. In the r21 notation,

`m=rho y`, `rho^2=a^2+||k||^2`, `gamma=rho^2/|a|`,                  (2.4)

and the spectral identity gives

`gamma |sigma| >= s_3(A)^2`.                                        (2.5)

The r24 heavy endpoint supplies an actual physical right-bank coordinate `r` satisfying

`eta_r := v_r^2+q_r^2 > 1/2`.                                       (2.6)

Write

`h_r := beta v_r + m q_r`.                                          (2.7)

This run treats every such heavy row with `h_r !=0` and quantifies exactly what remains when `h_r` is small.

## 3. Heavy-row pivot and exact Schur residual

Set `z=X_r`. Removing the `r`th right coordinate, write

`H=h_r z+H_0`, `V=v_r z+V_0`.                                       (3.1)

Then

`Q=(h_r^2/a) z^2 + 2z[(h_r/a)H_0+sigma v_r U]
   +(1/a)H_0^2+2sigma U V_0`.                                       (3.2)

Since `h_r!=0`, completing the square in the **original physical coordinate** `z` gives

`Q = d [z+c(W)]^2 + R(W)`, `d=h_r^2/a`,                            (3.3)

where `W` denotes all original coordinates except `z` and

`R = 2 sigma U L - (a sigma^2 v_r^2/h_r^2) U^2`,                   (3.4)

`L = V_0-(v_r/h_r)H_0`.                                             (3.5)

No conditioning or spectral-coordinate independence is involved.

Let `ell` be the physical coefficient vector of the linear form `L` on the remaining coordinates. The component of `ell` on `R\{r}` is

`ell_{R\{r}}
 = v_- -(v_r/h_r)(beta v_-+m q_-)
 = (m/h_r)(q_r v_- - v_r q_-)`.                                    (3.6)

Because `v,q` are orthonormal,

`||q_r v_- - v_r q_-||_2^2 = v_r^2+q_r^2 = eta_r`.                (3.7)

The left vector `u` is supported on the disjoint bank `L`. Therefore, with

`b := ||P_{u^perp} ell||_2`,                                        (3.8)

we obtain the quantitative transverse bound

`boxed: b >= m sqrt(eta_r)/|h_r|`.                                  (3.9)

The quadratic matrix of `R` lives on `span(u,ell)` and, in the orthonormal basis `(u,e)` with `e` in the direction of `P_{u^perp}ell`, has the form

`[[2 sigma alpha-c, sigma b],[sigma b,0]]`,                         (3.10)

for real `alpha` and `c=a sigma^2 v_r^2/h_r^2`. Hence it has exact rank two and its nonzero eigenvalue product satisfies the **exact identity**

`|pdet(R_quad)| = sigma^2 b^2`,                                     (3.11)

and consequently

`boxed:
 |pdet(R_quad)| >= sigma^2 m^2 eta_r / h_r^2.
}`                                                                   (3.12)

This is the key new certificate. It is an aggregate physical Schur determinant obtained after pivoting the heavy row; no single tiny cross minor is inverted.

## 4. Translation-uniform half-Riesz and assigned time integral

Apply the completed orientation-free rank-two theorem to the residual `R`. There is no affine term in the homogeneous packet, so the sharper constant applies:

`sup_s E|R-s|^(-1/2)
 <= 16 sqrt(30) |pdet(R_quad)|^(-1/4)`

`<= 16 sqrt(30)
    sqrt( |h_r| / (|sigma| m sqrt(eta_r)) ).`                       (4.1)

Let `R'` be an independent copy of the **whole residual**. The exact Riesz identity gives

`int_R |t|^(-1/2)|phi_R(t)|^2 dt
 = sqrt(2 pi) E|R-R'|^(-1/2)`.                                     (4.2)

Conditioning only on `R'` and using (4.1),

`boxed:
 int_R |t|^(-1/2)|phi_R(t)|^2 dt
 <= 16 sqrt(60 pi)
    sqrt( |h_r| / (|sigma| m sqrt(eta_r)) ).
}`                                                                   (4.3)

The numerical outside coefficient is

`16 sqrt(60 pi)=219.6698958873045...`.

This is a dependence-safe decoupled-time estimate. The independent-copy operation is performed on the entire residual random variable. At no point are any `X_j-X'_j` and `X_j+X'_j` declared independent or separately density-capped.

## 5. Linear small-ball scaling after the same physical pivot

For every deterministic shift `c`, the square pushforward of a cap-one scalar obeys

`p_{d(Z+c)^2}(w) <= |d|^(-1/2)|w|^(-1/2)`.                         (5.1)

Applying this conditionally to the actual physical coordinate `z=X_r` in (3.3), and then using (4.1), gives

`||p_Q||_infinity
 <= |d|^(-1/2) sup_s E|R-s|^(-1/2)`

`<= 16 sqrt(30)
    sqrt( |a| / (|sigma| m sqrt(eta_r) |h_r|) ).`                   (5.2)

Thus every interval `I` satisfies

`boxed:
 P(Q in I)
 <=16 sqrt(30)
   sqrt( |a| / (|sigma| m sqrt(eta_r) |h_r|) ) |I|.
}`                                                                   (5.3)

This proves essential boundedness on the stated heavy-row packet. Continuity is **not** proved by this receiver.

### Target-normalized consequence in the r24 endpoint

In the one-sided endpoint, `m=rho y`, `y^2>1/2`, `eta_r>1/2`, and (2.5) holds. Therefore

`|a|/(|sigma| m sqrt(eta_r)|h_r|)
 <= 2 rho/[s_3(A)^2 |h_r|]`.                                       (5.4)

Hence

`boxed:
 ||p_Q||_infinity
 <= (16 sqrt(60)/s_3(A)) sqrt(rho/|h_r|).
}`                                                                   (5.5)

Under the owner normalization `s_3(A)>=1`, every heavy row satisfying `|h_r|>=theta rho` is paid by

`||p_Q||_infinity <=16 sqrt(60/theta)`.                             (5.6)

For example `theta=1/8` gives the explicit universal constant

`16 sqrt(480)=350.5424368033063...`.                               (5.7)

Therefore the formerly generic heavy-right-plane endpoint is narrowed further: after the diffuse-plane branch is paid by account01/B06 r24, the only state not paid by the present receiver is a **heavy leverage row whose square coefficient is simultaneously angularly cancelled**, `|h_r|/rho ->0` (including the exact `h_r=0` endpoint).

## 6. Designated partner applied to an actual inequality

Let `Q'` be an independent copy. Since `p_Q` is a probability density,

`||p_Q||_2^2 <= ||p_Q||_infinity`.                                 (6.1)

Apply the valid account04/B03 collision lemma:

`P(|Q-Q'|<=eps) <=2 eps ||p_Q||_2^2`.                              (6.2)

Combining with (5.2) gives the actual partner-consumed estimate

`boxed:
 P(|Q-Q'|<=eps)
 <=32 sqrt(30)
   sqrt( |a| / (|sigma| m sqrt(eta_r)|h_r|) ) eps.
}`                                                                   (6.3)

In the target-normalized one-sided endpoint this becomes

`P(|Q-Q'|<=eps)
 <=(32 sqrt(60)/s_3(A)) sqrt(rho/|h_r|) eps`.                       (6.4)

The partner's refuted weighted-L2 compiler is not used.

## 7. Algebra/arithmetic checks

A direct finite-dimensional check of (3.11) was performed on random orthonormal pairs `(v,q)`: the two nonzero eigenvalues of the residual matrix had product `sigma^2 b^2` to floating-point precision in each trial, while (3.9) supplied the stated lower bound. Exact constants used above are

`16 sqrt(30)=87.63560920082658...`,
`16 sqrt(60)=123.93546707863734...`,
`16 sqrt(60 pi)=219.66989588730453...`,
`16 sqrt(480)=350.5424368033063...`.

The identities (3.6)-(3.12), rather than the finite computation, are the proof.

## 8. What remains

The unrestricted three-large-eigenvalue theorem remains **OPEN** and the full continuity conclusion remains **OPEN**.

Within the current exact-rank-three one-sided-overlap endpoint, the new first unpaid implication is now more specific:

`QFORM-HEAVY-ROW-ANGULAR-CANCELLATION-ENDPOINT-v1`:

> exploit `eta_r>1/2` together with `|beta v_r+m q_r| << rho` without deleting the small transverse term, and route it to the exact/near-coloop, grouped-hub, or aggregate-volume mechanism with a constant stable as `h_r ->0`.

The present result is deliberately not advertised as a full proof and does not switch to an easy subclass: it advances the currently identified heavy physical-row survivor of the full-target route.
