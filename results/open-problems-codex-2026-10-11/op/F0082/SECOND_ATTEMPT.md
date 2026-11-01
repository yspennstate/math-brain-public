# Second attempt at F0082 — 2026-10-11

The remaining gap is a stationary non-crossing nearly perfect family with uniformly tight matched displacements. The previous attempt did not establish that tightness for Euclidean optimizers or subcritical-cost matchings.

Two previously untried approaches:

1. **Balanced convex cells.** Construct a translation-invariant tessellation into bounded convex cells, each containing equal red and blue counts. Finite Euclidean matching inside each cell would give the desired perfect planar matching directly, without an infinite matching limit. First test adaptive rectangles inside stationary horizontal strips. This is an explicit construction route; an obstruction for strip rectangles would delimit it but would not exclude arbitrary planar convex cells.

2. **A coercive objective compatible with uncrossing.** Find an increasing unbounded radial cost growing slowly enough to have uniformly bounded expected cost, while requiring every proper uncrossing to decrease the two-edge cost. This would combine automatic planarity with displacement tightness, bypassing divergent expected Euclidean length. The earlier capped-cost counterexample does not classify all such costs. Test whether the geometric uncrossing condition itself forces convexity/linear growth.

I will pursue Approach 2 first: it directly addresses the missing tightness with an exact finite functional inequality that can be tested and potentially proved. Approach 1 will be checked at the strip-rectangle boundary as an independent fallback.

Brain query before the attempt: `Poisson planar matching uniform tightness uncrossing displacement Holroyd`. Returned general tightness/annulus-curve cards, not a Poisson partner-length bound. These do not imply endpoint tightness; an already-straight segment can have an escaping endpoint without accumulating annulus crossings.


## A. Classification of continuous universal uncrossing costs

**Definition.** A continuous function f:(0,infinity)->R has the universal weak uncrossing property if, for every four distinct planar points in general position whose red-blue segments [r1,b1] and [r2,b2] cross properly,

f(|r1-b2|)+f(|r2-b1|) <= f(|r1-b1|)+f(|r2-b2|).

The strict property replaces <= by <. These are statements about every crossing configuration, not merely configurations typical of a particular infinite matching.

**Theorem.** Such a continuous f has the weak property if and only if f(t)=At+B with A>=0. It has the strict property if and only if it has this form with A>0.

**Proof of necessity.** Fix arbitrary positive a,b,c,d. Put u=(1,0), v_theta=(cos(theta),sin(theta)), for 0<theta<pi, and set

r1=-a u, b1=b u, r2=-c v_theta, b2=d v_theta.

The two old segments intersect properly at the origin, which is in their interiors. The supporting lines are distinct; the four endpoints are distinct, and no three endpoints are collinear: a line containing the two endpoints on one supporting line cannot contain a nonzero endpoint on the other. This remains true even when some arm lengths coincide. Old lengths are a+b and c+d. Swapped lengths are

sqrt(a^2+d^2+2ad cos(theta)),
sqrt(c^2+b^2+2cb cos(theta)).

As theta decreases to zero, these approach a+d and c+b respectively. Applying the weak property for every positive theta and using continuity gives

f(a+d)+f(c+b) <= f(a+b)+f(c+d).                         (A1)

Apply exactly the same argument with b and d interchanged to obtain the reverse inequality. Hence

f(a+d)+f(c+b) = f(a+b)+f(c+d)                         (A2)

for all positive a,b,c,d.

Given x,y>0, take a=b=x/2 and c=d=y/2. Then (A2) yields

2 f((x+y)/2)=f(x)+f(y).                              (A3)

To prove that continuity and (A3) imply affinity without omitting the functional-equation step, fix any 0<x<y. Repeated midpoint subdivision proves, by induction on n, that

f((1-k/2^n)x+(k/2^n)y)=(1-k/2^n)f(x)+(k/2^n)f(y)

for integers 0<=k<=2^n. The base n=0 consists of the endpoints. At level n+1, even k reduce to the preceding level and odd k are the midpoint of their adjacent even neighbours; (A3) gives the formula. Every t in [0,1] is a limit of these dyadic fractions. Continuity therefore gives the formula for all t. Thus f is linear on every compact interval in (0,infinity).

Fix two distinct positive base points x0<y0 and define A=(f(y0)-f(x0))/(y0-x0), B=f(x0)-Ax0. For any z>0, choose a compact positive interval containing x0,y0,z. On that interval the preceding interpolation identity implies that all its secant slopes agree; using the two base points identifies the slope and intercept as A,B. Hence f(z)=Az+B for all positive z.

For a proper crossing, the strict Euclidean length improvement from ATTEMPT.md Section 1 says that the old total length exceeds the swapped total length. If A<0, the cost comparison is reversed, contradicting the weak property. Thus A>=0. For the strict property A=0 also fails since all comparisons are equal, leaving A>0.

**Sufficiency.** When f(t)=At+B, each two-edge comparison cancels the 2B term. The strict Euclidean improvement multiplied by A is weakly positive if A>=0 and strictly positive if A>0. This proves both converses and the theorem.

**Consequence for the missing tightness.** Every continuous radial cost that strictly improves all crossings is exactly linear in length up to a positive scale and an additive constant. Theorem 2 of the original Poisson Matching paper says that every invariant perfect two-colour planar matching has infinite mean edge length. Therefore its expected f-cost is infinite too. In particular the proposed route of combining this universal local uncrossing property with a uniformly bounded expected coercive f-cost cannot work for an almost-perfect family: if such a family existed, Markov's inequality would give uniform displacement tightness, ATTEMPT.md Section 3 would give a perfect limit, and the same expectation bound would force finite mean length, contradicting the source theorem. A detailed direct bound is recorded below after checking it.

This is a no-go theorem for an optimization strategy, not a nonexistence theorem for non-crossing Poisson matching. It does not classify position-dependent costs, objectives involving more than additive edge costs, crossing constraints imposed explicitly, discontinuous costs, or improvements restricted to selected configurations.


## B. Stronger classification: arbitrary continuous displacement costs

The radial assumption can be removed for costs continuous at zero. Let C:R^2->R be continuous. For an oriented red-blue edge use cost C(b-r). Require the universal weak uncrossing inequality

C(b2-r1)+C(b1-r2) <= C(b1-r1)+C(b2-r2)                (B1)

for every proper crossing in general position.

**Theorem.** Property (B1) holds if and only if C(v)=B+h(v), where B is constant and h is continuous, positively homogeneous (h(tv)=t h(v) for t>=0), and subadditive (h(x+y)<=h(x)+h(y)). The strict property holds if and only if, additionally, h(x+y)<h(x)+h(y) whenever x and y are linearly independent. If C is coercive, meaning C(v)->+infinity when |v|->infinity, then there is m>0 with C(v)-C(0)>=m|v| for every v.

**Proof, necessity of positive homogeneity.** Fix a unit vector u and choose unit vectors v_theta tending to u but not parallel to u. Apply (B1) to r1=-a u,b1=b u,r2=-c v_theta,b2=d v_theta, with a,b,c,d>0. Continuity gives precisely (A1) for the ray function f_u(t)=C(tu). Interchanging b,d gives equality. The midpoint and dyadic argument in Section A proves f_u(t)=A_u t+B_u for t>0; the conclusion of affinity in that argument precedes and does not need the scalar sign restriction. By continuity of C at zero, B_u=C(0)=B for every direction. Define h(v)=C(v)-B, including h(0)=0. The ray formula proves h(tv)=t h(v) for t>=0. The coefficient A_u may initially have either sign; no radial symmetry or monotonicity was used.

**Proof, necessity of subadditivity.** For linearly independent x,y and any epsilon>0, put

r1=-x, b1=epsilon x, r2=-epsilon y, b2=y.

The origin is a proper intersection and all endpoints are distinct and in general position. Old edge vectors are (1+epsilon)x and (1+epsilon)y; the swapped vectors are x+y and epsilon(x+y). Substituting C=B+h and using homogeneity, (B1) becomes

(1+epsilon) h(x+y) <= (1+epsilon)(h(x)+h(y)).

Division by the positive 1+epsilon gives subadditivity. For linearly dependent x,y, approximate them by pairs of linearly independent vectors and use continuity of h. Such approximation is possible in R^2 including when one vector is zero; the zero cases also follow directly from h(0)=0. This proves subadditivity everywhere. If (B1) was strict, the same independent-vector configuration proves strict subadditivity for every linearly independent x,y.

**Proof, sufficiency.** Translate an arbitrary proper crossing point to the origin. Write r1=-a u,b1=b u,r2=-c v,b2=d v, where a,b,c,d>0 and u,v are linearly independent unit vectors. The two swapped edge vectors are a u+d v and c v+b u. Subadditivity followed by positive homogeneity gives

h(a u+d v)+h(c v+b u)
 <= a h(u)+d h(v)+c h(v)+b h(u)
 = h((a+b)u)+h((c+d)v).

Adding 2B proves (B1). If h is strictly subadditive on independent vectors, both applications here are strict, giving the strict property. This also proves its asserted converse. No differentiability, symmetry, or positivity of h is needed.

**Proof, coercive growth.** For each unit vector u, if h(u)<=0, then C(tu)=B+t h(u) does not tend to +infinity as t tends to infinity. Coercivity therefore forces h(u)>0 for every unit u. Continuity and compactness of the unit circle give m=min_{|u|=1}h(u)>0. Homogeneity yields h(v)=|v|h(v/|v|)>=m|v| for nonzero v, and the inequality at zero is automatic.

**Corollary: finite-coercive-cost planarity route is impossible.** Let M_n be stationary planar partial matchings on the prescribed independent Poisson input law with unmatched intensity u_n->0. Suppose C satisfies the preceding universal weak uncrossing property, is continuous and coercive, and

sup_n E sum_{r in R_n intersect [0,1)^2, matched} C(M_n(r)-r) <= K < infinity.

The negative part of C is bounded because C=B+h and h>=m|v|>=0. Let lambda_n=1-u_n be the matched red intensity. Then

m E sum_{matched red r in unit square} |M_n(r)-r|
 <= E sum_{matched red r in unit square} (C(M_n(r)-r)-B)
 <= K+|B|.

Consequently the mean matched-length intensities are uniformly bounded by H=(K+|B|)/m. Markov's inequality gives t_n(T)<=H/T. The compactness criterion in ATTEMPT.md Section 3 therefore produces an invariant perfect planar limit.

To verify that this limit has finite mean, rather than only finite-length partners, choose a nonnegative compactly supported continuous f(r), and continuous radial psi:[0,infinity)->[0,1] nonincreasing, equal to one on [0,1] and zero on [2,infinity). Define q_T(v)=|v|psi(|v|/T) for T>=1. The integrand f(r)q_T(b-r) has compact support on the product space. Its integral against eta_n converges along the joint vague subsequence. Its magnitude is bounded by 2T||f||_infinity R_n(supp f), so the Poisson second-moment bound permits passage of expectations. Stationarity and the bound H give E integral f(r)q_T(b-r) eta_n<=H integral f. This bound passes to the limit. As T increases, q_T increases pointwise to |v| because psi is nonincreasing. Monotone convergence yields E integral f(r)|b-r| eta<=H integral f. Stationarity identifies this coefficient as the typical red edge's mean length. Hence that mean is finite, contrary to Theorem 2 of Poisson Matching in d=2.

Thus no such planar nearly perfect family with a uniform expected C-cost can exist. This corollary assumes planarity of the partial matchings: a weak uncrossing cost can have ties, so minimization alone does not force planarity. With the strict property, finite minimizing matchings are automatically planar and the same obstruction applies directly to their proposed uniform cost bound.

**Scope.** This closes the entire continuous, translation-invariant, additive, coercive displacement-cost strategy with universal uncrossing. It does not exclude constructing a planar matching with infinite expected cost, nor minimizing explicitly under non-crossing constraints using a slow cost which itself fails universal uncrossing. The desired tightness requires only a vanishing tail, not any finite first moment.


## C. Balanced-cell construction and a stationary-cocycle obstruction

**Sufficient construction target.** Suppose one can construct, jointly with R,B and invariant under all translations, a countable partition of the plane into bounded convex Borel cells, each with equal finite red and blue counts, and every Poisson point in the interior of its assigned cell. Then a perfect stationary non-crossing matching follows: apply the finite minimum-length bipartite matching rule in each cell. Points in a convex cell's interior have their connecting segment inside that interior. Distinct cell interiors are disjoint, so all edges from distinct cells are disjoint; within a cell finite uncrossing applies. To make the selection translation-equivariant, sort its finite red and blue point lists lexicographically (translation preserves lexicographic order), enumerate bijections, and take the first length minimizer. This is measurable for a measurable random cell partition and commutes with translations. The finitely many points in each bounded cell have equal counts, so every point is matched. Extra randomization of the partition is allowed.

This is a sufficient target, not an equivalence. A given non-crossing matching is not known to admit such a convex-cell partition, especially if infinitely many remote segments accumulate near it.

The simplest implementation would use horizontal strips and partition each into adaptive bounded rectangles with balanced counts. The following excludes that implementation even with arbitrary extra randomness and dependence on all the other strips.

**Proposition (no stationary balanced interval partition).** Let Xi_R,Xi_B be independent homogeneous Poisson point processes on R of the same rate lambda>0. There is no jointly translation-invariant random locally finite, bi-infinite set of cuts C, disjoint from Xi_R union Xi_B, such that every interval between consecutive cuts contains equal red and blue counts. No finite mean interval length or cut intensity is assumed.

**Proof.** Define the signed count S(x) by S(0)=0 and, for x<y,

S(y)-S(x)=Xi_R((x,y])-Xi_B((x,y]).

For x<0 this defines S(x) by the negative signed count on (x,0]. With probability one 0 and any fixed deterministic t are not input points. Since cuts avoid input points, balanced intervals give S(c')=S(c) for consecutive cuts c<c'. Local finiteness ensures finitely many cuts between any two cuts, so all cut values are the same integer K. Let c0=min(C intersect [0,infinity)); bi-infinite, closed locally finite cuts ensure c0 is finite and exists. Then K=S(c0) is a measurable finite random integer: its defining interval contains finitely many input points almost surely. No moment estimate for K is required.

Observe the process from coordinate t: shift all points and cuts by -t, and renormalize the signed count to zero at the new origin. Its signed count is S_t(x)=S(x+t)-S(t). Every shifted cut has value K-S(t). Thus its selected common cut value is K_t=K-S(t). Joint stationarity says K_t has the same distribution as K for each deterministic t. Consequently S(t)=K-K_t.

For any epsilon>0 choose a finite M with P(|K|>M)<epsilon. Such an M exists simply because K is finite almost surely. Then, without assuming any independence,

P(|S(t)|>2M) <= P(|K|>M)+P(|K_t|>M) < 2epsilon

for every t. Hence the signed-count increments are uniformly tight in t.

But for t>0, S(t) is the difference of independent Poisson(lambda t) variables. Its characteristic function after division by sqrt(2 lambda t) is

exp(2 lambda t (cos(z/sqrt(2 lambda t))-1)) -> exp(-z^2/2).

Thus S(t)/sqrt(2 lambda t) converges in distribution to a standard normal variable. For any fixed finite M this implies P(|S(t)|<=2M)->0. Explicitly, for any delta>0, eventually 2M/sqrt(2 lambda t)<delta; the limsup of that probability is at most P(|Z|<=delta) by convergence at the normal continuity points, and this tends to zero as delta decreases to zero. Therefore P(|S(t)|>2M)->1. Taking epsilon=1/8 contradicts the uniform bound below 1/4 above. This proves the proposition.

**Application to strips.** Restrict the planar Poisson processes to a strip of deterministic positive width h, and project onto the horizontal coordinate. The projected processes are independent one-dimensional Poisson processes of rate h: counts in horizontal intervals are exactly counts in their interval-by-strip rectangles, with means h times interval length and independent increments. Projection almost surely has no collisions because finite-window points have continuous coordinates. Cuts of a balanced rectangular partition give exactly the prohibited balanced interval partition. A partition of the whole plane into independent randomly phased horizontal strips of width h does not evade this: the strip containing the origin is unchanged by horizontal translations, and conditional on its independent phase its projected inputs have the same rate-h Poisson laws. The cuts may depend on all other points and extra randomness; stationarity and the marginal signed-count law are the only properties used.

Therefore stationary balanced cells cannot be obtained merely by assembling locally finite bounded rectangles within fixed-width horizontal strips. This agrees with Holroyd's already known impossibility of stationary locally finite strip matchings (Geometric properties, Theorem 3(i), PDF p.3); it does not assert the still stronger impossibility of arbitrary planar strip matchings. Those can in principle have infinitely many long edges through every bounded set, and need not arise from a bounded-cell partition.

**Additional check: colour-blind convex cells cannot balance the inputs.** If a partition is determined only by the uncoloured union of the two intensity-one Poisson processes and auxiliary randomness independent of their colour marks, it cannot almost surely balance every bounded cell. Conditional on the union and auxiliary randomness, the colour marks are independent fair Bernoulli variables. Every nonempty cell contains a finite positive number N of points. If N is odd its probability of being balanced is zero; if N=2m>=2 the probability is binom(2m,m)/2^(2m)<=1/2. The inequality holds at m=1 with equality, and the ratio of the m+1 probability to the m probability is (2m+1)/(2m+2)<1. Infinitely many cells are nonempty, because every cell contains finitely many points while the union has infinitely many points. After a measurable enumeration of these cells using their least point in an exhaustion by bounded squares, the first n balance events involve disjoint sets of independent colour marks, so their joint conditional probability is at most 2^(-n). Let n tend to infinity. The conditional probability that all cells balance is zero, and hence so is the unconditional probability. Thus any successful bounded convex-cell construction must use the colours themselves.

The unresolved part of this approach is a colour-aware stationary convex partition of genuinely two-dimensional geometry, with bounded cells and exact count balance. Neither the strip obstruction nor the colour-blind obstruction excludes that target.


## D. Does a clever finite-minimizer tie rule evade the cost theorem?

No. For a continuous full-displacement cost C, the following are equivalent:

1. C has the universal weak uncrossing property (B1).
2. For every finite pair of equal-sized red and blue point sets in planar general position, there exists at least one non-crossing C-minimum perfect matching.

To prove 1=>2, among the finitely many C-minimum matchings choose one minimizing total Euclidean length. If it crosses, uncross the two edges. Property (B1) says that the cost does not increase. If it decreases, C-minimality is contradicted; if it stays equal, strict Euclidean decrease contradicts the secondary minimum. Thus this tie rule gives a non-crossing optimum. This proof does not require C to be coercive or strictly compatible with uncrossing.

For 2=>1, if (B1) fails at a crossing quadruple, its crossing matching has strictly smaller C-cost than the other perfect matching. These are the only two bijections on these two red and two blue points. Hence the crossing matching is the unique C-minimum, contradicting assertion 2. This proves the equivalence.

Together with Section B, this characterizes exactly the continuous additive displacement costs for which every finite general-position input admits a planar optimizer: they are constant plus continuous sublinear costs. If they are also coercive, they dominate length. Thus a secondary tie rule does not rescue the proposed slowly growing cost strategy.

A concrete convex-cost failure is certified exactly: r1=(-1/2,0), b1=(9/2,0), r2=(-27/10,-18/5), b2=(3/10,2/5). The old crossing is at zero because r2=-9 b2 and b1=-9 r1. Its two squared lengths are 25 and 25. The swapped squared lengths are 4/5 and 324/5, for a total 328/5>50. Therefore the unique squared-length optimum crosses. The endpoints lie on two distinct lines through zero with origin interior to both old segments, so the quadruple is in general position. These rational identities and the strict cost comparison are kernel-checked in UncrossingCostChecks.lean.

## E. Hostile-referee audit and final remaining gap

- The cost theorem quantifies over ALL crossing quadruples. Its proof does not silently assume a particular random matching encounters them. The finite-optimizer equivalence explains exactly when that universal quantifier is necessary.
- The nearly parallel configurations used for the functional equation are general-position configurations for every positive angle; degeneracy occurs only in the limiting step, where continuity is explicitly invoked.
- Both arm orientations are tested. Using only one would give a one-sided Jensen inequality and wrongly suggest that arbitrary convex costs suffice. The reverse orientation forces equality.
- The vector theorem needs continuity at zero. Its proof explicitly uses this to identify a common ray intercept C(0). No extension to singular or discontinuous costs is claimed.
- Sublinear here means subadditive and positively homogeneous, not necessarily symmetric or nonnegative. Nonnegativity and a strictly positive uniform directional lower bound are deduced ONLY after assuming coercivity.
- The finite-cost obstruction is not inferred merely from the possibility of infinite expected length. The full proof passes a uniform mean bound through a compactly supported displacement cutoff and monotone convergence, obtaining the actual contradiction to source Theorem 2.
- The convex-cell route requires all points in cell interiors and a measurable stationary cell partition. An arbitrary planar matching is not assumed to yield such a partition.
- The strip theorem assumes a locally finite bi-infinite cut set avoiding input points, and neither finite cut intensity nor any moments of interval size. Its stationary difference bound uses a union bound, never independence of K and K_t. The normal-limit contradiction is justified for shrinking thresholds.
- The strip conclusion is expressly restricted to bounded-cell rectangle constructions. It is not a theorem excluding arbitrary planar strip matchings.
- The colour-blind obstruction conditions on all uncoloured geometric data and independent auxiliary randomness; after that conditioning, the colours really are independent. A colour-aware partition cannot be treated this way.
- Numerical cost_probe.json has ten finite comparisons: linear cost decreases in both orientations; sqrt, log(1+t), and t^0.9 fail in one orientation; squared length fails in the other. These support the exact proof but are not substituted for it.
- second_lean_check.log records exit 0 with no diagnostics. Lean checks the four-arm inequality-to-midpoint identity and exact squared-distance counterexample. It does not check the continuous functional equation, stochastic compactness, cocycle proof, or F0082 itself.

**Remaining gap after this attempt.** The original planar Poisson perfect-matching question is still unresolved here. A uniformly tight stationary non-crossing nearly perfect family is still missing. Continuous coercive additive displacement objectives with automatic finite planarity cannot provide a finite expected-cost bound, because they necessarily grow at least linearly. A different viable construction might use explicit non-crossing constraints with a slower cost, an infinite-mean construction with tail control, or a colour-aware stationary balanced convex-cell partition not confined to fixed-width strips. None of these has been constructed or excluded. No conjectural step is labelled proved, and no novelty claim is made for the strategy-obstruction results.
