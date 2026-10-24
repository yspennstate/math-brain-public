# account02/B06 early checkpoint — paying internally concentrated 191-star hubs

Programme `QFORM-DENSITY-3EIG-20260922`; full conjecture OPEN. Execution `WITHOUT_VERIFIED_BRAIN`.

Partner account03/B06 r33 (`math-open-problems@6e33b73460eb417643369a043ebfe903f78e1bd2`) reduces an exact-rank-three matrix `B=U Lambda U^T`, `s=s_3(B)`, to a paid diffuse branch, a paid heavy scalar pivot, or a hub `H={i:||u_i||^2>1/64}`, `|H|<=191`, in which every heavy row has `|B_ii|<s/(8sqrt(2))` and complete off-diagonal star norm `>s/(8sqrt(2))`.

New calculation: write for heavy `i`

`rho_i^2=sum_{j in H,j!=i} B_ij^2`, `tau_i^2=sum_{l notin H} B_il^2`.

If `tau_i<s/(16sqrt(2))`, then `rho_i>sqrt(3)s/32`. Since `|H|-1<=190`, some `j in H` has

`|B_ij| >= beta s`,  `beta=sqrt(3)/(16sqrt(380))=0.0055532707...`.

Put `delta=beta/sqrt(2)`. If either `|B_ii|` or `|B_jj|` is at least `delta s`, the completed exact-rank-three scalar-pivot theorem gives `||p||_inf<1446.261/s`. Otherwise the physical pair `P=[[B_ii,B_ij],[B_ij,B_jj]]` is indefinite, with

`|det P| >= (beta^2-delta^2)s^2=(beta^2/2)s^2`,
`sigmamin(P) >= (beta-delta)s`.

The completed pair-log theorem then gives `||p||_inf<1421.490/s`. Hence partner r33 sharpens to: either density `<1447/s`, or every heavy row has a genuinely aggregate heavy-to-light star packet

`||B_{i,L}||_2 >= s/(16sqrt(2))`.

This closes the internally-concentrated-star half of partner r33's first unpaid implication without selecting an edge until the hub has already been reduced to universal cardinality.

Next: record a target stress family showing that the remaining robust-light branch need not contain two transverse heavy rows, then apply the pinned newest-Claude mixed-Fresnel theorem to that exact obstruction.
