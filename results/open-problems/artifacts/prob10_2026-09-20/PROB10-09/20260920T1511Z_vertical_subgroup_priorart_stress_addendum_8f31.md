# PROB10-09 prior-art stress addendum — finite-image action for the frozen extension

The mathematical spectral-budget idea in `20260920T1458Z_vertical_subgroup_spectral_budget_idea_8f31.md` is unchanged. During the required negation/prior-art stress test, I replaced the initially suggested exponentially growing Nielsen action by a finite-image nontrivial action. This makes the class-exclusion argument cleaner without changing the Cayley degree, quotient estimate, vertical norm, nonbacktracking calculation, or exact checker.

## Corrected frozen group

Let `N=F_3 x F_3`, with free bases `(x_1,x_2,x_3)` and `(y_1,y_2,y_3)`. Let `sigma in Aut(N)` simultaneously swap `x_1<->x_2` and `y_1<->y_2`, fixing `x_3,y_3`. Thus `sigma^2=1` and `sigma` is nontrivial.

Let `Q=Gamma_5=<a_1,b_1,...,a_5,b_5 | product_i [a_i,b_i]=1>`. Define `alpha:Q->Aut(N)` by `alpha(a_1)=sigma` and by sending `b_1,a_2,b_2,...,a_5,b_5` to the identity. The surface relator maps to the identity, so `alpha` is well-defined. Put

`Gamma=N semidirect_alpha Q`.

Use split horizontal lifts of the standard 20 quotient directions and the standard 12-direction product marking of `N`. The graph is still 32-regular. The kernel is genuinely noncentral because `a_1` conjugates `x_1` to `x_2` (and `N` itself is nonabelian).

## Why the principal known all-Cayley classes checked here do not subsume this group

- `Gamma` is not Gromov hyperbolic: it contains `Z^2` (for example `<x_3,y_3>`).
- `Gamma` is not acylindrically hyperbolic. It has the infinite normal subgroup `N=F_3 x F_3`, which is not acylindrically hyperbolic (a direct product of two infinite groups), while every infinite normal subgroup of an acylindrically hyperbolic group is acylindrically hyperbolic.
- The explicit Hutchcroft--Pan 2024 sufficient class `amenable wq-normal subgroup of exponential growth` is absent here: every amenable subgroup of `Gamma` has polynomial growth. Indeed an amenable subgroup projects to a cyclic subgroup of the torsion-free hyperbolic surface group. Its intersection with `N` has cyclic coordinate projections to each `F_3`, hence is a subgroup of `Z^2`. After passing to index at most two in the cyclic quotient, the finite-image action `alpha` disappears; normalizers of infinite cyclic subgroups in free groups are cyclic, so the remaining inner conjugations act trivially on a finite-index subgroup of the abelian kernel intersection. Thus the amenable subgroup is virtually abelian of rank at most three.

This argument only screens the named/current classes consumed by this run. It is **not** a worldwide novelty proof. A bounded current search did not locate a theorem already giving this fixed-marking quantitative gap, but external priority remains UNVERIFIED until independent literature review.
