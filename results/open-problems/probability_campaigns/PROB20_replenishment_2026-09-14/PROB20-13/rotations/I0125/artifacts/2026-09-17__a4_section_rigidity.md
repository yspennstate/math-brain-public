# Exact A4-section rigidity lemma for the five-dimensional kissing problem

Target normalization: a kissing code is a finite set `C \subset S^4 \subset R^5` with `x.y <= 1/2` for every two distinct points.

## Theorem

Let

`R = {(e_i-e_j)/sqrt(2) : 1 <= i != j <= 5}`,

so `R` is the 20-point `A_4` root system in the hyperplane

`H = {x in R^5 : x_1+...+x_5=0}`.

If a five-dimensional kissing code `C` contains an isometric copy of `R`, then

`|C| <= 40`.

Moreover, if `|C|=40`, then after an orthogonal transformation `C` is one of the two known 40-point configurations with this exact `A_4` central section: `D_5` or `Q_5`.

This is a restricted theorem. It does not change the unrestricted interval `40 <= tau_5 <= 44`.

## Proof

Rotate the code so that its `A_4` subsystem is exactly `R`. Put

`w=(1,1,1,1,1)/sqrt(5)`.

Every `x in C\R` has a unique decomposition

`x = h w + y`, with `y in H`.

For every `i != j`, both `(e_i-e_j)/sqrt(2)` and its negative belong to `R`. Hence the kissing inequalities imply

`|y_i-y_j| <= 1/sqrt(2)` for all `i,j`.                                            (1)

### Lemma 1: the five-coordinate range bound

If `y in H` and `delta=max_i y_i-min_i y_i`, then

`||y||^2 <= (6/5) delta^2`.                                                        (2)

Proof. Because `sum_i y_i=0`, `||y||^2` is five times the empirical variance. If `delta>0`, normalize the coordinates affinely to `z_i in [0,1]` with the same relative positions. The variance functional

`V(z)=sum_i z_i^2-(sum_i z_i)^2/5`

is convex, so on the cube `[0,1]^5` its maximum is attained at a vertex. If exactly `k` coordinates of that vertex equal 1, then

`V=k-k^2/5=k(5-k)/5 <= 6/5`.

Rescaling by `delta` proves (2). Equality occurs only when the full range is attained and, after ordering, two coordinates lie at one endpoint and three at the other (or vice versa). QED.

By (1) and Lemma 1,

`||y||^2 <= (6/5)(1/2)=3/5`.

Since `||x||=1`,

`h^2 = 1-||y||^2 >= 2/5`.                                                         (3)

Thus every point outside `R` lies strictly on one side or the other of `H`.

Let `C_+` be the points with `h>0`. Except for the possible pole `w`, write each such point as

`x = a w + sqrt(1-a^2) u`,

where `a>=sqrt(2/5)` and `u in H`, `||u||=1`. For two such points with heights `a,b`, the kissing inequality gives

`u.v <= F(a,b):=(1/2-ab)/(sqrt(1-a^2)sqrt(1-b^2))`.                              (4)

For `a,b >= sqrt(2/5)`,

`partial F/partial a` has the sign of `a/2-b`,

which is negative because `a/2 <= 1/2 < sqrt(2/5) <= b`; symmetrically `F` decreases in `b`. Therefore

`F(a,b) <= F(sqrt(2/5),sqrt(2/5)) = 1/6`.                                        (5)

If the pole `w` occurs, it cannot coexist with another positive-height point, since its inner product with such a point is at least `sqrt(2/5)>1/2`. Otherwise the projected vectors from `C_+` form a spherical code in `S^3` with maximal inner product at most `1/6`.

Bachoc and Vallentin proved the optimality and uniqueness of the `(4,10,1/6)` Petersen spherical code (JCTA 116 (2009), 195-204). In particular a 10-point code at this threshold is the Petersen code. For completeness, it cannot be extended by an eleventh point at the same threshold: in the standard realization indexed by 2-subsets `A={i,j}` of `{1,...,5}`, its vectors are proportional to the centered incidence vectors, and for any unit `z in H`,

`max_{i<j} (z_i+z_j) >= 1/sqrt(5)`.

Indeed, writing `z_1>=z_2>=...>=z_5`, fixing `t=z_1+z_2`, and maximizing the squared norm under the ordering and zero-sum constraints gives `||z||^2 <= 5t^2`, with equality at a vector proportional to `(1,1,1,1,-4)`. Hence some Petersen vector has inner product at least `1/sqrt(6)>1/6` with `z`. Thus no eleventh point exists.

Consequently

`|C_+| <= 10`.

The identical argument on the negative side gives `|C_-|<=10`, and therefore

`|C| = 20+|C_+|+|C_-| <= 40`.

This proves the bound.

### Equality classification

Assume now `|C|=40`. Then both hemispheres contain exactly ten points. Their projections are therefore Petersen codes. Every point of a Petersen code has another point at inner product exactly `1/6`. For such a pair, (4)-(5) must be equality, which forces both heights to have absolute value exactly `sqrt(2/5)`. Hence every extra point has

`h^2=2/5` and `||y||^2=3/5`.

Equality in Lemma 1 now forces the five coordinates of `y` to have exactly two values. After choosing a 2-subset `A`, one possibility is

`y_i = 3/(5sqrt(2))` for `i in A`, and `y_i = -2/(5sqrt(2))` otherwise,

and the other possibility is its negative (equivalently the complementary 3-subset description). After normalization in `H`, the ten vectors indexed by 2-subsets form the standard Petersen code `P`; all equality directions are `P union (-P)`.

It remains to classify a ten-element feasible layer chosen from `P union (-P)`. For 2-subsets `A,B`,

`u_A.u_B = (5|A intersect B|-4)/6`,

while

`u_A.(-u_B)=-(5|A intersect B|-4)/6`.

Thus the only forbidden mixed-sign pairs are `u_A` and `-u_B` with `A` and `B` disjoint, for which the inner product is `2/3`. The resulting forbidden graph between `P` and `-P` is the connected 3-regular bipartite double cover of the Petersen graph (the Desargues graph).

In any connected `d`-regular bipartite graph with equal part sizes `n`, an independent set of size `n` must be one entire bipartition class: if it contains `A` on the left and `B` on the right, regular edge counting gives `|A| <= n-|B|`; equality at total size `n` would force no edge between the complementary nonempty pieces, contradicting connectedness. Hence each ten-point hemisphere layer is either all of `P` or all of `-P`.

There are therefore only four sign choices for the two hemisphere layers. Up to reflection across `H` and global isometry, opposite choices give the `D_5` root configuration, while equal choices give Szolloesi's `Q_5` layer-reflection configuration. This proves the equality classification. QED.

## Prior-art boundary checked 2026-09-17

- Cohn-Rajagopal (2026), Section 2, explicitly describes the `A_4` central section of `D_5` and the layer reflection producing `Q_5`, but the bounded search performed for this run did not locate the above conditional theorem `A_4 subset => |C|<=40` or its equality classification stated there.
- Bachoc-Vallentin (2009) supplies the crucial independent exact `(4,10,1/6)` Petersen-code theorem.
- Public notes in `wustep/maths/problems/kissing-5d/` already contain exact maximality certificates for each of `D_5,L_5,Q_5,R_5`, a separate 24-cell/D4-section `<=40` theorem, and an `A_4` equatorial no-extra-point check for `Q_5`. Those are close prior attempts and must be credited; they do not, in the inspected notes, state this full A4-section bound/classification.

No publication-novelty claim is made. The theorem is a source-relevant restricted obstruction and leaves `W_5=4`.
