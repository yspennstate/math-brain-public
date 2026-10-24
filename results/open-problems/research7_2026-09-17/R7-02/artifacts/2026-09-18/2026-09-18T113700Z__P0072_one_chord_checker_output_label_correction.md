# P0072 one-chord checker — immutable output-label correction

The executed checker and all assertions in

`2026-09-18T113000Z__P0072_one_chord_exact_checker.py`

are unchanged and valid. The archived `.out` file ends `ALL_EXACT_CHECKS_PASS`.

One human-readable explanatory `print` line in that immutable output is missing the later multiplication by `n ~ (a0+a3)T`. It prints the leading coefficient of `T q_R/R` on the intersection chart,

\[
\frac{2a_0+3a_3}{(a_0+a_3)(a_0+2a_3)}
\frac{(A+1)(B+1)}{A+B+1},
\]

while the proof-relevant normalized quantity is `n q_R/R`, namely

\[
\boxed{
\frac{2a_0+3a_3}{a_0+2a_3}
\frac{(A+1)(B+1)}{A+B+1}\ge\frac32.
}
\]

This is exactly equation (4.9) in

`2026-09-18T113200Z__P0072_one_chord_extinction_theorem.md`.

The checker assertion itself verifies the pre-normalization leading expansion and does not assert the mistaken printed inequality. This addendum corrects only the explanatory label; no mathematical calculation, assertion, or theorem statement is changed.
