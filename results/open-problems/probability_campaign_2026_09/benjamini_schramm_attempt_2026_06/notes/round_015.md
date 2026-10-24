# Round 015 log

Date: 2026-06-08

## Focus

Improved the regular amenable-factor product theorem by using the exact
nonbacktracking root condition instead of the cruder spectral-factor corollary.

## Improved statement

Let \(T_d\) be the \(d\)-regular tree, \(s=\sqrt{d-1}\), and let \(H\) be an
infinite connected amenable \(\Delta\)-regular graph.  Then
\[
  p_c(T_d\square H)<p_{2\to2}(T_d\square H)
\]
whenever
\[
  s\ge1+\sqrt\Delta.
\]

This supersedes the previous easy consequence \(s\ge2+\sqrt\Delta\).

## Algebra

Amenability and regularity give \(\|A_H\|_{2\to2}=\Delta\), so the
nonbacktracking product theorem asks for
\[
  \beta(d+\Delta,2s+\Delta)<s^2.
\]
Here \(D-1=s^2+\Delta\) and \(\rho=2s+\Delta\).  In the small-\(\rho\) branch,
the needed inequality is
\[
  \sqrt{s^2+\Delta}<s^2.
\]
Writing \(a=\sqrt\Delta\), this holds at \(s=1+a\) because
\[
  (1+a)^4-(1+a)^2-a^2
  =
  a(a^3+4a^2+4a+2)>0,
\]
and it remains true for larger \(s\).

In the larger-root branch, \(\beta(D,\rho)<s^2\) follows from
\[
  s^2>\rho/2
  \quad\text{and}\quad
  s^4-\rho s^2+(D-1)>0.
\]
At and above \(s=1+a\),
\[
  s^2-\rho/2
  =
  s^2-s-\Delta/2
  \ge
  a(a+2)/2>0,
\]
and
\[
  s^4-\rho s^2+(D-1)
  =
  s^2((s-1)^2-\Delta)+\Delta
  \ge
  \Delta>0.
\]

## Integer thresholds

The sufficient condition is
\[
  d\ge(1+\sqrt\Delta)^2+1.
\]
For example, it gives:

- \(\Delta=2\): \(d\ge7\), recovering the \(T_d\square\mathbb Z\) threshold.
- \(\Delta=3\): \(d\ge9\).
- \(\Delta=4\): \(d\ge10\).
- \(\Delta=10\): \(d\ge19\).

## Status

This is a genuine strengthening of the product part of Route A7 but still does
not reach the low-branching regimes such as \(T_3\square\mathbb Z\).  The next
useful target is a bound that exploits more of the self-avoidance constraint
than ordinary nonbacktracking.
