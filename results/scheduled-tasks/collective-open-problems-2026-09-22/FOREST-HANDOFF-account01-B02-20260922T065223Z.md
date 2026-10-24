# FOREST handoff — account01/B02 — 20260922T065223Z

Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent FOREST: `OPEN`  
Context: `WITHOUT_VERIFIED_BRAIN`  
Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B02/20260922T065223Z-b02-forest-auto11-cont/report.md`, blob `f618a531fd59dffd8848d2b70cae7a3029340e29`.

## Named partner consumed

Applied account02/B03 `20260922T061345Z`, shared blob `4c17f361f23133c2048906f198e84eefc9904b63`: global STAR-2 is parent-hard; after block factorization the unresolved triangle-contraction case has the two marks and a doubled star edge in one common 2-connected block; coordinate star-doubling interactions have both signs.

## New exact no-go for the injection design

On `K4` with disjoint marks `e=12,f=34`, the fixed product fibre

`A intersect B=empty`, `A union B=E(K4)`

contains 4 negative-side pairs `(00,11)` but only 2 positive-side pairs `(10,01)`. Therefore no forest-pair injection preserving union/intersection (equivalently every edge's total pair multiplicity) can prove FOREST. This is a genuine exact obstruction, not a parent counterexample: the full unit counts are `(15,9,9,5)` and the total Rayleigh gap is `6`.

## Exact K4 signed compensation

For derivative Rayleigh `R_ef=(partial_e Z)(partial_f Z)-Z partial_ef Z`:

- disjoint marks `e=12,f=34`, with `a=w13,b=w14,c=w23,d=w24`:

`R_12,34 = ad(1+a)(1+d)+bc(1+b)(1+c)-2abcd >= 0`.

The coefficient `-2` is exactly the 4-versus-2 fixed-fibre deficit. Positivity follows from AM-GM because the product of the two positive channel terms is at least `(abcd)^2`.

- adjacent marks `e=12,f=13`, with `p=w14,q=w23,r=w24,s=w34`, `S=1+p+r+s`:

`R_12,13 = q^2 S^2 + q S(S+2rs) + rs(1+r)(1+s) >= 0`.

Thus weighted `K4` is proved directly.

## New K4-parallel lemma

Every loopless multigraph whose simplification is `K4` is independence-correlated for arbitrary positive weights. Collapse each parallel class `C` to class weight `W_C=sum_{h in C}w_h`. Forests use at most one physical edge from a class, hence `Z_Q(w)=Z_K4(W)`. For marks in distinct classes the derivative Rayleigh polynomial is exactly the corresponding weighted-K4 polynomial; marks in one class have zero joint term.

Applied to the partner's STAR-2 common-block reduction: if the unresolved common 2-connected quotient block simplifies to `K4`, it is safe even when a queried edge is one physical member of a doubled class. Together with the established strong-correlation result for `K4`-minor-free binary cores, the unpaid simple core must contain a `K4` minor but not equal `K4` (hence at least five vertices).

## First unpaid implication

The next switching cannot be a fixed-fibre recolouring. It must transport pair multiplicity across a proper `K4`-minor cell while carrying the outside connectivity state, reproducing the two-channel compensation in the disjoint `K4` identity without losing acyclicity or multiplicity control.

Exact checker/output are in the canonical run; output terminates `STATUS=PASS` and verifies the two formulas, fibre `4>2`, unit gap `6`, and a physical parallel-class collapse instance.
