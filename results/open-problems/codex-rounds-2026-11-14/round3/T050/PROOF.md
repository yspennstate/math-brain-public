# A positive defect bound for local roads with Gamma weights

This note proves an auxiliary lower bound. It does not prove strict convexity.
It extends the distributional scope of the lower-bound ingredient in
OpenAI, *Strict convexity and differentiability of the planar exponential
first-passage limit shape* (September 24, 2026), Proposition 9.5, and sharpens
its final comparison by using a bounded excess cost. The source is
[the opened manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf).

## Statement and assumptions

Give the edges of the scaled square lattice G_n = n^{-1} Z^2 independent
Gamma(kappa, lambda) weights, with kappa, lambda > 0. A microscopic edge keeps
its full weight after the spatial rescaling. Thus this note uses original
passage-cost units. Repeated traversals are charged repeatedly.

Fix linearly independent rational vectors v,w, 0 < s < 1/4, and put

    A = v + s w,       B = w + s v,
    ||x||_* = |[v w]^{-1}x|_infinity,
    r = s/1000,        rho = 2r.

Take n with nA,nB in Z^2. Suppose a stationary extension of the weight space
carries an additive calibration C_n satisfying, simultaneously for lattice
vertices,

    |C_n(x,y)| <= T_n(x,y),
    E C_n(x,y) = n h(y-x),
    C_n(x+z,y+z; omega) = C_n(x,y; theta_z omega),

where h is a deterministic linear functional and T_n is the passage metric
on G_n. Stationarity includes the extension variables. The road rules below
use only the edge weights and independent private inputs, not the extension
variables. No locality of C_n is assumed.

An admissible d-road, d=A or B, has the following properties.

1. It is an oriented, two-sided nearest-neighbor walk with a continuous
   nondecreasing nominal parameter t tending to the respective infinities
   at its ends. Compact parameter intervals contain finitely many edge
   occurrences. At parameter t its location x obeys ||x-td||_* <= r.
2. Its restriction to a deterministic parameter interval I, with its cuts
   and occurrence labels, is determined by inputs within distance 10 of
   {td:t in I}. Private inputs have spatial locations, product law, and
   translation actions preserving that law. They are independent of the
   stationary extension. Fresh translated copies of the rule are allowed.
3. Translation by d and shift of parameter by one commute with the rule.
   At integer level i mark its first occurrence X_i. The segment from X_i
   to X_{i+1} has finite expected cost. A pause at an integer level belongs
   to the following period.

For partial edge traversals interpolate the potential C_n(0,x) affinely
and charge the corresponding fraction of the edge weight. Define

    Q(gamma) = tau(gamma) - n h(y-x),
    D(gamma) = tau(gamma) - C_n(x,y)

for a path from x to y. For a pair of roads let

    beta = max{ E Q(gamma_A[0,1]), E Q(gamma_B[0,1]) }.

Choose uniform geometry bounds K,M >= 1 with

    ||e_i||_* <= K (i=1,2),       |A|_2, |B|_2 <= M.

Here e_i are the unscaled coordinate unit vectors, so a microscopic edge
has *-length at most K/n. Set

    L = 200,              C_R = 2(L+2) = 404,
    C_V = (8M+3)^2,        C_E = 2 C_V,
    theta = lambda (6^(1/kappa)-1),
    a = log(2)/(8 K theta),
    epsilon = min{1/2, 1/(8 sqrt(kappa C_V))},
    q_n = (16/3) C_V n^2 exp{-3 log(2)n/(8K)}.

**Theorem.** For every such pair, once n >= K/r and q_n <= 1/8,

    beta >= 3 a epsilon/(8 C_R) > 0.                    (1)

The bound is uniform over road rules and over s,v,w for which the same K,M
work; the lower threshold on n may depend on r. Consequently the same bound
holds for the infimum of beta over this road class. No existence of a
minimizing pair is required.

## Proof

### 1. Periods and random cuts

Put P(x)=C_n(0,x)-nh(x). For any directed edge traversal the calibration
increment has absolute value at most its weight. This follows by domination
by passage time and comparison with that single edge. It remains true for
partial traversals by affine interpolation. Therefore D is nonnegative on
every forward subpath and additive under concatenation.

The marking convention and covariance give

    X_1(omega,U) = d + X_0(theta_d omega,theta_d U).

Additivity and covariance of the centered calibration imply

    P_omega(X_1) = P_omega(d)
                 + P_{theta_d omega}(X_0(theta_d omega,theta_d U)).

All terms are integrable. Indeed, each marked cut lies in a deterministic
bounded neighborhood of its nominal location, hence on one of finitely many
edges at fixed n. Connect 0 to all their endpoints by a finite collection
of deterministic coordinate paths. Domination bounds the absolute
calibration at every such endpoint by the sum of weights in this finite
collection; affine interpolation bounds the cuts inside the edges. Gamma
weights have finite mean.

The first term on the right has mean zero. Stationarity gives equality
of the mean of the second term and the mean of P(X_0). Hence

    E[P(X_1)-P(X_0)] = 0,
    E D(gamma[0,1]) = E Q(gamma[0,1]).                 (2)

Translation gives the same identity for every period and translated road.
In particular beta >= 0. The mean of P at a selected cut itself need not
be zero. If a selected forward road portion is contained between marked
cuts with indices j and k, its defect is at most the sum of the k-j complete
period defects. This is a pathwise consequence of additivity and
nonnegativity and requires no independence of the selected endpoints.

### 2. Two paths with common endpoints

Use (xi,eta)=[A B]^{-1}x as oblique coordinates. Since

    [v w]^{-1}[A B] = [[1,s],[s,1]],

the infinity operator norms of this matrix and its inverse are 1+s and
1/(1-s). In particular

    |(xi,eta)|_infinity <= 2 ||x||_*,
    ||x||_* >= (3/4)|(xi,eta)|_infinity.               (3)

Make four translated copies of the road rules, on nominal lines eta=0,
eta=L (A-roads) and xi=0,xi=L (B-roads), using fresh independent private
fields. These translations are lattice translations because nA,nB are
integer vectors. Each road stays within oblique distance rho of its
nominal position.

At each nominal corner, inspect parameter windows of half-width 4rho on
the incident roads. In coordinates centered at the corner, the A-road
has a subarc crossing the rectangle [-2rho,2rho]^2 from left to right,
with |eta|<=rho. To obtain the subarc, stop at its first hit on xi=2rho
and start at its last preceding hit on xi=-2rho. These hits exist because
the inspected window starts with xi<=-3rho and ends with xi>=3rho.
The B-road similarly has a bottom-to-top subarc with |xi|<=rho.

These arcs intersect. One elementary form of the planar crossing lemma
says that a left-to-right arc in a rectangle meets a bottom-to-top arc.
For finite polygonal arcs, erase loops in the first arc, retaining a
simple arc; join its ends outside the rectangle on one side. The resulting
Jordan curve separates the bottom and top sides inside the rectangle.
Continuity forces the second arc to hit the first. This argument is
unchanged by an invertible linear coordinate transformation.

Any intersection of our two arcs has both coordinates at most rho in
absolute value, since it belongs to both narrow strips. Square-lattice
edges intersect only at a shared vertex or along a shared edge. Moving
to an endpoint of a shared edge changes oblique coordinates by at most
2K/n <= 2r = rho. The resulting common vertex is within 2rho of the
corner. Tracking puts each of its nominal parameters within 3rho of the
corner value. Thus both occurrences belong to the inspected windows.
Choose the lexicographically first eligible vertex and the first eligible
pair of occurrences there. This is a measurable choice from finite records.

Call the selected corner vertices p_00,p_10,p_01,p_11. Let R_1 follow the
bottom and right roads forward from p_00 through p_10 to p_11, and let
R_2 follow the left and top roads forward from p_00 through p_01 to p_11.
Corner parameter errors are less than one. Each side is contained in the
periods indexed -1,0,...,L, so (2) and the pathwise period bound give

    E D(R_j) <= C_R beta,        j=1,2.               (4)

Write D_j=D(R_j). Because the two routes have identical endpoints,

    tau(R_1)-tau(R_2) = D_1-D_2 <= D_1.              (5)

This one-sided inequality is the useful comparison.

### 3. A deterministic region avoided by the second rule

Let S have oblique coordinates

    |xi-L/2|<=2,       |eta|<=2,

and let E_n(S) be its internal microscopic edges. All the inputs needed
for R_2 lie within *-distance 10 of the left and top nominal segments
extended by parameter 4rho at both ends, together with the short bottom
and right corner windows needed to choose its endpoints. The unused
bottom-right corner window is separated as well. The oblique distance
from S to this deterministic union is at least L/2-2-4rho. By (3) its
*-distance is at least (3/4)(98-4rho)>10. Thus scaling weights on E_n(S)
leaves R_2 and both of its endpoints unchanged, including after its rule
and corner selections are recomputed. Private inputs are kept fixed.

The bottom-road portion with nominal parameter between L/2-1 and L/2+1
belongs to R_1. It lies in S, and so do both endpoints of each edge
occurrence it touches: the coordinate bounds are
1+rho+2K/n < 2 and rho+2K/n < 2. Remove at most a first and last partial
edge from this portion. Its remaining vertex endpoints are separated in
xi-coordinate by at least

    2-2rho-4K/n >= 2-4rho > 1.

This remains valid for nominal pauses. The chosen portion has finitely
many occurrences, and removing its endpoint occurrences shifts each
endpoint by at most one edge. Loop erasure preserves the remaining
endpoints and does not increase cost. Since each edge changes xi by
at most 2K/n, the erased path has at least floor(n/(2K)) edges.

Every vertex of S is at Euclidean distance at most 4M from its center.
An axis-parallel enclosing square therefore contains at most C_V n^2
lattice vertices, including boundary rounding. Orient every internal
edge to the right or upward; each vertex starts at most two such edges.
Consequently

    |S intersect G_n| <= C_V n^2,
    |E_n(S)| <= C_E n^2.                              (6)

### 4. A uniform lower-tail bound

For a Gamma variable X the density integral gives

    E exp(-theta X) = (lambda/(lambda+theta))^kappa.

Our choice of theta makes this 1/6. A self-avoiding path of m edges uses
distinct independent weights; exponential Markov inequality bounds the
probability that its cost is at most t by exp(theta t)6^(-m).
There are at most 4*3^(m-1) such paths from a given starting vertex.
Summing over m>=R gives

    P(some self-avoiding path from V has length >=R and cost <=t)
       <= (8/3)|V| exp(theta t) 2^(-R).               (7)

If the total R_1 cost on occurrences of edges of E_n(S) is less than an,
the loop-erased path in step 3 is a witness for (7) with
V=S intersect G_n, R=floor(n/(2K)), and t=an. Since
theta a=log(2)/(8K) and R>=n/(2K)-1, (6) and (7) show that this event
has probability at most the displayed q_n. Thus, on an event H with
P(H)>=1-q_n, R_1 spends at least an on the edges that will be scaled.
This bound includes all possible selected routes; it does not condition
on a selected path and then incorrectly assert independence of its weights.

### 5. Cost of changing the law

Put b=1-epsilon/n and let F multiply all weights of E_n(S) by b.
Let P_0 denote the edge/private-input marginal law and P_1=F_*P_0.
Use different notation for these probability laws and the potential P(x).
For X~Gamma(kappa,lambda), bX has density

    p_b(x) = b^(-kappa) lambda^kappa x^(kappa-1)
             exp(-lambda x/b)/Gamma(kappa).

The log density ratio against the original density is

    log(p_b(x)/p_1(x)) = -kappa log b - lambda x(1/b-1).

Taking expectation with respect to p_b, whose mean is b kappa/lambda,
gives relative entropy kappa(b-1-log b). For x=epsilon/n<=1/2,

    -x-log(1-x) = integral_0^x t/(1-t) dt <= x^2.

Independence and (6) therefore give

    KL(P_1 || P_0) <= kappa C_E epsilon^2,
    TV(P_1,P_0) <= epsilon sqrt(kappa C_E/2)
                 = epsilon sqrt(kappa C_V) <= 1/8.   (8)

Here TV is half the L^1 distance. For completeness, the entropy inequality
used in (8) follows by applying the log-sum inequality to an event and its
complement. The resulting binary entropy, as a function of its first
probability p with the second probability q fixed, vanishes with zero
derivative at p=q and has second derivative 1/[p(1-p)]>=4. It is therefore
at least 2(p-q)^2. Take the supremum over events.

### 6. Transfer a bounded excess cost

Let v_0=a epsilon. In any environment define W to be the cost of the
recomputed R_2 minus the passage time between its recomputed endpoints.
This is a nonnegative measurable function of edge weights and private
inputs. Passage time is the infimum of a countable set of finite path
costs, so this assertion does not require existence of a geodesic.
Let f=min(W,v_0), so 0<=f<=v_0.

On H, the old path R_1 saves at least v_0 under F. The old R_1 remains a
valid physical competitor between the unchanged R_2 endpoints. It need
not be the route that its rule would select in the changed environment.
By (5),

    W(F omega,U) >= v_0-D_1(omega,U) on H.

Clipping preserves this lower bound because D_1>=0. Outside H the
clipped quantity is at least zero. Taking expectations on the original
stationary extension gives

    E_{P_1} f >= v_0(1-q_n)-E D_1.                   (9)

For a function with range [0,v_0], the difference of its expectations
under two laws is at most v_0 times their total variation. This follows
by writing f as the integral of its level-set indicators. Thus

    E_{P_0} f >= v_0(1-q_n-TV(P_1,P_0))-E D_1.

In the original environment domination yields W<=D_2, also at the
random endpoints, because it holds simultaneously for all lattice pairs.
Combine this with (4), (8), and q_n<=1/8 to obtain

    2 C_R beta >= E D_1 + E D_2
                >= v_0(1-q_n-TV(P_1,P_0))
                >= (3/4) v_0.

This is (1). Notice that the changed law is used only for f, which has no
calibration input. A calibration on a stationary extension is sufficient;
it is never evaluated in the changed environment. Taking the infimum
over road pairs completes the proof.

## Relation to a hypothetical flat face

For iid Gamma weights all moments are finite and there is no atom at zero.
The stationary calibration above is supplied by Michael Damron and Jack
Hanson, *Busemann functions and infinite geodesics in two-dimensional
first-passage percolation*, [arXiv:1209.3036](https://arxiv.org/abs/1209.3036),
Section 3: Proposition 3.2 gives stationarity, Proposition 3.4 additivity
and domination, and Theorem 3.5 identifies the mean with the prescribed
supporting functional. Their construction starts with any supporting
functional, as specified in Section 3.1; see
[the primary PDF](https://arxiv.org/pdf/1209.3036).

Choose h supporting a putative nontrivial face and v,w in its cone near
the extreme endpoints. Those endpoints are linearly independent, so their
neighborhoods admit uniform finite K,M. Applying the theorem gives the
positive lower bound for the Gamma version of the admissible class.
The calibration construction is an external theorem, not reproved here.
No contraction inequality for this Gamma class is established.

## Independent checks on the constants

The cheap-path estimate can instead use only the first R edges of any
long witness. There are at most 4*3^(R-1) such prefixes per starting
vertex, so the right side of (7) improves to
(4/3)|V| exp(theta t)2^(-R). This independently verifies the weaker
constant used above. Its exponent after rounding is still
-3 log(2)n/(8K).

A separate likelihood calculation checks the law-change bound without
entropy. If l=p_b/p_1 is the one-edge density ratio, direct integration gives

    E_{p_1} l^2 = [b(2-b)]^(-kappa)
                 = [1-(epsilon/n)^2]^(-kappa).

For m=|E_n(S)| independent changed weights,

    E_{P_0}(dP_1/dP_0)^2 = [1-(epsilon/n)^2]^(-kappa m).

Since -log(1-u)<=u/(1-u)<=4u/3 for u<=1/4 and
kappa C_E epsilon^2<=1/32, this is at most exp(1/24).
Cauchy-Schwarz gives

    TV <= (1/2)sqrt(exp(1/24)-1) < 1/8.

The final strict inequality uses exp(1/24)<=24/23<17/16. Thus both
entropy and second moment give the same required tolerance.

The clipped transfer can also be checked by integrating tail events.
For 0<t<v_0, on H the implication D_1<v_0-t => W(F omega)>t holds.
Integrating its probability over t gives
E_{P_1}f >= v_0(1-q_n)-E min(D_1,v_0), which implies (9).
This confirms the direction and the coefficient of the final inequality.

For kappa=lambda=1, theta=5 and a=log(2)/(40K), matching the exponential
threshold. With the same geometry and epsilon, (1) is three times the
source's displayed a epsilon/(8 C_R) bound. This is only an improvement
of that certified constant, not an optimality claim. Changing lambda
multiplies the bound by lambda^(-1), as passage costs require. As kappa
tends to zero the constant can tend to zero; uniformity in kappa is not
asserted. Loops, repeated edges, and nominal pauses do not affect the
argument because costs count occurrences and loop erasure is used only
to produce a witness for the uniform lower-tail event.
