# HARD8-03 — failed energy-potential route certificate

The primary report recorded that the stronger potential conjecture

`min_{S maximal dissociated} sum_{v notin S} nu_S(v) <= rank(V)`

is false even for a small Boolean configuration. This append-only note supplies the exact reproducible certificate.

## Exact configuration

Take the ten distinct nonzero Boolean columns in `R^4`

```
0: (1,1,0,0)
1: (1,0,1,0)
2: (0,1,1,0)
3: (1,1,1,0)
4: (1,0,0,1)
5: (0,1,0,1)
6: (1,1,0,1)
7: (0,0,1,1)
8: (1,0,1,1)
9: (0,1,1,1)
```

Their exact real rank is `4`.

The archived verifier exhaustively enumerates all maximal dissociated subsets and all exact ternary representations. It finds exactly `150` maximal dissociated subsets and

`min_S sum_{v notin S} nu_S(v) = 5 > 4 = rank(V)`.

One minimizer is

`S=(0,1,3,4,5)`,

with omitted columns `2,6,7,8,9`, each having minimum negative width exactly `1`. Thus the total is exactly `5`.

The executed output was

```
RANK 4
MAXIMAL_DISSOCIATED_SETS 150
MIN_TOTAL_NEGATIVE_WIDTH 5
MINIMIZER ((0, 1, 3, 4, 5), {2: 1, 6: 1, 7: 1, 8: 1, 9: 1}, 5)
ALL_CHECKS_PASSED
```

This refutes only the stronger energy-potential shortcut. It does **not** refute the profile inequality `(P_k)`; indeed the profile uses rank of the heavy tail rather than cardinality-weighted negative-width energy.

## GitHub receipt

- Verifier path: `hard8_2026-09-16/HARD8-03/artifacts/2026-09-16T12-12-08Z__failed_energy_potential_verifier.py`
- Creation commit: `a226b775e04d6ccc89fdf5c400c76e745d3ab062`
- Exact-commit readback: **VERIFIED**.
- Blob SHA: `11b36f1c6045b93cb2c57e6183a56b2c53c8af97`.

The verifier uses exact `Fraction` arithmetic, exact subset-sum dissociation, and exhaustive ternary representations; no floating point, randomness, external solver, or timeout inference is used.