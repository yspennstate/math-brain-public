# Research outcomes and failed routes

18 September 2026. This is a record of mathematical attempts and their outcomes, not an assertion of continuous compute, an independently audited proof, or a replacement for the source reports.

## Sidorenko

**Change representation / freeze one spectral direction.** Reconstructed the leaf-free edge-subset polynomial. Repository comparison showed that the full rank-two theorem and sharp skewness envelope were already proved by C30. These are credited as inputs, not counted as new.

**Differentiate a parameter / find the extremal object.** Instead of asking only for positivity, normalized the skewness by its exact feasibility envelope and differentiated the graph polynomial. A strictly positive 65-coefficient Bernstein certificate proves monotonic decrease in normalized skewness. This identifies the exact two-block extremizer at each negative eigenvalue. A second certificate gives the sharp sixth-order remainder.

**Try to combine directions.** Positivity of the whole kernel does not imply positivity of its spectral truncations. An exact three-block example proves this. A further search produced two separately admissible directions for which adding one decreases the graph density, and their combined slack is smaller than the sum of individual slacks. The exact fractions, not the numerical search, are the retained certificates. These failures rule out two proposed extension mechanisms, not the graph conjecture.

**Full-rank transfer route.** The existing triple-moment/reflection-operator reduction still leads to an odd trace with possible negative spectral contributions. No general lower bound was obtained from positive-semidefiniteness of the auxiliary block operator alone. The mixed third-moment tensor remains uncontrolled. No arbitrary-rank theorem is inferred from the rank-two extremizer.

## FEI

**Read and repair the reduction.** Compared the final handoff to its underlying proof. The handoff's pointwise H<=B+cI statement is false, while the global-constant comparison and universal implication are valid. Preserved an exact addressing/parity-lift counterexample and supplied the correct hereditary pointwise replacement.

**Move to coding theory / amplify before lifting.** A parity lift alone gives only the previously observed factor-two comparison if used crudely. Tensor amplification makes its additive influence overhead negligible. A systematic linear code extends this observation to every fixed erasure-block size, preserving the full optimal FEI constant. The written union-bound proof also permits growing block sizes o(N/log N).

**Attempt local-to-global closure.** Vanishing spectral erasure entropy, even on growing blocks, does not isolate an easier FEI class. The coding theorem proves that the full difficulty remains. It does not invalidate a hereditary physical-restriction proof, since restriction can break the code. No universal bounded-coherence decomposition or uniform leaf theorem was found; those hypotheses were not assumed away.

## Ising

**Compactify and solve the support optimization.** Explicitly parametrized the moment body's frontier using the decreasing ratio tanh(x)/x and saturated threshold profiles. Derived a support-slack entropy estimate, without asserting it resolves the interior maximum.

**Use the exact fixed point before bounding the tail.** Gaussian integration by parts cancels the large s^2 term, isolating the linear moment functional c(a). A global Mills-type majorant yields the known excluded half-body. Reading Huang Section 7.4 then identified Lemma 7.17 as the antecedent; that qualitative conclusion is explicitly marked as rediscovery.

**Make the analytic exclusion quantitative.** Elementary rational Gaussian bounds give D>1/15. One fixed tilt, s=1024, then proves a strict margin less than -1/15 on c(a)<=1/230400. This adds a usable positive-width collar under the explicit source parameter/fixed-point hypotheses, rather than asserting a new qualitative half-space theorem.

**Replay boundary.** Inspected the full certificate driver and rederived the geometric implications of the four stored star-interior packets using exact rational interval arithmetic. The Gaussian integrals and all 1404 Region-I jobs were not rerun. The absence of python-flint in the working environment and a failed fresh-download route were recorded rather than replaced by a false full-reproduction claim.

## Disposition

Retain the new proofs, exact examples, and explicit remaining obligations. No full Sidorenko or FEI closure, no new full capacity validation, no independent audit count, no task rotation, and no public release follow from this continuation. First-priority status of the added statements is unverified.
