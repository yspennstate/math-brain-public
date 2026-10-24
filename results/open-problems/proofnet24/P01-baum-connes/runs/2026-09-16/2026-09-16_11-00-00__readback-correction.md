# ProofNet24 P01 — readback correction

This immutable addendum corrects two **typographical rendering defects only** in

`proofnet24/P01-baum-connes/runs/2026-09-16/2026-09-16_11-00-00__run-report.md`

creation commit `dd61e19f161b43dd04fc143018aed7110a33b749`, blob `d0c7b197588fd86154c5797b83fa6dac618fb791`.

No theorem statement, proof dependency, status, constant, or conclusion changes.

1. In Section 3, the sentence following `B=A+\varepsilon I` should read

\[
\|A-B\|=\varepsilon\to0,
\]

not the plain-text rendering `||A-B||=varepsilon ->0`.

2. In Section 10, after defining the normalized Chebyshev candidate, the displayed norm should read

\[
\|q_n\|_{[-1,1]}=\frac{1}{T_n(c)}.
\]

The original readback contains a malformed `\frac` rendering at that one location. Equation (10.1) immediately below already contains the correct formula.

All substantive P61A–D claims and proofs are unchanged.
