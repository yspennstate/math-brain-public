# Same-run verification-timing correction

This file corrects one provenance sentence in `REPORT.md` Section 7. The scientific theorem and all displayed numerical values are unchanged.

Before publication, B13 executed a logically equivalent checker candidate and obtained the output committed in `CHECK_OUTPUT.txt`. The candidate contained two overwritten/no-op assignments that were removed while preparing the committed source, so its bytes were not identical to the final `CHECK.py` bytes.

After the committed `CHECK.py` was read back, B13 reconstructed and executed those exact final source bytes locally. They again returned the identical `CHECK_OUTPUT.txt` output. The exact final checker source has SHA-256

`19f63555523b97ba5df7dd695b0b733dc6d4d392c48658ab610c52a53b38c5de`

and the deterministic output has SHA-256

`a26010d89f993056d11de679a93160e7f53f40f484eb8cb4866ea4818d3615e9`.

Therefore the correct provenance statement is: **the final committed checker bytes were executed locally after readback and reproduced the committed deterministic output exactly**. Do not use the original report's phrase “executed locally before publication” as a byte-identity timing claim.
