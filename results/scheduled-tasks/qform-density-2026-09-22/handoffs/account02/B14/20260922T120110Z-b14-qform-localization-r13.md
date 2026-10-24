# account02/B14 handoff — tail-free compactification and bang-bang localization

Status: **TARGET-LEVEL REDUCTION PROVED / FULL QFORM TARGET OPEN**.

Canonical report: `yspennstate/math-open-problems@ea6b7ae2aba8b38748214a4d38f47fa6f790b8e0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T120110Z-b14-qform-localization-r13/REPORT.md`.

## Main result

For any measurable `T:R^n->R` (hence for `T(x)=x^T A x`), a density-domination theorem proved uniformly for compactly supported independent coordinate densities `0<=f_i<=1` extends to arbitrary supports with **the same constant**. Truncate without renormalizing, fill each missing tail mass by a disjoint compact indicator interval so the completed law remains an admissible probability density, dominate the truncated pushforward by the completed pushforward, and let the truncation grow. No moment or tail-rate input occurs.

The same completion has `L1` error at most `2 sum_i tau_i`; therefore any uniform compact-support bound `int |phi_Q(t)|dt<=K` passes to arbitrary supports by pointwise convergence plus Fatou, preserving `K` and hence the continuous-density bound `K/(2pi)`.

At the target small-ball level there is an exact coordinatewise bathtub reduction. For each fixed output interval, every compactly supported admissible product density is dominated by a product of indicator densities `1_{E_i}` with `|E_i|=1`. Approximating those sets in symmetric difference gives the exact equivalent geometric target:

`|{x in E_1 x ... x E_n : x^T A x in I}| <= C |I|`

for every target matrix `A`, every bounded interval `I`, and every `E_i` that is a finite union of bounded intervals of total length `1`.

Thus arbitrary tails, shifts, and disconnected fragments require no extra constant. What remains is uniformity in fragment count, diameter, location and separation. A bound growing in any of those parameters is insufficient.

Translation covariance is exact:

`(y+a)^T A (y+a)=y^T A y+2(Aa)^T y+a^T A a`.

Hence recentering must be uniform in the translation-generated linear term; the Hessian spectrum is unchanged.

## Applied peer result

Consumed the complete account03/B05 theorem at `yspennstate/math-open-problems@c828d2ee2f8acef5eb96892bc8a9a25594db0f51`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260922T113800Z-account03-B05-qform-r11/REPORT.md`. Its remaining weighted-Wiener problem may now be attacked on compactly supported inputs only; unbounded support then transfers by the Fourier compactification above. The bang-bang reduction is **not** asserted for `int|phi|`, where the absolute value destroys multilinearity.

The assigned account03/B14 partner had no completed current-qform handoff visible when read; no stale artifact was substituted.

Mandatory pointwise-decay correction remains active: the phase-aligned counterexample already lies in the finite-union unit-measure class, so compact localization does not revive pointwise decay.

First remaining B14 implication: prove the geometric small-ball inequality above uniformly for finite-union unit-measure coordinate sets and general rotated indefinite `A` with three `|lambda|>=1`, or construct a genuine counterexample in that reduced class.
