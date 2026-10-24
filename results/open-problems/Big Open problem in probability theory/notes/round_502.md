# Round 502 explicit fresh-block excess multiplier

Round 500 used the fresh-column block inequality \(B_q(z,w)<1\).  The
optimizing multiplier can be computed explicitly, which clarifies the sign
of the excess weight.

Put \(s=\sqrt q\) and
\[
  B_q(z,w)
  =
  szw\left(
    1+\frac{zw}{1-zw}+\frac{z/w}{1-z/w}
  \right).
\]
Let
\[
  a=zw,\qquad r=z^2.
\]
The domain is \(r<a<1\), and
\[
  B_q(z,w)
  =
  s\left(
    \frac{a}{1-a}
    +
    \frac{ar}{a-r}
  \right).
\]
Differentiating gives
\[
  \frac{1}{(1-a)^2}
  =
  \frac{r^2}{(a-r)^2},
\]
so the minimizer is
\[
  a_*(z)=\frac{2z^2}{1+z^2},
  \qquad
  w_*(z)=\frac{a_*(z)}{z}
  =
  \frac{2z}{1+z^2}.
\]
For \(0<z<1\), this satisfies \(z<w_*(z)<1\).  At the minimizer,
\[
  \min_w B_q(z,w)
  =
  \frac{4s z^2}{1-z^2}.
\]
Therefore
\[
  \min_w B_q(z,w)<1
  \quad\Longleftrightarrow\quad
  z<\frac{1}{\sqrt{1+4s}}.
\]

This exactly recovers the fresh-column threshold.  Since
\[
  M_q=\max\{s+1,\sqrt{1+4s}\},
\]
every \(z<M_q^{-1}\) lies below the fresh threshold, and \(w_*(z)\) is an
available calibrated choice.

Two consequences for the packet norm:

1. The useful excess multiplier is typically \(w<1\), so high excess is
   penalized in the norm rather than rewarded.
2. Passing a \(k\)-packet to a child cone shifts \(2k\) boundary ports one
   unit deeper and therefore contributes \(w_*^{2k}\), a favorable per-atom
   factor that can be combined with the packet fugacity \(\xi\).

Thus the fresh-column part of the closure problem is completely calibrated.
The remaining issue is not the choice of \(w\), but the interaction between
the pair-span kernel, the adjacent-gap gas, and recursive multi-packet
avoidance.
