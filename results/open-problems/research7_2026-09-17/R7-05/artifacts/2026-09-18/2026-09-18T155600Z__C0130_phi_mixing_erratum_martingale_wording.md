Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# Erratum / clarification — Gordin martingale wording

Target: `C0130`.

Corrected artifact: `research7_2026-09-17/R7-05/artifacts/2026-09-18/2026-09-18T154900Z__C0130_truncation_phi_mixing_functional_resolvent.md`, creation commit `924633fbbf3c73aaca56240a3f25903475bfc6e0`.

Exact-SHA readback exposed one wording slip in Section 3.2. After

\[
D_{j+1}=G_{j+1}-E[G_{j+1}\mid\mathcal G_j],
\]

the sentence

> `(D_{j+1},G_{j+1})` is a bounded martingale-difference sequence

should read:

> **`(D_{j+1})` is a bounded martingale-difference sequence, while `(G_j)` is the bounded adapted coboundary process.**

The displayed identity

\[
Y_j=G_j-G_{j+1}+D_{j+1}
\]

is already correct. No theorem, estimate, hypothesis, metric value, or subsequent derivation changes.