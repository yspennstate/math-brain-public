# fleet02/B07 early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`; full conjecture remains OPEN. This run attacks the actual bounded-coordinate receiver first, then the latest fleet03/B07 r26 BICORE survivor without selecting an individual coordinate minor.

## Sources already applied at equations

- own completed `QFORM-DETERMINANT-MARGINAL-TAIL-CORE-v1`, `yspennstate/math-open-problems@1f5ab2ddba6e99675fb9177666c5e64e396e54e5`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T023322Z-r11/REPORT.md`;
- fleet01/B07 r19 coarse determinant-role theorem, observed on `math-open-problems` master before this write, giving one packet with `P0>=1/256`, `P1>=4/3125`, `P2>=1/256`, or `P3>=1/4`, and a heavy-support core/diffuse split at marginal threshold `3/5`;
- designated partner fleet03/B07 r26, canonical source `yspennstate/math-open-problems@86ff1278a9b52d8a2736c340b7f54893c6b8c267`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T060629Z-fleet03-B07-qform-r26/REPORT.md`;
- required Claude/e5 D' theorem, `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

## New calculation 1: the actual bounded-dimensional N3 core is completely paid

Work in the live sufficient no-pivot class `N3(tau)` with `tau=1/128`. Then every matrix entry satisfies

`|A_uv| <= epsilon_tau := sqrt(tau+tau^2)`

(the diagonal bound is smaller). In the fleet01/B07 coarse-role core alternative, row and column heavy supports each have size at most four, their union `H` has size at most eight, and the retained physical third-compound mass is at least

`Z3(A[R0,C0]) >= P_h/2 >= 2/3125`.

Apply `QFORM-DETERMINANT-MARGINAL-TAIL-CORE-v1` with `p,q<=4`, `r<=4`, `d=|H|<=8`, and `L^2<=pq(tau+tau^2)<=16(tau+tau^2)`. Its finite-coordinate spectral receiver gives

`||p_Q||_infinity
 <= 2 sqrt(6 pi d) sqrt(C(r,3)) p q (tau+tau^2) / sqrt(2/3125)
 <= 3200 sqrt(30 pi) (tau+tau^2)`.

At `tau=1/128`,

`boxed: ||p_Q||_infinity < 244.600.`

Thus the bounded physical-core half of the *bare-spectral* coarse determinant dichotomy is now fully paid in N3. No operator-norm hypothesis is missing: N3 itself supplies the required fixed entry cap. This is the actual bounded-dimensional spectral subproblem requested by the B07 card.

## New calculation 2: refine the latest partner r26 BICORE branch

For partner r26 BICORE, its actual residual physical cross block `N` has `G=||N||_F`, `||N||_op^2<G^2/3`, and therefore (r26 (3.25))

`Z:=E3(N) > G^6/27`.

Let `alpha,beta` be the natural third-volume inclusion marginals.

1. If either orientation has all marginals at most `2/3`, the required e5 D' theorem applies directly and gives

`||p_Q||_infinity <= (9 sqrt(3)e/2) Z^(-1/6) < 27e/(2G)`.

This is an equation-level use of the required e5 result with arbitrary same-bank curvature/outside couplings retained.

2. Otherwise define heavy supports

`R0={i: alpha_i>3/5}`, `C0={j: beta_j>3/5}`.

Each has at most four physical coordinates. If the determinant-marginal tails satisfy `delta_R+delta_C<=1/2`, then the own tail-core theorem yields

`E3(N[R0,C0]) >= Z/2 > G^6/54`.

Using the N3 entry cap and the same `p,q<=4,d<=8` receiver,

`boxed:
 ||p_Q||_infinity
 < 2304 sqrt(2 pi) (tau+tau^2) G^(-3).`

In the inherited r22 collar of r26, `G>theta F/(36sqrt(2))` and `F>kappa/Lambda`, so this becomes a universal constant depending only on the fixed proof parameters.

3. If instead `delta_R+delta_C>1/2`, then for a random volume minor the number `Y` of coordinates outside the two heavy supports satisfies `E Y>1/2` and `Y<=6`, hence `P(Y>=1)>1/12`. Therefore the still-unpaid BICORE state contains a genuine support-diffuse determinant packet of mass

`boxed: P_light > Z/12 > G^6/324,`

while every light coordinate has marginal at most `3/5`; simultaneously D' has failed in both orientations, so each orientation has an actual `>2/3` volume anchor.

Thus the latest partner BICORE is no longer one heavy-core debt: it is either e5-D'-paid, bounded-core-paid, or a quantitatively support-diffuse bi-anchor third-volume packet.

## First unpaid implication

`QFORM-BICORE-SUPPORT-DIFFUSE-VOLUME-RECEIVER-v1`: starting from actual row/column volume anchors of marginal `>2/3` plus a light-coordinate third-minor packet `>G^6/324` with all light marginals `<=3/5`, consume the aggregate packet while retaining arbitrary same-bank quadratic curvature and the outer edge/star resources of fleet03/B07 r26. Do not extract one local minor.
