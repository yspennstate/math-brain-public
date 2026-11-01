# C005 calculations

The mathematical report is `../../agents/C005.md`.

The main verifier is:

```bash
python computations/C005/exact_and_integral.py
```

Run from the campaign directory, or use the script's absolute path. It writes
`exact_and_integral_results.json`, checks the rational value `-1/308` by all-atom
enumeration in three and six dimensions, and compares two positive Laplace
integrals against independently calculated log-determinant mixed derivatives.
The exact part uses only Python's standard-library fractions. The numerical
part requires NumPy and SciPy.

The other Python files and JSON/NPZ outputs retain the bounded exploration that
led to the exact result. They are diagnostics only:

- `exterior_search.py`: helper routines and sampled physical-kernel operators.
- `logdet_external_search.py`: independent interior-kernel/logdet-table samples.
- `projection_search.py`: compressed rank-two projections, with one retained
  full-exterior negative sample per input type. Local decomposable minimization
  is not a certificate of global nonnegativity.
- `resolvent_search.py`: approximate six-site resolvent obstructions, superseded
  mathematically by the exact example in the main verifier.

The restricted theorem rests on the analytic integral proof in the report;
quadrature is corroboration. No output asserts general entropy concavity.
