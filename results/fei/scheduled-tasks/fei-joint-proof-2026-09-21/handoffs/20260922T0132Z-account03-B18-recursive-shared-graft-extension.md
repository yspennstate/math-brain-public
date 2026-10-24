# FEI handoff — account03/B18 recursive shared-graft extension

**Status:** `ESSENTIAL_STEP_APPLIED`; full FEI remains `OPEN / NOT PROVED`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Scientific report:
`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T011005Z-recursive-shared-graft-extension/REPORT.md`.

Consumed completed peer result: account01/B18 `20260922T0117Z-recursive-shared-graft/REPORT.md` (commit `b9b63c908139fcd280a4913229afd7ab62ca50aa`, blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`), plus account02/B17's exact gate-margin composition cocycle.

New proved inference: apply account01/B18's exact balanced-monotone shared-core recurrence two further times. Exact rational log enclosures certify genuine finite balanced Boolean gates `F_3,F_4` with

- `H(F_3)/(I(F_3)-1) > 6.5218509158557171794336583919648574196767563718341573`, exceeding the peer `F_2` upper endpoint by `>1.52e-7`;
- `H(F_4)/(I(F_4)-1) > 6.5218509485644448965490881329959858569477358114202360`, exceeding `F_3` by `>3.27e-8` and `F_2` by `>1.85e-7`.

Hence balanced self-composition proves

`C_FEI > 6.5218509485644448965490881329959858569477358114202360`.

Relative to the old read-once centre `6.4548`, `F_4` requires normalized quadratic gate margin

`>0.2682037942577795861963525319839434277909432456809443`.

By account02/B17's barycenter/cocycle theorem, if `F_4` decomposes then some composition-prime factor has at least this margin at its induced bias. Separately, the newer account01/B12 report `20260922T011847Z-prime-n18-gate/REPORT.md` (blob `9ab98c0e82f7cf0f34eac98923df23b7b160670b`) proves the source-valid n=18 Numaro gate itself is composition-prime, providing an explicit prime witness to the failure of AND/decomposable extremality.

**Exact failed claim:** do not freeze the scalar `PRIME-GATE-LIFT` successor at the previous `F_2` cap, or even at the intermediate `F_3` cap; the same source-valid Boolean mechanism immediately forces a larger centre.

**Remaining implication:** either prove the exact tail of the shared-graft recurrence and only then set a finite scalar centre, followed by an all-prime/all-bias gate proof, or replace the one-parameter lift by a different finite-cap symmetric potential surviving shared-coordinate interference. The infinite recurrence has not been proved monotone in this handoff.

**Next recipients:** account01/B18 for the recurrence/tail theorem; account02/B17 for prime-factor propagation; all gate-potential builders should consume this lower floor before fixing a new candidate.
