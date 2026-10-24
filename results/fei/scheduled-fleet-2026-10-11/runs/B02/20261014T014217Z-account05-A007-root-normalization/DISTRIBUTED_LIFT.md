# Distributed-core lift of actual base forests

Use the fixed prime-conjunction references and all hypotheses of A007-ACTUAL-DATA-WITNESS-ROOT-LIFT v1, LIFT.md in stage 3. Base g=2B-1 is nonconstant, p=2^-r, F=2A_r B-1, lambda'=beta lambda, pi'=p pi, beta sum lambda<=1, full orders with the fresh core first. Set D=prod(1+lambda pi)-1 and D'=prod(1+p beta lambda pi)-1. All logs are bits, gamma=6/5. This is a continuation of the same C020/PI-J gap, not a new universal cost-payment claim.

For every nonempty covered data T let S(T) sum 2^(-B) over all actual base partition-forest events and eta_T be its normalized posterior. A base event rho recovers its assignment tau, used gates V, permissible roots R, and forest components V_a rooted at a in R. Write c=|R|, Q_tau for base congestion-only cost, and C_tau for base congestion plus rank. The components here are the trees of the ACTUAL base forest, not the SCCs; c is also the number of original source SCCs, but the two partitions need not coincide.

## Construction and inverse

Fix a nonempty selected core U, u=|U|. Allow EVERY map alpha:U->V. Each used gate l now owns its old data T_l and the core alpha^-1(l); no extra gate is introduced. Put u_a=|alpha^-1(V_a)|. On the c base components choose a directed spanning tree rooted at some a in R. An edge from component V_b to component V_d (b!=d) uses any selected core coordinate j owned by a gate l in V_b, and connects that gate l to the old root d. An inactive component u_b=0 has no outgoing edge. Preserve all old data-attached edges and all their local child sequences. At every added core-coordinate group, include every permutation of its distinct child gate labels.

For c=1 there is no component edge and the old root remains the root for EVERY alpha. For c>=2 a root a admits component trees precisely when u_a>0. The resulting gate-level parent graph is acyclic: a cycle involving added edges would project to a cycle of the component tree, while cycles within a component are excluded by the base forest. The root a reaches every used gate. In the enlarged ownership graph, every gate owning a core coordinate has edges to all other used gates. Since a reaches these gates by the constructed tree, it lies in the unique source SCC and is an admissible single root. The queue terminates after exactly one visit to each gate and selected subsets partition U union T.

The inverse reads the actual trace to recover all selected subsets, parents, attachment coordinates and local child sequences. Delete all core-attached edges. The resulting roots and components are exactly the original base forest, and replaying the original deterministic initial-root and coordinate orders recovers rho. Core ownership recovers alpha; the remaining core edges recover the component tree and its coordinate attachments. Thus EVERY pair (base actual event, alpha, added actual component event) has a distinct activated actual event. This includes different assignments, root sets, old chronological traces and local added permutations. Arbitrary chronology is replayed, not presumed unchanged. Core coordinates are identified by the globally fixed fresh block, so this inverse is decoder side information already in the reference, not a sampled-set selector.

## Exact component-tree count

Introduce one variable x_j for each selected core coordinate. Put q_b=sum_(j owned in V_b)x_j and X=sum_j x_j. A component edge b->d has weight q_b. For root a, the incoming Laplacian principal minor on the other c-1 components is

    X I - 1 (q_b)_(b!=a)^t,

so its determinant is q_a X^(c-2), for c>=2. To prove this directly, expand by columns. Taking two rank-one columns makes the determinant zero. Taking none gives X^(c-1), and the single-column terms subtract X^(c-2)sum_(b!=a)q_b. No external tree enumeration theorem is required. The row expansion into parent choices has the same no-cycle/cycle determinant proof as the accepted A006 interface.

Apply the factorial monomial functional M(prod_j x_j^h_j)=prod_j h_j!, counting the ACTUAL repeated-slot sequences. For independent unit exponentials, E X^d=(u)_d=u(u+1)...(u+d-1): expand multinomially; each weak composition contributes d!, and there are binom(u+d-1,d). Permutation symmetry of coordinates gives E[x_j X^(d-1)]=(u)_d/u. Thus the exact number of added actual events rooted at a is

    m_a(alpha,rho)=u_a (u+1)(u+2)...(u+c-2), c>=2,
    m_a(alpha,rho)=1, c=1 (the unique old root a).

In particular sum_a m_a=(u)_(c-1), independent of how core coordinates are distributed. If c>=2 and u_a=0 the count is zero. Both formulas include c=2 and u=1 correctly. The root a itself need NOT own a core coordinate; a gate below it in the old tree may supply the attachment, an improvement unavailable to the previous root-only star construction.

## Exact surrogate mass and signed transport

Let C'_(tau,alpha)(U,T) be the activated congestion-plus-rank cost. It depends only on the data assignment and core ownership, not on forest edges or added component events. The selected distributed surrogate mass is exactly

    S_dist(U,T)=p S(T) G_dist,U(T),
    G_dist,U(T)=E_(rho~eta_T) [beta^|V| sum_(alpha:U->V) sum_(a in R)
                  m_a(alpha,rho) (pi_a/prod_(b in R)pi_b)
                                  2^(C_tau-C'_(tau,alpha)(U,T))].

This is a mass of distinct actual events, not abstract descriptions. It is a lower bound for the full activated partition-forest mass; equality with full mass is not claimed. The selected actual probabilities are different: their size, subset, child-count and multiset laws must be retained, as in A008's complete operator. Factorial credit alone is not exact probability.

Every old root-star event is included (take alpha constant at an old root, and the corresponding component tree star), so S_dist>=S_lift from stage 3. At empty selected core the exact base/activated bijection and G_0 are unchanged. At core-only sets keep the already-paid single-gate mass p beta a0 2^(-C_U), where a0=sum lambda pi (not a root index). The exact normalization identity remains

    log D'-log[p S(T)G_dist,U(T)]
        =log D-log S(T)+log[D'/(pD)]-log G_dist,U(T).

The retained signed term is log[D'/(pD)]<=log beta, proved AFTER writing the identity from positive coefficients of prod(1+t lambda pi)-1. No negative log Z is discarded and no beta scale is chosen after observing U or T.

## Rank-stripped reduction and equal-width collapse

Define J_dist,U by replacing C_tau-C'_(tau,alpha) in G_dist,U with Q_tau-Q'_(tau,alpha), retaining the SAME eta_T. Let L_0=E_eta_T beta^|V|. Put

    Psi_dist=p Var(g) log[D'/(pD)]
      -p sum_(T nonempty) P_g(T)[p log L_0(T)
                          +2^-r sum_(U nonempty) log J_dist,U(T)].

The old private-rank pointwise inequality depends only on the total u, not on which gate owns each core coordinate: the ratio is (r+k)(K+1)/(k(u+K+1))<=r/u. Core rank depends only on U. Thus the complete proof of the stage-3 rank and extra empty-root payment applies unchanged, yielding

    R_F <= p R_g + (7/2)p I(g)+[6/5+log(e)/4] I_core(F)+Psi_dist.

Moreover J_dist,U>=J_U from the old family, so Psi_dist<=Psi pointwise after the SAME spectral averaging and signed normalization. This proves an all-dimensional improvement of the continuation without asserting a universally bounded Psi_dist.

For completeness, the constants can be rechecked directly here. Uniform selected U has u~Bin(r,1/2); E[1/(u+1)]=(2-2^-r)/(r+1) and Jensen give E[1_(u>0)log(r/u)]<=2. Empty U has probability p and shifts each old rank k by r, costing <=gamma log(r+1) per data coordinate. Therefore private rank costs <=p I(g)[2gamma+gamma p log(r+1)]<=3p I(g), since log(r+1)<=r and rp<=1/2. Empty-core root count c<=|T| incurs extra <=rp^2 I(g)<=p I(g)/2; beta labels stay in L_0. For core coordinate j, conditional selected predecessors are Bin(j-1,1/2), so E log[j/(K+1)]<=log[2(1-2^-j)]<=1. Thus E_U C_U<=gamma r/2. Its combined spectral weight across data and core-only sectors is p Var(g)+4pb^2=4pb (b=E B), giving <=gamma I_core(F). Core-only delta'=log[D'/(p beta a0)]<=p beta a0 log e with beta a0<=1/2; its spectral mass 4pb^2(1-p) gives <=(log e/4)I_core(F). These prove every paid constant without assuming a universal payment for the old or new joint functional. The required spectrum identities Fhat(U,T)=p ghat(T) for T nonempty and Fhat(U,empty)=2pb for U nonempty follow by multiplying the fresh AND indicator's coefficients; I_core(F)=2rp b and I(F)=p I(g)+I_core(F).

When all base clauses have common width w, let pi=2^-w. For a fixed tau its c is fixed by the original ownership graph and all permissible roots have that same rarity. The sum over a of m_a*pi/prod_R pi equals (u)_(c-1)*pi^(1-c), independent of old forest components. Hence conditional on tau,

    J_dist,U contribution = beta^|V| (u)_(c-1) pi^(1-c) Z_tau(u),
    Z_tau(u)=sum_(alpha:U->V) 2^(Q_tau-Q'_(tau,alpha))
      =sum_(u_l>=0,sum u_l=u) [u!/prod_l u_l!]
             product_l [((s_l+u_l)/(kappa_l+u))^(gamma(s_l+u_l))
                           /(s_l/kappa_l)^(gamma s_l)].

The last sum is an exact occupation polynomial with algebraic rational-base powers, not a floating-point certificate. It refunds all distinguishable core ownership maps while retaining subset congestion. The conditional base posterior on tau still contains the correct old rank and root/forest masses, computed by A006; it is not replaced by an unweighted ownership law. Unequal rarities keep the component-dependent weighted sum and do not admit this collapse for free.

## Exact first unsupported line

No dimension-independent bound Psi_dist<=K I(F) is established for arbitrary overlapping signed prime tables. Equal-width collapse removes dependence on old chronological forests from the added-root factor and exposes the exact occupation sum Z_tau; it does not pay globally scaled labels or congestion. The next payment must bound this signed whole-set expectation, including the base assignment posterior, or provide an exact actual-Boolean obstruction to this selected mechanism. FEI remains open.
