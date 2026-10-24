# Round 028 log

## Goal

Check whether deeper decorated columns can improve the remaining
\(T_3\square\mathbb Z\) comparison, and sharpen the ten-height depth-one
certificate if the deeper computation is not yet competitive.

## Frontier transfer

Added a row-frontier closure counter to `scripts/decorated_strip_bound.py`.
For a side tree of fixed finite depth, the state keeps:

- the connectivity partition of the current height row,
- whether each active component is seeded,
- the set of root-fiber heights contained in each active component,
- the output root heights already closed below the frontier,
- the number of open edges used.

This avoids the dense enumeration over all edge subsets in a decorated column.
Small-window checks against dense enumeration matched exactly:

\[
  h=3,\quad \text{side-depth}=2,\quad p=3/10,
\]
with both methods giving spectral lower bound \(0.426310751826\).

Depth two is now computable, but it is not yet competitive at the tested
sizes:

\[
  h=4,\ p=3/10:\quad \rho_{\rm lower}=0.455355263995,
\]
\[
  h=5,\ p=3/10:\quad \rho_{\rm lower}=0.474980517265.
\]

## Sharpened ten-height certificate

The ten-height depth-one sparse transfer was rerun just above the observed
crossing.  At
\[
  p=\frac{5909}{20000}=0.29545,
\]
the exact integer certificate with scale \(10^8\) gives
\[
  \min_A\frac{2(M(p)v)_A}{v_A}>1.000006.
\]
Thus Yamamoto's criterion gives
\[
  p_c(T_3\square\mathbb Z)<\frac{5909}{20000}.
\]

The current SAW operator target is now
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<\frac{20000}{5909}
  \approx3.38467.
\]

This is a small numerical tightening.  The finite-length SAW certificate
\(3.647512\) is still far above the target, so the remaining case still needs
either a structural SAW operator bound or a stronger non-oriented
percolation comparison.
