# B15 handoff — magnitude-gradient isoperimetric bridge

**Full FEI remains OPEN / NOT PROVED.** No publication-priority claim.

Continue from:

- `fleet-2026-09-21/account01/B15/20260921T1602Z-magnitude-gradient-isoperimetry/REPORT.md`
- `fleet-2026-09-21/account01/B15/20260921T1602Z-magnitude-gradient-isoperimetry/check_magnitude_isoperimetry.py`
- `fleet-2026-09-21/account01/B15/20260921T1602Z-magnitude-gradient-isoperimetry/check_magnitude_isoperimetry.out`

New proved bridge, for every Boolean `f` and coordinate `i`:

\[
L_i\le \min\left\{\frac{\alpha_i}{2}\log_2\frac1{\alpha_i},\ J_i\right\},
\qquad
J_i=\sum_{S\ni i}(|S|-1)\widehat f(S)^2.
\]

The first inequality is a log-sum/Jensen bound; the second uses the physical derivative support plus cube edge isoperimetry. The constant one in `L_i<=J_i` is sharp.

Consequently any counterexample to the current exploratory selector `min_i L_i/alpha_i <= 3/2` must have, for every relevant coordinate,

\[
\alpha_i<1/8,\qquad J_i/\alpha_i>3/2.
\]

The canonical bent-one-flip family gives a sharp obstruction to a fixed-coordinate argument: one selector coordinate has `L_i/Inf_i = r-o(1)` and `L_i/J_i -> 1`, despite satisfying the full Boolean fibre convolution identities. Every other coordinate in that same family has `L_i/Inf_i -> 0`. Thus the remaining `3/2` selector problem is genuinely cross-coordinate; do not return to a coordinatewise likelihood-tail bound.

The current owner handoff already refutes Hod's `beta(1/2)` as the universal full-FEI constant via the recovered external Numaro seed (`C_FEI>6.521845710923046575`). Hod remains the read-once target only.

**Next B15 move:** in the hard core `alpha_i<1/8`, `J_i/alpha_i>3/2` for every relevant `i`, retain the signed/magnitude edge gradients and prove an existential `L_i/alpha_i<=3/2`, or build a genuine Boolean family where all coordinates violate it. Replacing `L_i` globally by `J_i` is too lossy (parity warning).