# Round 016 log

Date: 2026-06-08

## Focus

Improved the line-factor theorem from \(d\ge7\) to \(d\ge5\) by combining the
nonbacktracking SAW bound with a sharper upper bound on
\(p_c(T_d\square\mathbb Z)\).

## Vertical-cluster branching bound

Root \(T_d\), orient away from the root, and keep \(q=d-1\) forward children.
At a visited tree vertex, expose the entire open cluster in its vertical
\(\mathbb Z\)-fiber.  If this cluster has size \(M\), a fixed forward child
fiber is reached with probability
\[
  1-(1-p)^M.
\]
The forward fibers are disjoint, so this gives a Galton-Watson comparison with
mean offspring
\[
  q\psi(p),\qquad
  \psi(p)=\mathbb E[1-(1-p)^M].
\]

For one-dimensional bond percolation,
\[
  \mathbb P(M=m)=m(1-p)^2p^{m-1},\qquad m\ge1,
\]
and
\[
  \mathbb E[t^M]=\frac{t(1-p)^2}{(1-pt)^2}.
\]
Hence
\[
  \psi(p)
  =
  1-\frac{(1-p)^3}{(1-p+p^2)^2}
  =
  \frac{p(p^3-p^2+1)}{(p^2-p+1)^2}.
\]
If \(q\psi(p)>1\), then \(p\) is supercritical for
\(T_d\square\mathbb Z\).

## Combination with nonbacktracking

For \(s=\sqrt{d-1}\), the nonbacktracking SAW exponent bound for
\(T_d\square\mathbb Z\) is
\[
  t=s+1+\sqrt{2s-1}.
\]
It is enough to prove \((d-1)\psi(1/t)>1\), since then
\[
  p_c(T_d\square\mathbb Z)<1/t
  \le 1/\gamma_{\rm SAW,2}(T_d\square\mathbb Z).
\]

Writing \(r=\sqrt{2s-1}\), direct reduction using \(r^2=2s-1\) gives
\[
  s^2\psi(1/t)-1
  =
  \frac{
    s(3s^3+4s^2-13s-6)r
    +(s+1)(s^4+7s^3-16s^2+s+1)
  }
  {(r^2+2rs+r+s^2+s+1)^2}.
\]
For \(s\ge2\), put \(u=s-2\).  Then
\[
  s(3s^3+4s^2-13s-6)
  =
  (u+2)(3u^3+22u^2+39u+8)>0
\]
and
\[
  (s+1)(s^4+7s^3-16s^2+s+1)
  =
  (u+3)(u^4+15u^3+50u^2+53u+11)>0.
\]
Thus the criterion holds for every \(s\ge2\), i.e. every \(d\ge5\).

## Status

The manuscript now proves
\[
  p_c(T_d\square\mathbb Z)<p_{2\to2}(T_d\square\mathbb Z)
  \qquad d\ge5.
\]
The cases \(T_3\square\mathbb Z\) and \(T_4\square\mathbb Z\) remain outside
the current SAW-plus-branching method.
