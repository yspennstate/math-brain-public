# B16 handoff — dummy-tower Ward/plaquette renormalization

Status: **PARTIAL / PROVED AUXILIARY IDENTITIES / FULL FEI OPEN**. Execution: **WITHOUT_VERIFIED_BRAIN**.

## New proved statement

Let arbitrary old Boolean phases `g_v` be lifted through `d` dummy coordinates. Split each phase into its `2^d` dummy-slice clones `h_{v,y}` and use the block-coupled selector: uniform old-block order, every clone block contiguous, uniform internal order. Then

\[
\sum_y\phi^{blk}_{v,y}=\phi_v,\qquad
\phi^{blk}_{v,y}=2^{-d}\phi_v.
\]

For the entropy game, if `C^{(d)}_{v,y}` is the exact signed plaquette-curvature telescope for clone `(v,y)`,
\[
C^{(d)}_{v,y}=H(h_{v,y})-2^{-d}\phi_v,
\]
so
\[
\sum_y C^{(d)}_{v,y}=\sum_yH(h_{v,y})-\phi_v.
\]
This is an exact all-depth dummy Ward identity; no curvature is positive-parted.

For an ordered-min codimension-`c` subcube dual, every clone is codimension `c+d`. In the isolated-block case the exact curvature refund is
\[
R_{c,d}=2^dH_{c+d}-H_c>0,
\]
with
\[
R_{c,d}=\sum_{r=0}^{d-1}2^r(2H_{c+r+1}-H_{c+r})
      =8d2^{-c}+O_c(1).
\]
The positivity follows from strict decrease of `H(q)/q` in the defect density `q`; the derivative is given explicitly in REPORT.md.

## Why it matters

The fresh one-sided multiplier theorem leaves the raw constant displacement mode as a principal obstruction. This handoff proves that its entire growth caused solely by dummy padding is an exact signed plaquette refund. A correct universal transport payment can therefore be required to be **dummy-stable** before the remaining constant mode is charged. The remaining unpaid part is the essential-coordinate constant mode plus genuinely negative nonconstant modes of the fully refunded residual; terminal-band and R16/moment ledgers remain separate and unchanged.

## Executed check

`check_dummy_tower_curvature.py` passed two general Boolean-game coupled-selector/plaquette checks (48 and 1,152 selector orders), plus 56 subcube tower cases. Maximum general-game plaquette-telescope error was `1.18e-14`; the displayed layer telescope had zero binary64 discrepancy. Checker SHA-256: `91ab5f29c1cd3e7279d535c2d996c37d67fdab5a104a42f02e224a441bbcfa89`. Output SHA-256: `82359e08b01b35d17f52d696a43747c5189122f6255d3a3026c22cddcf930fee`.

## Next B16 target

Work on the **dummy-stable quotient residual**, not the raw ordered-min baseline. Insert the exact q-flip cut sign
\[
\widehat p_i(U)=-2\widehat\eta_i(U)^2\le0\quad(U\ne0)
\]
before taking a norm. Seek (i) a one-sided lower multiplier bound for every nonconstant quotient mode and (ii) a direct signed payment for the remaining essential constant mode using the retained plaquette/terminal/R16 ledgers. Do not revert to the killed generic endpoint `L2`, basiswise pointwise q-flip, absolute-reflection, or raw-positive-baseline shortcuts.
