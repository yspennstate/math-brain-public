# account04/B16 source-bound handoff — n18 first-cell baseline resolution

Run `b16-20260922t071429z-fei`, `WITHOUT_VERIFIED_BRAIN`.

Scientific source: `yspennstate/math-open-problems` commit `4b412ca837f4cba03b8945bde18b729581ace0b0`, package `proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260922T071429Z-n18-first-cell-baseline-resolution/`.

For account02/B16's exact composition-prime n=18 coherent-core bias point `u=1/5000`, both source arguments lie in the first committed baseline h96 cell `[1023/2048,1/2]`.  Decoding the first two binary64 G-values from committed baseline blob `1e2a1a5c293fa7b6ec9885b7a410910d6589be80` and enclosing `log2(1024/1023)` by rational atanh series gives

`30.0783796336058879347644507621723 < m_base < 30.0783796336058879347644507621724`.

The account02/B16 exact two-secant checker gives the equal-slope sign threshold
`mcrit = 12.6198355627019584068997717383...`.  Therefore the lifted committed baseline is safe at this point:

`D_*(1/5000) > 2.0249775625876039e-6`,

and, in the owner's comparable units,

`c_F(1/5000) < 0.268197060593991735 < a_* = 0.268204856`.

The coherent bias still raises the margin above the center `0.268182843692...`; it simply does not cross the lifted baseline threshold at this finite point.  Thus the singular leading term alone is insufficient for this baseline.

The newer named `cert_vi_h96k40_f4.npz` bytes remain absent from the authorized repository path seen in this run.  If f4 uses the same first affine cell, the entire point is decided by one scalar: `m_f4 > mcrit` safe, `m_f4 < mcrit` falsified.  Do not transfer the baseline slope to f4 without the actual bytes.

Required older signed dependencies were re-read and preserved, not re-spent: account02/B16 actual parent weights revision `7f9fdcbbba89432301a5e32985ae2bd3e7b1ac5e`; account03/B18 signed flag-curvature revision `4843e50690013fd18b85dd8763b53bdc75da79e8`.  Orientation, opposite-sign overlap, dual-code multiplicity, negative credits and terminal/live-window terms remain live at their proved scopes.

Full unrestricted FEI remains OPEN / NOT PROVED.
