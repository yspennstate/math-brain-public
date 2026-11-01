# Independent audit of the sharp count-gap certificate

12 October 2026. Read-only algebra review for the extension project.

**Result: PASS.** The quotient, finite boundary treatment, error bounds, and claimed equivalent are valid. The last transfer to the polymer gap uses the separately audited equality gamma_M = gamma_Q.

Let
\[
(Ah)(k)=\beta(n-k-1)[h(k+1)-h(k)]
+\frac{k(k-1)}n[h(k-1)-h(k)]
-\left(\beta+\frac{2k}n\right)h(k),
\quad 1\le k\le n-1.
\]
Take
\[
h(k)=\frac1{(k+a)(k+a+1)},\qquad
a(a-1)=\beta n(n+a+1),\quad a>1.
\]
The adjacent ratios are
\[
\frac{h(k+1)}{h(k)}=1-\frac2{k+a+2},
\qquad
\frac{h(k-1)}{h(k)}=1+\frac2{k+a-1}.
\]
Direct substitution and separate simplification of birth and death terms give
\[
-\frac{Ah(k)}{h(k)}
=\left(\frac{2a}n-\beta\right)
+\frac{2\beta(n+a+1)}{k+a+2}
-\frac{2a(a-1)}{n(k+a-1)}.
\]
The root relation therefore yields exactly
\[
-\frac{Ah(k)}{h(k)}
=c-\frac{6a(a-1)}{n(k+a-1)(k+a+2)},
\qquad c=\frac{2a}n-\beta.
\]
The remainder is positive and at most
\[
\frac6n\frac{a-1}{a+3}<\frac6n,
\]
since its denominator is minimized at k=1. Positive-vector comparison gives
\[
c-\frac6n\le\gamma_Q\le c.
\]
The k=1 and k=n-1 endpoint terms with out-of-domain indices have zero coefficients. The same algebra is valid for n=2, when only k=1 remains.

Solving the quadratic for a gives
\[
a=\frac{\beta n+1+\sqrt{(\beta n+1)^2+4\beta n(n+1)}}2,
\quad
c=\frac1n+\sqrt{\beta^2+4\beta+\frac{6\beta}n+\frac1{n^2}}.
\]
Put d = sqrt(beta^2+4 beta). Then
\[
d+\frac1n\le c\le d+\frac4n.
\]
For the upper inequality, squaring the nonnegative sides reduces it to
6 beta/n + 1/n^2 <= 6d/n + 9/n^2, which follows from d >= beta.
Thus
\[
d-\frac5n\le\gamma_Q\le d+\frac4n.
\]
Since d >= 2 sqrt(beta), an error bounded by 5/n is o(d) whenever
n sqrt(beta) tends to infinity, with beta permitted to vary.
Consequently gamma_M ~ sqrt(beta^2+4 beta) under that condition, after using the established exact gap equality.

This audit is an algebra certificate. It makes no independent claim of literature priority.
