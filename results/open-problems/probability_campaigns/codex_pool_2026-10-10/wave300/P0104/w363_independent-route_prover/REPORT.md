P0104 is not solved. I recovered its source as ADH Questions 13 and 15, retained all three branches, and made the exponent and law precise. The original question leaves "suitable conditions" unspecified; current global openness is UNKNOWN after the bounded source checks.

The deliverable is one independent resampling route: an exact variance identity, an edge-forcing sandwich, a proved linear resampling-energy bound for weights 1 and 2 with cheap-edge probability 0.01, and an exact reduction to one missing small-degree spectral estimate. The identities are established mathematics rederived with their assumptions; no novelty claim is made. See ATTEMPT.md and CLAIMS.jsonl.

Measurement command: python -X utf8 ~/brain_workers/w363/verify_finite.py --gate-seconds 60 --max-configurations 128. PASS in 0.174503 seconds: 4 variance identities, 15 gradient correlations, 544 forcing sandwiches, 4 energy bounds, 4 harmonic identities. Two invalid shortcuts are rejected. Before replacing variance by the exact integral, the diamond shortcut gives 1/2; the actual variance is 23/64. A typical-size shortcut gives harmonic mean 1/16; a leaking distribution gives 23/128. These are exact finite controls, not a formal or asymptotic proof.

Risk: the unproved spectral-tail estimate is effectively the exponent problem for this special law. Ties, generic overlap results, other FPP models and unspecified source hypotheses must not be silently identified. The source-only statement was delivered to w364 before the referee packet; audit states and ingestion states remain separate.

Apply: the reviewer should audit the concept draft and its local proofs, then let the validating coordinator ingest the staged bundle. No live code/store patch or global recall change is proposed; do not run integration before review.

NEXT: Bound the weighted low-degree spectral tail F_n(k) for k<=n^(1/3), beginning with pq sum_e(E delta_e T_n)^2; G1 remains unproved.

Draft: ~\math-brain-inbox\w363\bundle_001.json. Five concept cards and four supported relations passed local structural validation. Reviewed, ingested and retrievable remain false.
