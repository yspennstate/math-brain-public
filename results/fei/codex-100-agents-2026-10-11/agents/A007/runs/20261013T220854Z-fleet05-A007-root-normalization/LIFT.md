# Actual partition-forest activation lift

All logarithms are base two except F in forests.tex. Fix a nonconstant Boolean g=2B-1, where B is the union of its nonempty signed prime conjunctions. Gate l has support R_l, rarity pi_l=2^(-|R_l|), one fixed full support order, and positive feasible lambda_l. Put a=sum_l lambda_l pi_l, D=prod_l(1+lambda_l pi_l)-1. Fix r>=1, p=2^-r, fresh positive common conjunction A_r, and F=2A_r B-1. Its prime conjunctions are exactly A_r times the old primes: every implicant of F must force all fresh signs; deleting those literals gives an implicant of B, and minimality is preserved. Choose a fixed beta in (0,1] with beta sum_l lambda_l<=1. Use lambda'_l=beta lambda_l, pi'_l=p pi_l, and order fresh coordinates first, followed by the old order. This reference is fixed before sampling a Fourier set. Put D'=prod_l(1+p beta lambda_l pi_l)-1. All incidence constraints hold.

For nonempty covered data set T, a used-gate assignment tau partitions T into nonempty T_l. Write V for its used gates, c for the number of source SCCs of its ownership graph, R for the roots of an actual base partition forest (one per source SCC). Write C_tau for the NONLABEL, NONROOT part of B: gamma sum_l |T_l| log(|T intersect R_l|/|T_l|)+(gamma/ln 2) sum_j F_tau(j)^j(T). Thus an actual base event has weight

    w=2^(-B)=(prod_V lambda_l)(prod_R pi_l) 2^(-C_tau).

Let S(T) be the sum of these weights over ALL actual base partition-forest events, and eta_T=w/S(T). Finite, positive S is guaranteed by the support cover. Surrogate weight is not the actual queue probability; size, child-count and subset normalizers are paid by K_ref in forests.tex.

## Nonempty selected core: injection retaining all data witnesses

For any nonempty core subset U, u=|U|, and any base event, choose a root a0 in R. Keep the assignment of every data coordinate, every old parent edge and its data attachment, and every child sequence within each old attachment group. Assign all U to a0. Attach each of the c-1 other old roots directly to a0 using a selected core coordinate, with every possible child sequence at repeated coordinates included. The resulting tree is acyclic and reaches every used gate from a0. In the new ownership graph a0 has edges to every other vertex, so it lies in the unique source SCC; a0 is a permissible single root. Every selected subset is nonempty and these subsets partition U union T.

For a core attachment assignment with group sizes h_j, the new event multiplicity is prod_j h_j!. Summing over assignments of c-1 distinct children to u groups gives

    m(u,c)=(c-1)! binom(u+c-2,c-1)=u(u+1)...(u+c-2),

with empty product 1. Indeed each weak composition of c-1 has (c-1)!/prod h_j! assignments, hence total weighted multiplicity (c-1)! per composition. This is NOT u^(c-1): repeated-coordinate child sequences are distinct queue outcomes.

The construction is injective on base event, chosen root, and added core sequences. An activated trace recovers coordinate ownership, so identifies a0. Delete all edges attached to core coordinates, recover the former root set, and retain all old within-data-group child sequences. Replaying with the original fixed initial-root and attachment-coordinate order recovers the unique base trace. This also proves disjointness across assignments. A breadth-first chronological order may change; the recovery uses the underlying local choices and replays them rather than claiming chronology is unchanged.

Let C'_(tau,a0)(U,T) be the activated nonlabel/nonroot cost. It depends on assignment and chosen owner, not on the base forest edges or new sequences. Define

    G_U(T)=E_eta_T [ beta^|V| m(u,c) sum_(a0 in R) (pi_a0/prod_R pi_l) 2^(C_tau-C'_(tau,a0)(U,T)) ].

The mass of this explicitly selected collection of distinct actual activated runs is EXACTLY

    S_lift(U,T)=p S(T) G_U(T).

The optimized full activated mass is at least S_lift; equality with the full mass is NOT asserted for U nonempty. The formula keeps gate labels, subset congestion, physical rank, root rarity and entropy of every added actual event.

## Empty selected core

If U is empty and T nonempty, partition forests are in bijection with base partition forests. The graph and root set do not change; new structural cost is

    C'_0tau=C_tau+gamma sum_(j in T) log(1+r/rank_tau(j)(j)).

All fresh coordinates are predecessors but unselected; this is the exact physical rank shift. Define

    G_0(T)=E_eta_T [p^(c-1) beta^|V| 2^(C_tau-C'_0tau)].

Here the full activated partition-forest mass is exactly p S(T) G_0(T).

## Core-only selected sets

For U nonempty and T empty choose exactly one visited gate, as root, selecting U and zero children. With identical fresh-coordinate orders all gates have the same structural cost

    C_U=gamma sum_(j in U) log(rank_core(j)/(number of selected core predecessors of j+1)).

Summing these distinct gate-name outcomes gives selected mass S_core(U)=p beta a 2^(-C_U). Thus its complete conditioned residual is

    log D'-log S_core(U)=delta'+C_U,
    delta'=log(D'/(p beta a)),  0<=delta'<=p beta a log(e).

The upper bound follows by expanding the product: D'<=exp(p beta a)-1<=p beta a exp(p beta a). This cancels the entire selected root/name rarity for this sector, even with overlapping data clauses. Other core-only multi-gate events may increase the full mass.

## Signed normalization and complete residual transport

Write D(t)=prod_l(1+t lambda_l pi_l)-1=sum_(k>=1) a_k t^k, a_k>=0. Since t=p beta<=1,

    beta a/D <= D'/(pD) <= beta.

The upper inequality is D(t)<=t D(1); it is applied ONLY AFTER retaining the signed normalization in the exact identity

    log D'-log[p S(T)G_U(T)]
      =log D-log S(T)+log[D'/(pD)]-log G_U(T).

Here log D=Lambda+log Z includes the nonempty-root conditioning term. In particular no negative log Z is discarded. The remaining scale-normalization credit may offset labels; it cannot be claimed to pay them all without an expectation estimate.

Let b=E B, v_g=Var(g), P_g(T)=ghat(T)^2. Direct multiplication gives Fhat(U,T)=p ghat(T) for T nonempty and every U, and Fhat(U,empty)=2pb for U nonempty. Hence I(F)=p I(g)+2rp b and Var(F)=4pb(1-pb). Let R_g=sum_(T nonempty) P_g(T)[log D-log S(T)] be the complete optimized base surrogate residual. The explicitly selected activated collection has complete residual

    R_lift=p R_g+p v_g log[D'/(pD)]
       -p sum_(T nonempty) P_g(T) E_(U uniform over all 2^r subsets) log G_U(T)
       +4p^2 b^2 sum_(U nonempty)(delta'+C_U).

The full optimized activated residual is <=R_lift. This is an all-dimensional identity for selected ACTUAL runs and a one-sided bound for the full reference, not an FEI closure claim. h2(Var(F)) and K_ref I(F) remain outside this residual, as in the source theorem.

The empty-core correction alone has a quantitative influence bound. Jensen gives

    -log G_0(T)<=E_eta_T [(c-1)r+|V|log(1/beta)+gamma sum_(j in T)log(1+r/rank_tau(j)(j))].

Since c,|V|<=|T|, its spectral contribution is at most

    p^2 I(g)[log(1/beta)+r+gamma log(r+1)]
      <=p^2 I(g)log(1/beta)+(1+gamma)p I(g)/2.

The second inequality uses log_2(r+1)<=r and r2^-r<=1/2. The beta label debt is explicitly retained.

## Quantitative payment of all activation rank and extra core-empty rarity

The transport can isolate a smaller unpaid functional. Write Q_tau for the congestion-only cost gamma sum_l s_l log(kappa_l/s_l), and Q'_(tau,a0)(U,T) for its activated counterpart. Define, with the SAME base posterior eta_T,

    J_U(T)=E_eta_T[beta^|V| m(u,c) sum_(a0 in R)
                         (pi_a0/prod_R pi_l) 2^(Q_tau-Q'_(tau,a0)(U,T))], U nonempty,
    L_0(T)=E_eta_T beta^|V|.

These retain signed root-removal credit, actual-event multiplicity and ALL congestion and label costs. They do not redefine the posterior or drop the old ranks from its weights. Define the signed joint debt

    Psi=p v_g log[D'/(pD)]
          -p sum_(T nonempty)P_g(T)[p log L_0(T)
                       +2^(-r) sum_(U nonempty) log J_U(T)].

Then the full optimized activated residual satisfies the all-dimensional bound

    R_F <= p R_g + (7/2) p I(g)
                    +[6/5+(log(e))/4] I_core(F) + Psi,
    I_core(F)=2rp b.

This pays activation rank without a log r loss, while explicitly leaving Psi unbounded.

Proof: for a data coordinate with old physical rank k and K selected old predecessors, its rank-cost change is gamma log[(r+k)(K+1)/(k(u+K+1))]. Since K+1<=k and r>=u>=1, this is at most gamma log(r/u). This estimate is independent of owner and forest. Each core coordinate's rank discrepancy depends only on U, not on its chosen gate, and totals C_U. Thus

    G_U(T)>=2^(-gamma |T| log(r/u)-C_U) J_U(T).

For empty U the exact shifted-rank formula and c<=|T| give

    G_0(T)>=2^(-r|T|-gamma |T|log(r+1)) L_0(T).

Here the r|T| term pays p^(c-1); no beta label term is thrown away.

Under uniform U, u is Bin(r,1/2). For u>=1, log(r/u)<=log(2r/(u+1)). The latter is nonnegative also for u=0 (r>=1), so the unconditioned nonempty-sector expectation is bounded by its full expectation. The exact binomial reciprocal identity

    E[1/(u+1)]=(2-2^-r)/(r+1)

and concavity of log give E[1_(u>0)log(r/u)]<=log[2r(2-2^-r)/(r+1)]<=2. Empty-core rank contributes at most gamma p^2 log(r+1) I(g)<=gamma p I(g)/2. Together the private rank cost is at most (5gamma/2)p I(g)=3p I(g). Empty-core extra root rarity contributes at most rp^2 I(g)<=p I(g)/2.

For core rank, condition on a core coordinate j being selected. Its selected predecessors have law Bin(j-1,1/2); E[1/(K+1)]=2(1-2^-j)/j, hence E log(j/(K+1))<=1 by Jensen. Summing gives E_U C_U<=gamma r/2. The nonempty-data sectors have total mass p v_g and the core-only sectors contribute 4p b^2 times this expectation; their combined coefficient is p(v_g+4b^2)=4pb. Thus all new core rank is <=2gamma rp b=gamma I_core(F).

Finally the core-only delta' contribution is 4pb^2(1-p)delta'. Using beta a<=1/2, delta'<=p beta a log(e), b<=1 and p(1-p)<=1/4, its ratio to I_core(F) is at most p(1-p)log(e)/r<=log(e)/4. Add these paid terms to the exact residual identity, leaving Psi untouched. All arguments hold for every r>=1 and arbitrary overlapping signed prime conjunctions.

## First unsupported line

No universal bound on the SIGNED correction

    p v_g log[D'/(pD)]-p sum_(T nonempty)P_g(T) E_U log G_U(T)
       +4p^2 b^2 sum_(U nonempty)(delta'+C_U)

by K I(F), uniformly over arbitrary overlapping prime tables and a suitable globally fixed feasible lambda,beta, is proved here. The quantitative reduction above isolates the narrower first unsupported line Psi<=K I(F). Even assuming a paid base R_g, this signed nonempty-core joint congestion/scale-label debt needs an estimate. A006's determinant factorial-moment interface computes the exact posterior masses entering G and J; it does not supply that estimate automatically. The rank shift and extra empty-core rarity are now paid, rather than left in that gap.
