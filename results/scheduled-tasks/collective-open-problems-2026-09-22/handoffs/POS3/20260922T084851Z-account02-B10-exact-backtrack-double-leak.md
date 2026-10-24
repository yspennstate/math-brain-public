# POS3 handoff — exact-backtrack double leakage

**Source run:** account02/B10 `20260922T084851Z-b10-pos3-r12`  
**Canonical science report:** `proofnet24/collective-POS3/account02/B10/20260922T084851Z-b10-pos3-r12/REPORT.md`, commit `57a563af112063929fae35a4aa28c4fe61aa64cf`, blob `0d6b6aaf49e848e27daf8bc78d672cb28ed58aa4`.  
**Status:** `ESSENTIAL_STEP_APPLIED`; parent POS3 remains OPEN.

## New exact implication

In the lead's heavy exact-backtrack bridge

`p lessdot r`, `q||p,r`, `p prec_* q prec_* r`,

write

`A=#{p<r<q}`, `H=#{p<q<r}`, `B=#{q<p<r}`, `E=A+H+B`.

For the full-law endpoint-position swap on `(p,q)`, let `O_L` be the outgoing illegal-swap set. The exact defect identity and the fact that every `A`-cell extension is centrally defective give

`|O_L cap H| >= H-B`.

Dually for `(q,r)`,

`|O_R cap H| >= H-A`.

Every defect in these middle-cell sets needs a **noncentral** Hasse witness. Width three leaves at most three external Hasse channels per side, because the central witnesses `r in U(p,q)` and `p in D(q,r)` already occupy one of the at-most-four channels.

The two external witness families are vertex-disjoint:

`((U(p,q) union D(p,q))\{r}) cap ((U(q,r) union D(q,r))\{p}) = emptyset`.

The four possible type intersections are ruled out respectively by `q<z` versus `z||q`, `z<q` versus `z||q`, a cycle `z<q<z`, or `p<z<r` contradicting the cover `p lessdot r`.

Hence a literal exact backtrack is never a closed two-state recycler: it has noncentral outgoing defects on both sides.

In the lead's low-endpoint branch `A,B<3E/11`, where `H>5E/11`, one left external channel and one right external channel, on distinct vertices, each carry strictly more than `2E/33` full extensions. Under no-balance, each is either a strict span-descent exit or an outward minority packet `>2/33`.

The named partner account03/B11 r11d factor-two identity additionally eliminates the minimum-support subcase where a side has exactly two total distinguishers and the external same-sign distinguisher is comparable with the central one: it would force `N(q<r)=2N(q<p)` on the left or `N(p<q)=2N(r<q)` on the right, contradicting the adjacent `>2/3` strong-majority inequalities.

## Next unpaid implication

`POS3-DISJOINT-DOUBLE-LEAK-REUSE-v1`: in a span-descent-exhausted candidate, show that the two disjoint `>2/33` packets forced by every low-endpoint exact backtrack cannot both be routed through later envelope expansions and reused indefinitely without balance, span descent, width four, a proper autonomous/ordinal reduction, or an already controlled exact-two/coherent-gate state.

All counts are on the original uniform set of full linear extensions; no deletion law is uniformized. No finite census is used.
