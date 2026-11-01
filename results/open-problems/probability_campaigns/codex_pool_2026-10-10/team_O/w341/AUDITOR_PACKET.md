Auditor: w347 (gpt-6-luna). Proposer: w341. Manager: claude-4a88bc43.

For the blind pass, first read CLAIMS_FOR_BLIND_AUDIT.json and the original problem statements in reports/assigned_ledger_rows.json or reports/resolved_targets.json. Derive an independent verdict before opening the corresponding proofs/ report. Then check that report and the source passages it cites. No independent KEEP is currently recorded.

Write verdicts in your own folder, suggested path audits/w341.jsonl, one row per claim: {"problem", "key", "verdict": "KEEP"|"FIX"|"DROP", "why", "label"}. A KEEP of a finite certificate is not a KEEP of a general conjecture. For a FIX, provide the corrected statement and failed hypothesis. This handoff is by disk because the worker brief forbids mesh sends and live writes.

| Problem | What to check most closely | Proof report |
| --- | --- | --- |
| P0288 | Spectral boundary branch, zero atom, signed inversion, lambda-transience, positive minor; prior-art still unverified | proofs/P0288_recheck.md |
| C0034 | Capacitated Hall direction, second marginal, rank-one domination reduction; exact higher-rank replay | proofs/C0034_rank_two.md |
| C0151 | Fresh auxiliary labels, supremum versus attained endpoint, conditional large-d gap; primary literature lead unverified | proofs/C0151_thinning.md |
| P0127 | Rooted n-vertex convention, growth-history multiplicities, TV=1/6 and line complexity | proofs/P0127_growth_bias.md |
| P0456 | Shared edge weights, 2n-3 count, finite versus asymptotic obstruction | proofs/P0456_finite_calibration.md |
| C0058 | Vertex incidence identity; configurationwise obstruction does not prohibit weak lumping under a special law | proofs/C0058_boundary_identity.md |
| C0082 | Equal degree D=2d, unoriented rooted cycles; cycle counts are not lace coefficients | proofs/C0082_cycle_counts.md |
| C0126 | Undirected walk on oriented cluster, two-step return and disjoint-cut energy bound; random tails unproved | proofs/C0126_walk_direction.md |
| P0014 | Trace/eigenvalue normalization, even frequencies, exact small cases; float LP checks and tail gap | proofs/P0014_fourier.md |
| P0042 | Largest core fixed point, critical endpoint, root vacancy 21/32 and ergodicity | proofs/P0042_tree4.md |

Reproduction: copy checks.py and higher_rank_certificates.py into a new directory inside your own worker folder and run `python -X utf8 -B checks.py` followed by `python -X utf8 -B higher_rank_certificates.py` there, so generated measurements stay in your authorized folder. Inspect the original certificates using a separate Fraction/Gram-determinant calculation if possible. Original files are measurements/C0034_certificates.jsonl (64) and measurements/C0034_higher_rank_certificates.jsonl (8). No machine test bank is involved. The Lean receipt is unavailable, not a passed formal proof.

The drafts/ folder holds ten complete draft files. All 35 claims, including their dated status records, remain pending. Deployment and store mutation are reserved to the reviewer. No general problem may be marked newly solved merely because a numerical batch or algebra check passed.

NEXT: record blind verdicts before reading the proof reports, then check the proofs and replay certificates.
