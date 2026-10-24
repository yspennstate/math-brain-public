# P15 Hadamard — HARD RESERVE handoff (2026-09-16)

Status: **HARD RESERVE / OPEN / PARTIAL**. The P15 hourly slot has been reassigned by the owner's NEW-METHODS directive; this file freezes the useful Hadamard state without claiming closure or metric progress.

## Frozen source and metric

Outside source: Bandeira, Kireeva, Maillard and Rödder (2025), *Randomstrasse101: Open Problems of 2024*, arXiv:2504.20539, Conjecture 14 (Hadamard conjecture), together with original Hadamard construction literature.

Frozen P15 metric: number of formerly open orders for which P15 itself supplies an exact Hadamard matrix with an executed exact `H H^T = n I` checker.

Final value on active P15 Hadamard work: **0**. Credited order set: **{}**.

Order 668 is known external work and is not P15 progress. P15 independently reconstructed the dated external matrix and exactly checked `H H^T = 668 I`; that validation is continuity evidence only.

## Status reconciliation preserved

- `668`: KNOWN external construction; exact P15 reconstruction/check succeeded; no metric credit.
- `2060`: KNOWN external 2026 construction after the earlier Miyamoto-status ambiguity was resolved by public explicit data. P15 reconstructed and exactly checked the matrix; no metric credit.
- `2092 = 4*523`: the last active P15 report treated this as the **current documented target** after a dated construction-table/status audit. This was carefully not promoted to a theorem that no unindexed construction exists.

Latest active report before reserve:

`proofnet24/P15-hadamard/runs/2026-09-16/2026-09-16_19-23-52__run-report.md`

That report records the exact source/status limitations and is the canonical continuation point if the hard-reserve problem is later reassigned.

## Exact restricted-family work preserved

### Order 2060 / v=514

P15 exactly excluded a bordered-Goethals–Seidel search restricted to invariance under the order-64 multiplier subgroup. The later neighboring HARD8-04 H32-invariant exclusion strictly subsumed that symmetry tier. These are **restricted-family nonexistence results only**, never nonexistence of a Hadamard matrix.

### Order 2092 / v=523

For a common multiplier subgroup `K <= F_523^*` of order `d | 522`, a `K`-invariant sign sequence has row sum

`r = epsilon_0 + d * sum_j epsilon_j`.

The Goethals–Seidel aggregate periodic-autocorrelation equations imply the necessary row-sum identity

`r_1^2 + r_2^2 + r_3^2 + r_4^2 = 2092`.

Exact enumeration over all divisors of 522 leaves only

`d in {1,2,3,6,9}`

as possible common-multiplier orders. Thus tiers `d in {18,29,58,87,174,261,522}` are exactly impossible within this common-multiplier GS family.

At `d=9`, the only sorted absolute row-sum profiles are

- `(1,19,19,37)`;
- `(17,17,17,35)`.

At `d=6`, the only sorted absolute row-sum profiles are

- `(5,5,19,41)`;
- `(7,19,29,29)`.

A separate exact self-check exhausted the order-58-multiplier-invariant Williamson family at length 523 and found no solution. Again this is only a restricted Williamson-family result.

## Failed / blocked routes preserved

- No unrestricted Williamson, Goethals–Seidel, Turyn-type or general Hadamard nonexistence claim was obtained.
- Multiplier-invariant negative searches are family exclusions, not evidence that `H(2092)` does not exist.
- The final active plan was an exact `d=9` GS search using the two row-sum profiles, then `d=6`, with proof-producing SAT/PB evidence if available. The then-current runtime did not expose a proof-producing SAT/PB solver, so no UNSAT certificate was claimed.
- P15 had already reached its second stuck-recovery episode on this target; the owner now explicitly moved the slot to CLOSABLE OUTSIDE work. Do not silently restart Hadamard in this slot.

## Restart conditions for a future hard-reserve owner

A future owner should begin from the latest active report above, re-run current-status/literature checks before assuming 2092 is unresolved, preserve the metric value `0` and set `{}`, and continue only with a genuinely new route or exact finite reduction. Any candidate construction must be converted to an explicit sign matrix and checked by exact integer arithmetic `H H^T = n I` before metric credit.

No email, Drive, public posting, paid compute, permission change or schedule change is part of this handoff.
