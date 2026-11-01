# Round 060 log

## Goal

Harden the exact bridge-certificate verifier so future finite-state
certificates are easier to check and harder to misuse.

## Verifier self-tests

Updated `scripts/bridge_certificate_verify.py` with a `--self-test` mode.  The
self-test checks:

- the toy \(T_3\) algebra certificate succeeds with final value \(1/2\);
- negative matrix entries are rejected;
- nonpositive Collatz vectors are rejected;
- failed Collatz--Wielandt inequalities are rejected;
- failed final strict inequalities are rejected.

## Certificate schema

Added `research/certificates/README.md`, documenting the JSON fields:

- `degree`;
- `pc_upper`;
- `rho_sphere_upper_sq`;
- `lambda_upper`;
- `matrix`;
- `positive_vector`.

The README also states explicitly that the verifier checks only the exact
Collatz--Wielandt algebra and the final inequality.  The bridge majorization
\[
  B_n^{\mathrm{NB}}(q(D-1))\le a^TM^nb
\]
remains the graph-specific obligation of the finite-state construction.
