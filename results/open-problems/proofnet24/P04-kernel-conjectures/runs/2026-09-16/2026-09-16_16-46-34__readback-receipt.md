# P04 immutable readback receipt — 2026-09-16 closure run

Status: `COMPLETE_READBACK_VERIFIED`

Canonical report:

`proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_16-46-34__run-report.md`

Creation commit: `f98f204e905acafc503548ba0214a24ece5506d6`  
Verified report blob: `dbb870bbb33ee6826866ebf90042ae96cb320c47`

Exact-commit readback reached the terminal marker:

`**End of complete run report.**`

The readback confirms the frozen P04 audit metric `1 -> 0`, both independent OTHER PASS audits, the closure-package paths and hashes, retirement of the personal kernel finishing scope, and the create-only outside handoff to `I0101`.

Additional exact readbacks completed in this run:

- `paper_target1_squared_ridge/target1_symbolic_checker.py` at creation commit `ad8da455c2eda1229cbcae657c99743bb5d4947c`, blob `0620f60a11a991698c338d23734217c7bec26330`;
- `paper_target1_squared_ridge/target1_symbolic_checker.out` at creation commit `22f070e1d05a8665bb93a2c6fd9cb8163086ad57`, blob `8934287e9e3b145fe278da07ff9ab7cc296addad`, containing `EXACT_SYMBOLIC_CHECK=PASS`;
- corrected canonical `paper_target1_squared_ridge/target1_squared_ridge.tex` at commit `aa1fd9c8df58c57cd3e4a90505807a4eacaf5ec9`, blob `195ba7d425600db0cdb9c5d1926b9fffa60a51df`; a focused readback confirmed the corrected Hermite `k \mathrm{odd}` expressions;
- `paper_target1_squared_ridge/README.md` at creation commit `7f42987410ea2e6ced3e481025a48d6c8a846dfe`, blob `feb5636907455b118d9012e4fe9c430aecbd05c2`;
- exclusive outside handoff claim `operations/claims/I0101.md` at creation commit `7617b2f33e2adb4a9030e9a98a4898fafd0e9547`, blob `219beba05bea819cb0233ca0aaa78fc25faa8ec0`.

The first TeX write had a local transport defect in the token `\rm`; it was corrected before closure by replacing the package file in place. No immutable historical run report was edited, and the correction changed no theorem, hypothesis, audit result, or mathematical dependency.

No root shared ledger was edited by P04; the canonical report requests P26 to reconcile packaging/retirement and the new outside assignment on its next ledger pass.
