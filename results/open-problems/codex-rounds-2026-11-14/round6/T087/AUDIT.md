# Audit of the conditional largest-cluster exponent

## The predecessor bounds

The round 5 rectangle step can be checked without summing its union
bound. Each face rectangle's maximum disjoint crossing count D has
tail at most R^k, so D is stochastically dominated by a geometric
variable with mean R/(1-R). The deterministic component-to-path
comparison then gives E K_n<=2d R/(1-R), with one factor 2d.

For its shell, the identity

    (2h+1)^d-(2h-1)^d
      =2 sum_{i=1}^d (2h-1)^{i-1}(2h+1)^{d-i}

counts by the first extremal coordinate and independently gives
S<=2d(2h+1)^{d-1}. Multiplying by 2d and using 2h+1<=4n/m gives
C_d=4d^2 4^{d-1}. At d=3, n=8m, h=12,

    S=25^3-23^3=3458,
    S=2*25^2+2*23*25+2*23^2=1250+1150+1058=3458,
    2d*S=20748,
    C_3*(n/m)^2=576*64=36864.

Thus the bound is in the correct direction at its limiting allowed
scale ratio. Its last-exit path extraction and small-box injection
remain valid when paths revisit the inner surface or end at corners.

## The tree packing

The extraction is performed on a spanning tree, rather than an induced
subgraph, so cycles and extra open edges cannot spoil it. At the deepest
vertex with a large descendant subtree, write the sizes of its child
subtrees as s_1,...,s_j. Each s_i<=t-1 and j<=Delta, so
the selected set has 1+sum s_i<=1+Delta(t-1)<=Delta*t vertices.
This is also seen as one root plus at most Delta branches, each too
small to have triggered an extraction on its own.

After k-1 removals, a tree that started with Delta*k*t vertices has
at least Delta*t vertices left. The construction cannot run out before
its kth selection. If the selected subtree is the entire current tree,
it is the last needed extraction or the initial size inequality would
be violated. For t=1 the construction simply removes leaves.

A star shows why an unrestricted graph degree cannot silently be
replaced by the constant 2: there may be many leaves but few disjoint
connected subsets of size at least two. Here Delta=2d is the actual
lattice degree bound. No assertion for unbounded-degree graphs follows
with the same constant.

## An independent check of k! and t^k

Sample k ordered roots independently and uniformly from the V vertices,
after fixing the edge configuration. If k disjoint extracted sets each
have at least t vertices, the chance that the sample hits a different
set in each coordinate is at least k!*(t/V)^k. These events for the
k! orders are disjoint. On each such sample, the k volume events have
disjoint open witnesses. Averaging over edge states and applying BK
for each fixed tuple bounds the unconditional chance of disjoint
witnesses by f_H(t)^k. Hence

    P(M_H>=Delta*k*t)*k!*(t/V)^k <= f_H(t)^k,

which recovers (7) by a second normalization calculation. Sampling
with replacement does not invalidate the bound: the lower bound uses
only samples in distinct extracted sets, hence distinct roots.

The volume event at a root is increasing. It is witnessed by finitely
many open edges in a connected subset of t vertices. Additional open
edges between the sets may merge their clusters, but they leave these
witnesses valid. BK does not require the full clusters to be distinct.
This is the key distinction from the nonmonotone crossing-count event.

## Exponents and thresholds

The cluster-tail exponent b=a/(d-a) gives
1+b=d/(d-a)=d/D. The finite-volume upper scale can therefore be found
in two ways: solve V F(t)/t=1 in logarithmic order, giving
d-(1+b)*log t/log n=0; or eliminate the tail parameter from
t^{1+b}=n^d. Both give t=n^D. At t=n^{D+h}, both give the residual
power -h*d/D, checking its sign in (11).

The integer t used for a fixed upper-tail threshold is a floor.
Then Delta*k*t<=n^{D+epsilon}, so the event of exceeding the latter
threshold implies the event bounded by the packing lemma. A ceiling
would reverse this needed inclusion near the threshold. For moments,
t_n is a ceiling and no such inclusion is used. The factorial series
bounds all fixed r>0; its successive-term ratio tends to zero.

The lower expected mass in the buffered argument is at least half of
V_{4m}pi(20m). Dividing by L_m<=2m^e gives the factor 1/4 in (21).
The two losses e are one from pi(20m)>=m^{-a-e} and one from L_m.
Its power is d-a-2e=D-2e. Choosing a good scale between
(n/16)^{1/(1+zeta)} and n/16 gives the exponent
(D-2e)/(1+zeta), which tends to D in the stated order of limits.
There is no inference that fixed-ratio arm probabilities are uniformly
comparable at every scale.

## Independence and the lower tail

The buffered variable U_m uses edges inside radius 7m; the annulus
variable J_m uses edges whose endpoints have norm between 8m and 16m.
Their edge sets are disjoint. W_m itself is not independent of J_m.
The covering boxes lie between radii 10m and 14m, so their connecting
paths cannot merge different annulus components outside the annulus.

For a nonnegative random variable Y with mean mu,

    E[Y 1_{Y>=mu/2}]>=mu/2,

and Cauchy–Schwarz gives the factor 1/4 in (23). Independently this is
the Paley–Zygmund inequality at parameter 1/2. Bounds
E M_n>=n^{D-h} and E M_n^2<=n^{2D+h} give a success probability
at least n^{-3h}/4. It is only subpolynomial, which is why a further
amplification step is necessary. The proof does not substitute an
expectation lower bound directly for a typical-size assertion.

For the amplification choose delta=epsilon/(4D), h=epsilon/4.
The target loss is at most delta*D+h=epsilon/2 before constants,
so the threshold in each small box exceeds n^{D-epsilon} eventually.
Expanding directly gives

    (1-epsilon/(4D))*(D-epsilon/4)
       =D-epsilon/2+epsilon^2/(16D).

Subtracting D-epsilon gives epsilon/2+epsilon^2/(16D)>0,
independently checking (27). The floor in m only changes a fixed
multiplicative constant, absorbed by this positive power margin.

Along each coordinate there are floor((2n+1)/(2m+1)) disjoint blocks.
Since floor x>=x/2 for x>=1, their number is at least n/(3m).
Counting coordinate choices gives at least 3^{-d} n^{d*delta} boxes.
A success probability at least m^{-d*delta/2} is at least
n^{-d*delta/2}. Thus the exponent in their product is

    d*delta-d*delta/2=d*delta/2=d*epsilon/(8D),

which independently checks the constant and power in (6). The product
formula concerns only internal edges of disjoint vertex boxes.
Connections through their complements are irrelevant to these events.

## Checks on the final conclusions

For r>=1, Jensen also gives the moment lower bound from E M_n.
For 0<r<1 that argument has the wrong direction, so the proof instead
uses the second-moment probability lower bound. It applies to all r>0.

As an exact arithmetic check, the planar value a=5/48 in dimension two
would give D=91/48, b=5/91, and 1+b=96/91=2/D. In dimensions with
mean-field arm exponent a=2, the conditional formula would give D=d-2.
For d>6 this does not assert the actual finite-box behavior, since the
predecessor count hypothesis is then a separate obstructed assumption.

The almost sure assertion uses the first Borel–Cantelli lemma on integer
scales. The polynomial upper bound is summable after taking A=2, and
exp(-c*n^u) is summable for every c,u>0. Independence across nested
boxes B_n is not required. Only countably many error tolerances are
intersected.

The original restriction 0<a<d/2 is retained when invoking the round 3
tail theorem. No result at a=0, a=d/2, or at p=1 is asserted. Almost
sure logarithmic convergence and the moment powers do not imply
bounded scale ratios, a nondegenerate scaling limit, or any of the
missing near-critical exponents. No numerical percolation estimate
has entered the argument.

No mathematical failure was found in this audit. The upper-tail packing
estimate holds on every finite bounded-degree Bernoulli graph; the
largest-cluster exponent conclusions remain conditional on the stated
unproved inputs for critical Z^3.
