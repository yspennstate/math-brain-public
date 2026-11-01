# Exact fixed-point certificates

The guaranteed solver applies to every rational four-type strictly non-Volterra coefficient array and every positive rational tolerance. It returns a rational candidate with a certified distance bound to the unique fixed point. All programs use Python's standard library.

## Guaranteed exact search

Run from this directory:

```bash
python3 computations/065_exact_grid_solver.py examples/qso-boundary-operator.json --tolerance 1/100000000 > certificate.json
python3 computations/qso_verify_certificate.py certificate.json --operator examples/qso-boundary-operator.json
```

The new solver uses integer arithmetic throughout its rounded iteration. It starts at the uniform state, preserves the coordinate cap `2/5`, and stops when five times the exact residual is at most the requested tolerance. The [complete proof and execution record](agents/065.md) give a finite iteration bound and polynomial bit complexity in the explicit rational input length. The [executed CLI certificate](computations/065_cli_certificate.json) was accepted by the independent verifier.

Use an explicit integer or numerator/denominator tolerance such as `1/100000000`. This program rejects decimal fractions and scientific-notation strings. There is no precision setting or discretionary iteration limit. Exit status `0` means certification succeeded; invalid inputs produce status `2`.

Input is a JSON object containing `pairs`, with one row for each of the ten unordered pairs `0 <= i <= j < 4`. A row contains integer indices `i`, `j` and a four-entry `p` list. Probabilities must be integers or exact strings such as `"1/3"`; each row must sum exactly to one, and offspring probabilities at the parent indices must be zero. Floating-point JSON values and booleans are rejected. The coefficient array for reversed parents is filled by symmetry.

The record contains the operator, candidate, exact residual, certified error and coordinate intervals. The independent verifier recomputes the certificate without importing the solver; `--operator` binds it to the intended input. Its arithmetic check validates the returned candidate, not the extra iteration-plan fields. The error theorem is [equation (10)](FOUR_TYPE_UNIQUENESS.md): inside the cap, distance is at most five times the residual of the original quadratic operator.

The Python API in `065_exact_grid_solver.py` is `solve(data, tolerance)`. Coefficients may be exact integers, `Fraction` values or explicit rational strings. The tolerance must be an integer or `Fraction`, excluding booleans. The [focused exact checks](computations/065_verify_exact_grid_solver.py) include a coefficient perturbation of `10^-400` certified at tolerance `10^-420`.

## Earlier floating-point search with exact certification

The existing `qso_certified_solver.py` remains available:

```bash
python3 computations/qso_certified_solver.py examples/qso-boundary-operator.json --tolerance 1e-8 > certificate.json
python3 computations/qso_verify_certificate.py certificate.json --operator examples/qso-boundary-operator.json
```

The [earlier example certificate](examples/qso-boundary-certificate.json) was generated and independently verified with this search. Its operator has boundary fixed point `(1/3, 1/3, 1/3, 0)`.

The search uses ordinary floating-point arithmetic and the globally convergent averaged iteration with weight `2/5`. It then rounds a candidate to an exact rational probability vector and recomputes every residual term using `fractions.Fraction`. The emitted record includes the complete coefficient array, candidate, exact residual, certified error, coordinate intervals and the result of an exact tolerance comparison. The independent verifier recomputes these quantities without importing solver code. Supplying `--operator` also checks that the certificate refers to the intended input.

Exit status `0` means that the requested tolerance was certified. Status `2` can mean an invalid input or an unmet tolerance; inspect the error or the returned record's `tolerance_met` field. `--digits` selects the decimal grid (1–30), and `--max-steps` caps the search (0–100000). Increasing digits does not increase the precision of the floating-point search. An unattained tolerance does not produce a success claim.

For Python callers, the public `solve` and `certify` functions accept coefficient entries and candidate coordinates only as `Fraction` or integers. `solve` also requires an exact positive `Fraction` or integer tolerance. The lower-level numerical and polynomial helpers are implementation functions and do not independently validate an arbitrary coefficient array.

The [026 audit](agents/026.md) found that the original public API could accept floating-point candidates and falsely report zero residual after a tiny coefficient perturbation. The canonical solver has been corrected. The immutable `026_original_qso_certified_solver.py` is retained solely to reproduce that historical failure. The exact regression uses a perturbation of `1/10^20`, whose nonzero residual is `1/(8*10^20)`. Current verification is in [verify_qso_solver.py](computations/verify_qso_solver.py); the full adversarial audit is in [026_verify_qso_certificates.py](computations/026_verify_qso_certificates.py).

The independent arithmetic check depends on the analytic theorem for its error guarantee. It is not a proof-assistant verification of that theorem.
