# BT4 handoff — fleet04/B05 five-remainder exclusion

Source run: `proofnet24/collective-BT4/fleet04/B05/b05-20260922t031519z-r32/report.md`  
Candidate: `BT4-COUNT-v4-FIVE-R-EXCLUSION`  
Outcome: `ESSENTIAL_STEP_APPLIED`, not a full proof.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Inputs actually consumed

- lead fleet02/B04 `20260922T022208Z-b04-bt4-r11`, report blob `930c6906cc2532269bc35e0d0b0ea8e246eb250b`, controlling correction blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`;
- named partner fleet01/B06 `BT4-GATE-ESCAPE-v1`, blob `adb2dcf7289ec7290cfc75ad760355ff540dff3d`;
- fleet01/B06 fixed-pair/collar theorem from `20260922T013522Z-b06-bt4-r11`;
- fleet03/B05 support-correct linkage/tax, blob `f1545c2e4a546d17150bb20bbc59650a29eb2672`.

## New proved step

In the inherited exact-seven oriented minimum-counterexample normal form, a global `NO-SIX` state with `|R|<=5` cannot be simultaneously no-cross and no-neutral.

An `R`-supported five-witness already forces cross/equality or `|R|>=7` by the fleet01/B06 three-collar theorem. If all witnesses are cycle-supported, choose one heavy witness `z` with heavy fan `m>=3`. The corrected lead state supplies a heavy-cycle inport in the no-cross branch. Directed Menger gives two internally disjoint `z^-`-to-`z^+` paths avoiding `z`; no-cross forces both to avoid the other packed cycles, so fleet03/B05 extracts two `R`-internal marked-segment bypasses with disjoint interiors. The segment tax is `ell_j >= m+s_j-1`. If equality holds, the `m` distinct positive fan distances are exactly `1,...,m`, and the farthest target gives a size-neutral exchange. Excluding neutral exchange therefore gives `ell_j >= m+s_j`, so each bypass uses at least `m>=3` internal remainder vertices. Thus `|R|>=2m>=6`.

## Exact six-remainder boundary

If `|R|=6` and cross/neutral outputs are still excluded, every five-witness is cycle-supported and every chosen witness has heavy fan `m=3`, pair split `3+2`, and two length-four singleton-segment bypasses from `z^-` to `z^+`; their two three-vertex internal sets partition all six vertices of `R`.

For the at-least-three witnesses of a fixed pair, two share a heavy target. The newest fleet01/B06 common-gate theorem then forces, in the same no-cross/no-neutral branch, a strict transverse `R`-bypass across a common gate on that heavy packed cycle.

## Next exact obligation

Close the **six-remainder two-axis core**: combine the witness-specific two-chain partitions of `R` with the same-heavy transverse gate bypass to force a legal two-cycle reconstruction, a neutral exchange, a cross-packed transition, a directed cycle in an exchanged remainder, or a SIX configuration.

Do not assume different witness partitions are distinct or probabilistically independent. `H6`, `HX`, and all `|R|>=7` strict-collar states remain live.
