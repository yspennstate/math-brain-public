# Original-source vacuum calibration commutes with physical spectral marginalization

All logarithms are base two. Cal(P,z) is the normalized law with vacuum mass z and the same conditional nonempty distribution as P. If z=1 it is the point law at the vacuum. If P is the vacuum point law, finite cross entropy of an actual Boolean descendant forces that descendant to be constant and hence z=1. No undefined 0/0 expression is used.

## 1. Exact missing substitution

Let S be a fixed normalized source reference. For any queried coordinate set A let S_A denote its frequency marginal, deleting A. For a nonconstant Boolean current node v with true vacuum probability z_v<1 and finite CE, S_A(empty)<1 and

    Cal(S_A,z_v)=alpha S_A+beta delta_empty,
    alpha=(1-z_v)/(1-S_A(empty))>0,
    beta=z_v-alpha S_A(empty).

Beta need not be nonnegative: this is an algebraic representation of an ACTUAL nonnegative normalized law, not a convex-mixture assertion. Any further spectral marginal M fixes delta_empty. Its nonempty atoms are therefore alpha times those of M S_A. It follows, for an actual child w,

    Cal(M Cal(S_A,z_v),z_w)=Cal(M S_A,z_w).              (C)

If z_w=1 both sides are explicitly delta_empty. If z_v=1 then v and every descendant are constant, so z_w=1. If M S_A is delta_empty, finiteness on occupied actual atoms forces w constant. Otherwise all nonempty denominators are positive and alpha cancels exactly. This proves (C) on the full Boolean-path domain.

The same identity holds across any sequence of physical marginalizations. Thus, after the FIRST reset to Cal(S_A,z_v), every later prescribed return to Cal(S_B,z_w) from the SAME ORIGINAL S is exactly calibration of the CURRENT inherited reference. Each signed CE reset is

    CE(P_w,Cal(S_B,z_w))-CE(P_w,Q_inherited)
       =-D_Ber(z_w || Q_inherited(empty))<=0.            (R)

Every reference-only atom and complete normalizer is included. Source reference S is fixed at the exit ancestor; it is not reoptimized at a descendant. This is the exact substitution into A096's unpaid ORIGINAL-source-return line, provided 'return' includes the specified final vacuum calibration. Returning to raw S_B without that calibration is a different policy and is not asserted free here.

## 2. Independently reconstruct the supplied-likelihood first-frontier theorem

Let g be any Boolean function on a finite uniform cube, m=P_g(empty). Supply a nonnegative subprobability D with D(empty)=m, total mass<=1 and finite c=CE(P_g,D). Supply normalized S,Q with S>=D, Q(empty)>=m and Q(T)>=gamma D(T) at every nonempty T, 0<gamma<=1. Put L=log2(1/gamma). These are supplied hypotheses, not a universal reference construction.

Write D=m delta_empty+N. Root dominance gives Q>=m delta_empty+gamma N. It survives every physical-frequency marginal. At each queried node, the average of the two actual child squared spectra is the marginal of the parent spectrum. Hence the exact CE chain for the SAME comparison measure is

    CE(P_v,D_v)-mean_children CE(P_child,M D_v)
       =B_j(g_v)+E_fiber KL(P_v(.|fiber)||D_v(.|fiber))
       >=B_j(g_v).

Occupied fibers have positive D mass by finite CE; their conditional law is normalized even if D has total mass below one. This telescopes over a finite adaptive physical tree without any independence assumption.

At a selected first-reset leaf ell, CE(P_ell,Cal(S_ell,m_ell))<=CE(P_ell,S_ell)<=CE(P_ell,D_ell). At an old retained leaf the nonvacuum likelihood loss is <=L. At vacuum, writing u=N_ell(empty), weighted AM>=GM gives

    log2[(m+u)/(m+gamma u)]<=u/(m+u)*L<=(1-m)L,

because u<=1-m. For m=0 omit any unoccupied zero vacuum term; m=1 is the constant source. The complete retained-leaf excess is therefore <=L[(1-m)+m Var(g_ell)]. Physical conditional means form a finite martingale, so E_leaf Var(g_leaf)<=1-m. Thus erasure debits plus all complete first-frontier terminal costs are <=c+(1-m^2)L, with the sharper retained-leaf weighted sum from A096 unchanged. This reconstructs A096-SELECTIVE-FRONTIER-LIKELIHOOD-TRANSFER@1 at its exact scope, without importing its checker or assuming any of its integrated negative-cell statements.

## 3. Arbitrarily repeated ORIGINAL-source canonical resets

In ANY finite adaptive physical query tree choose arbitrary nodes, including internal nodes, for the prescribed reset Cal(S_A,P_node(empty)) from the SAME root S. At all other nodes carry the CURRENT complete reference through the actual spectral marginal; root incoming reference is Q. All unreset siblings remain, even when nonconstant.

The first-reset nodes form an antichain. Prune the tree there, keeping every branch with no reset up to its stopping leaf. Section2 bounds this first frontier by c+(1-m^2)L. Below each first-reset node, identity(C) makes EVERY further ORIGINAL-source canonical reset a CURRENT-reference vacuum calibration. Equation(R) makes each reset nonpositive. The ordinary complete-reference CE chain pays each intervening query. Replace each first-frontier leaf by its full continuation and telescope. Therefore the SAME bound

    sum_internal reach B + sum_final reach CE(P_final,Q_final)
       <=c+(1-m^2)log2(1/gamma)                         (T*)

holds for arbitrary repeated original-source canonical resets, with every old sibling and executed erasure retained. No factor depending on reset count, depth, dimension or number of retained siblings is introduced. Each reset is to a normalized actual reference; D remains only a proof comparison.

## 4. Downstream exact scope

Substitute (T*) for the first-frontier theorem in A096's retained negative-cell exit assembly. Its local exit envelope remains c+22e and its creating transaction remains <W+13e. The original-bank assembly is unchanged: at most d_root-1 eligible creating exits, reach*e=e_root, original reserve>=5a_root2^d_root e_root, and 5a2^d-13(d-1)>=7 for a>=1,d>=2. CONDITIONAL on the exact upstream live substitutions and occupied-source floor listed in A096's second claim, arbitrarily repeated ORIGINAL-source canonical resets inside each exit now retain SAME K=2C0+10 (18 structurally) and >=7e_root reserve. This corollary does not independently accept every upstream integration step.

The source S for an exit is the fixed source at that exit's creating live node. The theorem does not allow switching to a different ancestor's S or reoptimizing its conditional nonempty distribution. Arbitrary positive-profile reshaping, a reset to a different nonempty conditional distribution, and an influence-priced universal likelihood supplier remain unpaid. Thus full FEI remains OPEN. The next genuinely new reset must change the nonempty conditional reference, since repeated vacuum-only returns are the identity(C), not a new liability.
