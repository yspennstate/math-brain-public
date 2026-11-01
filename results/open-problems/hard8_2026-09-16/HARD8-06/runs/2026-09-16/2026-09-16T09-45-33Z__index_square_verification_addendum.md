# HARD8-06 — verification addendum for relative index-square result

Mathematical addendum:
`hard8_2026-09-16/HARD8-06/runs/2026-09-16/2026-09-16T09-44-44Z__index_square_addendum.md`

- creation commit: `840dbeb1d44339da3f2b2f7b52553ecff572ed19`
- exact-commit readback blob: `e2376226f2da187f321696b7345a0c9bc535c8f3`
- status: **VERIFIED**

Exact integral-basis verifier:
`hard8_2026-09-16/HARD8-06/artifacts/2026-09-16T09-44-44Z__relative_index_square_verifier.py`

- creation commit: `786de908b090d8afc8ac8ac571462b8ea82c7e4f`
- exact-commit readback blob: `bec19e3061b6e4c6e9002d42b3eb4569348a2ec5`
- status: **VERIFIED**

The verifier was executed before publication with Python 3 and SymPy's exact `round_two` maximal-order algorithm. It completed:

```text
PASS
exact integral-basis samples: 10
```

The ten irreducible reciprocal examples include nontrivial monogenic indices and nontrivial square quotients. For example, for `R=y^2-4y-4` it independently obtained

```text
I_F=2, I_L=8, endpoint=64, N_rel=16, square quotient=4.
```

Another example, `R=y^2-3y-1`, yielded

```text
I_F=1, I_L=3, endpoint=27, N_rel=3, square quotient=9.
```

Every sample exactly satisfied

`N_rel * I_L^2 = |Q(1)Q(-1)| * I_F^4`

and the quotient `|Q(1)Q(-1)| / N_rel` was an integer square. No floating point, randomness, heuristic acceptance, or timeout-based inference was used.