# Round 485 explicit phase formula for \(\Lambda_q\)

Round 485 solves the singularity comparison in Round 484.

Write
\[
  s=\sqrt q,\qquad y=\Lambda_q^2=t_q^{-1}.
\]
The two elementary singularities of \(F_q\) are
\[
  t=\frac1q,\qquad t=\frac1{4\sqrt q},
\]
corresponding to \(y=q=s^2\) and \(y=4s\).  The branch singularity gives the
rate
\[
  2q^{1/4}=2s^{1/2}.
\]

The possible interior singularity satisfies
\[
  \frac{tA(st)}{1-s^2t}=1,
  \qquad
  A(x)=\frac{1-\sqrt{1-4x}}{2x}.
\]
In terms of \(y=1/t\), this is
\[
  \frac{1-\sqrt{1-4s/y}}{2s}=1-\frac{s^2}{y}.
\]
Squaring gives
\[
  (s-1)y^2+(-2s^3+s^2+1)y+s^5=0.
\]
The valid root is the smaller one, because it is the one for which the
unsquared right-hand side is nonnegative:
\[
  y_-(s)=
  \frac{
    2s^3-s^2-1
    -
    \sqrt{(2s^3-s^2-1)^2-4(s-1)s^5}
  }{2(s-1)}.
\]

The interior root appears before the elementary branch singularity exactly
when
\[
  \frac{tA(st)}{1-s^2t}\bigg|_{t=1/(4s)}\ge1,
\]
that is
\[
  \frac{2}{4s-s^2}\ge1.
\]
For \(s\ge1\), this is equivalent to
\[
  s\ge 2+\sqrt2,
  \qquad
  q\ge 6+4\sqrt2.
\]

Therefore the optimized repeated-bubble rate is
\[
  \Lambda_q=
  \begin{cases}
    2q^{1/4},
      & q<6+4\sqrt2,\\[4pt]
    \sqrt{y_-(\sqrt q)},
      & q\ge 6+4\sqrt2.
  \end{cases}
\]
For integer \(q=d-1\), the transition starts at \(q=12\).

As \(q\to\infty\),
\[
  \Lambda_q=\sqrt q+O(q^{-1/2}),
\]
so this corrected repeated-bubble family still falls short of the global
product-shuffle scale \(\sqrt q+1\).  It nevertheless improves the explicit
paid-exit subbound \(\sqrt{q+1}\) for all integer \(q\ge12\).
