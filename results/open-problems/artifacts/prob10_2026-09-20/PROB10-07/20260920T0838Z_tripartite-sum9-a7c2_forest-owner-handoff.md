# PROB10-07 -> forest-owner handoff: complete-tripartite width nine

This is a non-mutating handoff for readers of the historical P14/HARD10-01 uniform-forest work. It does not edit or seize any P14/HARD10-01/NM13 claim and does not repeat their graph-order enumeration.

Parent source: Grimmett–Winkler pairwise edge negative correlation for the uniform measure on **all forests** of an arbitrary finite graph. Parent status remains **OPEN / PARTIAL**.

Historical owner state consumed before this run:

- `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`: complete arbitrary-simple-graph order metric remains 9; vertex-minimal counterexample may be taken 3-connected; generic three-terminal/star-mesh mixed term remains the obstruction.
- `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`: same order-nine baseline and explicit environmental-covariance / three-cut blocker; HARD10-01 itself rotated away after its allowed recovery cycles.
- newest neighboring structural work read in this run includes `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T08-19-21Z__triangle-right-p6-sign-theorem.md` and `proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T07-40-30Z__p6-path-recurrence-report.md`. Those tracks treat three-terminal join/layer/path families; this PROB10-07 result instead treats a fixed complete-bipartite terminal core and an independent repeated third part.

## New restricted theorem

For every integer `n>=1`, every distinct present edge pair is strictly negatively correlated under the uniform measure on all forests of each of

- `K_{1,8,n}`;
- `K_{2,7,n}`;
- `K_{3,6,n}`;
- `K_{4,5,n}`.

Together with the preceding PROB10-07 width-1 through width-8 results, this proves the source inequality for every complete tripartite graph `K_{r,s,t}` with sorted part sizes `r<=s<=t` satisfying

`r+s <= 9`.

This is an infinite-parameter structural-family theorem. It does **not** move the complete arbitrary-graph order metric, which stays `9 -> 9`, and it is not a universal resolution.

## Certificate mechanism

The proof uses all `Bell(9)=21147` connectivity partitions of the nine fixed terminals. One unmarked third-part vertex has exact transition `M=10 I+N`, with `N^9=0` because every `N` transition strictly coarsens the terminal partition. Exposing the at most two repeated-part vertices incident with a marked edge pair reduces every marked forest count to `10^x` times a degree-at-most-eight polynomial. Across the four new families there are exactly 55 edge-pair symmetry orbits. Every normalized Rayleigh polynomial has nonnegative exact rational monomial coefficients and is strictly positive at the first physical integer parameter.

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2_checker.py`

Executed output:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2.out`

The output terminates `PROB10_07_TRIPARTITE_SUM9_EXACT_PASS`. It additionally brute-force checks every one of the 136 actual edge pairs of `K_{1,8,1}`, finding 30,618 forests and minimum Rayleigh numerator 2,125,764.

The full immutable run report is:

`runs/prob10_2026-09-20/PROB10-07/20260920T0838Z_tripartite-sum9-a7c2.md`

The earlier R13 target remains preserved at `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`.

No independent audit is claimed here. External novelty/priority of the complete-tripartite theorem remains UNVERIFIED.