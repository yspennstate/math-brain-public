# Round 071 log

## Goal

Calibrate the bounded-degree raw-count detour certificate on a non-regular
quasi-transitive tree.

## Semiregular-tree calibration

Added Example `semiregular-tree-detour`.  For the \((a,b)\)-semiregular tree,
put
\[
  r=(a-1)(b-1)>1.
\]
The two-type branching threshold gives
\[
  p_c(T_{a,b})=r^{-1/2}.
\]
A two-type Schur estimate for the distance-sphere kernels gives
\[
  \rho_{\mathrm{sph},2}(T_{a,b})\le r^{1/4},
\]
so
\[
  p_c(T_{a,b})\rho_{\mathrm{sph},2}(T_{a,b})\le r^{-1/4}<1.
\]
Since a tree has only the geodesic nonbacktracking walk between vertices at
their graph distance, \(V_n^{\mathrm{NB}}(p_c)=1\) for every \(n\).  Thus the
bounded-degree detour certificate applies with \(M=(1)\).

## Exact rational checker calibration

Added `semiregular_tree_2_3_detour.json`.  It records the rational bounds
\[
  q=\frac34,\qquad R=\frac32,\qquad M=(1),
\]
and the checker verifies
\[
  (q\lambda)^2R=\frac{27}{32}<1.
\]
The shared one-state tree detour majorization now covers both the regular-tree
and semiregular-tree detour calibrations.
