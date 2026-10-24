# account02/B08 r32 early calculation — singular-hub star half-potential

Programme `QFORM-DENSITY-3EIG-20260922`; full target OPEN.

## First unpaid implication attacked

The preceding B08 state had an actual original hub pivot `|a|>4031 L/8192`, diffuse two-row arm `s_2(M)>=L/8`, and no physical `2x2` principal block with `sigma_min>=L/64`. The remaining rank-one carrier was resonant/aligned with that hub. This run first attacks the exact singular-hub endpoint rather than treating the near-singular block as a small perturbation.

## New calculation

Let two ORIGINAL coordinates `p,q` have physical block

`B=[[a,c],[c,b]]`, `a!=0`, `det B=ab-c^2=0`.

Write the arms into all remaining original coordinates as rows `u,v`, and set

`g=v-(c/a)u`.

After the fixed-source square completion at coordinate `p`, the Schur remainder has **zero** `q^2` coefficient and can be written, uniformly in all conditioned outside values and affine terms, as

`S = 2 X_q ( <g,X_L> + eta ) + W(X_L)`,

where `W` is an arbitrary measurable function of the remaining original product coordinates; in the quadratic-form application it contains the entire remaining quadratic block. No diagonal, rank or moment condition is imposed on `W`.

For fixed `X_L`, put `Y=<g,X_L>+eta`. For every target `s`, the cap-one law of the original coordinate `X_q` gives

`E_q |2 Y X_q + W-s|^(-1/2) <= 2 |Y|^(-1/2)`.

Indeed, after scaling by `2|Y|`, the bathtub extremizer for the kernel `|x-t|^(-1/2)` is an interval of length one and its integral is `2 sqrt(2)`.

The normalized linear projection `(g/||g||).X_L` has density at most `sqrt(2)` by Ball--Rogozin/Livshyts--Paouris--Pivovarov, hence `Y` has density cap

`K<=sqrt(2)/||g||`.

A second one-dimensional bathtub computation yields

`E |Y|^(-1/2) <= 2 sqrt(2K)`.

Therefore

`H_{1/2}(S) <= 2^(11/4) ||g||^(-1/2)`.

Applying the completed square-peel Lemma 4.2 from the required fixed source
`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md`, gives the full-ambient essential-density estimate

`boxed: ||p_Q||_infinity <= 2^(11/4) (|a| ||g||)^(-1/2).`

This is uniform in the entire remaining quadratic block and all induced affine terms. Continuity is not asserted by this route.

In the aligned two-row state, `g=(-c/a,1)M`, so

`||g|| >= s_2(M) sqrt(1+(c/a)^2) >= s_2(M)`.

Consequently the inherited actual gates imply, at `det B=0`,

`||p_Q||_infinity < C_sing/L`,

`C_sing = 2^(11/4) / sqrt((4031/8192)(1/8)) = 27.1247693734...`.

Thus the exact singular physical-hub endpoint is paid. The still-unpaid hub block is punctured: `0<sigma_min(B)<L/64`; it cannot be reached from `det B=0` by deleting the small quadratic coefficient because the input supports are arbitrary and unbounded.

## Partner gate to splice next

The newest compatible designated-partner theorem is account03/B08 r48, `QFORM-RANK2-INDEFINITE-TANGENT-SHEAR-v1`. In an invertible aligned carrier `R`, if `mu<=1/3` and some physical twist `d_j` makes `diag(d_j,R)` indefinite, then

`||p_Q||_infinity <= 8.653498 [|d_j det R| det(MM^T)]^(-1/3)`.

Thus the 619/L benchmark is already paid whenever

`|d_j det R| det(MM^T) >= 2.733e-6 L^3`.

The final report will combine this with the actual `L/64` pair gate and exhibit a target-valid near-singular family showing why the remaining nonzero Schur-hub coefficient cannot be discarded perturbatively.
