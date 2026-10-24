# Second serious attempt at P0306 (2026-10-11)

Target and previous gap: for each fixed gamma in (0,2), prove dim_{D_h}(T_{2-star} intersect R)<=1 for the ambient Neumann-GFF LQG metric. The previous attempt reduced this to a tilted mixed two-arm/diameter estimate but did not prove that estimate.

## Two approaches not previously pursued

1. **Boundary record sets and geodesic-tree coding.** In Brownian geometry, continuous label functions code distances and geodesic trees. Try to represent boundary two-stars as a countable union of record sets for rooted distance profiles. If two record points on the same component have ambient distance controlled by their label difference, that component is a Lipschitz image of a subset of R and has dimension at most one. This is different from the previous independence/KPZ and full-interval covering approaches: it covers only star points and might exploit exact Brownian-disk coding first. Required ingredients are the countable cover of all stars and an upper distance inequality, not merely the automatic lower bound from a Lipschitz distance profile.

2. **Annular barriers under a logarithmic GFF tilt.** Use the GFF Markov decomposition into scale increments, and prove that each of many boundary half-annuli has a positive-probability geodesic merger barrier even under the tilt. Quantitative iteration could bound the probability of two disjoint arms. One must then compare its exponent to 1-xi Q+xi^2 and include normalized diameter moments. Qualitative confluence only supplies an unspecified positive exponent, so matching the sharp dimension requires additional information.

Approach 1 is selected: it could bypass the unavailable sharp probability exponent and offers an exact stronger special case. Every proposed coding implication will be treated as an unproved hypothesis until verified in a source or derived explicitly.

## 1. Exact real-tree special case

Let T be a separable real tree: every pair of points has a unique arc and that arc is an isometric metric interval. Then the two-star set is exactly the set of points x for which T minus {x} has at least two components, and it has Hausdorff dimension at most 1. If T contains a nontrivial segment, its two-star set has dimension exactly 1.

**Proof.** Two arcs starting at x and intersecting only at x have their endpoints in different components of T minus {x}; otherwise the unique arc between those endpoints would avoid x, contradicting uniqueness of arcs in a tree. Conversely endpoints in two different components give arcs from x intersecting only at x. Components of T minus {x} are open in T minus {x}, and in fact open in T: for y not equal to x, the ball of radius d(x,y) about y cannot cross x, since an arc through x has length at least d(x,y). Let {q_i} be a countable dense set. For each two-star x select q_i and q_j in two distinct nonempty open components. The unique arc [q_i,q_j] contains x. Hence all two-stars lie in the countable union of segments [q_i,q_j]. Each segment is isometric to a bounded real interval and has dimension at most 1; the elementary interval covering proof is already given in ATTEMPT.md Section 5. Countable stability gives the upper bound. Interior points of any nontrivial segment are two-stars and form an isometric open interval, proving the lower bound. QED.

This proves a genuine theorem about a neighbouring metric model, not a positive-gamma LQG special case. Brownian disks and LQG surfaces are not real trees.

## 2. What a tree coding would need to solve P0306

Suppose the boundary two-star set S is contained in union_j F_j(B_j), where B_j is a subset of the two-star skeleton of a separable real tree T_j and F_j:B_j -> (closed H,D_h) is C_j-Lipschitz. Then dim_{D_h}(S)<=1.

**Proof.** The previous theorem gives a countable isometric-segment cover of each B_j. On a segment, a cover by metric sets with t-dimensional total cost tending to zero, t>1, maps to a cover with cost at most C_j^t times that cost. Thus H^t(F_j(B_j))=0; the statement also holds when C_j=0 because the image has at most one point. Taking the countable union over j and a sequence t decreasing to 1 proves the conclusion. QED.

The hypotheses requiring verification are: (i) all boundary two-stars, including exceptional endpoints, are in these images, and (ii) the coding map is Lipschitz from the tree toward the LQG metric. A 1-Lipschitz projection from the surface to a tree is the reverse direction and gives no upper bound.

## 3. A planar geodesic countermodel to the record-set shortcut

Unlike the earlier abstract snowflake example, this is an ambient planar length metric with genuine geodesic two-stars. It is not LQG and does not have its confluence property.

Equip the open upper half-plane with the Riemannian length

    L(P)=integral sqrt(x'(t)^2+y'(t)^2)/sqrt(y(t)) dt,

and let D be the induced length metric. Take its metric completion. The completion is the ordinary closed half-plane, and for boundary points

    D((x,0),(z,0))=2 sqrt(pi |x-z|).                         (7)

**Completion and topology.** For every interior curve, its length is at least 2|sqrt(y_end)-sqrt(y_start)|, by dropping its horizontal derivative and integrating the absolute vertical derivative. Thus points (x,epsilon) converge to a distinct completion point (x,0) as epsilon decreases to zero, with their vertical distance exactly 2|sqrt(epsilon)-sqrt(eta)|. If a curve of length L starts at height y_0 and has maximum height H, then sqrt(H)<=sqrt(y_0)+L/2 and |x_end-x_start|<=L sqrt(H). These follow respectively from the vertical bound to a highest point and from L>=integral |x'|/sqrt(H). Consequently D-small distances imply Euclidean-small differences on bounded height ranges, and a D-Cauchy sequence has bounded coordinates and a Euclidean limit. Near an interior limit the metric is bounded above by a constant times Euclidean distance along short straight segments. Near a boundary point, join two interior points by ascending to height h=max(y_1,y_2,|x_1-x_2|), traversing horizontally, and descending. The length is at most 4sqrt(h)+|x_1-x_2|/sqrt(h)<=5sqrt(h), tending to zero as both points approach that boundary point. This proves that all Cauchy sequences converge to exactly the described completion points and proves equality of the completed metric and Euclidean topologies. The same bounds show that each closed D-ball has bounded Euclidean coordinates; it is Euclidean closed and hence compact. Thus D is proper.

The original space is a length space by construction. Its completion remains a length space: for two completion points first join them to interior approximants by arbitrarily short vertical curves (for boundary points), then use a nearly minimizing interior curve. The metric length of a weighted curve is at most its weighted cost, by applying the definition of D to each subcurve; triangle inequalities give the reverse inequality for the infimum of metric lengths. A proper length space is geodesic: choose paths with lengths decreasing to the distance, parameterize them by length with constant tails on a common bounded time interval, and use compactness of a containing ball and Arzela–Ascoli to obtain a 1-Lipschitz limiting path. Its endpoints have distance equal to the limiting duration; triangle inequalities force equality on every subinterval. This supplies geodesics between all completion points.

**Lower bound in (7).** Put Delta=|x-z|>0, and approximate both boundary endpoints at the same height epsilon. For any interior connecting curve let H>=epsilon be its highest height and p=1/sqrt(H). Cauchy–Schwarz applied pointwise to the vector (p,sqrt(1/y-1/H)) yields

    sqrt(x'^2+y'^2)/sqrt(y)
       >= p x' + sqrt(1/y-1/H)|y'|,

after orienting the horizontal displacement to be positive. Integrate. The total variation of the vertical coordinate, weighted by the nonnegative integrand, contributes at least twice its integral from epsilon to H, since the path starts and ends at epsilon and reaches H. Therefore

    L >= Delta/sqrt(H) + 2 integral_epsilon^H sqrt(1/y-1/H)dy
      >= Delta/sqrt(H)+pi sqrt(H)-4sqrt(epsilon)
      >= 2sqrt(pi Delta)-4sqrt(epsilon).

The integral from 0 to H equals (pi/2)sqrt(H), by y=H sin^2(u), u in [0,pi/2]. The deleted integral from 0 to epsilon is at most 2sqrt(epsilon). The last inequality is the nonnegative square (sqrt(Delta)/H^(1/4)-sqrt(pi)H^(1/4))^2>=0. Taking the infimum over paths and epsilon decreasing to zero proves the lower bound. Piecewise smooth paths suffice in the Riemannian definition; weighted variation and the inequalities hold for each of them.

**Upper bound and explicit geodesics.** Set H=Delta/pi. The cycloid

    x(theta)=x_0+(H/2)(theta-sin(theta)),
    y(theta)=(H/2)(1-cos(theta)),        0<=theta<=2pi

joins (x_0,0) to (x_0+Delta,0). Its Euclidean speed squared is H y(theta), so its weighted speed is the constant sqrt(H) in the open interval. Its length is 2pi sqrt(H)=2sqrt(pi Delta). To justify this as a completion curve without using a boundary integrand, truncate at the two points where y=epsilon and connect horizontally at that height to (x_0,epsilon) and (x_0+Delta,epsilon). The endpoint horizontal offsets are O(epsilon^(3/2)), since theta-sin(theta)=O(theta^3) and y(theta) is of order theta^2. Those horizontal costs are O(epsilon) and the truncated cycloid cost converges to the displayed value. Hence the upper bound holds in the completion. A path attaining the distance is a geodesic after length parametrization: otherwise replacing a subsegment by a shorter path contradicts its global minimality. This proves (7) and the geodesic assertion.

Reflecting the cycloid horizontally gives a second minimizing arc from (x_0,0) to (x_0-Delta,0). One arc has x>x_0 at all positive interior times and the other has x<x_0. They intersect only at their initial point. Every boundary point is therefore a two-star. From (7), boundary covers have diameters equal to 2sqrt(pi) times the square roots of their Euclidean diameters. The same covering-sum argument as ATTEMPT.md Section 5 gives boundary two-star dimension exactly 2.

**Failure of record-set inverse control.** Let the root be (0,0). On the boundary interval [1,2], the distance profile is f(x)=2sqrt(pi x), strictly increasing. Every x is a suffix-minimum record: f(x)=min_{u in [x,2]}f(u). Nevertheless for 1<=x<z<=2,

    D(x,z)/|f(z)-f(x)|=(sqrt(x)+sqrt(z))/sqrt(z-x),

which diverges as z decreases to x. Thus a boundary record set can have dimension 2 in the ambient metric, even when the ambient space is a proper planar geodesic length space and every record point is a genuine two-star. The profile map contracts distances but has no locally Lipschitz inverse. The argument disproves a deterministic record-set shortcut, not P0306.

**Why this is not a target counterexample.** The metric is a deterministic singular Riemannian metric, not a Neumann GFF metric. Its interior is smooth and does not have LQG geodesic confluence: two nearby minimizing geodesics in a sufficiently small interior normal neighborhood cannot merge for a nontrivial interval unless their geodesic initial data agree, by uniqueness of the smooth geodesic ODE. Thus no claim about the LQG exceptional set follows from this example.
