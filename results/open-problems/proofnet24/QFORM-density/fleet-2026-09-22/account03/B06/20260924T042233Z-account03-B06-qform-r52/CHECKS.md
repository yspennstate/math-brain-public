# r52 finite sanity checks

The proof in `REPORT.md` is exact; this file records only a deterministic numerical sanity check performed in the current worker runtime.

Fixed seed: `20260924`.

Samples: `10000` random positive-semidefinite `3 x 3` Gram matrices constructed with ordered eigenvalues `s1 >= s2 >= s3 >= 0` and `s3 < 1/15`.

Checked:

1. `max{1,e1(G),e2(G)} > (5/16) det(I+G)`;
2. with `u` a minimum-eigenvalue unit eigenvector and `h` maximizing `u_h^2`, `det G[J,J] >= s1*s2/3`;
3. Gram-Schur identity `||P_{ker Z_J} z_h||^2 = det(G)/det G[J,J]` for `ZZ^T=G`;
4. `||P_{ker Z_J} z_h||^2 <= 3 s3`.

Observed output:

- minimum sampled `max{1,e1,e2}/det(I+G)`: `0.43460563973296334`;
- required lower bound: `0.3125`;
- maximum cofactor-bound defect: `0`;
- maximum normalized residual-identity discrepancy: `3.914006228714111e-14`;
- maximum sampled residual-to-`s3` ratio: `2.8792754346620777`, below the proved bound `3`.

These computations are diagnostics only and are not used as proof.