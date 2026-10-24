Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# Immutable erratum for the C0032 Gevrey/holonomicity artifact

Applies to:

`research7_2026-09-17/R7-06/artifacts/2026-09-19/2026-09-19T005723Z__C0032_gevery_holonomic_certified_inversion.md`

Creation commit of that artifact: `956e30c76930a6a42cb62279f60f290fe7bc460b`.

Exact-SHA readback found one Markdown/TeX escape typo in the proof of Theorem 2.1.  The finite geometric identity should read

\[
\frac{1}{1+x}
=\sum_{n=0}^{N}(-x)^n+\frac{(-x)^{N+1}}{1+x}.
\]

The original immutable artifact rendered the second `\frac` incorrectly as `\nrac` because of an escaping error.  Equations (2.1), (2.2), and (2.3) themselves are correctly written, and every subsequent derivation uses the intended finite geometric identity.  This erratum changes no theorem, bound, metric, status, or conclusion.