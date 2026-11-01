# Round 106 log

## Goal

Connect annular operator control to pointwise two-point decay and spherical
operator growth.

## Result

Added `lem:pointwise-annular-operator-control` and
`cor:pointwise-dyadic-annular`.

For every annulus \(I\),
\[
  \|T_p^I\|_{2\to2}
  \le
  \sum_{n\in I\cap\mathbb N}
    \tau_p^{\max}(n)\|S_n^G\|_{2\to2}.
\]

Thus, under the mean-field susceptibility assumption, the normalized dyadic
condition
\[
  \lim_{J\to\infty}\limsup_{p\uparrow p_c}
  \sum_{j\ge J}2^{\alpha(j-J)}
  \left(
    \frac{\sum_{2^j<n\le2^{j+1}}
      \tau_p^{\max}(n)\|S_n^G\|_{2\to2}}
    {\bar\chi_p}
  \right)^2=0
\]
implies \(p_c<p_{2\to2}\).

## Interpretation

This is a normalized, near-critical version of the older critical-shell
summability route.  It does not require proving \(T_{p_c}\) bounded outright;
it asks that each far dyadic annulus be small relative to the diverging
susceptibility, with a square-summable tail.
