# HARD8-02 — verification addendum — 2026-09-16T08:19:01Z

This append-only note records the exact computation and GitHub receipts for the mathematical checkpoint

`hard8_2026-09-16/HARD8-02/runs/2026-09-16/2026-09-16T08-10-57Z__report.md`.

## Main report receipt

Main-report creation commit:

`5cb970b8a34611bc5cafbe7b5e027e2091894b04`

The file was read back at that exact commit after creation. Readback returned the expected title and opening theorem list, so the mathematical report is **VERIFIED**.

## Exact verifier

Artifact:

`hard8_2026-09-16/HARD8-02/artifacts/2026-09-16T08-10-57Z__root_transfer_block_verifier.py`

Artifact creation commit:

`beb3c739e2c056aef264defd72a850b1b42f7610`

The artifact was read back at that exact commit after creation, so the source artifact is **VERIFIED**.

The verifier uses exact integer arithmetic plus NetworkX only for finite graph generation/connectivity. It contains no floating point, randomized search, SAT solver, or timeout-based mathematical inference.

## Actual completed run

Command used on the locally identical source:

`python root_transfer_verifier.py --max-n 7 --delta 2`

Output:

```text
PASS
trees 24
graceful_labelings 2650
certificates 25578
low_certificates 12789
high_certificates 12789
verified_transfers 76734
max_n 7
delta 2
```

Interpretation:

* all 24 non-isomorphic trees of orders 2 through 7 were enumerated;
* 2,650 graceful labelings were generated exactly;
* across all root choices and thresholds the program found 25,578 one-gap certificates, split symmetrically into 12,789 low and 12,789 high certificates;
* for every certificate it tested `K=k,k+1,k+2` using the closed-form balanced-broom construction;
* all 76,734 constructed enlargements were checked to have edge-difference set exactly `1,...,m+K+1` and to carry the claimed new one-gap certificate at the transferred root;
* the induced new-vertex forest was checked to have exactly `k+1` components and hence to meet the proved component lower bound with equality.

The script also checks, for all `0<=k<=20` and `1<=s<=20`, the arithmetic identity that the number of missing colours in `{k+1,...,k+s}` which are at least `s` equals `min(s,k+1)`.

A larger exhaustive run through order 8 was attempted first but exceeded the available 45-second local execution window. It was stopped with no mathematical conclusion drawn from the timeout. The completed order-7 check is only a finite consistency test; the arbitrary-size statements in the main report are established by symbolic proofs, not by this enumeration.

## Status

**OPEN.** The full graceful tree conjecture is not resolved. This run's durable advance is the sharp single-block component obstruction together with the optimal balanced-broom root-transfer construction and the `k=0` connected-graft classification.
