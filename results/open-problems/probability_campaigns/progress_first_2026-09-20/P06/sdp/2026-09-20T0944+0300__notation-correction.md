Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated completed-run model/reasoning telemetry is unavailable, so I do not claim otherwise.**

# Notation correction to the 09:30 fixed-projector report

This is a notation-only correction to the immutable report

`probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T0930+0300__fixed_projector_second_finite_step.md`

created at commit `04add55e2718c83206ae6803afec365c84af3dae`.

In equations (4.5) and (4.7), the first square-mixture density coefficient was typeset as `\nu_n` / `\nu`. It must be read as **`u_n` / `u`**, consistently with equations (4.4), (4.6), (4.8), and the subsequent proof:

\[
u_n^{\mathrm{(intended\ label)}}\equiv u_n={2\lambda_n\beta_n\over1+\beta_n^2},
\qquad
v_n={\lambda_n\beta_n^2\over1+\beta_n^2},
\]

and, for `delta=1-beta`,

\[
u^{\mathrm{(intended\ label)}}\equiv u=2\delta+O(\delta^2),
\qquad
v=\delta+O(\delta^2).
\]

The corrected mathematical symbols are the plain Latin coefficient names `u_n` and `u`; the original leading backslash was a typesetting typo and is not the Newton decrement. No formula, bound, proof step, status, or conclusion changes.