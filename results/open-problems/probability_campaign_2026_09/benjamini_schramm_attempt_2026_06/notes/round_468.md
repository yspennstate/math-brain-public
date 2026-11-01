# Round 468 exact two-port transfer in \(T_d\square K_2\)

Round 468 computes the two-port transfer from Round 467.

Let \(S(z)\) be the branch-switch generating function from Round 466 inside
a descendant cone:
\[
  S(z)=\frac{z}{1-qz^2},
  \qquad q=d-1.
\]
It counts self-avoiding paths from \((v,0)\) to \((v,1)\) inside the
descendant cone of \(v\), avoiding the parent of \(v\).

For a component \(C_t\), let \(F(z)\) count full boundary-to-boundary
self-avoiding exterior returns from the port \(A_t=(t,0)\) to the port
\(B_t=(\operatorname{par}(t),1)\), or in the reverse direction.  There are
only two possibilities.

1. Direct transfer through \((t,1)\):
   \[
     A_t\to (t,1)\to B_t,
   \]
   contributing \(z^2\).
2. Choose one of the \(q\) child cones \(c\) of \(t\), enter it in one layer,
   switch layers inside that cone, and return through \((t,1)\).  This
   contributes
   \[
     q z^3 S(z).
   \]

Thus
\[
  F(z)=z^2+qz^3S(z)
      =z^2+\frac{qz^4}{1-qz^2}.
\]
The radius of convergence is \(q^{-1/2}\), so the coefficient growth is
\[
  [z^n]F(z)=O(q^{n/2})
\]
and the lower-bound family from Round 462 attains this exponent.

There are no other nontrivial port transfers in a component.  A transfer from
\(A_t\) back to \(A_t\), or from \(B_t\) back to \(B_t\), would force the
self-avoiding path to revisit the same boundary port; in the annular return
setting these diagonal same-port terms are irrelevant and contribute only
bounded degenerate cases if allowed by convention.

Therefore the exponential growth of all nondegenerate two-port exterior
returns in \(T_d\square K_2\) is exactly
\[
  \sqrt q=\sqrt{d-1}.
\]
