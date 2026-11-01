# PROB20-14 — analytic-form qualification for 2026-09-15T21:44:12Z report

**SOLUTION STATUS: PARTIAL (unchanged).**

Section 6 first states the additive-functional recursion
\[
A_f(z)=\frac{zF_f(T(z))}{1-z\phi'(T(z))},
\]
which is valid for the stated nonnegative tolls for which the series is defined.

The subsequent primitive representation
\[
A_f(z)=z^2\frac d{dz}H_f(T(z)),\qquad H_f'(t)=F_f(t)/t,
\]
should be read with the additional hypothesis `f(0)=0` (or more generally in a setting where a suitable primitive is defined). If `f(0) != 0`, the formal quotient `F_f(t)/t` has a `t^{-1}` term and the power-series primitive used there is not analytic at zero.

The only toll used for the new fractional-tail identity is
\[
f_K(d)=d^q\mathbf1_{\{d>K\}},
\]
which satisfies `f_K(0)=0`. Therefore equations (6.5), the random-initial-population reduction, Theorem 5.1, and every substantive conclusion of the report are unchanged. This addendum records the hypothesis explicitly rather than silently broadening the analytic identity.
