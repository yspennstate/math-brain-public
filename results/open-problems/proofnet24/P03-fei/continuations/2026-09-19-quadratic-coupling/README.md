# Quadratic coupling and cubic-core FEI continuation

19 September 2026. Full FEI remains OPEN. This folder contains an analytical class theorem, its exact self-checks, and a clearly labeled unsuccessful exploratory global-drift probe. No independent audit, Lean verification, or comprehensive novelty clearance is claimed.

Read REPORT.md in full. The main result is H(F)<=4 I_aff(F)<=4 J(F)<=4 I(F) for products of jointly independent affine clauses with arbitrary quadratic coupling, including a separate arbitrary cubic core coupled quadratically to all clause and free coordinates. The constant four is sharp over the class. Dependent higher-degree clause forms and cubic terms sharing wide-clause parameters are not covered.

A core of bounded degree d>=3 gives the analogous explicit constant 2^(d-1), not a uniform bound as d grows. The report preserves the distinction between this class theorem and unrestricted FEI.

Run:

```sh
python verify_quadratic_coupling.py --output verification.json
```

The only dependency is the included unchanged prior_exact_entropy.py, reused from the balanced-substitution work. It implements exact Walsh transforms, rational logarithm expressions, and outward rational logarithm bounds. verification.json is an actual executed output; a second run matched every non-timing field. Universal conclusions depend on the written proofs, not extrapolation from these finite checks.

The exploratory/ program uses NumPy and floating-point entropy. It probes affine-influence drift on majority functions and is NOT proof evidence or a claimed universal estimate.

Continue by addressing genuinely dependent higher-degree forms, the accumulated allocation bound, or the correctly quantified erasure inequality. Do not revive the disproved scalar/full-resolvent pointwise estimates. Read the newest master index before continuing and distinguish consumed source versions from actual new mathematical changes.

A later scheduled worker posted two proposed affine potentials during this run. SCHEDULED_POTENTIAL_CHECK.md gives their exact counterexamples and the tensorization obstruction. Run `python check_scheduled_potentials.py` to reproduce scheduled_potential_checks.json. Its resource candidate fails for every constant; its entropy candidate is refuted for coefficient four, not for every possible coefficient. The positive class theorem is unchanged.
