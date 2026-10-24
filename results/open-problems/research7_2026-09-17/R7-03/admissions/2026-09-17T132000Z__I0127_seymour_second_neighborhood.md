# R7-03 admission record — I0127 / Seymour's Second Neighborhood Conjecture

Date: 2026-09-17 UTC  
Worker: R7-03 Boundary-Case Research  
Native scheduler ID: `6aabe7be74008191b526b109ee4e9e80`  
Captured master at opening: `1bc1730f533ba3a8a1852bb498aed9905a4ebc4c`; fresh pre-claim master later rechecked separately.

## Outside source and exact target

Canonical candidate: `I0127`.

Full source target (classical Seymour Second Neighborhood Conjecture, proposed by Paul Seymour circa 1990 and first published in the Dean–Latka line): every finite **oriented graph** `D` (finite simple digraph with no pair of opposite arcs) contains a vertex `v` such that

`|N_2^+(v)| >= |N_1^+(v)|`,

where `N_1^+(v)` is the out-neighborhood and `N_2^+(v)` is the **exact** second out-neighborhood: vertices reachable from `v` by a directed path of length two, excluding `v` and excluding direct out-neighbors.

Modern source restatements/current-status anchors checked for this admission:

- Stanisław M. S. Halkiewicz, *Seymour's Second Neighbourhood Conjecture for Oriented Graphs of Order at Most Seven and Split-Twin Extensions*, arXiv:2601.21563 (2026), which states the full conjecture and gives an exact exhaustive verification through order seven.
- Yandong Bai, Binlong Li, Boram Park, *Towards a strengthening of the second neighborhood conjecture*, arXiv:2607.18047 (20 July 2026), whose abstract explicitly says the general conjecture remains open and proves a stronger matching statement when minimum outdegree is at most 5.
- Arpan Sadhukhan, R. B. Sandeep, Sagnik Sen, *A proof of Seymour's second neighborhood conjecture for oriented graphs with minimum out-degree equal to 7*, arXiv:2606.30588 (29 June 2026), claiming the minimum-outdegree-7 case and recording Kaneko–Locke's older theorem through minimum outdegree 6.
- Jake Brukhman, *A dense-case theorem for Seymour's second neighborhood conjecture*, arXiv:2608.11530 (12 August 2026), proving the conjecture when `n <= 2 delta + 2`, where `delta` is minimum outdegree.

Current-status check dated 2026-09-17: bounded web/arXiv searches for the exact conjecture and 2026 follow-ups found the above partial results and later strengthening work, but no unrestricted proof or counterexample. This is bounded negative evidence, not a novelty certificate.

## Ownership, aliases, exclusions, and prior attempts

The live queue row `I0127` is PENDING / counterexample-shaped and requires fresh admission. The R7 shard check is valid:

`sum(ord(c) for c in "I0127") mod 7 = 2`,

so it belongs to R7-03's deterministic initial shard.

At captured master `1bc1730f533ba3a8a1852bb498aed9905a4ebc4c`, direct fetch of `operations/claims/I0127.md` returned 404. Repository search for the exact ID plus `Seymour second neighbourhood` returned only the queue proposal; no prior fleet proof package, canonical owner, POSTED entry, or INDEX closure was recovered. Immediately before the canonical claim, the claim path is rechecked at fresh master and must still be absent.

This target is distinct from active Caccetta–Häggkvist, Sullivan, tournament-only, strengthened matching, and random-graph variants. Those do not replace the full source quantifiers.

## Honest classification and frozen metric

Classification: **HARD OUTSIDE with a closable finite boundary milestone**. It is not relabeled CLOSABLE merely because finite order cases can be certified.

Frozen metric:

`n_SSNC := largest integer n such that the full Seymour conjecture is rigorously known for every oriented graph with at most n vertices`.

Admission baseline: `n_SSNC = 18`, conditional only on accepting the two current 2026 preprints as mathematical inputs in the literature baseline. Reason: Sadhukhan–Sandeep–Sen rule out counterexamples with minimum outdegree at most 7; any remaining counterexample has `delta >= 8`. Brukhman's theorem covers every graph with `n <= 2 delta + 2`; therefore every `n <= 18` is covered. Brukhman's own abstract states the equivalent consequence that, conditional on the minimum-outdegree-7 preprint, a counterexample has order at least 19.

The first concrete milestone is `n_SSNC: 18 -> 19`. For order 19, Brukhman's theorem handles every hypothetical counterexample with `delta >= 9`, so the only unresolved degree slice is exactly

`n = 19, delta = 8`.

A proof of this finite slice moves the metric to 19 but is **PARTIAL** relative to the full source conjecture. A single exact oriented-graph counterexample at any order refutes the full source.

## First attack plan

Initial Section-B methods required for R7-03:

- **B2 ATTACK THE NEGATION FIRST:** model a 19-vertex counterexample with minimum outdegree 8 and exact second-neighborhood constraints; any feasible candidate must be exact-checked. A solver timeout is not a counterexample or infeasibility proof.
- **B6 DEFORM TO A POINT YOU CAN SOLVE:** start from Brukhman's solved dense case `n = 2 delta + 2` and isolate the one-unit slack that appears at `n = 2 delta + 3`, here `(n,delta)=(19,8)`.
- **B30 ONE SCALE / ONE DIRECTION AT A TIME:** convert the dense proof's global double count into target-by-target trap inequalities and classify the remaining degree/slack patterns before any large computation.

No claim of novelty is made by this admission. Full source closure still requires source-level resolution, current prior-art checks, applicable certificates, independent P26 plus one distinct OTHER-track audit, and a self-contained paper package.
