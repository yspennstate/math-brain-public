# Simultaneous envelopes from anchor increment estimates

The following finite-window theorem supplies the passage from anchor
estimates to arbitrary attachments. Its constants retain the number of
periods and anchor comparisons. No independence is needed in this step.

## 1. Data and notation

Work on a lattice metric graph with finite positive edge weights. A path
cost counts traversal multiplicity and charges fractions of edges in
proportion to their lengths. Fix a deterministic linear functional f on
the ambient space. For a physical path from x to y put

    Q(path) = cost(path) - f(y-x).

Suppose a random potential P, affine on each physical edge, satisfies

    D(path) := Q(path) - P(y) + P(x) >= 0                 (1)

for every finite physical path, simultaneously. In particular this holds
for selected paths and interior-edge endpoints. P may be nonlocal.

There are m road windows. Window a consists of p_a >= 1 complete marked
periods, indexed i=0,...,p_a-1, with anchors x_{a,i}. A shorter window may
be enclosed in such a window. Traversal order is distinguished from
physical location: repeated visits have different occurrence labels.
Each period has finitely many edge occurrences and a continuous
nondecreasing nominal parameter t from i to i+1. Pauses are allowed.
The first occurrence at an integer starts the following period.

Let g_{a,i} be local integrable anchor gauges. Define

    D_{a,i} = D(road a from anchor i to anchor i+1),
    e_{a,i} = g_{a,i+1}-g_{a,i}
              -P(x_{a,i+1})+P(x_{a,i}),
    C_{a,i} = Q(road a from anchor i to anchor i+1)
              -g_{a,i+1}+g_{a,i}.

All these variables are integrable. Thus

    C_{a,i} = D_{a,i}-e_{a,i}.                         (2)

Choose a finite deterministic tree T whose vertices include the starting
anchors x_{a,0}, with their road labels. Additional anchor vertices are
permitted. Every vertex v has an integrable gauge g_v and a physical
anchor x_v. Distinct vertices may represent the same physical point.
For each oriented tree edge u -> v define

    e_{uv} = g_v-g_u-P(x_v)+P(x_u).

Assume its absolute first moment is finite. Write

    p = sum_a p_a,       q = number of edges of T,
    Lambda = 2 sum_{a,i} E D_{a,i}
             + sum_{a,i} E|e_{a,i}| + sum_{uv in T} E|e_{uv}|.       (3)

All full window records and all their anchor gauges are measurable from
one deterministic finite set S of local inputs. Records include the
continuous nominal maps along the finitely many occurrences. The
comparison-tree errors are only estimates; they need not be local and
are not additional inputs to the envelopes below.

For an occurrence o in period i, with parameter t, extend the gauge by

    g_a(o) = g_{a,i} + Q_a(i,o) - (t-i) C_{a,i}.        (4)

Here Q_a(i,o) is the forward physical cost Q along that road. For two
occurrences in reversed order, a *signed road cost* is defined by
negating the forward cost. It is an accounting convention; it is not
the cost of a physical path traversed backward.

## 2. Theorem

Fix an integer K >= 0. There is a nonnegative S-measurable variable U
with

    E U <= (2K+1) Lambda                              (5)

which simultaneously bounds:

* the absolute corrected signed cost of every subtrip in any window;
* every absolute gauge difference at a common physical point of two
  window occurrences;
* the absolute corrected signed cost of every concatenation of road
  subtrips with at most K switches at common physical points.

The corrected cost of a trip from occurrence x to occurrence y is its
signed Q-cost minus its terminal gauge plus its initial gauge. At a
switch, the end label and the next start label may differ.
A switch counts any transfer between occurrence records at a common point,
including a transfer between different visits of the same road. Each leg
is one interval in occurrence order, with either sign.

Let G be a prescribed deterministic finite closed metric subgraph.
For each window fix a center occurrence c_a in that window, chosen by
a local measurable rule. There is a nonnegative local variable U' with

    E U' <= 3 Lambda                                 (6)

such that every physical path gamma in G from an occurrence x in
window a to an occurrence y in window b satisfies

    Q_a(c_a,x) + Q(gamma) + Q_b(y,c_b)
                   -g_b(c_b)+g_a(c_a) >= -U'.         (7)

The two road arms in (7) are signed road costs. The support of U' is
contained in S together with the edge inputs of G. The bounds do not
depend on the number of microscopic vertices, occurrences or possible
paths in G.

If, for some beta >= 0 and c >= 0,

    E D_{a,i} <= beta,
    E|e_{a,i}| <= c beta,       E|e_{uv}| <= c beta,

then

    Lambda <= [2p+c(p+q)] beta.                       (8)

In particular the conclusion has an explicit constant for fixed m,
window lengths and comparison-tree size. Neither (5) nor (6) asserts
uniformity as those structural quantities tend to infinity.

## 3. Variation along a period

Write h_a(o)=g_a(o)-P(x(o)). Subtract P in (4) to get

    h_a(o)-h_a(i) = D_a(i,o) - (t-i) C_{a,i}.         (9)

The first function on the right is nondecreasing along the entire
occurrence order: its increment on a forward subpath is the nonnegative
quantity (1). Its total increase is D_{a,i}. The nominal parameter is
also nondecreasing with total increase one. Therefore the total variation
of h_a on that period is at most

    D_{a,i} + |C_{a,i}|.                             (10)

For completeness, for any finite ordered partition o_0,...,o_r of the
period, the triangle inequality in (9) gives

    sum_j |h_a(o_j)-h_a(o_{j-1})|
       <= sum_j [D_a(o_{j-1},o_j)
                  + (t_j-t_{j-1}) |C_{a,i}|]
       = D_{a,i}+|C_{a,i}|.

Take the supremum over partitions. Pauses cause no difficulty because
their nominal increments vanish while their defects remain nonnegative.
At the end of a period, (2) makes (4) equal the next anchor gauge.
Thus the gauges and h are continuous in traversal order across marks,
including a pause assigned to the next period.

Define the possibly nonlocal variable

    B = sum_{a,i} [D_{a,i}+|C_{a,i}|]
                         + sum_{uv in T}|e_{uv}|.     (11)

Equation (2) gives

    E B <= Lambda.                                  (12)

For any two window occurrences o,o', one has

    |h(o')-h(o)| <= B.                              (13)

If both lie in one window, traverse that window between them and use
(10). Otherwise go from the first occurrence back to its starting
anchor, follow the unique path in T between the two starting anchors,
and then go forward to the second occurrence. Each of the two window
portions uses each of its periods at most once. The tree path uses
each edge at most once. The increment of h across a tree edge is
exactly e_{uv}, with the appropriate sign. All these terms are included
in (11), proving (13). Multiple physical visits do not change this
argument, which is an argument on labeled occurrences.

## 4. Local road and switch envelopes

If ordered occurrences o,o' belong to the same period, (4) cancels to

    Q_a(o,o') - g_a(o') + g_a(o)
                          = [t(o')-t(o)] C_{a,i}.     (14)

For a subtrip across several periods, split at the intervening marks.
The coefficients have absolute value at most one, and no period is
used twice. Consequently every absolute corrected signed subtrip cost
is at most the local variable

    A = sum_{a,i}|C_{a,i}| <= B.                     (15)

Let S_switch be the supremum of |g_b(o')-g_a(o)| over pairs of window
occurrences with the same physical point; set it to zero if there are
none. Since P has the same value at that point for both occurrences,
(13) gives

    S_switch <= B.                                 (16)

Both A and S_switch use only S. Their measurability, including the
supremum in S_switch, is justified in Section 6.

Set

    U = (2K+1) max(A,S_switch).                      (17)

A concatenation with r <= K switches has r+1 road legs. On summing
their corrected costs, the remaining gauge adjustments at switches
are g_old(o)-g_new(o'). Their absolute values are at most S_switch.
The global corrected cost therefore has absolute value at most

    (r+1) A + r S_switch <= U.

Individual subtrips and switch differences are also bounded by U.
Equations (12), (15) and (16) prove (5).

## 5. Physical competitors

For a physical gamma from x in window a to y in window b, (1) yields

    Q(gamma)-g_b(y)+g_a(x)
        >= P(y)-P(x)-g_b(y)+g_a(x)
         = h_a(x)-h_b(y) >= -B.                     (18)

The left side of (7) is the expression on the left of (18), plus the
two corrected signed road arms

    Q_a(c_a,x)-g_a(x)+g_a(c_a),
    Q_b(y,c_b)-g_b(c_b)+g_b(y).

Each has absolute value at most A by (15). Thus every expression (7)
is at least -B-2A >= -3B, simultaneously over endpoints and paths.

Define U' as the supremum of the negative parts of those expressions,
over all allowed endpoint pairs and physical paths in G. Set U'=0
when the family is empty. It is a local measurable variable by Section
6. It obeys U' <= 3B, so (12) proves (6). This construction does not
require a local pointwise upper bound on |P-g| at one anchor.

## 6. Measurability and the support of the suprema

A full window can be parameterized on [0,1] in traversal order, assigning
positive parameter length to each nonconstant edge occurrence. Both its
physical position x_a(r) and its gauge g_a(r) are continuous. Constant
occurrences can be retained with constant position and gauge. The
parameterizations are measurable functions of the finite local records.
There are only countably many possible finite edge records.

For two such windows put

    F_j(r,s) = |g_b(s)-g_a(r)| - j |x_b(s)-x_a(r)|.

For each j, continuity identifies its supremum on [0,1]^2 with its
supremum on rational parameter pairs, a measurable countable supremum.
The positive parts of these suprema decrease as j increases. Their
limit is the desired common-point supremum, with value zero when
there is no common point. To prove this assertion, a common-point
pair gives the lower bound for every j. For the reverse bound, take
maximizing pairs along a subsequence on which a positive limiting
value is attained. The gauge differences are bounded on the compact
parameter square, so their physical distances must tend to zero.
A convergent subsequence therefore limits to a common-point pair;
continuity gives the upper bound. If there is no common point, the
physical distance has a positive minimum and the limit is zero.
Taking a maximum over the finitely many window pairs proves the
claimed measurability of S_switch. Only local records and gauges enter.

For U', split each edge occurrence at the endpoints of its intersections
with G. A finite closed metric subgraph meets each physical edge in
finitely many closed segments or points. There are therefore finitely
many allowed compact occurrence pieces. On each such piece, use its
edge fraction as a parameter on [0,1]; singletons are constant pieces.
The gauges and signed arm costs are continuous in this parameter.

Consider two pieces lying in one connected component of G. The
shortest-path distance d_G between their endpoints is continuous.
Indeed its change when either endpoint moves is at most the sum of
the weighted lengths by which the endpoints move within their edge
segments. A finite positive weighted graph attains this distance: a
minimizer can be chosen with no repeated vertex after subdividing at
the two endpoints, and there are finitely many resulting simple route
types. Thus replacing cost(gamma) by d_G(x,y) gives exactly the infimum
over physical paths with these endpoints. The resulting expression
in (7) is continuous on the compact parameter square. Its minimum
equals the infimum over rational pairs. Distances are minima over
finitely many measurable path sums, so this minimum is measurable.
Ignore pairs in distinct components, which admit no path. A finite
maximum of the negative parts of the minima is U'. Empty families
give zero. The argument proves both finiteness and measurability.

The variables defining U use only the full window inputs and their
anchor gauges. U' also uses the weights of G. The potential P and the
comparison-tree variables were used only to prove estimates. In
particular, adding intermediate tree anchors for an estimate does not
enlarge the support of the observable envelopes. If every window
input and anchor-gauge support lies in a deterministic spatial region,
the same region supports U, irrespective of how many labels occur
there. This support statement does not give a label-independent
expectation bound.

## 7. A second estimate and the dependence on label count

There is a separate check of the coefficient in (10). Let theta=t-i,
and let F(o)=D_a(i,o). Then 0 <= F(o) <= D_{a,i}, and (2), (9) give

    h_a(o) = (1-theta) h_a(i) + theta h_a(i+1)
                         + F(o)-theta D_{a,i}.       (19)

For two ordered occurrences, their h increment is

    (theta'-theta) e_{a,i}
       + [F(o')-F(o)] - (theta'-theta) D_{a,i}.

The two nonnegative terms in the final difference lie between 0 and
D_{a,i}. This independently bounds the absolute increment by
D_{a,i}+|e_{a,i}|.
For a general partition, the monotone F and theta terms give the
variation estimate (10). Finally (2) gives

    D_{a,i}+|C_{a,i}| <= 2D_{a,i}+|e_{a,i}|,

which verifies (3), (8) and (12) by direct summation. The switch count
is independently r+1 legs and r switch adjustments, yielding 2r+1.
For a physical competitor the three contributions are one endpoint
error difference and two corrected arms, giving the factor three.

A coefficient independent of the number of labels cannot follow from
the increment assumptions alone. Fix m >= 2 and beta > 0. Let J be
uniform on {1,...,m}, available as one local input. Take P=0, a root
gauge g_0=0, and f=0. Let each of the m labeled one-period windows
traverse the same edge out and back, starting at the same vertex.
Give this edge weight beta/2, so every period has Q=D=beta. Set its
nominal parameter equal to its cumulative passage cost divided by beta.
Give label a the same gauge at both anchors, namely

    g_a = beta [m 1_{J=a}-1].                        (20)

All gauges have mean zero, so anchor means are preserved. Period
increment errors vanish and C=beta. Formula (4) makes the gauge constant
along the whole window because Q_a(0,o)=t beta. In particular all m
gauges are available at their common starting vertex. Every root
comparison has

    E|g_a-g_0| = 2 beta (1-1/m) <= 2 beta.

For a != b, E|g_a-g_b|=2 beta as well. Thus even all individual
pairwise comparison errors have a fixed bound. Nevertheless

    max_a |g_a-g_0| = (m-1) beta

on every outcome. Any simultaneous switch envelope has expectation
at least m beta, since the difference between the exceptional label
and any other label is m beta at their common vertex. The root maximum
already gives the weaker value (m-1) beta if a reference window with
gauge zero is also included. The first-moment calculation also follows by
separating the event J=a, of probability 1/m, from its complement:
beta[(m-1)/m+(m-1)/m]. The maximum is deterministic since exactly
one label has value (m-1) beta and all others have value -beta.

This finite-window example concerns the sufficiency of the anchor
estimates, not a counterexample to an FPP statement or to a particular
canonical gauge construction. It explains why the count in (8) must
be retained when only these estimates are available.

## 8. Application and limits

Round 4's finite-cell theorem supplies the needed anchor increment
estimates: neighboring registrations cost C_{d,H} epsilon; a comparison
along ell neighboring registrations costs at most ell C_{d,H} epsilon
by telescoping. Connecting the starting anchors by such chains gives
the finite tree used above. The road-period defect bound is a separate
input. This proves the simultaneous-envelope step under these explicit
inputs, including arbitrary selected attachment occurrences and interior
edge points, without counting microscopic occurrences.

The relevant source is OpenAI, *Strict convexity and differentiability
of the planar exponential first-passage limit shape*, September 24, 2026,
[manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf),
Section 10.3 and Lemma 10.4. The theorem above makes that finite-window
step explicit. It does not bound the label or tree counts in later
constructions, prove a contraction, or establish strict convexity.
