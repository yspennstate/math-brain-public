# Round 014 log

Date: 2026-06-08

## Focus

Audited the nonbacktracking product route and turned the spectral-factor
criterion into a regular amenable-factor corollary.

## Recurrence audit

For a \(D\)-regular graph \(X\), the nonbacktracking endpoint kernels satisfy
\[
  N_0=I,\qquad N_1=A_X,\qquad N_2=A_X^2-DI,
\]
and
\[
  N_n=A_XN_{n-1}-(D-1)N_{n-2}\qquad n\ge3.
\]
The counting reason is that \(A_XN_{n-1}\) prepends one edge to a
nonbacktracking path of length \(n-1\).  The bad prepended paths immediately
backtrack; after deleting that two-edge backtrack, each remaining
nonbacktracking tail of length \(n-2\) has \(D-1\) possible prepended
neighbours.

As a sanity check, a direct enumeration on \(C_4\), \(K_4\), and the cube
agreed with this recurrence for all lengths \(0\le n\le6\).

## Threshold audit

The \(H=\mathbb Z\) nonbacktracking condition was checked numerically:
\[
  \beta(d+2,2\sqrt{d-1}+2)<d-1
\]
fails for \(d=3,4,5,6\) and holds for \(d\ge7\) in the tested range.  This
matches the manuscript's \(d\ge7\) statement.

For the lattice threshold
\[
  \sqrt{d-1}\ge 2+\sqrt{2r},
\]
the direct quantity
\[
  F_r(s)=s^2-s-r-\sqrt{r(2s+r-2)}
\]
is positive at \(s=2+\sqrt{2r}\) in the tested cases \(r=1,2,3,5,10,25\),
matching the symbolic proof \(F_r(2+\sqrt{2r})=2+2\sqrt{2r}\).

## Amenable-factor corollary

If \(H\) is infinite, connected, amenable, and \(\Delta\)-regular, then
\[
  \|A_H\|_{2\to2}=\Delta.
\]
The upper bound is Schur's test.  The lower bound follows from Folner sets:
\[
  \frac{\langle\mathbf 1_F,A_H\mathbf 1_F\rangle}{|F|}
  =
  \Delta-\frac{|\partial_EF|}{|F|}.
\]
Therefore the spectral-factor corollary applies with \(\alpha=\Delta\), giving
\[
  p_c(T_d\square H)<p_{2\to2}(T_d\square H)
\]
whenever
\[
  \sqrt{d-1}\ge2+\sqrt\Delta.
\]

## Status

This round strengthens the manuscript's catalogue of verified Route A7 product
families.  It is still not a proof of the full Benjamini-Schramm conjecture:
the low-branching product regimes and the general nonamenable quasi-transitive
case remain open in this program.
