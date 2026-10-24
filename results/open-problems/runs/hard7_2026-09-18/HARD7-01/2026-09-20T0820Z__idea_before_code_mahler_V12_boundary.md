Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric remains `d_sym: 3 -> 3` unless the argument below closes all 4D bodies. Planned methods: **B6 / B13 / B29**.

# HARD7-01 route note — deform the twelve-vertex boundary to a three-dimensional difference-body inequality

This note is intentionally written before any new checker.

The preceding run reduced the generic twelve-vertex 4D Mahler subclass to the rank-two Gale/box-spline inequality BS12. Rather than sample more Gale matrices, this run attacks the compactification/boundary where a facet acquires all six antipodal vertex pairs.

## B6: exact deformation endpoint with a six-vertex facet

Let a centrally symmetric four-polytope with twelve vertices have a facet containing six vertices. A proper facet contains at most one vertex from each antipodal pair, so this facet contains exactly one representative of every pair. After an affine change of coordinates,

`P = conv((L,1),(-L,-1))`

for a three-dimensional convex body/polytope `L`. Put `D=L-L`.

The intended exact calculation is

`|P| = (|D|+4|L|)/6`,

`|P^o| = 4 |D^o|`,

and hence

`|P||P^o| = (2/3)(|D|+4|L|)|D^o|`.

Thus the sharp 4D Mahler inequality on this entire boundary class is equivalent to the three-dimensional inequality

`(|L-L|+4|L|)|(L-L)^o| >= 16`.                 (DF6)

This has the correct equality values both when `L` is centrally symmetric/Hanner-like and when `L` is a tetrahedron. I will derive it on the page from mixed volumes and a one-dimensional polar-fiber integration, not infer it numerically.

## B13: exploit shadow rigidity before touching the continuous inequality

For a putative 4D local minimizer with `V=F=12` and no six-vertex facet, every facet has four or five vertices. If `x` is the number of opposite five-vertex facet pairs, the admissible-speed debt is `E=x`. Any three facet hyperplanes in `R^4` have a nonzero common direction, so applying the directional shadow bound to the three largest debts forces `x>=5`. Duality gives the same tail restriction to the six opposite vertex pairs.

The most symmetric remaining combinatorial corner is therefore the case in which all twelve facets have five vertices and all twelve vertices have degree five. Quotienting by central symmetry gives a `6 x 6` incidence matrix with exactly one omission in every row and column, hence (after relabeling) the complement of a perfect matching.

A five-vertex three-dimensional facet is either a square pyramid or a triangular bipyramid. In the complement-of-matching incidence pattern, two facet pairs share only four antipodal vertex-pairs, and one facet cannot have ridge intersections with both orientations of the same opposite facet pair because the two common-sign counts add to four. Thus a five-vertex facet has at most five ridges and must be a square pyramid. Duality forces every vertex figure to be a square pyramid as well.

Orient the six facet pairs and six vertex pairs. Off the omitted matching, write a sign `s_ij in {+1,-1}` for which representative of the j-th vertex pair lies on the i-th facet. The square-pyramid condition says: for every pair of rows, among the four common supported columns the number of equal signs is `0 or 4` for exactly one partner and `1 or 3` for the other four partners; the analogous condition holds for columns.

The exact finite question worth checking is whether these row/column sign constraints leave any patterns, and if so how many orbits they have under relabeling and row/column orientation flips. If they collapse to one orbit, the full continuous realizability question becomes a single symbolic rank calculation rather than another combinatorial enumeration.

## B29: add the points at infinity / cube-section boundary

For such an all-five/all-five configuration, the six polar cube-section vertices may be written as the rows of

`Q = S + diag(t_1,...,t_6)`,

where `S` is the off-diagonal sign matrix and every `|t_i|<1` because the omitted coordinate is genuinely unsaturated. All six rows lie in the same four-dimensional central section of `[-1,1]^6`, so necessarily `rank(Q)<=4`.

The strongest possible finite obstruction would be: every admissible sign orbit has a `5 x 5` minor of `Q` that factors into terms nonzero on the open cube `(-1,1)^6`. That would rule out the all-five/all-five combinatorial corner completely and force any `V=F=12` candidate toward either a six-vertex facet (hence DF6) or the remaining asymmetric degree patterns.

Only after this route is explicit will I write a checker. The source target remains the full symmetric Mahler conjecture; even a complete `V=F=12` reduction is auxiliary and does not move `d_sym`.