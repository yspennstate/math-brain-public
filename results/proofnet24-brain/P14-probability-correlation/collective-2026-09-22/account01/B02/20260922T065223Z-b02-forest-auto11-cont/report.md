# FOREST B02 attempt — cross-fibre obstruction and exact K4-parallel compensation

Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent FOREST: `OPEN`  
Context: `WITHOUT_VERIFIED_BRAIN`

## Controls and inherited state

Fresh control read was taken on main commit `f9afa023f5de4438dbd889a70d300b481046f385`, owner revision `2026-09-22.2`, under `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. No installation or benchmark work was resumed.

Latest complete lead handoff consumed: account01/B01 `20260922T050946Z`, shared blob `4cee205cb7d254caf785692838111988a0b8a155`. Its triangle-contraction/STAR-2 debt is retained, but its rank-degree CLC strengthening remains rejected by the previous B02 source correction; no rank-degree CLC statement is used here.

Named OTHER-account result consumed and applied: account02/B03 `20260922T061345Z`, shared blob `4c17f361f23133c2048906f198e84eefc9904b63`. The parts used here are: (i) global STAR-2 is parent-hard, so minimal-counterexample structure must be retained; (ii) after block factorization the unresolved triangle-contraction case has `e,f` and at least one doubled star edge in one common 2-connected block; and (iii) coordinatewise star-doubling interactions have both signs, so a fixed-sign monotonicity repair is invalid.

## 1. Exact no-go: a union/intersection-preserving pair injection cannot prove FOREST

Take `K4` with disjoint marked edges `e=12`, `f=34`. Consider the product fibre of ordered forest pairs `(A,B)` with

- `A intersect B = empty`,
- `A union B = E(K4)`,
- domain status `(A_e,A_f;B_e,B_f)=(0,0;1,1)`, versus
- target status `(1,0;0,1)`.

Exact enumeration gives

`#domain = 4`,  `#target = 2`.

Thus there is no injection from the Rayleigh-negative product side to the positive side that preserves `A intersect B` and `A union B` (equivalently, preserves every edge's total multiplicity across the ordered pair). This is not a counterexample to FOREST: the full unit `K4` counts are

`(N00,N10,N01,N11)=(15,9,9,5)`

and the full Rayleigh gap is `9*9-15*5=6>0`. The deficit is genuinely paid by other fibres. Therefore a successful forest-pair injection must transport mass across pair-multiplicity fibres, or use an equivalent signed identity; pure recolouring of a fixed union/intersection is impossible already on `K4`.

This is the concrete combinatorial meaning of the negative coefficient in the disjoint-edge multivariate Rayleigh polynomial below.

## 2. Exact weighted K4 signed compensation

Let `Z` be the weighted forest generating polynomial and use the derivative Rayleigh form

`R_ef = (partial_e Z)(partial_f Z) - Z partial_ef Z`.

The weighted event-count Rayleigh gap differs from this by the positive factor `w_e w_f`, so the sign is identical.

### Disjoint orbit

For marks `e=12`, `f=34`, write

`a=w13, b=w14, c=w23, d=w24`.

Direct forest decomposition gives the exact identity

`R_12,34 = ad(1+a)(1+d) + bc(1+b)(1+c) - 2abcd`.      (1)

The coefficient of `abcd` is `-2`, exactly matching the `4 versus 2` fixed-fibre deficit above. Nevertheless (1) is nonnegative for all nonnegative weights. Set

`X=ad(1+a)(1+d)`, `Y=bc(1+b)(1+c)`.

Then

`XY = abcd (1+a)(1+b)(1+c)(1+d) >= (abcd)^2`,

because each `1+x >= x`. Hence by AM-GM,

`X+Y >= 2 sqrt(XY) >= 2abcd`,

which proves `R_12,34 >= 0`.

### Adjacent orbit

For marks `e=12`, `f=13`, put

`p=w14, q=w23, r=w24, s=w34`, `S=1+p+r+s`.

The exact identity is

`R_12,13 = q^2 S^2 + q S(S+2rs) + rs(1+r)(1+s)`.      (2)

Every term in (2) is nonnegative. Since adjacent and disjoint pairs are the only two edge-pair orbits of `K4`, (1)-(2) prove weighted independence correlation of `K4` directly.

## 3. New closure needed by the partner: every parallel extension of K4 is safe

Let `Q` be any loopless multigraph whose simplification is `K4`, with arbitrary positive physical-edge weights. For every parallel class `C` let

`W_C = sum_{h in C} w_h`.

A multigraph forest contains at most one physical edge from each parallel class. Projecting a forest to its used classes is therefore a simple `K4` forest, and summing the physical choices in every selected class gives the exact partition identity

`Z_Q(w) = Z_K4(W)`.

If queried physical edges `e,f` lie in distinct parallel classes, the chain rule gives

`partial_{w_e} Z_Q = partial_{W_[e]} Z_K4`,
`partial_{w_f} Z_Q = partial_{W_[f]} Z_K4`,
`partial_{w_e w_f} Z_Q = partial_{W_[e] W_[f]} Z_K4`.

Hence `R^Q_ef` is exactly the corresponding weighted `K4` Rayleigh polynomial at the class-sum weights, and (1)-(2) make it nonnegative. If `e,f` lie in the same parallel class, no forest contains both, so `partial_ef Z_Q=0` and `R^Q_ef=(partial_e Z_Q)(partial_f Z_Q)>=0`.

Therefore:

**K4-parallel lemma. Every loopless multigraph whose simplification is `K4` is independence-correlated for arbitrary positive weights.**

This is directly relevant to account02/B03's unresolved STAR-2 common-block configuration. Contraction of a triangle creates parallel classes on a star. If the common 2-connected block containing the marks and doubled class simplifies to `K4`, it is safe regardless of which physical copy is marked and regardless of the class weights. The unresolved common block must therefore be strictly more complicated than a `K4` simplification.

Combining this with the established Semple-Welsh strong-correlation result for binary matroids with no `M(K4)` minor gives the sharper structural frontier: a genuinely unpaid STAR-2 common block must have a simplification that contains a `K4` minor but is not itself `K4`. In particular its simple core has at least five vertices. No fixed-graph Cocks globalization is used in this deduction.

## 4. Why this changes the switching target

The `K4` fibre deficit proves that the hoped-for multiplicity-one map cannot stay inside a fixed `(A intersect B,A union B)` fibre. The positive formula (1) shows the smallest exact repair: the negative all-exclusive `abcd` fibre is compensated by fibres in which opposite-channel edges have multiplicity two or zero. Thus a viable global switching must deliberately alter union/intersection while preserving acyclicity, and must pair two crossing channels rather than assign a fixed sign to individual star-doubling interactions. This is consistent with account02/B03's mixed-sign simultaneous-doubling witnesses.

A compact conditional end-to-end route is now:

1. retain the source-valid triangle-free conditioning/minimality argument;
2. in the triangle-contraction quotient, factor off blocks as in account02/B03;
3. use strong correlation for `K4`-minor-free simple cores and the K4-parallel lemma above for the `K4` core itself;
4. on the remaining common 2-connected core (simple core contains a proper `K4` minor), construct a cross-fibre signed switching which transports the negative K4-type all-exclusive multiplicity into the two opposite positive channels, with the outside connectivity state carried as part of the mark.

The first unpaid implication is step 4. A fibre-preserving recolouring is now rigorously ruled out, so the next construction must change pair multiplicities across a K4-minor cell (or use an algebraically equivalent signed flow).

## 5. Exact regression

`k4_cross_fiber_check.py` independently enumerates all K4 forests, reconstructs (1)-(2) coefficient-by-coefficient, verifies the fixed fibre count `4>2`, verifies the full unit gap `6`, and checks the physical-parallel-class collapse on an exact integer-weight doubled-class instance. Output:

- `K4_DISJOINT_NEGATIVE_FIBRE_COEFF -2`
- `K4_FIXED_FIBRE_DOMAIN_TARGET 4 2`
- `K4_UNIT_COUNTS_00_10_01_11_GAP 15 9 9 5 6`
- `K4_ADJACENT_ALL_COEFFS_NONNEG 27 1`
- `PARALLEL_COLLAPSE_WEIGHTED_GAP 340272`
- `STATUS=PASS`

Finite computation is used only as an exact regression for the displayed identities; the K4-parallel lemma is proved symbolically above.

## Status

`ESSENTIAL_STEP_APPLIED`. Parent FOREST remains open. No benchmark/install work, protected control mutation, scheduler mutation, email, Drive, public posting, paid/remote compute, or permission changes were performed.
