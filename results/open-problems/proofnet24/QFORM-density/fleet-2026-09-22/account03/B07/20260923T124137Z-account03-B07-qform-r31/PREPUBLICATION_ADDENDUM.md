# Pre-publication correction and status

This addendum is authoritative for one elementary inequality in `REPORT.md` Section 5.1.

The report sentence

> Also `h<1`, so `h/400 > h^2/64 = 2 tau0`.

uses a premise that is true but unnecessarily too weak for the displayed implication. Replace it by the following rigorous statement:

`h=(2sqrt(2)-1)/1572864 < 2/1572864 < 4/25`,

and therefore

`h/400 > h^2/64 = 2 tau0`.

Indeed, after dividing by the positive `h`, this is exactly `h<64/400=4/25`.

Thus the subsequent conclusion `|b|>2tau0`, indefiniteness of the selected physical pair, the determinant bound `D>(3/4)b^2`, and the singular-value bound `kappa>|b|/2` are unchanged.

No other theorem statement or constant in `REPORT.md` is changed by this correction. Full QFORM remains open; full-target continuity remains open.
