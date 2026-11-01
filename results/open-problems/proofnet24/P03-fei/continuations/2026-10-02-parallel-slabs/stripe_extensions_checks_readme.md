# Reproduce the slab, union, chain, and obstruction checks

Requirements: Python3 with NumPy. All checkers use only the standard library and NumPy, except the three-crossing checker, which needs only the standard library. No secret, service credential, external API, or unrelated research helper is used.

Run from the directory containing the scripts:

```sh
python stripe_extension_verify_parallel_slabs.py
python stripe_extension_verify_union_and_chains.py
python verify_three_crossing_obstruction.py
```

The first checker passed3,846nonconstant parallel slabs through dimension12, including2,184narrow and1,662wide cases. It verifies signed stability, low-degree bounds, pair-spectrum tails, empty-atom handling, data-processing direction, and the finite dyadic KL comparison. The existential Keller--Klein constant is not assigned a numerical value: the script uses a measured reciprocal only to stress-check the algebraic conversion, and the proof uses the actual universal theorem constant.

The shared union/chain checker passed3,200unions,616functions and47,172maximal-chain permutations. It verifies the union entropy estimate, exact joining-edge cancellation term, expected comparator influence, disagreement identities, and the stronger orthogonal-projection energy identity. Its original simpler count-k entropy assertions are finite sanity checks. The maximum-run/deficit improvement has a separate analytic proof and independent audits; no asymptotic theorem is inferred from the sample.

The three-crossing checker passed40odd values3<=N<=81. It verifies exact rational majority coefficients, directly enumerates Boolean encoding at small N, and computes local entropy increments at100-digit Decimal precision. This avoids catastrophic cancellation when alpha=2^-N. The asymptotic lower bound is proved analytically in the accompanying note; the finite data alone do not prove divergence. This construction refutes a largest-weight local proof criterion, not FEI.

`stripe_endpoint_equality_counterexample.json` is an exact four-row rational truth table: at interval width2w, largest-coordinate influence1/2 differs from the sum3/4+3/4 of the crossing influences. It documents the repaired strict-separation scope. The final arbitrary slab theorem remains valid by its narrow/wide split.

All author drafts, repaired proofs, independent audits, failed endpoint claim and exact certificate are preserved. Floating-point entropy evaluations are corroborating tests, distinct from exact rational combinatorial identities and analytic proofs. Script-generated JSON files are deterministic under their fixed seeds.
