# PROB10-04 idea before code — a degree-two deterministic rescue pair inside the Díaz type model

This is a deliberately narrow continuation of the PROB10-04 cluster-aware counting route after reading the current neighboring work.  It does **not** duplicate NM13-13's degree-one `t_{1,1}` random-score matching or its newer two-survey interpolation certificate.  The new object is an unweighted three-flip obstruction based on a true `t_{2,2}` center and two false degree-`(1,1,1)` leaves.

## Exact local pattern

Use Díaz's extended clause coordinates

`alpha = ((ps,ns),(pu,nu))`.

Fix the two clause types

- safe-`ps` anchor `a=((1,1),(1,0))`: its unique `ps` literal is protected by an `ns2` literal;
- blocker `b=((0,1),(1,1))`: its unique satisfied literal is an `ns1`, and it has a unique `nu` slot.

Select

- a **center** `y` from `t_{2,2}` whose two `ps` copies both land in distinct type-`a` clauses;
- a **leaf** `x` from `f_{1,1,1}` whose unique `ns1` copy lands in a type-`b` clause.  Since its negative degree is exactly one, it has no `ns2` occurrence at all.

If two distinct selected leaves `x,z` have type-`b` blockers whose unique `nu` slots are occupied by the two `nu` copies of the same selected center `y`, then simultaneously flipping

`x:0->1, z:0->1, y:1->0`

preserves flat satisfiability and increases the number of true light variables by one.

Reason: each leaf can only destroy its own unique `ns1` blocker, and the corresponding center `nu` becomes true there; every other leaf occurrence is positive and therefore only helps.  The center can only destroy its two `ps` literals, but both are in type-`a` clauses and each such clause retains its `ns2` literal.  The selected leaves cannot supply those `ns2` anchors because their negative degree is one and that occurrence is already their `ns1` blocker.

Hence a global maximum of the number of true light variables among flat-satisfying assignments cannot contain this completed degree-two rescue pattern.

## Configuration-model transfer to prove

For a fixed interior Díaz coarse type `x`, write

- `E=f_{1,1,1}` for the selected-leaf density;
- `C=t_{2,2}` for the potential-center density;
- `B=c_b` for the type-`b` blocker density;
- `Q=c_a` for the number-density of safe type-`a` `ps` slots (one per type-`a` clause);
- `L1=ell_ns1`, `P=ell_ps`, `U=ell_nu`.

The copy-allocation stage is uniform within each copy label.  Therefore:

1. the number `S n` of selected leaf `ns1` copies landing in the `Bn` blocker slots is hypergeometric with mean `(E B/L1)n`, hence is linear with exponentially high probability at every fixed interior type;
2. the number `A n` of `t_{2,2}` variables whose two `ps` copies both land in the `Qn` safe slots has mean asymptotic to `C(Q/P)^2 n` and is exponentially concentrated by bounded differences for random permutations;
3. conditional on these choices, the `Sn` canonical `nu` slots of the selected blockers receive a uniformly random `Sn`-subset of the `Un` `nu` copies.  The `An` available centers contribute `An` disjoint marked pairs of `nu` copies.

Thus rescue-freeness forces a uniform `S`-subset of `U` points to contain **no complete one of `A` marked disjoint pairs**.

## Exact finite pair-avoidance identity and target bound

Let `N_0(U,A,S)` count `S`-subsets of `U` points containing no complete marked pair when `A` disjoint pairs are marked.  Then

`N_0(U,A,S) = sum_r C(A,r) 2^r C(U-2A,S-r)`,

where impossible binomial terms are zero.  Equivalently

`N_0(U,A,S) = [z^S] (1+2z)^A (1+z)^(U-2A)`.

The useful bound should be completely finite and self-contained.  Put `z=S/(U-S)`.  Coefficient domination gives

`N_0 <= z^{-S}(1+2z)^A(1+z)^(U-2A)`.

Because `S` is a mode of `Bin(U,S/U)`,

`C(U,S) z^S/(1+z)^U >= 1/(U+1)`.

Therefore

`P_pair0(U,A,S) <= (U+1) [1-(S/U)^2]^A`.                    (★)

If `A/U` and `S/U` stay bounded below by positive constants, (★) is an explicit `exp(-kappa n+O(log n))` penalty.  This is the exact missing bridge from the previous PROB10-04 blocker-occupancy mechanism into the Díaz copy-allocation architecture, but only for this fixed-degree subpattern.

## What would count as progress this run

The intended theorem is **not** a new threshold endpoint by itself.  It is:

> For every fixed interior Díaz type with positive `f_{1,1,1}`, `t_{2,2}`, `c_a`, `c_b`, `ell_ps`, `ell_ns1`, and `ell_nu`, the fraction of Díaz copy allocations that can support a Hamming-weight-maximal flat-satisfying assignment is smaller by `exp(-kappa(x)n+o(n))` for an explicit positive `kappa(x)` obtained from (★) and the two concentration steps.

The source-level threshold metric moves only if this penalty is globally and quantitatively reoptimized over the full Díaz feasible polytope or inserted into another already-rigorous upper functional.  The neighboring `4.418` interpolation result is a separate candidate theorem and is not to be rederived here.
