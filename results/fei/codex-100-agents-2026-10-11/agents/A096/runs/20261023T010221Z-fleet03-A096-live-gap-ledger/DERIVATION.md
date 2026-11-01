# Selective terminal reset after an arbitrary finite physical tree

All logarithms are base two. Erasure B_j(f) means spectral conditional entropy: if p(T)=fhat(T)^2, it is sum_T phi(p(T),p(T+j)), with T not containing j and phi(x,y)=(x+y)log2(x+y)-x log2 x-y log2 y. It is not the difference between parent entropy and the average restricted entropies. Cross entropy CE(p,q)=-sum p log2 q includes all normalizers. A subprobability below is a comparison device, never a supplied terminal law.

## 1. General supplied-likelihood theorem

Let g be any Boolean function on a finite uniform cube. Put m=ghat(empty)^2. Supply a nonnegative subprobability D with D(empty)=m, total mass at most one, and finite c=CE(P_g,D). Supply normalized laws S and Q on the same frequency cube such that S>=D coordinatewise and

    Q(empty)>=m, Q(T)>=gamma D(T) for every nonempty T,

where 0<gamma<=1 and L=-log2 gamma. D need only put mass on the occupied source spectrum: there is NO dominance requirement on reference-only labels in S. Let a finite adaptive tree query fresh physical coordinates on each path, with arbitrary stopping. At each leaf ell, marginalize S directly over every queried coordinate to S_ell, then calibrate its empty mass ONCE to the actual squared mean of g_ell. A constant leaf uses the explicit empty point law. Choose any subset A of leaves to receive these prescribed fresh references. Every other leaf keeps its FULL inherited reference Q_ell, the direct marginal of Q. Selection may depend on the physical history. Then

    sum_internal reach(v) B_j(g_v)
      + sum_leaves reach(ell) CE(P_gell, final_reference_ell)
      <= c+(1-m^2)L.                                      (T)

The sharper history-specific excess is

    L sum_(ell not in A) reach(ell)
      [ (1-m)+m Var(g_ell) ].                              (T')

In (T), the first resets occur at a stopping frontier. Already executed queries inside retained old branches can be incorporated in this tree. After a first reset, arbitrary further physical queries and calibrations of the CURRENT inherited reference are paid as well: each calibration decreases CE and the ordinary complete-reference chain pays each query. This closes repeated internal current-reference calibrations, with no new budget. What is not inferred is repeatedly resetting BACK to the original S marginal after intervening calibrations; that is a different operation, and (T) does not silently reinitialize its comparison measure.

## 2. Complete proof

Write D=m delta_empty+N. Its nonempty remainder has total mass at most 1-m. At any physical leaf, let M_ell denote deletion of all queried frequency coordinates. Marginalization of the root point mass is still the point mass. Thus

    D_ell=m delta_empty+N_ell,
    Q_ell>=m delta_empty+gamma N_ell,
    S_ell>=D_ell.                                         (1)

Finite CE of D at the root implies finite CE of D_ell on every occupied child atom. Indeed a nonzero child Fourier coefficient requires at least one nonzero ancestor coefficient in its frequency fiber. This argument applies independently to every adaptive branch.

For a queried coordinate, averaging the two actual squared child spectra equals the frequency marginal of the parent squared spectrum. Consequently the exact complete-reference chain identity holds for the subprobability D as well:

    CE(P_v,D_v)-mean_children CE(P_child,M_j D_v)
      = B_j(g_v)+sum_fibers p_fiber KL(p(.|fiber)||D(.|fiber))
      >= B_j(g_v).                                       (2)

Each occupied fiber has positive D mass, so its conditional law is normalized even though the total D mass can be below one. Telescoping (2), with physical reach weights, gives

    sum reach B + sum_leaf reach CE(P_leaf,D_leaf)<=c.     (3)

Fresh terminal: calibration of a normalized law changes its CE by minus the binary KL between the actual vacuum occupancy and its old vacuum probability. Hence

    CE(P_leaf,cal(S_leaf))<=CE(P_leaf,S_leaf)
                            <=CE(P_leaf,D_leaf).         (4)

All endpoint cases are well defined: finite source CE guarantees positivity on occupied atoms; at a constant child the explicit point reference costs zero, whereas CE against a subprobability is nonnegative. If the raw marginal is already the empty point law, finite CE forces a constant child. If its vacuum probability is zero and the true vacuum is zero, calibration preserves it. No 0/0 normalization is used.

Retained terminal: for T!=empty, (1) bounds log2(D_leaf(T)/Q_leaf(T)) by L. At empty, writing u=N_leaf(empty), concavity of log gives

    log2[(m+u)/(m+gamma u)] <= u/(m+u) L <= (1-m)L,       (5)

since 0<=u<=1-m. When m=0 this is the bound L; any zero, unoccupied vacuum term is omitted. When m=1 the remainder is zero and the claim follows directly. Thus for v_leaf=Var(g_leaf)=1-P_leaf(empty),

    CE(P_leaf,Q_leaf)-CE(P_leaf,D_leaf)
       <= L[v_leaf+(1-v_leaf)(1-m)]
       = L[(1-m)+m v_leaf].                              (6)

Combining (3), (4), and (6) proves (T'). The physical conditional means form a finite martingale; equivalently the law of total variance gives sum_leaf reach Var(g_leaf)<=Var(g)=1-m. The retained subset only reduces this nonnegative sum and its total reach is at most one. Therefore the excess is at most L[(1-m)+m(1-m)]=(1-m^2)L. This proves (T). All complete old terminal costs, conditional occupancy refunds and already executed erasures occur in (2)-(3); none are dropped.

Continuation corollary: at a fresh leaf, replace its terminal by any finite tree of physical queries with any subset of children calibrated from their CURRENT complete inherited references. Equation (2) for a normalized reference pays each query, and (4)'s binary-KL identity makes each such calibration nonpositive. Induction bounds the entire replacement by the original fresh leaf CE. Thus first-reset leaves can become internal nodes with repeated current-reference calibrations, while all other old branches remain in the ledger. The first-reset nodes form an antichain and serve as the frontier in (T). This is a proof, not a new supplied quota or an assumption of independent branches.

## 3. Application to retained negative-cell exits

Use A085 PROOF.md section 2's independently reconstructed occupied-source likelihood floor, with the exact A097/A073 canonical references. At a live node let g=1-2A_a, F=g+2A_(a+b+r), s=2^-a, e=2^(1-a-b-r), m=(1-2s)^2, d=b+r>=2. Supply normalized current source R with R(empty)=m and finite c. The eligible creating query is dummy (b>=1) or control (r>=2). Its retained exit is g with one irrelevant physical coordinate removed. No reset has yet occurred in that exit. Let Q be its entire inherited reference.

Take the original source R embedded with control frequency zero. Remove its reference-only atoms to form D before marginalizing the creating coordinate; D(empty)=m and CE(P_g,D)=c remain true because a creating dummy/control coordinate is irrelevant to g. Let S be the FULL source law marginalized over the creating coordinate, with remaining control frequencies fixed to zero. S>=D, including ghost atoms. No intermediate calibration is performed. A085's coefficient computation gives

    Q(empty)>=m, Q(T)>=gamma D(T),
    gamma=(1-h)/(1+h/2), h=e/s=2^(1-d)<=1/2.

This supplies precisely the hypotheses of section 1; reference-only Q atoms are not required to dominate the source ghosts. All denominators in this floor are positive. The elementary bound L<11h/4 yields

For completeness, the floor's coefficient calculation is as follows. Put t=2^-(a+b). For a true nonempty active source coefficient -2s, the data marginal denominator is Z=4s^2-4se+2et>0 and its reference numerator is at least (1-h)R(T). At a control exit the multiplier is N/Z, N=(2s-e)^2+e^2, and (1+h/2)N-Z=2e(s-t)+e^3/s>=0. At a dummy exit one contributing multiplier is (2s-e)^2/Z; here t<=s/2 and e<=s/2, so Z/(2s-e)^2-1=(2et-e^2)/(2s-e)^2<=es/(2s^2)=h/2. All additional packets are nonnegative. Thus both multipliers are at least 1/(1+h/2). The joint vacuum is exactly (1-2s+e)^2, at least m because 1-2s>=0, and marginalization adds nonnegative packets. This proves the required floor without domination of ghost labels. Finally -log2(1-h)<=2h on [0,1/2] by convexity below its endpoint chord, and log2(1+h/2)<=h/(2 ln2)<3h/4 since ln2>2/3. Thus L<11h/4, as used below:

    (1-m)L<11e,
    (1-m^2)L <=2(1-m)L<22e.                             (7)

Therefore ANY finite adaptive physical tree inside this exit, with ANY subset of its terminal leaves reset to direct-original-source marginal then one final calibration and every other terminal retaining its old complete marginal, costs <c+22e including all its erasures. The tree may query active, dummy, and remaining control coordinates in any adaptive order. This includes a second prescribed reset in a previously retained sibling, with further nonconstant old siblings still present. It strictly extends the one-inside-query policy, although the bound is coarser than A085's c+11e/2 for that special policy. The continuation corollary additionally covers source-calibrated descendants of previously reset leaves when each later calibration uses the CURRENT inherited reference. Repeated returns to the original pre-calibration source marginal are a separate unpaid policy.

## 4. SAME original rate18 bank

The creating nonactive erasure is <12e. Its live on-child canonical envelope is at most c+20e(a+b+r-1). Inserting the complete exit tree bound of section 3 gives

    B_creation + mean(on-envelope, exit-tree-cost)
       <12e + [c+20e(a+b+r-1)+c+22e]/2
       = W+13e, W=c+10e(a+b+r).                         (8)

An untouched exit or a cheaper A085/A099 policy also satisfies this coarser 13e bound. Active live steps retain A096's paid canonical substitutions, including its separately specified final active point boundary. Along the single edited live branch, reach(v)e_v=e_root. At most d_root-1 eligible nonactive queries occur before the required d>=2 condition ends. The exact source-bank comparison used by A097/A073 gives

    K I(F_root)-W_root >=5 I(g_root)
       =5 a_root 2^d_root e_root,
    K=2C0+10,

for supplied raw source cost<=C0 I(g_root), with d_root>=2. Hence the entire augmented tree is charged to the SAME original K bank, with residual at least

    [5 a_root 2^d_root-13(d_root-1)]e_root >=7e_root.     (9)

For a_root>=1,d>=2, the bracket has minimum at a=1,d=2, value7; its increment in d is 5*2^d-13>=7. Each old live debit and each exit terminal is counted once; the auxiliary D is never an actual reference or a renewed source quota. Structural source R=P_g admits C0=4, so the original rate stays18. This statement is conditional only on the EXACT upstream paid live substitutions/source-bank theorem, not on a new influence price at any descendant.

## 5. First unsupported universal line

The abstract transfer theorem (T) is proved for arbitrary Boolean g with supplied likelihood domination and supplied finite source comparison c. Its negative-cell application and same-bank assembly have a complete analytic derivation, pending independent review. The unsupported universal line remains: for every arbitrary Boolean f, construct an influence-priced source/reference and retained-exit floor meeting these hypotheses from one original budget. An arbitrary inherited reference need not satisfy this floor. Also unpaid: repeated internal resets BACK to the original source marginal after intervening calibrations, with further selective old siblings. Repeated calibration of the CURRENT inherited source reference is already paid by the continuation corollary and is not an open gap. Neither finite validation nor (T) supplies the needed source hypotheses for every Boolean function, so full FEI is OPEN.
