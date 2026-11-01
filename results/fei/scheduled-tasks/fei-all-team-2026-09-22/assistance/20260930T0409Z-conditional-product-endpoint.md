# Exact conditional-product endpoint and two-address barrier

Full FEI remains OPEN. These additions extend the verified entropy-wringing package in [draft PR12](https://github.com/yspennstate/math-open-problems/pull/12), head 2591d8acb920ca59230530761efa3113bea2167a. All twelve package files at this head were fetched and compared exactly with the tested/reviewed local bytes. Nine additive files remain on the draft branch; they are not merged to master.

[Complete endpoint proof and exact Boolean barrier](https://github.com/yspennstate/math-open-problems/blob/2591d8acb920ca59230530761efa3113bea2167a/proofnet24/P03-fei/continuations/2026-09-30-entropy-wringing/ONE_BIT_ENDPOINT.md)

## Proved endpoint

Any unit vector of dyadic amplitudes whose squared law is product conditional on one spectral bit satisfies H<=2I. The key norm-arithmetic lemma says every nonzero dyadic product-amplitude vector has reduced odd squared-norm numerator congruent to1 mod4. Two such positive masses summing1 must both be1/2. Each resulting conditional active marginal is fair, with an odd fair-coordinate count. This extends the already archived zero-address rigidity; no novelty claim is made.

## Exact scope boundary

A six-variable Boolean function with two address bits has address masses (5/8,1/8,1/8,1/8), all four conditional laws product, and H=5,I=17/8, ratio40/17>2. Its first projection is the four-bit ternary g with normalized product marginals (1/2,1/2,1/2,1/5); the other three projections are disjoint edge indicators partitioning g's zero set. Thus the constant-two endpoint cannot be extended unchanged to two addresses. Finite collective bounds remain possible, and the general payment in REPORT.md (5.1) remains OPEN.

## Review and computation

The coordinating researcher independently checked the arithmetic theorem and supplied the Boolean two-address construction. The worker independently reconstructed the construction, integer Walsh masses and exact influence vector. check_endpoint.py exhausts all65,812 Boolean functions in dimensions1–4 for the distinguished spectral bit; 4,16,96,2176 functions respectively satisfy the conditional-product premise, with no biased conditional marginal. The exact six-variable witness was verified separately. The checker and output are on the draft branch, with ENDPOINT_MANIFEST.json; all scripts passed py_compile. No formal certification or publication-priority claim.
