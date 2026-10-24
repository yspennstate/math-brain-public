# Readback note

Canonical report commit: `7e5b308e1db40bc40e618a03386a885425c734ed`.

One notation-only typo was found on readback in the source-premise display for `Delta_{krs}`: the second subscript set is missing its closing brace. The intended and used definition is

`Delta_{krs}=det(U_{[n]\{k,r,s}}^T U_{[n]\{k,r,s}})`.

No displayed inequality or proof step changes.

Independent diagnostic (not part of the proof): for the sharp four-row frame with row norm `1/sqrt(2)` and angles `0,pi/4,pi/2,3pi/4`, direct determinant-weight evaluation gives total pair mass `1`, maximum leverage `1/2`, and iid-pair disjointness probability `3/16=0.1875`. A small random Parseval-frame scan with maximum leverage at most `1/2` found no value below `3/16`; the analytic proof in `REPORT.md`, not this diagnostic, establishes the theorem.
