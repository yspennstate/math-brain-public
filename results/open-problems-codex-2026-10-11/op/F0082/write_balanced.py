from pathlib import Path
p=Path('SECOND_ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write(r'''

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
''')
