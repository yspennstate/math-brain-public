# fleet03/B06 r51 finite checks

These are sanity checks only; the proof is in `REPORT.md`.

Fixed seed: 51.  Random full-row-rank `3 x n` frames and invertible symmetric `3 x 3` coefficient matrices were tested for `n=6,7,9`.

Representative outputs from the checker logic:

- `n=6`: `Omega3=0.0034547941576393527`; best cut product `0.8426540741349666`; exact expectation lower target `0.08479330268524161`; normalized cross-volume discrepancy `1.1941e-15`; `E_mu delta(H)-Omega3` about `1.2e-17`.
- `n=7`: `Omega3=0.011056111568351987`; best cut product `102.13279066057301`; exact expectation lower target `11.74701414233055`; normalized cross-volume discrepancy `0`; complement-average discrepancy about `1.9e-17`.
- `n=9`: `Omega3=0.15184283443985286`; best cut product `85399.69563124656`; exact expectation lower target `19216.449657939207`; normalized cross-volume discrepancy `1.59e-16`; complement-average discrepancy about `2.8e-17`.

All tested Pluecker masses summed to one within floating-point tolerance. The numerical test is not evidence for the universal density theorem; it only checks the exact finite algebra used in Sections 3, 4, and 7 of `REPORT.md`.

Expected terminal marker from `check_r51.py`: `QFORM_B06_R51_CHECK_PASS`.
