# Readback correction for R7-02 D0059 report

This artifact corrects a **typographical escape/rendering loss only** in the immutable report

`research7_2026-09-17/R7-02/runs/2026-09-17/2026-09-17T162022Z__report.md`

created at commit `0362a88ff719c6e6d4b1244d2554a9b8f5f9cf2b`.

Exact-SHA readback showed that equation (5.1) lost the leading `\f` in `\frac` during transport. The intended equation is

\[
D_{N+1}-D_N=\frac{((N+1)\varepsilon_{N+1}-c)^2}{N+1}\ge0.
\]

This is exactly the increment of the already-defined quantity

\[
D_N=\sum_{n=1}^N\frac{(n\varepsilon_n-c)^2}{n}.
\]

No theorem, hypothesis, metric, status, method outcome, or subsequent argument is changed. The original report remains immutable; this artifact is the authoritative readback correction for that one typographical token.