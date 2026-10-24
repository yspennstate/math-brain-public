Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# Erratum to the inverse-square opacity artifact

This immutable correction applies only to

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T153300Z__I0006_inverse_square_opacity_and_weibull_tilt.md`

at creation commit `35ebe742b7096f34f9498a1666944782a0dce939`.

In displayed equation (3.13), a Markdown/escape transcription dropped the leading `\f` of `\frac`. The intended and mathematically used inequality is

\[
p\left[
B-\frac{A}{2C_5}\log(1+R^2)
\right]\le0.
\tag{E.1}
\]

This follows directly by substituting Corollary 3.2,

\[
\mathbb E_0\sum_{j<\tau}w(X_j)
\ge
\frac{p}{2C_5}\log(1+R^2),
\]

into (3.12). No theorem, constant, later formula, or conclusion changes. The original artifact remains immutable; this file is the authoritative correction for equation (3.13).