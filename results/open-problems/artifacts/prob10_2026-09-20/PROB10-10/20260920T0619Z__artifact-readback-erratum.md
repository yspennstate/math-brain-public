# PROB10-10 artifact readback correction

During readback, the initially uploaded pair

- `20260920T0619Z__six_local_saw_cone_exact.py`
- `20260920T0619Z__six_local_saw_cone_exact.out`

was found not to be a reproducible matching code/output pair: the uploaded hard-coded candidate Collatz vector did not match the locally executed candidate vector recorded by the output (the output reports `zmax=64389239017`, while repository search/readback did not find that value in the hard-coded vector). Those two files are therefore **not cited as a certificate and must not be used to support any theorem claim**. They are preserved immutably as failed bookkeeping artifacts.

The authoritative reproducible pair is instead

- `20260920T0619Z__six_local_saw_cone_repro.py`
- `20260920T0619Z__six_local_saw_cone_repro.out`.

The replacement checker deterministically generates the candidate positive vector by ordinary floating power iteration, rounds it to integers, and then rechecks every promoted transfer-matrix inequality and every theorem-relevant sign with exact `Fraction` arithmetic. Floating point is used only to propose a vector, never to certify the sign. Its archived execution ends `ALL_EXACT_CHECKS_PASS = True`.

No existing file was overwritten or deleted. This note supersedes only the evidentiary status of the mismatched initial pair.
