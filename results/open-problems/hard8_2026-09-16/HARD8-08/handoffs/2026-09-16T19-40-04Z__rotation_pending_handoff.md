# HARD8-08 rotation-pending handoff — 2026-09-16T19:40:04Z

## Honest state
- Source target: Hadwiger–Nelson finite unit-distance certificates.
- Frozen metric: smallest vertex count of a rigorously certified 5-chromatic unit-distance graph found by this track.
- Metric this run: **509 -> 509, no movement**. The 509 graph is Parts's external benchmark, not a track discovery.
- Status: **OPEN / PARTIAL**.
- This follows STUCK RECOVERY 1 and STUCK RECOVERY 2. Under the owner policy this slot now requires a handoff/rotation rather than a third recovery cycle.
- At the captured fleet snapshot `a524970d07ca4c142a8da6cc2a2eb19ffa4debab`, `QUEUE.md` reports **zero newly certified READY entries**. Therefore no source-verified unassigned same-category successor was available to rotate into without inventing admission. The native recurrence is left unchanged; no self-disable, new schedule, or permission bypass was performed.

## New exact construction result from this execution
Let
\[
\rho=\frac{7+i\sqrt{15}}8,\qquad \zeta_6=\frac{1+i\sqrt3}{2}.
\]
Using Parts's exact base-coordinate map and orbit generators, the connection orbit `(0,4,4,0)` has exactly 12 vertices, all at squared radius 4. Enumerating all 12x12 prospective reference edges and both line-circle roots gives 288 raw roots but only **36 exact rotations**. Their reference-edge counts are:
- 12 rotations with 12 reference edges;
- 24 rotations with 6 reference edges.
The 12 maximal rotations are exactly
\[
\{\zeta_6^k\rho^{\pm1}:0\le k<6\}.
\]

The Parts auxiliary orbit `(0,0,2,6)` also has 12 vertices, split into two regular 6-cycles with squared radii
\[
n_\pm=\frac{17\pm\sqrt{33}}6.
\]
For the same 36 reference-induced rotations, exact integer/radical arithmetic gives the complete connection histogram
\[
(\#E_{RR},\#E_{AA},\#E_{RA},\#E_{AR})=
\begin{cases}
(12,12,0,0)&\text{for 12 rotations},\\
(6,0,0,0)&\text{for 24 rotations}.
\end{cases}
\]
Hence every reference-induced rotation that also creates even one full-orbit auxiliary edge is in the historical angle class `zeta_6^k rho^{+/-1}`. The previous idea “keep the Parts reference/auxiliary mechanism but change the angle” is therefore exhausted at the exact two-orbit level.

Executed checker/output:
- `artifacts/2026-09-16T19-40-04Z__reference_rotation_atlas_exact.py`
- `artifacts/2026-09-16T19-40-04Z__reference_rotation_atlas_exact.out`
The output terminates `ALL_EXACT_REFERENCE_ATLAS_CHECKS_PASSED`.

## New genuinely different exact angle family
The same auxiliary orbit exposes the next disjoint construction family. If an auxiliary edge joins two points on the *same* radius class `n_+` or `n_-`, the required reduced relative angle `delta_+` or `delta_-` satisfies
\[
\cos\delta_\pm=\frac{2n_\pm-1}{2n_\pm}
=\frac{205\pm3\sqrt{33}}{256}.
\]
These values are exactly different from the historical `cos(alpha)=7/8`. Since each radius class is a 6-cycle under `zeta_6`, the exact candidate rotations are
\[
q_{\pm,k,\epsilon}=\zeta_6^k\left(c_\pm+i\epsilon\sqrt{1-c_\pm^2}\right),
\quad c_\pm=\frac{205\pm3\sqrt{33}}{256},
\quad k=0,\ldots,5,\ \epsilon=\pm1.
\]
At the connection-orbit level each such candidate supplies six same-radius auxiliary edges and, by the exhaustive reference-induced classification above, no reference edge. This is the smallest exact angle family that genuinely breaks the historical Type-M connection mechanism rather than reparametrizing it.

A future reassignment should test these candidates first on the exact Parts `L_374`/`S_136` data, rebuilding *all* strict unit edges in the corresponding algebraic extension and then running 4-color SAT. A SAT instance kills the candidate with an explicit replayed coloring. UNSAT only counts with a replayable DRAT/LRAT-equivalent certificate plus an explicit 5-coloring. A six-chromatic claim would separately require 5-color UNSAT and is not implied by any 4-color result.

## Search-space correction
For fixed exact `L_374` and `S_136`, there are `374*136=50,864` raw non-center vertex pairs. A genuinely new cross edge gives one linear equation in `(cos theta,sin theta)` together with the unit-circle equation, so one pair determines at most two rotation roots. The complete single-edge atlas therefore has at most **101,728 raw roots** before exact deduplication. The prior two-edge-system plan would have started from **1,293,547,816** unordered raw pair systems. The single-edge formulation is complete for rotations that create a new non-center cross-unit edge and should replace the two-edge plan.

## Neighbor and source distinctions
- P19's latest handoff exhausted fixed-Parts terminal-relation mining and explicitly recommends adding new geometry rather than more deletions inside Parts-509.
- de Grey (2018) establishes the finite 5-chromatic lower bound route.
- Heule (2018) gives mechanically validated 553-vertex graphs.
- Parts gives the 509-vertex, 2442-edge benchmark with `L_374` and `S_136`.
- Haugland arXiv:2608.04542 is a 2131-vertex **5-chromatic** Moser-spindle-free construction, not a 6-chromatic graph and not a size record.
- arXiv:2404.05509 concerns off-diagonal six-colorings; it is not a finite ordinary unit-distance graph with chromatic number 6.

## Suggested fresh methods if this problem is later reassigned
Use **B6, B16, B23**: deform from the historical cross-radius angle to the exact same-radius `delta_+/-` family; compute all 24 algebraic rotations on the full Parts L/S data; and deliberately test the opposite architecture in which the reference-edge mechanism is absent.
