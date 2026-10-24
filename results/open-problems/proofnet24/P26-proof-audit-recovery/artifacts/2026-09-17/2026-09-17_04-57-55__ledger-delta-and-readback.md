Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested but is not selectable or authenticated in the exposed scheduler/runtime surface.

# P26 ledger delta, immutable readback receipt, and report correction

Run report:
`proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_04-57-55__run-report.md`

- creation commit: `a4c53db23ab43aee0b713e330658930b745334de`
- readback blob: `8f428614c8dc93f00687000ddcc7142b2fd2dae8`
- exact-commit readback reached `End of complete P26 run report.`

## Mathematical reconciliation

Fixed P26 metric: **8 -> 9**. Supported unchanged count: **0 -> 0**.

New counted package: János Komlós real Boolean vector-balancing conjecture as stated by Bansal--Jiang (2025, arXiv:2508.03961, §1), with the current external resolution claim Guo--Fang--Lu (2026, arXiv:2609.11189v1, Theorem 1.1): every finite family of real vectors of Euclidean norm at most one admits a signing with infinity norm `< 3 sqrt(2 pi)`.

Audit IDs:
- `P26-AUDIT-R13-GFL-KOMLOS-ENDTOEND-11 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_SCOPE_PASS / CURRENT_LITERATURE_KNOWN / EXTERNAL_PREPRINT_V1 / NO_ALGORITHMIC_OR_OPTIMALITY_CLAIM`;
- distinct OTHER-track audit: `R12-AUDIT-R13-KOMLOS-01 = PASS`, at `artifacts/R12/R12_AUDIT_R13_KOMLOS_01_2026-09-16.md`, blob `021f2832972456b069b39499c9cb83fe5d72680d`.

The exact universal theorem package is therefore 2/2 by P26 + R12 and is counted exactly once. The Beck--Fiala corollary is not a second package. R13's later finite-`n` claims C17/C18 are outside this audit.

## Exact checker receipts

Independent P26 checker:
`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_04-57-55__gfl_komlos_exact_checker.py`
- creation commit `d19f044533af877a16d009272f9bee50dbd782e3`
- readback blob `4da257123b3d451c8ec0b7673aff34b54afd5e66`

Output:
`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_04-57-55__gfl_komlos_exact_checker.out`
- creation commit `409c42712414080da7ffd9f3d1fcb2c17543735a`
- readback blob `571239c9d6c60ffb28eea522b6ed09cecf34054c`
- terminal line: `ALL_EXACT_CHECKS_PASS`

R13 checker reexecution transcript:
`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_04-57-55__r13_checker_reexecution.out`
- creation commit `fe505639c4f515be1db9dba6c023bea684ead6f7`
- readback blob `8136a3eda8143c4244ba02f589c1902d299bf2eb`

## Immutable report typesetting correction

Exact-commit readback found one escape/typesetting defect in equation (5.3) of the immutable report: the factor intended as `1/24` rendered as `rac1{24}`.

The corrected identity is

`M = ∫ |s| R*(y,s) dy ds = 3/2 - (1/24) ∫_0^6 (6-h) ||rho-rho(.+hv)||_1 dh.`

This is a rendering defect only. The immediately following bound, the exact arithmetic checker, and the derived coefficient `3/2` all use the correct `1/24`. The historical run report is not edited; this sidecar is the immutable correction.

## Root-ledger preservation and attempted reconciliation

Fresh root blobs observed before the attempted merge were:
- `RESULTS.md`: `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`;
- `POSTED.md`: `4cba5265702ede8ecf9c11938a4e70d55f52549c`;
- `QUEUE.md`: `770a58cc1bbe70d912d2254db077aa5756db27e1`.

A whole-file `RESULTS.md` merge was attempted at commit `518f04ab9f93dd12647cdf479a9998a4d4176946`. Commit readback revealed that the whole-file replacement had also rewritten unrelated historical lines, so that commit is **NOT a valid final ledger receipt** and must not be cited as a successful reconciliation.

The unsafe replacement was then surgically rolled back without force-push by a normal descendant commit:
- corrective commit: `0565271283b28ec2991d0d08d3840a82d3b143ee`;
- final `RESULTS.md` blob after readback: `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`, exactly the pre-attempt blob.

Thus no unrelated root-ledger content was left modified. The exposed connector has no line-patch primitive for ordinary repository files; another whole-file attempt would risk repeating unrelated rewrites. Under the conflict-preservation rule, the exact claim-scoped delta is preserved here rather than claiming a root write that did not safely land.

Pending `RESULTS.md` delta for a future patch-safe merge:
- P26 support metric `8 -> 9`, unchanged count `0 -> 0`;
- package: R13 / Guo--Fang--Lu universal real Boolean Komlós theorem, `<3 sqrt(2 pi)`;
- source status: `KNOWN / current external preprint v1 resolution claim`;
- audit IDs: `P26-AUDIT-R13-GFL-KOMLOS-ENDTOEND-11` and `R12-AUDIT-R13-KOMLOS-01`;
- report path/commit/blob as above;
- exact checker/output/reexecution receipts as above;
- scope exclusions: Beck--Fiala corollary is not a second package; R13 C17/C18 not audited by this receipt; no algorithmic/optimality claim.

Fresh post-rollback reads confirm:
- `RESULTS.md` blob `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`;
- `POSTED.md` blob `4cba5265702ede8ecf9c11938a4e70d55f52549c`;
- `QUEUE.md` blob `770a58cc1bbe70d912d2254db077aa5756db27e1`.

No `POSTED.md` change is supported by this external-preprint audit, and no `QUEUE.md` ownership/READY change is supported. Those two roots remain unchanged deliberately.

## Dated literature/status note

On 17 September 2026 the arXiv record for Guo--Fang--Lu still presents the 10 September 2026 theorem with the `3 sqrt(2 pi)` bound; a bounded search by exact arXiv identifier/title plus `correction`, `withdrawal`, and `counterexample` found no primary correction or withdrawal. This is bounded negative evidence only, not a refereeing or maturity certificate.

End of P26 ledger/readback receipt.
