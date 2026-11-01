Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-09 idea before code — surface-group product via free-subgroup percolation + nonbacktracking operator

## Frozen source target

The full source target remains the Benjamini–Schramm bond-percolation conjecture for Cayley graphs:

> For every locally finite Cayley graph `G` of a finitely generated nonamenable group, prove `p_c(G) < p_u(G)`.

This note does not claim that full conjecture. The goal of this bounded run is a rigorously certified new restricted family outside the already-known hyperbolic/product-of-trees/tree-times-amenable examples, plus a structural mechanism that can be reused.

## Candidate family

Let

`Gamma_3 = <a1,b1,a2,b2,a3,b3 | [a1,b1][a2,b2][a3,b3]=1>`

and

`Gamma_4 = <c1,d1,c2,d2,c3,d3,c4,d4 | [c1,d1][c2,d2][c3,d3][c4,d4]=1>`

be closed orientable surface groups of genera 3 and 4. Give each its standard symmetric generating set, and let

`G = Cay(Gamma_3 x Gamma_4, S_3 union S_4)`.

Then `G` is 28-regular.

### Free-subgroup comparison

By the Magnus Freiheitssatz, deleting one generator occurring in the one-relator surface presentation leaves a free subgroup on the remaining generators. Thus:

- in `Gamma_3`, deleting `b3` leaves `F_5`, whose standard symmetric Cayley graph is `T_10`;
- in `Gamma_4`, deleting `d4` leaves `F_7`, whose standard symmetric Cayley graph is `T_14`.

Using only those subgroup-generator edges in the product Cayley graph gives an embedded copy of `T_10 square T_14`. Hence

`p_c(G) <= p_c(T_10 square T_14)`.

Orient the `T_14` factor, so each explored vertex has `q=13` forward tree children, and take the vertical factor to be `T_10`. The archived June cluster-branching proposition says that if

`q * phi_H(p) > 1`, with `phi_H(p)=E[1-(1-p)^|C_H(o)|]`,

then the product is supercritical (and strict margin at `p0` gives `p_c < p0`).

At `p0=3/50`, lower-bound `phi_{T_10}` using only the vertical root and its ten neighbors. A child fiber is activated if either the root's horizontal child edge is open, or for one of the ten vertical neighbors both the root-neighbor vertical edge and that neighbor's horizontal child edge are open. These events use disjoint edge sets, so

`phi_{T_10}(p) >= L(p) := 1-(1-p)(1-p^2)^10`.

The intended exact check is

`13 L(3/50) > 1`,

which would imply

`p_c(G) < 3/50`.

## Nonbacktracking two-point lower bound for p_(2->2)

Split each surface-factor adjacency into the free-subgroup edges plus the omitted generator pair. The free parts are disjoint unions of regular trees on cosets, so

`||A_3|| <= 2 sqrt(9)+2 = 8`,

`||A_4|| <= 2 sqrt(13)+2`.

Since Cartesian-product adjacency is `A_3 tensor I + I tensor A_4`,

`||A_G|| <= R := 10 + 2 sqrt(13)`.

For a 28-regular graph, the standard nonbacktracking recurrence from the June archive gives the exponential kernel bound

`limsup ||N_n||^(1/n) <= beta(28,R)`,

where, because `R>2 sqrt(27)`,

`beta(28,R) = (R + sqrt(R^2-108))/2
             = 5 + sqrt(13) + sqrt(11+10 sqrt(13)).`

Every self-avoiding path is nonbacktracking. Therefore the two-point kernel is bounded in `ell^2` for every

`p < 1/beta(28,R)`,

so

`p_(2->2)(G) >= 1/beta(28,R)`.

The intended exact comparison is

`beta(28,R) < 50/3`,

which yields

`3/50 < 1/beta(28,R) <= p_(2->2)(G) <= p_u(G)`.

Consequently this family would have the certified quantitative gap

`p_u(G)-p_c(G) > 1/(5+sqrt(13)+sqrt(11+10 sqrt(13))) - 3/50 > 0`.

## Why nonbacktracking is doing real work

The same coarse adjacency norm by an all-walk/resolvent bound gives only

`p_(2->2) >= 1/(10+2sqrt(13))`,

and the intended exact check is that this is **below** `3/50`. Thus the all-walk route does not bridge the percolation upper bound, while the nonbacktracking recurrence does.

## Three genuinely different attacks compared

1. **Attack the negation / known-class screen.** The first obvious product candidate `T_d square T_e` is unusable as a fresh result because products of regular trees already have a known nonuniqueness phase. The surface-product candidate is instead not Gromov hyperbolic (it contains `Z^2`), has 4-cycles, and is not a tree-times-amenable product.
2. **Subgroup comparison.** Use Magnus free subgroups only to upper-bound `p_c` through an embedded `T_10 square T_14`; this is a geometric/percolative comparison, not an operator estimate.
3. **Nonbacktracking two-point operator.** Use the full 28-regular Cayley graph and a norm bound on its adjacency to obtain a lower bound on `p_(2->2)`; the ordinary all-walk version misses the required threshold.

These routes are logically independent enough to cross-check one another: one supplies the supercritical comparison, one supplies the operator subcritical comparison, and the known-class screen tests whether the candidate merely rediscovers an established special case.

## Structural criterion to extract if the arithmetic passes

For an infinite connected `D`-regular Cayley graph `X`, suppose:

- a subgroup-generated subgraph `H` has a certified strict bound `p_c(H)<p0`, hence `p_c(X)<p0`;
- `||A_X||<=R`;
- `p0 * beta(D,R) < 1`.

Then the nonbacktracking recurrence and the general inequality `p_(2->2)<=p_u` give

`p_c(X)<p0<1/beta(D,R)<=p_(2->2)(X)<=p_u(X)`

and hence

`p_u(X)-p_c(X) > 1/beta(D,R)-p0`.

This is a proved-scope target for the report if the exact inequalities are checked. It is a synthesis of recovered archive lemmas, not a claim of external novelty.

## Prior-art status before code

Current primary-source checks dated 2026-09-20 local time confirm that Hutchcroft's hyperbolic theorem covers nonamenable Gromov-hyperbolic quasi-transitive graphs, Hutchcroft–Pan cover a subgroup-relativization class at `p_u`, and Terlov–Timár treat weighted/nonunimodular settings. Bounded exact searches for surface-group products did not locate a source directly covering this explicit standard Cayley graph. This is negative search evidence only, not a worldwide novelty certificate; the final report must keep the result PARTIAL for the full Benjamini–Schramm conjecture and record the search limitation.
