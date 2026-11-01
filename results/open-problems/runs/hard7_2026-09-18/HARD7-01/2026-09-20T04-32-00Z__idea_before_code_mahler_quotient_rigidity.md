Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# Idea before code — exact antipodal quotient for Mahler shadow rigidity

Current canonical target remains `operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`: for every origin-symmetric convex body `K=-K subset R^n`, prove `|K||K^circ| >= 4^n/n!`. Frozen source metric remains `d_sym=3`; this checkpoint proposes auxiliary structural progress, not movement of the source metric.

This run must not repeat B2/B5/B11. I will use **B14 / B16 / B24**.

## Prior-art correction before the new attack

A fresh source check found M. A. Lopez and S. Reisner, *A special case of Mahler's conjecture*, Discrete Comput. Geom. 20 (1998), 163--177, DOI `10.1007/PL00000076`. Its abstract explicitly proves the symmetric conjecture for polytopes with at most `2n+2` vertices (or facets) when `n<=8`, with minimizers characterized. Therefore in dimension four the entire `V<=10` or `F<=10` source regime is already known. The previous run's ten-vertex shadow obstruction remains a valid internal structural calculation but is **not** a new Mahler theorem. The first vertex count not disposed of by that Lopez--Reisner statement is `V=12`.

I also checked the 2012 Fradelizi--Meyer--Zvavitch shadow-system paper and found a correction to the phrasing of the previous local-rigidity proof: their Corollary 2 says affine-volume shadow systems have **quasi-concave** volume product, and an interior local minimum forces constancy on at least one one-sided interval. Reparameterizing that constant subinterval lets one invoke their Proposition 1 equality characterization and recover the affine-shear conclusion. The final report will repair this explicitly rather than saying convexity of the volume product itself.

Recent 2026 neighbors include Chen--Li--Xi--Xu `arXiv:2605.09334` (three-dimensional theorem/shadow flow), Jimenez Cuevas `arXiv:2606.14709` (KKT/local Hanner work), and Guberman `arXiv:2608.10994` (floating bodies and combinatorial structure of minimizers). These make novelty of any structural local-minimizer lemma **UNVERIFIED**; I will not claim priority from a negative search.

## B14: quotient by central symmetry before counting constraints

Let `P=-P subset R^n` be a full-dimensional centrally symmetric polytope with vertex representatives

`Vert(P)={+-v_1,...,+-v_r}`, so `V=2r`,

and let `A:R^r -> R^n` be `Ae_i=v_i`. Put `K=ker A`, so `dim K=r-n`.

An odd speed is determined by `y_i=alpha(v_i)`, since `alpha(-v_i)=-y_i`. If a facet `G` contains the signed vertices `{sigma_i v_i : i in S_G}`, then because `aff(G)` is a supporting hyperplane not through zero, every affine function on `aff(G)` is the restriction of a linear functional on `R^n`. Hence the facet compatibility condition is exactly

`y_i = w dot v_i  (i in S_G)`

for some `w`, with the signs cancelling. Equivalently

`y perp K_G`, where `K_G := K cap R^{S_G}`.

Since the vertices of a facet span `R^n` linearly, `dim K_G=|S_G|-n=m(G)-n`.

Therefore for a direction `theta`, if `H_G=lin(G-G)`, the full admissible speed space is exactly

`A^s_theta(P) = ( span{K_G : theta notin H_G} )^perp`.

This upgrades the previous dimension lower bound to an exact quotient description. Local shadow rigidity is equivalent to

`span{K_G : theta notin H_G}=K`

for every nonzero `theta`.

## B24: optimize the exact weighted obstruction

Choose one facet from each opposite pair and set `e_G=m(G)-n`,

`E=sum e_G=(I-nF)/2`.

The old lower-bound consequence is, for every nonzero `theta`,

`r-E + sum_{theta in H_G} e_G <= n`.

Assume `r>n`. Let the positive excesses be decreasing. There must be at least `n` positive facet pairs; otherwise all positive facet-direction hyperplanes have a common nonzero direction and the displayed inequality gives `r<=n`. The largest `n-1` positive-excess hyperplanes always have nonzero common intersection. Hence

`sum_{1}^{n-1} e_(j) <= E+n-r`.

As the left side is at least `n-1`,

`E >= r-1`, equivalently

`I >= nF+V-2` whenever `V>2n`.

By polarity, whenever `F>2n`, also

`I >= nV+F-2`.

This improves the previous generic incidence debt `I>=nF+V-2n` by `2n-2` incidences.

Equality `E=r-1` is rigid: every positive excess equals one, there are exactly `r-1` nonsimplicial opposite facet pairs, and any `n` of their facet normals span `R^n`. Moreover, because exactly `n-1` such facet pairs can be made parallel to one nonzero direction, the exact quotient formula forces the remaining `r-n` one-dimensional circuit spaces `K_G` to span `K`. Thus **every `r-n` of the `r-1` circuit lines form a basis of `K`**.

For the first post-Lopez--Reisner case `n=4,V=12` (`r=6`, `dim K=2`), equality would force exactly five opposite pairs of five-vertex facets, every four of their normals independent, and their five circuit lines pairwise distinct. Since a five-vertex facet uses five of the six antipodal vertex pairs, repeated omission of the same vertex pair would give the same coordinate-kernel circuit line; therefore the five facets omit five distinct vertex-pair indices, leaving one distinguished antipodal pair present in every nonsimplicial facet pair.

## B16: exact finite test to run only after the idea

The checker will not sample Mahler volumes. It will exactly verify the finite combinatorial core for `n=4`:

1. for `r=5,...,10`, enumerate every positive-integer excess multiset with total `E<=r-1` and certify that the directional inequality has no solution with `E<r-1`, while equality has only the all-ones multiset of length `r-1`;
2. certify a five-hyperplane full-spark normal configuration in `R^4` and five pairwise-independent circuit lines in `R^2` that saturate the *abstract* rank/debt conditions at `r=6,E=5`.

The second item is deliberately a negation test: if the abstract data survive, then incidence/rank information alone cannot rule out the twelve-vertex equality budget. The next missing ingredient is realizability by a single centrally symmetric polytope (or a volume/floating-body constraint), not another incidence count.
