# r43 partner-scope supplement

This supplement records a source-scope correction discovered in the final readback/search pass. It does **not** alter Theorem 2.1, the anchored rank-one determinant identity, or the density/time bounds in `REPORT.md`.

The designated partner source

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260922T193150Z-account04-B03-collision-l2-r1/REPORT.md`

contains a false advertised two-square unweighted `L^2` compiler. The correction is source-pinned in account03/B03 r19:

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T212648Z-account03-B03-QFORM-r19/REPORT.md`.

The false step drops a factor `|t|^(1/2)` in a Cauchy--Schwarz identity and has wrong common coefficient homogeneity. **None of that false compiler is used in r43.**

The only account04/B03 r1 statement consumed in r43 is its valid elementary collision lemma

`P(|Y-Y'|<=epsilon) <=2 epsilon ||p_Y||_2^2`,

which account03/B03 r19 explicitly identifies as the partner's valid step and applies after repairing the surrounding theorem. In r43 the one-copy `L^infinity` theorem is proved independently first by the new triangle Plancherel argument; then `||p||_2^2<=||p||infinity` and the valid collision lemma give the displayed partner-consumed collision inequality.

Thus the partner application remains valid, but its provenance is deliberately narrowed to the corrected sublemma. The false `QFORM-COLLISION-L2-COMPILER-v1` is not revived.

`QFORM_B03_R43_PARTNER_SCOPE_PASS`
