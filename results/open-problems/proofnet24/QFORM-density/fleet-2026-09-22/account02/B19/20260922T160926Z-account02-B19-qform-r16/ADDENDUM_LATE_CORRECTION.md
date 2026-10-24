# Late source refresh: B09 stable-rank pivot theorem and same-square correction

After the primary report was committed, fresh programme main exposed account02/B09 run `20260922T160923Z-account02-B09-QFORM-r4`, canonical `yspennstate/math-open-problems@77d71ed8bbd7f8a3fd40958e54b5bf658163c27a`. I read and apply it here rather than leaving the primary synthesis stale.

B09 proves `QFORM-PIVOT-OFFDIAG-STABLERANK-v1`: for a genuine physical scalar pivot `a!=0`, if the scalar Schur complement `S` has offdiagonal stable rank at least `24`, a random physical cut plus the completed account03/B09 ridge theorem yields a bounded density. In the exact target, the window-heavy, diagonal-dominant case closes by `<340`. Therefore the live structural debt is already narrower than the primary report's generic disjoint-scalar wording: after the spectral-window branch, one only needs to route either an offdiagonal-heavy physical coordinate or a diagonal-heavy pivot whose Schur offdiagonal stable rank is `<24`.

The same B09 run independently records `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1`: `U^2+X^2+2UX=(U+X)^2` has an unbounded density at zero for independent cap-one uniforms. This is fully consistent with the primary report's half-negative-moment obstruction. The B19 example `U^2+V^2+(X-Y)^2`, whose matrix spectrum is `{2,1,1,0}`, strengthens the warning by embedding the failure of the half-moment intermediate requirement inside the exact target while showing that a second independent square can reroute the degeneracy.

## Updated conditional assembly

After applying B09, a hypothetical unresolved target matrix must evade all of the following source-valid exits:

1. the low-leverage `1/39` spectral-window theorem;
2. the complete `s_2(H)<=1/8` one-effective route of account03/B19 + account02/B19 r15 + account01/B19;
3. a diagonal-heavy physical pivot whose Schur offdiagonal stable rank is at least `24` (B09);
4. a product-compatible cross/ridge packet supplied by the B19 wedge/star theorem when it can be reserved in the relevant Schur geometry.

Thus the first unpaid synthesis implication is sharpened to `QFORM-LOW-SCHUR-STABLERANK-HEAVYBANK-ROUTING-v1`: in the remaining high-leverage branch, with either an offdiagonal-heavy physical coordinate or only diagonal-heavy pivots whose Schur offdiagonal stable rank is `<24`, prove that one can preserve an independent third smoother while grouping the low-stable-rank Schur resource into a paid hyperbolic/ridge/aggregate packet; alternatively show that failure of such grouping quantitatively forces the B19 low-leverage ridge-ready cut to survive a scalar Schur pivot. The same-square and half-moment corrections forbid paying the heavy row by the pivot that created it without a genuinely independent third smoothing resource.

No full-solution or continuity claim is added. Full QFORM remains OPEN.
