# PROB10-04 idea before code — heterogeneous rescue blocks and an exact negative-association compiler

This note is written **before** any new checker for the present run.  It continues only the scoped cluster-aware / overlap-counting route in `operations/claims/PROB10-04.md`.  It does not duplicate NM13-13's interpolation trial or NM13-06's constructive unit-propagation route.

## Why change the previous mechanism

The preceding report proved an `r`-block rescue only for centers `t_{r,r}`, leaves exactly `f_{1,1,1}`, one safe clause type `a=((1,1),(1,0))`, and one blocker type `b=((0,1),(1,1))`.  It then paid two concentration losses before applying the block-avoidance inequality.  That is qualitatively sufficient at an interior Diaz type but wastes almost all of the available local structure and leaves the quantitative reoptimization opaque.

The new target is an **explicit continuous penalty functional**, with no concentration constants, for a much larger deterministic rescue family.

## Deterministic heterogeneous rescue motif

Work with one flat-satisfying assignment represented by the Diaz extended type system.  Assume the represented formula is proper/simple (three distinct variables in each clause), as in the source target.

Define three pools.

1. `Q_safe`: every `ps` target slot in a clause having at least two satisfied literals before the move.  Equivalently, sum `ps(alpha)c_alpha` over extended clause types with `ps(alpha)+ns(alpha)>=2`.
2. `B_can`: choose one deterministic canonical `nu` slot in every blocking clause whose unique satisfied literal is `ns1` and which has at least one `nu` slot.  In 3-SAT these are the types `((0,1),(1,1))` and `((0,1),(0,2))`; there is one canonical slot per such clause.
3. `E_1`: all false light variables of class `f_{i,1,1}`, summed over the allowed positive degrees `i`.  Such a variable has exactly one negative occurrence, and it is its unique blocking `ns1` occurrence.

Now take **any** true light center of class `t_{i,j}` with `j>=2`, not merely `t_{r,r}`.  Call it completed when

- all its `i` `ps` copies land in `Q_safe` slots;
- all its `j` `nu` copies land in distinct canonical slots from `B_can`;
- the associated `j` blocker `ns1` slots are occupied by copies from `E_1`.

### Deterministic rescue lemma

A flat-satisfying proper formula maximizing the number of true light variables contains no completed center `t_{i,j}` with `j>=2`.

**Proof.**  Let `y` be a completed center, and let `x_1,...,x_j` be the distinct `E_1` leaves in the blocker clauses hit by the center's canonical `nu` copies.  Flip `y:1->0` and all `x_h:0->1` simultaneously.

Each leaf has negative degree one and that negative occurrence is exactly its `ns1` blocker.  Thus the only clause a leaf flip can hurt is its blocker; every positive occurrence changes from false to true.  The center's corresponding `nu` occurrence changes from false to true in that blocker, so every blocker stays satisfied.

The center's `nu` occurrences only become true.  A center `ps` occurrence can become false, but by definition it lies in a clause with at least one other satisfied literal.  None of those other satisfied literals can be the selected leaf's disappearing negative literal: every selected leaf's sole negative occurrence is `ns1`, hence lies in a clause in which it is the unique satisfied literal and therefore cannot share a clause with a center `ps` occurrence that is also satisfied.  Other selected-leaf changes only turn positive literals from false to true.  Properness prevents another occurrence of the center variable in the same clause.  Hence all center-anchor clauses remain satisfied.

The move gains `j` true leaves and loses one true center, so the number of true light variables increases by `j-1>0`, contradicting maximality.  QED.

This enlarges the old leaf pool from only `f_{1,1,1}` to every `f_{i,1,1}`, enlarges safe center anchors from one clause type to every multiply-satisfied clause, enlarges canonical blockers from one type to both possible negative-unique-satisfied blocker types with `nu>0`, and enlarges centers from the diagonal `t_{r,r}` to every `t_{i,j}` with `j>=2`.

## Exact finite matching compiler via negative association

Fix an integer coarse type.  Let

- `P` be the number of all `ps` target slots and `Q` the number in `Q_safe`;
- `U` be the number of all `nu` target slots and `B` the number in `B_can`;
- `L` be the number of all `ns1` target slots and `E` the number of marked leaf `ns1` source copies from `E_1`;
- `C_{i,j}` be the number of center variables of class `t_{i,j}`.

The Diaz copy allocation uses independent uniform bijections in the `ps`, `nu`, and `ns1` label classes.  For a center `c` of class `(i,j)`, the three one-layer completion probabilities are exactly

`a_i=(Q)_i/(P)_i`,

`b_j=(B)_j/(U)_j`,

`e_j=(E)_j/(L)_j`,

with `(x)_r=x(x-1)...(x-r+1)` and the value zero when a pool is too small.

### Proposed exact theorem

For all disjoint center copy blocks, including heterogeneous `(i,j)`,

`P(no center is completed) <= product_{i,j>=2} (1-a_i b_j e_j)^{C_{i,j}}`.      (NA)

This is stronger than the preceding concentration-plus-typical-event estimate and has no polynomial prefactor or unknown large-deviation constant.

### Proof route for (NA)

The indicator vector obtained by marking which source copies in a uniform bijection hit a fixed target subset is a uniform fixed-size `0/1` vector, hence negatively associated.  Negative association is preserved under coordinatewise monotone functions on disjoint coordinate blocks; the same product bound holds for decreasing block events as well (equivalently apply the property to complements).

Condition first on the complete `nu` matching.  Let `M` be the set of centers whose whole `nu` block hits canonical blocker slots.  Because there is only one canonical `nu` slot per blocker clause and the bijection is injective, the associated `ns1` target blocks for distinct centers in `M` are disjoint.

For a fixed set `J` of centers whose associated `ns1` blocks are all hit by marked leaf copies, negative association in the independent `ps` matching gives

`P(no A_c for c in J) <= product_{c in J}(1-a_{i(c)})`.

Average this over the `ns1` matching.  The leaf-block success indicators are monotone functions of disjoint blocks of a fixed-size sample, hence negatively associated.  Therefore

`P(no completed A_c L_c | nu) <= product_{c in M}(1-a_{i(c)} e_{j(c)})`.

Finally average over the `nu` matching.  Its canonical-block success indicators are again negatively associated, so

`P(no completed center) <= product_c (1-a_{i(c)}e_{j(c)}b_{j(c)})`,

which groups by center class to give (NA).

The standard negative-association theorem for sampling without replacement is the only external probabilistic input.  The deterministic rescue lemma is independent of it.

## Asymptotic correction functional

For a fixed interior density vector `x`, write

`q=Q/P`, `b=B/U`, `e=E/L`, `d=be`.

For each fixed bounded `i,j`, falling-factorial ratios converge to powers.  Therefore (NA) yields the explicit relative exponential penalty

`J_res(x) = - sum_{i,j: j>=2} t_{i,j}(x) log(1-q(x)^i d(x)^j) >= 0`.      (1)

The refined Diaz objective becomes, at least on the simple-source representatives,

`F_ref(x) <= F_Diaz(x) exp(-J_res(x))`.

The next quantitative task is not another local lemma: evaluate (1) at the published saddle and then determine whether a globally certified reoptimization can beat the existing endpoint.  If the local value is far smaller than the source's objective margin, that is an obstruction and this route should switch to a coupled motif rather than manufacture more rescue checkers.

## Negation test before code

A tempting further enlargement is to allow leaves `f_{i,j,1}` with `j>1`.  That is **not** automatically sound: such a leaf has `ns2` occurrences that change from true to false, and one of those can be the supposedly safe second satisfied literal in a center anchor clause.  Thus the collision-free `j=1` leaf pool above is close to the maximal enlargement available without tracking variable identities across additional clause slots.

A different, potentially much stronger next mechanism is an **alternating rescue cycle**: make the selected leaves' `pu` occurrences themselves be the literals that rescue the center's `ps` anchor clauses, while the center's `nu` occurrences rescue the leaves' `ns1` blockers.  This removes the pre-existing-safe-anchor factor `q^i`, but it couples four copy matchings through leaf identity.  The exact missing lemma would be an identity-preserving alternating-cycle count, not another independent occupancy bound.