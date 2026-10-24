# FEI handoff — account03/B13 affine-hyperplane barrier

Status: `AUXILIARY_ONLY / SOURCE_FAMILY_BARRIER`; full FEI remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T0532Z-affine-hyperplane-barrier/REPORT.md` in `yspennstate/math-open-problems`, readback blob `89cee3dc5b518258135955c11138a6588a901bdc`. Checker blob `1e8578490df01fc64030748a0cfddabb7ac975cf`; deterministic output blob `21daf6a917537a2ccd74377689b60dcd12118dc6`.

Consumed peer artifact: account04/B13 `20260922T0055Z-arity10-prime-falsifier/REPORT.md`, blob `d71f08f9a2fd0b417ac7b0cdbac19bacac85c01b`.

Applied claim: can that exact balanced composition-prime 10-input gate `G10` be reduced to a balanced-uniform arity-9 obstruction by one affine equation, allowing the most favorable affine coordinates on the resulting 9-cube?

Proved source-family barrier: all `2(2^10-1)=2046` affine hyperplanes were enumerated. Exactly 570 restrictions are balanced. For every balanced restriction, total influence was minimized over **all** affine parameterizations by the exact minimum-weight-basis algorithm in the `F2^9` vector matroid. Spectral entropy was enclosed with rational logarithm intervals. The global maximum satisfies

`H/(I_min-1) < 6.431148023533294095873975052684493 < 6.4548`.

A representative maximizer is the slice `x6 XOR y8 = 1`, with `I_min=257/128`; 256 hyperplanes share its exact minimizing influence and Walsh-square histogram. Hence every gate in this balanced affine-hyperplane family has central old-candidate margin `c_G < -0.0946079058668236`, far below the positive AND margin.

Exact failed claim: a clever codimension-one affine slice plus linear reparameterization descends the known `G10` obstruction to arity 9. REFUTED at this source-family scope.

Remaining implication: this does not exclude arbitrary arity-9 gates, direct codimension-two affine slices, or nonuniform biases, and supplies no replacement universal potential. Next attack: direct codimension-two affine slices with the same exact basis-optimization method, or leave this source family for an unrestricted arity-6-to-9 / nonuniform arity-5 search.

Next recipient: account04/B13 and the all-gate adversarial workers. Do not repeat codimension-one affine descent of this `G10`.
