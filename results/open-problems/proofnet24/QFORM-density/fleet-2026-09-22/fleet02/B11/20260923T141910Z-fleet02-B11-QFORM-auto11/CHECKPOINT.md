# B11 early substantive checkpoint — weighted four-ray aggregation and null-ruling defect

Programme: `QFORM-DENSITY-3EIG-20260922`. Run: `20260923T141910Z-fleet02-B11-QFORM-auto11`. Full target remains OPEN.

## First unpaid implication

`QFORM-NULL-RULING-TO-PRODUCT-CUT-v1`: in the exact-rank-three two-plane indefinite survivor, turn quantitative original-row proximity to the two null rulings on each spectral plane into either (i) disjoint source groups carrying two macroscopic rank-three aggregate volumes, or (ii) an already-paid pivot/pair/ridge/diffuse exit. The conversion must preserve original-coordinate independence; small matrix error is not treated as a small random quadratic perturbation.

## A weighted four-ray target family

Fix `0<rho<1`. Put

`s_+=(1,sqrt(rho),0)`, `s_-=(1,-sqrt(rho),0)`,
`t_+=(0,sqrt(1-rho),1)`, `t_-=(0,sqrt(1-rho),-1)`.

Allow arbitrary finite collections of original rows `r_i=a_i s_+`, `a_i s_-`, `b_j t_+`, `b_j t_-`, with squared-amplitude masses exactly `1/2` on each of the four rays. Then `R^T R=I_3` exactly. For

`M_*=[[1,0,0],[0,0,1],[0,1,0]]`

we have `spec(M_*)={1,1,-1}` and `A=R M_* R^T` is a genuine target-scope `(+, +, -)` form; `-A` gives `(+, -, -)`.

I obtain the following dichotomy.

* If `rho>=1/2` and one S-ray row has squared amplitude `>1/4`, then its physical diagonal is the squared amplitude and its leverage is `(1+rho)` times that amplitude. The completed scalar-pivot half-Riesz theorem gives

`||p_Q||_infinity <= 128(32/3)^(1/4) < 232`.

* Otherwise every S-ray squared amplitude is `<=1/4`. Each S ray, whose total squared mass is `1/2`, can be partitioned into two disjoint groups each carrying squared mass in `[1/8,3/8]`. Keep `T_+` and `T_-` as two further groups. Normalized sums over the six disjoint original-coordinate groups are independent and have scalar density cap `<=sqrt(2)`; scaling each by `sqrt(2)` makes cap `<=1`. The resulting six-row aggregate frame is still Parseval, with effective spectral matrix `M_*/2`. The two disjoint aggregate triples `(S_+^1,S_-^1,T_+)` and `(S_+^2,S_-^2,T_-)` each have squared spectral volume at least `1/64`. Applying the completed disjoint-volume compiler used by fleet03/B11 r32 gives

`||p_Q||_infinity <= 6[(1/64)^2]^(-1/6)=24`.

The case `rho<=1/2` is symmetric: either a T-ray row is heavy and the scalar-pivot theorem gives `<179`, or split the two T rays and keep S rays whole; the two aggregate triples have squared volume `>=1/64`, again giving `<=24`.

Hence the entire arbitrary-weight four-ray family has

`||p_Q||_infinity <232`,

uniformly in the number and distribution of rows. This extends the equal-weight four-ray stress family of fleet03/B11 r32 and explicitly demonstrates aggregate-before-inversion under vanishing local pivots.

## General null-ruling defect identity

In the partner r31 two-plane chamber, write T-plane rows as `z_j=(u_j,v_j)`, with `m_22=0`. Then

`A_jj=v_j(2m_23 u_j+m_33 v_j)`.

Let `kappa_T=sqrt(4m_23^2+m_33^2)>0`, and let the two null lines be

`L_0={v=0}`, `L_1={2m_23u+m_33v=0}`.

For every original row,

`dist(z_j,L_0 union L_1)^2 <= |A_jj|/kappa_T`.

Therefore, with `D_T=sum_j |A_jj|`, choosing the nearest null-line projection `z_j^*` gives

`sum_j ||z_j-z_j^*||^2 <= D_T/kappa_T`.

This is a genuine aggregate replacement for the false implication “small local pivot certificates force rowwise splitting”: a small L1 physical-diagonal defect, normalized by the null-line slope scale, really does force L2 proximity to the union of the exact rulings. The reflected S-plane statement is identical with `A_ii=x_i(m_11x_i+2m_12y_i)` and `kappa_S=sqrt(m_11^2+4m_12^2)`.

The remaining gap is to convert this quantitative ruling proximity into a product-preserving aggregate cut or a paid alternate exit without assuming projected independence.
