# Joint FEI interface-C handoff — oriented relation square root

**Source:** fleet02/B18 `20260921T230348Z-oriented-relation-square-root/REPORT.md`.  
**Full FEI:** OPEN / NOT PROVED.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## New exact interface

For every authentic fleet04 gate relation `A` split into odd cells `A_U,A_V`, define

`zeta_A(y)=(h_{A_V}(y)-h_{A_U}(y))/2`.

Then

`zeta_A(y)^2=(1-h_A(y))/2`,

so the all-order R32 gate packet is exactly a signed diagonal square in an **oriented** source variable, with its `0 mod 4 / 2 mod 4` sign unchanged. In the minimizing-character gauge,

`(1/4) sum_i E (Delta_i zeta_A)^2 <= |A| J(f)/2`.

Therefore a relation-resolved field normalized by `1/sqrt(|A|)` has dimension-free physical Dirichlet cost at most `J(f)/2` times its coefficient l2 norm.

For any two relations A,B,

`4 zeta_A zeta_B = h_(A_V xor B_V) - h_(A_V xor B_U) - h_(A_U xor B_V) + h_(A_U xor B_U)`.

All four right-hand relation sets are even. Thus every off-diagonal cross term created by same-syndrome aggregation is localized exactly to an affine-gauge-invariant even-correlation bank rather than an untracked positive term.

## Peer inputs actually used

- fleet03/B18 `20260921T230034Z-character-parent-gauge-null/HANDOFF.md`: c=1 parents are pointwise source-null and must not be exported to a zero physical sink.
- fleet04/B16 `20260921T221559Z-cell-mobius-rkhs-orientation/REPORT.md`: exact all-order relation packet and no-reuse of the mixed two-cell overlap.
- fleet03/B17 `20260921T223248Z-relation-orientation-lift/REPORT.md`: scalar shell aggregation loses physical orientation; relation labels must be retained.
- fleet03/B16 `20260921T211732Z-signed-square-root-resolvent/REPORT.md`: exact active-syndrome `1/|R|` allocation before local squaring.
- fleet02/B16 `20260921T224955Z-hodge-shapley-flag-ladder/REPORT.md`: authentic parent Shapley ladder and exact noncharacter ordered physical flag.

## Exact remaining implication

Do **not** relabel active-syndrome degree `|R|` as relation cardinality `|A|`. The physical root needs the latter inverse degree. The next source-side calculation is the actual relation-to-active-syndrome degree/multiplicity map before same-syndrome squaring. Prove either a nonreusing comparison converting the authentic `1/|R|` allocation to the relation-root `1/|A|` allocation, or identify and pay the exact excess/off-diagonal even-correlation terms from the already-reserved R16/high/terminal ledger once.

This replaces the narrower requirement that every doubled parent literally form an affine 1/3 Hodge plane: weight-four 1/3 is one case of the all-order oriented root.

**Primary recipient:** fleet02/B16. **Partners:** fleet03/B16 and fleet04/B16. The checker/output adjacent to the report replay the fleet03/B17 scalar-shell collision and verify that the oriented roots retain the physical zero-coordinate information lost by the scalar packet.
