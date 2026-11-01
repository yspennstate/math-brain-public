# Round 021 log

Date: 2026-06-08

## Focus

Tested a stronger oriented percolation comparison for the remaining
\(T_3\square\mathbb Z\) line-factor case.  Instead of keeping only one vertical
cluster after a tree move, the comparison keeps all open horizontal seed
heights from a retained parent interval and expands their union in the child
line.

## Finite-type interval process

Fix a cap \(M\).  Type \(m\in\{1,\ldots,M\}\) means that a reached fiber
contains a contiguous reachable interval of length \(m\), with type \(M\)
meaning length at least \(M\).  From a type-\(m\) parent interval, a child fiber
receives independent open horizontal seeds from the \(m\) sites; those seeds
are then expanded through independent one-dimensional vertical percolation.
The retained child type is the capped length of the longest contiguous reached
interval.

For \(T_3\square\mathbb Z\), each parent has two forward child fibers, so the
finite-type mean matrix is
\[
  A^{(M)}_{m\ell}(p)=2P^{(M)}_{m\ell}(p).
\]
If \(\rho(A^{(M)}(p))>1\), the finite-type Galton-Watson lower process survives
with positive probability, giving \(p\ge p_c(T_3\square\mathbb Z)\), and strict
supercriticality at \(p\) gives \(p_c<p\).

## Exact certificate

For \(M=6\) and \(p=61/200\), exact enumeration gives the certificate
\[
  v=(6271,11456,15785,19374,22333,24781)
\]
with
\[
  \min_m\frac{(A^{(6)}(p)v)_m}{v_m}>1.00714.
\]
Therefore
\[
  p_c(T_3\square\mathbb Z)<61/200.
\]

The exact computation only needs a finite vertical window
\([-(M-1),m-1+(M-1)]\) for a parent interval of length \(m\), since reaching the
window boundary already certifies capped type \(M\).  The computation is now in
`scripts/interval_branching_bound.py`.

## Interpretation

This improves the \(p_c\)-upper side for \(T_3\square\mathbb Z\), but it still
does not close the SAW operator gap.  Combining this with the SAW criterion
would require
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<200/61\approx3.27869,
\]
while the best current finite-length certificate is \(3.657847\).  The next
useful direction is either a structural self-avoidance bound below \(200/61\),
or a non-oriented percolation comparison that lowers the \(p_c\) upper bound
well below the interval-branching threshold.

## Full-state diagnostic

I also simulated the full oriented fiber process, where the state is the entire
finite reachable set of heights in a fiber rather than one retained interval.
The estimated mean generation growth factors were:

- \(p=0.285\): about \(0.958\).
- \(p=0.290\): about \(0.980\).
- \(p=0.295\): about \(1.002\).
- \(p=0.300\): about \(1.025\).
- \(p=0.305\): about \(1.043\).

This suggests that better finite-state truncations of the same oriented
mechanism may push the certified upper bound from \(0.305\) toward roughly
\(0.295\), but probably not toward the \(0.273\) range needed for the current
finite-length SAW bound.  The next serious percolation-side attempt should
therefore use a non-oriented comparison or a second-moment/path-counting
argument rather than just preserving more seed intervals in the same forward
branching process.
