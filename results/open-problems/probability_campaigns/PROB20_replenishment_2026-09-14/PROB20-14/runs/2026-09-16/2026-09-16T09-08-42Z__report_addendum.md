# PROB20-14 report addendum — transport correction

Exact-commit readback of `2026-09-16T09-08-40Z__report.md` found a UTF-8/escaping transport typo in equations (5.3) and (5.4): the intended LaTeX token for the coefficient one half was rendered as the fragment `rac12` in those two displays.

There is **no mathematical change**. The intended equations are, in transport-safe notation,

\[
x_n+(1/2)\log V(\rho_n)
\le \lambda_n-(1/2)\log n+C.
\tag{5.3 corrected}
\]

and

\[
x_n+(1/2)\log
V\!\left(\sqrt{n/(x_n+B\log n)}\right)
\le \lambda_n-(1/2)\log n+C.
\tag{5.4 corrected}
\]

All surrounding derivations, the adaptive-radius theorem, the Kesten-reference likelihood ratio, the entropy/local-cost identity, and the weighted-Scheffe reduction are unchanged. This append-only addendum supersedes only the corrupted typography in those two displays; the original report is not overwritten.