SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B15, 2026-09-22T21:14:30Z.

# account04/B15 — exact Gaussian heat-height closure

**Status:** ESSENTIAL_STEP_APPLIED / EXACT_POSITIVE_REGULARIZATION_NORMAL_FORM. Universal QFORM height remains OPEN. Execution is WITHOUT_VERIFIED_BRAIN.

Canonical report: `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`

Report blob: `522bccfa11f45d3f378fd3e28d311a27e2953de9`.

For every probability law \(\mu\), with
\[
\gamma_\varepsilon(u)=\frac{e^{-u^2/(2\varepsilon^2)}}{\sqrt{2\pi}\varepsilon},
\]
I proved
\[
\boxed{\sup_{\varepsilon>0,y}(\mu*\gamma_\varepsilon)(y)=\|p_\mu\|_\infty,}
\]
with value \(+\infty\) if no bounded density exists. The heat maxima are monotone as \(\varepsilon\downarrow0\). If \(p_\mu\in C_0\), Gaussian smoothing converges uniformly and these maxima increase to \(\max p_\mu\).

The damped Fourier identity is absolutely convergent without an absolute-Wiener premise:
\[
(\mu*\gamma_\varepsilon)(y)=\frac1{2\pi}\int e^{-ity}\widehat\mu(t)e^{-\varepsilon^2t^2/2}\,dt.
\]
Also \(\Pr(|Q-y|\le r)\le\sqrt{2\pi e}\,r\,\mathbb E\gamma_r(Q-y)\).

Applying completed partner account01/B15 r13
(`math-open-problems@1b7a876f7577cf99599322926154ce0032a034fd`) gives the zero-loss target identity
\[
\boxed{
C_{\rm full}=
\sup_{\substack{s_3(A)=1\\f_i>0\ {\rm analytic\ Schwartz}\\\|f_i\|_\infty\le1}}
\sup_{\varepsilon>0,y}\mathbb E\gamma_\varepsilon(X^TAX-y).
}
\]
The completed account02/B15 theorem
(`math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`) already proves every fixed rank-\(\ge3\) output has a matrix-dependent bounded \(C_0\) density. Thus absolute continuity and continuity are qualitatively closed; the universal height alone remains open.

First unpaid implication: uniformly bound the displayed positive heat functional without rotating independence, assuming pointwise undamped Fourier decay, or extracting one reciprocal tiny minor.

Fresh control remained revision 2026-09-22.15. No scheduler, email, notification, permission, public-release, or task setting was changed.
