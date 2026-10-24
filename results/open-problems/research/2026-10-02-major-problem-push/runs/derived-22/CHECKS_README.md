# Reproducing the rank-one `K_{2,3}` certificate

Requirements: Python 3 and SymPy (run used SymPy 1.14.0).

```bash
python theta_rank_one_apex_stability_exact.py
python theta_rank_one_apex_stability_k_independent.py
```

Expected author result: `status = PASS`, 54 backbone forests, 712 augmented
forests at unit weights, 32 spoke terms, thirteen structural identities,
ten pairs reduced to three exact templates, and four positive-definite
binary-form certificates.

The independent script is intentionally separate and additionally exercises
all ten Rayleigh pairs at exact rational parameter profiles.
