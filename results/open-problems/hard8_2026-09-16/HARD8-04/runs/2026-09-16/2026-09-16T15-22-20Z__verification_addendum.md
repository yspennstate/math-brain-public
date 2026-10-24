# HARD8-04 verification addendum — 2026-09-16T15:22:20Z

This append-only receipt supplements, without modifying, the immutable run report:

`hard8_2026-09-16/HARD8-04/runs/2026-09-16/2026-09-16T15-22-20Z__report.md`

## Report receipt

- creation commit: `484a1a8f35a1e9760d046d59b09d2d57a6aa59ba`
- exact-SHA readback blob: `af046747a4f9fc22b707d50f2d71335548efdc2c`
- status: **VERIFIED**

## Executed self-check confirmation

The two archived checker computations were executed in the run environment after source creation, and their computed results matched the already archived text outputs exactly in every mathematical field used by the report.

### H(2060)

From the four explicit length-515 sign sequences:

- lengths: `[515,515,515,515]`
- row sums: `[-17,5,39,15]`
- aggregate periodic-autocorrelation peak: `2060`
- maximum absolute off-peak aggregate autocorrelation: `0`
- independently assembled standard Goethals-Seidel serialization SHA-256: `0ad87cec498f617ee5a158dbc798b840c2a4f712f1bae7885d8693a0663ca018`
- all `2,120,770` distinct row pairs checked by exact integer Hamming arithmetic
- no failing row pair; all off-diagonal inner products zero and diagonal `2060`

Thus `HH^T = 2060 I` is an executed exact self-check, not an inferred or timeout-based result.

### T(523) multiplier profile gate

Exact enumeration of every divisor of `522` and every row-sum tuple within the square-sum bound recovered:

- nontrivial surviving multiplier orders exactly `{3,9}`;
- at `d=9`, the unique normalized row-sum pattern `19,(0,9,9)`, equivalently `(19,9,9,0)` up to the stated component normalization;
- `C(30,3)=4060` ordered support-orbit profiles.

The enumerated `d=3` row-sum patterns and all eliminated divisor rows agree exactly with the archived output.

## Artifact receipts

- H2060 checker commit `11c0163a29913febcbad1a3bd4065ac556011e2e`, blob `27a5b1d5c23779bd727acaa21b6f9946cd336b5a` — VERIFIED.
- H2060 output commit `59d151680a6fb9503a574e59f950eadda23c937c`, blob `df3752aab11acbea9276209513b58d431b5fb51b` — VERIFIED.
- T523 profile checker commit `04090b992c3ed639836e27c7a9cf66ed8ca4fd21`, blob `29f876a70bc388510f75820d1d329a5f01ef966b` — VERIFIED.
- T523 profile output commit `fec54bbe1990ee2d1bc5e53d0edab6e5934d73e7`, blob `35ce27ac9d694aa72431a850b6715e26c9048b3e` — VERIFIED.
- literature/status artifact commit `4787f91a1b3dd299be1ac1dc0021d993a1dc69ea`, blob `ef4ee0b5d03837a971fd774aa14004e8e2af319a` — VERIFIED.
- ledger delta commit `42c275810c2a2e3a7544ff4bbdfac632e1cc53c9`, blob `d6f4c91fa12375f155ffc826570a17b327e8d2fc` — VERIFIED.

No source-level closure is claimed. Self-checks remain self-checks, not independent OTHER-task audits.
