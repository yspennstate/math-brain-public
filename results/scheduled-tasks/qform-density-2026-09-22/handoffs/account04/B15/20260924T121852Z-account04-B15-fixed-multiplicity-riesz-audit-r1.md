# account04/B15 handoff — fixed-multiplicity Riesz and regularity audit

Run: `20260924T121852Z-account04-B15-fixed-multiplicity-riesz-audit-r1`

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Source pin: `math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, owner-supplied SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Published audit: `math-open-problems@04d69ef2b93b7d4247d2e3a9f1cf7994c39a3c89`.

Verdict:

- PASS for the mathematical 17-eigenvalue baseline.
- Gaussian inversion, the full Riesz half-potential constant, rough scalar/pair trace arguments, and the distinction between essential boundedness and continuity all check.
- Nonfatal wording gap: in the product-projection proof, after omitting (b_i=0) rows, write (sum_{b_i>0}(1-b_i)le d), or explicitly retain the all-index sum.
- Repository-package gap: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` advertised by the README were absent at the root.
- No multiplicity reduction certified. The order-four/13-direction route reaches only a (1/|t|) scalar envelope; (UV) for independent uniforms shows such an envelope alone is compatible with an unbounded logarithmic density.

This is one independent audit, not a release certificate. The full three-eigenvalue conjecture remains open.
