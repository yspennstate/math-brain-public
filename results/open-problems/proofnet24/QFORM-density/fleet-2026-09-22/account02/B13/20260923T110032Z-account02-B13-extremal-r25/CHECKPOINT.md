SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-23T11:00:32Z.
attacking: a product-preserving three-leaf Fourier compiler that tolerates arbitrary diagonal leaf curvature, then the resulting leaf-curvature domination obstruction.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`; role: `Extremal product laws`; execution: `WITHOUT_VERIFIED_BRAIN`.

First unpaid implication: `QFORM-TWOHUB-LEAFCURVATURE-DOMINATION-CLOSURE-v1`: after the compiler below, a high-density witness can only keep a transverse physical two-hub bank if the nonzero leaf-curvature graph dominates every third active leaf from each nonadjacent transverse pair. Convert that domination plus the pinned D5 low-fifth-volume constraint and the partner all-principal-triples-near-singular constraint into a universal slab bound, or construct a genuine bounded-finite-union product-indicator counterexample.

## New lemma under proof — `QFORM-THREELEAF-DIAGONAL-TWIST-v1`

Let `U=(U1,U2)` and `V1,V2,V3` be five distinct original coordinates, all independent with densities at most one, and let `Z` denote all remaining coordinates. After conditioning `Z`, suppose the selected three leaves have no mutual cross curvature, so

`Q = F(U,Z) + sum_{j=1}^3 [ d_j V_j^2 + (2 b_j dot U + c_j(Z)) V_j ]`,

with arbitrary measurable `F,c_j`, arbitrary real diagonal twists `d_j`, and physical vectors `b_j in R^2`. If `Delta=|det(b_1,b_2)|>0` and `b_3 != 0`, then the intended bound is

`||p_Q||_inf <= 3*2^(1/6) * (Delta ||b_3||_2)^(-1/3)`.

Proof skeleton already closed algebraically: for the twisted leaf transform

`G_j(s)=E exp(i t d_j V_j^2+i s V_j)`,

Plancherel gives `int |G_j|^2 <= 2 pi`, uniformly in `t,d_j`, because `f_j<=1` and has mass one. Writing the conditional characteristic integral over the two physical hub coordinates and applying Cauchy-Schwarz,

`I(t)^2 <= [int |G_1(2t b_1 dot u+s_1)|^2 |G_2(2t b_2 dot u+s_2)|^2 du]`
`          * [int f_{U1}(u1)^2 f_{U2}(u2)^2 |G_3(2t b_3 dot u+s_3)|^2 du]`.

The first bracket is at most `pi^2/(|t|^2 Delta)` by the physical change of variables `(b_1 dot u,b_2 dot u)`. For the second, `f_{Uk}^2<=f_{Uk}` and the Rogozin-Ball linear-form bound gives the density of `b_3 dot U` at most `sqrt(2)/||b_3||_2`; a one-dimensional change of variables plus Plancherel gives at most `sqrt(2) pi/(|t| ||b_3||_2)`. Hence

`|phi_Q(t)| <= min(1, 2^(1/4) pi^(3/2) (Delta ||b_3||_2)^(-1/2) |t|^(-3/2))`.

Fourier inversion and exact integration of `min(1,K|t|^-3/2)` yield `||p_Q||_inf <= (3/pi)K^(2/3)`, i.e. the displayed constant `3*2^(1/6)=3.3673861449...`.

This uses no support, moments, log-concavity, rotation of random coordinates, or deletion of the diagonal leaf curvature. It is complementary to the preceding rectangular exact-null-bank theorem: nonzero *diagonal* leaf curvature is harmless for any selected triple of mutually uncoupled leaves.

Sources consumed this run: fresh brain main control revision `2026-09-22.15`; designated partner account03/B13 r24 on the physical `3x3` principal compiler; required pinned `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` Fourier package (Rogozin-Ball and D5). Full QFORM and continuity remain open.
