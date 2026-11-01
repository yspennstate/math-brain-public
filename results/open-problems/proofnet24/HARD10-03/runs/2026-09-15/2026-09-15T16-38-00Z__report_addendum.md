# HARD10-03 run addendum — certificate receipts

**SOLUTION STATUS remains: PARTIAL.**

This append-only addendum records the optional finite-state certificate created after the full mathematical checkpoint

`proofnet24/HARD10-03/runs/2026-09-15/2026-09-15T16-21-30Z__report.md`

(commit `08ed8566574ffe9a49dc69491c102f429f4778bc`). The main report was read back at that exact commit before these computations were added.

## Certificate code

Path:

`proofnet24/HARD10-03/artifacts/2026-09-15T16-33-00Z__cycle_hitting_forest_check.py`

Commit:

`5d3655711eb03c29bf4a437de2ee5890524161ee`

Readback blob:

`86ed5d60746c2148d6d298bbc6feb0b8da4b9562`

The script completely enumerates the interchange semigroup on the four-cycle `C4` and checks, at physical time `t=0.7` and independent Bernoulli marking probability `r=0.23`:

1. the Bernoulli cycle-hitting determinant NEW-L11;
2. the complete cycle-transversal polynomial / rooted-forest identity NEW-L12;
3. the one-cycle / Laplacian-cofactor identity NEW-L13.

## Executed output

Path:

`proofnet24/HARD10-03/artifacts/2026-09-15T16-33-00Z__cycle_hitting_forest_check_output.json`

Commit:

`ed745be2cba0958374fba86ac8e7d377f06b88f3`

Readback blob:

`4f7da75511bfd2697d6bf2b1152c9ea5d040d31f`

Observed numerical discrepancies were:

* Bernoulli cycle-hitting identity absolute error: `3.61e-16`;
* full transversal-polynomial versus forest-polynomial maximum coefficient error: `3.77e-15`;
* one-cycle probability versus Laplacian cofactor absolute error: `3.61e-16`.

The directly enumerated one-cycle probability was

`0.13327484051031485`,

while the cofactor was

`0.1332748405103145`.

These are floating-point sanity checks only. They do not replace the analytic proofs and are not independent verification.

No email, Gmail, Google Drive, public posting, permission change, workflow modification, other-task change, or third-party contact was performed.
