# D0051 attempt — completed partial investigation, 2026-10-12

Work on the source's limsup definition and all xi>0, with separate, explicitly subcritical deductions. No solution established.

Already verified obstruction: field-independent metric KPZ does not apply to P. At gamma=sqrt(8/3), d_gamma=4, xi=gamma/4 and Q=2/gamma+gamma/2, it would predict dim_E P = xi Q - xi²/2 = 3/4. A nonconstant Euclidean-continuous geodesic joins distinct endpoints and has Euclidean Hausdorff dimension at least 1. The complete connectedness proof is in §A1 and the passed kernel-checked algebra is in SpectrumAlgebra.lean / lean_check.txt.

Remaining gap: evaluate the joint law of small-scale field thickness and geodesic occupation. Neither zero-one laws nor ambient thick-point dimensions identify it. The latest uniformity result leaves the spectrum values as unknown constants and uses a different thick-point convention.

## A. Annulus input and a source-compatible upper bound (proof completed)

Fix gamma in (0,2), xi=gamma/d_gamma, Q=2/gamma+gamma/2>2. Define beta(z)=limsup_{r downarrow 0} h_r(z)/log(1/r), precisely as in the source. Let P:[0,L]->C be a nonconstant finite D_h-length geodesic, parameterized by length, so D_h(P(t),P(u))=|t-u|. All dimensions below use the ambient restricted metrics. Put S_a={z: beta(z)>=a}.

Published input: Gwynne–Pfeffer, arXiv:1905.11790v3, Lemma 2.6, PDF p.15, states that for a bounded open U and zeta>0, with probability tending to one as epsilon->0,

D_h(partial B_r(z),partial B_{r/2}(z)) >= r^(xi Q+zeta) exp(xi h_r(z))

for every z in U and every 0<r<=epsilon. These events increase as epsilon decreases. Thus almost surely some positive epsilon works. Intersect over a countable exhaustion U and rational zeta>0. This gives one probability-one event of uniform sufficiently-small-scale bounds, independently of the choice of P and a. This uses a proved theorem as an input; it is not a new proof of the LQG annulus estimate.

**Theorem A.** On that event, for every such geodesic and every a<Q,

    dim_E(P intersect S_a) <= xi(Q-a).

In particular, for all alpha in [-2,2],

    dim_E(P intersect T_h^alpha) <= xi(Q-alpha).

Proof. Fix a<Q and a number s>xi(Q-a). Choose eta>0 and rational zeta>0 so small that p=xi(Q-a+eta)+zeta satisfies 0<p<s. The image P is compact in the Euclidean topology (the subcritical metric induces the Euclidean topology), so choose a bounded U containing it. If z=P(t) belongs to S_a, infinitely small r satisfy h_r(z)>=(a-eta)log(1/r). At any such r in the uniform annulus range, the annulus crossing distance is at least r^p.

For every u with |u-t|<r^p, P(u) belongs to B_r(z). Otherwise the geodesic subpath from z to P(u) crosses the annulus from radius r/2 to radius r; its length is at least that annulus distance, contradicting |u-t|<r^p. This explicitly uses the subpath geodesic property and Euclidean continuity.

Discard t=0,L, which add at most two points and dimension zero. Fix delta>0 and consider, at all interior t with P(t) in S_a, all such good r<delta for which I(t,r)=(t-r^p/10,t+r^p/10) lies inside (0,L). The radii can be made arbitrarily small at every such t, since p>0. The interval 5-covering lemma gives a countable disjoint subfamily I_j=I(t_j,r_j) whose fivefold concentric enlargements cover all these t. Each P(5I_j intersect [0,L]) is contained in B_{r_j}(P(t_j)), because |u-t_j|<r_j^p/2. Consequently the Euclidean balls B_{r_j}(P(t_j)) cover the target set, apart from the endpoints.

The disjoint intervals have sum length at most L, and length(I_j)=r_j^p/5. Therefore

    sum_j (2r_j)^s <= 2^s delta^(s-p) sum_j r_j^p
                       <= 5*2^s*L*delta^(s-p).

Their Euclidean diameters are at most 2delta. Let delta->0. This proves H_E^s(P intersect S_a)=0. Since every s>xi(Q-a) is allowed, the theorem follows. No independence or actual-limit thickness hypothesis entered the proof.

For completeness, the interval 5-covering lemma used here has the following elementary proof. Split a bounded family of intervals into dyadic length classes. In decreasing order of classes, choose a maximal disjoint subfamily among intervals disjoint from those already selected. At each class an interval not selected intersects a selected interval of length at least half its own. If I intersects J and length(I)<=2 length(J), then every point of I is within (5/2)length(J) of the center of J; hence I is contained in 5J. Positive-length disjoint intervals in a bounded range are countable (each contains a distinct rational); each class permits only finitely many selected intervals, and a greedy maximal selection terminates. Every original interval is therefore contained in a fivefold selected interval, proving the cover. Possible open-endpoint equality does not affect containment, as intersection of open intervals is strict.

**Corollary A1 (Brownian parameter, negative thickness collectively carries dimension).** At gamma=sqrt(8/3), xi=1/sqrt(6), Q=5/sqrt(6). For every a>-1/sqrt(6) with a<Q,

    dim_E(P intersect {beta>=a}) <= 5/6-a/sqrt(6) < 1,
    dim_E(P intersect {beta<a}) = dim_E(P) >= 1.

Proof. The identity Q-1/xi=-1/sqrt(6) follows from the parameters. The upper bound is Theorem A. A continuous path joining distinct Euclidean endpoints has dimension at least one: the map z->|z-P(0)| is 1-Lipschitz, and its image contains [0,|P(L)-P(0)|] by continuity and the intermediate value theorem; this interval has dimension one. The image P is the union of its beta>=a and beta<a parts. Hausdorff dimension of a union of two sets is their maximum, because Hausdorff s-measure is subadditive and dimension is monotone. Since the first part has dimension strictly less than one and P has dimension at least one, the second has exactly dim_E P. In particular the beta<0 points carry the full Euclidean dimension of P.

This is NOT a proof that a particular fixed negative alpha carries full dimension. An uncountable union of zero-dimensional singletons can be an interval. No countable-union stability argument may be used across all alpha. It also does not identify a maximizing thickness or the D_h-length-typical thickness.

## B. Bounds in both metrics and boundary cases

Convention: dim_H(empty)=0. The following are deductions from cited LQG/GFF theorems, not claimed as new ambient dimension results. All assertions in this section are for fixed subcritical gamma; no extension to critical/supercritical xi is claimed.

**B1: intrinsic dimension.** For every s,t in [0,L], D_h(P(s),P(t))=|s-t|, hence P is an isometry of an interval onto its image. An interval of positive length has Hausdorff dimension one. Upper bound: cover it by O(L/delta) intervals of length delta to obtain vanishing Hausdorff s-content for s>1. Lower bound: Lebesgue length is at most the sum of diameters in any interval cover, so H^1 is positive; for s<1 and diameters <=delta, sum diam^s >=delta^(s-1)L, which diverges as delta->0. Thus dim_D P=1 and dim_D(P intersect T_h^alpha)<=1. If P is constant, every intersection has dimension zero in both metrics.

**B2: ambient thickness bound, compatible with the source.** HMP Theorem 1.2 and its following paragraph (PDF p.3) give for circle averages both the actual-limit result and the limsup-at-least variant. In their field normalization the parameter is a_HMP=alpha²/2: h=sqrt(2*pi)F, since their Dirichlet inner product is integral grad f grad g rather than (1/(2*pi)) times that integral. By local coupling of a whole-plane GFF with a zero-boundary GFF plus a harmonic function, these statements hold on compact subsets for the field normalization used here; the harmonic function is bounded on compacts and disappears after dividing by log(1/r). A countable exhaustion extends them to C.

For alpha>0, T_h^alpha is a subset of {limsup h_r/log(1/r)>=alpha}. For alpha<0, every point in T_h^alpha has liminf(-h_r/log(1/r))=-alpha, and therefore limsup(-h_r/log(1/r))>=-alpha. Apply the positive-threshold upper bound to -h. For alpha=0 use the planar upper bound two. By intersecting the probability-one events for positive rational thresholds and both h and -h, then taking rational thresholds up to |alpha|, these upper bounds hold simultaneously for every alpha in [-2,2]:

    dim_E T_h^alpha <= 2-alpha²/2.

In particular both endpoint-thickness sets T_h^2 and T_h^-2 have Euclidean dimension zero. This proves zero dimension, not emptiness.

**B3: transfer of zero dimensions and a quantitative metric upper bound.** Gwynne–Pfeffer Remark 1.9 (PDF p.9), citing Dubédat–Falconet–Gwynne–Pfeffer–Sun Theorem 1.7, gives local Holder continuity of the identity from Euclidean space into D_h for every exponent b<xi(Q-2). Put c=xi(Q-2)>0. For any subset A in a compact set on which D_h(z,w)<=C|z-w|^b, a Euclidean cover of A with diameters delta_j maps to a D_h-cover with diameters <=C delta_j^b. For every t>dim_E A/b, choose bt>dim_E A and covers with sum delta_j^(bt) arbitrarily small. The D_h t-content is bounded by C^t times that sum; thus dim_D A<=dim_E A/b. Localize over countably many compact neighbourhoods and let b increase to c. Consequently

    dim_D A <= dim_E A/[xi(Q-2)].

Combining B1, B2, and A proves, for every alpha in [-2,2],

    dim_E(P intersect T_h^alpha) <= min(2-alpha²/2, xi(Q-alpha)),
    dim_D(P intersect T_h^alpha) <= min(1,
      min(2-alpha²/2,xi(Q-alpha))/[xi(Q-2)]).

One can also insert the published geodesic Euclidean upper bound C_geo=xi*(Q-xi+sqrt(xi²-2Qxi+4)) from Gwynne–Pfeffer Corollary 1.10 (PDF p.9) into the Euclidean minimum. The theorem already supplies its applicability and the relevant parameter branch; no independence is needed. At the Brownian parameter this is (4+sqrt(15))/6=1.31216... . The whole geodesic's Euclidean dimension is in [1,C_geo], with exact value not computed here.

**Proved endpoint special case:** dim_E(P intersect T_h^alpha)=dim_D(P intersect T_h^alpha)=0 for alpha=-2 or alpha=2, for every subcritical geodesic. This conclusion holds even when endpoints of the geodesic happen to be thick points. No endpoint exclusion or nonemptiness assertion is being hidden.

## C. Rejected routes and precise limitations

1. Field-independent KPZ cannot be applied to P. Theorem 1.4 of Gwynne–Pfeffer, PDF p.7, gives dim_E X=xi Q dim_D X-(xi²/2)(dim_D X)² only for sets independent of h. B1 would give dim_D P=1. At gamma=sqrt(8/3), xi Q=5/6 and xi²=1/6, so this substitution gives 3/4, contrary to the connected-path lower bound one proved in A1. The arithmetic is formalized below. This is a counterexample to dropping the independence hypothesis, not a counterexample to D0051.
2. The actual-limit thick-point lower dimension bound in GP Proposition 2.5 does not directly apply to the source's limsup level sets. A supplies its own interval covering argument instead. No two-sided conversion formula is asserted for either convention here.
3. The August 2026 zero-one law does not compute spectrum constants, and its thickness convention also differs from the source. Determinism alone does not show a maximizer exists or is unique.
4. Ambient dimensions and a heuristic probability that a ball is hit by P cannot be multiplied: P depends on h, and a Hausdorff dimension does not by itself determine a one-point hitting exponent. The earlier intake attempt's formula and sign prediction remain unproved.
5. An uncountable collection of alpha-level sets can have a union of larger dimension than any individual level. Full dimension of beta<0 therefore supplies no lower bound for a single fixed-alpha spectrum value.
6. The proof of A is subcritical. Its uniform annulus input, Euclidean continuity, and the Holder input in B have been verified only in that regime here. Q=2 makes the Holder exponent vanish; Q<2 changes the topology and introduces singular points. Those regimes remain untreated beyond the general isometric dimension-one observation for a finite geodesic.

## D. Hostile referee audit

- Almost-sure quantifier: Lemma 2.6's probability-tending-to-one events are increasing as the maximum radius decreases, so eventual validity is probability one. Countable U/zeta choices suffice; P and a can then be arbitrary, including dependent/random ones.
- Limsup: only arbitrarily small good radii are used. No all-scales lower bound on h is claimed.
- Direction of annulus inequality: exp(xi h_r)>=r^(-xi(a-eta)) at good radii; multiplying by r^(xi Q+zeta) yields r^p. For 0<r<1 and p>0, this tends to zero.
- Subpath length: a geodesic starting at the centre must cross both annulus boundaries before leaving B_r. The portion between these crossings has length at least their ambient D_h-distance.
- Enlarged interval containment: I has half-length r^p/10, so 5I has half-length r^p/2, strictly below the annulus crossing cost. Enlarging spatial balls instead would require a new bound and is not done.
- Endpoints: two discarded points cannot alter any dimension and can be covered separately at arbitrarily small cost.
- Covering family: disjoint parameter intervals, rather than disjoint spatial balls, control the total cost. This is essential; a geodesic could revisit a spatial neighbourhood.
- Exponents: choose 0<p<s before taking delta->0; sum cost then vanishes as delta^(s-p). Setting s=p would not give vanishing content and is not used.
- Negative alpha ambient bound: sign reflection gives a liminf for -h; that set is contained in the positive limsup-at-least set, enough for the upper bound.
- Full-dimension negative subset: uses only a union of TWO sets. It never takes a supremum over uncountably many levels.
- Exact-value claims: only the endpoint special cases and intrinsic dimension are computed. No conjectural fixed-level lower bound has been promoted to a proof.

## E. Remaining gap

No matching lower bound for dim_E(P intersect T_h^alpha) or dim_D(P intersect T_h^alpha) is proved for any non-endpoint fixed alpha. The complete spectrum, the existence and uniqueness of maximizing alpha, the exact geodesic Euclidean dimension, and a typical D_h-length thickness remain unresolved. To close the principal gap, one would need a sharp lower occupation estimate / Frostman construction conditioned on the field-dependent geodesic and thickness, with correlation control across scales. The threshold-covering argument is upper-bound only. We have no such lower estimate or counterexample to the proposed uniqueness. Literature search was bounded and partly API-blocked; the record is “no exact solution located”, not a certification of global openness. Novelty of the partial deductions is not claimed.

## F. Finite checks and formalization scope

finite_checks.py uses exact rational arithmetic to test 10,000 interval configurations satisfying the hypotheses of the 5-cover enlargement argument. It also checks 5/6-(1/6)/2=3/4 exactly. numerical_checks.json tabulates the proved upper bounds at eleven Brownian-parameter thickness values; these are evaluations of bounds, not measurements or estimates of the spectrum. The maximum job memory was far below 1 GB and the finite checks finished in seconds.

SpectrumAlgebra.lean formalizes only the Brownian-parameter arithmetic and threshold inequalities. The GFF input, Hausdorff covers, and analytic conclusions are proved on paper in this file, not in Lean. Initial Lean runs failed because of a UTF-8 BOM and then a missing Real import; both were corrected before any formal-check claim. Final Lean run: exit code 0, 174.29 seconds; all four lemmas passed the kernel using only propext, Classical.choice, and Quot.sound. Receipt: lean_check.txt. No sorry, native_decide, or omnibus Mathlib import is present. The runner uses a 3600-second timeout, runs from ~/lean_verify, and keeps the .lean source in D0051. Formal coverage is strictly the four algebra lemmas, not the analytic proof.

## G. Negative-level uniformity reduction from the new paper

Fix gamma in (0,2) and alpha in [-2,0). Bhatia–Kavvadias §2.1 defines a positive b-thick point using liminf h_r/log(1/r)=b and defines a negative alpha-thick point of h by requiring that it be a (-alpha)-thick point of -h. Since liminf(-f)=-limsup(f), their negative-alpha set is exactly the source's T_h^alpha. Thus Theorem 1(2), PDF pp.2–3, implies that on a probability-one event there are deterministic constants Delta_E(alpha), Delta_D(alpha) equal to the two dimensions on every nondegenerate interior segment of every D_h-geodesic.

The constants also give the dimensions of the full nonconstant finite geodesic. Indeed, its interior is the countable union of P([L/n,L-L/n]) for integers n>=3. Each interval is a nondegenerate interior segment, and Hausdorff dimension of a countable union is the supremum of the component dimensions (subadditivity of Hausdorff s-measure proves the upper bound; monotonicity proves the lower bound). Adding at most two endpoints does not alter a nonnegative dimension. This proves the stated reduction, using the published theorem rather than reproving its zero-one law. The event is for each fixed alpha, not an asserted simultaneous event for uncountably many alpha. No values of these constants are evaluated by the paper. Its nonnegative-level convention is different, so this reduction does not apply there.

## Final verdict of the first attempt

PARTIAL. Subcritical upper bounds, Brownian-parameter collective negative-thickness concentration, endpoint dimensions zero in both metrics, and the negative-level determinism reduction are established as specified above. D0051 as posed for all xi and all alpha is not solved. No exact literature solution was located in the bounded search. All unresolved statements are explicit in §E; no uniqueness or fixed-level lower-bound conjecture is claimed as a theorem.

## H. Second serious attempt and revised gap

At the user's request the problem was reopened and two new routes recorded: Gaussian variational occupation transforms and Frostman disintegration / localization in thickness bands. The latter was pursued fully; all proofs, construction details, and hostile checks are in SECOND_ATTEMPT.md.

New proved reduction: each metric separately has a nonempty compact set of thicknesses such that every open thickness band around any one of them carries the full geodesic dimension. These regularized maximizing sets exist even though exact-level maximizing sets need not follow. At gamma=sqrt(8/3), every Euclidean regularized maximizer lies in [-sqrt(2),-1/sqrt(6)]. Both metric regularized maxima avoid +-2.

New explicit obstruction: a compact Cantor union with a continuous injective label has a UNIQUE full-dimensional band maximizer but every exact level has dimension zero. A continuous countable-range variant has exact-level dimensions approaching one with a nonattained supremum. These are counterexamples to deterministic upgrades, not to the actual LQG model.

New sufficient occupation criterion: an atom in the D_h-arclength thickness law gives an exact metric level of dimension one. A common atom for Euclidean finite-energy Frostman thickness laws at exponents approaching dim_E P gives a full Euclidean level. No such occupation atom has been proved. The remaining gap is an LQG-specific atom or dimension-preservation theorem through the collapse of shrinking thickness bands; general disintegration does not supply it. Critical and supercritical cases remain unresolved.

Second-attempt verification: 10,180 Cantor-cylinder gap checks and 99 exact component separation checks passed; three finite/algebraic lemmas passed Lean, receipt band_lean_check.txt. All analytic conclusions remain paper proofs with cited primary inputs. Verdict remains PARTIAL; no exact new non-endpoint LQG spectrum value is established.
