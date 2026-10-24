# P0072 proof-artifact display correction

This addendum records one transcription-only correction to the immutable mathematical artifact

`research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T063200Z__P0072_spanning_forest_dual_and_suspension_ODE.md`.

In Section 2, the displayed martingale-drift calculation should read

\[
\mathbb E[\Delta M_{ij}(n)\mid\mathcal F_n]
=
\frac{p_{si}}{W_{si}}+\frac{p_{it}}{W_{it}}
-\frac{p_{sj}}{W_{sj}}-\frac{p_{jt}}{W_{jt}}
=0.
\]

The earlier artifact dropped the backslash in the third `\frac` during serialization. No mathematical assertion, proof step, or conclusion changes.
