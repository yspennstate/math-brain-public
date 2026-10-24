# HARD8-03 — 2026-09-16T08:22:06Z checkpoint receipts

This is an append-only receipt companion to

`hard8_2026-09-16/HARD8-03/runs/2026-09-16/2026-09-16T08-22-06Z__report.md`.

## GitHub receipts

- Primary mathematical report commit: `9daf8ca76b0d87cb22b9147eb6b61d02bd06a964`.
- Primary report read back successfully at exactly that commit: **VERIFIED**.
- Verifier path: `hard8_2026-09-16/HARD8-03/artifacts/2026-09-16T08-22-06Z__rank_tail_verifier.py`.
- Verifier commit: `a9074a1eba85f99eeadbe77701711fc0fc9fed6e`.
- Verifier read back successfully at exactly that commit: **VERIFIED**.
- Approval/security denial: **NOT EXPOSED**.

## Exact checks completed in-session

The pure-Python implementation corresponding to the archived verifier completed successfully before delivery.

### Coordinate-partition family

For each listed `(g,h)` it checked exact rational rank, exhaustive enumeration of every maximal dissociated subset, exact minimum negative representation width of each omitted column, and exact rank of the omitted/heavy block:

- `(2,2)`: rows 4, columns 4, rank 3, maximal sets 4, width 1, heavy rank 1.
- `(2,3)`: rows 9, columns 6, rank 5, maximal sets 6, width 2, heavy rank 1.
- `(2,4)`: rows 16, columns 8, rank 7, maximal sets 8, width 3, heavy rank 1.
- `(3,2)`: rows 8, columns 6, rank 4, maximal sets 12, width 1, heavy rank 2.
- `(3,3)`: rows 27, columns 9, rank 7, maximal sets 27, width 2, heavy rank 2.

These counts match the proved formulas

`rank=1+g(h-1)`, `#maximal=g h^(g-1)`, `width=h-1`, and `heavy rank=g-1`.

### Exhaustive dimension-4 rank-tail experiment

The verifier exhaustively examined all `32,767` nonempty subsets of the 15 nonzero Boolean vectors in `{0,1}^4`. For each configuration it enumerated all maximal dissociated subsets and, for `k=1,2,3`, minimized the exact real rank of the columns whose minimum negative representation width exceeded `k`.

- configurations checked: `32,767`
- violations of `rank(heavy) <= floor(r/(k+1))`: `0`
- largest observed ratio `(k+1) rank(heavy)/r`: `2/4 = 1/2`

The experiment is finite evidence only. The general rank-tail assertion remains conjectural and is not promoted to theorem status.
