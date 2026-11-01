# Correction to REPORT.md Section 5

The displayed partner inequality is correct:

`|phi_(Q_m)(t)| <= min(1, sqrt(pi*m/(2|t|)))`.

One following prose sentence in `REPORT.md` misstated the scaling inside the **squared** estimate. The correct statement is:

- the squared estimate `|phi|^2 <= pi/(|t b|)` has coefficient of order `m` when `|b|<=2/m`;
- the amplitude estimate has coefficient of order `sqrt(m)`;
- its `|t|^{-1/2}` exponent remains nonintegrable.

No theorem statement, construction, spectrum calculation, or conclusion changes. This correction is preserved separately rather than rewriting the immutable report.
