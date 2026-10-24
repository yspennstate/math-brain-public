# C009 computations

The authoritative report is `../../agents/C009.md`.

Run the independent exact certificate with Python 3 and no third-party libraries:

```sh
python verify.py
```

It reconstructs all matrix and determinant polynomial identities using `fractions.Fraction`, checks all Bernstein coefficient signs, and verifies the exact negative middle-slice example. The expected output is `verification_results.json` (138 assertions).

The symbolic generation scripts require SymPy:

```sh
python center_symbolic.py
python middle_symbolic.py
python rational_family.py
```

The first two verify generic rational/sum-of-squares identities. The third regenerates `rational_family_certificate.json`; `verify.py` verifies that certificate independently of SymPy.

`explore.py` and `slices.py` require NumPy and contain numerical exploration only. Their computations are not proofs. `exploration_output.json` preserves the seed-9009, 20,000-sample output of `explore.py`.
