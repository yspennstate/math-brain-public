# Probability proof audit — 30 September 2026

## Result

Recovered, reconstructed, and independently audited the repository's September 16 full-scope candidate answer to Hasebe–Ueda Problem 3.11. The proof classifies freely strongly unimodal laws as exactly the Dirac measures, without moment assumptions. The present improvement is a fixed unimodal witness with atom weight 1/32 instead of 1/1000, and an exact first-order comparison margin of 9/100.

The mathematical audit passes after two explicit analytic exposition repairs: a common canonical inverse cone fixes the high anchor uniformly, and interior identification followed by the identity theorem avoids an unjustified boundary-convergence inference. See the reconstruction's Section 5 and the independent audit's Section 4.

This is a **recovered full-scope proof candidate with independent mathematical audit and a sharpened witness**. It is not a claim of a newly discovered classification, certified publication priority, formal verification, or journal acceptance. Original reports and their historical status remain unchanged. The September 30 reconstruction is the version reviewed here.

## Files

- [Full proof reconstruction](FREE_UNIMODALITY_RECONSTRUCTION.md)
- [Independent analytic audit](AUDIT.md)
- [Ranked candidates and source-status checks](CANDIDATES_AND_STATUS.md)
- [Exact rational checker](check_witness.py) and [actual output](witness_check.json)
- [File hashes](MANIFEST.json)

Run `python check_witness.py` for the finite constant certificate. It is intentionally not a formal verification of the complex-analytic proof.

## Famous targets remain open

The unrestricted Fourier entropy–influence and Benjamini–Schramm nonuniqueness conjectures remain unsolved in this package. The selected Hasebe–Ueda question is narrower and less famous, but had the strongest concrete route to an end-to-end rigorous deliverable. The candidate report also records a precise September 2026 primary-source overlap for the repository's plateaued-FEI constant-four result; stronger refinements require separate comparison.
