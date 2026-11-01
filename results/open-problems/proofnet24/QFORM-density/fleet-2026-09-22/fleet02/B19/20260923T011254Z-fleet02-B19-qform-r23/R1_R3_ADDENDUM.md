# fleet02/B19 r23 — current-partner R1/R3 addendum

Status: supporting reductions proved; full QFORM and N3 remain open.

After the first checkpoint, a newer completed designated-partner mathematics source was found: fleet03/B19 r21, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T235209Z-fleet03-B19-QFORM-r21/REPORT.md`. Its no-pivot compiler fixes `tau=2^-20`, constructs a physical cut `B=A[L,R]` with `||B||_F^2>2/3`, and leaves exactly three classes R1--R3 after the diffuse D' branch. The following two deductions apply that result at equation level.

## 1. R1 actually has order-one curvature transverse to the rank-one cross span

Partner R1 gives

`B = sigma u v^T + E`,
`||E||_F < 1/590`,
`sigma>4/5`,

with unit `u,v`; at least one of them is diffuse. Write

`S=diag(A[L,L],A[R,R])`,
`K=[[0,sigma u v^T],[sigma v u^T,0]]`,
`R=[[0,E],[E^T,0]]`.

Let `W=span{(u,0),(0,v)}` and `P=P_W`. Since `K+PSP` is supported on the two-dimensional space `W`, it has rank at most two. Because the original target has `s_3(A)>=1`, Eckart--Young gives

`1 <= ||A-(K+PSP)||_op`
`   <= ||S-PSP||_op + ||R||_op`.

As `||R||_op=||E||_op<=||E||_F<1/590`, one obtains the sharper structural statement

`boxed: ||S-PSP||_op > 589/590.`

Because `S` is block diagonal and `P` splits as the projections onto `u` and `v`, this is exactly

`boxed: max{ ||A[L,L]-(u^T A[L,L]u)uu^T||_op,`
`             ||A[R,R]-(v^T A[R,R]v)vv^T||_op } >589/590.`

Thus the partner's same-side curvature cannot merely be curvature along the already-used rank-one cross channel: an order-one transverse same-side operator survives after that direction is removed.

On whichever side realizes this maximum, write the corresponding self block relative to its cross singular vector `q` as

`C=[[a,b^T],[b,C_perp]]` on `span{q} direct_sum q^perp`.

Then

`C-a q q^T = [[0,b^T],[b,C_perp]]`,

whose operator norm is at most `||b||+||C_perp||`. Hence R1 further satisfies the explicit dichotomy

`boxed: ||P_(q^perp) C q|| >589/1180`

or

`boxed: ||P_(q^perp) C P_(q^perp)||_op >589/1180.`

This is the first-gap refinement needed by grouped-square/two-slope compilers: the missing third curvature is quantitatively transverse, not merely a large same-side norm that could lie in the old two-dimensional span. No matrix coefficient is deleted from the random phase.

## 2. R3 is paid whenever the anchored packet clusters on one nonanchor row pair (or column pair)

Partner R3 supplies a four-coloured packet of physical `3x3` cross minors, every minor containing one fixed row anchor and one fixed column anchor, with total squared-determinant mass

`Z_A > E_3/12 >= 2^-36/12.`

Normalize the retained squared masses to a probability law. Suppose the two nonanchor **row** indices equal one fixed physical pair with probability at least `rho>0`. Let `I_0` be the resulting fixed physical row triple (anchor plus that pair). Cauchy--Binet on the complete three-row cross bank gives

`det(B[I_0,:] B[I_0,:]^T)`
` = sum_(|T|=3) det(B[I_0,T])^2`
` >= rho Z_A.`

Therefore that `3 x |R|` physical cross bank has exact rank three and nonzero-singular-value product

`Pi_3 >= sqrt(rho Z_A).`

The completed fleet03/B19 r16 exact-cross-rank theorem, with one active bank consisting of exactly three original coordinates, gives

`||p_Q||_infinity <= 3 sqrt(e) Pi_3^(-1/3)`
`                   <= 3 sqrt(e) (rho Z_A)^(-1/6).`

The same statement holds for a fixed nonanchor **column** pair after transposition. At the convenient threshold `rho=1/4`, using the partner's explicit packet mass,

`boxed: ||p_Q||_infinity <604.`

Consequently every still-unpaid R3 packet has **every** nonanchor row-pair atom and every nonanchor column-pair atom `<1/4`. This is a real exclusion of the most concentrated clustered-coheavy endpoint without selecting one physical `3x3` minor. The residual R3 geometry is pair-diffuse but may still have a one-vertex-heavy marginal, which is precisely where the mixed-order minor theorem should next be spent.

## 3. Updated first gap

The global proof graph remains full target -> fixed-threshold N3 (Claude geometric synthesis) -> fleet03/B19 r21 compiler. The first listed unpaid state R1 is now sharpened to the two quantitative transverse alternatives above. R2 remains the near-rank-two physical cross tube with fixed `E_2>2^-20` and nonzero tail retained. R3 is narrowed by the pair-atom payment above.

No full-proof claim is made; two independent end-to-end reviews do not exist.
