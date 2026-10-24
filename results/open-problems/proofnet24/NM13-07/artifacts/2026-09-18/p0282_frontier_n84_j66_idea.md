# P0282 idea before archival checker — sparse moving frontier at n=84

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282`  
Frozen metric on entry: `N_exact = 83`  
Source status on entry: `OPEN`; worker status `PARTIAL`

All thirty numbered Section-B methods have already been genuinely used on P0282, so no report can truthfully supply three previously unused method numbers. This run therefore uses a different recycled triple from the preceding run and labels it honestly: **#4 PROVE SOMETHING WEAKER, COMPLETELY; #13 FIND WHAT ONLY INCREASES; #30 DO ONE SCALE, ONE DIRECTION AT A TIME — all RECYCLED.** The mathematical route is new even though the menu labels are not.

## Route A — prove the next finite wedge completely (#4, recycled)

The current exact certificates give:

- complete fixed-size rows through `N=83`;
- an adaptive exact tail-correction seam sufficient to cover every source-valid fixed defect `j<=62`;
- the next defect `j=63` has exactly two uncovered points, `(n,s)=(84,42)` and `(85,41)`, where `s=2j-n`.

A full exact row-84 certificate would absorb the first point automatically and move the frozen metric. The remaining point can be evaluated by the existing finite Plancherel-tail correction. Rather than stop at `j=63`, target the smallest sparse frontier that buys several complete defects at once.

## Route B — use the coverage potential as a monovariant (#13, recycled)

For certified complete rows through `N` and certified tail depths through `S`, the coverage-frontier lemma gives complete fixed-defect coverage through

`J_complete = floor((N+S+1)/2)`.

Treat `C=N+S` as a coverage potential: any exact increment in either row depth or tail depth can only increase the guaranteed complete-defect frontier. With `N=84`, choosing `S=47` gives

`floor((84+47+1)/2)=66`.

This is a source-relevant monotone target: if the necessary seam passes, the complete fixed-defect theorem advances from `j<=62` to `j<=66` while the frozen row metric advances from 83 to 84.

## Route C — one depth at a time on the actual seam (#30, recycled)

Do not compute the whole rectangle `41<=s<=47, 4<=j<=66`. Evaluate only source-valid points not already covered by rows `n<=84`:

`41<=s<=47`, `j<=66`, `n=2j-s>84`, `n>=j+2`.

There are only 16 such obligations (counts by depth `s=41,...,47`: `4,3,3,2,2,1,1`). This sparse wedge contains the entire missing source obligation for defects through 66.

## Exact verification plan

1. Enumerate every partition of 84, compute hook-length dimensions, accumulate RSK counts `ell_{84,k}`, independently verify the Euler partition number and `sum_k ell_{84,k}=84!`, and test every source Turan margin. This alone is allowed to move `N_exact` from 83 to 84.
2. Reuse only the already-proved fixed-defect recurrence/completion formula and the finite Plancherel-tail correction, but instantiate it solely on the 16 uncovered seam points. Any nonpositive genuine source margin is a source-valid counterexample and stops the run.
3. Independently cross-check the deepest newly introduced endpoints by direct RSK/hook enumeration at the small rows `n=s+4` for `s=41,...,47`.

The theorem delta `j<=66` is not a replacement metric. The source conjecture remains the all-`n`, all-`k` statement and remains OPEN unless a genuine source counterexample or complete proof is obtained.

## What would count as failure or new information

- A negative row-84 margin would refute the source conjecture.
- A nonpositive seam margin would also refute it at an explicit source-valid `(n,k)`.
- If all tests pass, the useful research output is the exact moving-frontier theorem plus the identification of the next sparse obstruction, not merely another larger checker.