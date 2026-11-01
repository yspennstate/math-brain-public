# P0282 idea before archival checker — stitch row and depth certificates on the exact uncovered frontier

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282`  
Frozen metric on entry: `N_exact = 82`  
Source status on entry: `OPEN`; worker status `PARTIAL`

All thirty numbered Section-B methods have already been used at least once on P0282. Therefore this run must use recycled labels honestly while making a mathematically new attack. Planned labels are #11 DUALIZE, #27 SWAP THE QUANTIFIERS, and #19 MAKE IT AN ALGORITHM; all three are **RECYCLED**.

## New route

The preceding run has two different exact certificate families:

1. complete fixed-size rows through `n <= N`, currently `N=82`;
2. exact tail-corrected boundary layers `s = 2j-n <= S`, currently `S=30`, for the relevant defect range.

These should not be treated as unrelated partial results. For a fixed defect `j=n-k`, source validity is `n>=j+2`. A point not covered by the complete rows has `n>=N+1`. A point not covered by the depth theorem has `s=2j-n>=S+1`, equivalently `n<=2j-S-1`. Therefore no uncovered point exists whenever

`N+1 > 2j-S-1`,

i.e.

`2j-S <= N+1`.

So, provided the depth theorem is available for the needed defects, row coverage through `N` plus depth coverage through `S` proves the full source inequality for every defect

`j <= floor((N+S+1)/2)`.

This immediately corrects an undercount in the previous prose: with the already archived `N=82` and `S=30`, the union of those certificates already covers **every source-valid n for defects j<=56**, not merely j<=32. This is a derived corollary of archived exact results, not a new finite computation.

## Adaptive frontier rather than another rectangle

The goal of this run is to move the source-relevant complete-defect frontier efficiently, not to scan another large `(s,j)` box.

If a complete row `n=83` is certified and the depth frontier is extended to `S=40`, the coverage formula becomes

`floor((83+40+1)/2)=62`.

But most points with `31<=s<=40` are already covered by rows `n<=83`. The checker should evaluate **only** source-valid pairs satisfying

- `31 <= s <= 40`,
- `j <= 62`,
- `n=2j-s > 83`.

Those are the exact seam points not covered by the two existing certificate families. This is the quantifier swap: instead of proving a rectangle and then asking what it buys, first specify the desired complete-defect conclusion and enumerate only its missing obligations.

## Exact verification plan

Use exact integer arithmetic only.

- For row 83: enumerate all partitions of 83, compute hook-length dimensions, accumulate the RSK counts `ell_{83,k}`, independently check the partition number by Euler's generalized-pentagonal recurrence, check `sum_k ell_{83,k}=83!`, and test every Turan margin.
- For each new seam point: use the already proved fixed-defect completion recurrence and the preceding run's exact finite Plancherel-tail correction formula; test the genuine source margin, not the uncorrected polynomial surrogate.
- Independently cross-check the deepest new boundary endpoints by direct RSK/hook enumeration in small rows.

The frozen metric remains `N_exact`; it may move only if the entire row 83 passes. The complete-defect frontier is a theorem delta, not a replacement metric.

## Failure criterion and next obstruction

If any seam margin is nonpositive, stop and report the exact source-valid counterexample. If the seam passes, the next uncovered defect after `j<=62` is `j=63`; at `(N,S)=(83,40)` its two missing source points are exactly `n=84,85`, equivalently depths `s=42,41`. That two-point seam is the next structural target, not a blanket deeper scan.
