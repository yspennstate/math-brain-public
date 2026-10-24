# PROB20-05 assignment-map artifact provenance

During this checkpoint, the full `k=1` mixed-domino search checked all 3,862 residual permutations and reduced the selected certificates to 723 distinct exact six-tuples `(CSL,CSH,sV,ZL,ZH,ZV)`. The exact tuple set and all radical sign checks are archived in `2026-09-16T02-11-44Z__eleven_bin_domino_exact_check.py` (commit `75c473f6b7be71ff6de276240416dee197cbec7f`).

A later attempt to archive the separate compressed permutation-to-certificate assignment map under `2026-09-16T02-11-44Z__eleven_bin_k1_assignment_map.b85` accidentally wrote only the first 120 bytes of the local 29,264-byte payload. That path is therefore an **incomplete prefix and must not be treated as a certificate or full map**. It is retained append-only rather than overwritten, consistent with the task's no-overwrite rule. Its creation commit is `7b97b30d13b1e6e2ef4a6f7ed5dd5c064530387e`.

The mathematical report does not rely on that incomplete prefix. The substantive archived evidence is: the report, the exact all-`S_11` integer enumerator, and the exact 723-tuple/12-tuple radical checker. The full permutation-to-tuple association was checked in the run but is **not separately archived in full** in this checkpoint; this is a reproducibility gap to close in a later append-only artifact if needed.
