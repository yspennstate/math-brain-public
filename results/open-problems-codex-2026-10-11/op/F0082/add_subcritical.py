from pathlib import Path
p=Path('ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write(r'''

## 7. Subcritical-cost route and its specific obstruction

Theorem 7(ii) of Holroyd–Janson–Wästlund (2022; arXiv PDF p.8) provides invariant perfect gamma-minimal matchings for each gamma<1 in dimension two. It does not state planarity. Section 5 gives a gamma=1/2 finite counterexample to the implication from gamma-minimality to planarity.

There is nonetheless the following conditional route. Choose gamma_n=1-1/(n+1) and an invariant perfect gamma_n-minimal matching for each n. If their matched-displacement intensities are uniformly tight, a subsequence converges to an invariant perfect 1-minimal matching, hence to a non-crossing matching.

Proof: repeat the compactness, endpoint-degree and perfectness arguments of Section 3; none of those arguments used non-crossing. Fix finitely many edges of the perfect limit and a permutation of their blue endpoints. Using disjoint isolating balls, each limit edge has a corresponding edge of all sufficiently late approximants, with endpoints converging to the limit endpoints. The gamma_n-minimal inequality for these edges holds against the chosen permutation. All pair distances converge to positive finite numbers, since red and blue Poisson points are distinct. Joint continuity of (x,gamma) -> x^gamma for x>0 lets us pass to the limit and gives the sum-of-lengths minimal inequality. This reasoning is pathwise for every finite collection of limit edges and every permutation. Thus the limit is 1-minimal, and Section 1 excludes crossings. Uniform tightness has not been proved.

A generic uniform quasistability bound as gamma approaches 1 cannot fix this gap. In the sense of Proposition 28 of the same paper, there is no finite constant kappa valid for all finite gamma-minimal configurations and all gamma in (0,1). Here is a proof. Given any kappa, choose L>kappa+1 and L>2. On the line put red points 0,L and blue points -L,1. Matching 0 to -L and L to 1 has cost L^gamma+(L-1)^gamma; the only other perfect matching has cost 1+(2L)^gamma. At gamma=1 the first cost is 2L-1, strictly below 2L+1. By continuity in gamma, it remains strictly smaller for some gamma<1 sufficiently close to 1 and positive. Hence it is the unique gamma-minimal perfect matching of this configuration (and its finite submatchings have no possible improvements). The opposite-colour points 0 and 1 are distance 1 apart, but the minimum of their partner distances is L-1>kappa. This contradicts any uniform inequality min(|x-M(x)|,|y-M(y)|)<=kappa|x-y|.

This is a finite, collinear example about deterministic quasistability constants. It does not refute tightness for random planar Poisson inputs. Because the cost inequality is strict, small perturbations of the four points into general position in R^2 retain both the unique optimum and the failure of any proposed fixed kappa, if L was chosen with a margin. Thus excluding collinear configurations does not remove this generic obstruction.
''')
