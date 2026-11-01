# Readback addendum — notation-only correction and exact checks

Canonical report: `REPORT.md`, commit `1cf28b1faa4ca92850b551bd1cc23457164639d6`.

Readback found one notation-only typo in displayed equation (4.5): the exponent was missing a closing delimiter. The intended and mathematically used inequality is

\[
\mathbb E|Q-Q'|^{-1/2}
\le \frac{16}{3}2^{-1/8}(|\sigma|m)^{-1/4}
=4.890688230424913\ldots (|\sigma|m)^{-1/4}.
\]

No hypothesis, proof step, constant, status, or conclusion changes. The other exact outer constants in the report are

\[
\frac{16}{3}2^{3/8}\sqrt\pi=12.25913740078814\ldots,
\quad 2^{7/4}=3.363585661014858\ldots,
\quad 2^{11/4}=6.727171322029716\ldots.
\]

For the target-valid obstruction family `Q_eta=(X+eta W)^2+2UV`, the square block has eigenvalues `1+eta^2,0` and the hyperbolic block has eigenvalues `+1,-1`, so the full spectrum is exactly `{1+eta^2,1,-1,0}`. The pinned one-coordinate completion receiver remains uniform: `||p_{Q_eta}||_infinity<=7` for all `0<eta<=1` and every independent cap-one input law.