# A simultaneous local envelope for road attachments

This checks `found:lem-envelope` in OpenAI, *Strict convexity and differentiability of the planar exponential first-passage limit shape*, September 24, 2026. The [primary foundations source](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/strict/foundations.tex) is saved as [source-foundations.tex](source-foundations.tex). The result is conditional on the dominated calibration, finite collection of prescribed roads, and anchor estimates below. It concerns a single complete environment. Phase conditioning, link estimates, and the full strict-convexity argument are outside this result.

## 1. Hypotheses and bounds

Work on the nearest-neighbor metric graph, with strictly positive edge weights. Allow partial-edge traversals, charged in proportion to their length. Fix a linear functional `nh`. Suppose a calibration `P` is continuous and affine on each edge and, for every oriented physical path from x to y,

`Q(path) := tau(path)-nh(y-x) >= P(y)-P(x)`.

Consequently the defect `D(path)=Q(path)-P(y)+P(x)` is nonnegative and additive. This follows from edgewise domination in the manuscript. Nonnegativity applies separately to both orientations. A signed road interval, in contrast, multiplies its forward cost and defect by its traversal sign; its signed defect may be negative.

Fix finitely many prescribed road records with continuous nondecreasing nominal parameters and finitely many edge occurrences on every compact parameter interval. Their marked cuts at integer levels use the first occurrence convention. Select N complete marked periods covering the prescribed windows and every road adjustment to be used. Every selected period has integrable nonnegative defect `d_i` with `E d_i <= beta`. Its two marked anchors have integrable local gauges. All gauges are constructed in the same environment and use the same calibration.

Let a finite connected comparison graph contain every selected marked anchor and any auxiliary anchors needed to connect them. Its edges are a list of M prescribed anchor comparisons, including one edge for each selected period. Repetitions in this list are permitted and counted. At an anchor a put

`e_a = g_a-P(a)`.

Assume, for each listed oriented edge `(a,b)`,

`E |e_b-e_a| <= kappa beta`.                                      (1)

There is no assumption on the absolute error `e_a`. All anchors and comparison routes are prescribed before observing their errors. Let

`A = sum_(listed edges (a,b)) |e_b-e_a|`,

`D = sum_(selected periods i) d_i`.

Thus

`E A <= M kappa beta`, `E D <= N beta`.                            (2)

Interpolate each period as in the manuscript. There are local nonnegative envelopes with the following properties:

* For at most k switches, where `k>=1`, U bounds any concatenation of at most `k+1` corrected signed road trips and at most k switch gauge differences. It also bounds each individual trip or switch, and

  `E U <= [(2k+1)M kappa+(3k+1)N] beta`.                          (3)

* For every physical path in a prescribed deterministic finite closed metric subgraph, with endpoints in the selected windows, the corrected cost is at least `-U'_0`, simultaneously over paths and endpoint occurrences, with

  `E U'_0 <= (M kappa+2N) beta`.                                 (4)

* With signed road adjustments from prescribed center occurrences to the two endpoints, the cost corrected at the centers is at least `-U'_c`, with

  `E U'_c <= (M kappa+4N) beta`.                                 (5)

  If both centers are marked anchors in the comparison graph, replace `4N` by `2N`.

The envelopes are defined from local costs, not from A or D. Their support is the union of the finitely many road/gauge supports and the prescribed subgraph. The bounds have no dependence on the number of microscopic occurrences or physical competitors.

A road trip here means one interval of one recorded road, used with either sign. Repeated use is counted as another trip. Arbitrarily many repetitions of a trip or switch are not included in (3).

## 2. The interpolation identity

Consider one period from marked occurrence i to its next marked occurrence i+1. For an intermediate occurrence x, write `theta=t(x)-i`, so `0<=theta<=1`. Put

`q_i=Q(i,i+1)`, `C_i=q_i-g_(i+1)+g_i`,

`g(x)=g_i+Q(i,x)-theta C_i`.

All subinterval costs refer to occurrence order, including repeated visits. At the terminal cut this agrees with `g_(i+1)`. At a nominal pause theta remains constant while Q and g vary continuously together. A pause at an integer level belongs to the following period, so no occurrence is lost.

Since `q_i=P(i+1)-P(i)+d_i`, subtraction gives

`C_i=d_i-(e_(i+1)-e_i)`.                                         (6)

Also, if `d(i,x)=Q(i,x)-P(x)+P(i)`, then

`e(x)=e_i+d(i,x)-theta C_i`

`     =(1-theta)e_i+theta e_(i+1)+d(i,x)-theta d_i`.                (7)

Additivity and nonnegative subinterval defects give `0<=d(i,x)<=d_i`. Therefore

`|d(i,x)-theta d_i|<=d_i`.                                        (8)

This is uniform over every occurrence in the period, including points inside edges and pauses. It does not require an occurrence to have been chosen independently of the environment.

Connectedness gives, for any two marked anchors a,b in the comparison graph,

`|e_b-e_a|<=A`:                                                   (9)

choose a simple graph path between them, telescope the errors, and bound its sum by the whole edge list. Thus the range of all marked errors has width at most A. Equation (7) places every interpolated error within `d_i` of that marked-error interval. For any two occurrences x,y in the selected periods, even on different labels,

`|e(x)-e(y)| <= A+d_i+d_j <= A+2D`.                              (10)

The last inequality also covers two occurrences in the same period. It intentionally allows that period to be charged twice.

There is a second derivation of (7): expanding the definition of C directly yields

`g(x)=(1-theta)g_i+theta g_(i+1)+Q(i,x)-theta q_i`.

Substituting `Q(i,x)=P(x)-P(i)+d(i,x)` and the expression for q_i gives (7). This checks both signs without using (6) as an intermediate step.

## 3. Corrected road trips and switches

For ordered occurrences x,y in one period, with nominal fractions theta and phi, additivity cancels the raw costs in the interpolation formula:

`Q(x,y)-g(y)+g(x)=(phi-theta)C_i`.                               (11)

A signed reversal changes the signs on both sides. Splitting a trip along a road at marked cuts gives coefficients of absolute value at most one for each of its traversed periods. Every permitted trip stays in the selected periods. Hence its absolute corrected cost is at most `sum_i |C_i|`. Each selected period's anchor edge is in the comparison list, so (6) gives

`sum_i |C_i| <= D+A`.                                            (12)

At a switch between two labeled occurrences at the same physical point, P has the same value for both labels. Consequently

`|g_a(x)-g_b(x)|=|e_a(x)-e_b(x)|<=A+2D`.                         (13)

Let R be the supremum of absolute corrected signed costs of one allowed road trip. Let S be the supremum of absolute switch gauge differences at allowed physical coincidences; set an empty supremum to zero. These quantities are local and measurable, as shown below. Equations (12)–(13) give

`R<=D+A`, `S<=A+2D`.

Define `U=(k+1)R+kS`. The triangle inequality bounds every concatenation under consideration by U. Since `k>=1`, U also bounds R and S separately. Pathwise,

`U <= (2k+1)A+(3k+1)D`.

Taking expectations and using (2) proves (3).

For a nominal interval of length at most ell contained in a prescribed bounded number of periods, each coefficient in (11) is at most ell. Thus the same argument gives the manuscript's sharper short-window estimate `ell sum_i |C_i|`. A zero-length nominal pause has zero corrected cost along a single period, although its raw physical cost may be positive.

## 4. Physical competitors and the local lower envelope

Let gamma be any oriented physical path from an occurrence x of road a to an occurrence y of road b. Define its endpoint-corrected cost by

`F_0(gamma;x,y)=Q(gamma)-g_b(y)+g_a(x)`.

Domination and (10) imply

`F_0 >= P(y)-P(x)-g_b(y)+g_a(x)`

`    =e_a(x)-e_b(y) >= -(A+2D)`.                                (14)

This is one pathwise bound for all such paths and endpoints. A finite graph is not needed for inequality (14); it is used to define a local measurable optimizer and envelope.

Restrict gamma to the prescribed deterministic finite closed metric subgraph G. Let v_0 be the infimum of F_0 over the allowed paths and occurrences. When there is no competitor, set `U'_0=0`; otherwise set `U'_0=max(0,-v_0)`. Its definition reads only G's edge weights, the local road records, and the local interpolated gauges. Section 6 proves that the infimum is measurable and attained when feasible. By (14),

`0<=U'_0<=A+2D`.

Equation (2) proves (4). The dominator on the right may be nonlocal. Locality follows from the definition on the left and does not require a local approximation of the absolute calibration.

## 5. Signed center adjustments

Let c_a,c_b be prescribed occurrences on the respective roads. Include all periods between these centers and the attachment windows in the selected period list. Let `Q_a(c_a,x)` be the signed cost on the oriented road: use its forward cost if c_a precedes x, and minus the forward cost if x precedes c_a. Define `Q_b(y,c_b)` the same way. These are signed comparisons, not physical reverse path costs.

The cost corrected at the centers is

`F_c=Q_a(c_a,x)+Q(gamma)+Q_b(y,c_b)-g_b(c_b)+g_a(c_a)`.            (15)

Equivalently, add to F_0 the two corrected signed road costs from c_a to x and from y to c_b. Expanding that expression cancels the attachment gauges and gives exactly (15).

Write `d_a(c_a,x)` and `d_b(y,c_b)` for the corresponding signed defects. Calibration increments telescope in (15), yielding the independent identity

`F_c=D(gamma)+d_a(c_a,x)+d_b(y,c_b)+e_a(c_a)-e_b(c_b)`.            (16)

Each signed road defect has absolute value at most D. The same period can occur in both adjustments, so their sum is bounded below by `-2D`. By (10), the center-error difference is at least `-(A+2D)`. Thus

`F_c>=-(A+4D)`.                                                  (17)

If both centers are marked anchors of the comparison graph, (9) replaces (10), giving the stronger `F_c>=-(A+2D)`. This distinction matters when a wall's deterministic center level is not an integer cut; no marked-cut assumption is implicit in (5).

Define U'_c by the negative part of the minimum of (15) in G, with zero for an empty feasible family. The same locality and measurability argument applies. Equation (17) and (2) prove (5). The number of possible endpoint occurrences never enters the bound.

## 6. Extrema, measurability and finite support

Fix the local input record. A compact nominal window contains finitely many edge occurrences. Each occurrence, including its endpoint fractions, is a compact interval after restricting to a closed nominal window. Its parameter and partial costs are continuous; so is its interpolated gauge. Distinct visits to one physical point retain separate occurrence labels.

For R, each pair of occurrence intervals on a prescribed road gives a compact feasible set of endpoint fractions, including the closed occurrence-order condition. For S, equality of the two physical points adds a closed condition. The corrected objectives are continuous. Finite unions therefore have maxima when nonempty.

For U', subdivide the deterministic subgraph at all boundary intersection points. A minimizing physical path can have each closed excursion deleted: its endpoints, endpoint corrections and signed arms stay fixed, and its passage cost decreases because edge weights are positive. A path with no such excursion has a simple vertex skeleton, with at most two extra endpoint partial-edge segments. There are finitely many such skeletons in the finite graph. Include the direct same-edge route and the constant route when endpoints coincide. Endpoint degeneracies can be retained in closed route templates even when a zero-length segment then appears. Every template is a genuine path, and deleting loops shows that their finite union contains a global minimizer if any competitor exists.

For each template and labeled endpoint-occurrence pair, the two endpoint fractions lie in `[0,1]^2`. Membership in the closed windows and subgraph, the specified route orientations, and any physical coincidences are closed constraints. They can be expressed by `F(q)=0` with F continuous, nonnegative, and measurable in the local record. The objective c is continuous in q and measurable in that record. On a nonempty feasible compact set,

`min_(F=0)c = lim_(j->infinity) inf {c(q): q rational in [0,1]^2, F(q)<1/j}`.  (18)

For justification, the sets on the right decrease with j. Continuity near a minimizer gives limsup at most the minimum. Any sequence of nearly minimizing relaxed rational points has a convergent subsequence by compactness. Its limit has F=0, and continuity gives the reverse inequality. If the feasible set is empty, compactness gives `min F>0`, so the sets are eventually empty and their infima are +infinity. Every rational infimum is measurable; so are the limit and the finite or countable infimum over coded templates. The random number of occurrences causes no difficulty: the paper's local record has a countable measurable collection of finite codes.

The same reasoning for -c gives the maxima used in R and S. It also gives measurable selected endpoint fractions if needed: on the compact minimizer set, successively minimize its first and second coordinates, expressing each new minimization through the same relaxed formula with additional continuous equality constraints. A fixed order of relative route codes resolves ties.

All these definitions read only the prescribed subgraph and the local road/gauge supports. Analytic comparison paths and the nonlocal calibration may enter the expectation proof, but their realized inputs do not enter the envelope definitions. If the graph is disconnected or no endpoints can be joined, the empty-family convention applies. Extra closed band or drawdown constraints preserve the argument when loop deletion preserves them, as it does for constraints inherited by subsequences of the traversal order.

## 7. Why the finite comparison hypotheses are available conditionally

The preceding finite-cell result gives (1) with `kappa=C_H K`, where K is the network increment constant and C_H depends only on the fixed support radius H. For the prescribed additional labels audited in round 5 one can use `H=ceil(D_0)+30`, `K=20ceil(D_0)+41`, where D_0 bounds the nominal anchor displacement from its assigned coarse index. This is a pairwise estimate; the present finite sums deliberately retain the factor counting the prescribed comparisons.

After including the centers in each nominal span, suppose there are m spans of length at most L. The periods whose closed parameter intervals meet them number at most `N<=m(ceil(L)+2)`. This generous count includes integer endpoints and their pauses. Their bounding anchors number at most 2N. Assign coherent coarse indices along each translated road; consecutive period anchors then have neighboring indices. Let every required index lie in `Q_b(0)`, with b a fixed integer determined by the macroscopic neighborhood. Connect each anchor to the canonical anchor at its index by one same-index label comparison, then to index 0 by at most 2b canonical grid comparisons. Add the N period edges. This gives a connected comparison list with

`M <= 2N(2b+1)+N = N(4b+3)`.                                   (19)

The same count obtained anchor by anchor is `4bN+2N+N`. Both counts are independent of n, microscopic vertex count, and the number of candidate physical paths. Fixed road/gauge support radii and bounded b give a fixed support radius for the envelopes. Uniform phase-conditioned estimates still require (1) and the period-defect bounds after conditioning; they do not follow from an unconditional estimate alone.

## 8. Limits

Equations (3)–(5) establish the local-envelope statement under its specified inputs, including the simultaneous physical-competitor lower bound. They require finitely many prescribed labels and bounded road-adjustment spans. They give no uniform bound over arbitrarily many labels selected from their realized errors, over unbounded adjustment lengths, or between unrelated calibration worlds. The physical competitor always charges positive traversal costs; only its endpoint road arms are signed.

The remaining manuscript checks include `found:lem-gauge-tail`, phase locality and the phase-conditioned estimates, the link propositions, and closure of the improved road class. This envelope calculation does not establish strict convexity for any FPP law.

## 9. Exact finite checks

The accompanying [check_envelope.py](check_envelope.py) uses rational arithmetic. It checks the interpolation and signed-interval identities on 2187 configurations and 54675 occurrence pairs, including nominal pauses. A 21-vertex subdivided grid supplies physical paths with edgewise domination in both orientations. Dijkstra and Floyd computations agree on all 441 distances. The resulting 5808 endpoint checks, 17424 center-adjusted checks and 480 switch coincidences agree with the displayed formulas. These finite examples supplement the general argument above.

The fixture has N=4 periods and M=9 listed comparisons. Its total defect has the independent unsubdivided-edge count

`D = (24-16)/7 + (3*2+5+2*6+7+8+9+12)/13`

`  = 8/7+59/13 = 517/91`.

The first numerator subtracts the total calibration increment from the total absolute edge increments; the second counts the positive edge slacks with road traversal multiplicity. This agrees with the sum of the four period defects. The script also checks adding physical loops, a common gauge offset, and the failure of variants that omit the interpolation defect, cancel different calibrations, or confuse signed reversal with physical reversal.
