# Constructive lead for separated three-site rank-one approaches

Coordinator checkpoint, 15 September 2026. This is an unfinished route for C089; it is not a proved full boundary theorem. ROOT_RANK_ONE_BOUNDARY already covers comparable transverse eigenvalue scales. The target here is to avoid any bound on their ratio.

Write K=q uu*+VMV*, with q in a compact subinterval of (0,1), u fully supported, V an isometry onto u-perp, and a positive active 2x2 M whose largest eigenvalue tends to zero. Put d=det M, d0=det(I-M), f=tr M-2d. The exact count masses are

    f0=(1-q)d0,
    f1=q d0+(1-q)f,
    f2=q f+(1-q)d,
    f3=q d.

For a direction changing only M, write tau=tr A and v=tr(adj(M)A). The two rare count atoms alone give the exact Fisher lower bound

    FI >= [q tau+(1-3q)v]^2/[q f+(1-q)d] + q v^2/d.

For positive A (reverse a negative definite A), v<=||M||op tau. Thus for sufficiently small ||M||op the first numerator controls tau^2 uniformly, with no lower eigenvalue bound. A weighted combination of the two quadratic terms can be optimized at fixed det A using

    (tr(CA))^2+(tr(DA))^2 >= 2 det(C+D) det A

for positive C,D. With C proportional to I/sqrt(tr M) and D proportional to adj(M)/sqrt(det M), this gives growth containing both 1/tr M and sqrt(tr M/d). The second term is especially useful for extreme eigenvalue separation: it dominates logarithmic divergence as the smaller eigenvalue tends to zero. This suggests retaining both rare-count features instead of replacing them by a condition-number-dependent scalar bound.

For n=3 the atom laws can also be retained exactly. Set a_i=|u_i|^2, r_i=1-a_i, and e_(ij)=(det[u,V1]_(ij),det[u,V2]_(ij)). Then

    p0=(1-q)d0,
    p_i=q d0 a_i+(1-q) V_i(M-dI)V_i*,
    p_(ij)=q e_(ij) M e_(ij)*+(a_k-q)d,  {i,j,k}={1,2,3},
    p123=q d.

The active determinant second-derivative coefficients are therefore 1-q; a_i-(1-q); a_k-q; and q, respectively. All scalar endpoint and singleton atoms remain bounded below as M tends to zero with u fully supported. The pair and full logarithms must be combined before estimating them. Prior rank-two-indefinite positivity already controls the sign of the common frozen coefficient for indefinite active directions; definite active directions need the two-feature Fisher compensation above.

What remains: prove a uniform active-plane gap, retain the population and all four mixing directions, and absorb their cross terms in a metric that works at arbitrary eigenvalue ratios and possible zero coordinates of the individual transverse eigenvectors. Neither count Fisher alone nor a comparable-scale estimate proves these remaining obligations.
