# Independent FEI convolution/product audit

Read [AUDIT.md](AUDIT.md) for the analytic statement-by-statement review and exact source pins. Every substantive theorem in the two scoped packages passed; full FEI and publication novelty remain unproved/unverified.

Run the standalone independent checks with Python 3.10 or later:

    python independent_check.py

Only the Python standard library is required. The explicit input is retained at `product/witness.json`. The script computes Walsh coefficients by direct summation, verifies the two finite entropy gaps with rational logarithm enclosures, reconstructs all 128 translated joint laws and influence identities for the seven-bit witness, and checks 1,056 all-point surgery instances. It writes `independent_results.json` with exact rational endpoints and a hash of the executed script.

The two original verifiers were separately fetched at the report's pinned commits, verified against their Git blob hashes, and replayed without modifications. Their results exactly matched their respective committed JSON outputs. `source_manifest.json` records the original repository paths and verified blob hashes; its `local` field denotes the isolated audit-copy layout, not an additional claim that all source copies are included here.

Finite checks supplement the analytic review; they do not prove any universal FEI inequality. The September 20 provenance of the eleven-variable witness is retained explicitly.
