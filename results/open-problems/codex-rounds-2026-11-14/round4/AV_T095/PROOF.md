# The rare-fast crossing input

The result checked here is Lemma `df:cr:rare-fast` in OpenAI, *Strict convexity and differentiability of the planar exponential first-passage limit shape* (September 24, 2026), revision `4eaee87548250b2682affda7d05d947c05554bae`. Sources: [crossings](source-crossings.tex) and [preliminaries](source-preliminaries.tex). The argument below verifies this input and its local-travel prerequisites from the stated uniform shape theorem and elementary Gamma moments. It does not verify the remaining differentiability argument or the strict-convexity argument.

## Statement and hypotheses

Fix iid Gamma(shape κ, rate λ) weights on the unoriented nearest-neighbor edges of Z², with κ,λ>0. Let T be passage time and μ its deterministic norm. The probabilistic input used throughout is

\[
 \sup_{z\in\mathbb Z^2:|z|\ge L}
 \frac{|T(0,z)-\mu(z)|}{|z|}\longrightarrow0
 \quad\text{almost surely as }L\to\infty.                 \tag{1}
\]

Write α|z|≤μ(z)≤β|z| with α,β>0. Fix b∈[−1,1], u=(1,b), x(z)=z₁, r(z)=z₂−bz₁ and m₀=μ(u). Let a₊ and a₋ be the right and left derivatives at zero of h↦μ(u+he₂). Define

\[
 f_\sigma(z)=m_0x(z)+a_\sigma r(z),\qquad
 H_\sigma(P)=\tau(P)-f_\sigma(\Delta P).
\]

For fixed A,R,ε>0 and σ∈{−,+}, the probability that there is a path from column 0 to column n, contained in

\[
 -An\le x\le(1+A)n,\qquad |r|\le Rs,
\]

with Hσ(P)<−εs tends to zero jointly as s→∞ and n/s→∞. Here s is real, n is a positive integer, endpoints are unrestricted within the columns, and all traversals contribute to path cost.

## 1. Supports and local connections

Convexity of g(h)=μ(u+he₂) implies that both one-sided derivatives are subgradients at zero. For x(z)>0, homogeneity therefore gives fσ(z)≤μ(z). If the inequality failed at any other z, a sufficiently small convex combination w=(1−t)u+tz would have x(w)>0 and μ(w)≤(1−t)μ(u)+tμ(z)<fσ(w), a contradiction. Thus fσ≤μ everywhere. The defining derivatives give

\[
 0\le\mu(u+he_2)-f_\sigma(u+he_2)=o(|h|)
 \quad(h\to0,\ \sigma h>0).                            \tag{2}
\]

No equality a₊=a₋ is assumed.

For completeness, (1) implies, for fixed C,δ>0,

\[
 s^{-1}\max_{|z|\le Cs}|T(0,z)-\mu(z)|\to0,
 \qquad
 \mathbb P\{\inf_{|z|\ge\delta s/3}T(0,z)
                       \ge\alpha\delta s/6\}\to1.       \tag{3}
\]

For the first assertion, separate finitely many points in a fixed ball from the uniform relative error outside it. For the second, use relative error at most α/2. Translation invariance gives identical probability bounds at every deterministic origin.

Fix D,η,δ>0 and deterministic p,q with |q−p|≤Ds. Divide [p,q] into B equal pieces and round the division points to lattice vertices, retaining p,q. Choose B fixed with βD/B<αδ/24. The norm of each rounded increment is μ(q−p)/B+O(1), uniformly in p,q. Apply (3) at the B starting vertices, with an error per piece smaller than both ηs/(2B) and αδs/24 after absorbing rounding. With probability tending to one, each piece has passage time below αδs/12, while exiting the ball of radius δs/3 about its start costs at least αδs/6. Choose a path within 1 of its passage-time infimum. For sufficiently large s its cost is below that escape threshold, so nonnegativity prevents exit. Concatenation costs at most μ(q−p)+ηs/2+B≤μ(q−p)+ηs and stays within δs of [p,q]. The number of origins is fixed, so the probability bound is uniform in the deterministic endpoints. No event simultaneous over all origins is needed.

To allow endpoints selected after observing the weights, take two deterministic vertical intervals of union diameter at most Ds. Choose γ>0 with

\[
 (4\kappa/\lambda+2\beta)\gamma\le\eta/2,
 \qquad \gamma\le\delta/2.
\]

Put nets in both intervals including the extreme lattice vertices, with gaps at most floor(γs). There are at most 2D/γ+2 net vertices in each interval for large s. The sum V of any gap's weights uses at most γs distinct edges. Direct integration of the Gamma density gives E exp(λτ/2)=2^κ. Exponential Markov therefore gives

\[
 \mathbb P\{V>2\kappa\gamma s/\lambda\}
 \le e^{-\kappa\gamma s}2^{\kappa\gamma s}
 =e^{-\kappa(1-\log2)\gamma s}.                         \tag{4}
\]

There are boundedly many gaps and net pairs. Apply the preceding local-travel result to all net pairs with errors η/2,δ/2. On their common event, attach any endpoints p,q vertically to their assigned net vertices. The two attachments cost at most 4κγs/λ; the change in μ between the two endpoint displacements is at most 2βγs. Their total error is at most ηs. Corresponding straight segments are at Hausdorff distance at most γs, so the tube and attachments stay within δs of [p,q]. This proves the interval-travel input, uniformly over deterministic interval locations and lattice phases.

## 2. The oriented-path lemma, with an explicit density

Suppose events Gv, v∈Z², are jointly independent on every finite set of sites with pairwise sup distance greater than an integer k≥0. Set

\[
 q=(2k+1)^2,\qquad \zeta=2^{-48q}.                     \tag{5}
\]

If P(Gvᶜ)≤ζ at every site, there is a positive probability of an infinite path of good sites from 0 using steps (1,0),(0,1). Neither stationarity nor independence of adjacent tests is required.

To prove this, let S be the endpoints of finite oriented paths from 0 whose sites except possibly the terminal one are good. Then 0∈S. If S were infinite, the tree of such paths, with at most two children per node, would have arbitrarily large depth and an infinite branch. Every site on that branch is nonterminal on a longer prefix and hence good. Thus absence of an infinite good path implies S finite.

Orient the boundaries of the squares centered at sites of S counterclockwise and cancel shared sides. The remaining finite directed graph is balanced at each vertex. Following unused edges until returning to a start, and repeating, decomposes it into closed directed trails without repeated edges. Their winding numbers about 0 sum to 1: this is true for the original squares, and cancellation preserves it. At least one trail has nonzero winding. It has length m≥4, with S on its left along every edge, including at corner contacts.

A closed lattice trail has equally many east and west steps, and equally many north and south steps. Exactly m/2 steps are north or west. Across a north step, the right square is the east neighbor of the left one; across a west step, it is the north neighbor. The left site's membership in S supplies a path reaching it. If it were good, its forward neighbor would also be in S, contrary to that boundary edge. Those left sites are therefore bad. A site has at most four incident boundary edges, so the trail forces at least m/8 distinct bad sites.

Greedily choose such sites separated by sup distance greater than k. Each choice removes at most q candidates, so at least m/(8q) sites are selected. For a fixed candidate trail the sites are deterministic. Independence bounds the probability of its forced badness by ζ^{m/(8q)}.

Nonzero winding puts 0 inside the coordinate bounding box. Coordinate spans are at most m, so each dual-lattice starting vertex has coordinates in [−m,m]. There are at most (2m+3)²≤9(m+1)² possibilities, even using this loose count, followed by at most 4^m step sequences. Union bounding gives

\[
 \mathbb P(\text{no infinite good path})
 \le 9\sum_{m\ge4}(m+1)^2
              [4\zeta^{1/(8q)}]^m
 =9\sum_{m\ge4}(m+1)^2\,16^{-m}<1.                    \tag{6}
\]

One independent upper bound is (m+1)²≤4^{m−1} for m≥4: check m=4, then the ratio is at most (6/5)²<4. Hence the last sum is at most

\[
 \frac94\sum_{m\ge4}4^{-m}=\frac3{256}<1.
\]

Alternatively, its exact value is obtained by subtracting the terms m=0,1,2,3 from (1+a)/(1−a)³ at a=1/16, then multiplying by 9. Both checks are implemented in audit.py. The threshold (5) is merely sufficient.

## 3. Trial amplification and a fixed dependence radius

Suppose contrary to the claimed joint limit that a sequence s→∞, n/s→∞ has crossing probability at least p₀>0. Choose

\[
 k=\lceil4(A+3)+8\rceil+1,
\]

then ζ from (5), then a fixed positive integer M with (1−p₀)^M<ζ/2. This also permits p₀=1, when M=1 suffices. Put

\[
 S_0=100M(R+1)\lceil s\rceil,
 \quad C_0=200M(R+1),\quad d=\lceil D_0s\rceil.
\]

The fixed constant D₀ will be chosen only after M. For an auxiliary site v=(v₁,v₂), set

\[
 i=v_1+v_2,\quad X_i=i(n+d),\quad
 Y_v=\sigma(i+v_2)S_0.
\]

Each oriented step increases i by 1 and moves Y by σS₀ or 2σS₀. At v place M exact lattice translates of the alleged fast-crossing event with translation vectors

\[
 t_{v,j}=\left(X_i,
 \left\lfloor bX_i+Y_v+(2j-M-1)3(R+1)\lceil s\rceil
                                      +\tfrac12\right\rfloor\right),
 \quad 1\le j\le M.                                   \tag{7}
\]

The r-coordinate of each translated center differs from its intended center by at most 1/2. Consecutive intended centers differ by 6(R+1)ceil(s), so actual centers are separated by at least that quantity minus 1, strictly larger than 2Rs for s≥1. All strips lie in |r−Yv|≤S₀/4: indeed their extreme displacement is bounded by

\[
 3(M-1)(R+1)\lceil s\rceil+\tfrac12+Rs
 <25M(R+1)\lceil s\rceil.
\]

These trials use disjoint vertex sets and thus disjoint internal edge sets. Exact lattice translation preserves displacements, costs in law, and Hσ; it does not require the strip centers to agree with their unrounded intended locations. The probability all M fail is at most (1−p₀)^M.

## 4. Connectors for all endpoints

For either forward neighbor v′, connect the entire interval

\[
 x=X_i+n,\ |r-Y_v|\le S_0/4
\]

to the entire interval

\[
 x=X_{i+1},\ |r-Y_{v'}|\le S_0/4.
\]

A connector displacement z satisfies x(z)=d and

\[
 S_0/2\le\sigma r(z)\le5S_0/2\le3S_0.
\]

Since S₀/s≤C₀ for s≥1, (2) supplies h₀>0 such that

\[
 0\le\mu(u+he_2)-f_\sigma(u+he_2)
 \le\frac{\varepsilon}{12C_0}|h|
 \quad(0<\sigma h\le h_0).
\]

Choose fixed D₀≥1 with 3C₀/D₀≤h₀. Then h=r(z)/d is on the required side, |h|≤h₀, and homogeneity gives

\[
 \mu(z)-f_\sigma(z)
 \le\frac{\varepsilon}{12C_0}|r(z)|\le\varepsilon s/4.
\]

The union of the two endpoint intervals has diameter at most Ds for a fixed D depending on M,R,D₀,b. Their joining segments satisfy |r−Yv|≤9S₀/4. Choose a fixed δ≤1/2; the δs tubes fit in

\[
 X_i+n-s\le x\le X_{i+1}+s,
 \qquad |r-Y_v|\le4S_0,                               \tag{8}
\]

because r has Euclidean Lipschitz constant sqrt(1+b²)≤sqrt(2), and the transverse margin is 7S₀/4. Interval travel with error εs/4 now supplies, with probability 1−o(1), connections for every endpoint pair at once. Each costs at most fσ(z)+εs/2. Define the test using existence of paths only on the internal edges of (8); the interval-travel event implies this measurable, finite-region test. The failure probability is uniform in v, including lattice phase. Neither independence from the trials nor a success rate for an adaptively chosen pair is needed.

Call v good if some trial succeeds and both connector tests pass. A union bound gives P(v bad)≤(1−p₀)^M+o(1)≤ζ eventually.

For sufficiently large sequence index, n≥d+s, since d=O(s) with fixed D₀. The entire test at v is supported within

\[
 |x-X_i|\le(A+3)n,\qquad |r-Y_v|\le4S_0.             \tag{9}
\]

If two such regions share a vertex, write j=i+v₂ and obtain

\[
 |\Delta i|\le\frac{2(A+3)n}{n+d}\le2(A+3),
 \qquad |\Delta j|\le8.
\]

Inverting the coordinates, v₂=j−i and v₁=2i−j, gives

\[
 |\Delta v_2|\le2(A+3)+8,
 \qquad |\Delta v_1|\le4(A+3)+8<k.
\]

Consequently tests at pairwise sup distance greater than k use disjoint edge sets and are jointly independent. Both S₀ factors cancel in the transverse comparison; n+d≥n gives the longitudinal bound. Thus k is independent of M and D₀. The order of choices is k,ζ,M,D₀, then a sufficiently large member of the sequence, and contains no circular dependency.

## 5. Contradiction at one fixed scale

Fix that sufficiently large member. Section 2 gives a positive probability of an infinite oriented path of good sites from 0. At each visited site choose a successful trial, and connect it to the chosen trial at the next site using Section 4. Arbitrary endpoints are permitted on a single connector-test event. Prepend a vertical path from the lattice origin to the first trial's starting vertex; it has a finite random defect C because all weights are finite almost surely. Its displacement is bounded at this fixed scale, although C need not have a deterministic upper bound.

Let zt be the endpoint of the trial at the t-th site, numbered from zero. Additivity yields

\[
 T(0,z_t)-f_\sigma(z_t)
 \le C-(t+1)\varepsilon s+t\varepsilon s/2.             \tag{10}
\]

Retraced edges cause no problem: the constructed walk's cost counts multiplicities and still bounds T from above.

Along an oriented path, i=t and 0≤v₂≤t. Consequently

\[
 x(z_t)=t(n+d)+n,\qquad |r(z_t)|\le2tS_0+S_0/4.
\]

Thus |zt|→∞ and |zt|≤C′(t+1) for a deterministic constant C′ at this fixed scale, using |b|≤1. On the probability-one event (1), the uniform estimate applies even to these environment-dependent endpoints:

\[
 T(0,z_t)\ge\mu(z_t)-o(t)\ge f_\sigma(z_t)-o(t).
\]

This contradicts (10), whose negative linear coefficient is −εs/2. The positive-probability infinite-path event must intersect the probability-one shape event, so the contradiction excludes the supposed sequence. The original joint limit follows. Exact lattice translates of its event have exactly the same probability.

## Checks of possible exceptions

The proof fixes the scale before taking t→∞; interchanging those limits would lose the linear contradiction. The origins in local travel are deterministic, whereas the final endpoints are random and use the uniform assertion (1) from the fixed origin. The connector drift is always to the side matching σ, which is essential for (2). The two trials at neighboring auxiliary sites can overlap; only separated tests and trials within a single site require independence. No global simultaneous success of all connectors is asserted. Rounding in (7) works also for negative x,b,Y and half-integer ties. Gamma shapes below 1 are allowed because (4) depends on a moment integral, not boundedness of the density at zero. No hypothesis that the limit shape already has a corner is used here.

The new conclusion discharges the two crossing inputs of the earlier characteristic-length reduction, subject to (1) for the fixed Gamma law. It supplies no new change of measure for other continuous laws and no completed verification of the full manuscript. The next unexamined step in the differentiability chain is the transverse-witness argument and its interface with the endpoint estimates.
