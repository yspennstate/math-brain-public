# Round 064 log

## Goal

Turn the regular-tree toy certificate from an algebra-only example into a
fully checked certificate, including its graph-specific bridge majorization.

## Built-in majorization check

Added `bridge_majorization = "regular_tree_one_state"` to the JSON format and
implemented the corresponding exact verifier.  For the \(D\)-regular tree,
\[
  B_n^{\mathrm{NB}}(s)=\frac{1}{D(D-1)^{n-1}}
\]
for all \(n\ge1\), since a nonbacktracking walk can reach a distance-\(n\)
target only by following the unique geodesic.

For a one-state certificate with scalar transition \(m\) and scalar boundary
weight \(ab\), the verifier checks the inequality
\[
  \frac{1}{D(D-1)^{n-1}}\le ab\,m^n
\]
for every \(n\ge1\).  It does this exactly by comparing \(m\) with
\((D-1)^{-1}\) and, in the supercritical scalar case, checking the \(n=1\)
constraint.

## Scope

This is intentionally narrow.  It closes the repository's regular-tree
calibration example end to end, but general graph-specific bridge
majorizations still require a radial, automaton, or transfer-matrix proof.
