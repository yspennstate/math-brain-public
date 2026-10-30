# Controlling correction to REPORT.md

The theorem and numerical constant are unchanged. In Section 2, immediately after (2.10), one monotonicity sentence has the inequality direction for an auxiliary symbol `A` written poorly. The correct argument is:

In the `theta>=1` branch,

`B_sq = 2 D^(-1/2) [2 + log(4 sqrt(2D/(kappa |h|)))]`.

Under `D>=1`, `kappa>=1`, `|h|>=1/26`, this is bounded above by

`2 D^(-1/2) [2 + log(4 sqrt(52D))]`.

Writing `x=sqrt(D)>=1` and

`A0 = 2 + log(4 sqrt(52)) > 1`,

this upper envelope is `2(A0+log x)/x`, whose derivative is

`2[1-A0-log x]/x^2 < 0`.

Hence its maximum is at `D=1`, giving

`4 + 2 log(4 sqrt(2)) + log 26 = 10.723832440821...`.

So (2.10), the hybrid theorem `<10.735`, and all later conclusions remain valid. This file controls the affected explanatory sentence in REPORT.md; the immutable report itself is not rewritten.
