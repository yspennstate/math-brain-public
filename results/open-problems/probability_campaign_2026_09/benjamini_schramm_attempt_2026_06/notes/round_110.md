# Round 110 log

## Goal

Record how large an annular obstruction witness must be.

## Result

Added `lem:annular-profile-size-bounds`.

For every annulus or shell set \(I\),
\[
  \frac{\mathcal R_p^I(K)}{\bar\chi_p}
  \le
  \min\{1, |K|/\bar\chi_p\}.
\]

Updated `prop:dyadic-annular-obstruction` so the concrete witnesses can be
chosen with
\[
  \mathcal R_p^{>2^J}(K)/\bar\chi_p>2\epsilon,
  \qquad
  |K|>2\epsilon\bar\chi_p.
\]

## Interpretation

Any failure of far-leg tightness requires finite sets whose size is comparable
to the near-critical susceptibility.  The obstruction is therefore
macroscopic, not a bounded-set or small-cluster artefact.
