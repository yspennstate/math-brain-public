# BT4 shared handoff — fleet02/B20 neutral-equality cage

Source run: `20260922T010226Z-fleet02-B20-r11`
Full report: `proofnet24/collective-BT4/fleet02/B20/20260922T010226Z-fleet02-B20-r11/report.md`
Full report commit: `49783fccebd3a6619a0ab42f4ec9ec95afb9fb12`
Outcome: `ESSENTIAL_STEP_APPLIED`; target-level BT4 status remains OPEN.

Inputs actually consumed:
- lead fleet02/B04 `20260922T001806Z-b04-bt4-a1ceeb3c` plus correction;
- named partner fleet04/B06 `20260922T001024Z-b06-bt4-r43`, report blob `08cf8f4283de825d533677d6edf5707523744a22`;
- fleet03/B05 corrected marked-segment/linkage package, blobs `f1545c2e4a546d17150bb20bbc59650a29eb2672` and `f19feaaea52a2a892e510bd8fe03dbb18290fcb5`.

New exact facts for the dynamic neutral marked-segment branch. Choose a minimum-total 3-packing secondarily minimizing `Phi=sum |Ci|^2`. For a neutral exchange around marked `w in B`, heavy target `A`, fan size `m>=3`, segment size `s`, bypass length `ell=m+s-1`, put `d=m-2`. Then:

1. `|A|-|B| <= m-2`, because the neutral replacement changes lengths by `(|A|,|B|)->(|A|-d,|B|+d)` and `Delta Phi=2d(|B|-|A|+d)>=0`.
2. If `B` is shortest and `|A|-|B|>=m-1`, equality is impossible, hence the tax is strict: `ell>=m+s`.
3. Neutral equality forces `|N-(w)∩A|=1`: equality makes `N+(w)∩A` the proper consecutive length-`m` block following any A-inport, so two distinct inports are impossible.
4. Since the normal form is 3-vertex-strong and B is chordless, a surviving neutral equality forces an additional in-neighbor `y->w` from `R` or the third packed cycle.
5. If w is a cycle-supported exact five-fan, it has a unique R-exit `w->r`. If the extra in-neighbor is `y in R`, there is no directed `r`-to-`y` path in `R-int(Q)`: otherwise that path plus `w->r` and `y->w` is a directed cycle disjoint from old A,C and the bypass cycle B_Q, giving four directed vertex-disjoint cycles.

Thus the unpaid neutral orbit is reduced to a near-balanced, unique-inport cage with a forced third-side inlink and (for five-fans) a concrete forbidden R-reachability relation. Next target: combine fleet04/B06 fan-avoiding saturation/forced exits with this cage and fleet03/B05's two-linkage trichotomy. Handle six-fans separately because they have no R-exit.

No full proof or novelty claim.
