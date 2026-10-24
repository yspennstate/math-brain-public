# P16 Černý — HARD RESERVE handoff (2026-09-16)

Status: **HARD RESERVE / OPEN / PARTIAL**. This line of work is no longer the active P16 allocation. Do not manufacture another unchanged enumeration certificate; resume only after explicit reassignment with a genuinely new route or a complete missing shard.

## Outside source

Ján Černý, “Poznámka k homogénnym experimentom s konečnými automatmi,” *Matematicko-fyzikálny časopis* 14(3) (1964), 208–216, DML-CZ 126647.

## Frozen metric and certified value

The P16 finite metric is the largest `n` for which **both** the exactly-three-letter and exactly-four-letter classes of `n`-state synchronizing complete deterministic finite automata are completely verified against the Černý square reset-threshold bound.

Certified value at handoff: **7**.

- The full ternary class is known/verified through `n=8`.
- All alphabet sizes, hence in particular the four-letter class, are covered through `n=7`.
- The missing finite cell is therefore exactly `n=8`, syntactic alphabet size `q=4`.

The alphabet is syntactic: distinct symbols are allowed to induce the same state transformation. Duplicate induced transformations may be collapsed without changing synchronizability, reachable subsets, or shortest reset length; conversely a support of fewer than four distinct transformations belongs to the exactly-four-symbol scope by duplicating letters. Because the ternary `n=8` cell is already covered, any genuinely missing `n=8,q=4` counterexample may be reduced to four distinct induced transformations. Identity/constant letters and nonessential letters are covered by the exact reductions recorded in the canonical P16 reports, but they remain part of the original full scope and are not silently deleted from the metric.

A timeout, sampled search, simple-idempotent subclass, canonical-parent shard, or any other restricted family remains **PARTIAL** and does not move the metric.

## Latest exact route and obstruction

Latest canonical report before reserve:

`proofnet24/P16-cerny/runs/2026-09-16/2026-09-16_18-40-14__run-report.md`

Creation commit: `62732ea4348f46db980213a3cb918028a3391d5f`  
Verified blob: `58ca54f55b9eebb210e40b360d1564652c534adf`.

That run ported the Kisielewicz–Szykuła Theorem-2/Theorem-3 extension-safe parent sieve and validated it by a complete exact `n=4` computation. It did **not** complete the `n=8,q=4` cell. The live obstruction is a complete, canonical, reproducible stream of nonsynchronizing ternary eight-state parents followed by threshold-49 classification and durable fourth-letter shards for every retained parent. The actual retained-parent count at `n=8` remains **UNMEASURED**.

## Resume condition

A future owner should start from the canonical report above and the earlier HARD8-01/P16 reductions. Resume only with one of:

1. a provably complete external/canonical ternary `n=8` parent stream;
2. a genuinely new parent-safe theorem that makes the complete stream tractable and is proved on the page;
3. a full independent enumeration with proved symmetry reduction and durable complete shards.

Do not restart raw enumeration from scratch and do not reinterpret a restricted certificate as complete `n=8` coverage.
