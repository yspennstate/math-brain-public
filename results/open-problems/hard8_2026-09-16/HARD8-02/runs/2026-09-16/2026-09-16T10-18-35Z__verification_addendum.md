# HARD8-02 — verification addendum — 2026-09-16T10:18:35Z

This append-only note records the exact computation and GitHub receipts for the mathematical checkpoint

`hard8_2026-09-16/HARD8-02/runs/2026-09-16/2026-09-16T10-16-29Z__report.md`.

## Report receipt

The report was created on branch `master` with commit

`27cb714c52148b3c4569e6ac82811aebf4d2c59d`.

It was then read back by exact path at that exact commit. GitHub returned content blob SHA

`7e34e3bdae0f20b6265e854faea2adb920654534`.

Status: **VERIFIED**.

## Verifier receipt

The exact standard-library verifier is

`hard8_2026-09-16/HARD8-02/artifacts/2026-09-16T10-16-29Z__tensor_absorber_verifier.py`.

It was created on branch `master` with commit

`603ca2115a50d1616b980dbf4aaea2f9e54ad94e`.

It was then read back by exact path at that exact commit. GitHub returned content blob SHA

`beaca497d312f6415f36475e0665c1354bf14496`.

Status: **VERIFIED**.

## Exact completed run

The verifier was executed from the same archived source text using the Python standard library only. It completed with output:

```text
PATH_TENSOR_CHECKS 1829
LABELED_TREE_COUNTS {2: (1, 2), 3: (3, 9), 4: (16, 64), 5: (125, 625), 6: (1296, 7416)}
EXTREMAL_ROOTED_PAIRS 8116
EXHAUSTIVE_TENSOR_CHECKS 40580
BLOCK_SUM_CHECKS 8897
BLOCK_SUM_EQUALITIES 147
ALL_CHECKS_PASSED
```

Interpretation:

* `PATH_TENSOR_CHECKS 1829` checks every endpoint-rooted path order `h=2,...,60` and every cutoff `k=0,...,30`.
* The labeled-tree census exhausts all Cayley labeled trees through order 6. For each distinguished root, the script exhaustively searches permutations for a graceful labeling with that root at the maximum label. The supported rooted-pair counts are shown in the second coordinate of each tuple.
* `EXHAUSTIVE_TENSOR_CHECKS 40580` then verifies the full tensor labeling, suffix-root block, internal difference interval, attachment interval, and centered-residue identity for every one of those rooted motifs at cutoffs `k=0,...,4`.
* `BLOCK_SUM_CHECKS 8897` checks the block-separable sum identity for `1<=c<=41`, `0<=k<=30`, and local edge differences `1<=d<=7`; equality occurs exactly when `c=2k+1`.

No floating point, randomness, SAT/MIP solver, heuristic acceptance, or timeout-based inference is used. These computations are sanity checks; the checkpoint's theorems have direct symbolic proofs.

## Status ledger

The full graceful tree conjecture remains **OPEN**.

New verified project results from this checkpoint:

1. `2k+1` copies of every root-extremal graceful rooted tree admit an explicit suffix-root cutoff-`k` absorber.
2. This gives all endpoint-rooted paths, all lengths, in closed form.
3. The new cutoff after grafting an `h`-vertex motif obeys `2K+1=(2h-1)(2k+1)`.
4. Inside the block-separable tensor ansatz with one consecutive `c`-block per local graceful edge color, the multiplicity is necessarily `c=2k+1`.

No universal proof or certified counterexample is claimed.