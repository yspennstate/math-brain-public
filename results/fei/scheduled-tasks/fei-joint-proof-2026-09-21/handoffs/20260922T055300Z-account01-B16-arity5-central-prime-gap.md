# account01/B16 FEI handoff — arity-five central prime gap

Status: `ESSENTIAL_STEP_APPLIED`; full FEI remains `OPEN / NOT PROVED`. Execution: `WITHOUT_VERIFIED_BRAIN`.

Source-bound scientific package:
`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T053717Z-arity5-central-prime-gap/REPORT.md`
(report blob `0ebb4f09053461b185e9432401d06c88f5ed68ba`). Checker blob `3e1b91a41155399a76339b9fe444b316b74948c4`; output blob `363a9044a8c29afd1818b90408c7d02d7de3a067`.

Consumed exact other-account input: account02/B17 `20260922T004442Z-gate-composition-cocycle`, which proves gate slack and Poincare currency compose with the same nonnegative weights, hence normalized margin is a convex average of factor margins.

New theorem, using the exact account01/B17 five-input uniform certificate: for every output cardinality `m`, every exact minimizer of the certified central objective `6.4573 I-H` is cube-automorphic to B17's explicit read-once comparator. For `m<16` every such minimizer has a binary AND/OR two-coordinate inner factor; `m=16` gives only literals. Therefore no essential composition-prime five-input gate ties the central objective minimum.

Quantitative margin conversion: for every strict five-input table with positive Poincare currency `M`,

`D_{Gamma_.01}/M >= 2453251107/47363281250 = 0.0517964769807835...`.

Since `D_{Gamma_.01}=D_{Gamma_RO}+0.01 M`, every essential composition-prime five-input gate at uniform bias obeys

`c_Gamma_RO <= -3959236589/94726562500 = -0.0417964769807835...`.

Thus every nonnegative-margin extremizer on the complete five-input uniform-center slice is necessarily decomposable. By finiteness and continuity, a common open neighborhood of the center is also safe for all essential five-input prime gates, though this run does not quantify its radius.

Next exact obligation: leave the center. Prove decomposable extremality for all nonuniform five-input product biases, or construct a genuine composition-prime five-input bias counterexample. Higher arities remain open. Do not treat this slice theorem as full FEI.
