# PROB20-11 — artifact-status correction for the 2026-09-15 run

**SOLUTION STATUS: PARTIAL.**

This append-only note corrects one persistence statement in

`runs/2026-09-15/2026-09-15T161900Z__report.md`
(commit `b0acf1e0c29fd7ab4d83a23f4ae73eff05166000`).

That report says that standalone source certificates for all six K=4 eliminations described there were stored separately under `artifacts/`. At the end of the run, those six standalone source files were **not all durably present** in the repository. The Markdown mathematical writeup itself is durably committed and read back at that commit, but the corresponding six-source-code claim should be treated as a persistence gap rather than as a verified artifact claim.

The later continuation

`runs/2026-09-15/2026-09-15T163000Z__report_part2.md`
(commit `bf8d4d15dd8e1efb7b47fc610ff10f89a1163151`)
was also read back successfully. Its four `3-star + disjoint edge` eliminations **do** have a durable standalone exact certificate:

`artifacts/2026-09-15T163000Z__star_edge_certificate.py`

committed at `c72776377ed35801e78b9fb63e7349a3849a4e1c`, blob `a9dbc0fa94687a3be08d7b8f469e52004a84e627`, and read back successfully at that exact commit.

The cumulative mathematical frontier stated in the two reports is unchanged: the exact bracket remains \(M_{12}\in\{4,6\}\), all K=0,1,2,3 close-pair cases are eliminated, and the corrected K=4 frontier is reduced from 77 canonical classes to at most 66 after the exact eliminations written up in this run. The code-persistence correction affects reproducibility status only; it does not promote or retract any theorem by itself.

**Recovery gap:** reconstruct and persist standalone exact source for the six K=4 eliminations in the 161900Z report before describing those six computations as independently rerunnable from repository artifacts alone.
