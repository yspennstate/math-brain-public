# account02/B10 early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T071805Z-b10-qform`.
Status: supporting structural calculation; full QFORM open.

In the completed account03/B10 near-coloop notation, let the heavy physical row be `r_0=sqrt(c)e` and write mixed complement rows as `r_j=s_j e+w_j`, `w_j perpendicular e`. Put

`H=sum_(j in M) w_j w_j^T`, with eigenvalues `eta>=theta>=0`.

The sharpened unpaid collar inherited from account03/B10 r24 is

`1-eta < 2(1-rho_M)|alpha| <= 2|alpha|`,

where `rho_M=sum_M s_j^2` and `alpha=e^T Lambda e`; the one-sheet side for signature `(2,1)` is already paid by the ruled theorem at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`:

`ess sup_(t>=0) p_Q(t) <= pi sqrt(2)`.

First new calculation: colour every mixed original coordinate independently by `Y` or `Z` with probability `1/2`. With

`H_Y=sum_(j in Y) w_jw_j^T`, `H_Z=sum_(k in Z) w_kw_k^T`,

and `M_perp(H_Y,H_Z)=tr(adj(H_Y)H_Z)=sum_(j in Y,k in Z) det(w_j,w_k)^2`, one has exactly

`E M_perp(H_Y,H_Z) = (1/2) det H = (1/2) eta theta`.

Therefore a deterministic ORIGINAL-coordinate partition `M=Y disjoint_union Z` satisfies

`M_perp(H_Y,H_Z) >= eta theta/2`.

Because the hub supplies the longitudinal spectral direction, its incident aggregate Pluecker packet across the two independent banks obeys

`sum_(j in Y,k in Z) det(r_0,r_j,r_k)^2 = c M_perp(H_Y,H_Z) >= c eta theta/2`.

Thus if `theta>=1/16`, then account03/B10's collar has `eta>7/8` and the packet is at least `7c/256`; the remaining debt is no longer existence of product provenance but a receiver for one singleton hub plus two disjoint vector-valued original-product banks, retaining same-bank longitudinal/transverse contamination.

If `theta<1/16`, the coefficient geometry is quantitatively near-collinear: the mixed bank has off-axis transverse energy `<1/16`, while the pure-transverse complement Gram `I_2-H` has the crossed eigenvalues `1-eta<2|alpha|` and `1-theta>15/16`. This is the separate near-collinear interpolation chamber.
