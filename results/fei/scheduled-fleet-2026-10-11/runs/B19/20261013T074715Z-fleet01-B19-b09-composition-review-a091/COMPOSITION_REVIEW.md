# A091 composition review verdict

The B09 physical-block identity and Maassen--Uffink repair are accepted for all finite Boolean functions under interior product measures.  The repaired two-bit AND certificate separately accepts the finite refutation of `J_A<=M_A`.

Composition scope is narrower than the prose in B09 section 5 suggests:

- `M`, `J`, and `Delta` add for exact disjoint products/tensors with aligned revealed blocks.
- They do not add through a general nonlinear Boolean outer gate; AND of two uniform dictators already changes the base totals `(M,J)=(0,0)` into `(1,1)` when one input is revealed.
- O'Donnell--Tan composes the normalized biased `FEI+` functional, including the outer-gate term at induced biases.  It does not directly compose the B09 `M,J,Delta` ledger.

The endpoint-order assertion had a logical gap in the original report.  A new genuine Boolean AND family repairs it:

\[
J-M=4q(1-2q)p\log_2(1/p)+O(p),\qquad 0<q<1/2.
\]

This new repair requires a fresh independent review because B19 contributed it.  Full FEI remains open.
