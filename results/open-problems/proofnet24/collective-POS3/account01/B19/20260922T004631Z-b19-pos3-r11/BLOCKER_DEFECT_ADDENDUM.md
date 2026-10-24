# POS3 B19 addendum — chain blockers are exactly the ordered-profile fiber defect

This is an additive derivation to the immutable main report `REPORT.md`. The parent POS3 target remains **OPEN / NOT PROVED**.

## 1. Direct-swap identity inside one projected fiber

Retain the main report notation. Let `C={c_1<...<c_m}`, let `Q=P\C`, and suppose

`tau=(...,u,v,...) in L(Q)`

has adjacent incomparable `u,v`. Let `tau'` be obtained by swapping them.

A full lift of `tau` may have elements of `C`, but no elements of `Q`, between `u` and `v`. Swap the *positions* of `u` and `v` in the full linear extension while leaving every other element fixed. This sends a lift of `tau` to a lift of `tau'` exactly when no element between the two positions blocks the swap.

For the forward order `u` before `v`, the only possible blockers in `C` are

`B_C^-(u,v)={c_j : c_j<v and c_j||u}`

and

`B_C^+(u,v)={c_j : u<c_j and c_j||v}`.

The direct position swap is invalid iff at least one element of their union lies strictly between `u` and `v`. The reverse order has the symmetric blocker sets. On the subsets where the swap is valid, position-swap is an involutive bijection. Therefore

`W_C(tau)-W_C(tau')`

is exactly

`(# forward lifts with a forward C-blocker between u,v)`

minus

`(# reverse lifts with a reverse C-blocker between v,u)`.        (1.1)

This is the projected-fiber version of the order-polytope swap-defect identity proved independently by account03/B11.

## 2. Ordered profiles have no reverse blockers

Assume

`lambda(u)<=lambda(v)` and `rho(u)<=rho(v)`.

Then the forward blocker sets are exactly the two chain segments

`B_C^-(u,v)={c_j : lambda(u)<j<=lambda(v)}`,

`B_C^+(u,v)={c_j : rho(u)<j<=rho(v)}`.                 (2.1)

Indeed, if `lambda(u)<j<=lambda(v)`, then `c_j<v` but `c_j` is not below `u`. It also cannot satisfy `u<c_j`, because that would give `u<c_j<v`, contradicting `u||v`; hence `c_j||u`. The successor statement is dual.

Conversely every chain predecessor blocker of `v` must have index above `lambda(u)` and at most `lambda(v)`, and every chain successor blocker of `u` must have index above `rho(u)` and at most `rho(v)`.

There are **no reverse C-blockers**. A chain element below `u` but incomparable with `v` would require an index at most `lambda(u)` but above `lambda(v)`, impossible. A chain element above `v` but incomparable with `u` would require an index above `rho(v)` but at most `rho(u)`, also impossible.

Hence (1.1) becomes the exact nonnegative formula

`W_C(...,u,v,...)-W_C(...,v,u,...)`

`= # {full lifts of tau in which at least one element of (2.1) lies between u and v}`.       (2.2)

Thus the arbitrary-chain monotonicity theorem from the main report has a second, more structural proof: direct swapping injects every reverse fiber into the forward fiber; the unmatched mass is exactly a union of genuine blocker events.

## 3. The interval displacement is exactly the number of chain blockers

For ordered profiles put

`Delta_0=(lambda(v)-lambda(u))+(rho(v)-rho(u))`.

Because `u||v`, the two allowed intervals overlap, so the two blocker segments in (2.1) are disjoint. Consequently

`Delta_0 = |B_C^-(u,v)|+|B_C^+(u,v)|`.                (3.1)

Under a fixed outer chain-prefix window `[L,U]`, the main report uses truncated intervals

`A=I(u) cap [L,U]=[alpha,beta]`,

`B=I(v) cap [L,U]=[gamma,delta]`

and

`Delta_{L,U}=(gamma-alpha)+(delta-beta)`.

The first term counts precisely the predecessor blockers in (2.1) whose chain index is still above the imposed lower prefix `L`; the second counts precisely the successor blockers whose index is still at or below the imposed upper prefix `U`. Thus the “midpoint displacement” in the reflection proof is not an abstract parameter: it is the number of **effective chain blockers visible in that outer context**.

Combining this with the main short-gap identity gives two different exact descriptions of the same local defect:

1. as the number of forward prefix pairs in the short-gap band `0<=b-a<Delta_{L,U}`;
2. as the number of forward lifts for which at least one effective chain blocker lies between `u` and `v`.

The two descriptions need not match lift-by-lift under the reflection injection, but their cardinalities agree exactly.

## 4. Why the one-element theorem has defect at most one

When `|C|=1`, an incomparable pair cannot have disjoint allowed intervals. Therefore an endpoint-ordered incomparable profile can contain at most one chain blocker in total. Formula (2.2) immediately gives

`|W(tau)-W(tau')|<=1`,

recovering the account04/B20 one-element theorem from the arbitrary-chain blocker formula.

For longer chains the number of blockers in (3.1) is unbounded. The width-two family in the main report has `m` predecessor blockers and one adjacent-swap defect exactly `m`. This explains, structurally rather than only numerically, why the one-element Lipschitz theorem cannot persist for arbitrary chain deletion.

## 5. Connection to the fresh double-blocker theorem

Account03/B11 proves that an adjacent strong-majority pair in a hypothetical width-three counterexample requires a positive swap-defect union supported by at least two canonical blockers; a single local blocker event cannot carry the necessary `>1/3` mass. Formula (2.2) shows that, whenever a chain deletion produces endpoint-ordered profiles, the gradient of the exact insertion weight across the corresponding projected adjacent swap is **literally blocker-union mass** from that deleted chain.

So the two collective mechanisms are not merely analogous:

> the chain-deletion weight gradient and the order-polytope swap defect are the same obstruction viewed after projection versus before projection.

For nested profiles, both forward and reverse chain blockers can coexist, and (1.1) becomes a signed difference of two blocker-union masses. This is exactly where context-dependent swap sign enters.

The remaining global task can therefore be stated in blocker language: across a three-chain cover, show that the simultaneous blocker unions required to push all three width-two projected balanced pairs outside `[1/3,2/3]` cannot be realized in the connected module-prime strong-majority core, or else construct an exact realization and isolate a further invariant.

## 6. Regression check

`verify_blocker_defect_addendum.py` exhaustively checked every endpoint-ordered overlapping interval-profile pair through `m<=8` and every feasible outer window. It verified that the local weight difference equals the number of forward local lifts containing at least one chain blocker between the swapped elements.

Recorded output:

`ordered_overlapping_contexts=27026`

`POS3_CHAIN_BLOCKER_DEFECT_CHECK_PASS`

The check is regression evidence only; (1.1)–(3.1) follow from the explicit direct-swap involution and interval definitions.
