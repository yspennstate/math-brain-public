# Submitted w394 bundle_002: scoped referee verdict

Read `~/math-brain-inbox/w394/bundle_002.json` after w394 marked `bundle_001` superseded. Six concept entries and five typed relations are present. The underlying w394 claims C01-C06 received individual verdicts in `REVIEW_PACKET.md`; C06 is conditional on the upstream preprint premises. The package may remain draft concept material. Two text fixes are required before ingestion:

1. The anchored-boundary entry says “A finite geodesic attains this infimum.” Under arbitrary positive deterministic lattice weights, existence of a finite minimizer for every pair is not assured. Define the term conditionally: “Call a finite path a geodesic if it attains this infimum; arbitrary positive deterministic weights need not give a minimizer for every pair.” This leaves the event and its reduction intact.
2. The first edge is `refutes` from the partition counterexample to a node whose content already says the fixed-endpoint inference is refuted. The counterexample **supports** that warning; it does not refute the warning node. Change the type to allowed `semantic_association`, with a rationale that explicitly says it illustrates the failed inference.

The other four edges are scoped `semantic_association` links with matching endpoint content. `stage_w394_fix.py` writes a corrected worker-local copy and a small unified diff naming the submitted inbox path. Apply only if the destination still matches the reviewed file. No live inbox edit was made by w395.

Verdict: **FIX bundle_002 before ingestion**. After the two edits, the six concepts and five relations are structurally suitable as draft warning material, subject to the normal second source/edge audit and integrator gates. This is not a theorem endorsement or parent P0117 solution.
