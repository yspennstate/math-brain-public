# HARD8-03 — verification addendum for 2026-09-16T10:11:07Z checkpoint

This append-only receipt accompanies:

`hard8_2026-09-16/HARD8-03/runs/2026-09-16/2026-09-16T10-11-07Z__report.md`.

## 1. GitHub publication/readback receipts

### Mathematical report

- Path: `hard8_2026-09-16/HARD8-03/runs/2026-09-16/2026-09-16T10-11-07Z__report.md`
- Creation commit: `7c1c2ebe553b923b9052031f39e3b398ccc2296c`
- Read back using exactly that commit: **VERIFIED**.
- Blob SHA returned on exact-commit readback: `a4507b4797399e2e77ac1d5831d52f94eec60f9f`.

### Exact verifier

- Path: `hard8_2026-09-16/HARD8-03/artifacts/2026-09-16T10-11-07Z__exchange_profile_verifier.py`
- Creation commit: `87d3ee7e1c0e17a8957c57edf1f1d022bb5e7c2e`
- Read back using exactly that commit: **VERIFIED**.
- Blob SHA returned on exact-commit readback: `aa79e98d9ed12145e468e0d0dfc366cd2e81c8db`.

No older report/artifact, shared index, workflow, repository setting, branch, or access rule was modified.

## 2. Actual verifier execution

The archived verifier was run locally before GitHub publication using the standard Python interpreter. It uses only standard-library modules, exact integer arithmetic, and `fractions.Fraction`; there is no floating-point acceptance test, randomness, external solver, SAT timeout, or heuristic certificate.

The completed execution ended with:

`ALL_CHECKS_PASSED`

The exact reported checks included:

### Equal-sum-block concrete instances

- `(h_1,h_2)=(2,3)`: rank `4`, maximal dissociated sets `5`, profile `{0:1,1:0,2:0,3:0}`.
- `(2,2,3)`: rank `5`, maximal sets `16`, profile `{0:2,1:0,2:0,3:0}`.
- `(2,3,3)`: rank `6`, maximal sets `21`, profile `{0:2,1:1,2:0,3:0}`.
- `(3,4)`: rank `6`, maximal sets `7`, profile `{0:1,1:1,2:0,3:0,4:0}`.

For these instances the verifier checks the complete-group/maximal-set structure, unique omitted-column representations, exact widths, the formula `rho(k)=max(0,N_k-1)`, and `(k+1)rho(k)<=r`.

### Nullity-one concrete circuits

The verifier checked signed circuits of types `2-vs-1`, `2-vs-2`, and `3-vs-2`, including exhaustive maximal-set optimization. Their profiles agree exactly with the report's formula

`rho(k)=1` for `k<min(a-1,b-1)` and `0` otherwise.

### Rank-5, 14-column exchange census

The verifier exhaustively checks all `623` maximal dissociated sets:

- size `6`: `403`;
- size `7`: `220`.

For every maximal set, every omitted target, and every possible removed basis element, it checks independently that the exchanged set is dissociated **iff** the removed basis element lies in the intersection of supports of all signed representations of that target. This is a finite exhaustive check of the single-exchange criterion on the entire witness configuration.

The `k=1` heavy-rank distribution over all maximal sets is exactly:

- rank `0`: `120`;
- rank `1`: `153`;
- rank `2`: `150`;
- rank `3`: `113`;
- rank `4`: `70`;
- rank `5`: `17`.

For the bad set `{0,1,2,3,4,5}`, the verifier reproduces omitted widths

`[2,3,2,2,2,2,2,2]`

and heavy rank `5`. It verifies that target column `6` has the unique signed coefficient vector

`(0,0,-1,1,-1,1)`,

and that swapping column `3` out and column `6` in yields a maximal set with heavy rank `0`.

For the local-minimum set `{0,1,3,5,8,10}`, it verifies heavy rank `2`, with only columns `6` and `9` heavy (each width `2`). It enumerates exactly `16` size-preserving maximal single-swap neighbors, distributed as:

- heavy rank `2`: `7`;
- heavy rank `3`: `6`;
- heavy rank `4`: `3`;
- heavy rank `0` or `1`: `0`.

Thus the strict-improving-single-swap lemma is exactly refuted by this finite witness.

It verifies the plateau path

`{0,1,3,5,8,10}` -> `{0,3,5,8,10,11}` -> `{0,4,5,8,10,11}` -> `{0,4,6,8,10,11}`

with heavy ranks

`2 -> 2 -> 2 -> 0`.

The fixed-cardinality single-swap graph is connected separately on the `403` size-6 maximal sets and on the `220` size-7 maximal sets.

Strict local minima under heavy rank are exactly:

- size 6: `17` of rank 0, `26` of rank 1, `20` of rank 2;
- size 7: `103`, all rank 0.

Finally, for every heavy-rank sublevel in this finite witness, every connected component contains a rank-0 maximal set. This supports plateau descent here but is explicitly only finite evidence, not a universal theorem.

## 3. Review status

The mathematical arguments are self-reviewed and exactly machine-checked on the finite instances above; this is not independent peer review. The full deterministic log-rank conjecture remains open, and the candidate universal profile inequality `(k+1)rho_V(k)<=rank(V)` remains unproved.
