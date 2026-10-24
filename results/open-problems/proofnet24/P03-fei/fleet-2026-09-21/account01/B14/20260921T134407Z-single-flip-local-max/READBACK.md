# B14 exact readback and hash correction

The mathematical statements in `REPORT.md` are unchanged. This note supersedes only the two artifact SHA-256 strings written into that report before exact repository byte readback.

- `single_flip_rigorous.py`: Git blob `58db62e96c9f62b40e15e49b71bee2ba98a0bfb7`; SHA-256 `ffeb4c99d872d1401b8b7ac9c93af49102292b5c35593bc1867e9bc7ef8476ac`.
- `single_flip_rigorous.json`: Git blob `e27ba55140990d5ded90b0cf2413ed5ff9303cc6`; SHA-256 `4c44e9137b081178938fc810ba37a8a37a105a036603874a338842c5da9fe033`.
- Complete executed 45-orbit stdout: SHA-256 `5d992897247e5eaab7b1b1b48903f30ad86a8cd6f6b1bb8d7f1246677b513c70`.

The committed script differs from the locally staged executed source only in one explanatory docstring (`1 <= y <= 2` instead of `1 <= y < 2`); the executable statements are identical. The exact committed bytes were re-executed after readback and produced byte-identical stdout with the SHA-256 above.

The compact JSON records `orbits_evaluated=45`, the strict exact-Fraction comparison flags, the baseline interval, the certified best one-point flip, the best non-top upper bound, and the stdout digest. Full FEI remains OPEN.
