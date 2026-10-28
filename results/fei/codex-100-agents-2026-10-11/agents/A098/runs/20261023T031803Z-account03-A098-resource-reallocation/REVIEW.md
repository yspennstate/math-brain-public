# Independent reconstruction: original-source canonical returns

Verdict: HOLDS for A097-ORIGINAL-SOURCE-CANONICAL-RETURN-COMMUTATION@1, statement hash852163b441b806ea7c76fde654e1fd52d4566db61962c3fc8df2fd4da1102659. Its sole dependency A096-SELECTIVE-FRONTIER-LIKELIHOOD-TRANSFER@1, hash8b8a71cb40c53d689cc4939c1b157a41d6c345a377c865d963a587da89bfc7da, is also independently reconstructed below. No repair is supplied. The integrated negative-cell rate18/7e result is NOT part of this independent acceptance.

## Exact theorem and units

Let g be any Boolean function on a finite uniform cube, P its squared Fourier law, and m=P(empty). Let D be nonnegative with total mass at most1, D(empty)=m, and c=CE(P,D)<infinity. Supply normalized S,Q with S>=D, Q(empty)>=m and Q(T)>=gamma D(T) for T nonempty, 0<gamma<=1. Costs are bits and erasure is B_j=H(S_j|S_-j), not the full entropy decrement. Every query is an actual fresh physical coordinate; reaches are physical probabilities. In any finite adaptive query/stopping tree, selected nodes reset to the direct marginal of the SAME ORIGINAL S, followed by final vacuum calibration to their actual squared mean. Other nodes inherit the current complete reference marginal. All complementary children and all prior erasure debits remain.

The whole erasure-plus-complete-terminal-CE ledger is at most c+(1-m^2)log2(1/gamma). No influence-priced source or likelihood floor is constructed by this result.

## 1. Support propagation and endpoints

For one actual physical query, the average of the two child squared Fourier laws equals the spectral marginal of P. A zero parent fiber therefore forces both child atoms to vanish. Induction over the finite tree shows finite CE against every marginalized D and S on occupied atoms. An actual nonconstant descendant has positive true nonempty mass, so its source marginal has nonempty mass as well. A constant parent has only constant descendants. A constant child is assigned the vacuum point law directly. Thus the divisions below are used only when nonzero. At m=0, any unoccupied zero-vacuum logarithm is omitted; at m=1, D=S=Q are the vacuum point law and the entire ledger is zero. gamma=1 simply makes L=log2(1/gamma)=0; gamma=0 is excluded.

## 2. Calibration absorption without a mixture assumption

For a normalized source law R with R(0)<1 and target z<1, calibration is

    Cal(R,z)=a R+b delta_0,
    a=(1-z)/(1-R(0))>0, b=z-aR(0).

Although b can be negative, this is an algebraic identity of a nonnegative normalized law. Every coordinate-deletion marginal M fixes delta_0. For each nonempty output label T,

    [M Cal(R,z)](T)=a [MR](T),
    1-[M Cal(R,z)](0)=a(1-[MR](0)).

Final calibration to w therefore cancels the SAME positive factor a and yields exactly

    Cal(M Cal(R,z),w)=Cal(MR,w).

At w=1 both sides are explicitly delta_0. At z=1 only w=1 is possible on an actual Boolean path. If MR is delta_0, support propagation forces the child constant. These endpoint conventions prove the identity throughout the stated finite-CE Boolean-path domain. They do not allow a fictitious nonconstant child of a constant parent.

After the first original-source reset, induction over arbitrary interleaved marginals and calibrations identifies every later prescribed original-source return with calibration of the CURRENT reference. If a node's actual vacuum mass is w and incoming reference vacuum mass is q0, CE changes by exactly

    -[w log2(w/q0)+(1-w)log2((1-w)/(1-q0))].

This is minus binary KL, hence nonpositive. Endpoint terms are interpreted on occupied support. Ghost/reference-only mass is retained in the conditional nonempty law and in every normalizer. A reset to an uncalibrated raw marginal, a changed source, or a changed nonempty conditional law is outside this identity.

## 3. Reconstruct the first-frontier bound

Write D=m delta_0+N, with N(0)=0 and total N<=1-m. Root hypotheses imply Q>=m delta_0+gamma N coordinatewise. Every path marginal preserves that inequality and S>=D.

For any one query with the SAME comparison measure, conditional disintegration gives

    CE(P_parent,D_parent)-average CE(P_child,MD_parent)
      =B_j+sum_fibers P(fiber) KL(P(.|fiber)||D(.|fiber)) >= B_j.

On each occupied fiber, D(fiber)>0; its normalized conditional law is a probability even though D is globally a subprobability. Finite telescoping with physical reaches pays all queries and every comparison-measure terminal by c. No independence of rows or branches is assumed.

At a selected first-reset leaf, S_leaf>=D_leaf, so CE(P_leaf,S_leaf)<=CE(P_leaf,D_leaf). Final calibration decreases CE by binary KL, including constant endpoints. At a retained leaf, the nonvacuum likelihood ratio D_leaf/Q_leaf is at most1/gamma. At vacuum put u=N_leaf(0), with 0<=u<=1-m. Weighted arithmetic-geometric mean gives

    m+gamma u >= (m+u) gamma^[u/(m+u)],
    log2((m+u)/(m+gamma u)) <= [u/(m+u)] L <= (1-m)L.

The last inequality follows from u<=1-m, not from an unjustified cancellation when m+u=0. That zero case is unoccupied. If v_leaf=Var(g_leaf), its full retained-terminal excess over CE(P_leaf,D_leaf) is at most

    L[v_leaf+(1-v_leaf)(1-m)]=L[(1-m)+m v_leaf].

The stopped tree is finite. The law of total variance gives E Var(g_leaf)<=Var(g)=1-m; the retained subset has reach at most1 and can only reduce this nonnegative sum. Thus total excess<=L[(1-m)+m(1-m)]=(1-m^2)L. This proves the exact A096 first-frontier theorem at its supplied-reference scope. The square on m is intentional: m already means squared mean, so the bound is 1-(E g)^4, not 1-(E g)^2.

## 4. Arbitrary repeated original-source resets

Prune at the first reset on each path, retaining every path without a reset up to its stopping leaf. These first-reset nodes form an antichain, and section3 pays the pruned complete ledger once. Beneath each selected leaf, section2 shows every later original-source return is a nonpositive CURRENT-reference calibration. The same complete-reference disintegration pays every intervening actual query. Replacing each selected terminal with its full finite continuation therefore never increases the first-frontier bound. This proves A097's full supplied-reference theorem, with all old siblings and prior debits. There is no reset-count, depth, dimension or extra source-quota factor.

## 5. Failure controls and independent checks

The independent checker uses integer butterfly Walsh transforms, separately counted physical pivotal edges, exact Fraction laws, and fixed outward rational atanh log intervals. The author used direct character sums and a different rational grid. Here every eight-atom denominator4 law is used; 9801 admissible tuples are certified, including1413 with negative affine beta. All256 labelled three-bit Boolean tables have actual child/marginal and support checks under three supplied source profiles. Full CE ledgers use the declared384 policies on32 Boolean fixtures; this is bounded validation, not exhaustive arbitrary-history coverage. The analytic argument supplies the general quantifiers. Fifteen positive first resets and63 old nonconstant terminal occurrences ensure the global payment is exercised beyond free-reset examples.

An actual parity3 query has two nonconstant parity2 children. With incoming occupied-label probability1/2 and a prescribed return to uniform nonempty law, the return costs log2(3)-1>1/2 bit (9>8). This is an excluded conditional-nonempty profile change. It shows why the retired canonical-return task cannot be replaced by an unpriced arbitrary profile reset. It is not a FEI counterexample.

## 6. Acceptance and exact open line

The full supplied-reference A097 theorem and its exact A096 first-frontier dependency independently HOLD. This review neither accepts the entire integrated negative-cell18/7e dependency chain nor constructs a universal influence-priced source. A003's parallel absorption mechanism is compatible and should be recorded as an alias, not another mathematical queue item requiring the same proof.

The genuinely next transaction changes the conditional NONEMPTY source profile after an actual paid non-point query. It must specify old/new complete laws, charge the actual weighted log-likelihood quotient minus any vacuum refund to a named unused original bank, and keep both terminals and every old debit. A050/A046's correlation-preserving non-point source is a concrete existing fixture. More vacuum-only returns or larger point-source grids cannot pay that missing term.

The exact target reused from the existing minimal-target interface is explicit. At a reset let P(0)=z, incoming Q(0)=q0, and prescribe normalized R with R(0)=z. For z<1 let P+,Q+,R+ be conditional nonempty laws. Expanding the vacuum and nonempty sums gives

    CE(P,R)-CE(P,Q)
      =(1-z) E_(P+) log2(Q+/R+) - D_Ber(z||q0).

The complete old reference, its full normalizer and the actual occupied-law weighting are essential. At z=1 the shape term is absent. The proposed next payment is the physical-reach-weighted sum of this SIGNED expression at one named changed-profile frontier, against a specified unused original allowance after prior bookings. It is not a new free-return lemma.
