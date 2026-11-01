# C0023: finite dependence and the missing quantitative bridge

Target and model are in STATEMENT.md. Current openness is UNKNOWN. The following are campaign deductions, awaiting independent review by w431. They do not prove C0023.

## Saved lemma L1: a high-density finite-range counterexample

Fix integers d>=2 and L>=1. Let (U_z)_{z in Z^d} be independent uniform(0,1) labels. Almost surely every finite set has a unique minimum. Put W_x=x+[-L,L]^d (integer vertices), and a(x)=argmin_{z in W_x} U_z. Declare x good if a(y)=a(x) for every nearest neighbor y of x. Let X_x be its indicator.

The field X is stationary, ergodic, and r-dependent with r=2L+2 in the sup norm: X_x is determined by labels in the union of W_y over y=x and its neighbors, which lies in x+[-L-1,L+1]^d. For two sets at sup-norm distance greater than 2L+2, their determining label sets are disjoint; independence applies to the corresponding sigma-fields, not merely individual pairs. Ergodicity follows because X is a measurable translation-equivariant factor of the ergodic iid label field.

Every nearest-neighbor component of good vertices is finite. If x and y are adjacent good vertices, their anchors coincide. Hence all vertices of any connected good component share an anchor a. Each such vertex x satisfies a in W_x, so the component lies in a+[-L,L]^d and has at most (2L+1)^d vertices.

Its exact good density is

    q(d,L) = (2L-1)^d / [(2L+1)^(d-1) (2L+1+2d)].

Proof of the formula: write I=intersection_{y=x or y~x} W_y and J=union_{y=x or y~x} W_y. All anchors agree iff the unique minimum on J belongs to I. Necessity holds because a shared minimum belongs to every W_y and minimizes the union; sufficiency is immediate. Now |I|=(2L-1)^d. The union is W_x and 2d disjoint outer faces of size (2L+1)^(d-1), giving the denominator. The minimum is uniformly located on J by exchangeability of continuous iid labels.

Consequently q(d,L)->1 as L->infinity while every good component is finite. This refutes the inference that marginal good probabilities tending to one plus finite dependence at each scale suffice for percolation when the dependence range is allowed to grow. This example does not assert FKG or coordinatewise monotonicity of good events and is not a counterexample to Bernoulli bond critical nonpercolation.

## Saved lemma L2: an explicit sufficient criterion at fixed range

Let X be a {0,1}-valued field on Z^d, d>=2, such that sigma-fields on sets at sup-norm distance greater than integer r>=0 are independent. Suppose P(X_x=0)<=delta for every vertex. Put K=(r+1)^2. If delta<=64^(-K), then the good sites have an infinite nearest-neighbor component with positive probability; no stationarity or FKG assumption is needed.

Proof: restrict to the coordinate Z^2 plane. Color it by its two coordinates modulo r+1. Sites of any one color are mutually independent: successive use of the sigma-field range assumption is valid since every remaining site is farther than r from the previously selected set. Any specified set of m bad sites contains at least ceil(m/K) sites of one color, so its all-bad probability is at most delta^(m/K). No product over dependent sites is used.

If the origin is good but its good component in this plane is finite, its exterior vertex boundary contains a simple star-connected circuit of bad sites enclosing the origin. The elementary square-lattice contour fact follows by tracing the outer polygonal boundary of the union of unit squares of the finite component; successive exterior squares touch at sides or corners, and loops can be erased while preserving an enclosing circuit. For a circuit of m vertices, its intersection with the positive horizontal ray supplies a starting vertex (j,0), 1<=j<=m: enclosing the origin forces a crossing of that ray and of the opposite half-plane, and its diameter is at most m in the sup norm. For each of at most m starts there are at most 8^m star-step sequences. Thus the number of such circuits is at most m*8^m.

Set alpha=8*delta^(1/K)<=1/8. A union bound over the enclosing circuits gives

    P(origin belongs to an infinite good component)
      >= 1-delta-sum_{m>=1} m*alpha^m
      = 1-delta-alpha/(1-alpha)^2
      >= 1-1/64-8/49 = 2575/3136 > 0.

The sum includes impossible short circuits and is therefore a conservative bound. Delta=0 is immediate. An infinite component in the plane is also one in the full lattice. The constant 64 is sufficient, not optimal.

## Saved lemma L3: finite-event stability under lowering p

For any event G determined by M distinct independent Bernoulli edge bits, and any p,p' in [0,1],

    |P_p(G)-P_p'(G)| <= 1-(1-|p-p'|)^M <= M|p-p'|.

Proof: use iid uniform labels for the M edges and threshold them at p and p'. The event indicators can differ only if some label lies between the two parameters. The probability of that union is exactly 1-(1-|p-p'|)^M. This applies to nonmonotone local events as well. It does not make the block events independent.

## Saved conditional bridge L4 and the single hardest gap

Suppose a fixed finite block construction in bond percolation has good events G_z, z in a coarse Z^2, each determined by at most M>=1 edge bits. Assume the determining sets for index sets separated by more than r are disjoint. Assume a deterministic compatibility property: any infinite connected collection of good blocks yields an infinite open component in the physical lattice. This property must hold for every edge configuration and for each parameter; global infinite-cluster membership may not be used to define G_z.

If P_{p_c}(G_z^c)<=delta<delta_star=64^(-(r+1)^2) uniformly in z, take

    eta = min(p_c/2, (delta_star-delta)/(2M)) > 0.

At p'=p_c-eta the bad marginals are less than delta_star by L3. The dependence range is unchanged because the same finite determining sets are used. L2 and compatibility give an infinite physical open cluster with positive probability at p'<p_c. Countability then gives a vertex of positive percolation probability; translation invariance of the original Bernoulli law implies theta_d(p')>0, a contradiction.

HARDEST GAP: derive, from a hypothetical theta_d(p_c)>0 and Bernoulli geometry, a finite, deterministically compatible block system whose actual bad marginal delta and actual dependence range r satisfy delta<64^(-(r+1)^2). Qualitative uniqueness or delta_n->0 with uncontrolled r_n does not supply this. L1 proves that the latter inference is false for general finite-dependent block fields. A different valid domination theorem or uniformly small failure conditional on the actual exposure filtration could replace this sufficient criterion, but its hypotheses must be proved.

## Peer improvement, separately attributed and awaiting w431

w430's 2026-10-10 message points to REVIEW_PACKET.md and gives the weaker sufficient hypothesis delta<=64^(-4)/(r+1)^2. Their idea is to partition the coordinate plane into all-good squares of side r+1: the coarse field is 1-dependent and its bad marginal is at most (r+1)^2*delta by a union bound. Apply L2 to the coarse field. This is w430's new result, not an independent new result claimed by w429. Its designated review by w431 remains pending. The local prototype retains the conservative original criterion; no production guarantee rests on the peer result yet.

This changes the promising NEXT proof step: attempt to construct compatible blocks under hypothetical theta(p_c)>0 with delta*(r+1)^2<64^(-4), while proving every finite-dependence and compatibility hypothesis. If that peer criterion is kept, it replaces the exponential-in-range hurdle. The critical block construction remains unproved.

NEXT: w431 checks the original contour lemma and w430's coarsening lemma; attempt a compatible critical block construction with delta*(r+1)^2<64^(-4).
