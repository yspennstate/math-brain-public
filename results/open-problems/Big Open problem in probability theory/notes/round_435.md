# Round 435 annular-return kernel target

Round 435 reformulates the spread-return problem in terms of annular return
kernels, which are the natural objects behind exterior-return intervals.

For a root \(x\) and level \(u\ge1\), define the annular exterior-return
relation
\[
  \mathcal A_u^x(a,b)
\]
for \(a,b\in S_{u-1}(x)\) to mean that there is an open path from \(a\) to
\(b\) whose first and last edges go to \(S_u(x)\) and whose internal vertices
stay outside \(B_{u-1}(x)\).  Equivalently, it is the percolation analogue of
an exterior-return witness through level \(u\).  The corresponding two-point
annular kernel is
\[
  R_{p,u}^x(a,b)
  =
  \mathbf P_p(\mathcal A_u^x(a,b)).
\]

A time-disjoint family of exterior-return intervals through levels
\(u_1,\ldots,u_m\) in a single open self-avoiding witness yields disjoint
occurrences of the annular events \(\mathcal A_{u_i}^x(a_i,b_i)\), after
recording the boundary endpoints \(a_i,b_i\).  Thus a BK/Reimer step should
bound the probability of such a family by a sum of products
\[
  \prod_{i=1}^m R_{p,u_i}^x(a_i,b_i),
\]
with additional endpoint-routing factors outside the intervals.

This changes the target from counting all self-avoiding annular corridors to
bounding annular return probabilities.  A usable fixed-density spread-return
estimate would follow from an averaged annular-return bound of the schematic
form
\[
  \sup_{x,u}
  \frac{1}{|S_{u-1}(x)|}
  \sum_{a,b\in S_{u-1}(x)} R_{p,u}^x(a,b)
  \le \rho_{\rm ann}<1
\]
uniformly in the relevant near-critical window, or from a weaker bound whose
product beats the entropy term from Round 427.

This is still not proved.  It is, however, the right kind of statement:
nonamenability can plausibly enter through escape from annuli or boundary
expansion, while the deterministic radial corridor from Round 434 shows that
pure SAW geometry cannot supply the required cost by itself.

The next mathematical task is to compare \(R_{p,u}^x\) with existing
two-point kernels:

* a crude upper bound is \(R_{p,u}^x(a,b)\le \tau_p(a,b)\);
* a useful bound needs the killed kernel outside \(B_{u-1}(x)\);
* averaged annular-return decay would follow if boundary-to-boundary
  susceptibility in the exterior component is uniformly subcritical.

This connects the spread-return obstruction back to the finite-set escape
program: repeated annular returns are precisely failures of mass to escape
from nested finite balls.
