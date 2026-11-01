# Notation correction for REPORT.md

This immutable addendum corrects one notation collision in `REPORT.md`; it does **not** change any theorem, hypothesis, constant, or conclusion.

In the proof of Theorem 2.1, equations (2.8)--(2.10) use the standard entropy inequality

\[
h_2(t)\le t\log_2(\mathrm e/t),
\]

where `\mathrm e=2.71828...` is **Euler's number**. The report also denotes the support symmetric-difference error by the letter `e`. Accordingly, every occurrence of `e` inside `log_2(e/t)`, `log_2(2e/9)`, and the sentence `e<3` in that scalar entropy-envelope passage means Euler's number `\mathrm e`, not the support-error variable.

With unambiguous notation, the relevant line is

\[
H(S_Z)
<\frac92q\left(2r+\log_2\frac{2\mathrm e}{9}\right),
\]

and since `\mathrm e<3`,

\[
\frac{2\mathrm e}{9}<\frac23<2^{-1/2},
\]

so the logarithm is below `-1/2` exactly as used. All subsequent inequalities are unchanged.
