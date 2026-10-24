# Round 040 log

## Goal

Check whether Yamamoto's fixed-direction exponent machinery gives a direct
\(p_{2\to2}\) bound for \(T_d\Box\mathbb Z\), rather than only numerical
\(p_c\)-upper bounds.

## Observation

Let \(b=d-1\).  Yamamoto proves that for \(p<p_u\),
\[
  I_n(p)=\sum_{k\in\mathbb Z}
  \mathbb P_p\bigl((o,0)\leftrightarrow (x_n,k)\bigr)
\]
is finite, submultiplicative in \(n\), and satisfies
\[
  \lim_{n\to\infty} I_n(p)^{1/n}=\alpha(p),
\]
where \(\alpha(p)\) is the fixed-direction exponent.  Yamamoto also uses
Schonmann's theorem and strict monotonicity of \(\alpha\) to get
\[
  \alpha(p)<b^{-1/2},\qquad p<p_u.
\]
Therefore for every \(p<p_u\) there is \(\theta<b^{-1/2}\) and a constant
\(C\) such that
\[
  I_n(p)\le C\theta^n.
\]

## Consequence for the two-point operator

Write the two-point kernel on \(T_d\Box\mathbb Z\) as
\[
  T_p=\sum_{n\ge0}\sum_{k\in\mathbb Z}
  a_{n,k}(p) R_n\otimes S^k,
\]
where \(R_n\) is the tree sphere kernel and \(a_{n,k}(p)\) is the connection
probability to a fixed tree vertex at distance \(n\) and height \(k\).  Since
\[
  \sum_k a_{n,k}(p)=I_n(p),
\]
and
\[
  \|R_n\|_{2\to2}\le C_d(n+1)b^{n/2},
\]
we get
\[
  \|T_p\|_{2\to2}
  \le
  C'\sum_{n\ge0}(n+1)(\theta\sqrt b)^n
  <\infty.
\]
Thus \(T_p\) is bounded on \(\ell^2\) for every \(p<p_u\).

Since the general inequality gives \(p_{2\to2}\le p_u\), this proves
\[
  p_{2\to2}(T_d\Box\mathbb Z)=p_u(T_d\Box\mathbb Z).
\]

## Line-factor conclusion

Hutchcroft's non-uniqueness theorem applies to \(T_d\Box\mathbb Z\) for
\(d\ge3\), giving \(p_c<p_u\).  Combining this with the equality above gives
\[
  p_c(T_d\Box\mathbb Z)<p_{2\to2}(T_d\Box\mathbb Z),
  \qquad d\ge3.
\]

This closes the \(T_3\Box\mathbb Z\) line-factor bottleneck directly.  The
finite-length SAW and decorated-strip computations remain useful diagnostics,
but they are no longer needed for the line-factor theorem.
