Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated completed-run model/reasoning telemetry is unavailable, so I do not claim otherwise.**

# Notation-only correction to the finite-K square-root escape report

This file corrects one typographical symbol in the immutable substantive report
`probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T1027+0300__finite_K_square_root_escape.md`, creation commit `f2d9525692614c3b593d3390f644e72c56829d29`, readback blob `37c7f6034c26e11d162fea6850854d9d8e09d3e8`.

In equation (3.2), the first density coefficient is the **Latin letter** `u`, not the Newton-decrement symbol `nu`. The corrected equation is

\[
\boxed{
u={2\lambda\beta\over1+\beta^2},
\qquad
v={\lambda\beta^2\over1+\beta^2}.}
\]

In plain text, the left-hand symbol in the first formula above is `u` (Unicode/ASCII Latin u). Some TeX renderers visually interpret the source sequence `\nu` as Greek nu; the intended source formula is therefore, unambiguously,

`u = 2 lambda beta / (1 + beta^2)`.

All subsequent statements `u,v=O(sqrt(rho))` and the mathematical proof use this Latin density coefficient. No theorem, bound, probability estimate, or conclusion changes.