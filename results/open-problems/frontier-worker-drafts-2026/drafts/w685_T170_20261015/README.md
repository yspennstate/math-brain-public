# T170: unique-height renewal draft (w685)

Status: **proof (unaudited)**. The proposed Exp(1) FPP diagonal bound is **mu_diag(21) >= 0.073881518494** in Euclidean units. This archive makes no claim of independent proof approval, verified novelty or a newly certified non-ball dimension.

Start with `proofs/unique_height_renewal.md`; section 4 is the all-length decomposition requiring particular scrutiny. Separate scalar, norm and outward-rounded contraction certificates have their own scopes.

Reproduce on Windows with Python 3.14 and NumPy: `python -X utf8 scripts/run_height_renewal_certificate.py`. The positive vector is supplied as an arbitrary witness, not assumed to be an exact eigenvector. The runner checks producer exits and pins artifacts in `logs/height_renewal_delivery_manifest.json`. The saved clean run passed all computational checks, sequentially and below normal priority, with estimated peak memory below 400 MB. These checks do not replace mathematical review.

`CLAIMS.jsonl` contains only the four exact-version unaudited claims in this slice. `bundles/bundle_003.json` stages four owner-work concept drafts; no live brain ingestion is implied.
