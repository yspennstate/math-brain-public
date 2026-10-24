# Round 074 log

## Goal

Sharpen the finite cyclic examples from Round 073 using the nonbacktracking
operator bound.

## Finite regular factors

The nonbacktracking product theorem does not need the factor \(H\) to be
infinite; \(T_d\square H\) is infinite because of the tree factor.  I widened
the statement to finite or infinite connected \(\Delta\)-regular \(H\).

For finite connected \(\Delta\)-regular \(H\),
\[
  \|A_H\|_{2\to2}=\Delta,
\]
so the product criterion becomes
\[
  \beta(d+\Delta,2\sqrt{d-1}+\Delta)<d-1.
\]

## Improved cyclic thresholds

For \(T_d\square K_2\), \(\Delta=1\).  Writing \(b=d-1\), the check is
\[
  \beta(d+1,2\sqrt b+1)<b,
\]
which holds for \(b\ge4\), hence \(d\ge5\).

For \(T_d\square C_m\), \(m\ge3\), \(\Delta=2\), and
\[
  \beta(d+2,2\sqrt b+2)<b
\]
holds for \(b\ge6\), hence \(d\ge7\).

These improve the coarse adjacency-walk thresholds \(d\ge7\) and \(d\ge9\) from
Round 073.
