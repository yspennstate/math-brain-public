from pathlib import Path
p=Path('.')
p.joinpath('ATTEMPT.md').write_text(r'''# F0082 research attempt — 2026-10-11

## Exact question and scope

Let R and B be independent homogeneous Poisson point processes of intensity 1 on R^2. Does there exist a random perfect bipartite matching M, with the joint law (R,B,M) invariant under every translation of R^2, such that its straight closed edge segments are pairwise disjoint almost surely? Extra randomness is allowed; being a factor is not required. No moment bound and no local finiteness of the set of segments is required.

The source's Open Problems (ii), PDF p.34, states precisely this question, with the matching definitions and intensity assumptions in its introduction. I have not proved an answer to this question. The results below are partial constructions, an equivalence/reduction, and counterexamples to proposed shortcuts. They are not claimed to be new literature results.

## 1. Finite geometric uncrossing

Let two matched edges [r1,b1], [r2,b2] cross properly at x, with no three of their four endpoints collinear. Replace them with [r1,b2], [r2,b1]. This preserves bipartiteness, vertex degrees and the set of matched vertices. Since x lies in the interiors of the old edges,

|r1-b1|=|r1-x|+|x-b1|,   |r2-b2|=|r2-x|+|x-b2|.

Strict triangle inequalities give

|r1-b2| < |r1-x|+|x-b2|,   |r2-b1| < |r2-x|+|x-b1|.

For example, equality in the first inequality would put r1,x,b2 on a line, so the two crossing supporting lines would coincide, contrary to a proper crossing. Summing gives a strict decrease in total length. Consequently any minimum-total-length matching among maximum-cardinality matchings of finite red and blue sets in general position has disjoint edge segments. Distinct edges have no shared endpoints; an intersection that is not proper would entail three collinear endpoints, excluded by general position.

Such a minimum exists: there are only finitely many matchings. Maximum cardinality is min(number of red, number of blue), since the allowed bipartite graph is complete. Repeatedly uncrossing an arbitrary finite matching also terminates because there are finitely many matchings on its matched vertices and every move strictly reduces length. This argument does not supply an infinite-volume Lyapunov function.

For the Poisson processes, all points are distinct and no three points are collinear almost surely. To see this, in each bounded square condition on the two finite point counts. Their locations have a joint Lebesgue density. Every particular pair is distinct almost surely, and conditional on a pair of distinct points, a third lies on their line with probability zero. A finite union over pairs/triples and a countable union over squares proves the assertion for all points.

## 2. Stationary nearly perfect planar partial matchings

**Proposition.** For each L>0 there is a translation-invariant non-crossing partial red-blue matching whose total unmatched intensity is

u_L = E|X-Y|/L^2 <= sqrt(2)/L,

where X,Y are independent Poisson(L^2). Each colour's unmatched intensity is u_L=nu_L/2 <= 1/(sqrt(2)L). Furthermore nu_L is asymptotic to 2/(sqrt(pi)L) as L tends to infinity.

**Construction and full proof.** Independently of R,B take U uniform on [0,L)^2. Partition the plane into half-open squares U+Lk+[0,L)^2, k in Z^2. In each square select a maximum-cardinality red-blue matching minimizing total Euclidean length. For ties use lexicographic order on the lists of endpoints expressed relative to the square's lower corner. This is a measurable selection: on every fixed pair of finite counts there are finitely many candidates, their costs are continuous in the endpoint coordinates, and lexicographic comparisons are Borel. Sorting finite point coordinates is also measurable. All points avoid the grid boundaries almost surely by conditioning on U.

Each square's edges are non-crossing by Section 1. They lie in the square's interior: a convex combination of interior points of a square is still interior. Thus edges from different squares are disjoint. The selection commutes with translation of the points and their square. For a deterministic translation t, U+t reduced modulo L is again uniform on [0,L)^2 and independent of the translated Poisson inputs; reindexing squares gives the same rule. Therefore the entire joint law is translation-invariant.

If a square contains X red and Y blue points, it leaves (X-Y)_+ red and (Y-X)_+ blue unmatched, or |X-Y| in total. The expected intensity is the expected number per fundamental square divided by L^2. Here is a direct justification avoiding the use of a random cell as a fixed observation window. Construct first the rule on the unshifted grid. Its expected unmatched counting measure is LZ^2-periodic, and its expected mass in one fundamental cell is E|X-Y|. Average its translates by U over that cell. The resulting measure is translation-invariant; Fubini and tiling show that its mass in any rectangle is its area times E|X-Y|/L^2. Equivalently, test a compactly supported function f, integrate the periodic measure against f(x+U), and sum the translated cell integrals: the answer is E|X-Y|/L^2 times integral f. The same proof applies to each colour. Symmetry of X,Y gives equal expected unmatched counts, independently of the matching tie rule.

Since E(X-Y)=0 and E(X-Y)^2=2L^2, Cauchy-Schwarz gives E|X-Y|<=sqrt(2)L. This proves the bounds. For the asymptotic, the characteristic function of (X-Y)/L is exp(2L^2(cos(t/L)-1)), converging to exp(-t^2). Thus (X-Y)/L converges in distribution to a centred normal variable Z of variance 2. These variables have second moments 2, which makes their absolute values uniformly integrable: E[|W|1{|W|>K}]<=E W^2/K=2/K. Hence E|X-Y|/L tends to E|Z|=2/sqrt(pi), proving the claimed asymptotic.

**What this does not prove.** A typical point's partner in these matchings might escape to infinity as L grows. The unmatched-intensity estimate bounds only points left unmatched at each finite scale. It says nothing uniform about matched edge lengths. Matching the remaining points later can create crossings with the existing segments, so simply iterating the construction is not justified.

## 3. Exact tightness reduction

For a stationary partial matching M_n on the prescribed Poisson input law, let u_n be its unmatched red intensity, and define

t_n(T) = E sum_{r in R_n intersect [0,1)^2} 1{r is matched and |M_n(r)-r|>T}.

The expected red endpoint measure has intensity 1; t_n is an intensity, not a tail conditional on being matched. Write the blue analogue similarly. They are equal: the marked edge process with displacement b-r has the same red and blue marginal intensity for each translation-invariant displacement class. In detail its expected measure in coordinates (r,v=b-r) has the form dr times a finite measure rho_n(dv), by stationarity and uniqueness of locally finite translation-invariant measures on R^2. Pushing (r,v) to r+v gives the same coefficient rho_n for blue endpoints. Restrict to |v|>T for the equality of the tails, or use all v for equality of unmatched intensities.

**Proposition (criterion).** The original question has a positive answer if and only if there exists a sequence of stationary non-crossing partial matchings of the given Poisson processes such that

u_n -> 0,   lim_{T->infinity} sup_n t_n(T)=0.

No bound on E edge length is needed. For the grid construction of Section 2, establishing this condition would give a solution, but the criterion does not assert that the grid construction meets it.

**Full proof of sufficiency.** Encode a matching by the counting measure eta_n=sum_{(r,b) in M_n} delta_(r,b) on R^2 x R^2. Consider the joint random measures (R_n,B_n,eta_n) with the vague topologies. The underlying spaces are locally compact second countable, and their spaces of Radon measures are metrizable Polish spaces. On any compact product K x K', eta_n(K x K')<=R_n(K). The Poisson laws of the latter counts are fixed and tight. Applying these bounds to a compact exhaustion gives tightness of eta_n: choose increasing count bounds on the exhaustion with summable probabilities of violation; measures satisfying all these bounds form a relatively compact set for vague convergence (on each compact, finite measures with bounded mass have subsequential weak limits; a diagonal argument gives a Radon limit). Slightly enlarge the compacts if needed to use continuous cutoff bounds, which produce closed compact constraints. The same bounds apply to the point measures. Thus Prokhorov yields a subsequence with joint weak limit (R,B,eta). Skorokhod representation permits joint almost-sure vague convergence along this subsequence. The marginal law of R,B remains exactly that of the independent Poisson processes, since it was the same for every n.

On the event that R,B are simple and locally finite, eta is the counting measure of a partial matching on these points. Here are the local details. Each bounded region contains finitely many limit points, separated by disjoint small balls with point-free boundaries. Vague convergence of the integer-valued point measures implies that sufficiently late each such ball contains exactly one point of the corresponding colour, and all other points in a smaller compact set are accounted for. Endpoint support of eta follows as well: an endpoint neighbourhood containing no corresponding limit points contains no corresponding late points. For each pair of red and blue isolation balls, at most one edge can occur, and it converges, when present, to the isolated pair. Since each red isolation ball contains only one red point, it cannot support edges to two disjoint blue isolation balls; similarly for blue points. Varying through a countable exhaustion proves that eta has atoms of mass 1 only at allowable pairs and degrees at most 1. An atom can be lost to infinity; no assertion of perfectness has yet been made.

The limiting partial matching is non-crossing. If two limiting edges crossed properly, each would have late approximating edges with endpoints in their isolation balls, and proper crossing is an open condition on four noncollinear endpoints. These late edges would cross, a contradiction. All other possible intersections of distinct edges would require three collinear Poisson points or repeated endpoints, already excluded. Translation of all three measures is continuous for the vague topology. Hence the invariant joint laws have an invariant weak limit.

It remains to rule out missing partners; this is exactly where the tightness assumption is used. Take any nonnegative continuous compactly supported f on R^2. Choose a continuous radial cutoff g_T on displacement vectors, equal to 1 on the ball of radius T, between 0 and 1, and zero outside the ball of radius T+1. Stationarity of marked endpoint intensities gives

E integral f(r)g_T(b-r) eta_n(dr,db)
  >= (1-u_n-t_n(T)) integral f(r)dr.

The integrand is continuous and compactly supported on the product space, so its integral converges almost surely in the Skorokhod representation. Its absolute value is bounded by ||f||_infinity R_n(supp f), and these Poisson counts have uniformly bounded second moments. Therefore the integrals are uniformly integrable and their expectations converge. Letting n tend along the subsequence gives

E integral f(r)g_T(b-r) eta(dr,db)
  >= (1-sup_n t_n(T)) integral f.

The left side is at most E sum_{matched red r} f(r), which is at most E integral f dR=integral f. Let T tend to infinity in the lower bound; uniform tightness forces equality of the two endpoint intensities. Thus the nonnegative random variable sum_{unmatched red r}f(r) has expectation zero and is zero almost surely. Use a countable collection of such f positive on an exhaustion of the plane to conclude that every red point is matched. The analogous argument applies to blue using the equality of the tails and unmatched intensities established above. This proves perfectness and sufficiency.

**Necessity.** Given a perfect invariant non-crossing matching, take M_n=M for every n. Then u_n=0. In the unit square there are finitely many red points almost surely and every partner is at finite distance. The sum of indicators for distances exceeding T decreases to zero and is dominated by the integrable Poisson count in the square. Dominated convergence gives t_n(T)->0, uniformly in this constant sequence. This proves necessity.

This is an equivalence with a compactness condition, not a proof that such a sequence exists. The fixed Poisson marginals and proper-crossing exclusion are essential parts of the sufficiency proof.

## 4. Counterexample to omission of tightness (different input law)

The following is an example about the topology of matchings, not a counterexample to F0082. Let alpha=sqrt(2), U uniform on [0,1)^2, R=U+Z^2 and B=U+Z^2+(1/2,alpha). Match U+(i,j) to U+(i+n+1/2,j+alpha) for each integer n>=1. Each matching is perfect and stationary under every real translation: translating U modulo Z^2 preserves its uniform law and reindexes both lattices.

Every edge has direction v_n=(n+1/2,alpha). Supporting lines of distinct edges are distinct parallel lines. Indeed coincident lines would require an integer displacement (k,l) parallel to v_n, or l(n+1/2)=k alpha. If k is nonzero this equates a rational with a nonzero irrational. If k=0 it forces l=0. Thus distinct edges are disjoint. The displacement lengths tend to infinity. On every compact subset of R^2 x R^2, eta_n is eventually zero because both endpoints in a compact set would bound their displacement length. Therefore eta_n converges vaguely to the empty edge measure, despite perfectness, stationarity and non-crossing at every n. The inputs here are dependent lattices rather than independent Poisson processes; this example disproves only a general compactness shortcut.

## 5. Counterexample to bounded-cost uncrossing

Take r1=(-1/10,0), b1=(1/10,0), r2=(0,-10), b2=(0,10). The matching (r1,b1),(r2,b2) has a proper crossing at the origin and lengths 1/5,20. The other matching has both lengths sqrt(10001/100)>1. For c(l)=min(l,1), the crossing matching costs 6/5, whereas the uncrossed matching costs 2. These are the only two perfect bipartite matchings, so the unique capped-cost minimizer crosses. In ordinary length the uncrossed cost is strictly smaller: 2 sqrt(10001/100)<101/5 since their positive squares are 10001/25<10201/25. Therefore replacing unbounded length by a bounded cost to obtain a compact optimization problem loses the automatic non-crossing property.

For the concave cost c(l)=sqrt(l), the crossing cost is sqrt(1/5)+sqrt(20)<5, while the uncrossed cost is 2(10001/100)^(1/4)>2 sqrt(10)>6. To verify the first strict inequality: its square is 1/5+20+2 sqrt(4)=121/5<25. Thus even power-cost minimality at gamma=1/2 cannot generally guarantee non-crossing. This explains why the higher-dimensional existence theorem for gamma<1 is not an answer to the original question.

## 6. Checks and remaining gap

The reproducible script experiments.py uses seed 82011, independent Poisson counts and uniform locations in a square, and SciPy's rectangular linear_sum_assignment with Euclidean costs. It records counts, tails, quantiles, unmatched intensity and all proper-crossing checks in the first two samples per size, in experiments.json. This is numerical evidence only; floating-point optimization is not used as a proof. Grid-boundary independence and translation randomization are mathematical, not simulated. Finite-size tail observations cannot establish or refute uniform tightness. A sample unmatched intensity can exceed the analytic expected-intensity bound because that bound is not a samplewise assertion.

FiniteChecks.lean checks only the conditional algebraic summation step of uncrossing and rational squared-distance/cost certificates for Section 5. It does not formalize Poisson processes, Euclidean geometry, compactness, or any solution to F0082. It uses ordinary kernel-checked tactics, no native_decide and no sorry. Execution result is recorded separately in lean_check.log.

Hostile-referee checks: (1) uncrossing preserves matched vertices even with unequal counts; (2) all squares are convex and edges stay in interiors; (3) random phase, rather than a fixed grid, supplies full invariance; (4) general position eliminates nongeneric intersections in the limit; (5) endpoint degrees can be lost under vague limits, so tightness is explicitly required; (6) the expectation limit uses uniform integrability from Poisson counts, not only convergence in distribution; (7) equality of red/blue endpoint intensities holds for each displacement class; (8) the lattice example is explicitly outside the Poisson hypotheses; (9) finite optimizer means or moment divergence do not decide tightness; (10) the capped and gamma=1/2 examples exclude treating later sublinear-cost existence as a planar theorem.

Remaining gap, precisely: construct any stationary non-crossing partial matchings on the independent intensity-one planar Poisson inputs with unmatched intensity tending to zero AND uniformly tight matched-displacement intensity. Section 2 supplies the first property but neither a proof nor a disproof of the second. Alternatively one needs a different direct perfect planar construction or an impossibility theorem applying to all randomized stationary matchings. No such construction or impossibility theorem has been obtained here.
''',encoding='utf8')
p.joinpath('STATUS.md').write_text('STATE: WORKING\nNEXT: Finish citation audit, numerical and Lean checks; referee the tightness reduction.\nVERDICT: PARTIAL\n2026-10-11: Confirmed source; proved stationary nearly perfect planar partial matching with unmatched intensity <= sqrt(2)/L, and recorded the precise tightness criterion and counterexamples to shortcuts in ATTEMPT.md.\n',encoding='utf8')
