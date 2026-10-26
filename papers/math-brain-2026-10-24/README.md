# Math Brain: Shared, Auditable Memory for Multi-Agent Mathematical Research

Revised 26 October 2026. The directory name is retained to preserve existing links.

`math_brain.pdf` is the current paper. Its original text, figures and tables are open access under [CC BY 4.0](LICENSE.md); the source-package code is MIT-licensed. No fee, account or individual permission is needed to read or download it.

Build with `latexmk -pdf main.tex`. The source incorporates the 25 October three-arm results and compaction appendix. It corrects the release/licensing section and related statements throughout the paper.

- `scripts/check_release.py`: verify the public export's file hashes, counts, row digests, foreign keys and SQLite integrity.
- `scripts/mcnemar.py --power`: recompute exact paired p values, smallest significant splits, Holm corrections, and planning power from the reported aggregate counts.
- `release_integrity.json` and `paired_statistics.json`: the checked outputs.
- [RELEASE_REVIEW.md](RELEASE_REVIEW.md): verified results and the remaining private-store, privacy, source-rights and benchmark review requirements.

This is a corrected open-access edition. It does not certify that every condition for the entire release has been cleared, nor does it add an independent mathematical referee review of all cited papers.
