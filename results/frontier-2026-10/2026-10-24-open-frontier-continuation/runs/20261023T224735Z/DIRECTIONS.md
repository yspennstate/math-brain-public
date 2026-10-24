# Continuation after the finite-orthonormal-input theorem

## Closed within this exact model

The later-switching gap left in run 20261023T222120Z is now closed for every fixed finite orthonormal training set in fixed dimension, continuous-time two-layer iid-stable ReLU training, and the specified absorbing selection. The all-phase sensitivity energy and Sard argument replace the two-dimensional cone restriction. The scalar critical-step GD gap is also closed for h_m=gamma/(log m)^(1/alpha), including fixed-grid boundary and macroscopic limits. Do not rederive these scopes as new results.

## Next unpaid obstruction: nonorthogonal inputs

For a nonorthogonal input Gram matrix G, the projected equations have the form

V_ij'=beta_m W_i sum_l G_jl r_l 1{V_il>0}.

Even when V_ij=0, another active gate can move this projection. A previously inactive projection can activate. Therefore neither independent projected-coordinate absorption nor monotonicity of the initial-square alive clocks is inherited from the actual gradient flow. The Helly proof and the irreversible diagonal-population rule cannot simply be reused. Establish the correct finite-width boundary convention and coupled endpoint dynamics first; retain a genuinely nonorthogonal pair as the smallest test case.

A useful first derivation is an endpoint with W_i/a_m -> z: the hidden displacement has order L_m and its scaled trajectory should respond to the residual through a piecewise-linear vector field. Initial marks choose a sector at the origin. Proving existence, uniqueness/selection, and dependence on those marks for that coupled limiting field is an unpaid singular-initialization problem. No such limit is asserted here.

## Other unpaid tasks

1. Multi-input discrete GD with steps comparable to the initial switching scale, particularly overshoots across several coupled activation boundaries. The reviewed scalar hyperbolic clock relies on a scalar residual sign and does not prove this case.
2. Quantitative rates for the orthonormal hybrid theorem: control initialization coupling, random small residual margins, and distances to grazing/collision exceptional sets. An O(1/L_m) gate threshold is not an O(1/L_m) error in the macroscopic switch time.
3. Test-input predictions and an exact definition of feature learning stronger than training-kernel motion. Nonfreezing alone does not establish generalization improvement or a full learned feature distribution.
4. Deep networks and their correct ReLU normalization. The catalog asks a broader question than the shallow model treated here.
5. A kernel path topology through aggregate jumps. L1 is proved. J1 cannot be inferred from coalescence of several finite-width jumps; M1 or graph-based convergence would need its own argument.

## Failed routes and repaired steps retained

- The two-input mixed-sign cone cannot be used for k>=3: the explicit deterministic three-input example has two removals.
- Applying first-stage genericity afresh after conditioning on a random previous switch would be unjustified. The new parameter-chart sensitivity/Sard argument is what pays this dependence issue.
- Claiming absolute O(1/L_m) switching-time accuracy from a gate threshold was too strong without a rate for the cumulative residual; this was corrected.
- The finite-width kernel cannot be treated as constant after the initial layer for general orthogonal rotations; the prior counterexample remains valid and is now explained by the full hybrid law.
- Fixed critical-step held Euler boundary paths differ from continuous boundary paths between grid points. The macroscopic scalar limit nevertheless agrees, by the exact secant identity and one-time charging of each crossing.

Preserve all explicit absorbing-flow, iid-coordinate, fixed-dimension and normalization assumptions. Full T384 stays OPEN. If the nonorthogonal singular-initialization route remains unchanged after repeated substantive attempts, switch mechanism or move to another verified-open row rather than repeating the orthonormal theorem.
