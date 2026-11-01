# Round 030 log

## Goal

Test whether two lower-bound directions can improve enough to compete with the
current decorated-strip bound for \(T_3\square\mathbb Z\):

- larger side-depth decorated strips;
- larger caps in the finite-type interval branching process.

## Decorated-strip float scan

Added `scripts/decorated_strip_float_scan.py`, a floating-point companion to
the exact decorated-strip certificate.  It uses the same row-frontier
connectivity state as `scripts/decorated_strip_bound.py`, but accumulates
probabilities directly at a fixed \(p\).  This is not a certificate; it is a
screening tool for larger strips.

Validation:

\[
  h=3,\quad\text{side-depth}=2,\quad p=0.3:
  \qquad \rho_{\rm lower}=0.426310751826,
\]
matching the exact transfer.

The larger tested case
\[
  h=6,\quad\text{side-depth}=2,\quad p=0.3
\]
gave
\[
  \rho_{\rm lower}=0.488883555861.
\]
Thus side-depth \(2\) is still not competitive at this window size.

## Fast interval scan

Added `scripts/interval_branching_fast_scan.py`, a floating-point diagnostic
for the same interval process used by `scripts/interval_branching_bound.py`.
Instead of enumerating all horizontal seed masks and vertical edge masks, it
scans open vertical components.  For each component it records its length and
the number of parent-interval sites it contains; when the component closes, it
is seeded with probability \(1-(1-p)^k\).  This computes the same transition
law in floating point.

Validation against the exact script:

\[
  M=6,\ p=0.305:\quad \rho_{\rm lower}=1.00719363799,
\]
\[
  M=7,\ p=0.3:\quad \rho_{\rm lower}=0.987013803082.
\]

These match the exact enumerator values.

## Larger-cap thresholds

The floating threshold where the cap-\(M\) mean matrix first has spectral
radius \(1\) is:

\[
\begin{array}{c|c}
M & p_M \\
\hline
6 & 0.303335949245\\
7 & 0.302987507205\\
8 & 0.302876735094\\
10 & 0.302831341492\\
12 & 0.302827045924
\end{array}
\]

The improvement has essentially saturated near \(0.302827\).  This is far
above the current finite-length SAW threshold
\[
  1/\|C_{15}\|_{2\to2}^{1/15}=0.274159516989.
\]

## Consequence

The capped interval-branching family, at least in this one-interval form, is
not a viable route to closing the \(T_3\square\mathbb Z\) case.  Future
percolation-side attempts need to retain substantially more geometry than a
single contiguous interval in each reached fiber, or else switch to a direct
\(p_{2\to2}\) estimate.
