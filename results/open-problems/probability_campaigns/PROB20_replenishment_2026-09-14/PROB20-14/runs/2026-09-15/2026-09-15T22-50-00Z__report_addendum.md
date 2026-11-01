# PROB20-14 — notation/logic addendum to 2026-09-15T22:43:38Z report

**SOLUTION STATUS: PARTIAL (unchanged).**

Two clarifications to the preceding append-only report:

1. In equation (6.1), the left side is the convolution mass of the excess-total-progeny law and must read
   \[
   \boxed{u_m^{*b}\le K_\varepsilon(1+\varepsilon)^b u_m.}
   \]
   The displayed source text accidentally contains `\nu^{*b}_m`; this is a notation typo only. Equations (5.1)–(5.6), (6.2)–(6.4), and all subsequent uses correctly concern the law `u`.

2. In Theorem 8.1, if the shift `C>M`, then by convention `u^{*B}_{M-C}=0`, so the domination argument only needs (6.3) on `0<=C<=M`. The claimed equivalence in (8.4) is genuinely two-sided: if the total local-ratio limit (2.5) holds, then after subtracting the already convergent `H` contribution (Theorem 7.1) and the convergent finite set `G cap {B<=J}` (8.3), the remaining nonnegative term converges for each fixed `J` to `E[B;G,B>J]`, which tends to zero as `J->infinity` because `E B<infinity`. Conversely, (8.4) plus those two convergent pieces gives (2.5).

No mathematical claim beyond these clarifications is changed.
