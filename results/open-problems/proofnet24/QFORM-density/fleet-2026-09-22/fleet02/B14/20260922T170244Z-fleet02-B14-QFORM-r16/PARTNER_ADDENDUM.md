# fleet02/B14 r16 — newer partner addendum

A newer completed assigned-partner result became visible after the immutable main report was written: fleet03/B14 run `20260922T170256Z-fleet03-B14-QFORM-r14`, canonical report `yspennstate/math-open-problems@2ff9848af396e557949eef94059b756eaad74f17`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260922T170256Z-fleet03-B14-QFORM-r14/REPORT.md`.

Its theorem exactly localizes arbitrary nonnegative measurable payoffs, including unbounded singular kernels, from all cap-one product laws to compact finite-fragment indicator products. In particular for every symmetric `B`, affine vector `c`, and `alpha>0`,

\[
\sup_{\mu\in D_m}\sup_t E_\mu |Y^TBY+c^TY-t|^{-\alpha}
=
\sup_{\mu\in F_m}\sup_t E_\mu |Y^TBY+c^TY-t|^{-\alpha}.
\]

It also proves the exact translation quotient: this worst-case constant is invariant under `c -> c+2Bs`, so it depends only on `P_{ker B}c`.

This strengthens, rather than supersedes, the r16 mass-linear compiler. The partner theorem removes the **first localization step** for the half-Riesz kernel without any TV/unbounded-payoff gap. The r16 compiler controls any **further positive decomposition** of a finite-fragment extreme law: local contributions must still be linear in their unnormalized piece mass, or their weighted average must be bounded before normalization. The r16 normalize-then-cap, distant-shift, and no-moment barriers therefore remain operative downstream.

Applied to the scalar-Schur bridge

\[
Q(x,y)=a x^2+2x u^Ty+d_0x+y^TBy+d^Ty+c,
\]

the partner theorem gives

\[
p_Q(t)\le |a|^{-1/2} E|t-S(Y)|^{-1/2}
\]

and says the worst-case half-Riesz constant of the Schur remainder may be proved only on compact finite-fragment product indicators, with no localization loss. Its range-affine component can be translated away; only the kernel-affine component is essential.

Thus the sharpened first unpaid implication for B14 is:

> Prove a dimension-free half-Riesz bound for the relevant higher-rank Schur remainder, with arbitrary kernel-affine component, on compact finite-fragment product indicators, while preserving the unnormalized-mass interface under any further slicing. Equivalently, find a product-preserving structural reduction to an already completed rank-two/grouped family. No support, moment, fragment-count, or range-affine translation payment is allowed or needed.

The full QFORM conjecture remains open. This addendum records actual application of the newest completed assigned-partner theorem; it makes no claim of full closure.
