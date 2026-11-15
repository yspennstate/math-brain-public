# Local comparisons for additional road anchors

This checks the comparison-network lemma `found:lem-network` in OpenAI, *Strict convexity and differentiability of the planar exponential first-passage limit shape*, September 24, 2026. The [primary foundations source](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/foundations.tex) was reopened and saved as [fresh-strict-foundations.tex](fresh-strict-foundations.tex). The result is conditional on the dominated calibration and admissible-road hypotheses below. It verifies an input to the common-gauge argument; it does not establish strict convexity.

## Hypotheses and quantitative conclusion

Use physical coordinates in the basis `(A,B)`, so A- and B-roads have horizontal and vertical nominal lines. Assume the manuscript's coordinate conversion bound: a vector of tracking norm at most a has coordinate maximum norm at most 2a. Put `delta=2r`, where `0<r<1/100`. Assume every microscopic edge has coordinate maximum length at most delta, as follows from `n>=K_lat/r` and the stated edge bound `2K_lat/n`. All translations used here are allowed lattice translations.

Each road is an admissible oriented walk with continuous nondecreasing nominal parameter, finitely many edge occurrences on compact parameter intervals, tracking radius r, and dependence radius 10. Its cuts at integer levels are the first occurrences of those levels. Every deterministic marked period has nonnegative defect of expectation at most beta. This assumption is required for every additional road label as well as for the two roads generating the network.

Write P for the integrable centered calibration. For a forward road interval from x to y define

`Q(x,y)=tau(interval)-n h(y-x)`,

`D(x,y)=Q(x,y)-P(y)+P(x)>=0`.

Extend these quantities additively on edge occurrences, using partial edge costs when needed. Defect is nonnegative on partial intervals, by domination on each oriented edge and linear interpolation. A signed use of an interval means multiplying its forward Q-cost and calibration increment by the same sign. It is an estimate of a potential difference.

For an extra marked anchor assigned to index z, let q be its deterministic nominal center. Suppose `|q-z|_infinity<=D`, with `D>=0`. Its road may have any deterministic translated origin and either direction. The anchor itself is within delta of q. Let `d=ceil(D)` and choose

`H=d+30`, `K_D=20d+41`.

For every fixed pair of labels at indices z,z' with `|z-z'|_1<=1`, there is a comparison E such that

`E |E-P(X_z',lambda')+P(X_z,lambda)| <= K_D beta`.

It is measurable on the input cells `Q_H(z)`. The constants do not depend on n, s, beta, the number of labels, or the input road rule. Coordinate conversion is assumed uniform in s as stated in the manuscript. A bound on the physical rather than nominal anchor location is accommodated by increasing D by one.

The labels and translated origins are prescribed before this comparison. The conclusion is pairwise; it does not bound the maximum over arbitrarily many labels selected using their realized costs. No independence between road paths is needed for the error estimate.

## 1. Crossings of local road portions

Place a horizontal road on `y=b` and a vertical road on `x=a`. Inspect their nominal intervals of radius `4delta` about the crossing. At the ends of the horizontal interval, the first coordinate is at most `a-3delta` and at least `a+3delta`, respectively; throughout, the second coordinate belongs to `[b-delta,b+delta]`. These assertions follow from tracking, including during nominal pauses. The vertical portion has the transposed properties.

Consider the square of coordinate half-width `2delta` about `(a,b)`. The horizontal portion contains a subarc in this square joining its west and east sides: take its first hit of the east side and its last hit of the west side before that hit. Between these hits its first coordinate stays between the two sides. Its second coordinate always stays in the smaller horizontal strip. The vertical portion similarly contains a subarc joining the south and north sides. The planar rectangle crossing property forces these arcs to intersect. This property applies to continuous curves with self-intersections: erase loops to obtain a simple crossing arc and use planar separation, or apply separation to the finite embedded graph traced by the curves.

An intersection of the full horizontal and vertical portions has both coordinates within delta of `(a,b)`. On the nearest-neighbor lattice an intersection is a common vertex or belongs to an edge shared by both walks. In the latter case take an endpoint of that edge. Its coordinate distance from `(a,b)` is at most `2delta`, because the edge length is at most delta. On each road the nominal parameter there differs from the crossing level by at most `3delta`: at most `2delta` for the corresponding spatial coordinate and delta for tracking. Thus this common vertex occurrence belongs to both inspected windows. If the curve intersection occurred inside truncated occurrences, the selected vertex is still in the full inspected windows, since `3delta<4delta`.

There are finitely many occurrences in these windows. Choose the first common vertex occurrence on the horizontal road, then the first compatible occurrence on the vertical road. This selection is measurable from the two local records and covariant under their translations. Repeated visits and loops are distinguished by their occurrence labels. The crossing existence argument uses neither monotonicity of a spatial coordinate nor absence of loops.

## 2. The grid and a five-period error bound

Put canonical horizontal roads on `y=j` and canonical vertical roads on `x=i`, for integers i,j. Let `N(i,j)` be the selected intersection from Section 1. It has an occurrence on each road within nominal distance `3delta` of i or j.

Since `6delta<1`, the occurrences of `N(i,j)` and `N(i+1,j)` are strictly ordered along the horizontal road. Their forward interval is contained between nominal levels `i-1` and `i+2`. Define the horizontal grid comparison as its Q-cost. Its discrepancy from `P(N(i+1,j))-P(N(i,j))` is its nonnegative defect.

This defect is bounded pathwise by the sum of five deterministic complete-period defects with indices `i-2,...,i+2`. The larger window avoids any issue with endpoint pauses and the first-cut convention. Its expected discrepancy is at most `5beta`. The vertical construction is identical. A reversed comparison is the negative of the forward comparison and has the same absolute discrepancy bound. A same-index comparison is zero if both labels are the canonical grid anchor.

The bound remains valid when the interval endpoints depend on the environment. Only domination by a fixed sum of nonnegative complete-period defects was used; there was no conditional expectation at a selected endpoint.

## 3. Attaching one extra marked anchor

First take an extra horizontal road with nominal center `q=(q_1,q_2)` at its marked anchor X. Put

`i=floor(q_1+1/2)`, `j=floor(q_2+1/2)`.

Intersect this extra road with the canonical vertical road `x=i`, using Section 1 around `(i,q_2)`; call the selected common vertex Y. Along the extra road, Y is within nominal distance

`|i-q_1|+3delta <= 1/2+3delta < 1`

of X's marked level. Consequently the signed interval from X to Y has absolute calibration discrepancy bounded by four complete-period defects around that marked level. Four periods are a generous bound, covering every endpoint convention; its expectation is at most `4beta`.

Along the vertical canonical road, Y is within nominal distance `3delta` of `q_2`, while `N(i,j)` is within `3delta` of j. Both levels lie strictly between `j-1` and `j+1`, because `1/2+3delta<1`. The signed interval from Y to `N(i,j)` is therefore dominated, in absolute calibration discrepancy, by four complete-period defects with indices `j-2,...,j+1`. Its expectation is at most `4beta`.

The sum of these two signed Q-costs estimates `P(N(i,j))-P(X)` with L1 error at most `8beta`. The calibration value at the shared physical vertex Y cancels exactly. No relation between the nominal origins of the two roads is needed. For an extra vertical road, interchange the coordinates and attach first to `y=j` and then to `N(i,j)`. The same bound holds.

## 4. Two-anchor comparison and label count

Attach X and X' to grid anchors `N(i,j)` and `N(i',j')`. Join these grid anchors by a fixed Manhattan route, first horizontal and then vertical. If both nominal centers are within D of their assigned indices, then

`|(i,j)-z|_infinity <= D+1/2`,

`|(i',j')-z'|_infinity <= D+1/2`.

Thus, for `|z-z'|_1<=1`, the number M of grid edges satisfies

`M <= |q-q'|_1+2 <= 4D+3 <= 4d+5`.

Use the X attachment, the grid route, and the negative of the X' attachment. Their true calibration increments telescope to `P(X')-P(X)`. The triangle inequality yields

`||E-(P(X')-P(X))||_1 <= [8+5M+8] beta`

`<= [16+5(4d+5)] beta = (20d+41) beta`.

Only the two specified extra labels enter. Extra labels elsewhere are never queried, so there is no factor counting them. The same formula covers same-index pairs, neighboring-index pairs, and either combination of road directions. Grid anchors can be treated directly, omitting an attachment and improving the bound.

## 5. Local support and independent cells

All grid indices on the Manhattan route lie in the coordinate box spanned by its endpoints. Relative to z their maximum distance is at most `D+3/2`. Crossing selection uses nominal windows of radius `4delta<1`; the road portions used for costs lie between such windows or between an extra marked center and its nearest crossing. Every nominal location queried for this construction is consequently within coordinate distance `D+5` of z. This bound includes the transverse road records needed to select both endpoint occurrences.

The road dependence radius is 10 in the tracking norm. By the coordinate-conversion bound, every input used is within coordinate distance 20 of one of these nominal locations. Hence all inputs lie within distance `D+25` of z. Assign microscopic weights to a single unit parallelogram by a fixed half-open convention, and assign private variables by their spatial locations, retaining their type and road labels. The cell-index rounding costs at most one in each coordinate. An additional unit covers a choice of edge representative. Therefore `Q_(d+30)(z)` contains every required input cell. These are bounds on the local comparison E; P itself remains nonlocal.

Grouping disjoint primitive product coordinates into these cells gives independent cell variables. Two roads may read the same actual weight; it is stored once, and the roads simply read the same cell coordinate. Private arrays with different roles are distinct primitive coordinates even when their spatial locations agree. For countably many prescribed labels this is an ordinary countable product construction. Pairwise comparisons never require a simultaneous measurable maximum over an uncountable label family.

For a privately completed inserted baseline, keep the tube weights and replace each requested exterior weight by the private weight stored at the same spatial location. This operation preserves the queried input region. Private road seeds have the original spatial dependence as well. Thus the support bound above holds for that extra label with exactly the same H. Its period defect bound and admissibility in the world are hypotheses; the preceding [common-gauge check](round4-common-gauge-proof.md) derives them from the hybrid iid law, translation invariance of the tube, and the random-cut identity. This comparison does not require its private completion to equal the world's exterior.

Under these restrictions, adding the inserted baseline leaves all original canonical road comparisons unchanged and supplies the new endpoint-label comparisons. The number of inserted labels does not alter H or the per-pair constant. Separate phase-conditioned estimates are required if one later conditions on phases; no claim about those estimates follows merely from this network construction.

## 6. Independent rechecks and limits

The constants can be counted independently: at most two attachment intervals at each end, each costing `4beta`, and at most `4d+5` grid intervals, each costing `5beta`. This gives `4*4+5*(4d+5)=20d+41`. For `D=0,1,2,5,20`, the pairs `(H,K_D)` are `(30,41),(31,61),(32,81),(35,141),(50,441)`. All error bounds are for signed comparisons; charging a reverse traversal as a physical path would invalidate this telescoping argument.

The script [check_network.py](check_network.py) checks the rounding and route bounds with exact integer arithmetic; period containment with exact rational arithmetic; finite planar strip crossings by exhaustive path enumeration; signed telescoping with exact rational potentials and nonnegative defects; and the failure of a selected-label maximum to inherit a uniform per-label bound. These checks supplement the argument for arbitrary admissible roads.

The construction verifies the network comparison input under the displayed hypotheses. It does not check the dominated calibration's existence, the downstream local envelope lemma, the phase constructions, the link estimates, or closure of the improved road class. In particular, no conclusion about correctness of the manuscript's full strict-convexity proof is drawn.
