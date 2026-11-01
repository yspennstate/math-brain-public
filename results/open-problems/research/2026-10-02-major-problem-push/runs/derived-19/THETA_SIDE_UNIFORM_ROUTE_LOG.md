# Route log: the first theta block

## Route A: direct real-stability certificate — success

Exact enumeration exposed four pair orbits for side activities `p,q`.
Treating each Rayleigh difference as a quadratic in one remaining variable
produced factorized discriminants. After the internal-variable shift by
`p+q+1` and the endpoint shifts by `3p+1,3q+1`, every residual factor is a
two-variable positive-definite quadratic form. This yields the complete proof
in `theta_uniform_apex_stability_proof.md`.

## Route B: profile-ray root search — useful evidence, then superseded

Random real evaluations of the unweighted five-variable Rayleigh
differences found no negative value. This did not prove stability. It was
used only to choose the exact symbolic calculation, which then superseded
the numerical evidence.

## Route C: two-terminal determinant gluing — unresolved

The cactus proof normalizes the single shared vector to a universal
one-dimensional Gram block. For a two-terminal network, the normalized
Gram block also contains an off-diagonal terminal correlation depending on
the network. Parallel gluing therefore does not follow from the cactus
Schur-complement argument. No valid closure theorem was inferred.

## Route D: increasing the weight generality — partial success

The first exact proof used one common activity `t`. Replacing it by `p` on
the three edges at one endpoint and `q` on the other preserved the internal
`S_3` symmetry. A second derivation proved this larger two-parameter family.
Six independent activities make the expressions much larger and destroy the
four-orbit reduction; they remain a concrete next target.

A deterministic numerical search then tested 120 unrelated six-weight
vectors, all ten spoke-pair Rayleigh differences, and 30,000 real
specializations per pair (36,000,000 evaluations). It found no negative
value. The smallest value was about `1.03e-6`. This is finite floating-point
evidence only, not a theorem and not a substitute for an SOS or exact
counterexample.
