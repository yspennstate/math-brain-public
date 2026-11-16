You are working on one case of a graph inequality. Work in this folder only and write as you go: keep LOG.md current
after every step, and put the final write-up in RESULT.md. Label every statement PROVED (with an exact certificate and a
replay script), NUMERICAL or OPEN. Never present a numerical finding as a proof.

READ FIRST (read-only, do not modify): ~/agent_run/STRAT9/ - RESULT.md proves T >= 0 for the 5+1 case (a connected
five-vertex carrier holding both top eigenvalues plus one isolated vertex) at N = 6 for every frame with a <= 14/25, at
every scale when b/a <= 3/20, up to ratio-dependent ceilings V6(r) (66/125 .. 76/125), plus 47 face boxes, and states the
remaining region (11) exactly ("Remaining region specified exactly"). Its tools (frame.py, cells.py, padding.py,
moment_polytope.py, face_intervals.py, verify_*.py, replay_all.py) are your starting point: copy what you need here.
Also ~/agent_run/STRAT8/RESULT.md (the N = 5 face residual: box partition, 5,272 open leaves) for its box method.

TASK: shrink region (11), aiming to close it.
1. Map (11) numerically first: sample it (respecting every condition in (11)), record min T, min T/a^2, and where the
   pressure is (which r, which a, how close to the zero-weight face, which edge is zero). The point residual_witness.json
   has T6 > 0; find the least-T points in (11). If any point has T < 0, stop and certify it exactly - that is a
   counterexample and the most important possible outcome.
2. Extend the moment cells above a = 14/25: finer ratio strips (r intervals of width 1/50 or smaller where needed), cells
   with a split scale interval, and higher-degree multipliers if the linear-in-moments bound saturates. Each accepted
   record is exact rational, replayed by a script.
3. Where cells cannot reach (near the face, a near E), use exact interval/Bernstein boxes in the face chart as STRAT9
   did, with adaptive splitting; keep a ledger of proved / excluded / open leaves with volumes.
4. State the new remaining region exactly, as STRAT9 did, and give the before/after (the ceiling a by ratio, open leaves).
   If the method allows, repeat for N >= 7 (one isolated vertex added each time, padding identity (5) of STRAT9).
5. Write replay_all.py that reruns every exact certificate sequentially.

Keep memory under 4 GB and use at most 4 processes, single-threaded numerics (OPENBLAS_NUM_THREADS=1). No network and no
language-model workers. Write only in this folder.
