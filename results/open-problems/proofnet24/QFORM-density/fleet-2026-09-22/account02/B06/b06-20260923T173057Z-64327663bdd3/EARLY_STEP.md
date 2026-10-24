SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T17:30:57Z.
attacking: the previous at-most-two-coordinate fused-volume concentration branch; split it into localized square mass versus a dimension-free transverse residual hub without taking any curved-fiber supremum.

# Early substantive calculation

In the rank-one Fresnel/cross setup let `||v||=1`, `M` be the complete physical cross block,

`C=(I-vv^T)M`, `Z=||C||_F^2>0`,

and put probability weight on `(p,q,t)`, `p<q`, proportional to

`(v_p M_qt-v_q M_pt)^2`.

The preceding B06 identity gives the row marginal

`alpha_i = v_i^2 + ||C_i||_2^2/Z`.

Let `H` contain at most two ORIGINAL coordinates and suppose the sampled fused pair touches `H` with probability `tau>3/4`. Then

`sum_{h in H} alpha_h = E |{p,q} intersect H| >= tau >3/4`,

hence

`||v_H||_2^2 + ||C_H||_F^2/Z >3/4`.

Therefore either

`||v_H||_2^2>1/2`,

or

`||C_H||_F^2>Z/4`, so some `h in H` satisfies

`||C_h||_2>sqrt(Z/8)`.

For the live partner r39 cross block `N`, `Z=||(I-vv^T)N||_F^2>=x_2>11907/1048576`; hence the second branch forces the absolute ORIGINAL-row certificate

`||C_h||_2 > sqrt(11907/8388608) = 0.0376752572742...`.

This does not assert `||M_h||` is large: `C_h=M_h-v_h(v^TM)`. The correct next split is

`||M_h|| >= ||C_h||/2`

or

`|v_h| ||v^TM|| >= ||C_h||/2`.

Thus failure of the diffuse fused gate yields either localized square mass on at most two coordinates, a genuine physical cross hub, or a quantitative two-step chain through the common rank-one cross coefficient. The complete cross tail is retained.
