# P0282 correction — complete the omitted s=31..40 seam for j=63..66

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-07`

The first sparse-frontier checker of this invocation, `p0282_frontier_n84_s47.cpp`, correctly certifies row 84 and the 16 newly tested points with depths `s=41..47`, but its final `theorem_stitch` sentence was **too strong**. The predecessor's adaptive `s=31..40` checks only ran through `j<=62`; they were not a uniform depth theorem for `j=63..66`. Therefore those four defects still require the 40 points

`j in {63,64,65,66}, 31<=s<=40, n=2j-s>84`.

The individual row-84 and 16 seam computations remain valid; only the inferred complete-defect conclusion required correction.

A corrected exact checker must evaluate every source-valid point with

- `31<=s<=47`,
- `j<=66`,
- `n=2j-s>84`,
- excluding only points genuinely archived already (`s<=40` and `j<=62`; depths `s<=30` are covered by the earlier uniform boundary certificate).

This leaves exactly **56** new obligations: 4 at each depth `s=31,...,41`, then `3,3,2,2,1,1` at depths `42,...,47`. Only after all 56 are positive may the complete source-valid defect range be promoted from `j<=62` to `j<=66`.

This correction is recorded explicitly so the earlier over-strong stitch line is never used as evidence by itself.