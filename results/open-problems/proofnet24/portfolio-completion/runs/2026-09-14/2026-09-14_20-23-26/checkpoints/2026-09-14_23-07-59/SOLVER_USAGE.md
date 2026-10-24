# Exact fixed-point certificates

The solver applies to all four-type strictly non-Volterra coefficient arrays. Its mathematical guarantee is [equation (10)](FOUR_TYPE_UNIQUENESS.md): for a rational probability vector with every coordinate at most `2/5`, the distance to the unique fixed point is at most five times its exact residual. Both scripts require only Python's standard library.

Run from this directory:

```bash
python3 computations/qso_certified_solver.py examples/qso-boundary-operator.json --tolerance 1e-8 > certificate.json
python3 computations/qso_verify_certificate.py certificate.json --operator examples/qso-boundary-operator.json
```

The [supplied example certificate](examples/qso-boundary-certificate.json) was generated and independently verified with these commands. This operator has the boundary fixed point `(1/3, 1/3, 1/3, 0)`; the decimal-grid approximation receives a nonzero exact error bound.

Input is a JSON object containing `pairs`, with one row for each of the ten unordered pairs `0 <= i <= j < 4`. A row contains integer indices `i`, `j` and a four-entry `p` list. Probabilities must be integers or exact strings such as `"1/3"`; each row must sum exactly to one, and offspring probabilities at the parent indices must be zero. Floating-point JSON values and booleans are rejected. The coefficient array for reversed parents is filled by symmetry.

The search uses ordinary floating-point arithmetic and the globally convergent averaged iteration with weight `2/5`. It then rounds a candidate to an exact rational probability vector and recomputes every residual term using `fractions.Fraction`. The emitted record includes the complete coefficient array, candidate, exact residual, certified error, coordinate intervals and the result of an exact tolerance comparison. The independent verifier recomputes these quantities without importing solver code. Supplying `--operator` also checks that the certificate refers to the intended input.

Exit status `0` means that the requested tolerance was certified. Status `2` can mean an invalid input or an unmet tolerance; inspect the error or the returned record's `tolerance_met` field. `--digits` selects the decimal grid (1–30), and `--max-steps` caps the search (0–100000). Increasing digits does not increase the precision of the floating-point search. An unattained tolerance does not produce a success claim.

For Python callers, the public `solve` and `certify` functions accept coefficient entries and candidate coordinates only as `Fraction` or integers. `solve` also requires an exact positive `Fraction` or integer tolerance. The lower-level numerical and polynomial helpers are implementation functions and do not independently validate an arbitrary coefficient array.

The [026 audit](agents/026.md) found that the original public API could accept floating-point candidates and falsely report zero residual after a tiny coefficient perturbation. The canonical solver has been corrected. The immutable `026_original_qso_certified_solver.py` is retained solely to reproduce that historical failure. The exact regression uses a perturbation of `1/10^20`, whose nonzero residual is `1/(8*10^20)`. Current verification is in [verify_qso_solver.py](computations/verify_qso_solver.py); the full adversarial audit is in [026_verify_qso_certificates.py](computations/026_verify_qso_certificates.py).

The independent arithmetic check depends on the analytic theorem for its error guarantee. It is not a proof-assistant verification of that theorem.
