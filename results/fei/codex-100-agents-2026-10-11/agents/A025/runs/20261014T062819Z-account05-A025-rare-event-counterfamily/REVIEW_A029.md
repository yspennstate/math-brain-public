# Independent artifact-scoped review: finite-label bank conservation

Source: A029 run20261014T055200Z DERIVATION.md, section “Multi-state
boundary bank through physical mixed histories”. HOLDS at that scope.
No blanket acceptance of its sharp compression, entropy sufficient
condition, earlier claims, or source computation is asserted. No repair
is supplied. This is an artifact-scoped review; no source claim ID is
invented for the addition.

For each actual data edge let r_j be its core pivotal indicator. A product
gj*gk flips iff r_j XOR r_k=1. With physical label probabilities pi and
q=sum pi_j r_j, summing independent two-label draws gives
sum_(j<k) pi_j pi_k (r_j XOR r_k)=q(1-q). Therefore
R=2 sum_i E q_i(1-q_i). This is equality, not a sum-of-core upper bound.

At a fair controller query, q=(q0+q1)/2, and direct subtraction gives
R-avg Rchild=(1/2)sum_i E(q0-q1)^2. At a data query i, label probabilities
do not change; the other directional product influences telescope across
both actual data children. The removed contribution is exactly
2 E q_i(1-q_i). Jensen yields <=2d_i(1-d_i). Every adaptive physical
history fixes queried bits, leaving independent uniform unqueried data
and control cubes; hence these identities apply at every node. Summing
with physical reaches proves Rroot=sum reach*release+E Rleaf. At resolved
labels the bank is zero while core entropy can remain. A fixed root
multiplier is permitted; replacing it in a selected child requires pricing
the change. This reconstructs the source's scope without a terminal reset.

Independent actual Boolean reconstruction in this run checks the bank
and release at six non-flat three-core roots, including common point
activation and both actual x children. Independent scalar edge profiles
are checked in out/REPLAY_RESULTS.json. The all-dimensional argument is
the exact edge variance and physical conditioning above, not finite
validation. No A029 helper or result is imported.

The new family in PROOF.md preserves these equalities. It refutes only
an added local entropy-price rule based on released R and query influence
without inherited child surplus. Conservation is accepted, entropy
payment is not inferred from it. The logarithmic price obstruction is
thus a downstream condition, not a source error.
