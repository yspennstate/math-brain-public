# account02/B07 checkpoint — three-anchor L2 receiver and skeleton/pollution split

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

First unpaid implication attacked: consume account03/B07 r25's nested-third-volume **S branch** while retaining arbitrary same-bank curvature. Do not replace the determinant-weighted packet by one minor.

## A. Three-original-anchor full-curvature receiver

Let `H` consist of exactly three ORIGINAL coordinates and let `L` be any disjoint original-coordinate bank. After conditioning on every other original coordinate, write

`Q(x,y)=x^T B x+2 y^T C x+y^T D y+b_H^T x+b_L^T y+c`,

where `x in R^3`, `y in R^L`, and `C=A[L,H]` has full column rank. Put

`d_H=sqrt(det(C^T C))=s_1(C)s_2(C)s_3(C)`.

Then

`||p_Q||_infinity <= 3 sqrt(2) d_H^(-1/3)`.                 (A.1)

All self curvature in `B,D`, all affine terms and all conditioned outside couplings are arbitrary.

Proof sketch. For fixed `t`, put `g_t(x)=prod_(h in H) f_h(x_h) exp(it[x^TBx+b_H^Tx])`. Then `||g_t||_2<=1`, so by Plancherel `||hat g_t||_2<=(2pi)^(3/2)`. Let `Z=C^T X_L`. Livshyts--Paouris--Pivovarov's product-projection theorem gives

`||p_Z||_infinity <= 2^(3/2)/d_H`.

Disintegrating the arbitrary light phase against `Z` produces a complex density `h_t(z)` with `|h_t(z)|<=p_Z(z)`, hence `||h_t||_2<=||p_Z||_infinity^(1/2)`. Therefore

`|phi_Q(t)| <= ||h_t||_2 ||hat g_t(2t .)||_2
             <= 2^(3/4) pi^(3/2) d_H^(-1/2)|t|^(-3/2)`.

Integrating `min(1,K|t|^-3/2)` gives (A.1). This is a sharper three-anchor specialization of the earlier B07 cross-fiber Plancherel mechanism; the new point for the present branch is that arbitrary curvature on `L` is absorbed into the complex disintegration before Cauchy--Schwarz.

## B. Apply account03/B07 r25 to a real dichotomy

Partner source: `yspennstate/math-open-problems@5e2f0ed9c6f5b7621d6344af21b13a05234fdd47`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T053905Z-account03-B07-qform-r25/REPORT.md`.

On its S branch, in physical notation

`B_cross=[[x,u^T],[y,v^T],[c,N]]`,

and

`s:=||c||_2 ||u wedge v||_2 >= sqrt(P)/3`.                    (B.1)

In the inherited high-tail collar `P>Z/6`, `Z>=theta^2 F^6/6`, `F=||B_cross||_F`, so

`s > theta F^3/18`.                                           (B.2)

Let the three anchors be `H={i,k,a}` and condition outside `H union R union C`. Rotate only the first two **columns of the deterministic coupling matrix** for singular-value bookkeeping (no probabilistic rotation is made). The cross-origin skeleton from the partner packet is

`C_0 = [ rows R: 0,0,c ; rows C: u,v,0 ]`

up to that harmless deterministic 2x2 column rotation. It has rank three and

`pdet(C_0)=s`, `||C_0||_F<=F`, hence

`s_3(C_0) >= a_0:=s/F^2 > theta F/18`.                        (B.3)

The ACTUAL three-anchor coupling matrix is

`C_H=A[R union C,H]=C_0+E`,

where `E` consists exactly of the same-side pollution omitted by the original left/right cross cut: the two anchor-to-`R` stars and the `a`-to-`C` star. Put `d_H=sqrt(det(C_H^T C_H))`.

There is a dimension-free alternative:

* **3-anchor payment:** if `d_H >= a_0^3/8`, (A.1) gives

  `||p_Q||_infinity <= 6 sqrt(2)/a_0
                      =6 sqrt(2) F^2/s
                      <108 sqrt(2)/(theta F)`;                (B.4)

  if the inherited `CRF>kappa`, `CR<=Lambda` collar is retained, then `F>kappa/Lambda` and

  `||p_Q||_infinity <108 sqrt(2) Lambda/(theta kappa)`.        (B.5)

* **forced same-side pollution:** if `d_H<a_0^3/8`, then `s_3(C_H)<a_0/2`. Weyl and (B.3) give

  `||E||_op>a_0/2`.                                           (B.6)

  Because `E` has disjoint physical row supports,

  `E=[ P_R  0 ; 0  q_C ]`

  after the same deterministic column bookkeeping, where `P_R` is the two-anchor same-side coupling to `R` and `q_C=A[C,a]`. Consequently an ORIGINAL physical anchor has a same-side star of norm at least

  `max(||A[R,i]||,||A[R,k]||,||A[C,a]||) > a_0/4
                                            > theta F/72`.    (B.7)

Thus the partner's S branch is no longer merely “three independent linear banks plus arbitrary curvature”: either the actual three-anchor coupling volume already pays the full form, or the allegedly arbitrary curvature contains a quantitatively large ORIGINAL-coordinate star. The surviving step must exploit that star together with the retained determinant packet; it may not discard it as nuisance curvature.

## C. Required newest-Claude result applied

The e5 Fourier route proves D' at threshold `h=2/3`. On the same high-tail state, if the global third-volume law is `2/3`-diffuse on either physical side, then

`||p_Q||_infinity <= 9 sqrt(3e) Z^(-1/6)
                  <= 9 sqrt(3e) 6^(1/6) theta^(-1/3) F^(-1)`,

and hence is universal on `F>kappa/Lambda`. Therefore the new split B is only needed after the source-valid determinant-marginal diffuse exit has failed.

## D. First remaining implication

`QFORM-NESTED-S-FORCED-POLLUTION-RECEIVER-v1`: in the branch (B.7), combine the large original same-side star with the partner's `s=||c|| ||u wedge v||` reserve and the inherited high-tail/no-pivot information to reach a completed pair/hub/ridge/physical-core receiver, without rotating the input law or selecting one tiny determinant.
