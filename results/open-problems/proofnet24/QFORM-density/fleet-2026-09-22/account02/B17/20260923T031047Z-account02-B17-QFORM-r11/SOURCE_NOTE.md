# Source note for the first-order expansion

The weighted local Edgeworth statement used as equation (8.5) of `REPORT.md` is independently available as a completed proved lemma, so the first-order correction does not depend on treating the account03/B17 local-CLT tail estimate as a black-box higher-order theorem.

Canonical source:

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`

Its “Weighted local Edgeworth lemma” proves for the same normalized centered-unit-interval bank, with `sigma^2=1/12`,

\[
g_m(y)=\gamma_\sigma(y)\left[1-\frac1{20m}H_4(y/\sigma)\right]
+O(m^{-2})(1+|y|)^{-8},
\]

by the exact sinc characteristic function, Fourier inversion on an expanding central interval, the bound `|sinc u|<=min(1,|u|^{-1})` off it, and the same estimates after finitely many Fourier derivatives.

The designated partner `account03/B17` r22 source

`yspennstate/math-open-problems@f593cf73a4e7547eac4183f8e61062fca5176706`

is still actually applied in the main report: its source-valid bank local limit and explicit outer-tail bound supply the finite-bank/Gaussian compatibility and its separate two-heavy/shared-bank theorem gives the complementary exact obstruction (10.1). The account04 lemma is cited here specifically to source-pin the stronger weighted `O(m^{-2})` remainder needed for equations (8.8)--(8.10).
