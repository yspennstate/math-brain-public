# Round 023 log

Date: 2026-06-08

## Focus

Looked for a non-oriented \(p_c\) comparison for the remaining
\(T_3\square\mathbb Z\) case.  The oriented interval process appears to have an
intrinsic threshold near \(0.295\), so I switched to Yamamoto's fixed-direction
characterization of \(p_c(T_d\square\mathbb Z)\).

## Decorated strip

Let \(x_n\) be a vertex at tree distance \(n\) from \(o\), and let
\[
  \alpha(p)
  =
  \lim_{n\to\infty}
  \mathbb P_p((o,0)\leftrightarrow(x_n,0))^{1/n}.
\]
Yamamoto's criterion implies that for \(T_3\square\mathbb Z\),
\(\alpha(p)>1/2\) gives \(p>p_c\).

I restricted the connection event to a finite decorated strip:

- the geodesic from \(o\) to \(x_n\);
- the seven heights \(\{-3,\ldots,3\}\);
- at each geodesic fiber, the one off-geodesic side fiber, also with those
  seven heights.

This is non-oriented: paths can leave the geodesic into the side fiber and
return at another height.  Integrating out one decorated column gives a transfer
matrix on the \(2^7-1=127\) non-empty subsets of the geodesic fiber.

## Exact certificate

At \(p=303/1000\), the decorated column has \(19\) edges.  Exact enumeration of
the \(2^{19}\) edge configurations and exact integer arithmetic verify a
positive integer vector \(v\in\mathbb Z^{127}\) with
\[
  \min_A \frac{2(M(p)v)_A}{v_A} > 1.00218.
\]
Thus \(\rho(M(p))>1/2\), so \(\alpha(303/1000)>1/2\).  Therefore
\[
  p_c(T_3\square\mathbb Z)<303/1000.
\]

The computation is reproducible with
`scripts/decorated_strip_bound.py --height-count 7 --p-num 303 --p-den 1000`.

## Interpretation

This improves the previous certified upper bound
\[
  p_c(T_3\square\mathbb Z)<61/200=0.305
\]
to \(0.303\).  It is still not enough for the current SAW operator criterion,
which now requires
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<1000/303\approx3.30033.
\]
The best finite-length certificate remains \(3.647512\).  The decorated-strip
method is nevertheless the first genuinely non-oriented \(p_c\) improvement in
this project, and larger height windows or deeper finite side branches are the
next \(p_c\)-side target.
