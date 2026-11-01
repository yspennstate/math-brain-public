# HARD8-04 — rotation-pending handoff after two stuck recoveries and final execution

Model actually exposed in the final execution: GPT-5.6 Sol; reasoning level UNVERIFIED. The scheduler surface exposed no model selector, no reasoning-effort selector, and no authenticated runtime model/effort field. `GPT-6 / maximum` remained prompt text only.

Status: **OPEN / PARTIAL / ROTATION_PENDING for this native slot**. This is not a mathematical retirement of the Hadamard conjecture. It is the owner-directed same-slot handoff after HARD8-04 used STUCK RECOVERY 1, STUCK RECOVERY 2, and the selected final pre-rotation execution without moving its frozen metric.

Native slot: `6aaa2bb424dc81919d9aa012c3b09f46`.

Outside source: Bandeira, Kireeva, Maillard and Rödder, *Randomstrasse101: Open Problems of 2024*, arXiv:2504.20539, Conjecture 14: every positive multiple of four is the order of a Hadamard matrix.

Frozen metric: number of **previously genuinely open orders newly covered by this track** with source/current-status evidence retained and an explicit exact construction. Final HARD8-04 value: **0**. Credited-order set: **{}**. Order `668` is a known external result and never receives novelty credit. The recovered project state also records `2060` as external known work. `2092=4*523` is only the current documented search target after dated checks, never a theorem that no unindexed construction exists.

## Current-status gate at handoff

On 2026-09-17 the live arXiv HTML for arXiv:2504.20539 was reread and still states Conjecture 14 in the ordinary all-multiples-of-four form. The Cati--Pasechnik construction-database paper arXiv:2411.18897 was reread as the principal audited finite-order baseline. Fresh bounded searches for `Hadamard 2092`, `order 2092 Hadamard`, `523 Goethals-Seidel`, `Williamson 523`, and nearby 2026 construction work did not surface a status-changing primary explicit `H(2092)` construction. This is a dated negative search outcome only, not proof of openness or novelty. Any later reassignment must rerun the source/current-version/later-author/citing-literature gate before choosing an order.

## Frozen exact construction state

The most developed restricted route is common-multiplier Goethals--Seidel at length `523` with the order-nine subgroup `K<=F_523^*`. P15's preserved row-sum arithmetic leaves the two `d=9` profiles

- `(1,19,19,37)`;
- `(17,17,17,35)`.

For the broader second profile, after normalization the four negative-set sizes are

`(253,253,253,244)`

and each block contains `0`, selecting respectively `28,28,28,27` of the 58 nonzero K-orbits.

The pinned exact split-prime checkpoint at

`hard8_2026-09-16/HARD8-04/artifacts/2026-09-16T22-21-35Z__d9_split617_exact_lift_check.py`

proves that the 29 `F_617` character equations are sufficient for exact integer periodic complementarity in this restricted family. Thus a binary solution of those equations would give an exact GS seed; deterministic expansion and an exact `H H^T=2092 I` check would still be mandatory before metric credit.

## New final-execution reduction: signed near-skew quadratic code

Pair the 58 nonzero K-cosets as `{C_j,C_{j+29}}`, `j in Z/29Z`. For a block that contains `0`, omits a set `O` of pairs, and chooses exactly one orbit from each nonomitted pair, write the orientation as `s_j in {+1,-1}`. Let `eta_r` be the pinned `F_617` Gauss periods and

`F(c)=1+sum_{selected C_j} eta_{c+j}`.

Then, exactly in `F_617`,

`F(c)+F(c+29) = 1 - sum_{j in O}(eta_{c+j}+eta_{c+j+29})`,

and

`F(c)-F(c+29) = sum_{j notin O} s_j (eta_{c+j}-eta_{c+j+29})`.

Therefore

`4 F(c)F(c+29) = S_O(c)^2 - D_s(c)^2`,

where the omission pattern determines `S_O` and the orientations enter only through the square of a linear code functional `D_s`. The four-block GS equations become 29 coupled **sum-of-four-squares equations over F_617 with binary signed-code liftability constraints**. This is the cleanest representation left by HARD8-04 for a future exact solver.

## Exact exclusion from the final B1/B3/B8 execution

The final run tested the lowest-degree algebraic orientation code on the quotient `Z/29Z`.

For each of the first three blocks, omit one pair `a` and orient every other pair by

`s(j)=sigma * chi(j-a)`,

where `chi` is the quadratic character mod 29. This gives exactly 58 one-hole codewords. For the fourth block, omit two pairs `a<b` and orient the remaining pairs by

`s(j)=sigma * chi((j-a)(j-b))`,

which gives exactly 812 two-hole codewords.

The exact meet-in-the-middle checker exhausts all `58^3*812 = 158,430,944` labelled quartets through symmetry-reduced contribution sums. It finds `130,692` symmetry-reduced hits on the first split-617 equation, `192` on the first two equations, and **zero** on the first three equations. Hence no quartet in this low-degree Paley orientation-code ansatz can satisfy all 29 equations.

Checker:

`hard8_2026-09-16/HARD8-04/artifacts/2026-09-17T01-24-57Z__d9_paley_code_exact_exclusion.py`

creation commit `b5c1f91fda6047f1142e1435862b0e55bb15c7a2`, exact readback blob `18d7d16bae803382ff50c99bba143560a51feecb`.

Executed output:

`hard8_2026-09-16/HARD8-04/artifacts/2026-09-17T01-24-57Z__d9_paley_code_exact_exclusion_output.txt`

creation commit `f1f55c3bbbaef3186c2ff9b720b399088a4e268c`, exact readback blob `3bc20bd8ffb2fceb00de790f97505d9fc33b1296`; terminates `ALL_EXACT_PALEY_CODE_EXCLUSION_CHECKS_PASSED`.

This is a restricted-family exclusion only. It is not SAT-UNSAT for all d=9 GS seeds and says nothing about unrestricted Hadamard existence at order 2092.

## Why the slot must now move on

Recovered HARD8-04 history contains more than three consecutive metric-nonmovement reports. The owner policy allowed at most two hard-target stuck-recovery cycles. They were used in

- STUCK RECOVERY 1: `hard8_2026-09-16/HARD8-04/runs/2026-09-16/2026-09-16T23-17-04Z__report.md`, commit `3f6f26a99dc0475115110a43d58c4f6dbc94af19`;
- STUCK RECOVERY 2: `hard8_2026-09-16/HARD8-04/runs/2026-09-17/2026-09-17T00-19-31Z__report.md`, commit `fbf43fe5fdd4a194c85e585a87d3bf6b651eeef6`.

The selected final execution B1/B3/B8 also failed to move the frozen metric. **Do not start STUCK RECOVERY 3 in this native slot.** A later explicit owner reassignment may revive Hadamard from this handoff, but only after fresh source/status/ownership checks and with a genuinely new route.

## Rotation state

At the captured input master `7e761e0a8b38410a678f32799b58204e76462876`, `QUEUE.md` says there are **zero newly certified READY entries**. Therefore this handoff does not invent or steal a successor. The same native slot should remain enabled as an admission/successor gate and rotate only when a source-verified, unassigned outside target is actually admitted under then-current policy. Because the visible fleet remains hard-heavy relative to the owner's approximately 60% closable / 30% hard target, prefer an eligible **CLOSABLE OUTSIDE** successor unless a newer owner directive changes that allocation.

No metric carries into the successor. No shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md` edit is authorized from this worker.

## If Hadamard is later reassigned

Start from the signed-code formulation above, not from another local annealing pass. A plausible genuinely new exact route is to encode the 29 sum-of-four-squares equations plus signed-code/binary liftability directly into a proof-producing SAT/PB/SMT system, or to discover a higher-degree global character code that is not covered by the Paley exclusion. Any UNSAT result is only for the exact encoded family. Any satisfying seed must be expanded to explicit sign sequences and then to an exact Hadamard construction with `H H^T=nI` checked exactly.

No email/Gmail, Drive, public posting, paid compute, credential access, permission change, workflow execution, force-push, peer/history edit, or shared-root edit was performed in this handoff.
