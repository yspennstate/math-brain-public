# Necessary roots in the unchanged conditioned queue

Fix a finite gate table, positive feasible packing, actual root activities x_e=lambda_e*pi_e, and D=prod_e(1+x_e)-1. The original queue has nonempty subsets at every successful visit and children chosen only from gates containing their attachment coordinate. Let Q_*(A) be its full output subprobability conditioned on at least one initial root. This includes arbitrary repeated visits, overlapping selections and all actual output ambiguity; it is not merely a selected forest reference.

For a nonempty target A, join two coordinates of A when some gate contains both. Let C_1,...,C_k be the connected components. A gate meeting A belongs to exactly one component: G_c={e: nonempty A intersect R_e subset C_c}. Gates disjoint from A belong to none. Put D_c=prod_{e in G_c}(1+x_e)-1. If a coordinate has no covering gate then Q_*(A)=0; otherwise

    Q_*(A) <= product_c D_c / D.                       (1)

Proof: in a finite successful run outputting exactly A every selected subset lies in A. Every root must meet A, and any parent-child attachment is in A and in both gates, so the entire descendant tree stays in the root's component. To output every component, the initial root set must hit every G_c and avoid every gate disjoint from A. Distinct G_c are disjoint collections of gate names. Summing the EXACT nonempty-product root weights prod_{e in R}x_e/D over precisely this event gives (1). There is no unproved multiplication of conditional success bounds: only the independent original root activation law is factored. Failed/infinite runs only decrease Q_*.

Suppose also that the total activity S_c=sum_{e in G_c}x_e is at most pi<=1/2 for each component. Finite-product expansion gives prod(1+x_e)<=1/(1-S_c), since each elementary symmetric polynomial is at most S_c^j. Thus D_c<=S_c/(1-pi), while D>=sum_c S_c. Moreover product S_c/sum S_c<=pi^(k-1)/k: for each c, product S_c<=S_c*pi^(k-1), and then sum these k inequalities. Consequently

    Q_*(A) <= pi^(k-1) / [k(1-pi)^k].                (2)

If pi=2^-r, the full bit cost satisfies

    -log2 Q_*(A) >= (k-1)r+log2 k+k log2(1-pi)
                  >= (k-1)r-3k pi.                  (3)

For the last inequality use -ln(1-pi)<=pi/(1-pi)<=2pi and ln2>2/3. The signed normalizer is retained in D throughout. In particular its refund removes ONE leading root-rarity charge; it does not remove the remaining k-1 charges.

The lemma is universal for the stated queue. It provides a necessary condition for influence-paid coding, not an upper payment theorem. It remains valid with any ordered covers, any positive allowed subset weights, any offspring law using selected attachment coordinates, and every original feasible reference.
